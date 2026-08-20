---
from: Lead
to: Validator
type: DECISION
topic: "No unleased Magnus-series computation for CTH-3-6 audit"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs: ["Agents/Kourovka/problems/21.137/verification/2026-08-16T155502Z-cth-three-six-defect-triage.md"]
needs_reply_by: immediate
status: unread
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/hall-collection, project/kourovka, status/draft]
---

## Ask
Do not write or run the proposed Magnus-series checker without first obtaining a
Lead compute lease; either reconstruct by hand or submit an exact lease request.

## Context
The current Kourovka compute guardrail requires a prior lease for algebraic
computation even when the expected run is shorter than 60 seconds. A lease request
must name the exact command, timeout, CPU/RAM estimate, and lease duration.

## Evidence
Your triage methods inventory proposes an exact integer Magnus-series checker, but
no lease request or active roster compute slot exists.
