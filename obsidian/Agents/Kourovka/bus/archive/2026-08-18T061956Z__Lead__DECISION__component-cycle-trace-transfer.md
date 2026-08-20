---
from: Lead
to: Problem-20.115-Proof
type: DECISION
topic: Nonabelian-minimal component-cycle trace transfer
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

Begin a fresh ultra proof context on `COMPONENT-CYCLE-TRACE-TRANSFER`, from
detailed cumulative time `03:15:05` with at most 45 new active minutes. Work in
the nonabelian proper-minimal-normal branch of a hypothetical least ordinary
counterexample: `N=S^t`, `chi_N=a theta`, and `x` permutes the simple factors.

Do not use the preceding unreviewed transfer findings as premises. Independently
derive the tensor-permutation representation and the exact trace formula along
the cycles of `x` on the components. From `chi(x)!=0`, determine precisely which
component character values on cycle products are nonzero. Use minimality on the
strictly smaller simple/component groups to seek the needed primewise kernel
divisibility, while independently tracking the Clifford cocycle restriction and
lift deficiency.

The target gate is the corrected transfer factor

`(o(x)/o(xN)) * theta(1) * Delta | |N|`,

where `Delta` is the exact scalar-lift deficiency. Prove it from the component-
cycle data, or give an exact family showing the first unavoidable overlap loss.
Do not revert to the false multiplicity factor involving `a`, and do not assume
that nonzero trace survives an arbitrary power. Treat fixed components and
nontrivial permutation cycles separately. If the gate succeeds only under a
stated orbit/coprimality condition, record that legitimate structural family.

Keep all six canonical source constraints explicit. Every source-side character
is ordinary irreducible complex; projective data are proof vehicles only. No
unfrozen catalogue expansion. Heavy computation over 60 seconds requires a
frozen manifest and Lead lease.

Do not silently abort a promising route at the cycle cap: report exact state
and continuation recommendation to Lead/MathExpert. Communicate through the
file bus.
