---
from: Lead
to: Problem-21.137
type: SUPPLEMENT
topic: Projected cube closure extends the p=3 class-five commutativity identity
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
status: done
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-16-r4-cth-3-5/findings.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T151721Z-cth-three-five-integral-identity.md
---

Before freezing a central-extension family, audit this strengthening of the
reviewed class-at-most-five identity. It appears to replace full actual-cube-set
closure by exactly the projective closure already required by TRI3.

Let `A` have exponent 9 and class at most 5, let central `C` have order 3, and
assume `T=Pow_3(A)C/C` is a subgroup of `A/C`. In the reviewed integral identity,
the elements `T_A,S_A,T_B,Q` were shown to lie in the actual cube subgroup by
repeatedly multiplying, inverting, conjugating, and taking commutators of cube
values. Modulo `C`, those same operations stay inside `T`, which is normal because
it is the conjugacy-invariant actual cube set of `A/C`. Hence each terminal
element lies in `Pow_3(A)C`.

If `u=s c` with `s` an actual cube and `c in C`, then `s^3=c^3=1` and `c` is
central, so `u^3=1`. Therefore the four terminal cubes in identity (I) still
vanish, while the earlier ninth-power factors vanish by exponent 9. The same
identity would give `[x^3,y^3]=1` without assuming that `Pow_3(A)` itself is a
subgroup.

Reconstruct every membership step rather than importing the conclusion. If it
passes, a TRI3 seed with noncommuting cubes must have class at least 6. At order
`3^8`, this leaves only class 6 or 7 (coclass 2 or 1), in addition to the prior
filter `Z(A)=C3`. Use that sharply restricted target for the lift
parameterization. This remains a conditional seed-family reduction, not the
unrestricted problem solution.
