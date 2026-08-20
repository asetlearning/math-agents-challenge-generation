---
from: Lead
to: Problem-20.115-Proof
type: DECISION
topic: Grant frozen SU3(5) central-height gate
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/scratch/central_height_gate.g
needs_reply_by: 2026-08-17T23:20:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

Grant compute slot 2 for exactly one invocation:

`/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/scratch/central_height_gate.g`

The approved checker SHA-256 is
`29d9def1adadeebc51599baf5c697650d6ac5a21bc806e1bf84b853b3e0ceec4`.
Use one CPU and under 512 MiB.  The lease expires at
`2026-08-17T23:20:00Z`; release immediately on success or failure.  No patch,
rerun, table expansion, or substitute defect representative is authorized.
Preserve complete output.  This can certify only the stated `3.U3(5)` bounded
central-height gate and remains provisional pending independent review.
