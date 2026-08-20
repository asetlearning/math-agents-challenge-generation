#!/usr/bin/env python3
"""Diagnostic only: q=11 internal-point no-common-neighbour cliques."""

from collections import Counter, defaultdict

p = 11


def inv(a):
    return pow(a, p - 2, p)


def canon(v):
    for x in v:
        if x % p:
            s = inv(x % p)
            return tuple((s * y) % p for y in v)
    raise ValueError("zero")


def qform(v):
    a, b, c = v
    return (a * a + b * c) % p


def beta(x, y):
    a, b, c = x
    d, e, f = y
    return (2 * a * d + b * f + c * e) % p


sq = {x * x % p for x in range(1, p)}
pts = sorted({canon((a, b, c)) for a in range(p) for b in range(p) for c in range(p) if (a, b, c) != (0, 0, 0)})
D = [v for v in pts if qform(v) not in sq and qform(v) != 0]
E = [v for v in pts if qform(v) in sq and qform(v) != 0]
n = len(D)
orth = [0] * n
for i, x in enumerate(D):
    for j, y in enumerate(D):
        if i != j and beta(x, y) == 0:
            orth[i] |= 1 << j

# H joins pairs with no common colour-2 neighbour.
H = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        if orth[i] & orth[j] == 0:
            H[i] |= 1 << j
            H[j] |= 1 << i


def bronk(R, P, X):
    if not P and not X:
        yield R
        return
    union = P | X
    if union:
        u = max((i for i in range(n) if union >> i & 1), key=lambda i: (P & H[i]).bit_count())
        cand = P & ~H[u]
    else:
        cand = P
    while cand:
        bit = cand & -cand
        v = bit.bit_length() - 1
        yield from bronk(R | bit, P & H[v], X & H[v])
        P &= ~bit
        X |= bit
        cand &= ~bit


maximal = list(bronk(0, (1 << n) - 1, 0))


def det3(x, y, z):
    return (
        x[0] * (y[1] * z[2] - y[2] * z[1])
        - x[1] * (y[0] * z[2] - y[2] * z[0])
        + x[2] * (y[0] * z[1] - y[1] * z[0])
    ) % p


def collinear(mask):
    ids = [i for i in range(n) if mask >> i & 1]
    if len(ids) < 3:
        return True
    x, y = D[ids[0]], D[ids[1]]
    return all(det3(x, y, D[k]) == 0 for k in ids[2:])


stats = Counter((m.bit_count(), collinear(m)) for m in maximal)
print("q", p, "D", n, "E", len(E), "orth_degree_set", sorted({x.bit_count() for x in orth}), "split_degree_set", sorted({x.bit_count() for x in H}))
print("maximal_clique_stats", sorted(stats.items()))
top = max(m.bit_count() for m in maximal)
print("maximum", top, "count", sum(m.bit_count() == top for m in maximal))
for m in maximal:
    if m.bit_count() == top and not collinear(m):
        print("noncollinear_top", [D[i] for i in range(n) if m >> i & 1])
        break

five = [m for m in maximal if m.bit_count() == 5]
tri = [m for m in maximal if m.bit_count() == 3]
polar_blocks = {
    sum(1 << i for i, x in enumerate(D) if beta(e, x) == 0)
    for e in E
}
collinear_five = {m for m in five if collinear(m)}
assert len(D) == 55 and len(E) == 66
assert {x.bit_count() for x in orth} == {6}
assert {x.bit_count() for x in H} == {24}
assert len(polar_blocks) == 66 and {m.bit_count() for m in polar_blocks} == {5}
assert polar_blocks == collinear_five
sig5 = defaultdict(Counter)
for m in five:
    sig = tuple(Counter((m & z).bit_count() for z in five if z != m)[k] for k in range(1, 5))
    sig5[collinear(m)][sig] += 1
print("five_intersection_signatures", {k: dict(v) for k, v in sig5.items()})
sig3 = defaultdict(Counter)
for m in five:
    sig = tuple(Counter((m & z).bit_count() for z in tri)[k] for k in range(1, 4))
    sig3[collinear(m)][sig] += 1
print("triangle_intersection_signatures", {k: dict(v) for k, v in sig3.items()})


def mmul(A, B):
    return (
        (A[0] * B[0] + A[1] * B[2]) % p,
        (A[0] * B[1] + A[1] * B[3]) % p,
        (A[2] * B[0] + A[3] * B[2]) % p,
        (A[2] * B[1] + A[3] * B[3]) % p,
    )


def normalize(v):
    target = (-inv(qform(v))) % p
    lam = next(x for x in range(1, p) if x * x % p == target)
    a, b, c = ((lam * z) % p for z in v)
    return (a, b, c, -a % p)


M = [normalize(v) for v in D]


def porder(A):
    z = (1, 0, 0, 1)
    for k in range(1, 2 * (p + 1) + 1):
        z = mmul(z, A)
        if z == (1, 0, 0, 1) or z == (-1 % p, 0, 0, -1 % p):
            return k
    raise RuntimeError(A)


orders = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        orders[i][j] = orders[j][i] = porder(mmul(M[i], M[j]))

colour_sigs = defaultdict(Counter)
for m in five:
    ids = [i for i in range(n) if m >> i & 1]
    sig = tuple(sorted(Counter(orders[i][j] for z, i in enumerate(ids) for j in ids[z + 1 :]).items()))
    colour_sigs[collinear(m)][sig] += 1
print("induced_colour_multisets", {k: dict(v) for k, v in colour_sigs.items()})
assert stats == Counter({(3, False): 440, (5, False): 165, (5, True): 66})
assert sig5[True] == Counter({(65, 10, 5, 0): 66})
assert sig5[False] == Counter({(70, 8, 2, 2): 165})
assert colour_sigs[True] == Counter({((5, 10),): 66})
assert colour_sigs[False] == Counter({((5, 10),): 165})
print("all_assertions", "PASS")
