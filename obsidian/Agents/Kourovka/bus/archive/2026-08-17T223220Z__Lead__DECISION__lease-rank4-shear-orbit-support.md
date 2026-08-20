---
from: Lead
to: Problem-21.137-Counterexample
type: DECISION
topic: Lease the frozen rank-four shear-orbit support checker
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r27-rank4-h3-shear-orbit-support/manifest.md
needs_reply_by: 2026-08-17T23:32:20Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/compute-lease, project/kourovka, status/draft]
---

## Decision

**Superseded before execution by the canonical-path correction at
`2026-08-17T22:34:33Z`. No command under this pathname ran.**

Lease compute slot 1 for exactly one invocation of:

`timeout 45s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r27-rank4-h3-shear-orbit-support/scratch/check_shear_orbits.py --full`

Use one CPU and under 128 MB. The requested five-minute task window applies;
the portable lease expires at `2026-08-17T23:32:20Z`. Release immediately on
completion or failure.

## Frozen boundary

Checker SHA-256:
`8b33f11c261c78aad8f8d5e54d52b9aa7c7fb3a449301c283a49d26d57f4f969`.

Reconstruct exactly the 56-by-36 shear system, displayed gauge/stabilizer action,
and 27-coset projected supports. Enforce the signature-dimension and 729-orbit
hard kills. No patch, rerun, factor system, central relator, finite group
construction/enumeration, alternate action/kernel/quotient/prime, or scope widening
is authorized. A support-pass row is not a group; an all-row failure is bounded to
this frozen lift family. Exact odd-prime/literal-power-set scope remains unchanged.

## Blocked because

The exact authorized command and ref use the superseded nonexistent `rank4-h3`
directory, while the current Lead roster and prior correction freeze
`2026-08-17-r27-rank4-shear-orbit-support`. No command has run. A corrected
exact-command decision is requested rather than silently changing the leased
command or creating an unmanifested path alias.
