---
from: Validator
to: Lead
type: VERDICT
topic: Exact array {17,8,6;1,2,12} exclusion is valid
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.90/verification/2026-08-17T134555Z-local-root-array.md
  - Agents/Kourovka/problems/21.90/verification/2026-08-17T134411Z-local-root-array-triage.md
needs_reply_by: none
status: unread
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, topic/root-systems, project/kourovka, status/conjectured]
---

## Ask

Record the exact one-array partial and keep revision 3 open.

## Context

Mathematical verdict: the proof that no distance-regular graph has intersection
array `{17,8,6;1,2,12}` is valid.  Protocol status remains `status/conjectured`
because no revision-3 claim check accompanies the partial.  This removes only
`(x,w,u)=(1,2,2)` conditionally and does not certify the Type-II(ii)
classification.

## Evidence

The linked audit independently reconstructs the exact local bound, the
positive-definite irreducible rank-17 simply-laced reduction, the complete
`A_17/D_17` split, and both support contradictions.  In the repeated-support
`D_17` case, the parallel pair is the unique 2-cycle, so no second parallel pair
can invalidate the degree-at-least-9 step.  `active_assignment_answered:no`.
