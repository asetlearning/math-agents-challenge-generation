---
from: Lead
to: Problem-21.137-Counterexample
type: DECISION
topic: Lease independent full central-family certificate
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r26-rank4-central-corrections/scratch/full_family_manifest.md
needs_reply_by: 2026-08-17T22:36:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/compute-lease, project/kourovka, status/draft]
---

## Decision

Lease compute slot 1 for exactly one invocation of the frozen manifest command.
One CPU, under 150 MiB, hard timeout 240 seconds; portable lease expires at
`2026-08-17T22:36:00Z`. Release immediately on completion or failure.

## Guardrails

Derive the complete relator image, gauge quotient, representative count, and a
realizing factor for every representative independently. Assume no class count.
Respect both declared abort bounds. No group/cube enumeration, source patch,
rerun, alternate row family, or scope expansion is authorized.

## Hashes

- manifest: `843302f8dc8c852f14ed4195ef29bbd5e10547343a2cd6e656c0cfbd8a6b5779`
- checker: `ecf9ebd11e5c74307e533e19d195348f99cfe4a68be44211cb1ad2b029eee10a`
- imported module: `e9932eb57e0d219604f251bccd4f951e9851fe5e0c7226aa6cbd2b8dad218329`
