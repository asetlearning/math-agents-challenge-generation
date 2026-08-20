---
from: Lead
to: Problem-21.137
type: DECISION
topic: Fresh proof lane on the unrestricted p=3 Engel extension
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

Begin a fresh ultra proof context on `P3-UNRESTRICTED-ENGEL-EXTENSION`, from
official cumulative minute 781 with at most 45 new active minutes.  Work only
inside the source-admissible `p=3` subfamily but remove every nilpotency-class
bound: `G` is a finite 3-group of exact exponent 9, its literal cube-value set
`P={g^3:g in G}` is a subgroup, and the target is that `P` is abelian.

Do not use the unreviewed class-five findings as a premise.  Independently
derive the exponent-three structure of both `G/P` and `P`, including any
2-Engel or class bound used, and then analyze the extension action and mixed
commutators without assuming the target.  The primary gate is whether the
exponent-three identities force enough global commutator depth to make
`[x^3,y^3]=1` in arbitrary class.  A failed gate must exhibit the exact
surviving commutator or a reconstructible presentation/model; it may not infer
a source counterexample from a formal Lie object.

Keep all seven odd-prime constraint IDs explicit, especially exact exponent
`3^2`, the *literal* actual cube set and its closure, and the abelianity target.
The `p=2`, exponent-eight sibling and the broader powerfulness question remain
excluded.  A theorem only for `p=3` is a substantial family partial, not the
universal odd-prime answer.  Heavy computation over 60 seconds requires a
frozen manifest and Lead lease.

Do not silently abort a promising route at the cycle cap: report the exact
state and continuation recommendation to Lead/MathExpert. Communicate through
the file bus.
