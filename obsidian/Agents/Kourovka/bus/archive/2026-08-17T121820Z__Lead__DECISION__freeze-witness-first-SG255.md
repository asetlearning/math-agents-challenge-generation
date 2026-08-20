---
from: Lead
to: Problem-20.49
type: DECISION
topic: Freeze a corrected witness-first completion of SG255
problem: 20.49
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
supersedes: []
refs:
  - Agents/Kourovka/bus/inbox/Lead/2026-08-17T121548Z__Problem-20.49__REPORT__slot2-released-partial-sg255.md
  - Agents/Kourovka/bus/inbox/Lead/2026-08-17T121713Z__Problem-20.49__CHECKPOINT__sg255-timeout-decision.md
  - Agents/Kourovka/roster/Problem-20.49.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/exponent, project/kourovka, status/draft]
---

## Decision

Choose refinement A. Treat the manually preserved first-run transcript only as an
operational diagnostic, not mathematical evidence. Freeze the exact persistent
`SG255-WITNESS-FIRST` pass specified in the roster. It must cover precisely every
nonsoluble SmallGroups representative of order at most 255, preserve one exact
full-exponent pair immediately for each negative row, and exhaust all pairs only
for a genuine candidate. Do not run it before a fresh hash-matched Lead lease and
do not enlarge the layer.
