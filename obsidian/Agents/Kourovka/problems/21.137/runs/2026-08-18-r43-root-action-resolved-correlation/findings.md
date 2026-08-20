---
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
cycle: 31
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/conjectured
---

# ROOT-ACTION-RESOLVED-CORRELATION outcome

## Active target

For every odd prime `p` and finite same-`p` group `G` of exponent exactly
`p^2`, if the literal set `P={g^p:g in G}` is itself a subgroup, prove that
`P` is abelian. The general powerfulness clause and the separate `p=2`,
exponent-eight clause are excluded.

## Outcome

`STRATEGY_EXHAUSTED` for the actual-root action-summed correlation. The exact
action-resolved identities are strictly finer than the aggregate pair kernel,
but on the surviving skew central character they are only `p`-th roots of the
three already-known value-conjugation translations. They transport an arbitrary
amplitude around action-dependent quotient orbits; after summing the complete
multiset of actual actions there is no common quotient action to factor out.
The unrestricted target and the complete `p=3` subfamily remain open.

## Exact action-summed identities

For `theta_x=(u |-> u^x)` and complete counts over all root pairs, set

`F^X_(a,alpha)(b,c)=#{(x,y):x^p=a,theta_x=alpha,y^p=b,(xy)^p=c}`.

The bijection `(x,y)->(x,y^x)` gives

`F^X_(a,alpha)(b,c)=F^X_(a,alpha)(b^alpha,c^alpha)`.       `(AX)`

The symmetric complete counts resolved by `theta_y=beta` and
`theta_(xy)=gamma` obey

`F^Y_(b,beta)(a,c)=F^Y_(b,beta)(a^beta,c^beta)`,          `(AY)`

`F^W_(c,gamma)(a,b)=F^W_(c,gamma)(a^gamma,b^gamma)`.      `(AW)`

No root or section is selected. Summing all actual `x`-actions gives the exact
choice-independent row

`K(a,b,c)=sum_alpha F^X_(a,alpha)(b^alpha,c^alpha)`,

and analogues for `Y` and `xy`. This is finer than an identity in `K`, but its
right side cannot be rewritten at one common value triple because `alpha`
varies through the actual root multiset.

## Why the skew line survives

In a least counterexample, independently quotienting by an order-`p` subgroup
of `P' cap Z(G)` gives `P'=Z=C_p<=Z(G)`. Put
`[u,v]=z^beta(ubar,vbar)` and for value cosets `A,B,C` write

`(delta,epsilon,zeta)=(beta(A,B),beta(B,C),beta(C,A))`.

For the quotient action of an `x`-root, `(AX)^p` is conjugation by `a=x^p`.
The three action-resolved transports therefore have central monodromies

`t_X=(0,-delta,zeta)`,
`t_Y=(delta,0,-epsilon)`,
`t_W=(-zeta,epsilon,0)`.

The surviving skew frequency `w=(epsilon,zeta,delta)` is orthogonal to all
three. If `delta!=0`, the `x`-action cannot fix `B` modulo `Z`: otherwise it
would shift `b` only by a central element of order `p`, so its `p`-th power
would fix `b`, contradicting `b^a!=b`. Thus the finer identity genuinely moves
the amplitude through a length-`p` quotient orbit, but its monodromy phase is
one. The same holds for the `y` and `xy` actions.

Action support does not restore the missing central coordinate:
`alpha^p=theta_a`, `beta^p=theta_b`, and `(beta o alpha)^p=theta_c` are unchanged
when `a,b,c` are independently multiplied by `z`. Consequently the full action
labels see the quotient transport but remain blind to precisely the central
Fourier line detecting `[a,b]`.

## Exact `p=3` local support certificate

On the actual value group `P=H_3(3) x C_3^2`, an explicit pair of automorphisms
`alpha,beta` fixes noncommuting values `a,b`; their product fixes `c`; their
cubes are conjugation by `a,b,c`; and
`(delta,epsilon,zeta)=(1,2,2)`. All three quotient transports are nontrivial
three-cycles and all three skew monodromies are zero. The exact checker is

`Agents/Kourovka/problems/21.137/runs/2026-08-18-r43-root-action-resolved-correlation/scratch/check_local_action_triple.py`

with SHA-256
`50e501552d7d5114096ffbe923ab7a1e0855d0666420237faf81cedd87f5b430`.

Observed output:

```text
formal_object=local_actions_on_H3(3)xC3^2_not_an_ambient_group
alpha_beta_product_cube_labels=A,B,C
pairings_delta_epsilon_zeta=1,2,2
root_values_fixed_by_respective_actions=pass
linear_parts_and_product_have_order_three=pass
cube_actions_equal_inner_A_inner_B_inner_C=pass
three_action_monodromy_pairings=0,0,0
nontrivial_quotient_orbits_for_X_Y_XY=pass
```

This is **not an ambient exponent-nine group, not a literal cube map, and not a
counterexample**. It proves only that the action/fixed-value/product-action gates
do not themselves eliminate the nonorthogonal skew configuration.

## Boundary and next representation

The named representation has now lost the Hall information exactly at the
required action sum. Continuing would only manipulate the same transport
operators. The only natural next question is a materially different global
extension-realizability obstruction: can the displayed locally compatible
action triple coexist with one multiplication law and all literal root fibres?
That reopens simultaneous extension/factor coherence, which this lane explicitly
excluded and which requires a Lead/MathExpert decision rather than an unapproved
continuation.

All seven canonical rows were retained. No universal conclusion row was proved,
and no finite group violating it was constructed: `active_assignment_answered:
no`.
