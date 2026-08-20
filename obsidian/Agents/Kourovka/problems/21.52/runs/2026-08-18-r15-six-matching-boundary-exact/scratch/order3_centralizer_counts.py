#!/usr/bin/env python3
"""Exact common-colour-2 counts for product-order-3 six-matching pairs.

Use (a,p,q): a common edges, p alternating 2-edge paths (natural 3-point
S3-orbits), q alternating 6-cycles (regular 6-point S3-orbits).  Then
a+p+3q=6 and f=n-12-p.
"""

from fractions import Fraction
from math import comb, factorial

def add(a,b):
    z=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a): z[i]+=x
    for i,x in enumerate(b): z[i]+=x
    while len(z)>1 and z[-1]==0:z.pop()
    return z
def mul(a,b):
    z=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    while len(z)>1 and z[-1]==0:z.pop()
    return z
def scale(a,q):return [q*x for x in a]
def val(a,x):
    z=Fraction(0)
    for q in reversed(a):z=z*x+q
    return z
def shift(a,N):
    z=[Fraction(0)]*len(a)
    for i,q in enumerate(a):
        for j in range(i+1):z[j]+=q*comb(i,j)*N**(i-j)
    return z
def fall(off,d):
    z=[Fraction(1)]
    for i in range(d):z=mul(z,[Fraction(-off-i),Fraction(1)])
    return z
def umul(a,b):
    z=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=6:z[i+j]+=x*y
    return z

def c2_wreath(m):
    z=[0]*7
    for r in range(m//2+1):
        coef=factorial(m)//(factorial(m-2*r)*factorial(r))
        for j in range(m-2*r+1):
            d=2*r+j
            if d<=6:z[d]+=coef*comb(m-2*r,j)
    return z
def natural3_copies(m):
    z=[0]*7
    for r in range(m//2+1):
        d=3*r
        if d<=6:z[d]+=factorial(m)//(factorial(m-2*r)*2**r*factorial(r))
    return z
def regular6_wreath(m):
    z=[0]*7
    for r in range(m//2+1):
        coef=factorial(m)*3**r//(factorial(m-2*r)*factorial(r))
        for j in range(m-2*r+1):
            d=6*r+3*j
            if d<=6:z[d]+=coef*comb(m-2*r,j)*3**j
    return z

def count(a,p,q):
    other=[1]+[0]*6
    for g in (c2_wreath(a),natural3_copies(p),regular6_wreath(q)):
        other=umul(other,g)
    ans=[Fraction(0)]
    off=12+p
    for j in range(7):
        if other[6-j]:ans=add(ans,scale(fall(off,2*j),Fraction(other[6-j],2**j*factorial(j))))
    return ans

types=[(6-p-3*q,p,q) for q in range(3) for p in range(7-3*q)
       if (6-p-3*q,p,q)!=(6,0,0)]
counts={t:count(*t) for t in types}
target=(5,1,0)

print("VALUES AND COLLISIONS 12..80")
for n in range(12,81):
    buckets={}
    for t,P in counts.items():
        if n>=12+t[1]:buckets.setdefault(int(val(P,n)),[]).append(t)
    tb=buckets[int(val(counts[target],n))] if n>=13 else []
    print(n,"target",int(val(counts[target],n)) if n>=13 else None,
          "target_block",tb,"all_collisions",[v for v in buckets.values() if len(v)>1])

print("SYMBOLIC TARGET SEPARATION")
for t,P in counts.items():
    if t==target:continue
    D=add(counts[target],scale(P,-1)); start=max(13,12+t[1])
    roots=[n for n in range(start,1001) if val(D,n)==0]
    threshold=None; coeffs=None
    for N in range(start,1001):
        s=shift(D,N); nz=[x for x in s if x]
        if nz and (all(x>0 for x in nz) or all(x<0 for x in nz)):
            threshold=N;coeffs=s;break
    print(t,"roots",roots,"sign_threshold",threshold,"shift_coeffs",coeffs)
