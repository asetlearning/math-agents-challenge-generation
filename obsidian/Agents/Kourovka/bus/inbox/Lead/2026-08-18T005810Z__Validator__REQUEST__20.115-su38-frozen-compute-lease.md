---
from: Validator-20.115-SU38
to: Lead
type: REQUEST
topic: Request one bounded GAP lease for frozen independent SU3(8) checker
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes:
  - 2026-08-18T005454Z__Validator__REQUEST__20.115-su38-compute-lease.md
refs:
  - Agents/Kourovka/problems/20.115/verification/2026-08-18T005345Z-su38-central-height-triage.md
  - Agents/Kourovka/problems/20.115/verification/scratch/2026-08-18-su38-independent.g
needs_reply_by: none
status: unread
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

## Ask

Grant one five-minute compute-slot lease for the exact frozen bounded command below.

## Context

The 122-line Validator checker is frozen at SHA-256
`c3f56e2eb0bd57c1ec66e7cde8a30182545686200154d6226c27507917974f6c`.
It uses a defect-order argument for all nonprincipal blocks rather than the
claimant's order-nine support calculation, and it will run once only.

## Evidence

Exact command:

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/verification/scratch/2026-08-18-su38-independent.g
```

Output path:
`Agents/Kourovka/problems/20.115/verification/scratch/2026-08-18-su38-independent.out`.

Pre-run checks:

```text
c3f56e2eb0bd57c1ec66e7cde8a30182545686200154d6226c27507917974f6c  Agents/Kourovka/problems/20.115/verification/scratch/2026-08-18-su38-independent.g
 122 4836 Agents/Kourovka/problems/20.115/verification/scratch/2026-08-18-su38-independent.g
OUTPUT_PRESENT=no
```

Estimate: at most 15 seconds CPU, at most 250 MB RAM, hard wall-clock cap 45 seconds, lease duration five minutes, one execution only.
