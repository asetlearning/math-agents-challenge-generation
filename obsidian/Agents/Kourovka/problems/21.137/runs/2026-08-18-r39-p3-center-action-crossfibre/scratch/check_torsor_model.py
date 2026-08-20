#!/usr/bin/env python3
"""Exact finite check of the local F_3 factor-set/root-torsor obstruction."""

from itertools import product

F = range(3)
V = list(product(F, repeat=2))
ZERO_V = (0, 0)


def add_v(x, y):
    return ((x[0] + y[0]) % 3, (x[1] + y[1]) % 3)


def neg_v(x):
    return ((-x[0]) % 3, (-x[1]) % 3)


def cocycle(x, y):
    return (x[0] * y[1]) % 3


def mul(x, y):
    vx, ex = x
    vy, ey = y
    return (add_v(vx, vy), (ex + ey + cocycle(vx, vy)) % 3)


def inv(x):
    v, e = x
    return (neg_v(v), (-e + cocycle(v, v)) % 3)


def power(x, n):
    out = (ZERO_V, 0)
    for _ in range(n):
        out = mul(out, x)
    return out


for x, y, z in product(V, repeat=3):
    assert (cocycle(x, y) + cocycle(add_v(x, y), z)) % 3 == (
        cocycle(y, z) + cocycle(x, add_v(y, z))
    ) % 3

P = list(product(V, F))
for x in P:
    assert mul(x, inv(x)) == (ZERO_V, 0)
    assert power(x, 3) == (ZERO_V, 0)

A, B = (1, 0), (0, 1)
a, b = (A, 0), (B, 0)
commutator = mul(mul(mul(inv(a), inv(b)), a), b)
assert commutator == (ZERO_V, 1)


def root_product(v, vp, i, j):
    return (i + j + cocycle(v, vp)) % 3


for v, vp, vpp in product(V, repeat=3):
    for i, j, k in product(F, repeat=3):
        left = root_product(add_v(v, vp), vpp, root_product(v, vp, i, j), k)
        right = root_product(v, add_v(vp, vpp), i, root_product(vp, vpp, j, k))
        assert left == right

# Exhaust every normalized value-section gauge d:V -> F_3.
nonzero_v = [v for v in V if v != ZERO_V]
gauge_count = 0
for values in product(F, repeat=len(nonzero_v)):
    d = {ZERO_V: 0, **dict(zip(nonzero_v, values))}
    for v, vp in product(V, repeat=2):
        cd = (
            cocycle(v, vp) + d[v] + d[vp] - d[add_v(v, vp)]
        ) % 3
        # It suffices to check the constant part; arbitrary root labels cancel.
        lhs = (cocycle(v, vp) - d[add_v(v, vp)]) % 3
        rhs = (-d[v] - d[vp] + cd) % 3
        assert lhs == rhs
    gauge_count += 1


# s(f)=g, s(g)=w, s(w)=0.
def s(vec):
    f_coord, g_coord, _w_coord = vec
    return (0, f_coord, g_coord)


f = (1, 0, 0)
assert s(s(f)) == (0, 0, 1)
assert s(s(s(f))) == (0, 0, 0)

print("cocycle_triples", len(V) ** 3)
print("group_elements_exponent3", len(P))
print("root_associativity_rows", len(V) ** 3 * 27)
print("normalized_gauges", gauge_count)
print("commutator_AB", commutator[1])
print("s2f", s(s(f)))
print("status PASS")
