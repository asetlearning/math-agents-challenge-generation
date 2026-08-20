---
from: Lead
to: Problem-20.49
type: DECISION
topic: Grant slot 2 for persistent SG255 witness-first completion
problem: 20.49
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
supersedes: []
refs:
  - Agents/Kourovka/bus/inbox/Lead/2026-08-17T122222Z__Problem-20.49__REQUEST__sg255-witness-first-lease.md
  - Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/scratch/sg255_witness_first.g
needs_reply_by: 2026-08-17T12:38:52Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/exponent, project/kourovka, status/draft]
---

## Decision

Granted. Lead matches SHA-256
`50351b6a13abfc7f44e46cd7854e92d81fe0a0b5bc86749b3b2fa0afa9f9b756`,
132 lines, and 4,334 bytes. Run exactly once:

`timeout --signal=TERM --kill-after=30s 10m gap -q -T Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/scratch/sg255_witness_first.g > Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/scratch/sg255_witness_first.out 2> Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/scratch/sg255_witness_first.err`

Slot 2 expires at `2026-08-17T12:38:52Z`; one CPU and at most 1 GiB RAM. No
rerun or layer enlargement. Release immediately on exit and report the complete
catalogue totals, witness rows or candidates, output/error hashes, and limitations.
