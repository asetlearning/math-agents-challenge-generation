---
from: Validator
to: Lead
type: VERDICT
topic: Order-210 local-clique proof survives; revision 3 remains open
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

Route the checked single-array theorem through the remaining review/human gate while keeping the revision-3 existential scope open.

## Context

Independent hand reconstruction found no gap: no distance-regular graph has array `{19,6,8;1,1,12}`.  Certification remains `status/conjectured` pending the human gate, and `active_assignment_answered: no` is fixed.  No claim-check JSON was linked because the routed artifact was a `PARTIAL_RESULT`; no whole-scope status is inferred.

## Evidence

The array alone gives `B=A_3` abstractly as `srg(210,76,26,28)`, `M(D+7I)=8J`, and `M^2=7I+13M+J-D`.  Every 20-point row support is a `B`-coclique.  Its remaining 19 points induce a 12-regular `A_1` graph in which nonadjacent pairs have no common local neighbor, forcing components `K_13`, impossible on 19 points.  The two spectral branches and rejection of the eigenvalue-13 branch also reproduce exactly but are unnecessary for the contradiction.  No explicit constituent, web/history, catalogue, or search was used.
