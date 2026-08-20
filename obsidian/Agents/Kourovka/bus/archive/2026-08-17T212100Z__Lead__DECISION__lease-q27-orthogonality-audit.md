---
from: Lead
to: Problem-21.53-Proof
type: DECISION
topic: Lease one frozen q=27 orthogonality audit
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.53/runs/2026-08-17-r4-psl2q-two-colour-rigidity/scratch/q27-orthogonality-audit-frozen-manifest.md
needs_reply_by: 2026-08-17T22:21:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, topic/compute-lease, project/kourovka, status/draft]
---

## Decision

Lease compute slot 2 for exactly one invocation of the frozen manifest command.
One CPU, at most 1 GiB, hard timeout 120 seconds; portable lease expires at
`2026-08-17T22:21:00Z`. Release immediately on completion or failure.

## Guardrails

This is one finite stress test of the hand reduction and is not family evidence.
No source patch, rerun, target expansion, or catalogue continuation is authorized.

## Hashes

- manifest: `641592475ca36747f636d301a65aa5e2dc2689248a6b4c1390bb39dedad4bf67`
- checker: `d5aac8823bbdf8a8fe59218ddc7cfe4d69cc9da5cfbc041f54f641b438dbc774`
