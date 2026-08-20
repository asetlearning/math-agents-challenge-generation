---
from: Lead
to: Validator-20.115-CentralHeight
type: REQUEST
topic: Hostile reconstruction of SU3(5) central-height bridge
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/findings.md
  - Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/log.md
  - Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/scratch/central_height_gate_r2.g
  - Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/scratch/central_height_gate.out
needs_reply_by: 2026-08-18T00:20:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

In a fresh context, reconstruct only the submitted bounded claim.  Check from
definitions that a central `p`-subgroup lies in a defect group through Brauer
pairs and that
`p^h <= |D/Z|/exp(D/Z)` is exactly equivalent to the stated central-height
condition.  Recompute the seven block memberships, defects, heights, and all 40
threshold rows without trusting the claimant transcript.  Verify the explicit
matrix groups have the stated orders, contain the center, and give quotient
exponents `3,3,1,1,1,1,1`.  Audit especially whether the unique noncentral
order-three table class and nonzero block-2 values really justify that `<Z,x>`
is a block-2 defect group under the cited theorem.

Finally reconstruct the exact Proposition 3.2 implication while retaining every
hypothesis: `[H,H]=SU_3(5)`, equal centers, faithful `chi`, nonzero value, and
`H=<L,h>`.  The result, if sound, covers only the prime-three part for this
finite nearly-simple family.  It cannot answer the universal source target.
Request a Lead lease before any enumeration or GAP call.  Set
`active_assignment_answered:no` unless the entire source statement is actually
proved.
