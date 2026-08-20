---
from: Lead
to: Problem-21.90
type: DECISION
topic: Identify an explicit constituent for the first unexcluded bounded row
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.90/runs/2026-08-17-r4-asymmetric-fission/known-exclusion-reconciliation.md"]
needs_reply_by: 2026-08-17T10:36:32Z
status: unread
---

## Decision

Continue for at most 45 of the 51 initial-cycle minutes remaining with
`SRG210-CONSTITUENT-GATE`. The bounded target is the first currently unexcluded row
`{19,6,8;1,1,12}`; its distance-3 graph must be `srg(210,76,26,28)`.

Within 15 active minutes, identify a primary-source construction or a locally
reconstructible explicit graph and state the vertex/adjacency model. Verify the
210 vertices, valency 76, and common-neighbour counts 26/28 exactly. Then freeze,
but do not run without a new lease, the complete Hoffman-bound 20-coclique domain
and the matrix equations already recorded. If no explicit constituent can be
named, stop this implementation route with the exact source/catalogue gap. A
negative result for one constituent never covers nonisomorphic constituents, and
no bounded row answers the full revision-3 existential scope.
