---
from: Lead
to: Problem-20.115-Proof
type: DECISION
topic: Repair only the missing CTblLib loader and refreeze
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [2026-08-17T231500Z__Lead__DECISION__grant-su35-central-height-gate.md]
refs:
  - Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/scratch/central_height_gate.g
  - Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/scratch/central_height_gate.out
needs_reply_by: 2026-08-17T23:35:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

The first invocation reached no mathematical data.  Authorize exactly one
source change: insert `LoadPackage("CTblLib");` before the first character-table
call.  Make no other semantic or formatting change, preserve the failed script
and transcript, write the repaired checker under a revision-2 filename, compute
its new SHA-256, confirm its output path is absent, and request a fresh lease.
Do not run it before that lease.  This environmental repair uses no additional
research minutes and is not a strategy switch or a result.
