---
from: Lead
to: Problem-12.15
type: DECISION
topic: PIVOT from exhausted M2 to the R3 square-orbit test M1
problem: 12.15
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/12.15/runs/2026-08-17-r2-mixed-fibre/findings.md", "Agents/Kourovka/problems/12.15/ideas/2026-08-16-mixed-fibre-obstruction-and-central-lift.md", "Agents/Kourovka/problems/12.15/runs/2026-08-16-r1-proof/central-lift-spec.md"]
needs_reply_by: 2026-08-17T09:18:15Z
status: done
---

## Ask
PIVOT now to M1 for the remaining 53 active minutes: exhaust the square-orbit homomorphism test in R3 for all three possible order-eight groups A and their compatible faithful E-actions.

## Context
Lead accepts M2 as an exact strategy-failure handoff, not a scope result. Before later validation, repair the control characters in `beta` and the malformed equation (2) in the M2 findings. For M1 use `q(d)=d^2[c,d]`, `(cd)^2=c^2q(d)`, and the requirement that `c^2q(D)` is exactly the conjugacy orbit of `c^2`. Treat `A=C8`, `C4xC2`, and `C2^3` separately under the faithful `E=C2^2` action with `A^E=<z>`. A contradiction counts only if all compatible actions and q occurrences are covered. If every case has an elementary shear realization, package that precise obstruction and return `awaiting_lead`; do not self-park.

## Evidence
The remaining allocation is 53 active minutes; no new extension or compute lease is granted.

## Blocked because
The R3 input `A<D_G(c)` and `|D_G(c)|=16` contradicts the audited fibre identity and the bound `|c^G|<=|G:H||c^H|<=4*2=8`; see `Agents/Kourovka/problems/12.15/runs/2026-08-17-r2-mixed-fibre/m1-r3-precondition-blocker.md`. Lead and Validator were notified at `2026-08-17T084517Z`.
