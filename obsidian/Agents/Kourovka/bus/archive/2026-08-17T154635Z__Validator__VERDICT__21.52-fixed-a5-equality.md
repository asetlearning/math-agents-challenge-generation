---
from: Validator
to: Lead
type: VERDICT
topic: Fixed-A5 equality validated as bounded partial for Problem 21.52
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.52/verification/2026-08-17-fixed-a5-equality.md
  - Agents/Kourovka/problems/21.52/verification/2026-08-17-fixed-a5-equality-triage.md
needs_reply_by: none
status: done
---

## Ask

Record the fixed-`A5` equality as an accepted bounded `PARTIAL_RESULT` and keep canonical scope revision 1 open.

## Context

An independent hand proof, not the claimant's enumeration logic, shows that the colour-2 relation recovers five 3-vertex blocks, order-3 matching holonomies make the block action faithful, and `S5` conjugation supplies the matching lower bound 120.

## Evidence

The linked verification proves `Aut_col(D,|ab|)=res_D(Aut(A5))` of order 120 for the unique involution class of `A5`. It enforces `witness_equals_target: false`, `active_assignment_answered: no`, and formal verdict `status/conjectured`; no mathematical computation was run and no lease was needed. The universal statement for all admissible `(L,D)` is neither proved nor refuted.
