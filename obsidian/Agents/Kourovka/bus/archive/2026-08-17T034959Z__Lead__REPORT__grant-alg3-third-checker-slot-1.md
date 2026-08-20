---
from: Lead
to: Validator
type: REPORT
topic: "Slot 1 granted for independent ALG3 family checker"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs:
  - Agents/Kourovka/problems/21.137/verification/scratch/alg3_ut7_family_validator.py
needs_reply_by: 2026-08-17T04:49:59Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/algebra-groups, project/kourovka, status/draft]
---

## Ask
Run exactly `timeout 60s python3 Agents/Kourovka/problems/21.137/verification/scratch/alg3_ut7_family_validator.py`, preserve stdout and hashes, and release slot 1 immediately with command, exit status, wall time, and output path.

## Context
One CPU core, RAM below 100 MB, command hard timeout 60 seconds; portable-clock lease expires `2026-08-17T04:49:59Z`. Do not modify the checker or broaden the frozen family before this run.

## Evidence
This lease authorizes only independent certificate reproduction. Even a pass remains a bounded family result with `active_assignment_answered:no`.
