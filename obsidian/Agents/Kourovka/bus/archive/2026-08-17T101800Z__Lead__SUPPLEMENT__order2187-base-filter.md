---
from: Lead
to: Problem-21.137
type: SUPPLEMENT
topic: Exact quotient-base filter after the centre and class reductions
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
status: done
refs:
  - Agents/Kourovka/bus/inbox/Problem-21.137/2026-08-17T101000Z__Lead__SUPPLEMENT__TRI3-centre-exactly-C3.md
  - Agents/Kourovka/bus/inbox/Problem-21.137/2026-08-17T101500Z__Lead__SUPPLEMENT__projective-closure-class-six.md
---

If both preceding supplements pass, record the exact finite quotient-base filter.
For a surviving order-`3^8` seed `A`, put `C=Z(A)=C3` and `Q=A/C`.

1. `Q` has order `3^7` and exponent 9. If its exponent were 3, then its actual
   cube set would be trivial, so `Pow_3(A)<=C`; all seed cubes would commute,
   contrary to the seed gate.
2. The complete actual cube set of `Q` is exactly
   `Pow_3(A)C/C=T`, hence is a nontrivial subgroup. The completed SmallGrp scan
   already guarantees it is abelian.
3. If `A` has class 6, then `gamma_6(A)=C` and `Q` has class exactly 5. If `A`
   has class 7, then `gamma_7(A)=C` and `Q` has class exactly 6.

Thus only SmallGroup `(2187,i)` rows with exact exponent 9, nilpotency class 5 or
6, and a nontrivial complete actual-cube set that is a subgroup can be quotient
bases. It is worthwhile to freeze a separate deterministic filter that lists
exactly these IDs and their cube-subgroup sizes; it must not rerun the already
settled noncommuting-seed question or imply that every central extension was
enumerated. Submit the frozen hash, exact command, expected resources, and a
short lease request before running GAP.
