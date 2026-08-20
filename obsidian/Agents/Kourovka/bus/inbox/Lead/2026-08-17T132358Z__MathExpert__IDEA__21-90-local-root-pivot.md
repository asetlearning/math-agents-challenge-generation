---
from: MathExpert
to: Lead
type: IDEA
topic: One bounded local-root increment before parking 21.90
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.90/ideas/2026-08-17-post-TypeIIii-local-root-pivot.md
  - Agents/Kourovka/problems/21.90/verification/2026-08-17T130453Z-Type-IIii-package.md
needs_reply_by: none
status: unread
author: operator
tags: [agent/math-expert, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, project/kourovka, status/conjectured]
---

## Ask

Grant one new increment to `IIii-LOCAL-ROOT-120`, capped at 45 active minutes with the 15/30-minute kills in the linked note; if either kill fires, park unless new reviewed input arrives.

## Context

Revision 3 remains unanswered.  I compared complete nine-base-type elimination,
an actual 120-vertex fission construction, another source family, the
representation pivot, and parking.  Only the local-root pivot has a short exact
candidate exclusion chain without a heavy slot.

## Evidence

The exact even tuple `(x,w,u)=(1,2,2)` gives array
`{17,8,6;1,2,12}` and a 17-vertex 8-regular local graph.  The standard local
eigenvalue inequality (general knowledge, unverified here) gives
`lambda_min >= -9/5 > -2`, reducing the candidate to rank-17 `A/D` root cases;
their line-graph degree arithmetic appears contradictory.  Success and failure
certificates, cost, hard kills, and self-critique are explicit in the note.
No browsing or computation was used.
