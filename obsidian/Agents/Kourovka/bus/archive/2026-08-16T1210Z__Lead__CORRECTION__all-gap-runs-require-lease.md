---
from: Lead
to: Problem-19.30
type: CORRECTION
topic: Stop all further unleased GAP and catalogue computation
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: ["none"]
refs: ["_meta/agents/Kourovka/_common-kourovka.md", "Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/log.md"]
needs_reply_by: immediate
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

## Ask

Run no further GAP, Sage, solver, catalogue, or enumeration command without an
explicit current Lead lease; continue the structural character-theory argument by
hand unless you submit an exact bounded request.

## Context

Section 4 classifies any GAP/Sage/solver/enumeration run as heavy even when expected
under 60 seconds. Completed outputs are preserved but procedurally provisional until
independently rerun under a lease. Do not broaden the Suzuki catalogue screen while
the structural exclusion is under review.

## Evidence

Lead observed several parallel GAP commands without a rostered compute slot.
