#!/usr/bin/env python3
"""Exact common-commuting-neighbour counts for two commuting k-matchings.

Discovery/checking aid only.  Formula is derived by H-orbit species in log/findings.
"""

from fractions import Fraction
from math import factorial


def mul(a, b, K):
    c = [0] * (K + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= K:
                c[i + j] += x * y
    return c


def F(m, K):
    out = [0] * (K + 1)
    for s in range(m // 2 + 1):
        for r in range(m - 2 * s + 1):
            d = r + 2 * s
            if d <= K:
                out[d] += factorial(m) // (
                    factorial(r) * factorial(m - r - 2 * s) * factorial(s)
                )
    return out


def G(m, K):
    out = [0] * (K + 1)
    for s in range(m // 2 + 1):
        for r in range(m - 2 * s + 1):
            d = 2 * r + 4 * s
            if d <= K:
                out[d] += (
                    factorial(m)
                    * 3**r
                    * 2**s
                    // (factorial(r) * factorial(m - r - 2 * s) * factorial(s))
                )
    return out


def M(f, K):
    out = [0] * (K + 1)
    for t in range(min(K, f // 2) + 1):
        out[t] = factorial(f) // (factorial(f - 2 * t) * 2**t * factorial(t))
    return out


def count(k, n, a, b, c):
    f = n - 2 * k - 2 * b
    q = [1] + [0] * k
    for fac in (F(a, k), F(b, k), F(b, k), G(c, k), M(f, k)):
        q = mul(q, fac, k)
    return q[k]


def params(k):
    for c in range(k // 2 + 1):
        for b in range(k - 2 * c + 1):
            a = k - b - 2 * c
            if a == k:  # x=y, not an edge
                continue
            yield a, b, c


def center_type_k_count(k, a, b, c):
    poly = [1] + [0] * k
    for m in (a, b, b):
        if m:
            fac = [0] * (k + 1)
            fac[0] = 1
            if m <= k:
                fac[m] += 1
            poly = mul(poly, fac, k)
    if c:
        fac = [0] * (k + 1)
        fac[0] = 1
        if 2 * c <= k:
            fac[2 * c] = 3
        poly = mul(poly, fac, k)
    return poly[k]


if __name__ == "__main__":
    for k in range(2, 13, 2):
        target = (k - 1, 1, 0)
        first_good = None
        collisions = []
        for n in range(2 * k + 2, 20 * k + 21):
            tv = count(k, n, *target)
            cs = [p for p in params(k) if p != target and count(k, n, *p) == tv]
            if cs:
                collisions.append((n, cs))
            elif all(not [p for p in params(k) if p != target and count(k, m, *p) == count(k, m, *target)] for m in range(n, 20 * k + 21)):
                first_good = n
                break
        print("k", k, "first suffix collision-free through probe", first_good,
              "early collisions", collisions[:8])
    print("\nORDER SNAPSHOTS")
    for k in (4, 6, 8):
        for n in (2 * k + 2, 3 * k, 5 * k):
            vals = sorted((count(k, n, *p), p) for p in params(k))
            target = (k - 1, 1, 0)
            ix = [p for _, p in vals].index(target)
            lo = vals[max(0, ix - 3):ix]
            hi = vals[ix + 1:ix + 4]
            print("k,n", k, n, "rank", ix, "/", len(vals), "lo", lo,
                  "target", vals[ix], "hi", hi)
    print("\nCENTER=2 PARAMS")
    for k in range(4, 18, 2):
        same = [p for p in params(k) if center_type_k_count(k, *p) == 2]
        print(k, same)
    print("\nTARGET MAX AMONG CENTER=2")
    for k in range(4, 42, 2):
        target = (k - 1, 1, 0)
        good = None
        for n in range(2 * k + 2, 8 * k + 21):
            tv = count(k, n, *target)
            competitors = [p for p in params(k)
                           if p != target and center_type_k_count(k, *p) == 2]
            if all(tv > count(k, n, *p) for p in competitors):
                good = n
                break
        print(k, good, "ratio", None if good is None else good / k)
    print("\nCOEFFICIENTWISE TARGET DOMINANCE AT n=6k+2")
    for k in range(4, 24, 2):
        n = 6 * k + 2
        targ = [1] + [0] * k
        for fac in (F(k - 1, k), F(1, k), F(1, k), M(n - 2*k - 2, k)):
            targ = mul(targ, fac, k)
        bad = []
        for b in range(2, k + 1):
            cand = [1] + [0] * k
            for fac in (F(k - b, k), F(b, k), F(b, k), M(n - 2*k - 2*b, k)):
                cand = mul(cand, fac, k)
            ds = [i for i in range(k + 1) if targ[i] < cand[i]]
            if ds:
                bad.append((b, ds[:4]))
        print(k, bad)
    print("\nCRUDE STEP DOMINANCE M(f+2) >= R_b^2 M(f)")
    for k in range(4, 30, 2):
        failures = []
        for b in range(2, k + 1):
            f = 2 * k + 2
            d = b - 1
            R = [1, 1, 2*d] + [0] * (k - 2)
            rhs = mul(mul(R, R, k), M(f, k), k)
            lhs = M(f + 2, k)
            ds = [t for t in range(k + 1) if lhs[t] < rhs[t]]
            if ds:
                failures.append((b, ds[:3]))
        print(k, failures[:5])
    print("\nCRUDE STEP DOMINANCE f=8k^2")
    for k in range(4, 52, 2):
        failures = []
        f = 8 * k * k
        for b in range(2, k + 1):
            d = b - 1
            R = [1, 1, 2*d] + [0] * (k - 2)
            rhs = mul(mul(R, R, k), M(f, k), k)
            lhs = M(f + 2, k)
            if any(lhs[t] < rhs[t] for t in range(k + 1)):
                failures.append(b)
        print(k, failures[:3])
