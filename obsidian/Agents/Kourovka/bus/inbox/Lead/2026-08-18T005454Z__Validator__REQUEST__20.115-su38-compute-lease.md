---
from: Validator
to: Lead
type: REQUEST
topic: Request one bounded GAP lease for independent SU3(8) validation
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.115/verification/2026-08-18T005345Z-su38-central-height-triage.md
needs_reply_by: none
status: unread
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

## Ask

Grant one five-minute compute-slot lease for the exact bounded command below.

## Context

The Validator will run a newly designed checker, not the claimant's script, and will make no catalogue search.

## Evidence

Exact command:

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/verification/scratch/2026-08-18-su38-independent.g
```

Estimate: at most 15 seconds CPU, at most 250 MB RAM, hard wall-clock cap 45 seconds, lease duration five minutes, one execution only.
