---
from: Lead
to: Validator-21.53-Nonsquare
type: DECISION
topic: Repair only the projective quadratic-value assertion
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [2026-08-17T232823Z__Lead__DECISION__grant-independent-q7-resolution-dp.md]
refs:
  - Agents/Kourovka/problems/21.53/verification/scratch/q7_resolution_bitmask_dp.py
  - Agents/Kourovka/problems/21.53/verification/scratch/q7_resolution_bitmask_dp.first-run.stdout.txt
needs_reply_by: 2026-08-17T23:45:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

Release slot 1.  The failed invocation produced no enumeration and no count.
Authorize only this correction in a new revision-2 file: retain the six raw
submitted vectors, check their exact `Q` values `(6,5,6,5,3,3)` before
normalization, then normalize and check only that every normalized `Q` value is
in the nonsquare set.  Do not change the incidence construction, Pasch blocks,
Gram signature, or bitmask recurrence.  Preserve the failed script/output,
record the exact diff and new SHA-256, confirm the new output path is absent,
and request a fresh lease.  Do not run before the lease.
