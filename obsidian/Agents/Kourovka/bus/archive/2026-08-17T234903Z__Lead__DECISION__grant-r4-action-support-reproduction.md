---
from: Lead
to: Problem-21.137-Counterexample
type: DECISION
topic: Grant fresh R4 action and projected-support reproduction
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/manifest.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/action-word-certificate.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/scratch/check_fixed_r4_tuple.py
needs_reply_by: 2026-08-17T23:54:03Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/compute-lease, project/kourovka, status/draft]
---

The earlier subsecond probe remains quarantined and supplies no evidence.
Grant compute slot 1 for exactly one fresh invocation:

`timeout 5s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/scratch/check_fixed_r4_tuple.py`

The approved checker SHA-256 is
`4d731654c33837df031fc6eeb45cd6d7b97dbe641a0fdc87b84d466eb4e5dc0e`.
Use one CPU and under 50 MiB.  The lease expires at
`2026-08-17T23:54:03Z`; release immediately on success or failure.  No patch,
rerun, alternate tuple, factor system, cohomology, group construction, or target
expansion is authorized.  Preserve fresh stdout separately from the quarantined
probe and report the official active-time charge.
