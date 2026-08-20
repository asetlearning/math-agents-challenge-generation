---
title: "P3-CENTER-ACTION-CROSSFIBRE outcome"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: false
active_minutes_new: 18
cumulative_active_minutes: 824
state: awaiting_lead
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

## Exact outcome

In a least `p=3` counterexample, `W=P'` is independently forced to be the unique
minimal normal subgroup, central of order 3, and the last nonzero augmentation
layer of `Z(P)`. For a root `x^3=a` and `f in Z(P)`, right conjugation
`s=alpha_x-1` gives the exact block identity

`(x f)^3=x^3+s^2 f`.

For the central extension `1 -> W -> G -> Q -> 1`, a normalized factor set `c`
and cube coordinate `theta(q)=c(q,q)+c(q^2,q)` give the exact cross-fibre equation

`theta(t)=theta(q)+theta(r)+c(q^3,r^3)`

for some product root `t`. Because `P` is the literal cube set and a subgroup,
every fibre satisfies `theta(R_v)=W`. The product equation is therefore
automatically solvable and does not constrain the skew part of `c`, hence does not
force `s^2 f` to vanish.

The log gives all section, root, value-section, and central-lift transformations
and an explicit `F_3^2` bilinear factor-set/root-torsor model with
`c(A,B)-c(B,A)!=0` and a center module satisfying `s^2 f=w!=0`. The model obeys
every identity derived in this lane. It is not a global group and is explicitly
not a counterexample.

## Scope boundary

This treats only the complete `p=3` subfamily. It does not answer the universal
odd-prime target. The seven canonical rows remain: universal odd-prime quantifier;
`p=3` odd and not 2; finite 3-group; exact exponent 9; `P` the literal cube-value
set; `P` a subgroup; desired conclusion `P` abelian. The exponent-eight 2-group
sibling and broader powerfulness clause are excluded.

## Recommendation

Stop `P3-CENTER-ACTION-CROSSFIBRE`. Any continuation must add a global relation
between simultaneous root actions, not another existential root choice or
factor-set/fibre observable. A concrete next gate is whether the relations
`alpha_x^3=Inn(x^3)` for roots above `a`, `b`, and `ab` can be imposed
simultaneously with quotient relations in `Aut(P)`; absent such a binding relation,
the full target fibre absorbs the surviving center-action square.

## What this does not establish

- It does not prove or refute the `p=3` source clause.
- It does not prove a global formal datum extends to a finite group.
- It does not address any odd prime other than 3.
- It does not address `p=2`, exponent 8, or the broader powerfulness question.
