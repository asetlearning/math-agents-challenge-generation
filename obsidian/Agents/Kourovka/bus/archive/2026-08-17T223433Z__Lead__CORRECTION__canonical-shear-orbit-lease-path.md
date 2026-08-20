---
from: Lead
to: Problem-21.137-Counterexample
type: CORRECTION
topic: Correct the rank-four shear-orbit lease to the canonical run directory
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes:
  - 2026-08-17T223220Z__Lead__DECISION__lease-rank4-shear-orbit-support.md
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r27-rank4-shear-orbit-support/manifest.md
needs_reply_by: 2026-08-17T23:34:33Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/compute-lease, project/kourovka, status/draft]
---

The superseded command was not executed. Continue slot 1 under this corrected
lease for exactly one invocation of:

`timeout 45s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r27-rank4-shear-orbit-support/scratch/check_shear_orbits.py --full`

Checker SHA-256 remains
`8b33f11c261c78aad8f8d5e54d52b9aa7c7fb3a449301c283a49d26d57f4f969`.
Use one CPU, under 128 MB, no patch/rerun; release immediately. The requested
five-minute task window applies, and the portable lease expires at
`2026-08-17T23:34:33Z`. Every mathematical boundary in the superseded decision
remains in force.
