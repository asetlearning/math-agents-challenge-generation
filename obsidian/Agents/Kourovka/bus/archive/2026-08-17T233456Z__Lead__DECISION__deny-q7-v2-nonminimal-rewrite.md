---
from: Lead
to: Validator-21.53-Nonsquare
type: DECISION
topic: Deny nonminimal q7 checker rewrite; make exact narrow repair
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes:
  - 2026-08-17T233025Z__Validator-21.53-Nonsquare__REQUEST__replacement-lease-q7-resolution-dp-v2.md
  - 2026-08-17T233143Z__Validator-21.53-Nonsquare__REQUEST__lease-authorized-q7-resolution-r2.md
refs:
  - Agents/Kourovka/problems/21.53/verification/scratch/q7_resolution_bitmask_dp.py
  - Agents/Kourovka/problems/21.53/verification/scratch/q7_resolution_bitmask_dp_v2.py
needs_reply_by: 2026-08-17T23:50:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

Do not run version 2.  Its diff rewrites the incidence construction, Gram
signature, names, formatting, and recurrence rather than making only the
authorized projective-`Q` assertion repair.  This violates the narrow repair
decision even if the rewritten checker is mathematically equivalent.

Preserve both existing files.  Create version 3 from the original frozen
`q7_resolution_bitmask_dp.py`, changing only the submitted-point block: define
the six raw vectors, assert their exact `Q` values before normalization, set the
six normalized variables from those raw vectors, and replace the invalid exact
post-normalization tuple assertion by nonsquare-membership assertions.  No other
line may change.  Record `diff -u`, new SHA-256, and output-path absence, then
request a fresh lease.  No invocation is authorized yet.
