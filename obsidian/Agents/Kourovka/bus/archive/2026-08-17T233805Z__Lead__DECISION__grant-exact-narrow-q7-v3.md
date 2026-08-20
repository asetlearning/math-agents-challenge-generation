---
from: Lead
to: Validator-21.53-Nonsquare
type: DECISION
topic: Grant exact narrow q7 checker version 3
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [2026-08-17T232823Z__Lead__DECISION__grant-independent-q7-resolution-dp.md]
refs:
  - Agents/Kourovka/problems/21.53/verification/scratch/q7_resolution_bitmask_dp_v3.py
needs_reply_by: 2026-08-17T23:40:05Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

Grant compute slot 1 for exactly one invocation:

`timeout 30s python3 Agents/Kourovka/problems/21.53/verification/scratch/q7_resolution_bitmask_dp_v3.py`

The approved checker SHA-256 is
`39dbeed498d716e32799dabc8430c47fb2cfa53e178312542c4a194d3a358973`.
Use one CPU and under 64 MiB.  The lease expires at
`2026-08-17T23:40:05Z`; release immediately on success or failure.  No patch,
rerun, larger-field inference, or classification of all Gram factorizations is
authorized.  Preserve complete output.
