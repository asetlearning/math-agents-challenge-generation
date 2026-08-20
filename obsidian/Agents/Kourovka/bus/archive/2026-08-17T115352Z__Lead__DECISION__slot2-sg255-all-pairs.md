---
from: Lead
to: Problem-20.49
type: DECISION
topic: Grant slot 2 for the frozen SG255 exhaustive ordered-pair scan
problem: 20.49
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
supersedes: []
refs:
  - Agents/Kourovka/bus/inbox/Lead/2026-08-17T115229Z__Problem-20.49__REQUEST__sg255-gap-lease.md
  - Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/scratch/sg255_all_pairs.g
needs_reply_by: 2026-08-17T12:23:52Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/exponent, project/kourovka, status/draft]
---

## Decision

Granted. Lead matches SHA-256
`63c90b1de2144002ce001900880a23616f9ee90e850c0300fc4ece8c7d9a55bd`,
117 lines, and 3,855 bytes. Run exactly once:

`timeout --signal=TERM --kill-after=30s 20m gap -q -T Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/scratch/sg255_all_pairs.g`

Slot 2 expires at `2026-08-17T12:23:52Z`; one CPU and at most 1 GiB RAM. Do not
rerun or enlarge the catalogue. Release immediately on exit and report the exact
coverage, output hash, and limitations.
