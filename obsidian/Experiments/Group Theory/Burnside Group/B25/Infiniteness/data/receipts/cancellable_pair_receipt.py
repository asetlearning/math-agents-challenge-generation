#!/usr/bin/env python3
"""Machine receipt for the cancellable-pair theorem (the 'aligned bands vanish' step).

Claim (used in the Gate-2 final ruling): for an ALIGNED, opposite-oriented pair of
p^5-cells sharing an arc alpha with 4 <= |alpha| <= 19, the outer contour of the union
freely reduces to the empty word; for PHASE-OFFSET gluings it does not.

Model: cell C has cyclic boundary word W = p^5 (20 letters). Cell C' (opposite
orientation) has cyclic boundary word W' = inv(W) (= (p^{-1})^5 as a linear word,
W'[j] = swapcase(W[19-j])). A gluing of C' to C along alpha = cyclic subword W[s:s+m]
is any position t with cyclic W'[t:t+m] == inv(alpha). The canonical ALIGNED gluing is
t0 = (20 - s - m) mod 20; matches at t = t0 + delta occur when delta != 0 due to the
4-periodicity of p^5, and those are the PHASE-OFFSET gluings (delta mod 4 != 0 shifts
the period phase; delta mod 4 == 0 with delta != 0 shifts by whole periods).

For every gluing, outer contour = u . v' with u = cyclic complement W[s+m .. s],
v' = cyclic complement W'[t+m .. t]. Verify: free reduction of u.v' is empty iff the
gluing is aligned-or-whole-period-shifted; report the reduced contour length otherwise.
Exhaustive: 5 periods x m in 4..19 x s in 0..19 x all matching t.
"""
PERIODS = ["AABB", "AAbb", "ABAb", "ABaB", "ABab"]

def inv(w): return w[::-1].swapcase()

def red(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase(): out.pop()
        else: out.append(c)
    return "".join(out)

def cyc(w, i, ln):
    return "".join(w[(i + j) % len(w)] for j in range(ln))

total = aligned_ok = aligned_bad = offset_nonempty = offset_empty = 0
offset_lens = set()
for p in PERIODS:
    W = p * 5
    Wp = inv(W)
    for m in range(4, 20):
        for s in range(20):
            alpha = cyc(W, s, m)
            ia = inv(alpha)
            u = cyc(W, (s + m) % 20, 20 - m)
            for t in range(20):
                if cyc(Wp, t, m) != ia: continue
                total += 1
                vprime = cyc(Wp, (t + m) % 20, 20 - m)
                r = red(u + vprime)
                delta = (t - (20 - s - m)) % 20
                if delta % 4 == 0:
                    if r == "": aligned_ok += 1
                    else:
                        aligned_bad += 1
                        print(f"ALIGNED-FAIL p={p} m={m} s={s} t={t} contour_len={len(r)}")
                else:
                    if r == "":
                        offset_empty += 1
                        print(f"OFFSET-EMPTY (unexpected) p={p} m={m} s={s} t={t} delta={delta}")
                    else:
                        offset_nonempty += 1
                        offset_lens.add(len(r))
print(f"gluings checked: {total}")
print(f"aligned (delta=0 mod 4): contour==empty {aligned_ok}, contour!=empty {aligned_bad}")
print(f"phase-offset: contour nonempty {offset_nonempty}, empty {offset_empty}; "
      f"nonempty contour lengths observed: {sorted(offset_lens)}")
print("VERDICT:", "PASS — every aligned opposite gluing cancels; no offset gluing does"
      if aligned_bad == 0 and offset_empty == 0 else "FAIL — see lines above")
