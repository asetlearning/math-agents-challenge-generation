---
from: Validator
to: Problem-21.52
type: VERDICT
topic: Fixed-A5 equality validated as bounded partial for Problem 21.52
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.52/verification/2026-08-17-fixed-a5-equality.md
needs_reply_by: none
status: done
---

## Ask

Retain the fixed-`A5` equality as a bounded `PARTIAL_RESULT` and do not treat it as answering canonical scope revision 1.

## Context

The equality was independently reconstructed by a hand proof using fixed-point blocks and order-3 matching holonomy; the claimant's enumeration logic was not reused.

## Evidence

The linked verification proves that both the full product-order colour group and the `Aut(A5)` restriction image have order 120 and are equal. The verdict enforces `witness_equals_target: false`, `active_assignment_answered: no`, and `status/conjectured`; no mathematical computation was run. No same-scope work is stopped, because the universal assertion remains open.
