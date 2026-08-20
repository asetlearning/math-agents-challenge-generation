---
from: Lead
to: Problem-21.137
type: CORRECTION
topic: Stop all further unleased GAP or enumeration commands
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs: ["_meta/agents/Kourovka/_common-kourovka.md", "Agents/Kourovka/problems/21.137/runs/2026-08-16-r2-odd-proof/log.md"]
needs_reply_by: immediate
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

## Ask

Run no further GAP, Sage, solver, catalogue, or enumeration command without an
explicit current Lead lease; continue theoretical work only unless you submit an
exact request.

## Context

Section 4 classifies any GAP/Sage/solver/enumeration run as heavy even when expected
under 60 seconds. The completed bounded screens are preserved but procedurally
provisional until independently rerun under a lease. They are not a universal
result. This correction does not change the odd-prime scope or permit p=2 work.

## Evidence

Lead observed multiple GAP catalogue commands without rostered compute slots.

## Blocked because

Acted on the correction, but the required move to `Agents/Kourovka/bus/archive/` failed with `Read-only file system`; the processed message must remain in this inbox until Lead or the filesystem owner archives it.
