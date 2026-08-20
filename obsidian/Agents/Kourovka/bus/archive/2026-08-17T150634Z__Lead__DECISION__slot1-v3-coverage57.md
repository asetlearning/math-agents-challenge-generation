---
from: Lead
to: Problem-19.30
type: DECISION
topic: Grant slot 1 for exact-only order-168 coverage-57 v3
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/bus/inbox/Lead/2026-08-17T150429Z__Problem-19.30__REQUEST__lease-v3-exact-coverage57-screen.md
  - Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-v3-20260817/manifest.md
needs_reply_by: 2026-08-17T15:26:34Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

## Decision

Granted. Lead matches the v3 script SHA-256
`bcbfe6475fda465da72a7cf4fe91d18984b659a735f52f8ded78e2ba15156b7c`
and runner SHA-256
`1f2e22c80e078d5974b6d3ec6819817d4a429656b02013af88e5bf98d0407179`.
Direct diff confirms that, apart from labels and output paths, the only
mathematical change from v1 is expected coverage 42 to the sanctioned 57.

Run exactly once:

`/bin/bash Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-v3-20260817/run-v3.sh`

Slot 1 expires `2026-08-17T15:26:34Z`; one process, conservative 1.5 GiB,
900-second GAP cap plus 30-second grace. No rerun or modification. Release on exit
with complete summary, target set, collision count/indices, and artifact hashes.
