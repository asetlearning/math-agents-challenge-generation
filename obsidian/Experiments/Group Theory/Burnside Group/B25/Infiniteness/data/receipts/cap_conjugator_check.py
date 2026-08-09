#!/usr/bin/env python3
"""Replay script for cap_conjugator_receipt.md (originally run inline 2026-08-02).
Exhaustive: for each period p, rotation k=1..3, and every freely reduced cap |c|<=3,
decide c·rot_k(p)·c^-1 = p in G_3 (wordreduce -diff2 g3), then classify each solution
against the canonical coset u_k<rot_k(p)> (free level, exponents -6..6), with G_3
normal-form fallback for power-identity duplicates (e.g. aaa =G3 A^2)."""
import subprocess, itertools
KB = '/Users/maumayma/Desktop/reps/algo_mixing/infinite_b25/avenues/a6_bounded/kbmag'
WR = '/Users/maumayma/Desktop/reps/algo_mixing/kbmag_v1/standalone/bin/wordreduce'
def inv(w): return w[::-1].swapcase()
def fred(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase(): out.pop()
        else: out.append(c)
    return ''.join(out)
def nf(w):
    r = subprocess.run([WR, '-diff2', 'g3'], input=('*'.join(w) if w else '') + ';',
                       capture_output=True, text=True, cwd=KB)
    return ''.join(l.strip() for l in r.stdout.split('reduces to:')[1].splitlines()).replace(' ', '')
caps = ['']
for L in (1, 2, 3):
    caps += [''.join(t) for t in itertools.product('abAB', repeat=L)
             if all(''.join(t)[i] != ''.join(t)[i+1].swapcase() for i in range(L-1))]
print(f"caps enumerated: {len(caps)}")
sols, exotic = [], []
for p in ['AABB', 'AAbb', 'ABAb', 'ABaB', 'ABab']:
    pn = nf(p)
    for k in (1, 2, 3):
        rp = p[k:] + p[:k]; u = p[:k]
        coset_free = {fred(u + (rp*m if m >= 0 else inv(rp)*(-m))) for m in range(-6, 7)}
        coset_nf = {nf(x) for x in coset_free if len(x) <= 6}
        for c in caps:
            if nf(c + rp + inv(c)) == pn:
                tag = 'coset-free' if fred(c) in coset_free else (
                      'coset-G3' if nf(c) in coset_nf else 'EXOTIC')
                sols.append((p, k, c, tag))
                if tag == 'EXOTIC': exotic.append((p, k, c))
for s in sols: print(s)
print(f"solutions: {len(sols)}; EXOTIC (not in u_k<rot_k p>): {exotic if exotic else 'NONE'}")
