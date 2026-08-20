#!/usr/bin/env python3
"""Independent component-multiset audit of the four-matching signature list."""

from math import gcd
import sys


# name, x-edge weight, y-edge weight, support size, product-order contribution
TYPES = [("E",1,1,2,1)]
for r in range(2,5):
    TYPES.append((f"C{2*r}",r,r,2*r,r))
for r in range(1,5):
    TYPES.append((f"P{2*r}",r,r,2*r+1,2*r+1))
for r in range(4):
    TYPES.append((f"P{2*r+1}X",r+1,r,2*r+2,2*r+2))
    TYPES.append((f"P{2*r+1}Y",r,r+1,2*r+2,2*r+2))
TYPES.sort()


def swap_name(s):
    if s.endswith("X"):
        return s[:-1]+"Y"
    if s.endswith("Y"):
        return s[:-1]+"X"
    return s


def canon(names):
    a="+".join(sorted(names))
    b="+".join(sorted(swap_name(x) for x in names))
    return min(a,b)


def lcm(a,b):
    return a//gcd(a,b)*b


found={}
def rec(start, ax, ay, names, support, order):
    if ax==4 and ay==4:
        lab=canon(names)
        if lab != "E+E+E+E":
            found[lab]=(support,order,int("E" in names))
        return
    for i in range(start,len(TYPES)):
        name,wx,wy,s,o=TYPES[i]
        if ax+wx<=4 and ay+wy<=4:
            rec(i,ax+wx,ay+wy,names+[name],support+s,lcm(order,o))
rec(0,0,0,[],0,1)

observed={}
with open(sys.argv[1],encoding="utf-8") as f:
    for line in f:
        row=line.rstrip().split("\t")
        if row[0]=="SIG":
            # separation certificate columns: id, common, m, label, pair order, ...
            observed[row[4]]=(int(row[3]),int(row[5]),int(row[2]))

if found != observed:
    print("missing_from_matching_enumerator",sorted(set(found)-set(observed)))
    print("extra_in_matching_enumerator",sorted(set(observed)-set(found)))
    for k in sorted(set(found)&set(observed)):
        if found[k]!=observed[k]: print("value_mismatch",k,found[k],observed[k])
    raise SystemExit(1)

print("signature_audit=PASS")
print("signatures",len(found))
print("common",sum(v[2] for v in found.values()))
print("no_common",sum(not v[2] for v in found.values()))
