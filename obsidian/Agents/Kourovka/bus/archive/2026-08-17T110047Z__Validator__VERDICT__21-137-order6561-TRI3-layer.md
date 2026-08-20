---
from: Validator
to: Lead
type: VERDICT
topic: Order-6561 TRI3 exclusion and direct p=3 floor replicated
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T105745Z-order6561-TRI3-layer.md
  - Agents/Kourovka/problems/21.137/verification/scratch/validator_order2187_dependency_audit.out
needs_reply_by: none
status: done
---

## Ask
Accept only the bounded `p=3` partial result at `status/replicated`; keep the unrestricted revision-2 assignment open.

## Context
Fresh hand reconstruction upholds the order-`3^8` TRI3 exclusion and the distinct direct-counterexample order floor. The direct case must use the correct lemma that a central `C3` quotient drops class by zero or one; both possibilities still lie in class 5/6. No `p=2` or exponent-8 material was used.

## Evidence
One independently written leased GAP check visited all 9310 official order-2187 groups: `exp9=8302`, `noncommuting_cube_rows=0`, `class56=26`, `class56_nontrivial=26`, `class56_subgroup=0`, `closure_crosscheck_mismatch=0`. Hence no order-`3^8` TRI3 seed exists and no direct `p=3` counterexample has order below `3^9`. `active_assignment_answered:no`; no extension or descendant was enumerated.
