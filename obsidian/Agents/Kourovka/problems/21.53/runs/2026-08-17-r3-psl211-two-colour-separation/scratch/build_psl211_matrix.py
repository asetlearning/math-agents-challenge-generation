#!/usr/bin/env python3
"""Deterministic PSL(2,11) quotient model and involution colour matrix.

Elements are canonical representatives of determinant-one 2x2 matrices over
F_11 modulo the central pair {+I,-I}.  No external group library is used.
"""

from __future__ import annotations

import csv
import json
import platform
import sys
from collections import Counter, deque
from pathlib import Path

Q = 11
HERE = Path(__file__).resolve().parent
IDENTITY = (1, 0, 0, 1)


def neg(a: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return tuple((-x) % Q for x in a)  # type: ignore[return-value]


def canonical(a: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    b = neg(a)
    return min(a, b)


def multiply(
    a: tuple[int, int, int, int], b: tuple[int, int, int, int]
) -> tuple[int, int, int, int]:
    a00, a01, a10, a11 = a
    b00, b01, b10, b11 = b
    return canonical(
        (
            (a00 * b00 + a01 * b10) % Q,
            (a00 * b01 + a01 * b11) % Q,
            (a10 * b00 + a11 * b10) % Q,
            (a10 * b01 + a11 * b11) % Q,
        )
    )


def inverse(a: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    a00, a01, a10, a11 = a
    return canonical((a11, (-a01) % Q, (-a10) % Q, a00))


def element_order(a: tuple[int, int, int, int]) -> int:
    x = IDENTITY
    for n in range(1, 661):
        x = multiply(x, a)
        if x == IDENTITY:
            return n
    raise AssertionError(f"order bound failed for {a}")


def generated_subgroup(
    generators: list[tuple[int, int, int, int]],
) -> set[tuple[int, int, int, int]]:
    gens = sorted(set(generators + [inverse(x) for x in generators]))
    seen = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        x = queue.popleft()
        for g in gens:
            y = multiply(x, g)
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen


def prime_factors(n: int) -> list[int]:
    ans: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ans.append(n)
    return ans


def main() -> None:
    sl2 = []
    for a in range(Q):
        for b in range(Q):
            for c in range(Q):
                for d in range(Q):
                    if (a * d - b * c) % Q == 1:
                        sl2.append((a, b, c, d))
    group = sorted({canonical(x) for x in sl2})
    group_set = set(group)
    assert len(sl2) == Q * (Q * Q - 1) == 1320
    assert len(group) == 660
    assert all(multiply(x, inverse(x)) == IDENTITY for x in group)

    u = canonical((1, 1, 0, 1))
    s = canonical((0, -1 % Q, 1, 0))
    generated = generated_subgroup([u, s])
    assert generated == group_set
    assert multiply(u, s) != multiply(s, u)

    # Direct finite simplicity check: every nonidentity conjugacy class normally
    # generates the whole enumerated group.
    unseen = set(group)
    classes: list[list[tuple[int, int, int, int]]] = []
    while unseen:
        x = min(unseen)
        orbit = sorted(
            {multiply(multiply(h, x), inverse(h)) for h in group}
        )
        assert set(orbit) <= unseen
        unseen.difference_update(orbit)
        classes.append(orbit)
    classes.sort(key=lambda cls: (element_order(cls[0]), len(cls), cls[0]))
    normal_closure_sizes = []
    for cls in classes:
        if cls == [IDENTITY]:
            normal_closure_sizes.append(1)
        else:
            normal_closure_sizes.append(len(generated_subgroup(cls)))
            assert normal_closure_sizes[-1] == len(group)

    involutions = sorted(
        x for x in group if x != IDENTITY and multiply(x, x) == IDENTITY
    )
    assert len(involutions) == 55
    involution_classes = [cls for cls in classes if element_order(cls[0]) == 2]
    assert len(involution_classes) == 1
    assert involution_classes[0] == involutions
    centralizer_size = sum(
        multiply(h, involutions[0]) == multiply(involutions[0], h) for h in group
    )
    assert centralizer_size == 12
    assert len(group) // centralizer_size == len(involutions)

    orders = {x: element_order(x) for x in group}
    n = len(involutions)
    matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    edge_counts: Counter[int] = Counter()
    valencies = [Counter() for _ in range(n)]
    edges: list[tuple[int, int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            colour = orders[multiply(involutions[i], involutions[j])]
            matrix[i][j] = matrix[j][i] = colour
            edge_counts[colour] += 1
            valencies[i][colour] += 1
            valencies[j][colour] += 1
            edges.append((i + 1, j + 1, colour))
    assert len(edges) == n * (n - 1) // 2 == 1485
    assert all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n))
    occurring_colours = sorted(edge_counts)
    common_valency = {
        colour: valencies[0][colour] for colour in occurring_colours
    }
    assert all(
        {colour: row[colour] for colour in occurring_colours} == common_valency
        for row in valencies
    )
    assert sum(common_valency.values()) == n - 1
    assert all(edge_counts[c] * 2 == n * common_valency[c] for c in occurring_colours)

    with (HERE / "vertices.tsv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow(["index", "a00", "a01", "a10", "a11"])
        for i, a in enumerate(involutions, start=1):
            writer.writerow([i, *a])

    with (HERE / "product_order_matrix.csv").open(
        "w", newline="", encoding="utf-8"
    ) as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["vertex", *range(1, n + 1)])
        for i, row in enumerate(matrix, start=1):
            writer.writerow([i, *row])

    with (HERE / "unordered_edges.tsv").open(
        "w", newline="", encoding="utf-8"
    ) as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow(["i", "j", "product_order"])
        writer.writerows(edges)

    # Frozen GAP-readable copy of the same complete matrix.  The automorphism
    # comparison script consumes this file and does not reconstruct group data.
    with (HERE / "matrix_data.g").open("w", encoding="utf-8") as f:
        f.write("PSL211ProductOrderMatrix := [\n")
        for row_number, row in enumerate(matrix):
            suffix = "," if row_number + 1 < len(matrix) else ""
            f.write("  " + repr(row).replace(" ", "") + suffix + "\n")
        f.write("];\n")

    class_summary = [
        {
            "representative": list(cls[0]),
            "element_order": element_order(cls[0]),
            "class_size": len(cls),
            "normal_closure_size": normal_closure_sizes[i],
        }
        for i, cls in enumerate(classes)
    ]
    factors = prime_factors(len(group))
    summary = {
        "model": "SL(2,11)/{+I,-I} with lexicographically canonical representatives",
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "field_order": Q,
        "sl2_order": len(sl2),
        "quotient_order": len(group),
        "prime_factorization": {"2": 2, "3": 1, "5": 1, "11": 1},
        "distinct_prime_divisors": factors,
        "second_smallest_distinct_prime": factors[1],
        "generators": {"u": list(u), "s": list(s)},
        "generated_subgroup_order": len(generated),
        "generators_noncommute": multiply(u, s) != multiply(s, u),
        "conjugacy_classes": class_summary,
        "every_nonidentity_class_normal_closure_order": len(group),
        "involution_count": len(involutions),
        "involution_class_count": len(involution_classes),
        "involution_class_sizes": [len(cls) for cls in involution_classes],
        "involution_centralizer_order": centralizer_size,
        "vertex_order": "lexicographic canonical matrix tuple",
        "matrix_diagonal": 1,
        "unordered_pair_count": len(edges),
        "occurring_edge_colours": occurring_colours,
        "colour_count": len(occurring_colours),
        "valency_by_colour": {str(k): common_valency[k] for k in occurring_colours},
        "edge_count_by_colour": {str(k): edge_counts[k] for k in occurring_colours},
        "aut_t_vacuity": "For every positive t not in occurring_edge_colours, Aut_t is S_55.",
    }
    with (HERE / "summary.json").open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, sort_keys=True)
        f.write("\n")

    print("PSL211_MATRIX_BUILD_OK")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
