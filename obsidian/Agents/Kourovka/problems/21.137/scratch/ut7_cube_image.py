#!/usr/bin/env python3
"""Exact frozen ALG3-UT7-CUBE-IMAGE enumerator for Kourovka 21.137.

The program uses only arithmetic in F_3 and the 21 coordinates of strictly
upper-triangular 7 by 7 matrices.  With no arguments it runs the complete
729-row family specified in the MathExpert handoff.  ``--self-test`` and
``--prefilter-only`` are bounded implementation checks and do not certify that
the family has been exhausted.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import os
import sys
import time
from collections import deque
from pathlib import Path
from typing import Iterable, Iterator, Sequence


P = 3
N = 7
POSITIONS = tuple((i, j) for i in range(N) for j in range(i + 1, N))
POS_INDEX = {ij: k for k, ij in enumerate(POSITIONS)}
NC = len(POSITIONS)
ZERO = (0,) * NC
POW3 = tuple(P**i for i in range(NC))

RUN_DIR = Path(
    "Agents/Kourovka/problems/21.137/runs/"
    "2026-08-17-r7-alg3-ut7-cube-image"
)
MANIFEST_PATH = RUN_DIR / "manifest.jsonl"
SUMMARY_PATH = RUN_DIR / "summary.json"

# Every nonzero term in a matrix product A*B is indexed here.  There are
# C(7,3)=35 possible paths i<k<j.
PRODUCT_TERMS = tuple(
    (POS_INDEX[(i, j)], POS_INDEX[(i, k)], POS_INDEX[(k, j)])
    for i in range(N)
    for k in range(i + 1, N)
    for j in range(k + 1, N)
)


def vec_add(a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
    return tuple((x + y) % P for x, y in zip(a, b))


def vec_sub(a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
    return tuple((x - y) % P for x, y in zip(a, b))


def vec_scale(c: int, a: Sequence[int]) -> tuple[int, ...]:
    c %= P
    return tuple((c * x) % P for x in a)


def matmul(a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
    out = [0] * NC
    for dst, left, right in PRODUCT_TERMS:
        out[dst] += a[left] * b[right]
    return tuple(x % P for x in out)


def matpow(a: Sequence[int], exponent: int) -> tuple[int, ...]:
    if exponent <= 0:
        raise ValueError("Only positive powers in the nonunital algebra are used")
    out = tuple(a)
    for _ in range(1, exponent):
        out = matmul(out, a)
    return out


def cube(a: Sequence[int]) -> tuple[int, ...]:
    return matmul(matmul(a, a), a)


def circle(a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
    return vec_add(vec_add(a, b), matmul(a, b))


def circle_inverse(a: Sequence[int]) -> tuple[int, ...]:
    # (1+a)^(-1)-1 = -a+a^2-a^3+...+a^6, since a^7=0 in UT_7.
    out = ZERO
    power = tuple(a)
    for exponent in range(1, N):
        out = vec_add(out, vec_scale(2 if exponent % 2 else 1, power))
        power = matmul(power, a)
    return out


def matrix_code(a: Sequence[int]) -> int:
    return sum(x * place for x, place in zip(a, POW3))


def decode_matrix(code: int) -> tuple[int, ...]:
    out = []
    for _ in range(NC):
        code, digit = divmod(code, P)
        out.append(digit)
    if code:
        raise ValueError("matrix code exceeds 21 ternary digits")
    return tuple(out)


def sparse_matrix(a: Sequence[int]) -> list[list[int]]:
    return [[i + 1, j + 1, a[k]] for k, (i, j) in enumerate(POSITIONS) if a[k]]


def generator_s() -> tuple[int, ...]:
    out = [0] * NC
    for i in range(N - 1):
        out[POS_INDEX[(i, i + 1)]] = 1
    return tuple(out)


def generator_t(tau: Sequence[int]) -> tuple[int, ...]:
    out = [0] * NC
    for i, value in enumerate(tau):
        out[POS_INDEX[(i, i + 1)]] = value % P
    return tuple(out)


S = generator_s()
S3 = cube(S)


class RREFSpace:
    """Small exact F_3 row space, maintained in reduced row-echelon form."""

    def __init__(self) -> None:
        self.rows: list[list[int]] = []
        self.pivots: list[int] = []

    def add(self, vector: Sequence[int]) -> bool:
        v = [x % P for x in vector]
        for pivot, row in zip(self.pivots, self.rows):
            coefficient = v[pivot]
            if coefficient:
                v = [(x - coefficient * y) % P for x, y in zip(v, row)]
        try:
            pivot = next(i for i, x in enumerate(v) if x)
        except StopIteration:
            return False

        inverse = 1 if v[pivot] == 1 else 2
        v = [(inverse * x) % P for x in v]

        for index, row in enumerate(self.rows):
            coefficient = row[pivot]
            if coefficient:
                self.rows[index] = [
                    (x - coefficient * y) % P for x, y in zip(row, v)
                ]

        insertion = 0
        while insertion < len(self.pivots) and self.pivots[insertion] < pivot:
            insertion += 1
        self.pivots.insert(insertion, pivot)
        self.rows.insert(insertion, v)
        return True

    def contains(self, vector: Sequence[int]) -> bool:
        v = [x % P for x in vector]
        for pivot, row in zip(self.pivots, self.rows):
            coefficient = v[pivot]
            if coefficient:
                v = [(x - coefficient * y) % P for x, y in zip(v, row)]
        return not any(v)

    def coordinates(self, vector: Sequence[int]) -> tuple[int, ...]:
        if not self.contains(vector):
            raise ValueError("vector is not in the row space")
        # In RREF each pivot column is a unit column, so these entries are the
        # unique coefficients relative to the ordered RREF rows.
        return tuple(vector[pivot] % P for pivot in self.pivots)

    def frozen_rows(self) -> tuple[tuple[int, ...], ...]:
        return tuple(tuple(row) for row in self.rows)


def algebra_basis(tau: Sequence[int]) -> tuple[tuple[int, ...], ...]:
    space = RREFSpace()
    space.add(S)
    space.add(generator_t(tau))
    while True:
        snapshot = space.frozen_rows()
        changed = False
        for left in snapshot:
            for right in snapshot:
                if space.add(matmul(left, right)):
                    changed = True
        if not changed:
            rows = space.frozen_rows()
            # Mechanical closure audit after the final RREF mutations.
            for left in rows:
                for right in rows:
                    if not space.contains(matmul(left, right)):
                        raise AssertionError("computed algebra basis is not multiplicatively closed")
            return rows


def iter_span(basis: Sequence[Sequence[int]]) -> Iterator[tuple[int, ...]]:
    """Enumerate each vector in the F_3-span exactly once."""

    def walk(index: int, current: tuple[int, ...]) -> Iterator[tuple[int, ...]]:
        if index == len(basis):
            yield current
            return
        row = tuple(basis[index])
        yield from walk(index + 1, current)
        yield from walk(index + 1, vec_add(current, row))
        yield from walk(index + 1, vec_add(current, vec_scale(2, row)))

    yield from walk(0, ZERO)


def leading_layer_witness(tau: Sequence[int]) -> dict | None:
    t = generator_t(tau)
    representatives: dict[tuple[int, ...], tuple[int, int]] = {}
    for a, b in itertools.product(range(P), repeat=2):
        v = vec_add(vec_scale(a, S), vec_scale(b, t))
        representatives.setdefault(cube(v), (a, b))

    values = sorted(representatives, key=matrix_code)
    value_set = set(values)
    for left in values:
        for right in values:
            total = vec_add(left, right)
            if total not in value_set:
                a, b = representatives[left]
                c, d = representatives[right]
                return {
                    "v_coefficients_S_T": [a, b],
                    "w_coefficients_S_T": [c, d],
                    "v_cube_code": matrix_code(left),
                    "w_cube_code": matrix_code(right),
                    "sum_code": matrix_code(total),
                    "C_size": len(value_set),
                }
    return None


def complete_cube_image(basis: Sequence[Sequence[int]]) -> set[tuple[int, ...]]:
    image: set[tuple[int, ...]] = set()
    expected = P ** len(basis)
    count = 0
    for element in iter_span(basis):
        image.add(cube(element))
        count += 1
    if count != expected:
        raise AssertionError(f"span enumerator emitted {count}, expected {expected}")
    return image


def subgroup_generated_by_actual_values(
    image: set[tuple[int, ...]], group_order: int
) -> tuple[set[tuple[int, ...]], list[tuple[int, ...]], dict | None]:
    """Return K=<image>_circle and a shortest two-letter closure defect.

    Every move is itself in the actual-value set (including inverses).  During
    BFS, the first edge from a vertex in X to a vertex outside X supplies a
    length-two word x circle y outside X.  Length zero and one cannot be a
    closure defect, so this is shortest.
    """

    if ZERO not in image:
        raise AssertionError("cube image omits zero")

    ordered_image = sorted(image, key=matrix_code)
    generators: list[tuple[int, ...]] = []
    subgroup: set[tuple[int, ...]] = {ZERO}
    first_defect: dict | None = None

    for candidate in ordered_image:
        if candidate in subgroup:
            continue
        generators.append(candidate)
        moves: list[tuple[int, ...]] = []
        seen_moves: set[tuple[int, ...]] = set()
        for generator in generators:
            for move in (generator, circle_inverse(generator)):
                if move not in image:
                    raise AssertionError("actual cube image is not inverse-stable")
                if move not in seen_moves and move != ZERO:
                    seen_moves.add(move)
                    moves.append(move)

        subgroup = {ZERO}
        queue: deque[tuple[int, ...]] = deque([ZERO])
        while queue:
            current = queue.popleft()
            for move in moves:
                product = circle(current, move)
                if first_defect is None and current in image and product not in image:
                    first_defect = {
                        "left_code": matrix_code(current),
                        "right_code": matrix_code(move),
                        "product_code": matrix_code(product),
                        "word_length": 2,
                    }
                if product not in subgroup:
                    subgroup.add(product)
                    if len(subgroup) > group_order:
                        raise AssertionError("generated subgroup exceeds ambient group order")
                    queue.append(product)

    if not image.issubset(subgroup):
        raise AssertionError("generated subgroup does not contain its generators")
    if len(subgroup) > len(image) and first_defect is None:
        raise AssertionError("subgroup is larger but no two-letter closure defect was found")
    if len(subgroup) == len(image) and subgroup != image:
        raise AssertionError("equal cardinality without equality")
    return subgroup, generators, first_defect


def multiplication_table(basis: Sequence[Sequence[int]]) -> list[list[list[int]]]:
    space = RREFSpace()
    for row in basis:
        if not space.add(row):
            raise AssertionError("basis lost independence")
    canonical = space.frozen_rows()
    if tuple(tuple(row) for row in basis) != canonical:
        raise AssertionError("basis is not canonical RREF")
    return [
        [list(space.coordinates(matmul(left, right))) for right in basis]
        for left in basis
    ]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_code_set(path: Path, values: Iterable[Sequence[int]]) -> dict:
    codes = sorted(matrix_code(value) for value in values)
    with gzip.open(path, "wt", encoding="utf-8", newline="\n") as handle:
        for code in codes:
            handle.write(f"{code}\n")
    return {
        "path": str(path),
        "count": len(codes),
        "sha256_gzip_bytes": sha256_file(path),
        "encoding": "base-3 integer sum coordinate[k]*3^k; coordinates use metadata position_order",
    }


def write_success_artifacts(
    tau: Sequence[int],
    basis: Sequence[Sequence[int]],
    image: set[tuple[int, ...]],
    subgroup: set[tuple[int, ...]],
    generators: Sequence[Sequence[int]],
) -> Path:
    tau_slug = "".join(str(x) for x in tau)
    target = RUN_DIR / "success" / f"tau-{tau_slug}"
    target.mkdir(parents=True, exist_ok=True)

    x_meta = write_code_set(target / "X-codes.txt.gz", image)
    k_meta = write_code_set(target / "K-codes.txt.gz", subgroup)
    t = generator_t(tau)
    t3 = cube(t)
    left_product = matmul(S3, t3)
    right_product = matmul(t3, S3)
    table = multiplication_table(basis)

    data = {
        "schema": "ALG3-UT7-CUBE-IMAGE-success-v1",
        "p": P,
        "n": N,
        "tau": list(tau),
        "position_order": [[i + 1, j + 1] for i, j in POSITIONS],
        "dim_J": len(basis),
        "order_G": P ** len(basis),
        "basis_codes": [matrix_code(row) for row in basis],
        "basis_sparse": [sparse_matrix(row) for row in basis],
        "multiplication_table_basis_coordinates": table,
        "nilpotence": {
            "ambient_identity": "every product of seven strictly upper-triangular 7x7 matrices is zero",
            "J_power_7_zero": True,
        },
        "S_code": matrix_code(S),
        "S3_code": matrix_code(S3),
        "S3_sparse": sparse_matrix(S3),
        "T_code": matrix_code(t),
        "T3_code": matrix_code(t3),
        "T3_sparse": sparse_matrix(t3),
        "S3_T3_code": matrix_code(left_product),
        "T3_S3_code": matrix_code(right_product),
        "endpoint_products_unequal": left_product != right_product,
        "X": x_meta,
        "K": k_meta,
        "Delta": len(subgroup) - len(image),
        "circle_generator_codes": [matrix_code(g) for g in generators],
        "constraint_matrix": [
            {
                "constraint_id": "21.137-odd-forall-p-G",
                "role": "admissibility",
                "candidate_value": "this one fully admissible G_tau",
                "result": "pass",
            },
            {
                "constraint_id": "21.137-odd-p-not-2",
                "role": "admissibility",
                "candidate_value": "p=3",
                "result": "pass",
            },
            {
                "constraint_id": "21.137-odd-finite-p-group",
                "role": "admissibility",
                "candidate_value": f"G=1+J_tau has order 3^{len(basis)}",
                "result": "pass",
            },
            {
                "constraint_id": "21.137-odd-exponent-p2",
                "role": "admissibility",
                "candidate_value": "exponent exactly 9",
                "result": "pass",
            },
            {
                "constraint_id": "21.137-odd-power-set-definition",
                "role": "admissibility",
                "candidate_value": f"complete actual cube image 1+X, |X|={len(image)}",
                "result": "pass",
            },
            {
                "constraint_id": "21.137-odd-power-set-subgroup",
                "role": "admissibility",
                "candidate_value": f"|K|-|X|={len(subgroup)-len(image)}",
                "result": "pass" if subgroup == image else "fail",
            },
            {
                "constraint_id": "21.137-odd-P-abelian",
                "role": "target_conclusion",
                "candidate_value": "S^3 T^3 != T^3 S^3",
                "result": "violated" if left_product != right_product else "not-violated",
            },
        ],
    }
    artifact = target / "candidate.json"
    artifact.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return artifact


def endpoint_data(tau: Sequence[int]) -> tuple[int, int, bool]:
    left = (tau[0] * tau[1] * tau[2]) % P
    right = (tau[3] * tau[4] * tau[5]) % P
    return left, right, left != right


def row_prefilter(tau: Sequence[int]) -> tuple[dict, tuple[tuple[int, ...], ...], dict | None]:
    left, right, endpoint_pass = endpoint_data(tau)
    basis = algebra_basis(tau)
    row = {
        "tau": list(tau),
        "endpoint_left_tau1tau2tau3": left,
        "endpoint_right_tau4tau5tau6": right,
        "endpoint_filter": endpoint_pass,
        "dim_J": len(basis),
    }
    if not endpoint_pass or len(basis) > 12:
        row["status"] = "outside F_12"
        row["outside_reasons"] = [
            reason
            for condition, reason in (
                (not endpoint_pass, "endpoint product equality"),
                (len(basis) > 12, "dim J > 12"),
            )
            if condition
        ]
        return row, basis, None

    witness = leading_layer_witness(tau)
    if witness is not None:
        row["status"] = "leading-layer not additive"
        row["leading_layer_witness"] = witness
    return row, basis, witness


def self_test() -> None:
    e12 = [0] * NC
    e23 = [0] * NC
    e13 = [0] * NC
    e12[POS_INDEX[(0, 1)]] = 1
    e23[POS_INDEX[(1, 2)]] = 1
    e13[POS_INDEX[(0, 2)]] = 1
    assert matmul(e12, e23) == tuple(e13)
    assert matmul(e23, e12) == ZERO

    expected_s3 = [0] * NC
    for i in range(4):
        expected_s3[POS_INDEX[(i, i + 3)]] = 1
    assert S3 == tuple(expected_s3)
    assert matpow(S, 7) == ZERO
    assert matpow(S, 6) != ZERO

    for tau in itertools.product(range(P), repeat=6):
        t3 = cube(generator_t(tau))
        direct_left = matmul(S3, t3)
        direct_right = matmul(t3, S3)
        left, right, endpoint_pass = endpoint_data(tau)
        expected_defect = [0] * NC
        expected_defect[POS_INDEX[(0, 6)]] = (right - left) % P
        assert vec_sub(direct_left, direct_right) == tuple(expected_defect)
        assert (direct_left != direct_right) == endpoint_pass

    for tau in ((0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1), (1, 2, 1, 2, 1, 2)):
        basis = algebra_basis(tau)
        space = RREFSpace()
        for row in basis:
            assert space.add(row)
        for row in basis:
            assert space.contains(row)
        for left in basis:
            for right in basis:
                assert space.contains(matmul(left, right))

    for a in (ZERO, S, S3, vec_add(S3, matpow(S, 4))):
        inverse = circle_inverse(a)
        assert circle(a, inverse) == ZERO
        assert circle(inverse, a) == ZERO
        assert decode_matrix(matrix_code(a)) == a


def run(prefilter_only: bool) -> int:
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    started = time.time()
    rows: list[dict] = []
    retained = 0
    leading_rejects = 0
    closure_rejects = 0
    successes = 0
    candidate_artifact: str | None = None

    manifest_tmp = MANIFEST_PATH.with_suffix(".jsonl.tmp")
    with manifest_tmp.open("w", encoding="utf-8", newline="\n") as manifest:
        for row_number, tau in enumerate(itertools.product(range(P), repeat=6), start=1):
            row, basis, leading_witness = row_prefilter(tau)
            if row.get("status") == "outside F_12":
                pass
            elif leading_witness is not None:
                leading_rejects += 1
            elif prefilter_only:
                retained += 1
                row["status"] = "leading-layer survivor; full closure not run"
            else:
                retained += 1
                image = complete_cube_image(basis)
                subgroup, generators, defect = subgroup_generated_by_actual_values(
                    image, P ** len(basis)
                )
                delta = len(subgroup) - len(image)
                row.update(
                    {
                        "X_size": len(image),
                        "K_size": len(subgroup),
                        "Delta": delta,
                        "circle_generator_codes": [matrix_code(g) for g in generators],
                    }
                )
                if delta > 0:
                    if defect is None:
                        raise AssertionError("positive Delta without closure witness")
                    row["status"] = "actual cube image not circle-closed"
                    row["shortest_circle_word_outside_X"] = defect
                    closure_rejects += 1
                else:
                    left, right, endpoint_pass = endpoint_data(tau)
                    if not endpoint_pass:
                        row["status"] = "Delta=0 but noncommuting endpoint gate fails"
                    else:
                        row["status"] = "TARGET-EQUAL CANDIDATE"
                        successes += 1
                        artifact = write_success_artifacts(
                            tau, basis, image, subgroup, generators
                        )
                        candidate_artifact = str(artifact)

            row["row_number"] = row_number
            manifest.write(json.dumps(row, sort_keys=True) + "\n")
            manifest.flush()
            rows.append(row)
            if successes:
                break

    os.replace(manifest_tmp, MANIFEST_PATH)
    complete_729 = len(rows) == P**6
    elapsed = time.time() - started
    status_counts: dict[str, int] = {}
    for row in rows:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1

    summary = {
        "schema": "ALG3-UT7-CUBE-IMAGE-summary-v1",
        "command_mode": "prefilter-only" if prefilter_only else "full",
        "rows_processed": len(rows),
        "complete_729_row_manifest": complete_729,
        "stopped_on_first_target_equal_candidate": bool(successes),
        "retained_after_endpoint_dimension_and_leading_filters": retained,
        "leading_layer_rejections": leading_rejects,
        "closure_rejections": closure_rejects,
        "successes": successes,
        "candidate_artifact": candidate_artifact,
        "status_counts": status_counts,
        "elapsed_wall_seconds": elapsed,
        "manifest_path": str(MANIFEST_PATH),
        "manifest_sha256": sha256_file(MANIFEST_PATH),
        "position_order": [[i + 1, j + 1] for i, j in POSITIONS],
        "matrix_encoding": "base-3 integer sum coordinate[k]*3^k",
        "scope_id": "21.137/odd-prime-exponent-p2",
        "assignment_revision": 2,
        "family": "tau in F_3^6, endpoint products unequal, dim(J_tau)<=12",
        "limitations": (
            "A complete no-pass run exhausts only the frozen F_12 family; "
            "it does not answer the unrestricted target."
        ),
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if (prefilter_only or successes or complete_729) else 2


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--prefilter-only", action="store_true")
    args = parser.parse_args()
    self_test()
    if args.self_test:
        print("self-test: PASS")
        return 0
    return run(prefilter_only=args.prefilter_only)


if __name__ == "__main__":
    sys.exit(main())
