#!/usr/bin/env python3
"""Independent bounded verifier for EQ11-CUBE-CAYLEY/E_12.

This checker does not import or execute the claimant's enumerator.  It rebuilds the
matrix algebras directly from the two stated generators over F_3, reconstructs the
729 parameter categories, and checks every saved input/cube row and boundary.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import struct
from collections import deque
from pathlib import Path


P = 3
N = 7
POSITIONS = tuple((i, j) for i in range(N) for j in range(i + 1, N))
POSITION_INDEX = {pair: k for k, pair in enumerate(POSITIONS)}
POW3 = tuple(P ** k for k in range(len(POSITIONS)))
ZERO = (0,) * len(POSITIONS)
S = tuple(1 if j == i + 1 else 0 for i, j in POSITIONS)
CUBE_PATHS = tuple(
    (
        POSITION_INDEX[(i, ell)],
        POSITION_INDEX[(i, j)],
        POSITION_INDEX[(j, k)],
        POSITION_INDEX[(k, ell)],
    )
    for i in range(N)
    for j in range(i + 1, N)
    for k in range(j + 1, N)
    for ell in range(k + 1, N)
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def vector_code(vector: tuple[int, ...] | list[int]) -> int:
    return sum(a * q for a, q in zip(vector, POW3))


def decode_matrix_code(code: int) -> tuple[int, ...]:
    digits = []
    value = code
    for _ in POSITIONS:
        digits.append(value % P)
        value //= P
    require(value == 0, f"matrix code out of range: {code}")
    return tuple(digits)


def sparse(vector: tuple[int, ...] | list[int]) -> list[list[int]]:
    return [[i + 1, j + 1, vector[k]] for k, (i, j) in enumerate(POSITIONS) if vector[k]]


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % P for x, y in zip(a, b))


def scale(c: int, a: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((c * x) % P for x in a)


def multiply(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(POSITIONS)
    for out, (i, ell) in enumerate(POSITIONS):
        total = 0
        for k in range(i + 1, ell):
            total += a[POSITION_INDEX[(i, k)]] * b[POSITION_INDEX[(k, ell)]]
        result[out] = total % P
    return tuple(result)


def cube(a: tuple[int, ...]) -> tuple[int, ...]:
    # For a strict upper-triangular matrix, (a^3)_{i,l} is the sum over
    # strictly increasing length-three paths i<j<k<l.
    result = [0] * len(POSITIONS)
    for out, ij, jk, kell in CUBE_PATHS:
        result[out] += a[ij] * a[jk] * a[kell]
    return tuple(x % P for x in result)


def circle(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return add(add(a, b), multiply(a, b))


def rref(rows: list[tuple[int, ...]]) -> tuple[tuple[int, ...], ...]:
    matrix = [list(x % P for x in row) for row in rows if any(x % P for x in row)]
    pivot_row = 0
    for col in range(len(POSITIONS)):
        found = next((r for r in range(pivot_row, len(matrix)) if matrix[r][col]), None)
        if found is None:
            continue
        matrix[pivot_row], matrix[found] = matrix[found], matrix[pivot_row]
        inverse = 1 if matrix[pivot_row][col] == 1 else 2
        matrix[pivot_row] = [(inverse * x) % P for x in matrix[pivot_row]]
        for r in range(len(matrix)):
            if r == pivot_row or matrix[r][col] == 0:
                continue
            coefficient = matrix[r][col]
            matrix[r] = [
                (x - coefficient * y) % P
                for x, y in zip(matrix[r], matrix[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return tuple(tuple(row) for row in matrix[:pivot_row])


def generated_algebra(tau: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    t = tuple(tau[i] if j == i + 1 else 0 for i, j in POSITIONS)
    generators = (S, t)
    basis = rref(list(generators))
    while True:
        enlarged = list(basis)
        for b in basis:
            for g in generators:
                enlarged.append(multiply(b, g))
        new_basis = rref(enlarged)
        if new_basis == basis:
            return basis
        basis = new_basis


def coordinates(vector: tuple[int, ...], basis: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    residue = list(vector)
    answer = []
    for row in basis:
        pivot = next(i for i, x in enumerate(row) if x)
        coefficient = residue[pivot]
        answer.append(coefficient)
        if coefficient:
            residue = [(x - coefficient * y) % P for x, y in zip(residue, row)]
    require(not any(residue), "vector is not in reconstructed algebra span")
    return tuple(answer)


def matrix_from_coordinate_code(code: int, basis: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    answer = [0] * len(POSITIONS)
    value = code
    for row in basis:
        coefficient = value % P
        value //= P
        if coefficient:
            answer = [(x + coefficient * y) % P for x, y in zip(answer, row)]
    require(value == 0, f"basis-coordinate code out of range: {code}")
    return tuple(answer)


def verify_descriptor(descriptor: dict, expected_header: str) -> tuple[Path, list[str]]:
    path = Path(descriptor["path"])
    raw = path.read_bytes()
    require(sha256_bytes(raw) == descriptor["sha256_gzip_bytes"], f"gzip hash mismatch: {path}")
    data = gzip.decompress(raw)
    require(
        sha256_bytes(data) == descriptor["sha256_uncompressed_canonical_text"],
        f"uncompressed hash mismatch: {path}",
    )
    lines = data.decode("utf-8").splitlines()
    require(len(lines) == descriptor["line_count"], f"line-count mismatch: {path}")
    require(lines and lines[0] == expected_header, f"header mismatch: {path}")
    return path, lines


def canonical_value_hash(values: set[int]) -> str:
    return sha256_bytes(b"".join(struct.pack("<Q", x) for x in sorted(values)))


def parse_cube_map(
    certificate: dict,
    basis: tuple[tuple[int, ...], ...],
) -> tuple[set[int], dict[int, tuple[int, int]]]:
    _, lines = verify_descriptor(
        certificate["cube_map"],
        "root_coord_code\troot_matrix_code\tcube_matrix_code",
    )
    expected_size = P ** len(basis)
    require(len(lines) == expected_size + 1, "cube-map domain is not complete")

    coefficients = [0] * len(basis)
    current = [0] * len(POSITIONS)
    values: set[int] = set()
    first_roots: dict[int, tuple[int, int]] = {}

    for expected_coordinate, line in enumerate(lines[1:]):
        fields = line.split("\t")
        require(len(fields) == 3, "malformed cube-map row")
        coordinate_code, matrix_code, saved_cube_code = map(int, fields)
        require(coordinate_code == expected_coordinate, "cube-map coordinate order/gap failure")
        recomputed_matrix_code = vector_code(current)
        require(matrix_code == recomputed_matrix_code, "root matrix does not match basis coordinate")
        recomputed_cube_code = vector_code(cube(tuple(current)))
        require(saved_cube_code == recomputed_cube_code, "saved cube differs from independent cube")
        values.add(recomputed_cube_code)
        first_roots.setdefault(recomputed_cube_code, (coordinate_code, matrix_code))

        if expected_coordinate + 1 < expected_size:
            for i, row in enumerate(basis):
                coefficients[i] += 1
                current = [(x + y) % P for x, y in zip(current, row)]
                if coefficients[i] < P:
                    break
                coefficients[i] = 0

    return values, first_roots


def verify_actual_values(
    certificate: dict,
    values: set[int],
    first_roots: dict[int, tuple[int, int]],
) -> None:
    descriptor = certificate["actual_values_and_roots"]
    _, lines = verify_descriptor(
        descriptor,
        "cube_matrix_code\troot_coord_code\troot_matrix_code",
    )
    saved: dict[int, tuple[int, int]] = {}
    for line in lines[1:]:
        value_code, coordinate_code, matrix_code = map(int, line.split("\t"))
        require(value_code not in saved, "duplicate actual-value row")
        saved[value_code] = (coordinate_code, matrix_code)
    require(saved == first_roots, "actual-value/root manifest differs from complete cube map")
    require(set(saved) == values, "actual-value manifest has the wrong value set")
    require(descriptor["value_count"] == len(values), "actual-value count mismatch")


def verify_boundary(
    certificate: dict,
    basis: tuple[tuple[int, ...], ...],
    values: set[int],
) -> dict:
    cayley = certificate["cayley"]
    embedded = dict(cayley["closure_boundary"])
    boundary_path = Path(cayley.get("closure_boundary", {}).get("path", ""))
    # The path lives in the family manifest rather than the embedded object.
    if not boundary_path.name:
        boundary_path = Path(certificate["actual_values_and_roots"]["path"]).parent / "closure-boundary.json"
    require(boundary_path.exists(), f"missing boundary file: {boundary_path}")
    expected_artifact_hash = embedded.pop("artifact_sha256")
    require(file_sha256(boundary_path) == expected_artifact_hash, "closure-boundary hash mismatch")
    boundary = json.loads(boundary_path.read_text(encoding="utf-8"))
    require(boundary == embedded, "embedded boundary differs from boundary artifact")
    require(boundary["actual_value_count"] == len(values), "boundary value count mismatch")

    reconstructed = {}
    for name in ("u", "b"):
        item = boundary[name]
        root = matrix_from_coordinate_code(item["root_coord_code"], basis)
        value = cube(root)
        require(vector_code(root) == item["root_matrix_code"], f"{name} root code mismatch")
        require(sparse(root) == item["root_sparse"], f"{name} root sparse mismatch")
        require(vector_code(value) == item["value_code"], f"{name} value mismatch")
        require(item["replayed_cube_code"] == item["value_code"], f"{name} replay field mismatch")
        require(sparse(value) == item["value_sparse"], f"{name} value sparse mismatch")
        require(item["value_code"] in values, f"{name} is not an actual cube value")
        reconstructed[name] = value

    product = circle(reconstructed["u"], reconstructed["b"])
    product_code = vector_code(product)
    require(product_code == boundary["w_code"], "boundary circle product code mismatch")
    require(product_code == boundary["replayed_u_circle_b_code"], "boundary replay mismatch")
    require(sparse(product) == boundary["w_sparse"], "boundary sparse mismatch")
    require(product_code not in values, "claimed closure boundary lies in actual cube set")
    require(boundary["w_absent_from_actual_value_manifest"] is True, "boundary absence flag false")
    generators = boundary["generator_codes"]
    require(generators[boundary["b_generator_index"]] == boundary["b"]["value_code"], "boundary generator index mismatch")
    require(all(g in values for g in generators), "boundary generator is not an actual cube")
    return {
        "u": boundary["u"]["value_code"],
        "b": boundary["b"]["value_code"],
        "w": product_code,
        "w_absent": True,
    }


def parse_int_column(descriptor: dict, header: str) -> list[int]:
    _, lines = verify_descriptor(descriptor, header)
    return [int(line) for line in lines[1:]]


def verify_cayley_equality(
    certificate: dict,
    values: set[int],
) -> dict:
    cayley = certificate["cayley"]
    generators = [decode_matrix_code(x) for x in cayley["generator_codes"]]
    require(all(vector_code(g) in values for g in generators), "Cayley generator is not an actual cube")

    generated: set[int] = {0}
    queue: deque[tuple[int, ...]] = deque([ZERO])
    while queue:
        state = queue.popleft()
        for generator in generators:
            product = circle(state, generator)
            product_code = vector_code(product)
            if product_code not in generated:
                require(len(generated) < 10000, "unexpectedly large Cayley state set")
                generated.add(product_code)
                queue.append(product)
    require(generated == values, "independent Cayley-generated set differs from actual cube set")

    saved_states = parse_int_column(cayley["state_manifest"], "matrix_code")
    require(set(saved_states) == generated and len(saved_states) == len(generated), "saved Cayley state set mismatch")
    require(cayley["state_manifest"]["state_count"] == len(generated), "state count mismatch")

    _, transition_lines = verify_descriptor(
        cayley["transition_table"],
        "state_code\tgenerator_index\tproduct_code",
    )
    saved_transitions = {
        tuple(map(int, line.split("\t"))) for line in transition_lines[1:]
    }
    expected_transitions = set()
    for state_code in generated:
        state = decode_matrix_code(state_code)
        for generator_index, generator in enumerate(generators):
            expected_transitions.add(
                (state_code, generator_index, vector_code(circle(state, generator)))
            )
    require(saved_transitions == expected_transitions, "Cayley transition table is incomplete or incorrect")

    _, discovery_lines = verify_descriptor(
        cayley["discovery_manifest"],
        "state_code\tparent_code\tgenerator_index",
    )
    discovered: set[int] = set()
    for line_number, line in enumerate(discovery_lines[1:]):
        state_text, parent_text, generator_text = line.split("\t")
        state_code = int(state_text)
        require(state_code not in discovered, "duplicate Cayley discovery state")
        if line_number == 0:
            require((state_code, parent_text, generator_text) == (0, "NONE", "NONE"), "bad Cayley root")
        else:
            parent_code = int(parent_text)
            generator_index = int(generator_text)
            require(parent_code in discovered, "Cayley discovery parent appears too late")
            product = circle(decode_matrix_code(parent_code), generators[generator_index])
            require(vector_code(product) == state_code, "bad Cayley discovery edge")
        discovered.add(state_code)
    require(discovered == generated, "Cayley discovery manifest is incomplete")

    table_path = Path(cayley["commuting_table_path"])
    require(file_sha256(table_path) == cayley["commuting_table_sha256"], "commuting-table hash mismatch")
    table = json.loads(table_path.read_text(encoding="utf-8"))
    require(table["generator_codes"] == cayley["generator_codes"], "commuting generator list mismatch")
    expected_pairs = []
    for i, left in enumerate(generators):
        for j in range(i, len(generators)):
            right = generators[j]
            lr = vector_code(circle(left, right))
            rl = vector_code(circle(right, left))
            expected_pairs.append(
                {
                    "commute": lr == rl,
                    "i": i,
                    "j": j,
                    "left_right_code": lr,
                    "right_left_code": rl,
                }
            )
    require(table["pairs"] == expected_pairs, "commuting table differs from independent products")
    require(table["pair_count_including_diagonal"] == len(expected_pairs), "commuting pair count mismatch")
    require(table["all_pairs_commute"] is True and all(x["commute"] for x in expected_pairs), "generators do not commute")

    # Stronger redundant check: all nine actual values commute pairwise.
    decoded_values = [decode_matrix_code(x) for x in values]
    for i, left in enumerate(decoded_values):
        for right in decoded_values[i:]:
            require(circle(left, right) == circle(right, left), "closed actual cube set is nonabelian")
    return {
        "generator_count": len(generators),
        "generated_state_count": len(generated),
        "actual_set_equals_cayley_set": True,
        "all_values_commute": True,
    }


def verify_constraint_matrix(certificate: dict, closure_equal: bool) -> None:
    expected_ids = [
        "21.137-odd-forall-p-G",
        "21.137-odd-p-not-2",
        "21.137-odd-finite-p-group",
        "21.137-odd-exponent-p2",
        "21.137-odd-power-set-definition",
        "21.137-odd-power-set-subgroup",
        "21.137-odd-P-abelian",
    ]
    matrix = certificate["constraint_matrix"]
    require([row["constraint_id"] for row in matrix] == expected_ids, "constraint rows missing/reordered")
    require(matrix[0]["result"] == "not-satisfied", "universal row improperly passed")
    require(all(matrix[i]["result"] == "pass" for i in range(1, 5)), "base admissibility row failed")
    if closure_equal:
        require(matrix[5]["result"] == "pass", "closed row not marked closed")
        require(matrix[6]["result"] == "proved-for-row", "closed row conclusion mismatch")
    else:
        require(matrix[5]["result"] == "fail", "boundary row not marked failed")
        require(matrix[6]["result"] == "not-reached", "conclusion evaluated after hypothesis failure")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True, type=Path)
    args = parser.parse_args()
    run_dir = args.run_dir

    expected_top_hashes = {
        "selected-rows.json": "a8725dcadb2a361fb2cfce5e4cf340003ec609ea63808bc512012ca4bbad782a",
        "family-manifest.jsonl": "42d0d723adfc86b74d8e90aae9d78a9a0b9326b0ea31f877214fe0268d95ad34",
        "summary.json": "4c899765f15dc0c579469f7c849a8a6b1f4207dbf09a0bd8f4a80b3f5f095fc9",
    }
    observed_top_hashes = {name: file_sha256(run_dir / name) for name in expected_top_hashes}
    require(observed_top_hashes == expected_top_hashes, "top-level frozen hashes changed")

    selected_artifact = json.loads((run_dir / "selected-rows.json").read_text(encoding="utf-8"))
    manifest = [
        json.loads(line)
        for line in (run_dir / "family-manifest.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))

    endpoint_equal_count = 0
    reconstructed_selection = []
    for tau in itertools.product(range(P), repeat=6):
        endpoint_equal = (tau[0] * tau[1] * tau[2] - tau[3] * tau[4] * tau[5]) % P == 0
        if not endpoint_equal:
            continue
        endpoint_equal_count += 1
        basis = generated_algebra(tau)
        if len(basis) <= 12:
            reconstructed_selection.append((tau, basis))

    require(endpoint_equal_count == 393, "endpoint-equality category count mismatch")
    require(len(reconstructed_selection) == 11, "reconstructed E_12 does not have eleven rows")
    require(selected_artifact["row_count"] == 11 and len(selected_artifact["rows"]) == 11, "selected artifact count mismatch")
    require(len(manifest) == 11, "family manifest count mismatch")

    row_results = []
    closed_count = 0
    boundary_count = 0
    for row_number, ((tau, basis), selected_row, manifest_row) in enumerate(
        zip(reconstructed_selection, selected_artifact["rows"], manifest), start=1
    ):
        require(selected_row["row_index"] == row_number, "selected row index mismatch")
        require(manifest_row["row_index"] == row_number, "manifest row index mismatch")
        require(tuple(selected_row["tau"]) == tau == tuple(manifest_row["tau"]), "tau mismatch")
        require(selected_row["dim_J"] == len(basis) == manifest_row["dim_J"], "dimension mismatch")
        basis_codes = [vector_code(row) for row in basis]
        require(selected_row["basis_codes"] == basis_codes, "selected basis mismatch")

        certificate_path = Path(manifest_row["row_certificate_path"])
        require(file_sha256(certificate_path) == manifest_row["row_certificate_sha256"], "row-certificate hash mismatch")
        certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
        require(certificate["schema"] == "EQ11-CUBE-CAYLEY-row-v1", "row schema mismatch")
        require(certificate["row_index"] == row_number and tuple(certificate["tau"]) == tau, "certificate identity mismatch")
        require(certificate["p"] == 3 and certificate["endpoint_equal"] is True, "prime/endpoint mismatch")
        require(certificate["dim_J"] == len(basis), "certificate dimension mismatch")
        require(certificate["basis_codes"] == basis_codes, "certificate basis-code mismatch")
        require(
            certificate["basis_sparse"] == [sparse(row) for row in basis],
            "certificate sparse basis mismatch",
        )
        require(certificate["position_order"] == [[i + 1, j + 1] for i, j in POSITIONS], "position order mismatch")
        require(certificate["order_G"] == P ** len(basis) == manifest_row["order_G"], "group order mismatch")
        require(certificate["active_assignment_answered"] == "no", "row improperly answers active assignment")

        multiplication_table = []
        for left in basis:
            multiplication_table.append(
                [list(coordinates(multiply(left, right), basis)) for right in basis]
            )
        require(
            certificate["multiplication_table_basis_coordinates"] == multiplication_table,
            "saved multiplication table mismatch",
        )

        s3 = cube(S)
        require(vector_code(s3) == certificate["S3_code"] != 0, "S^3 certificate mismatch")
        require(sparse(s3) == certificate["S3_sparse"], "S^3 sparse mismatch")
        require(certificate["J_power_7_zero"] is True, "J^7 flag false")
        # Every seven-fold product of strict 7x7 upper-triangular matrices is zero.
        # Hence (1+x)^9=1+x^9=1.  Since (1+S)^3 != 1, exponent is exactly 9.
        require(certificate["exponent_G"] == 9, "exponent field mismatch")

        values, first_roots = parse_cube_map(certificate, basis)
        verify_actual_values(certificate, values, first_roots)
        require(len(values) == manifest_row["actual_value_count"], "manifest actual-value count mismatch")

        closure_equal = certificate["cayley"]["closure_equal"]
        require(closure_equal == manifest_row["closure_equal"], "manifest closure outcome mismatch")
        if closure_equal:
            cayley_result = verify_cayley_equality(certificate, values)
            require(all(x == tau[0] for x in tau), "closure-passing row is not scalar")
            t = scale(tau[0], S)
            require(
                t == tuple(tau[i] if j == i + 1 else 0 for i, j in POSITIONS),
                "scalar-row T is not cS",
            )
            require(
                all(multiply(a, b) == multiply(b, a) for a in basis for b in basis),
                "scalar-row algebra is not commutative",
            )
            closed_count += 1
            detail = cayley_result
            expected_status = "actual cube subgroup abelian"
        else:
            detail = verify_boundary(certificate, basis, values)
            boundary_count += 1
            expected_status = "actual cube set not subgroup"
        require(certificate["cayley"]["status"] == expected_status, "certificate status mismatch")
        require(manifest_row["status"] == expected_status, "manifest status mismatch")
        verify_constraint_matrix(certificate, closure_equal)

        row_results.append(
            {
                "row": row_number,
                "tau": list(tau),
                "dim_J": len(basis),
                "order_G": P ** len(basis),
                "exponent": 9,
                "actual_cube_count": len(values),
                "canonical_values_sha256_le64": canonical_value_hash(values),
                "closure_equal": closure_equal,
                "detail": detail,
            }
        )

    require((boundary_count, closed_count) == (8, 3), "outcome partition is not eight plus three")
    require(summary["rows_processed"] == 11 and summary["selected_row_count"] == 11, "summary row count mismatch")
    require(summary["complete_11_row_manifest"] is True, "summary completeness flag false")
    require(summary["candidate_row"] is None, "summary unexpectedly names candidate")
    require(summary["active_assignment_answered"] == "no", "summary improperly answers active assignment")
    require(
        summary["status_counts"]
        == {"actual cube set not subgroup": 8, "actual cube subgroup abelian": 3},
        "summary status partition mismatch",
    )
    require(summary["selection_sha256"] == observed_top_hashes["selected-rows.json"], "summary selection hash mismatch")
    require(summary["manifest_sha256"] == observed_top_hashes["family-manifest.jsonl"], "summary manifest hash mismatch")

    output = {
        "checker": "independent-EQ11-CUBE-CAYLEY-v1",
        "implementation_relation": "does not import or execute claimant enumerator",
        "top_level_sha256": observed_top_hashes,
        "family": {
            "ambient_tau_count": 729,
            "endpoint_equal_count": endpoint_equal_count,
            "selected_E12_count": len(reconstructed_selection),
            "definition": "tau in F_3^6; tau1*tau2*tau3=tau4*tau5*tau6; dim <S,T_tau> <= 12",
        },
        "rows": row_results,
        "status_counts": {
            "actual_cube_set_not_subgroup": boundary_count,
            "actual_cube_subgroup_abelian": closed_count,
        },
        "bounded_outcome": "STRATEGY_EXHAUSTED for exactly EQ11-CUBE-CAYLEY/E_12",
        "active_assignment_answered": "no",
        "result": "PASS",
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
