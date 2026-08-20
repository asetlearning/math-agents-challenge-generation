#!/usr/bin/env python3
"""Check the finite truncated-polynomial norm specialization for small odd p."""


def add(a, b, p):
    out = dict(a)
    for mon, coeff in b.items():
        out[mon] = (out.get(mon, 0) + coeff) % p
        if out[mon] == 0:
            del out[mon]
    return out


def scale(a, scalar, p):
    return {mon: (scalar * coeff) % p for mon, coeff in a.items()
            if (scalar * coeff) % p}


def mul(a, b, p):
    out = {}
    for (i, j), ca in a.items():
        for (k, ell), cb in b.items():
            if i + k < p and j + ell < p:
                mon = (i + k, j + ell)
                out[mon] = (out.get(mon, 0) + ca * cb) % p
                if out[mon] == 0:
                    del out[mon]
    return out


def power(a, n, p):
    out = {(0, 0): 1}
    base = a
    while n:
        if n & 1:
            out = mul(out, base, p)
        base = mul(base, base, p)
        n //= 2
    return out


def norm(operator, p):
    out = {}
    term = {(0, 0): 1}
    for _ in range(p):
        out = add(out, term, p)
        term = mul(term, operator, p)
    return out


for prime in (3, 5, 7):
    one = {(0, 0): 1}
    s = {(1, 0): 1}
    t = {(0, 1): 1}
    x = add(one, s, prime)
    y = add(one, t, prime)
    z = mul(x, y, prime)
    nx, ny, nz = norm(x, prime), norm(y, prime), norm(z, prime)
    d = {(prime - 1, prime - 1): 1}
    lhs_xy = mul(mul(nx, ny, prime), one, prime)
    lhs_zx = mul(mul(nz, nx, prime), scale(one, -1, prime), prime)
    lhs_zy = mul(mul(nz, ny, prime), y, prime)
    fixed = mul(x, d, prime) == d and mul(y, d, prime) == d
    print({
        "p": prime,
        "X^p=Y^p=Z^p=1": power(x, prime, prime) == one
        and power(y, prime, prime) == one
        and power(z, prime, prime) == one,
        "d_nonzero": bool(d),
        "NX_NY_c=d": lhs_xy == d,
        "NZ_NX_minus_c=-d": lhs_zx == scale(d, -1, prime),
        "NZ_NY_Yc=d": lhs_zy == d,
        "d_fixed": fixed,
    })
