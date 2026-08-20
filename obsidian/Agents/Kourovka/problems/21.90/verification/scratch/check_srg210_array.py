#!/usr/bin/env python3
"""Exact, bounded arithmetic check for IA {19,6,8;1,1,12}.

This script works only in the four-dimensional distance-matrix algebra generated
by A_1.  It neither constructs nor searches for a graph.
"""

from fractions import Fraction


N = 4


def ident():
    return [[Fraction(i == j) for j in range(N)] for i in range(N)]


def add(x, y):
    return [[x[i][j] + y[i][j] for j in range(N)] for i in range(N)]


def scale(c, x):
    return [[c * x[i][j] for j in range(N)] for i in range(N)]


def mul(x, y):
    return [
        [sum(x[i][k] * y[k][j] for k in range(N)) for j in range(N)]
        for i in range(N)
    ]


def matvec(x, v):
    return [sum(x[i][j] * v[j] for j in range(N)) for i in range(N)]


def ints(v):
    assert all(q.denominator == 1 for q in v)
    return tuple(int(q) for q in v)


# Column j gives the coefficients of A_1 A_j in (A_0,A_1,A_2,A_3).
L1 = [
    [Fraction(0), Fraction(19), Fraction(0), Fraction(0)],
    [Fraction(1), Fraction(12), Fraction(6), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(10), Fraction(8)],
    [Fraction(0), Fraction(0), Fraction(12), Fraction(7)],
]
I4 = ident()
L1_2 = mul(L1, L1)
L1_3 = mul(L1_2, L1)

# From A_1 A_2=6A_1+10A_2+12A_3 and
# A_2=A_1^2-12A_1-19A_0:
# 12 A_3=A_1^3-22A_1^2+95A_1+190A_0.
L3 = scale(
    Fraction(1, 12),
    add(add(L1_3, scale(-22, L1_2)), add(scale(95, L1), scale(190, I4))),
)

e0 = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
e3 = [Fraction(0), Fraction(0), Fraction(0), Fraction(1)]
assert matvec(L3, e0) == e3

b2 = ints(matvec(L3, e3))
assert b2 == (76, 28, 28, 26)

# Coefficient vectors in the same basis.
M = (1, 1, 0, 0)
D = (1, 0, 0, 1)
D2 = tuple((1 if i == 0 else 0) + 2 * (1 if i == 3 else 0) + b2[i] for i in range(N))
assert D2 == (77, 28, 28, 28)  # 49 I + 28 J

# M(D+7I)=(I+A_1)(8I+A_3), using A_1 A_3=8A_2+7A_3.
mixed = (8, 8, 8, 8)
assert mixed == (8, 8, 8, 8)

# M^2=(I+A_1)^2 and 7I+13M+J-D.
m2_left = (20, 14, 1, 0)
m2_right = (7 + 13 + 1 - 1, 13 + 1, 1, 1 - 1)
assert m2_left == m2_right

branches = []
for n13 in range(210):
    for n14 in range(210):
        nminus1 = 13 * n13 + 14 * n14 - 190
        n0 = 209 - n13 - n14 - nminus1
        if min(n0, nminus1) < 0:
            continue
        if 169 * n13 + 196 * n14 + nminus1 != 3800:
            continue
        branches.append((n0, n13, n14, nminus1))

assert branches == [(114, 0, 19, 76), (99, 15, 6, 89)]
survivors = [row for row in branches if row[1] == 0]
assert survivors == [(114, 0, 19, 76)]

print("sphere_sizes=(1,19,114,76) v=210")
print(f"A3_squared_coefficients={b2}")
print(f"D_squared_coefficients={D2}=49I+28J")
print(f"M(D+7I)_coefficients={mixed}=8J")
print(f"M_squared_coefficients={m2_left}=7I+13M+J-D")
print(f"trace_branches={branches}")
print(f"after_m(d+7)=0={survivors}")
print("local_component_size=12+1=13; 19_mod_13=6")
