---
title: "CPTR pair transgression — exact extra-term certificate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: CPTR-PAIR-TRANSGRESSION
direction: proof
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - project/kourovka
  - status/conjectured
---

# CPTR pair transgression — exact extra-term certificate

## Outcome

`STRATEGY_EXHAUSTED` for `CPTR-PAIR-TRANSGRESSION` only.
`active_assignment_answered: no`.

The verified mixed bar chain gives an exact section-independent scalar identity,
but that identity is the evaluation of a coboundary and has value zero. Ordered
`(C5)` exposes the hoped-for target pairing as a separate, uncontrolled deep
carry term. Its basepoint value has an exact noncanonical-section correction.
Thus this 3-chain cannot by itself yield `beta=0`.

## Exact cycle evaluation

For

`Q(a,b,c)=ell_c(r_(a,b))
 +(1/2)beta(r_(ab,c),L_cr_(a,b))
 -(1/2)beta(r_(a,bc),r_(b,c))`,

the complete scalar `(C4)` row is `Q=delta s`. Since the previously audited
shuffle `Z(h,j)` has `partial Z=0`,

`Omega(h,j)=<Q,Z>=<s,partial Z>=0`.                         `(E0)`

The run log records the full eight-term summand, with every action, `ell`, and
quadratic `1/2 beta` term. Under the complete arbitrary-section laws,

`Omega'-Omega=<delta(s'-s),Z>=0`.

So `(E0)` is exact and section-independent, but numerically coboundary-trivial.

## Ordered `(C5)` extra term

For commuting order-`p` `h,j`, put

`u_(j,h)^(-1)u_(h,j)=(q,z)`,

`q=r_(h,j)-r_(j,h)`.

The identity `x_h^(x_j)=x_h(q,z)`, expanded with the actual descending ordered
norm, gives

`D_jc_h=D_h^(p-1)q`,                                      `(E3)`

`ell_j(c_h)=ell_h(D_h^(p-2)q)
             +(1/2)beta(D_h^(p-2)q,q)`.                    `(E4)`

Before simplification the central coordinate contains `p z`, the full sum of
`ell_h(E_mq)`, the ordered double sum of
`(1/2)beta(L_h^mq,L_h^nq)`, and the cross term with `c_h`; the log records why
each becomes the displayed expression or zero.

Using the ordered action-power identity

`ell_t(D_t^(p-1)a)=beta(a,c_t)`

for both `h,j` gives the strongest pair formula

`beta(c_h,c_j)
 =ell_j(D_j^(p-2)D_h^(p-1)q)
 =ell_h(D_h^(p-2)D_j^(p-1)q)`.                              `(E6)`

No evaluated row cancels the displayed scalar.

## Exact section extra term

Let `N_t=D_t^(p-1)` and change the section by
`x'_t=x_t(eta_t,z_t)`. Then

`q'=q+D_jeta_h-D_heta_j`, `c'_t=c_t+N_teta_t`,

and `(E3)--(E4)` remain covariant. But

`beta(c'_h,c'_j)-beta(c_h,c_j)
 =beta(N_heta_h,c_j)+beta(c_h,N_jeta_j)
  +beta(N_heta_h,N_jeta_j)`.                                `(E8)`

With only `eta_h` changed, the first extra term is exactly

`-beta(eta_h,D_h^(p-2)N_jq)`.

The available equations do not place that second argument in `rad(beta)`.
Hence the invariant zero `(E0)` cannot be identified with the target-facing
basepoint pairing without a new correction or vanishing lemma.

## Separate reach audit

Actual-value coverage yields

`A=union_(t in H)(c_t+N_tA)`

and a surjection to `A/[A,H]`. It does not prove
`[A,H]<=rad(beta)`, so `beta` does not presently descend to that quotient. It
also does not ensure that two arbitrary covered values have commuting root
cosets. Most decisively, `(E6)` does not establish even the frozen pair's
basepoint commutativity.

There is therefore neither a commuting-pair lemma nor the separately required
coverage bridge to `beta=0`.

## Constraint-and-conclusion audit

| constraint_id | role | result in this run |
|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | arbitrary odd `p` retained; universal conclusion unresolved |
| `21.137-odd-p-not-2` | admissibility | pass in the conditional calculation; `1/2` and characteristic `p` used |
| `21.137-odd-finite-p-group` | admissibility | retained from the reviewed hypothetical minimum-counterexample reduction |
| `21.137-odd-exponent-p2` | admissibility | retained conditionally; supplies the reviewed exponent-`p` coordinate setup |
| `21.137-odd-power-set-definition` | admissibility | actual-value affine supports only; no generated-subgroup substitution |
| `21.137-odd-power-set-subgroup` | admissibility | used only for the exact affine union cover |
| `21.137-odd-P-abelian` | target conclusion | unresolved; `beta=0` is not obtained |

## Evidence boundary

The adjacent `log.md` contains the line-by-line boundary, section change,
`(C4)`, ordered `(C5)`, and reach calculations. No computation, web/history,
uncurated context, delegate, excluded clause, or stopped construction family was
used. No claim-check file is required because this is
`STRATEGY_EXHAUSTED`, not `CLAIM` or `STALE_MATCH`.
