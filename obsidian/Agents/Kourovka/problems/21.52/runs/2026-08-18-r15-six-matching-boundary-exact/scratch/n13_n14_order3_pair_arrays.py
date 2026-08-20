#!/usr/bin/env python3
"""Complete exact two-point colour arrays for all order-3 pair orbits at n=13,14."""

from collections import Counter
import hashlib
from math import gcd

def matchings(points,k):
    if k==0:
        yield ()
        return
    if len(points)<2*k:return
    p=points[0]
    yield from matchings(points[1:],k)
    for i in range(1,len(points)):
        q=points[i]
        rest=points[1:i]+points[i+1:]
        for m in matchings(rest,k-1):yield ((p,q),)+m

def partner(m,n):
    p=list(range(n))
    for i,j in m:p[i]=j;p[j]=i
    return tuple(p)

def product_order(p,q):
    n=len(p); seen=[False]*n; ans=1
    for i in range(n):
        if not seen[i]:
            j=i;ell=0
            while not seen[j]:
                seen[j]=True;ell+=1;j=p[q[j]]
            ans=ans*ell//gcd(ans,ell)
    return ans

def rep(a,p,q,n):
    x=[];y=[];s=0
    for _ in range(a):x.append((s,s+1));y.append((s,s+1));s+=2
    for _ in range(p):x.append((s,s+1));y.append((s+1,s+2));s+=3
    for _ in range(q):
        x.extend(((s,s+1),(s+2,s+3),(s+4,s+5)))
        y.extend(((s+1,s+2),(s+3,s+4),(s+5,s)))
        s+=6
    assert len(x)==len(y)==6 and s==12+p and s<=n
    X=partner(x,n);Y=partner(y,n)
    assert product_order(X,Y)==3
    return X,Y

for n in (13,14):
    types=[(6-p-3*q,p,q) for q in range(3) for p in range(1 if q==0 else 0,min(6-3*q,n-12)+1)]
    # q=0,p=0 is x=y and was excluded by the lower bound above.
    reps={t:rep(*t,n) for t in types}
    arrays={t:Counter() for t in types}
    total=0
    for m in matchings(tuple(range(n)),6):
        z=partner(m,n); total+=1
        for t,(x,y) in reps.items():
            arrays[t][(product_order(x,z),product_order(y,z))]+=1
    print("n",n,"six_matchings",total,"types",types)
    for t in types:
        A=arrays[t]
        payload=";".join(f"{i},{j}:{v}" for (i,j),v in sorted(A.items()))
        print(t,"N22",A[(2,2)],"N33",A[(3,3)],
              "array_entries",len(A),"sha256",hashlib.sha256(payload.encode()).hexdigest())
    target=(5,1,0)
    sig=lambda t:(arrays[t][(2,2)],arrays[t][(3,3)])
    assert [t for t in types if sig(t)==sig(target)]==[target]
    print("PASS target signature",sig(target),"is unique at n",n)
