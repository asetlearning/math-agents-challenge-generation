#!/usr/bin/env python3
"""Enumerate component multisets for two distinct four-edge matchings."""
from math import gcd

types = [("E", 1, 1, 1, 2)]
for k in range(2, 5):
    types.append((f"C{k}", k, k, k, 2*k))
for k in range(1, 5):
    types.append((f"P{2*k}", k, k, 2*k+1, 2*k+1))
for k in range(0, 4):
    types.append((f"R{2*k+1}", k+1, k, 2*k+2, 2*k+2))
    types.append((f"B{2*k+1}", k, k+1, 2*k+2, 2*k+2))

ans = []
def rec(i, ar, br, chosen):
    if ar == br == 0:
        if chosen != [("E", 1, 1, 1, 2)] * 4:
            order = 1
            vertices = 0
            for _, _, _, o, v in chosen:
                order = order * o // gcd(order, o)
                vertices += v
            ans.append((order, vertices, tuple(x[0] for x in chosen)))
        return
    if i == len(types):
        return
    t = types[i]
    maxm = min(ar // t[1] if t[1] else 99,
               br // t[2] if t[2] else 99)
    for m in range(maxm + 1):
        rec(i+1, ar-m*t[1], br-m*t[2], chosen + [t]*m)

rec(0, 4, 4, [])
ans.sort(key=lambda z: (z[0], z[1], z[2]))
print("signature_count", len(ans))
print("orders", sorted(set(x[0] for x in ans)))
for order, vertices, sig in ans:
    print(f"{order:2d} V={vertices:2d} s={16-vertices:2d}  {' '.join(sig)}")
