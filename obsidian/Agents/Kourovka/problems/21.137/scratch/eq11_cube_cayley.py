#!/usr/bin/env python3
"""Exact EQ11-CUBE-CAYLEY enumerator for Kourovka 21.137.

This program freezes the endpoint-equal rows with dim J_tau <= 12 in the
two-generator UT_7(F_3) template.  For each row it writes the complete map
x -> x^3, retains a canonical root for every actual cube value, and runs the
boundary-sensitive positive-generator Cayley BFS specified by MathExpert.
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
    "2026-08-17-r8-eq11-cube-cayley"
)
ROWS_DIR = RUN_DIR / "rows"
SELECTION_PATH = RUN_DIR / "selected-rows.json"
MANIFEST_PATH = RUN_DIR / "family-manifest.jsonl"
SUMMARY_PATH = RUN_DIR / "summary.json"

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
    return tuple(((c % P) * x) % P for x in a)


def matmul(a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
    out = [0] * NC
    for dst, left, right in PRODUCT_TERMS:
        out[dst] += a[left] * b[right]
    return tuple(x % P for x in out)


def cube(a: Sequence[int]) -> tuple[int, ...]:
    return matmul(matmul(a, a), a)


def matpow(a: Sequence[int], exponent: int) -> tuple[int, ...]:
    if exponent < 1:
        raise ValueError("positive exponent required")
    out = tuple(a)
    for _ in range(1, exponent):
        out = matmul(out, a)
    return out


def circle(a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
    return vec_add(vec_add(a, b), matmul(a, b))


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
    """Exact reduced row space over F_3."""

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
            pivot = next(index for index, value in enumerate(v) if value)
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
            raise ValueError("vector is outside the space")
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
            for left in rows:
                for right in rows:
                    if not space.contains(matmul(left, right)):
                        raise AssertionError("algebra basis is not multiplicatively closed")
            return rows


def multiplication_table(basis: Sequence[Sequence[int]]) -> list[list[list[int]]]:
    space = RREFSpace()
    for row in basis:
        if not space.add(row):
            raise AssertionError("basis is dependent")
    if space.frozen_rows() != tuple(tuple(row) for row in basis):
        raise AssertionError("basis is not canonical RREF")
    return [
        [list(space.coordinates(matmul(left, right))) for right in basis]
        for left in basis
    ]


def coordinate_vector(code: int, basis: Sequence[Sequence[int]]) -> tuple[int, ...]:
    out = ZERO
    remaining = code
    for row in basis:
        remaining, coefficient = divmod(remaining, P)
        if coefficient:
            out = vec_add(out, vec_scale(coefficient, row))
    if remaining:
        raise ValueError("coordinate code exceeds basis dimension")
    return out


def iter_space_numeric(
    basis: Sequence[Sequence[int]],
) -> Iterator[tuple[int, tuple[int, ...]]]:
    """Yield coordinate codes 0..3^d-1 and their vectors in numeric order."""

    dimension = len(basis)
    coefficients = [0] * dimension
    current = ZERO
    total = P**dimension
    for code in range(total):
        yield code, current
        if code + 1 == total:
            break
        index = 0
        while True:
            current = vec_add(current, basis[index])
            if coefficients[index] < P - 1:
                coefficients[index] += 1
                break
            coefficients[index] = 0
            index += 1


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


class CanonicalGzipWriter:
    """Deterministic gzip stream plus SHA-256 of uncompressed canonical bytes."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.raw = path.open("wb")
        self.stream = gzip.GzipFile(filename="", mode="wb", fileobj=self.raw, mtime=0)
        self.semantic_digest = hashlib.sha256()
        self.lines = 0

    def write(self, line: str) -> None:
        data = line.encode("utf-8")
        self.stream.write(data)
        self.semantic_digest.update(data)
        self.lines += 1

    def close(self) -> dict:
        self.stream.close()
        self.raw.close()
        return {
            "path": str(self.path),
            "line_count": self.lines,
            "sha256_uncompressed_canonical_text": self.semantic_digest.hexdigest(),
            "sha256_gzip_bytes": sha256_file(self.path),
        }


def write_json(path: Path, value: object) -> str:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return sha256_file(path)


def endpoint_equal(tau: Sequence[int]) -> bool:
    return (
        tau[0] * tau[1] * tau[2] - tau[3] * tau[4] * tau[5]
    ) % P == 0


def freeze_family() -> list[tuple[tuple[int, ...], tuple[tuple[int, ...], ...]]]:
    selected = []
    for tau in itertools.product(range(P), repeat=6):
        basis = algebra_basis(tau)
        if endpoint_equal(tau) and len(basis) <= 12:
            selected.append((tuple(tau), basis))
    if len(selected) != 11:
        raise AssertionError(f"frozen E_12 must have 11 rows, found {len(selected)}")
    distribution: dict[int, int] = {}
    for _, basis in selected:
        distribution[len(basis)] = distribution.get(len(basis), 0) + 1
    if distribution != {6: 3, 11: 8}:
        raise AssertionError(f"unexpected E_12 dimension distribution: {distribution}")
    return selected


def enumerate_actual_cubes(
    row_dir: Path, basis: Sequence[Sequence[int]]
) -> tuple[dict[tuple[int, ...], tuple[int, int]], dict, dict]:
    """Write every x->x^3 entry and the unique value/canonical-root manifest."""

    cube_writer = CanonicalGzipWriter(row_dir / "cube-map.tsv.gz")
    cube_writer.write("root_coord_code\troot_matrix_code\tcube_matrix_code\n")
    roots: dict[tuple[int, ...], tuple[int, int]] = {}
    expected = P ** len(basis)
    count = 0
    for coordinate_code, element in iter_space_numeric(basis):
        value = cube(element)
        element_code = matrix_code(element)
        value_code = matrix_code(value)
        cube_writer.write(f"{coordinate_code}\t{element_code}\t{value_code}\n")
        roots.setdefault(value, (coordinate_code, element_code))
        count += 1
    cube_meta = cube_writer.close()
    if count != expected or cube_meta["line_count"] != expected + 1:
        raise AssertionError("incomplete x->x^3 manifest")

    root_writer = CanonicalGzipWriter(row_dir / "actual-values-and-roots.tsv.gz")
    root_writer.write("cube_matrix_code\troot_coord_code\troot_matrix_code\n")
    value_codes_digest = hashlib.sha256()
    for value in sorted(roots, key=matrix_code):
        coordinate_code, element_code = roots[value]
        value_code = matrix_code(value)
        root_writer.write(f"{value_code}\t{coordinate_code}\t{element_code}\n")
        value_codes_digest.update(f"{value_code}\n".encode("utf-8"))
    root_meta = root_writer.close()
    root_meta["value_count"] = len(roots)
    root_meta["value_codes_sha256"] = value_codes_digest.hexdigest()
    if root_meta["line_count"] != len(roots) + 1:
        raise AssertionError("incomplete unique-value/root manifest")
    return roots, cube_meta, root_meta


def bfs_once(
    generators: Sequence[tuple[int, ...]],
    values: set[tuple[int, ...]],
    transition_writer: CanonicalGzipWriter | None = None,
) -> tuple[set[tuple[int, ...]], dict | None, list[tuple[tuple[int, ...], int | None, tuple[int, ...] | None]]]:
    states: set[tuple[int, ...]] = {ZERO}
    queue: deque[tuple[int, ...]] = deque([ZERO])
    discoveries = [(ZERO, None, None)]
    while queue:
        current = queue.popleft()
        for generator_index, generator in enumerate(generators):
            product = circle(current, generator)
            if transition_writer is not None:
                transition_writer.write(
                    f"{matrix_code(current)}\t{generator_index}\t{matrix_code(product)}\n"
                )
            if product not in values:
                return (
                    states,
                    {
                        "u": current,
                        "generator_index": generator_index,
                        "b": generator,
                        "w": product,
                    },
                    discoveries,
                )
            if product not in states:
                states.add(product)
                queue.append(product)
                discoveries.append((product, generator_index, current))
    return states, None, discoveries


def root_record(
    value: tuple[int, ...],
    roots: dict[tuple[int, ...], tuple[int, int]],
    basis: Sequence[Sequence[int]],
) -> dict:
    coordinate_code, stored_matrix_code = roots[value]
    root = coordinate_vector(coordinate_code, basis)
    if matrix_code(root) != stored_matrix_code or cube(root) != value:
        raise AssertionError("canonical cube root replay failed")
    return {
        "value_code": matrix_code(value),
        "value_sparse": sparse_matrix(value),
        "root_coord_code": coordinate_code,
        "root_matrix_code": stored_matrix_code,
        "root_sparse": sparse_matrix(root),
        "replayed_cube_code": matrix_code(cube(root)),
    }


def write_code_manifest(path: Path, values: Iterable[Sequence[int]]) -> dict:
    writer = CanonicalGzipWriter(path)
    writer.write("matrix_code\n")
    codes_digest = hashlib.sha256()
    count = 0
    for value in sorted(values, key=matrix_code):
        code = matrix_code(value)
        writer.write(f"{code}\n")
        codes_digest.update(f"{code}\n".encode("utf-8"))
        count += 1
    meta = writer.close()
    meta["state_count"] = count
    meta["codes_sha256"] = codes_digest.hexdigest()
    return meta


def analyze_cayley(
    row_dir: Path,
    basis: Sequence[Sequence[int]],
    roots: dict[tuple[int, ...], tuple[int, int]],
    value_meta: dict,
) -> dict:
    values = set(roots)
    if ZERO not in values:
        raise AssertionError("actual cube set omits identity coordinate zero")
    ordered_values = sorted(values, key=matrix_code)
    generators: list[tuple[int, ...]] = []
    states: set[tuple[int, ...]] = {ZERO}

    for value in ordered_values:
        if value in states:
            continue
        generators.append(value)
        states, boundary, _ = bfs_once(generators, values)
        if boundary is not None:
            u = boundary["u"]
            b = boundary["b"]
            w = boundary["w"]
            replay = circle(u, b)
            if replay != w or u not in values or b not in values or w in values:
                raise AssertionError("closure-boundary replay failed")
            record = {
                "observable": "closure boundary",
                "generator_count_at_boundary": len(generators),
                "generator_codes": [matrix_code(g) for g in generators],
                "u": root_record(u, roots, basis),
                "b": root_record(b, roots, basis),
                "b_generator_index": boundary["generator_index"],
                "w_code": matrix_code(w),
                "w_sparse": sparse_matrix(w),
                "replayed_u_circle_b_code": matrix_code(replay),
                "w_absent_from_actual_value_manifest": True,
                "actual_value_count": len(values),
                "actual_value_codes_sha256": value_meta["value_codes_sha256"],
            }
            boundary_path = row_dir / "closure-boundary.json"
            record["artifact_sha256"] = write_json(boundary_path, record)
            return {
                "status": "actual cube set not subgroup",
                "closure_boundary": record,
                "closure_equal": False,
                "generator_codes": [matrix_code(g) for g in generators],
            }

    if states != values:
        raise AssertionError("scan ended without exact generated-set equality")
    if len(generators) > len(basis):
        raise AssertionError("greedy subgroup generator list exceeds log_3 ambient order")

    transition_writer = CanonicalGzipWriter(row_dir / "cayley-transitions.tsv.gz")
    transition_writer.write("state_code\tgenerator_index\tproduct_code\n")
    replay_states, replay_boundary, discoveries = bfs_once(
        generators, values, transition_writer=transition_writer
    )
    transition_meta = transition_writer.close()
    if replay_boundary is not None or replay_states != values:
        raise AssertionError("final Cayley equality replay failed")
    if transition_meta["line_count"] != len(values) * len(generators) + 1:
        raise AssertionError("incomplete Cayley transition table")

    state_meta = write_code_manifest(row_dir / "cayley-states.txt.gz", replay_states)
    if state_meta["codes_sha256"] != value_meta["value_codes_sha256"]:
        raise AssertionError("Cayley-state set differs from actual-value set")

    discovery_writer = CanonicalGzipWriter(row_dir / "cayley-discovery.tsv.gz")
    discovery_writer.write("state_code\tparent_code\tgenerator_index\n")
    for state, generator_index, parent in discoveries:
        if parent is None:
            discovery_writer.write(f"{matrix_code(state)}\tNONE\tNONE\n")
        else:
            discovery_writer.write(
                f"{matrix_code(state)}\t{matrix_code(parent)}\t{generator_index}\n"
            )
    discovery_meta = discovery_writer.close()
    if discovery_meta["line_count"] != len(values) + 1:
        raise AssertionError("incomplete Cayley discovery list")

    commuting_rows = []
    first_noncommuting = None
    for i, left in enumerate(generators):
        for j in range(i, len(generators)):
            right = generators[j]
            left_product = circle(left, right)
            right_product = circle(right, left)
            equal = left_product == right_product
            entry = {
                "i": i,
                "j": j,
                "left_right_code": matrix_code(left_product),
                "right_left_code": matrix_code(right_product),
                "commute": equal,
            }
            commuting_rows.append(entry)
            if i < j and not equal and first_noncommuting is None:
                difference = vec_sub(matmul(left, right), matmul(right, left))
                first_noncommuting = {
                    "i": i,
                    "j": j,
                    "left": root_record(left, roots, basis),
                    "right": root_record(right, roots, basis),
                    "left_circle_right_code": matrix_code(left_product),
                    "right_circle_left_code": matrix_code(right_product),
                    "matrix_product_difference_code": matrix_code(difference),
                    "matrix_product_difference_sparse": sparse_matrix(difference),
                }

    table = {
        "generator_codes": [matrix_code(g) for g in generators],
        "pair_count_including_diagonal": len(commuting_rows),
        "pairs": commuting_rows,
        "all_pairs_commute": first_noncommuting is None,
    }
    table_path = row_dir / "generator-commuting-table.json"
    table_hash = write_json(table_path, table)

    result = {
        "closure_boundary": None,
        "closure_equal": True,
        "actual_value_count": len(values),
        "cayley_state_count": len(replay_states),
        "generator_count": len(generators),
        "generator_codes": [matrix_code(g) for g in generators],
        "value_codes_sha256": value_meta["value_codes_sha256"],
        "cayley_state_codes_sha256": state_meta["codes_sha256"],
        "transition_table": transition_meta,
        "state_manifest": state_meta,
        "discovery_manifest": discovery_meta,
        "commuting_table_path": str(table_path),
        "commuting_table_sha256": table_hash,
        "first_noncommuting_pair": first_noncommuting,
    }
    if first_noncommuting is None:
        result["status"] = "actual cube subgroup abelian"
    else:
        result["status"] = "TARGET-EQUAL CANDIDATE"
    return result


def row_constraint_matrix(tau: Sequence[int], dimension: int, cayley: dict) -> list[dict]:
    closure = bool(cayley["closure_equal"])
    noncommuting = cayley.get("first_noncommuting_pair") is not None
    return [
        {
            "constraint_id": "21.137-odd-forall-p-G",
            "role": "admissibility",
            "candidate_value": "one tested G_tau" if closure and noncommuting else "no fully admissible witness in this row",
            "result": "pass" if closure and noncommuting else "not-satisfied",
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
            "candidate_value": f"G_tau=1+J_tau has order 3^{dimension}",
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
            "candidate_value": "complete enumerated actual cube set 1+{x^3:x in J_tau}",
            "result": "pass",
        },
        {
            "constraint_id": "21.137-odd-power-set-subgroup",
            "role": "admissibility",
            "candidate_value": "exact Cayley set equality" if closure else "direct closure-boundary triple",
            "result": "pass" if closure else "fail",
        },
        {
            "constraint_id": "21.137-odd-P-abelian",
            "role": "target_conclusion",
            "candidate_value": "noncommuting actual-cube generators" if noncommuting else "complete commuting-generator table" if closure else "not tested after closure failure",
            "result": "violated" if noncommuting else "proved-for-row" if closure else "not-reached",
        },
    ]


def analyze_row(
    row_index: int, tau: tuple[int, ...], basis: tuple[tuple[int, ...], ...]
) -> tuple[dict, bool]:
    slug = "".join(str(value) for value in tau)
    row_dir = ROWS_DIR / f"{row_index:02d}-tau-{slug}"
    row_dir.mkdir(parents=True, exist_ok=True)

    dimension = len(basis)
    t = generator_t(tau)
    endpoint_left = matmul(S3, cube(t))
    endpoint_right = matmul(cube(t), S3)
    if endpoint_left != endpoint_right:
        raise AssertionError("selected row violates endpoint equality")

    roots, cube_meta, value_meta = enumerate_actual_cubes(row_dir, basis)
    cayley = analyze_cayley(row_dir, basis, roots, value_meta)
    candidate = cayley["status"] == "TARGET-EQUAL CANDIDATE"

    row_data = {
        "schema": "EQ11-CUBE-CAYLEY-row-v1",
        "row_index": row_index,
        "tau": list(tau),
        "p": P,
        "position_order": [[i + 1, j + 1] for i, j in POSITIONS],
        "matrix_encoding": "sum coordinate[k]*3^k in position_order",
        "basis_coordinate_encoding": "sum coefficient[i]*3^i in canonical RREF basis order",
        "dim_J": dimension,
        "order_G": P**dimension,
        "basis_codes": [matrix_code(row) for row in basis],
        "basis_sparse": [sparse_matrix(row) for row in basis],
        "multiplication_table_basis_coordinates": multiplication_table(basis),
        "S3_code": matrix_code(S3),
        "S3_sparse": sparse_matrix(S3),
        "J_power_7_zero": True,
        "exponent_G": 9,
        "endpoint_equal": True,
        "S3_T3_code": matrix_code(endpoint_left),
        "T3_S3_code": matrix_code(endpoint_right),
        "cube_map": cube_meta,
        "actual_values_and_roots": value_meta,
        "cayley": cayley,
        "constraint_matrix": row_constraint_matrix(tau, dimension, cayley),
        "active_assignment_answered": "candidate-pending-review" if candidate else "no",
    }
    row_path = row_dir / "row-certificate.json"
    row_hash = write_json(row_path, row_data)
    manifest_row = {
        "row_index": row_index,
        "tau": list(tau),
        "dim_J": dimension,
        "order_G": P**dimension,
        "actual_value_count": value_meta["value_count"],
        "status": cayley["status"],
        "closure_equal": cayley["closure_equal"],
        "boundary_path": str(row_dir / "closure-boundary.json") if not cayley["closure_equal"] else None,
        "row_certificate_path": str(row_path),
        "row_certificate_sha256": row_hash,
    }
    if cayley["closure_equal"]:
        manifest_row["generator_count"] = cayley["generator_count"]
        manifest_row["first_noncommuting_pair"] = cayley["first_noncommuting_pair"]
    return manifest_row, candidate


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
    assert matpow(S, 7) == ZERO and matpow(S, 6) != ZERO
    assert decode_matrix(matrix_code(S3)) == S3

    # Numeric-coordinate iterator and decoder agree on a two-vector test basis.
    test_basis = (tuple(e12), tuple(e23))
    emitted = list(iter_space_numeric(test_basis))
    assert len(emitted) == 9
    assert [code for code, _ in emitted] == list(range(9))
    for code, vector in emitted:
        assert coordinate_vector(code, test_basis) == vector

    # Positive BFS on the cyclic order-3 subgroup generated by E12.
    a = tuple(e12)
    values = {ZERO, a, vec_scale(2, a)}
    states, boundary, _ = bfs_once([a], values)
    assert boundary is None and states == values


def run() -> int:
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    ROWS_DIR.mkdir(parents=True, exist_ok=True)
    started = time.time()
    family = freeze_family()
    selection = {
        "schema": "EQ11-CUBE-CAYLEY-selection-v1",
        "definition": "tau in F_3^6, endpoint products equal, dim J_tau<=12",
        "row_count": len(family),
        "rows": [
            {
                "row_index": index,
                "tau": list(tau),
                "dim_J": len(basis),
                "basis_codes": [matrix_code(row) for row in basis],
            }
            for index, (tau, basis) in enumerate(family, start=1)
        ],
    }
    selection_hash = write_json(SELECTION_PATH, selection)

    manifest_rows = []
    candidate = False
    manifest_tmp = MANIFEST_PATH.with_suffix(".jsonl.tmp")
    with manifest_tmp.open("w", encoding="utf-8", newline="\n") as manifest:
        for row_index, (tau, basis) in enumerate(family, start=1):
            row, candidate = analyze_row(row_index, tau, basis)
            manifest.write(json.dumps(row, sort_keys=True) + "\n")
            manifest.flush()
            manifest_rows.append(row)
            if candidate:
                break
    os.replace(manifest_tmp, MANIFEST_PATH)

    complete = len(manifest_rows) == 11
    status_counts: dict[str, int] = {}
    for row in manifest_rows:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1
    summary = {
        "schema": "EQ11-CUBE-CAYLEY-summary-v1",
        "scope_id": "21.137/odd-prime-exponent-p2",
        "assignment_revision": 2,
        "family": "E_12 endpoint-equal rows with dim J_tau<=12",
        "selected_row_count": len(family),
        "rows_processed": len(manifest_rows),
        "complete_11_row_manifest": complete,
        "stopped_on_first_target_equal_candidate": candidate,
        "candidate_row": next((row for row in manifest_rows if row["status"] == "TARGET-EQUAL CANDIDATE"), None),
        "status_counts": status_counts,
        "selection_path": str(SELECTION_PATH),
        "selection_sha256": selection_hash,
        "manifest_path": str(MANIFEST_PATH),
        "manifest_sha256": sha256_file(MANIFEST_PATH),
        "elapsed_wall_seconds": time.time() - started,
        "active_assignment_answered": "candidate-pending-review" if candidate else "no",
        "limitations": "No-pass exhaustion covers only the eleven frozen E_12 rows, not the unrestricted target.",
    }
    write_json(SUMMARY_PATH, summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if candidate or complete else 2


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    self_test()
    if args.self_test:
        print("self-test: PASS")
        return 0
    return run()


if __name__ == "__main__":
    sys.exit(main())
