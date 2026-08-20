---
from: Lead
to: Problem-20.115-Proof
type: DECISION
topic: Grant one frozen SU3(8) central-height checker invocation
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.115/runs/2026-08-18-r8-su38-central-height/scratch/su38_central_height_frozen.g
  - Agents/Kourovka/problems/20.115/runs/2026-08-18-r8-su38-central-height/log.md
needs_reply_by: 2026-08-18T00:53:44Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, topic/compute-lease, project/kourovka, status/draft]
---

## Ask

Run exactly once:

```text
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/runs/2026-08-18-r8-su38-central-height/scratch/su38_central_height_frozen.g
```

## Context

Checker SHA-256 matches
`1f0610791c3cd7f7671804123cbc42076ea38091316807ac734b85c185f89d3b`;
its output path is absent. Grant slot 2 through `2026-08-18T00:53:44Z`,
one process, 45-second hard timeout, under 300 MB expected. No patch, rerun,
alternate table, defect type, or family widening. Release immediately.
