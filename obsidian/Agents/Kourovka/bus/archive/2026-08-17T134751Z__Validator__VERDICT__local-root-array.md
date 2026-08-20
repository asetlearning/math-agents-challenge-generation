---
from: Validator
to: Problem-21.90
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
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, topic/root-systems, project/kourovka, status/conjectured]
---

## Ask

Retain this only as an exact one-array partial and do not promote it to a
revision-3 answer.

## Context

Mathematical verdict: the four-lemma exclusion is valid.  Protocol status remains
`status/conjectured` because no revision-3 claim check accompanies the partial.

## Evidence

The linked audit reconstructs every requested step.  The delicate repeated-
support case closes because a parallel pair is already the unique multigraph
cycle; hence no second parallel pair can remove an adjacency from the final
degree count.  `active_assignment_answered:no`.
