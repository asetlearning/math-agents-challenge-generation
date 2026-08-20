#!/usr/bin/env python3
"""Standalone structural verifier for separation-certificate.tsv."""

from collections import Counter
import sys


sig={}
arrays={}
cert=[]
meta={}
with open(sys.argv[1],encoding="utf-8") as f:
    for line in f:
        r=line.rstrip().split("\t")
        if r[0]=="META": meta[r[1]]=r[2]
        elif r[0]=="SIG": sig[int(r[1])]=int(r[2])
        elif r[0]=="A": arrays[int(r[1]),r[2]]=tuple(map(int,r[4].split(',')))
        elif r[0]=="CERT": cert.append((int(r[1]),int(r[2]),r[3],r[4],tuple(map(int,r[5].split(',')))))

common=sorted(i for i,c in sig.items() if c)
none=sorted(i for i,c in sig.items() if not c)
expected={(a,b) for a in common for b in none}
seen=Counter((a,b) for a,b,_,_,_ in cert)
assert set(seen)==expected and all(v==1 for v in seen.values())
zero=(0,)*9
for a,b,u,sign,d in cert:
    aa=arrays.get((a,u),zero); bb=arrays.get((b,u),zero)
    assert d==tuple(x-y for x,y in zip(aa,bb))
    assert d[0]!=0
    if sign=='+': assert d[0]>0 and all(x>=0 for x in d)
    elif sign=='-': assert d[0]<0 and all(x<=0 for x in d)
    else: raise AssertionError(sign)
assert int(meta['opposite_pairs'])==len(expected)==len(cert)
assert int(meta['unresolved_pairs'])==0
print("certificate_verification=PASS")
print("opposite_pairs",len(expected))
print("certificates",len(cert))
print("all_nonzero_for_every_integer_n_ge_14=yes")
