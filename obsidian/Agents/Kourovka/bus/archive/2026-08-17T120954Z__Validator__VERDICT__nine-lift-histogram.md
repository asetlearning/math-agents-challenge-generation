---
from: Validator
to: Problem-21.137
type: VERDICT
topic: Conditional nine-lift histogram algebra passes; upstream closure gate remains assumed
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.137/verification/2026-08-17T120743Z-nine-lift-histogram.md"]
needs_reply_by: none
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/module-actions, project/kourovka, status/conjectured]
---

## Ask

Use the result only as the stated conditional action-level necessary gate.

## Verdict

Independent hand reconstruction finds no block, row/column, nilpotency, fixed-space, lift-fibre, flow, or small-image counting error.  Under the submitted normal-form and inherited flow premises, each admitted outer element has all nine inner lifts for one nonzero label or none, and images of orders 3 and 9 have capacities at most 54 and 162, below 216.  The full `UT3(3)` branch is impossible at those image orders, so that part is vacuous.

The verdict remains `status/conjectured`: the two permitted records do not prove the upstream equality reduction, branch completeness, `k=81/|U|`, or the derivation of eight capacity-27 demands from actual cube-value-set closure.  Inverse-lift/commutator convention can change the label by an invertible sign, but only permutes the histogram.

## Scope

This concerns p=3 and a conditional order-3^9 action family only.  Exact exponent 9 and actual cube-value-set closure are not checked on a group, no factor system is opened, images of order 27 or 81 survive, and `active_assignment_answered: no`.  The unrestricted odd-prime scope is unanswered.
