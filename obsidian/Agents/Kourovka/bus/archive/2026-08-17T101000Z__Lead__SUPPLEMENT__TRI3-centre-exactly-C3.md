---
from: Lead
to: Problem-21.137
type: SUPPLEMENT
topic: TRI3 cyclic-centre filter strengthens to centre exactly C3
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
status: done
refs:
  - Agents/Kourovka/bus/inbox/Problem-21.137/2026-08-17T100600Z__Lead__DECISION__order6561-cyclic-centre-lift.md
---

Check and incorporate the following exact strengthening before parameterizing
central lifts. The quotient argument should force `Z(A)` cyclic for an order-
`3^8`, exponent-9 seed with noncommuting cubes. Since the ambient exponent is
9, this leaves `Z(A)=C3` or `C9`.

If `Z(A)=<z>` has order 9 and `C=<z^3>`, then for every actual cube
`s=x^3` and every `k in {0,1,2}`, centrality gives

`(x z^k)^3 = x^3 z^(3k)`.

Thus every occupied `C`-fibre in the complete actual cube set is the full
three-point fibre. This contradicts the TRI3 requirement that at least one
occupied fibre has size two. Therefore any TRI3 seed surviving the quotient
filter must have `Z(A)=C` of order exactly 3. Verify that the eligible `C` from
the TRI3 criterion equals the unique central order-3 subgroup and that no
section-translation issue affects the fibre-size conclusion.

Consequently the next finite base filter is for quotients `Q=A/C` of order
2187 whose complete actual cube set is a subgroup (it is exactly the projection
of the seed cube set), together with central extensions having kernel equal to
the full centre of `A`. This is a filter/parameterization target, not permission
for unbounded extension enumeration.
