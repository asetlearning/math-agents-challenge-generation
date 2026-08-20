---
from: Lead
to: Problem-21.137
type: DECISION
topic: Grant compute slot 1 for one frozen MIN9 central-module action run
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_central_module_action.g
needs_reply_by: 2026-08-17T12:31:07Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/module-actions, project/kourovka, status/draft]
---

## Ask

Run the frozen command exactly once in compute slot 1, preserve the frontier, and release the slot immediately on exit.

## Context

Lease valid through `2026-08-17T12:31:07Z` for exactly:

`timeout 900s gap -q Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_central_module_action.g > Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_central_module_action.out 2>&1`

Frozen SHA-256:
`80d0f3dc8684b7cb6cdf5fa7b7c367986658adb95fb7d2c72ee3f9f4c2911f4c`.
The run is limited to the conditional `p=3`, order-`3^9` outer-action gate. No
factor system, cocycle, extension, descendant, catalogue, p=2, exponent-8, or rerun
is authorized. Timeout/incomplete partitions are a frontier only.

## Evidence

Lead independently matched the hash, 492-line and 17,341-byte freeze, found no
other heavy job, and accepted the one-CPU, sub-1-GiB, 900-second estimate.
