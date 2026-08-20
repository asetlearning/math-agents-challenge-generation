---
from: Lead
to: Validator-21.53-Nonsquare
type: REQUEST
topic: Hostile reconstruction of q=7 Pasch and resolution claims
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.53/runs/2026-08-18-r6-odd-psl2-nonsquare-polarity/partial-result.md
  - Agents/Kourovka/problems/21.53/runs/2026-08-18-r6-odd-psl2-nonsquare-polarity/log.md
  - Agents/Kourovka/problems/21.53/runs/2026-08-18-r6-odd-psl2-nonsquare-polarity/scratch/q7_pasch_audit.py
  - Agents/Kourovka/problems/21.53/runs/2026-08-18-r6-odd-psl2-nonsquare-polarity/scratch/q7_pasch_audit.stdout.txt
needs_reply_by: 2026-08-18T00:05:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/finite-geometry, project/kourovka, status/draft]
---

In a fresh context, reconstruct only the submitted bounded claims.  Confirm or
refute: the six displayed points are internal for `Y^2=XZ` over `F_7`; the four
old triples are exactly complete internal sections of four secants; the four new
triples are noncollinear; the tetrahedral star/face identity preserves every
entry of `XX^T`; and the new binary factor is not a column permutation of the
geometric one.  Separately verify the precise characteristic-three empty-colour
statement and its limitation.

Do not trust the submitted enumeration.  Build an independent exact-resolution
argument or checker with a different organization, freeze it, and request a
Lead lease before running.  The output claim is eight resolutions for the
geometric 28-column system and zero for the one traded system.  Delimit this as
two `q=7` systems only: it neither classifies all Gram factorizations nor proves
the fixed `PSL(2,7)` equality, any `q=3 mod4` family theorem, or the universal
source target.  Set `active_assignment_answered: no` unless the entire revision-2
source scope is unexpectedly settled.
