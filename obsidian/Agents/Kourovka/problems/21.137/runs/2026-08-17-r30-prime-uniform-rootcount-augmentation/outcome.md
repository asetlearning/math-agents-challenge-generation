---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-algebras
  - project/kourovka
  - status/conjectured
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: PRIME-UNIFORM-ROOTCOUNT-AUGMENTATION
outcome: STRATEGY_EXHAUSTED
active_minutes_used: 4
official_cumulative_minutes_start: 699
official_cumulative_minutes_end: 703
active_assignment_answered: no
---

# Outcome: STRATEGY_EXHAUSTED

## Active target

Odd prime `p>2`; finite same-`p` group `G`; exponent exactly `p^2`; literal
actual set `P={g^p:g in G}` is itself a subgroup; decide whether `P` must be
abelian.  The `p=2`, exponent-eight sibling is excluded.

## Exact method-failure certificate

Put `X_a={x:x^p=a}` and `r(a)=|X_a|`.  If `a!=1`, right multiplication by
`a` is a free order-`p` permutation of `X_a`, because `a=x^p`,
`(xa^j)^p=a`, and `a` has order `p`.  Hence `p` divides every `r(a)` for
`a!=1`.  Since `sum_a r(a)=|G|` is also divisible by `p`, `p` divides
`r(1)` as well.  Therefore

`R=sum_(x in G)x^p=sum_(a in P)r(a)a=0 in F_pG`.

Consequently `R` has zero image in every augmentation/Jennings layer, including
the first layer where a nonzero symbol from `[P,P]` could occur.  The support
hypothesis is lost coefficientwise before filtration.

The only apparent salvage is to divide the integral coefficients by `p` and
reduce `Rhat=sum_a (r(a)/p)a` modulo `p`.  This is not an operation on `R in
F_pG`.  Its coefficients are uncontrolled normalized root counts.  Moreover,
for `b in P`, conjugation invariance makes those coefficients constant on each
`<b>`-orbit `a_0,...,a_(p-1)`, and the corresponding first-noncentral
commutator sum cancels exactly:

`sum_i (a_i b-b a_i)=b sum_i(a_(i+1)-a_i)=0`.

Thus the cyclic orbit identity removes rather than isolates every target term.
This is an exact prime-uniform obstruction to the named observable, not a proof
of the source target.

Full derivation: [log](log.md).

## What is ruled out

Any proof that factors through the element `R` in `F_pG`, its conjugation
centrality, or any linear projection of it to an augmentation/Jennings quotient.
Dividing root counts by `p` merely reintroduces the uncontrolled fibre weights
that this reset was required to escape.

## What is not ruled out

The exact odd-prime statement remains open.  The calculation says nothing about
whether a hypothetical group with nonabelian literal power subgroup exists.
It also does not rule out a nonlinear statistic retaining relations among
individual roots rather than collecting them into `R`.

## Recommended next action

Return the unused allocation to Lead for a representation-changing strategy,
preferably the counterexample direction or a nonlinear root-relation observable
that does not factor through normalized multiplicities.  Do not continue by
passing to `R/p`: that is precisely the uncontrolled-weight hard kill.  No new
strategy was started.

`active_assignment_answered: no`
