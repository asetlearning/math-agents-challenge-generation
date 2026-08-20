#!/usr/bin/env python3
"""Independent exact n=14 check of all feasible commuting-pair types."""

from itertools import combinations

N=14


def matchings(points,k):
    if k==0:
        yield ()
        return
    if len(points)<2*k:
        return
    p=points[0]
    # Either p is unused, or p is paired.  This generates every k-matching once.
    yield from matchings(points[1:],k)
    for i in range(1,len(points)):
        q=points[i]
        rest=points[1:i]+points[i+1:]
        for m in matchings(rest,k-1):
            yield ((p,q),)+m


def perm(m):
    p=list(range(N))
    for i,j in m: p[i],p[j]=j,i
    return tuple(p)


def commute(p,q):
    return all(p[q[i]]==q[p[i]] for i in range(N))


def representative(a,b,c):
    x=[]; y=[]; p=0
    for _ in range(a):
        x.append((p,p+1)); y.append((p,p+1)); p+=2
    for _ in range(b):
        x.append((p,p+1)); p+=2
    for _ in range(b):
        y.append((p,p+1)); p+=2
    for _ in range(c):
        x.extend(((p,p+1),(p+2,p+3)))
        y.extend(((p,p+2),(p+1,p+3)))
        p+=4
    assert len(x)==len(y)==6 and p==12+2*b and p<=N
    return perm(x),perm(y),tuple(x),tuple(y)


types=((4,0,1),(2,0,2),(0,0,3),(5,1,0),(3,1,1),(1,1,2))
reps={t:representative(*t) for t in types}
counts={t:0 for t in types}
total=0
for m in matchings(tuple(range(N)),6):
    total+=1
    z=perm(m)
    for t,(x,y,_,_) in reps.items():
        if commute(x,z) and commute(y,z): counts[t]+=1

print("n",N,"six_matchings",total)
for t in types:
    x,y,xm,ym=reps[t]
    print(t,"common_edges",len(set(xm)&set(ym)),"commute_xy",commute(x,y),
          "centralizer_six_matchings",counts[t],"graph_common_colour2",counts[t]-2)
assert total==945945
assert len(set(counts.values()))==len(types)
assert counts[(5,1,0)]==287
print("PASS target (5,1,0) is uniquely isolated at n=14")
