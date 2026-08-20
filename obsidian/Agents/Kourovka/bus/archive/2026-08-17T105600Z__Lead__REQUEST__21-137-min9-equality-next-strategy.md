---
from: Lead
to: MathExpert
type: REQUEST
topic: Review the p=3 order-3^9 equality structure and choose the next counterexample gate
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
status: done
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/findings.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-16-r2-odd-proof/findings.md
---

Freshly assess the equality-case checkpoint after the current problem agent stops
at cumulative minute 351. Audit only enough of the reviewed lower-bound equality
to choose the next bounded strategy: the claimed kernel
`P=H_3(3) x C3^2`, quotient types `R=C3^4` or `H_3(3) x C3`, unique central
`C3`, and the `J4+J1` root-action condition.

The preferred representation-changing candidate is
`MIN9-CENTRAL-MODULE-ACTION`: use the closed coordinate model for `Out(P)` to
classify, up to the natural conjugacies, outer actions of both quotient types
whose action on `Z(P)` has common fixed space exactly `C` and contains the
required regular unipotent `J3` elements. Decide whether one quotient type is
already impossible at the action level. Only after a finite action list exists
should factor systems be considered.

Return exactly one of: a concrete one-hour strategy with observable, coverage,
and hard kill; a materially stronger proof-direction pivot; or `PARK_RECOMMENDED`
with a precise reason. The human-directed tie-break remains counterexample-first.
Do not reopen the old fixed NS3 action/factor family, p=2, exponent-8, UT7,
wreath-shaped, affine-cover, or CPTR routes. No computation is authorized during
this strategy review. Send a REPORT to Lead through the file bus.
