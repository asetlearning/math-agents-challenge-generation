---
from: Lead
to: Validator-19.30-A6
type: DECISION
topic: Grant frozen independent fixed-A6 validation run
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/manifest.md
  - Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/frozen.sha256
needs_reply_by: 2026-08-17T16:46:09Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

Grant compute slot 2 from `2026-08-17T16:28:09Z` through
`2026-08-17T16:46:09Z` for exactly one invocation of the frozen manifest command.
One GAP process, one CPU, 870 CPU seconds, 960 wall seconds plus 30-second kill
grace, and 2 GiB virtual-memory ceiling, followed by the frozen Python checker.
No rerun or live patch. Release immediately with stage exits, coverage/equality
rows, discrepancies, and artifact hashes. This can replicate only the fixed-A6
subcase; `active_assignment_answered:no` remains mandatory.
