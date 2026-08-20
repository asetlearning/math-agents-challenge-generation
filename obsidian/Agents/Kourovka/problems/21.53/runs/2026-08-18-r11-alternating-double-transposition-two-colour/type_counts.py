#!/usr/bin/env python3
"""Small exact checker for the double-transposition overlay/count table.

No automorphism package is used.  Vertices are two-edge matchings on range(n).
For canonical x,y representatives this records exact product orders and the
four counts #{z: ord(xz)=i, ord(yz)=j}, i,j in {2,3}.
"""

from itertools import combinations
from math import gcd


def vertices(n):
    out = []
    for support in combinations(range(n), 4):
        a, b, c, d = support
        out.extend([
            ((a, b), (c, d)),
            ((a, c), (b, d)),
            ((a, d), (b, c)),
        ])
    return out


def perm(v, n):
    p = list(range(n))
    for a, b in v:
        p[a], p[b] = b, a
    return p


def product_order(v, w, n):
    pv, pw = perm(v, n), perm(w, n)
    # Composition pv * pw; order is independent of reversing two involutions.
    q = [pv[pw[i]] for i in range(n)]
    seen = [False] * n
    ans = 1
    for i in range(n):
        if not seen[i]:
            j, length = i, 0
            while not seen[j]:
                seen[j] = True
                length += 1
                j = q[j]
            ans = ans * length // gcd(ans, length)
    return ans


REPS = {
    "R4": (((0, 1), (2, 3)), ((0, 4), (1, 5))),
    "R5": (((0, 1), (2, 3)), ((0, 4), (1, 2))),
    "R6": (((0, 1), (2, 3)), ((0, 4), (5, 6))),
}


for n in range(7, 16):
    vs = vertices(n)
    print("n", n, "vertices", len(vs))
    for name, (x, y) in REPS.items():
        assert product_order(x, y, n) == int(name[1:])
        counts = {}
        for i in (2, 3):
            for j in (2, 3):
                counts[i, j] = sum(
                    product_order(x, z, n) == i
                    and product_order(y, z, n) == j
                    for z in vs
                )
        print(name, counts)
