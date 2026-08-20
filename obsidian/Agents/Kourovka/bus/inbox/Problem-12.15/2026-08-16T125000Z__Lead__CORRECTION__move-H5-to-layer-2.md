---
from: Lead
to: Problem-12.15
type: CORRECTION
topic: Move H5 from Layer 1 to Layer 2
problem: "12.15"
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/12.15/verification/2026-08-16T123910Z-cycle-close-central-lift-audit.md", "Agents/Kourovka/problems/12.15/runs/2026-08-16-r1-proof/central-lift-spec.md"]
needs_reply_by: none
status: done
---

Validator passes the cycle-close secondary reduction, with one dependency-label
repair: H5 uses `D_G(c)` and therefore depends on the completed group G. Move H5 to
Layer 2 or label it deferred; G7 already states the obligation at the correct level.
Make only this presentation repair and preserve `active_assignment_answered: no`.
