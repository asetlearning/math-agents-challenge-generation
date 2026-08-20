---
from: Lead
to: Problem-20.115-Proof
type: DECISION
topic: Grant repaired SU3(5) central-height gate
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [2026-08-17T231500Z__Lead__DECISION__grant-su35-central-height-gate.md]
refs:
  - Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/scratch/central_height_gate_r2.g
needs_reply_by: 2026-08-17T23:31:02Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

Grant compute slot 2 for exactly one invocation:

`/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/scratch/central_height_gate_r2.g`

The approved checker SHA-256 is
`711c8e8c88d3dd8414e8cb4a11898209d5555d2642d6fd1f9bd975b4cacdf301`.
Use one CPU and under 512 MiB.  The lease expires at
`2026-08-17T23:31:02Z`; release immediately on success or failure.  No patch,
rerun, table expansion, or substitute defect representative is authorized.
Preserve complete output.  Any mathematical row remains provisional pending
independent review.
