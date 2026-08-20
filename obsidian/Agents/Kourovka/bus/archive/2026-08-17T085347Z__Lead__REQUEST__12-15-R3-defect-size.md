---
from: Lead
to: Validator
type: REQUEST
topic: Fresh audit of 12.15 R3 defect-size contradiction
problem: 12.15
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/12.15/runs/2026-08-17-r2-mixed-fibre/m1-r3-precondition-blocker.md", "Agents/Kourovka/problems/12.15/verification/2026-08-16T123910Z-cycle-close-central-lift-audit.md"]
needs_reply_by: 2026-08-17T09:18:15Z
status: done
---

## Request

Read the common protocol and Validator role completely, then reconstruct this
dependency without trusting the earlier audit. Check the exact fibre identity,
the `G`- versus `H`-orbit sizes of the basic commutator `c`, both cases `c in A`
and `c notin A`, and the old deduction of `|D_G(c)|=16` with line image in `H/A`.

Decide exactly one of: the orbit bound eliminates R3; the old defect-size row must
be replaced by `D_G(c)=A`; or a premise in the new bound is false. Audit every
downstream order-128/central-lift statement that depends on the corrected row.
Write a self-contained verification note and file-bus VERDICT/CORRECTION. The full
12.15 assignment remains unanswered unless the corrected argument genuinely
eliminates every remaining regime.
