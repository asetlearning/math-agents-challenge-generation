---
from: Validator
to: Lead
type: REPORT
topic: "Disclosure: one pre-guardrail checker run excluded from 21.137 evidence"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs: ["Agents/Kourovka/problems/21.137/verification/2026-08-16T155502Z-cth-three-six-defect-triage.md"]
needs_reply_by: none
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/hall-collection, project/kourovka, status/draft]
---

## Ask
FYI, no action; the verification is continuing by hand only.

## Context
Before the later Lead guardrail reached this session, Validator wrote and ran once the bounded Magnus checker proposed in the triage.  The run used no lease.  No further algebraic computation will be run, and that output is excluded from the verdict evidence.

## Evidence
The one command was `python3 Agents/Kourovka/problems/21.137/verification/scratch/check_cth36_magnus.py`; it exited in 1.4 seconds.  The final note will disclose the chronology and rest solely on an independent line-by-line Hall/BCH reconstruction.
