#!/usr/bin/env python3
"""Independent finite-field checks for the 21.137 rank-four review.

This enumerates Sp_4(3) through symplectic bases (not through the claimant's
argument) and independently enumerates the relevant 3-by-3 matrix centralizer.
"""

from itertools import product

P = 3


def omega(x, y):
    # Basis order e1,e2,f1,f2.
    return (x[0] * y[2] + x[1] * y[3]
            - x[2] * y[0] - x[3] * y[1]) % P


def eye(n):
    return tuple(1 if i == j else 0 for i in range(n) for j in range(n))


def add(a, b):
    return tuple((x + y) % P for x, y in zip(a, b))


def sub(a, b):
    return tuple((x - y) % P for x, y in zip(a, b))


def mul(a, b, n):
    return tuple(
        sum(a[i * n + k] * b[k * n + j] for k in range(n)) % P
        for i in range(n) for j in range(n)
    )


def matrix_from_columns(columns):
    n = len(columns)
    return tuple(columns[j][i] for i in range(n) for j in range(n))


def rank(a, n):
    rows = [list(a[i * n:(i + 1) * n]) for i in range(n)]
    pivot_row = 0
    for col in range(n):
        pivot = next((r for r in range(pivot_row, n) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inv = 1 if rows[pivot_row][col] == 1 else 2
        rows[pivot_row] = [(inv * x) % P for x in rows[pivot_row]]
        for r in range(n):
            if r != pivot_row and rows[r][col]:
                scalar = rows[r][col]
                rows[r] = [
                    (rows[r][j] - scalar * rows[pivot_row][j]) % P
                    for j in range(n)
                ]
        pivot_row += 1
    return pivot_row


def check_sp4():
    vectors = list(product(range(P), repeat=4))
    zero = (0, 0, 0, 0)
    i4 = eye(4)
    zero4 = (0,) * 16
    seen = set()
    types = {0: 0, 1: 0, 2: 0}
    bad_square = []

    # A symplectic basis is (a,b,c,d) with omega(a,c)=omega(b,d)=1
    # and all other cross-pairings zero.  Enumerate a,c first, then the
    # nondegenerate two-dimensional orthogonal complement.
    for a in vectors:
        if a == zero:
            continue
        for c in vectors:
            if omega(a, c) != 1:
                continue
            complement = [
                v for v in vectors if omega(a, v) == 0 and omega(c, v) == 0
            ]
            for b in complement:
                if b == zero:
                    continue
                for d in complement:
                    if omega(b, d) != 1:
                        continue
                    m = matrix_from_columns((a, b, c, d))
                    seen.add(m)
                    if mul(mul(m, m, 4), m, 4) == i4:
                        n = sub(m, i4)
                        n2 = mul(n, n, 4)
                        if n2 != zero4:
                            bad_square.append(m)
                        types[rank(n, 4)] += 1

    expected = (P ** 4) * (P ** 2 - 1) * (P ** 4 - 1)
    print(f"Sp4(3) matrices from symplectic bases: {len(seen)} (expected {expected})")
    print(f"M^3=I type counts by rank(M-I): {types}")
    print(f"M^3=I with (M-I)^2 != 0: {len(bad_square)}")
    assert len(seen) == expected
    assert not bad_square
    assert sum(types.values()) > 1


def check_regular_centralizer():
    i3 = eye(3)
    zero3 = (0,) * 9
    # Columns give R(e1)=e2, R(e2)=c, R(c)=0.
    r = matrix_from_columns(((0, 1, 0), (0, 0, 1), (0, 0, 0)))
    r2 = mul(r, r, 3)
    commuting = set()
    constrained = set()
    for x in product(range(P), repeat=9):
        if mul(x, r, 3) != mul(r, x, 3):
            continue
        commuting.add(x)
        xc = (x[2], x[5], x[8])
        x3 = mul(mul(x, x, 3), x, 3)
        if xc == (0, 0, 0) and x3 == zero3:
            constrained.add(x)

    polynomial_centralizer = {
        add(add(tuple(a * y % P for y in i3),
                tuple(b * y % P for y in r)),
            tuple(d * y % P for y in r2))
        for a in range(P) for b in range(P) for d in range(P)
    }
    claimed = {
        add(tuple(b * y % P for y in r), tuple(d * y % P for y in r2))
        for b in range(P) for d in range(P)
    }
    print(f"End(F3^3) matrices commuting with regular R: {len(commuting)}")
    print(f"Centralizer equals F3[I,R,R^2]: {commuting == polynomial_centralizer}")
    print(f"Commuting R' with R'c=0 and (R')^3=0: {len(constrained)}")
    print(f"Constrained set equals {{bR+dR^2}}: {constrained == claimed}")
    assert commuting == polynomial_centralizer
    assert constrained == claimed


if __name__ == "__main__":
    check_sp4()
    check_regular_centralizer()
