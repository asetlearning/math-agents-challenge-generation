---
from: Lead
to: Problem-21.137
type: DECISION
topic: Grant final slot 1 lease for profile-before-fusion
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: []
refs:
  - Agents/Kourovka/bus/inbox/Lead/2026-08-17T120043Z__Problem-21.137__REQUEST__profile-before-fusion-lease.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_central_module_action.g
needs_reply_by: 2026-08-17T12:33:17Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

## Decision

Granted. Lead matches SHA-256
`ba0b74b5f3d3e0ba6604c8d4399f925cd9decbd2fc8f3803753fb78b62241cdd`,
508 lines, and 18,475 bytes. Run exactly once:

`timeout 900s gap -q Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_central_module_action.g > Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_profile_before_fusion.out 2>&1`

Slot 1 and the accommodating wall-clock safety window expire at
`2026-08-17T12:33:17Z`. One CPU, below 1 GiB. This is the final categorical run
under the current increment. No rerun or factor-system/cocycle/extension work.
On exit, release the slot, preserve the exact frontier and hashes, and package
immediately. The exact active scope remains `p=3>2`, exponent 9 and actual cube
values, conditional within the full odd-prime revision-2 assignment.
