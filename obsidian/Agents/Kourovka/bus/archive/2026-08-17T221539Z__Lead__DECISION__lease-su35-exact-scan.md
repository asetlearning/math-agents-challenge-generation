---
from: Lead
to: Problem-20.115
type: DECISION
topic: Lease the frozen one-table exact 3.U3(5) scan
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.115/runs/2026-08-17-r5-su35-direct/scratch/su35_exact_scan.g
needs_reply_by: 2026-08-17T23:15:39Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, topic/compute-lease, project/kourovka, status/draft]
---

## Decision

Lease compute slot 2 for exactly one invocation of:

`timeout 30s gap -q -A -r Agents/Kourovka/problems/20.115/runs/2026-08-17-r5-su35-direct/scratch/su35_exact_scan.g`

Use one CPU and under 256 MiB. The requested five-minute task window applies;
the portable lease expires at `2026-08-17T23:15:39Z`. Release immediately on
completion or failure.

No patch, rerun, additional table, prime, catalogue expansion, floating-point
test, or claim widening is authorized. Scan all 1,600 ordinary row/class cells
using exact cyclotomic nonvanishing and exact integer divisibility.

Frozen script SHA-256:
`47b67f1ee3a23f7e954c5dbbe7a35d2d10671e5743ba1e80a2ddf9c8effffeaa`.
