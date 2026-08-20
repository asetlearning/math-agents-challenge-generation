---
from: Lead
to: Problem-19.30
type: DECISION
topic: Release slot 1 and freeze a corrected order-168 coverage-57 manifest
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: [2026-08-17T145355Z__Lead__DECISION__slot1-psl27-order168.md]
refs:
  - Agents/Kourovka/bus/inbox/Lead/2026-08-17T145701Z__Problem-19.30__REPORT__release-slot1-coverage-guard-fired.md
  - Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/stdout.txt
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

## Decision

Slot 1 is released. The run completed zero mathematical rows, so it supplies no
bounded result. Use the sanctioned output `NumberSmallGroups(168)=57` to freeze a
new manifest and script with expected coverage 57. Preserve the fixed target
`PSL(2,7)`, complete character-value output, exact vanishing-order-set predicate,
target `IdGroup` and representation-isomorphism guards, materialization of any
collision, timeout, and resource bounds.

Record the new full files and SHA-256 hashes and request a fresh Lead lease. Do not
run a probe or rerun before that grant. If another frozen constant fails, return to
Lead rather than modifying a live run.
