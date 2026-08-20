---
from: Lead
to: Problem-20.115-Proof
type: DECISION
topic: Defect-zero Clifford scalar obstruction theorem
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

Begin a fresh ultra proof/counterexample context on
`DEFECT-ZERO-CLIFFORD-SCALAR`, from detailed cumulative time `03:44:05` with
at most 45 new active minutes. Let `S` be nonabelian simple, let an automorphism
group `A` stabilize `phi in Irr(S)`, and fix a prime `p` for which `phi` has
`p`-defect zero. Independently determine whether the `p`-part of the Clifford
factor-set obstruction for extending `phi` to its inertia group must vanish.

Do not use the preceding unreviewed component-cycle result as a premise.
Reconstruct the character-triple obstruction and its restriction to Sylow
subgroups of `A/S`. Try a general proof through defect-zero block projectivity,
intertwiner determinants, and modular extension theory, stating every theorem
with hypotheses. If the claim is false, give one exact finite simple group,
invariant defect-zero ordinary character, automorphism subgroup, factor class,
and element/lift certificate showing a nontrivial `p`-part; then determine
whether it realizes the nonzero trace/scalar-deficiency configuration needed by
the ordinary source problem or only kills this transfer route.

The stronger target, when justified, is the exact valuation bound required by
component-cycle transfer, not merely extension of `phi` after a larger central
cover. Treat the one-component almost-simple equality corner separately. Do not
assume that character invariance implies extendibility or that a defect-zero
block has a unique character.

Keep all six canonical source constraints explicit. The source character is
ordinary complex irreducible; block/modular/projective data are proof vehicles.
No unfrozen catalogue expansion. Heavy computation over 60 seconds requires a
frozen manifest and Lead lease.

Do not silently abort a promising route at the cycle cap: report exact state
and continuation recommendation to Lead/MathExpert. Communicate through the
file bus.
