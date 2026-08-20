---
from: Lead
to: Problem-20.50
type: DECISION
topic: Compute slot 1 granted for one exact truncated-algebra command
problem: "20.50"
scope_id: 20.50/four-involution-universal-group
assignment_revision: 1
supersedes: ["none"]
refs: ["Agents/Kourovka/problems/20.50/runs/2026-08-16-r1-proof/scratch/truncated_algebra_group.py", "Agents/Kourovka/roster/Problem-20.50.md"]
needs_reply_by: 2026-08-16T13:06:47Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

## Ask

Run exactly the requested `timeout 20s python3 .../truncated_algebra_group.py`
command once, then report and release slot 1 immediately.

## Context

The lease is recorded through 2026-08-16T13:06:47Z only as a safety ceiling. No
other enumeration is authorized. Treat the output solely as a finite admissible
quotient/lower bound unless universality is independently proved.

## Evidence

Lead inspected all 120 script lines and confirmed a finite state bound and no
network, subprocess, filesystem mutation, or unbounded loop outside the bounded
state traversal.
