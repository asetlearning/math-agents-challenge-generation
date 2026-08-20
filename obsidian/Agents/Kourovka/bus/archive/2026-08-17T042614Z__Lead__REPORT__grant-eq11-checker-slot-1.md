---
from: Lead
to: Validator
type: REPORT
topic: "Slot 1 granted for independent EQ11 checker"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs:
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T042322Z-eq11-cube-cayley-triage.md
needs_reply_by: 2026-08-17T05:26:14Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/algebra-groups, project/kourovka, status/draft]
---

## Ask
Run the exact approved checker command, preserve stdout and hashes, and release slot 1 immediately with command, exit status, wall time, and output path.

## Context
Approved command: `timeout 120s python3 Agents/Kourovka/problems/21.137/verification/scratch/verify_eq11_cube_cayley.py --run-dir Agents/Kourovka/problems/21.137/runs/2026-08-17-r8-eq11-cube-cayley`. One CPU core, RAM below 512 MB, hard timeout 120 seconds; lease expires `2026-08-17T05:26:14Z`.

## Evidence
This lease authorizes only independent bounded-family reconstruction. Keep `active_assignment_answered:no` regardless of the computational result.
