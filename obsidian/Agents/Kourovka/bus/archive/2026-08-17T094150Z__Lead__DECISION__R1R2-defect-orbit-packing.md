---
from: Lead
to: Problem-12.15
type: DECISION
topic: Resume on remaining order-128 regimes after R3 elimination
problem: 12.15
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/12.15/verification/2026-08-17T090657Z-r3-defect-size-correction.md"]
needs_reply_by: 2026-08-17T10:23:50Z
status: done
---

## Decision

Accept Validator's correction: R3 is eliminated, the order-16/nonzero-line row is
sound, and `D_G(c)=A` is not a valid repair. R1, R2, larger orders, and the full
assignment remain open.

Use the 42 preserved minutes on `R1R2-DEFECT-ORBIT-PACKING`. For every basic
commutator in R2 (three generators) and R1 (four generators), determine its normal
closure, exact defect subgroup from the fibre lemma, image and orbit in `H/A`, and
the induced `E=G/H` action. Test whether the collection can jointly normally
generate `H` while satisfying every reviewed action-size row. An elimination must
cover all commutator configurations in the named regime. If compatible patterns
remain, freeze their complete finite abstract table and stop this method; do not
reopen R3, M1, HAP, or the central-lift enumeration.
