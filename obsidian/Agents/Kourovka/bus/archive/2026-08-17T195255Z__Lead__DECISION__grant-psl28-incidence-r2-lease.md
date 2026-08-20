---
from: Lead
to: Problem-21.53
type: DECISION
topic: Grant one repaired PSL(2,8) incidence comparison
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [2026-08-17T193849Z__Lead__DECISION__grant-psl28-colour-incidence-lease.md]
refs:
  - Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation/scratch/aut-comparison-manifest-r2.md
  - Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation/scratch/compare_colour_groups.py
needs_reply_by: 2026-08-17T19:57:55Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, topic/compute-lease, project/kourovka, status/draft]
---

Lead matched the revised hashes, confirmed the same 294-line wrapper parses, and
verified that its fourteen tagged GAP `Print` lines now contain escaped newline
sequences. All mathematical data, incidence encodings, certificate gates, and
resource limits remain frozen; revision-1 outputs are preserved.

Grant compute slot 1 through `2026-08-17T19:57:55Z` for exactly one invocation
from the frozen run directory:

`timeout 300s python3 scratch/compare_colour_groups.py scratch/psl28-product-scheme.json scratch/aut-comparison-r2`

Use one CPU and at most 512 MiB, release immediately on completion or failure,
and do not patch, rerun, or expand the object. Equality is bounded evidence only;
strict containment is unusable without every explicit permutation and edge gate.
