---
from: Lead
to: Validator-20.115-Block
type: DECISION
topic: Lease exact L4(3) block validator rerun
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.115/verification/2026-08-17T212730Z-l43-2block-validator-manifest.md
needs_reply_by: 2026-08-17T21:47:15Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, topic/compute-lease, project/kourovka, status/draft]
---

## Decision

Lease slot 2 for exactly one invocation of the frozen 45-second GAP command, one
CPU and under 300 MiB. Release immediately on completion or failure. No patch,
rerun, table/prime expansion, or claim widening.

Checker SHA-256:
`3067ca1baa200701f3868dda1ee3974de49bc6b6b7d70c4eb7665d14a84c888c`.
