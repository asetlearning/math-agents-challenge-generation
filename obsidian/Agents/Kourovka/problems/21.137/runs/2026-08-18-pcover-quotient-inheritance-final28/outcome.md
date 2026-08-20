---
title: "PCOVER-QUOTIENT-INHERITANCE — pre-enumeration hard kill"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: PCOVER-QUOTIENT-INHERITANCE
direction: counterexample
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/p-group-generation
  - project/kourovka
  - status/draft
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/ideas/2026-08-18-post-r4-faithful-character-portfolio.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T105745Z-order6561-TRI3-layer.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T122251Z-min9-action-family-empty.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-18-pcover-quotient-inheritance-final28/manifest.json
---

# Outcome

`PCOVER-QUOTIENT-INHERITANCE` hard-kills at its pre-enumeration gate.  The exact
central-quotient predicate and a complete p-group-generation route can be
frozen, but the required ANUPQ/`pq` p-cover engine is absent.  Consequently no
numerical descendant-orbit bound can be obtained, no Lead lease is requested,
and no group computation is run.

This is `STRATEGY_EXHAUSTED` for this executable route only.  The active source
scope remains unanswered.

# Exact central-quotient parent predicate

Assume a hypothetical order-`3^9` minimum counterexample `H`.  Put

`P=Pow_3(H)={h^3:h in H}`

and use only the reviewed minimum-counterexample rows: `P` is a nonabelian
subgroup, `N=P'` is central of order three, and every nontrivial normal subgroup
of `H` contains `N`.

Let

`L_1(H)=H`,  `L_(i+1)(H)=L_i(H)^3[L_i(H),H]`

be the lower exponent-three central series, and let `L_c(H)` be its last
nontrivial term.  This term is central and elementary abelian.  Every order-three
subgroup of it is therefore a nontrivial normal subgroup of `H`, hence contains
`N`.  Such a subgroup has the same order as `N`, so it equals `N`.  An elementary
abelian group with a unique order-three subgroup has order three.  Therefore

`L_c(H)=N`.

Thus `Q=H/N` is exactly the lower-exponent-three parent of `H`, not an arbitrary
central quotient, and `|Q|=3^8`.  For the quotient map `pi:H->Q`, surjectivity
gives the exact set identity

`Pow_3(Q)=pi(Pow_3(H))=pi(P)=P/N`.

Here `N=P'<=P`.  Hence the literal cube set of `Q` is a subgroup and is abelian.
It is nontrivial: if `P/N=1`, then `P=N` is cyclic, contradicting
`N=P'!=1`.  Finally `exp(Q)` divides nine and cannot be three because then its
literal cube set would be trivial.  Therefore every possible parent satisfies
exactly the frozen predicate

1. `|Q|=3^8`;
2. `exp(Q)=9`;
3. the complete literal set `Pow_3(Q)` is a nontrivial abelian subgroup;
4. the 3-cover of `Q` has an allowable step-size-one descendant.

No converse is asserted: a parent passing these rows is not a witness.

# Complete parent-list route

The exact route is the standard p-group generation induction, frozen in the
manifest.

1. Start with every elementary abelian root `C3^d`, `1<=d<=8`.
2. At every retained isomorphism type `A`, compute its 3-cover, 3-multiplicator
   `M`, nucleus `U`, and automorphism orbits of all allowable subgroups `L<=M`
   with `LU=M`, allowing every step size compatible with the order-`3^8` cap.
   Emit `A*/L` and continue recursively.
3. It is safe to prune a branch when the ancestor exponent exceeds nine or its
   complete literal cube set is not a subgroup.  Both properties pass to every
   quotient of a qualifying parent.  Trivial cube image is not pruned.
4. At order `3^8`, retain precisely the four parent-predicate rows above.

Every finite 3-group has a unique lower-exponent-three parent and an iterated
parent chain ending at an elementary abelian root, so this is a completeness
route.  Allowing only step-size-one ancestors would not be complete and is
explicitly forbidden by the frozen method.

For each retained parent, the order-`3^9` descendants are the automorphism
orbits on allowable hyperplanes of `M` not containing `U`.  If
`m=dim_F3(M)` and `u=dim_F3(U)`, their raw number is at most

`(3^m-3^(m-u))/2`.

The exact global orbit count must be computed before materializing descendants
and must not exceed `10^5`.  The absent p-cover engine means that the required
`m,u` values and automorphism orbits are unavailable, so there is no honest
numerical bound.  This independently fires the missing-bound hard kill.

# Tool gate

Read-only probes found `/usr/bin/gap`, but no `pq`, `pga`, `anupq`, or `gap3`
executable and no ANUPQ package under the available system, user, or rooted GAP
package paths.  The installed Polycyclic package is not the p-cover/
p-group-generation engine required here.  Reimplementing that general-purpose
engine is forbidden.

No mathematical computation, enumeration, descendant construction, or group
test was run.  There is therefore no manifest eligible for a compute lease and
no candidate object.

# Target audit

The target remains the revision-2 odd-prime clause.  This lane used only `p=3`,
exact exponent nine, and the literal cube set.  It did not open any `p=2` or
exponent-eight material, R4 actions, or the reviewed MIN9 fixed outer-action
family.  It did not mistake a quotient, parent, action, or generated-power
subgroup for a witness.

`active_assignment_answered: no`.

# Active-time ledger

- Start: `2026-08-18T00:39:46Z`, official cumulative minute `737`.
- Stop: `2026-08-18T00:44:48Z`; charged active minutes: `5`.
- Official cumulative minute after charge: `742`.
- Unused portion of the 28-minute allocation returned to Lead: `23` minutes.
- Frozen manifest SHA-256:
  `a14300131145471807835fbf6c42b30736d2d4c3a0f048c3b8690049bb40479d`.

# What this does not establish

- It does not enumerate any order-`3^8` parent or order-`3^9` descendant.
- It does not give a numerical descendant count.
- It does not exclude a counterexample of any order.
- It does not construct a target-admissible group.
- It does not answer the unrestricted odd-prime statement.
