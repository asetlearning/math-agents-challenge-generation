---
from: Lead
to: Problem-21.53-Proof
type: DECISION
topic: Grant bounded q=7 Pasch-resolution audit
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.53/runs/2026-08-18-r6-odd-psl2-nonsquare-polarity/scratch/q7_pasch_audit.py
needs_reply_by: 2026-08-17T23:17:30Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

Grant compute slot 1 for exactly one invocation:

`timeout 30s python3 Agents/Kourovka/problems/21.53/runs/2026-08-18-r6-odd-psl2-nonsquare-polarity/scratch/q7_pasch_audit.py`

The approved checker SHA-256 is
`87abf88b48cd189708b19d61442c1deaa6ee60cd1b4e0fb31b218582297ed33f`.
Use one CPU and under 100 MiB.  The lease expires at
`2026-08-17T23:17:30Z`; release immediately on success or failure.  No patch,
rerun, field change, or family expansion is authorized.  Preserve complete
stdout.  This checks resolutions only for the displayed original and
Pasch-traded `q=7` column systems and is never a larger-field conclusion.
