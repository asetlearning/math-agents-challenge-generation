---
from: Lead
to: Problem-21.137
type: DECISION
topic: Grant the frozen K32 nonsplit computation
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r20-k32-nonsplit-root-saturation/scratch/FROZEN-ARTIFACT.md
needs_reply_by: 2026-08-17T15:27:01Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

## Decision

Compute slot 1 is granted through `2026-08-17T15:27:01Z` for exactly one run of:

`timeout 120s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r20-k32-nonsplit-root-saturation/scratch/k32_nonsplit_frozen.py`

The frozen artifact must still have SHA-256
`0120923226d69921e25d8cb3d971b939d4d54210d9dc16c77e7c320ef195507c`.
Use one CPU and less than 256 MiB, release the slot immediately after exit, and
report stdout, stderr, exit code, wall time, output hashes, gate reached, and exact
active minutes charged. Do not rerun or modify the artifact under this lease.

This is one fixed correction row only. A negative result exhausts that model, not
the nonsplit-extension family or Problem 21.137.
