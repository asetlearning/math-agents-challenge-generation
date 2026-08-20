#!/usr/bin/env python3
"""Exact common-colour-2 counts for pairs of six-matchings.

For a commuting ordered pair (x,y), use (a,b,c), where a is the number of
common transpositions, b is the number of x-only (and also y-only) two-point
orbits, and c is the number of regular V_4 four-point orbits.  Thus
a+b+2*c=6 and the number of common fixed points is f=n-12-2*b.
"""

from fractions import Fraction
from math import comb, factorial


def np_add(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i,x in enumerate(a): out[i] += x
    for i,x in enumerate(b): out[i] += x
    while len(out)>1 and out[-1] == 0: out.pop()
    return out


def np_mul(a, b):
    out = [Fraction(0)] * (len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j] += x*y
    while len(out)>1 and out[-1] == 0: out.pop()
    return out


def np_scale(a, q): return [q*x for x in a]


def np_eval(a, x):
    ans = Fraction(0)
    for q in reversed(a): ans = ans*x+q
    return ans


def np_shift(a, N):
    """Coefficients in m of p(N+m)."""
    out = [Fraction(0)]*len(a)
    for i,q in enumerate(a):
        for j in range(i+1): out[j] += q*comb(i,j)*N**(i-j)
    return out


def falling_shifted(offset, degree):
    # Product_{i=0}^{degree-1} (n-offset-i).
    out = [Fraction(1)]
    for i in range(degree): out = np_mul(out, [Fraction(-offset-i), Fraction(1)])
    return out


def two_orbit_factor(m):
    # Involutions in C2 wr S_m on m two-point H-orbits.
    ans = [0]*7
    for r in range(m//2 + 1):
        coeff = factorial(m) // (factorial(m-2*r) * factorial(r))
        for j in range(m-2*r+1):
            d=2*r+j
            if d<=6: ans[d] += coeff*comb(m-2*r,j)
    return ans


def regular_four_factor(m):
    # Involutions in V4 wr S_m on m regular four-point H-orbits.
    ans = [0]*7
    for r in range(m//2 + 1):
        coeff = factorial(m) * 2**r // (factorial(m-2*r) * factorial(r))
        for j in range(m-2*r+1):
            d=4*r+2*j
            if d<=6: ans[d] += coeff*comb(m-2*r,j)*3**j
    return ans


def up_mul(a,b):
    out=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=6: out[i+j]+=x*y
    return out


def centralizer_count(a, b, c):
    offset = 12+2*b
    other=[1]+[0]*6
    for q in (two_orbit_factor(a), two_orbit_factor(b),
              two_orbit_factor(b), regular_four_factor(c)):
        other=up_mul(other,q)
    ans=[Fraction(0)]
    for j in range(7):
        if other[6-j]:
            term=np_scale(falling_shifted(offset,2*j),
                          Fraction(other[6-j],2**j*factorial(j)))
            ans=np_add(ans,term)
    return ans


def pstr(p):
    terms=[]
    for i,q in enumerate(p):
        if q:
            terms.append(f"({q})*n^{i}")
    return " + ".join(terms) if terms else "0"


types = [(a,b,c) for c in range(4) for b in range(7-2*c)
         for a in [6-b-2*c] if (a,b,c) != (6,0,0)]
counts = {t: centralizer_count(*t) for t in types}

print("FORMULAS (including x,y; graph common-neighbour count is C-2)")
for t in types:
    print(t, "f=n-", 12+2*t[1], "C=", pstr(counts[t]))

print("\nFEASIBLE COLLISIONS BY DEGREE 12..80")
for nn in range(12, 81):
    buckets = {}
    for t,p in counts.items():
        if nn >= 12 + 2*t[1]:
            buckets.setdefault(int(np_eval(p,nn)), []).append(t)
    collisions = [v for v in buckets.values() if len(v)>1]
    target = (5,1,0)
    target_collision = []
    if nn >= 14:
        cv = int(np_eval(counts[target],nn))
        target_collision = buckets[cv]
    print(nn, "types", len([t for t in types if nn >= 12+2*t[1]]),
          "collision_blocks", collisions, "target_block", target_collision)

print("\nSYMBOLIC DIFFERENCES FROM (5,1,0)")
target = counts[(5,1,0)]
for t,p in counts.items():
    if t != (5,1,0):
        d=np_add(target,np_scale(p,-1))
        start=max(14,12+2*t[1])
        roots=[]
        for nn in range(start,1001):
            if np_eval(d,nn)==0: roots.append(nn)
        sign_threshold=None
        shifted_at=None
        for N in range(start,1001):
            s=np_shift(d,N)
            nz=[q for q in s if q]
            if nz and (all(q>0 for q in nz) or all(q<0 for q in nz)):
                sign_threshold=N; shifted_at=s; break
        print(t, "diff=",pstr(d),"roots",roots,"sign_threshold",sign_threshold,
              "shift_coeffs",shifted_at)
