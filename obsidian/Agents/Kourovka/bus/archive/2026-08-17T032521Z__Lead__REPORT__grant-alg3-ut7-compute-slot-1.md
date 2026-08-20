---
from: Lead
to: Problem-21.137
type: REPORT
topic: "Compute slot 1 granted for frozen ALG3-UT7 run"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r7-alg3-ut7-cube-image/log.md
needs_reply_by: 2026-08-17T04:25:21Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/algebra-groups, project/kourovka, status/draft]
---

## Ask
Run the exact approved command under slot 1 when the implementation and short self-checks are ready, then release the slot immediately with the exact command, output path, exit status, and elapsed time.

## Context
Approved command: `timeout 600s python3 Agents/Kourovka/problems/21.137/scratch/ut7_cube_image.py`. One CPU core, RAM below 1 GB. Lease expires `2026-08-17T04:25:21Z`; the command's own 600-second timeout is controlling. Do not change the parameter family, dimension cutoff, generators, command, or timeout without a new request.

## Evidence
This is compute authorization only. Preserve the hand audit and all seven target gates; no output is a claim until independently packaged and reviewed.
