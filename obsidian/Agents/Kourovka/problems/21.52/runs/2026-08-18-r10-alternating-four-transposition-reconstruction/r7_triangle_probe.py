#!/usr/bin/env python3
"""Probe whether colour-7 triangles can switch their unique common edge."""
import runpy, sys
from collections import Counter

p=runpy.run_path(__file__.replace('r7_triangle_probe.py','pair_array_probe.py'))
matchings=p['matching_tuples']; order=p['prod_order']
n=int(sys.argv[1]); ds=list(matchings(n)); a=ds[0]
aset=set(a)
nb=[]
for b in ds:
    if b!=a and order(a,b,n)==7:
        common=tuple(sorted(aset & set(b)))
        assert len(common)==1
        nb.append((b,common[0]))
tri=0; mixed=0; examples=[]; same_orders=Counter(); mixed_orders=Counter()
for i in range(len(nb)):
    b,e=nb[i]
    for j in range(i+1,len(nb)):
        c,f=nb[j]
        o=order(b,c,n)
        (same_orders if e==f else mixed_orders)[o]+=1
        if o==7:
            tri+=1
            if e!=f:
                mixed+=1
                if len(examples)<3: examples.append((a,b,c,e,f,tuple(set(b)&set(c))))
print('n',n,'vertices',len(ds),'degree7',len(nb),'triangles_at_a',tri,
      'mixed_at_a',mixed)
print('same_label_orders',dict(sorted(same_orders.items())))
print('mixed_label_orders',dict(sorted(mixed_orders.items())))
for x in examples: print('MIXED',x)
