#!/usr/bin/env python3
"""Small exact-arithmetic sanity checker for the 21.90 Type-II(ii) audit.

This is deliberately bounded and uses only Python integers/Fraction.  Universal
claims in the verification note are proved by hand; this checker independently
recovers the product coefficients from the proposed eigenmatrix on representative
solutions and catches transcription/sign errors.
"""

from fractions import Fraction
from math import isqrt


def matmul(a, b):
    return [[sum(a[i][z] * b[z][j] for z in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def solve(a, b):
    aug = [[Fraction(x) for x in row] + [Fraction(y)]
           for row, y in zip(a, b)]
    n = len(aug)
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row == col:
                continue
            scale = aug[row][col]
            aug[row] = [x - scale * y for x, y in zip(aug[row], aug[col])]
    return [row[-1] for row in aug]


def data(x, w, u):
    assert u * u == x * (w + 1) + 1
    h = x * w + 1
    t = u * w
    a = w * h - 1
    k = w * h * (u + 1) - 1
    v = 1 + k + k * t + k * w
    p = [
        [1, k, k * t, k * w],
        [1, w * (h + u) - 1, -u * w, -w * h],
        [1, -1, -u * w, u * w],
        [1, -h, w * u * u, -w * h],
    ]
    return h, t, a, k, v, p


def product_coefficients(p):
    out = {}
    for i in range(4):
        for j in range(i, 4):
            rhs = [row[i] * row[j] for row in p]
            coeff = solve(p, rhs)
            assert all(x.denominator == 1 for x in coeff)
            out[(i, j)] = tuple(int(x) for x in coeff)
    return out


samples = [(2, 3, 3), (8, 2, 5), (1, 2, 2), (21, 2, 8)]
print("representative even-xw solutions:", samples)
for x, w, u in samples:
    h, t, a, k, v, p = data(x, w, u)
    square = matmul(p, p)
    target = [[v if i == j else 0 for j in range(4)] for i in range(4)]
    assert square == target
    products = product_coefficients(p)
    zeros = sorted((i, j, ell) for (i, j), row in products.items()
                   for ell in range(1, 4)
                   if i and j and row[ell] == 0)
    print(f"  (x,w,u)=({x},{w},{u}): P^2=vI; multiplicities=(1,{k},{k*t},{k*w}); "
          f"nonzero-index zeros={zeros}")

x, w, u = samples[0]
h, t, a, k, v, p = data(x, w, u)
products = product_coefficients(p)
print("recovered products for (x,w,u)=(2,3,3):")
for pair in ((1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)):
    print(f"  p_{pair[0]}{pair[1]}^h={products[pair]}")

for r in range(11):
    w = 7
    u = 8 * r + 3
    x = 8 * r * r + 6 * r + 1
    assert x % 2 == w % 2 == 1
    assert x * (w + 1) + 1 == u * u
print("odd family r=0..10: square equation and oddness pass")

bounded = []
for w in range(1, 31):
    for x in range(1, 101):
        square = x * (w + 1) + 1
        u = isqrt(square)
        if u * u == square and (x * w) % 2 == 0:
            bounded.append((x, w, u))
            h, t, a, k, v, p = data(x, w, u)
            assert matmul(p, p) == [[v if i == j else 0 for j in range(4)]
                                    for i in range(4)]
            assert (v % 2) == 0
            if u % 2:
                assert all(z % 2 for z in (k, -h, u, -h))
                parity_count = v
            else:
                assert w % 2 == 0 and x % 2 == 1
                parity_count = v - k * t
            assert parity_count % 2 == 0
print(f"bounded parity/P sanity screen: {len(bounded)} solutions, zero failures")
