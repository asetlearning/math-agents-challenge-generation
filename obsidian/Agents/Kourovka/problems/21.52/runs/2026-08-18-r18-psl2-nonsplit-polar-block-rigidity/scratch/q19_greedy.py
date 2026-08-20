#!/usr/bin/env python3
"""Deterministic diagnostic: search for large noncollinear split-pair cliques at q=19."""

import random

p = 19


def canon(v):
    for x in v:
        if x % p:
            s = pow(x, p - 2, p)
            return tuple(s * y % p for y in v)
    raise ValueError


def qform(v):
    a, b, c = v
    return (a * a + b * c) % p


def beta(x, y):
    a, b, c = x
    d, e, f = y
    return (2 * a * d + b * f + c * e) % p


sq = {x * x % p for x in range(1, p)}
pts = sorted({canon((a, b, c)) for a in range(p) for b in range(p) for c in range(p) if (a, b, c) != (0, 0, 0)})
D = [v for v in pts if qform(v) not in sq and qform(v)]
n = len(D)
orth = [0] * n
for i, x in enumerate(D):
    for j, y in enumerate(D):
        if i != j and beta(x, y) == 0:
            orth[i] |= 1 << j
H = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        if not orth[i] & orth[j]:
            H[i] |= 1 << j
            H[j] |= 1 << i


def det3(x, y, z):
    return (x[0] * (y[1] * z[2] - y[2] * z[1]) - x[1] * (y[0] * z[2] - y[2] * z[0]) + x[2] * (y[0] * z[1] - y[1] * z[0])) % p


rng = random.Random(2152)
best = []
best_noncol = []
for _ in range(20000):
    v = rng.randrange(n)
    clique = [v]
    cand = H[v]
    while cand:
        ids = [i for i in range(n) if cand >> i & 1]
        # Prefer high remaining degree, with seeded random tie-breaking.
        rng.shuffle(ids)
        w = max(ids, key=lambda i: (cand & H[i]).bit_count())
        clique.append(w)
        cand &= H[w]
    if len(clique) > len(best):
        best = clique
    noncol = len(clique) < 3 or any(det3(D[clique[0]], D[clique[1]], D[z]) for z in clique[2:])
    if noncol and len(clique) > len(best_noncol):
        best_noncol = clique
print("q", p, "D", n, "orth_degree_set", sorted({x.bit_count() for x in orth}))
print("best", len(best), "best_noncollinear", len(best_noncol))
print("best_noncollinear_points", [D[i] for i in best_noncol])


def color_sort(P):
    order, bounds = [], []
    U = P
    colour = 0
    while U:
        colour += 1
        Q = U
        while Q:
            bit = Q & -Q
            v = bit.bit_length() - 1
            order.append(v)
            bounds.append(colour)
            U &= ~bit
            Q &= ~bit
            Q &= ~H[v]
    return order, bounds


exact_best = best[:]


def expand(C, P):
    global exact_best
    order, bounds = color_sort(P)
    for idx in range(len(order) - 1, -1, -1):
        if len(C) + bounds[idx] <= len(exact_best):
            return
        v = order[idx]
        expand(C + [v], P & H[v])
        P &= ~(1 << v)
        if len(C) + 1 > len(exact_best):
            exact_best = C + [v]


expand([], (1 << n) - 1)
print("exact_maximum", len(exact_best), "collinear", not any(det3(D[exact_best[0]], D[exact_best[1]], D[z]) for z in exact_best[2:]))

target_count = 0
target_noncol = 0


def enumerate_target(C, P):
    global target_count, target_noncol
    if len(C) == len(exact_best):
        target_count += 1
        if any(det3(D[C[0]], D[C[1]], D[z]) for z in C[2:]):
            target_noncol += 1
        return
    order, bounds = color_sort(P)
    for idx in range(len(order) - 1, -1, -1):
        if len(C) + bounds[idx] < len(exact_best):
            return
        v = order[idx]
        enumerate_target(C + [v], P & H[v])
        P &= ~(1 << v)


enumerate_target([], (1 << n) - 1)
print("maximum_cliques", target_count, "maximum_noncollinear", target_noncol)
assert n == 171
assert {x.bit_count() for x in orth} == {10}
assert {x.bit_count() for x in H} == {80}
assert len(exact_best) == 9
assert target_count == 190 and target_noncol == 0
print("all_exact_search_assertions", "PASS")
