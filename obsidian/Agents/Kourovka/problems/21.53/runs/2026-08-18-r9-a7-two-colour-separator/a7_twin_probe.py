#!/usr/bin/env python3
"""Cheap exact probe for two-colour twin vertices in the A7 class model."""

from itertools import combinations

from a7_inventory import compose, double_transposition, perm_order


vertices = set()
for support in combinations(range(7), 4):
    a, b, c, d = support
    vertices.add(double_transposition(a, b, c, d))
    vertices.add(double_transposition(a, c, b, d))
    vertices.add(double_transposition(a, d, b, c))
vertices = sorted(vertices)
n = len(vertices)

matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j] = matrix[j][i] = perm_order(compose(vertices[i], vertices[j]))

twins = []
for u in range(n):
    for v in range(u + 1, n):
        if all(
            ((matrix[u][w] == 2) == (matrix[v][w] == 2))
            and ((matrix[u][w] == 3) == (matrix[v][w] == 3))
            for w in range(n)
            if w not in (u, v)
        ):
            twins.append((u, v, matrix[u][v]))

print(f"VERTICES={n}")
print(f"CANDIDATE_VERTEX_TRANSPOSITIONS_CHECKED={n*(n-1)//2}")
print(f"TWO_COLOUR_TWIN_COUNT={len(twins)}")
print(f"TWO_COLOUR_TWINS={twins}")
print("TWIN_PROBE_STATUS=PASS")
