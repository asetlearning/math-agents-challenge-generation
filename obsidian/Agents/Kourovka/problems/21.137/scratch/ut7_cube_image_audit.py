#!/usr/bin/env python3
"""Independent frozen-family audit for ut7_cube_image.py.

This checker does not import the primary implementation.  It uses the grading
of the strictly upper-triangular algebra: every word of length k in S,T lies
on the k-th superdiagonal.  It independently recomputes all 729 dimensions and
all leading-layer cube sets, then checks every manifest row and witness.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


P = 3
MANIFEST = Path(
    "Agents/Kourovka/problems/21.137/runs/"
    "2026-08-17-r7-alg3-ut7-cube-image/manifest.jsonl"
)
POSITIONS = tuple((i, j) for i in range(7) for j in range(i + 1, 7))
POS_INDEX = {position: index for index, position in enumerate(POSITIONS)}


def rank_mod3(rows: list[list[int]]) -> int:
    # Separate textbook echelon algorithm; it deliberately shares no RREF code
    # with the primary enumerator.
    matrix = [[entry % P for entry in row] for row in rows if any(x % P for x in row)]
    rank = 0
    width = len(matrix[0]) if matrix else 0
    for column in range(width):
        pivot = next((r for r in range(rank, len(matrix)) if matrix[r][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = 1 if matrix[rank][column] == 1 else 2
        matrix[rank] = [(inverse * x) % P for x in matrix[rank]]
        for r in range(rank + 1, len(matrix)):
            coefficient = matrix[r][column]
            if coefficient:
                matrix[r] = [
                    (x - coefficient * y) % P
                    for x, y in zip(matrix[r], matrix[rank])
                ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def graded_dimension(tau: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    generators = ((1, 1, 1, 1, 1, 1), tau)
    degree_ranks = []
    for degree in range(1, 7):
        word_rows = []
        for word in itertools.product((0, 1), repeat=degree):
            row = []
            for start in range(7 - degree):
                coefficient = 1
                for offset, letter in enumerate(word):
                    coefficient = (
                        coefficient * generators[letter][start + offset]
                    ) % P
                row.append(coefficient)
            word_rows.append(row)
        degree_ranks.append(rank_mod3(word_rows))
    return sum(degree_ranks), tuple(degree_ranks)


def leading_cube(coefficients: tuple[int, int], tau: tuple[int, ...]) -> tuple[int, ...]:
    a, b = coefficients
    edge = tuple((a + b * value) % P for value in tau)
    return tuple(
        (edge[i] * edge[i + 1] * edge[i + 2]) % P for i in range(4)
    )


def add4(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % P for x, y in zip(left, right))


def leading_set(tau: tuple[int, ...]) -> set[tuple[int, ...]]:
    return {
        leading_cube(coefficients, tau)
        for coefficients in itertools.product(range(P), repeat=2)
    }


def degree3_code(value: tuple[int, ...]) -> int:
    code = 0
    for i, coefficient in enumerate(value):
        code += coefficient * (P ** POS_INDEX[(i, i + 3)])
    return code


def main() -> None:
    lines = MANIFEST.read_text(encoding="utf-8").splitlines()
    assert len(lines) == P**6
    records = [json.loads(line) for line in lines]
    dimension_distribution: dict[int, int] = {}
    degree_rank_patterns: dict[tuple[int, ...], int] = {}
    retained = 0
    leading_rejects = 0

    for row_number, (tau_raw, record) in enumerate(
        zip(itertools.product(range(P), repeat=6), records), start=1
    ):
        tau = tuple(tau_raw)
        assert record["row_number"] == row_number
        assert tuple(record["tau"]) == tau

        dimension, degree_ranks = graded_dimension(tau)
        dimension_distribution[dimension] = dimension_distribution.get(dimension, 0) + 1
        degree_rank_patterns[degree_ranks] = degree_rank_patterns.get(degree_ranks, 0) + 1
        assert record["dim_J"] == dimension

        first = tau[0] * tau[1] * tau[2] % P
        second = tau[3] * tau[4] * tau[5] % P
        endpoint = first != second
        assert record["endpoint_left_tau1tau2tau3"] == first
        assert record["endpoint_right_tau4tau5tau6"] == second
        assert record["endpoint_filter"] is endpoint

        if not endpoint or dimension > 12:
            assert record["status"] == "outside F_12"
            continue

        retained += 1
        values = leading_set(tau)
        is_additive = all(add4(x, y) in values for x in values for y in values)
        assert not is_additive
        assert record["status"] == "leading-layer not additive"
        leading_rejects += 1

        witness = record["leading_layer_witness"]
        v_coefficients = tuple(witness["v_coefficients_S_T"])
        w_coefficients = tuple(witness["w_coefficients_S_T"])
        v_cube = leading_cube(v_coefficients, tau)
        w_cube = leading_cube(w_coefficients, tau)
        total = add4(v_cube, w_cube)
        assert v_cube in values and w_cube in values and total not in values
        assert witness["C_size"] == len(values)
        assert witness["v_cube_code"] == degree3_code(v_cube)
        assert witness["w_cube_code"] == degree3_code(w_cube)
        assert witness["sum_code"] == degree3_code(total)

    digest = hashlib.sha256(MANIFEST.read_bytes()).hexdigest()
    print(
        json.dumps(
            {
                "audit": "PASS",
                "rows": len(records),
                "manifest_sha256": digest,
                "dimension_distribution": {
                    str(key): value for key, value in sorted(dimension_distribution.items())
                },
                "degree_rank_patterns": {
                    str(key): value for key, value in sorted(degree_rank_patterns.items())
                },
                "retained_F12_rows": retained,
                "leading_layer_rejections": leading_rejects,
                "leading_layer_survivors": retained - leading_rejects,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
