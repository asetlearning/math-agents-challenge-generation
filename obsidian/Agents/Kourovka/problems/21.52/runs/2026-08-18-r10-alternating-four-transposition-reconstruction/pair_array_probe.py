#!/usr/bin/env python3
"""Bounded probe: do full two-point product-order arrays separate union types?"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations
from math import gcd
import sys

def matching_tuples(n, k=4):
    # Every k-matching exactly once, encoded as a sorted tuple of sorted edges.
    def rec(avail, left, out):
        if left == 0:
            yield tuple(out)
            return
        if len(avail) < 2*left:
            return
        x = avail[0]
        # x unused
        yield from rec(avail[1:], left, out)
        # x matched
        for j in range(1, len(avail)):
            y = avail[j]
            nxt = avail[1:j] + avail[j+1:]
            yield from rec(nxt, left-1, out + [(x,y)])
    yield from rec(tuple(range(n)), k, [])

def prod_order(x, y, n):
    px = list(range(n)); py = list(range(n))
    for u,v in x: px[u]=v; px[v]=u
    for u,v in y: py[u]=v; py[v]=u
    p = [px[py[i]] for i in range(n)]
    seen = [False]*n; ans=1
    for i in range(n):
        if not seen[i]:
            j=i; m=0
            while not seen[j]: seen[j]=True; m+=1; j=p[j]
            ans=ans*m//gcd(ans,m)
    return ans

def realize(names):
    a=[]; b=[]; q=0
    for name in names:
        if name == "E":
            a.append((q,q+1)); b.append((q,q+1)); q += 2
            continue
        kind=name[0]; m=int(name[1:])
        if kind == "C":
            for j in range(m): a.append((q+2*j,q+2*j+1))
            for j in range(m-1): b.append((q+2*j+1,q+2*j+2))
            b.append((q+2*m-1,q)); q += 2*m
        elif kind == "P":
            for j in range(m):
                edge=(q+j,q+j+1)
                (a if j%2==0 else b).append(edge)
            q += m+1
        elif kind in "RB":
            major=a if kind=="R" else b; minor=b if kind=="R" else a
            for j in range(m):
                edge=(q+j,q+j+1)
                (major if j%2==0 else minor).append(edge)
            q += m+1
        else: raise ValueError(name)
    assert len(a)==len(b)==4
    norm=lambda z: tuple(sorted((min(x,y),max(x,y)) for x,y in z))
    return norm(a), norm(b), q

def signatures():
    types=[("E",1,1)]
    types += [(f"C{k}",k,k) for k in range(2,5)]
    types += [(f"P{2*k}",k,k) for k in range(1,5)]
    for k in range(4):
        types += [(f"R{2*k+1}",k+1,k),(f"B{2*k+1}",k,k+1)]
    out=[]
    def rec(i,r,b,z):
        if r==b==0:
            if z != ("E",)*4: out.append(z)
            return
        if i==len(types): return
        name,x,y=types[i]
        maxm=min(r//x if x else 99,b//y if y else 99)
        for m in range(maxm+1): rec(i+1,r-m*x,b-m*y,z+(name,)*m)
    rec(0,4,4,())
    return out

def main(n, details=False):
    cs=list(matching_tuples(n))
    colours=sorted({prod_order(cs[0],c,n) for c in cs if c != cs[0]})
    sigs=[]
    for names in signatures():
        a,b,v=realize(names)
        if v<=n: sigs.append((names,a,b,v))
    buckets=defaultdict(list)
    rows=[]
    for names,a,b,v in sigs:
        arr=Counter()
        for c in cs:
            if c != a and c != b:
                arr[(prod_order(a,c,n),prod_order(b,c,n))]+=1
        key=tuple((i,j,arr[(i,j)]) for i in colours for j in colours)
        buckets[key].append((names,prod_order(a,b,n),16-v))
        rows.append((names, names.count("E"), prod_order(a,b,n), 16-v, arr[(2,2)],
                     arr[(9,9)], arr[(7,7)], arr[(7,9)]+arr[(9,7)],
                     tuple(sorted((ij,k) for ij,k in arr.items() if k))))
    collisions=[z for z in buckets.values() if len(z)>1]
    print("n",n,"vertices",len(cs),"types",len(sigs),"colours",colours,
          "array_classes",len(buckets),"collisions",len(collisions))
    for z in collisions: print("COLLISION",z)
    if details:
        for row in rows:
            print("ROW",row[:-1])
            if n <= 9: print("ARRAY",row[0],row[-1])

if __name__ == '__main__': main(int(sys.argv[1]), len(sys.argv)>2)
