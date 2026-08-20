#!/usr/bin/env python3
"""Build the A6 double-transposition product-order scheme deterministically.

No third-party modules are used.  The output includes a complete matrix and two
vertex-coloured incidence graphs for dreadnaut: one encoding only colours 2,3,
and one encoding every occurring colour separately.
"""

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter
from pathlib import Path


def compose(left, right):
    """Return left after right, on zero-based points."""
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(p):
    ans = [0] * len(p)
    for i, image in enumerate(p):
        ans[image] = i
    return tuple(ans)


def permutation_order(p):
    seen = [False] * len(p)
    answer = 1
    for i in range(len(p)):
        if seen[i]:
            continue
        length = 0
        j = i
        while not seen[j]:
            seen[j] = True
            length += 1
            j = p[j]
        answer = math.lcm(answer, length)
    return answer


def is_even(p):
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return inversions % 2 == 0


def from_pairs(n, pairs):
    p = list(range(n))
    for a, b in pairs:
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def cycle_string(p):
    seen = [False] * len(p)
    cycles = []
    for i in range(len(p)):
        if seen[i] or p[i] == i:
            seen[i] = True
            continue
        cyc = []
        j = i
        while not seen[j]:
            seen[j] = True
            cyc.append(j + 1)
            j = p[j]
        cycles.append("(" + " ".join(map(str, cyc)) + ")")
    return "".join(cycles) or "()"


def double_transpositions(n):
    assert n == 6
    answer = set()
    for support in itertools.combinations(range(n), 4):
        a, b, c, d = support
        matchings = [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]
        for matching in matchings:
            answer.add(from_pairs(n, matching))
    return sorted(answer)


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def write_dreadnaut(path, matrix, labels):
    vertex_count = len(matrix)
    auxiliary = []
    cells = [(0, vertex_count - 1, "vertices")]
    next_vertex = vertex_count
    for label in labels:
        first = next_vertex
        for i in range(vertex_count):
            for j in range(i + 1, vertex_count):
                if matrix[i][j] == label:
                    auxiliary.append((next_vertex, i, j, label))
                    next_vertex += 1
        cells.append((first, next_vertex - 1, f"colour-{label}-edges"))

    adjacency = [set() for _ in range(next_vertex)]
    for aux, i, j, _label in auxiliary:
        adjacency[i].add(aux)
        adjacency[aux].add(i)
        adjacency[j].add(aux)
        adjacency[aux].add(j)

    lines = ["As", "$=0", f"n={next_vertex}", "g"]
    for v in range(next_vertex):
        # Each undirected edge is entered exactly once.
        neighbours = sorted(u for u in adjacency[v] if u > v)
        ending = ";" if v + 1 < next_vertex else "."
        lines.append(f"{v}: {' '.join(map(str, neighbours))}{ending}")
    partition = "|".join(
        str(first) if first == last else f"{first}:{last}"
        for first, last, _name in cells
    )
    lines.extend([f"f=[{partition}]", "+a", "+p", "x", "q"])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "dreadnaut_order": next_vertex,
        "auxiliary_vertices": len(auxiliary),
        "incidence_edges": 2 * len(auxiliary),
        "partition_cells": [
            {"first": first, "last": last, "meaning": name}
            for first, last, name in cells
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--params", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    params_path = Path(args.params)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    params = json.loads(params_path.read_text(encoding="utf-8"))

    n = params["ambient_degree"]
    vertices = double_transpositions(n)
    assert len(vertices) == 45
    identity = tuple(range(n))
    assert all(is_even(x) and x != identity and compose(x, x) == identity for x in vertices)

    alternating_group = [p for p in itertools.permutations(range(n)) if is_even(p)]
    assert len(alternating_group) == math.factorial(n) // 2 == 360
    base = vertices[0]
    orbit = {
        compose(compose(g, base), inverse(g))
        for g in alternating_group
    }
    assert orbit == set(vertices), "D must be one A6 conjugacy class"

    matrix = []
    for left in vertices:
        matrix.append([permutation_order(compose(left, right)) for right in vertices])
    assert all(matrix[i][i] == 1 for i in range(45))
    assert all(matrix[i][j] == matrix[j][i] for i in range(45) for j in range(45))

    colours = sorted({matrix[i][j] for i in range(45) for j in range(i + 1, 45)})
    expected = params["full_colours_expected"]
    assert colours == expected, (colours, expected)
    degree_profiles = []
    for i in range(45):
        degree_profiles.append(dict(sorted(Counter(matrix[i][j] for j in range(45) if j != i).items())))
    assert all(profile == degree_profiles[0] for profile in degree_profiles)
    edge_counts = {
        str(label): sum(matrix[i][j] == label for i in range(45) for j in range(i + 1, 45))
        for label in colours
    }

    vertices_path = out / "a6_vertices.json"
    matrix_path = out / "a6_product_order_matrix.json"
    vertices_path.write_text(
        json.dumps(
            [
                {"index": i, "images_zero_based": list(p), "cycle_notation_one_based": cycle_string(p)}
                for i, p in enumerate(vertices)
            ],
            indent=2,
            sort_keys=True,
        ) + "\n",
        encoding="utf-8",
    )
    matrix_path.write_text(json.dumps(matrix, separators=(",", ":")) + "\n", encoding="utf-8")

    two_path = out / "a6_two_colour.dre"
    full_path = out / "a6_full_colour.dre"
    two_encoding = write_dreadnaut(two_path, matrix, params["selected_colours"])
    full_encoding = write_dreadnaut(full_path, matrix, colours)

    summary = {
        "group": params["group"],
        "group_order": len(alternating_group),
        "group_prime_divisors": [2, 3, 5],
        "second_smallest_prime": 3,
        "class": params["class"],
        "class_size": len(vertices),
        "one_A6_conjugacy_orbit": True,
        "occurring_product_orders": colours,
        "common_vertex_degrees_by_colour": {str(k): v for k, v in degree_profiles[0].items()},
        "unordered_edge_counts_by_colour": edge_counts,
        "two_colour_encoding": two_encoding,
        "full_colour_encoding": full_encoding,
        "files": {
            "parameters": {"path": str(params_path), "sha256": sha256(params_path)},
            "vertices": {"path": str(vertices_path), "sha256": sha256(vertices_path)},
            "matrix": {"path": str(matrix_path), "sha256": sha256(matrix_path)},
            "two_colour_dreadnaut_input": {"path": str(two_path), "sha256": sha256(two_path)},
            "full_colour_dreadnaut_input": {"path": str(full_path), "sha256": sha256(full_path)},
        },
    }
    (out / "a6_build_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
