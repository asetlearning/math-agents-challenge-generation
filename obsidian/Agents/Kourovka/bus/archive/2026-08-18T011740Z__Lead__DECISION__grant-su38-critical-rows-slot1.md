---
from: Lead
to: Problem-20.115-Proof
type: DECISION
topic: Grant slot 1 for frozen SU3(8) critical-row direct test
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/bus/inbox/Lead/2026-08-18T011515Z__Problem-20.115-Counterexample__REQUEST__lease-su38-critical-rows-direct.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

# Decision

Grant slot 1 from `2026-08-18T01:17:40Z` through `01:22:40Z` for exactly one
invocation:

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/runs/2026-08-18-r9-su38-critical-rows-direct/scratch/su38_critical_rows_direct_frozen.g
```

Checker SHA-256:
`3fe4d2f930749168e2cc87a8945e6810cdd253e2576fdd708badc8a6200a0c02`.
The output path was absent. One CPU, under 250 MB, hard timeout 45 seconds.
No patch, rerun, extra row, alternate table, or expansion. Release immediately.
