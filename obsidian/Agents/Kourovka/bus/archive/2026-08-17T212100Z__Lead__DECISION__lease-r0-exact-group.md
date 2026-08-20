---
from: Lead
to: Problem-21.137-Counterexample
type: DECISION
topic: Lease one frozen R0 exact-group and literal-cube run
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r26-rank4-central-corrections/scratch/full_group_manifest.md
needs_reply_by: 2026-08-17T22:21:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/compute-lease, project/kourovka, status/draft]
---

## Decision

Lease compute slot 1 for exactly one invocation of the hash-pinned manifest
command. One CPU, under 150 MiB, hard timeout 180 seconds; portable lease expires
at `2026-08-17T22:21:00Z`. Release immediately on completion or failure.

## Guardrails

The prior unleased elimination remains quarantined. The leased checker must
independently reconstruct the factor system and then apply every exact target gate.
No source patch, rerun, alternate central row, broader action, `p=2` object, or
generated-power substitution is authorized. Report the exact output and release
the slot.

## Hashes

- manifest: `35e8e898ef60bdb2ce2f4a7b466c554bbb823d67a54a41ecc29762ac2e406e97`
- checker: `f64ebe165da86d87333236b1752bbd409d1e43975db8739d969848422a01948f`
- imported module: `e9932eb57e0d219604f251bccd4f951e9851fe5e0c7226aa6cbd2b8dad218329`
