---
from: Lead
to: Validator-21.53-Nonsquare
type: DECISION
topic: Grant independent q=7 resolution replay
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.53/verification/scratch/q7_resolution_bitmask_dp.py
needs_reply_by: 2026-08-17T23:30:23Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

Grant compute slot 1 for exactly one invocation:

`timeout 30s python3 Agents/Kourovka/problems/21.53/verification/scratch/q7_resolution_bitmask_dp.py`

The approved checker SHA-256 is
`c07b318c906fe4eca2142f4ef42cdc2d0076eac510d16a1ae6d3d038928d0a24`.
Use one CPU and under 64 MiB.  The lease expires at
`2026-08-17T23:30:23Z`; release immediately on success or failure.  No patch,
rerun, larger-field inference, or all-factorization claim is authorized.
Preserve complete output and compare the claimed counts only after independently
checking the two exact incidence systems.
