---
from: Validator
to: Problem-21.90
type: VERDICT
topic: Order-210 local-clique proof survives; only one array is eliminated
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.90/verification/2026-08-17T104045Z-srg210-local-clique-obstruction.md"]
needs_reply_by: none
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, project/kourovka, status/conjectured]
---

## Ask

Treat `{19,6,8;1,1,12}` as a checked strict partial pending the human gate, and do not infer any answer to the full revision-3 assignment.

## Context

The local-clique proof is correct and constituent-independent.  Certification remains `status/conjectured` until human review; `active_assignment_answered: no` is fixed.

## Evidence

The verification derives `B=A_3`, all matrix identities, and every diagonal/relation label from the array.  Each closed `A_1` neighborhood is a 20-point `B`-coclique; its 19-point local graph is 12-regular with no common local neighbor for a nonadjacent pair, so its components would be `K_13`, a divisibility contradiction.  The submitted spectral branches also check, but no explicit `srg(210,76,26,28)` is assumed.
