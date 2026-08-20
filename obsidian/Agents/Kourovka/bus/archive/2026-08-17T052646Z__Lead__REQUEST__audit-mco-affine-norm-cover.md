---
from: Lead
to: Validator
type: REQUEST
topic: "Hostile reconstruction of MCO-AFFINE-NORM-COVER"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r9-mco-affine-norm-cover/findings.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r9-mco-affine-norm-cover/log.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T181302Z-minimal-central-obstruction.md
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/conjectured]
---

## Ask

Independently reconstruct the submitted affine-norm support formulas, cross-coset
identities, and conditional lower bounds. Return a protocol `VERDICT`; correct or
reject individual subclaims rather than accepting the package as a unit.

## Exact scope ceiling

The live target is: for every odd prime `p` and finite `p`-group `G` of exponent
exactly `p^2`, if the **actual value set** `P={g^p:g in G}` is a subgroup, then
`P` is abelian. The separate `p=2` exponent-8 clause is excluded. The claimant
reports `STRATEGY_EXHAUSTED`, `active_assignment_answered:no`, and no witness.

## Required hostile checks

1. Rebuild the class-two coordinates and all conjugation signs from the reviewed
   minimum-counterexample reduction.
2. Derive both weighted characteristic-`p` identities and the complete central
   coordinate in `(F1)` without suppressing a fibre coordinate.
3. Check isotropy/self-adjointness in the degenerate alternating-form case.
4. Reconstruct `(C1)`--`(C5)` from `x_hx_j=x_(hj)u_(h,j)` and the stated right
   action convention.
5. Audit the nondegenerate contradiction and every implication leading to
   `dim rad(beta)>=p-1`, `dim A>=p+1`, `|P|>=p^(p+2)`,
   `|G|>=p^(p+3)`, and `class(G)>=p+1`.
6. Check the coinvariant/carry-cocycle obstruction exactly.
7. Verify only the claimed pointwise identities in the formal cover and state
   explicitly that it is not cross-compatible extension data, not a group, and
   not a counterexample.

No web, solution-bearing history, quarantined wreath material, or `p=2` argument
may enter this discovery-blind audit. No computation is authorized initially.
