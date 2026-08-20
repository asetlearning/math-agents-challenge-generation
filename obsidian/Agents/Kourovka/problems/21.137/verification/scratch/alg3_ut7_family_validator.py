#!/usr/bin/env python3
"""Validator-authored checker for the frozen ALG3-UT7/F_12 certificate.

This file imports neither claimant implementation.  It represents full 7-by-7
matrices, grows the generated associative algebra by right multiplication, and
uses a fresh rank computation after each candidate word.  It then checks the
preserved manifest and every saved leading-layer witness.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter, deque
from pathlib import Path


P = 3
N = 7
MANIFEST = Path(
    "Agents/Kourovka/problems/21.137/runs/"
    "2026-08-17-r7-alg3-ut7-cube-image/manifest.jsonl"
)
POSITIONS = tuple((i, j) for i in range(N) for j in range(i + 1, N))
ZERO = tuple(tuple(0 for _ in range(N)) for _ in range(N))


def add(left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]):
    return tuple(
        tuple((left[i][j] + right[i][j]) % P for j in range(N))
        for i in range(N)
    )


def scale(coefficient: int, matrix: tuple[tuple[int, ...], ...]):
    return tuple(
        tuple((coefficient * matrix[i][j]) % P for j in range(N))
        for i in range(N)
    )


def multiply(left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]):
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(N)) % P
            for j in range(N)
        )
        for i in range(N)
    )


def power(matrix: tuple[tuple[int, ...], ...], exponent: int):
    result = matrix
    for _ in range(1, exponent):
        result = multiply(result, matrix)
    return result


def upper_vector(matrix: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(matrix[i][j] for i, j in POSITIONS)


def rank_mod3(vectors: list[tuple[int, ...]]) -> int:
    rows = [[entry % P for entry in vector] for vector in vectors]
    pivot_row = 0
    width = len(rows[0]) if rows else 0
    for column in range(width):
        pivot = None
        for index in range(pivot_row, len(rows)):
            if rows[index][column] % P:
                pivot = index
                break
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        if rows[pivot_row][column] == 2:
            rows[pivot_row] = [(2 * entry) % P for entry in rows[pivot_row]]
        for index in range(len(rows)):
            if index == pivot_row:
                continue
            coefficient = rows[index][column]
            if coefficient:
                rows[index] = [
                    (x - coefficient * y) % P
                    for x, y in zip(rows[index], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def matrix_from_edges(edges: tuple[int, ...]):
    rows = [[0 for _ in range(N)] for _ in range(N)]
    for index, value in enumerate(edges):
        rows[index][index + 1] = value % P
    return tuple(tuple(row) for row in rows)


S = matrix_from_edges((1, 1, 1, 1, 1, 1))


def algebra_dimension(tau: tuple[int, ...]) -> int:
    generators = (S, matrix_from_edges(tau))
    basis_matrices: list[tuple[tuple[int, ...], ...]] = []
    basis_vectors: list[tuple[int, ...]] = []
    frontier: deque[tuple[tuple[int, ...], ...]] = deque()

    def insert(candidate: tuple[tuple[int, ...], ...]) -> None:
        vector = upper_vector(candidate)
        if rank_mod3(basis_vectors + [vector]) > len(basis_vectors):
            basis_matrices.append(candidate)
            basis_vectors.append(vector)
            frontier.append(candidate)

    for generator in generators:
        insert(generator)
    while frontier:
        word = frontier.popleft()
        for generator in generators:
            insert(multiply(word, generator))
    return len(basis_matrices)


def matrix_code(matrix: tuple[tuple[int, ...], ...]) -> int:
    return sum(matrix[i][j] * (P**place) for place, (i, j) in enumerate(POSITIONS))


def leading_values(tau: tuple[int, ...]):
    t_matrix = matrix_from_edges(tau)
    values = {}
    for coefficients in itertools.product(range(P), repeat=2):
        a, b = coefficients
        value = power(add(scale(a, S), scale(b, t_matrix)), 3)
        values.setdefault(value, coefficients)
    return values


def main() -> None:
    lines = MANIFEST.read_text(encoding="utf-8").splitlines()
    assert len(lines) == P**6
    records = [json.loads(line) for line in lines]
    dimensions = Counter()
    statuses = Counter()
    retained = []

    assert power(S, 3) != ZERO
    assert power(S, 7) == ZERO

    for row_number, (tau_raw, record) in enumerate(
        zip(itertools.product(range(P), repeat=6), records), start=1
    ):
        tau = tuple(tau_raw)
        assert record["row_number"] == row_number
        assert tuple(record["tau"]) == tau

        dimension = algebra_dimension(tau)
        dimensions[dimension] += 1
        assert record["dim_J"] == dimension

        left_endpoint = tau[0] * tau[1] * tau[2] % P
        right_endpoint = tau[3] * tau[4] * tau[5] % P
        endpoint_pass = left_endpoint != right_endpoint
        assert record["endpoint_left_tau1tau2tau3"] == left_endpoint
        assert record["endpoint_right_tau4tau5tau6"] == right_endpoint
        assert record["endpoint_filter"] is endpoint_pass

        status = record["status"]
        statuses[status] += 1
        if not endpoint_pass or dimension > 12:
            assert status == "outside F_12"
            expected_reasons = []
            if not endpoint_pass:
                expected_reasons.append("endpoint product equality")
            if dimension > 12:
                expected_reasons.append("dim J > 12")
            assert record["outside_reasons"] == expected_reasons
            continue

        retained.append(tau)
        assert status == "leading-layer not additive"
        values_to_coefficients = leading_values(tau)
        value_set = set(values_to_coefficients)
        witness = record["leading_layer_witness"]
        assert witness["C_size"] == len(value_set)

        t_matrix = matrix_from_edges(tau)
        a, b = witness["v_coefficients_S_T"]
        c, d = witness["w_coefficients_S_T"]
        v_cube = power(add(scale(a, S), scale(b, t_matrix)), 3)
        w_cube = power(add(scale(c, S), scale(d, t_matrix)), 3)
        total = add(v_cube, w_cube)
        assert v_cube in value_set
        assert w_cube in value_set
        assert total not in value_set
        assert witness["v_cube_code"] == matrix_code(v_cube)
        assert witness["w_cube_code"] == matrix_code(w_cube)
        assert witness["sum_code"] == matrix_code(total)

    digest = hashlib.sha256(MANIFEST.read_bytes()).hexdigest()
    print(
        json.dumps(
            {
                "audit": "PASS",
                "manifest_sha256": digest,
                "rows": len(records),
                "dimension_distribution": dict(sorted(dimensions.items())),
                "status_counts": dict(sorted(statuses.items())),
                "retained_rows": len(retained),
                "retained_tau": retained,
                "leading_layer_survivors": 0,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
