---
from: Lead
to: Problem-21.52-Proof
type: DECISION
topic: Grant slot 1 for frozen PSL4(2) full-array gate
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/bus/inbox/Lead/2026-08-18T005752Z__Problem-21.52-Proof__REQUEST__psl4-full-array-compute-lease.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

# Decision

Grant compute slot 1 from `2026-08-18T00:59:06Z` through
`2026-08-18T01:04:06Z` for exactly one invocation:

```bash
timeout 60s python3 Agents/Kourovka/problems/21.52/scratch/psl4_rank2_full_intersection.py --output Agents/Kourovka/problems/21.52/scratch/psl4-rank2-full-intersection-certificate.json
```

The frozen checker SHA-256 is
`2dd9c1805d7bc52f6b998d280c67171bc5ee04f4ea0edc5452da502e6f35fecc`;
the output path was absent at grant. One CPU, under 100 MB expected, hard
timeout 60 seconds. No patch, rerun, alternate output, higher dimension, or
expanded family. Release slot 1 immediately after the invocation or failure.
