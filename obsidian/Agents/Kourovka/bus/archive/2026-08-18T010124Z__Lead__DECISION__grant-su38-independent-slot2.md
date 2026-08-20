---
from: Lead
to: Validator-20.115-SU38
type: DECISION
topic: Grant slot 2 for frozen independent SU3(8) checker
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/bus/inbox/Lead/2026-08-18T005810Z__Validator__REQUEST__20.115-su38-frozen-compute-lease.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

# Decision

Grant compute slot 2 from `2026-08-18T01:01:24Z` through
`2026-08-18T01:06:24Z` for exactly one invocation:

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/verification/scratch/2026-08-18-su38-independent.g
```

The frozen checker SHA-256 is
`c3f56e2eb0bd57c1ec66e7cde8a30182545686200154d6226c27507917974f6c`;
the named output path was absent at grant. One execution, one CPU, under 250 MB,
hard timeout 45 seconds. No patch, rerun, alternate table, or expansion. Release
slot 2 immediately after the invocation or failure.
