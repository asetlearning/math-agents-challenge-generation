---
from: Lead
to: Problem-19.30
type: DECISION
topic: Grant the frozen A6 order-360 vanishing-set screen
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/a6-order360-freeze.md
  - Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/a6_order360_frozen.sha256
needs_reply_by: 2026-08-17T16:08:35Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

## Decision

Compute slot 2 is granted through `2026-08-17T16:08:35Z` for exactly one run of:

`/usr/bin/timeout --signal=TERM --kill-after=30s 960s /usr/bin/bash Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/run_a6_order360_screen.sh`

Require manifest SHA-256
`49eb981620fb1f03ddbaf26d56c9c86edf8755c3b809726d337594388b26157c`
and every contained hash. Use one GAP process, the frozen 2 GiB address ceiling,
870 CPU-second cap, and 960-second outer wall timeout. Release immediately after
exit and report output hashes, complete coverage, target row, collision rows,
runtime, exit status, and exact active minutes. No rerun or live patch. Zero
collisions answer only the fixed A6 subcase.
