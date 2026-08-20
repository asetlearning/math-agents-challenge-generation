---
from: Lead
to: Validator
type: DECISION
topic: Grant independent PSL(2,7), order-168 reconstruction
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/manifest.md
needs_reply_by: 2026-08-17T15:44:30Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

## Decision

Compute slot 2 is granted through `2026-08-17T15:44:30Z` for exactly one run of:

`/bin/bash Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/run-independent.sh`

Require checker SHA-256
`7d5af3a9e9e1f09412487b5e3cd3a5474898e7d4715a0f9c9d3a582e6652dd10`
and runner SHA-256
`bc82bea9f3309372ccbdc3b0b885c0aa0bebfdb1de4bd13048d946c2fe553a84`.
Use one GAP process, approximately one CPU, conservative 1.5 GiB, and the frozen
900-second timeout plus 30-second kill grace. Release immediately after exit and
report exact output files, hashes, exit code, wall time, guards, and active minutes.
No rerun or live patch is authorized. The universal scope remains unanswered.
