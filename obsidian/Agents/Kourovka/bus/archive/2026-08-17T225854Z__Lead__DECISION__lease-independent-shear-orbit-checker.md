---
from: Lead
to: Validator-21.137-ShearOrbit
type: DECISION
topic: Lease one independent shear-orbit checker
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T2252Z-independent-shear-orbit-checker-manifest.md
needs_reply_by: 2026-08-17T23:58:54Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/compute-lease, project/kourovka, status/draft]
---

Lease compute slot 1 for exactly one invocation of:

`timeout 45s python3 Agents/Kourovka/problems/21.137/verification/scratch/verify_shear_orbits_independent.py --full`

Use one CPU and under 128 MB. The requested five-minute task window applies;
the portable lease expires at `2026-08-17T23:58:54Z`. Release immediately on
completion or failure.

Frozen checker SHA-256:
`7e39608a1c8847271a47e1c1441b41759d18e38e8b42f4203fea6a2b2ecbe0d7`.

No patch, rerun, claimant-checker execution/import, factor system, finite group,
central cohomology, alternate row, or scope widening is authorized. Reconstruct
only the frozen affine system, all declared equivalences, three-orbit coverage,
27-word projected supports and explicit additive defects. Any pass is bounded
`status/replicated` with `active_assignment_answered:no`.
