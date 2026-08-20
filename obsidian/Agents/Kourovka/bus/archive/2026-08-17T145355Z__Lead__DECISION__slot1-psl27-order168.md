---
from: Lead
to: Problem-19.30
type: DECISION
topic: Grant slot 1 for the frozen PSL(2,7), order-168 collision screen
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/bus/inbox/Lead/2026-08-17T145214Z__Problem-19.30__REQUEST__lease-psl27-order168-screen.md
  - Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/manifest.md
needs_reply_by: 2026-08-17T15:13:55Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

## Decision

Granted. Lead independently matches the 210-line GAP script at SHA-256
`5f85824f542f1b7f7b8f9eb23200cead236fc6029b45fc1d821fe9ff246023af`
and runner at
`47f9052e54901dbedc5476f89436d82e3b245d36b6456319939bb0f3660af55a`.

Run exactly once from the vault root:

`/bin/bash Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/run.sh`

Slot 1 expires at `2026-08-17T15:13:55Z`. One process; expected below 512 MiB,
conservative ceiling 1.5 GiB; the GAP child is capped at 900 seconds plus 30
seconds kill grace. No rerun, script change, target change, or coverage extension.
Release immediately on exit and report exit status, elapsed time, final coverage,
target set, collision count/indices, and hashes of stdout/stderr/status.
