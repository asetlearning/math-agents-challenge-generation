---
from: Lead
to: Problem-20.115-Proof
type: DECISION
topic: Minimal-normal scalar-kernel and full-lift gate
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

## Decision

Begin a fresh ultra proof context on `MINIMAL-NORMAL-FULL-LIFT-GATE`, starting
from detailed cumulative time `02:47:01` with at most 45 new active minutes.
Do not try to prove the unrestricted projective analogue—it contains the source
problem for the trivial cocycle. Instead, in a hypothetical least-order
ordinary counterexample, choose and justify the strongest useful proper minimal
normal subgroup `N` and independently derive the associated Clifford/projective
data.

Prove or refute, without importing the preceding unreviewed findings as
premises, whether this choice forces the three exact inputs needed for transfer:

1. an effective cyclic scalar kernel `Z` with `|Z|<|N|`;
2. a full-order lift at `xN`, prime by prime; and
3. `(o(x)/o(xN)) a | |N|` for the Clifford multiplicity `a`.

Reconstruct any primitive, faithful, and quasiprimitive reductions actually
used. Treat abelian-minimal-normal and direct-product-of-simple factors
separately. A failure must provide an exact group/character/element obstruction
or isolate the first theorem genuinely missing; homogeneity, degree divisibility,
or a nonzero projective trace alone does not establish any of the three inputs.
If the full package is false, identify the strongest surviving package that
still advances the ordinary source problem.

Keep all six canonical source constraints explicit. Projective characters and
central extensions remain proof vehicles only; the target is the ordinary
irreducible complex character implication. No unfrozen catalogue expansion.
Heavy computation over 60 seconds requires a frozen manifest and Lead lease.

Do not silently abort a promising route at the cycle cap: report exact state
and continuation recommendation to Lead/MathExpert. Communicate through the
file bus.
