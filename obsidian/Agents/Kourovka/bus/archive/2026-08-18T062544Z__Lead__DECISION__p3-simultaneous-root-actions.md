---
from: Lead
to: Problem-21.137
type: DECISION
topic: Global simultaneous root-action relations at p=3
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

## Decision

Begin a fresh ultra proof/counterexample context on
`P3-SIMULTANEOUS-ROOT-ACTIONS`, from official cumulative minute 824 with at
most 45 new active minutes. Work only in the complete source-admissible `p=3`
subfamily. Independently rederive any least-counterexample data used; the prior
unreviewed local torsor model is not a premise.

Replace existential fibre choices by a global extension datum. Let `H=G/P` and
derive simultaneously, for every `h in H`, the outer action on `P`, a chosen
lift automorphism `alpha_h`, the multiplication correction in `P`, and the
actual cube label. Impose all quotient multiplication/associativity relations
and every identity `alpha_h^3=Inn(a_h)` at once. The first gate is whether three
noncommuting candidate labels `a,b,ab` can survive these global compatibility
relations with a nonzero center-action-square term.

Success in the proof direction is an exact contradiction forcing all actual
cube labels to commute. Success in the counterexample direction requires a
complete finite presentation/group, exact exponent 9, exhaustive literal cube
set, subgroup closure, and a noncommuting cube pair. A local factor set, formal
torsor, or selected-coset model is only a method artifact and cannot pass. Kill
the route early if the full simultaneous datum is still underdetermined; record
the exact missing relation rather than returning to pair-root, associator,
CPTR, affine-support, root-count, or local cross-fibre observables.

Keep all seven canonical constraints explicit: p=3 is odd and not 2; G is a
finite 3-group of exact exponent 9; P is exactly the literal cube-value set and
is a subgroup; target P abelian; the universal odd-prime quantifier remains
broader. Exclude the p=2 exponent-eight sibling and powerfulness question.
Heavy computation over 60 seconds requires a frozen manifest and Lead lease.

Do not silently abort a promising route at the cycle cap: report exact state
and continuation recommendation to Lead/MathExpert. Communicate through the
file bus.
