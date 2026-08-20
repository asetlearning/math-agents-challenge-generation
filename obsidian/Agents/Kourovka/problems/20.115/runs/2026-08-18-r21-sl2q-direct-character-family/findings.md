---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
cycle: 21
outcome: PARTIAL_RESULT
computed_in: "the abstract ordinary character table of SL(2,q), for every prime power q>=4"
active_assignment_answered: no
---

# Candidate family partial: every quasisimple `SL(2,q)` passes the source predicate

## Exact claim boundary

The derivation below gives the following candidate partial only:

> If `q>=4` is a prime power, `G=SL(2,q)`, `chi` is an ordinary irreducible
> complex character of `G`, and `x in G`, then
> `chi(x) != 0` implies `o(x) chi(1) | |G|`.

The quasisimple range is exactly `q>=4`: `PSL(2,q)` is nonabelian simple and
`SL(2,q)` is perfect there.  The groups for `q=2,3` are not quasisimple and are
not part of this family claim.  Nothing here answers the universal quantifier over
all finite groups.

## 1. Complete class inventory and exact orders

Put `p=char(F_q)` and

`U={b in F_(q^2)^*: b^(q+1)=1}`.

Thus `F_q^*` and `U` are cyclic of orders `q-1` and `q+1`.  Every element of
`SL(2,q)` is exactly one of the following types.

| type | representative/parameter | parameter identification | exact order |
|---|---|---|---|
| central | `z_e=eI` | `e in {+1,-1}` for odd `q`; only `e=1` for even `q` | `1` or `2` |
| unipotent | `u_(e,c)=e [[1,c],[0,1]]` | odd `q`: `e=+/-1` and `c` square/nonsquare; even `q`: one class | `p` if `e=1`; `2p` if `e=-1`; hence `2` for even `q` |
| split regular | `s_a=diag(a,a^-1)` | `a in F_q^*\{+/-1}`, modulo `a~a^-1` | `ord(a)`, hence divides `q-1` |
| nonsplit regular | eigenvalues `b,b^-1` | `b in U\{+/-1}`, modulo `b~b^-1` | `ord(b)`, hence divides `q+1` |

The order statements are orders in `SL(2,q)`, not projective orders.  If a torus
element has exact order `n`, its projective image has order `n` for odd `n` and
`n/2` for even `n`, because the unique involution in either cyclic torus is
`-I`; the lift nevertheless retains the full eigenvalue order `n`.  Also, for
odd `p`, if `v=I+N` with `N^2=0`, then `v^p=I`, while `(-v)^p=-I`; therefore the
two lifts of the same projective unipotent class have exact orders `p` and
`2p`.

For odd `q` the inventory has two central classes, four unipotent classes,
`(q-3)/2` split classes and `(q-1)/2` nonsplit classes, hence `q+4` classes.
For even `q` it has one central class, one unipotent class, `(q-2)/2` split
classes and `q/2` nonsplit classes, hence `q+1` classes.  The respective class
sizes are `1`; `(q^2-1)/2` (odd) or `q^2-1` (even) for each unipotent class;
`q(q+1)` for split regular classes; and `q(q-1)` for nonsplit regular classes.

## 2. Complete ordinary irreducible-character inventory

Let `theta` run over linear characters of `F_q^*`, and `phi` over linear
characters of `U`.  Parameters are identified with their inverses.  The complete
families are:

| family | parameter/count for even `q` | parameter/count for odd `q` | degree |
|---|---:|---:|---:|
| `1_G` | one | one | `1` |
| `St` | one | one | `q` |
| `X_theta` (principal series) | `theta!=1`: `(q-2)/2` | `theta^2!=1`: `(q-3)/2` | `q+1` |
| `Y_phi` (cuspidal series) | `phi!=1`: `q/2` | `phi^2!=1`: `(q-1)/2` | `q-1` |
| `X_alpha^+,X_alpha^-` | absent | two, `alpha` the quadratic character of `F_q^*` | `(q+1)/2` |
| `Y_beta^+,Y_beta^-` | absent | two, `beta` the quadratic character of `U` | `(q-1)/2` |

Here `Ind_B^G(theta)` is irreducible of degree `q+1` when
`theta!=theta^-1`; the rank-one Mackey double-coset calculation gives its
self-inner-product as one.  At `theta=1` it is `1_G+St`, and at the quadratic
`alpha` it has self-inner-product two and splits as `X_alpha^++X_alpha^-`.
The analogous nonsplit-torus construction gives `Y_phi`; the quadratic member
splits as `Y_beta^++Y_beta^-`.  The nonsquare-determinant diagonal automorphism
fixes every regular semisimple class and interchanges the two unipotent classes
of a fixed trace, so the two constituents of either exceptional pair agree on
all semisimple classes and can differ only on the unipotent pair.

These rows are exhaustive.  Besides matching the class counts above, their
degree-square sums are

`1+q^2+((q-2)/2)(q+1)^2+(q/2)(q-1)^2=q(q^2-1)`

for even `q`, and

`1+q^2+((q-3)/2)(q+1)^2+((q-1)/2)(q-1)^2`
`+2((q+1)/2)^2+2((q-1)/2)^2=q(q^2-1)`

for odd `q`.

## 3. Exact values and all cancellation gates

For odd `q`, let `alpha` also denote the quadratic character on `F_q^*`, choose
the quadratic Gauss sum `tau` with

`tau^2=alpha(-1)q=(-1)^((q-1)/2)q`,

and use `delta=+1,-1` to label the exceptional constituents.  Up to swapping
the two labels, the full table formulas are:

| row | `z_e` | `u_(e,c)` | `s_a` | `t_b` |
|---|---|---|---|---|
| `1_G` | `1` | `1` | `1` | `1` |
| `St` | `q` | `0` | `1` | `-1` |
| `X_theta` | `(q+1)theta(e)` | `theta(e)` | `theta(a)+theta(a)^-1` | `0` |
| `Y_phi` | `(q-1)phi(e)` | `-phi(e)` | `0` | `-(phi(b)+phi(b)^-1)` |
| `X_alpha^delta` | `((q+1)/2)alpha(e)` | `(alpha(e)/2)(1+delta alpha(c)tau)` | `alpha(a)` | `0` |
| `Y_beta^delta` | `((q-1)/2)beta(e)` | `(beta(e)/2)(-1+delta alpha(c)tau)` | `0` | `-beta(b)` |

For even `q`, omit the last two rows and the `e,c` choices; the first four
formulas remain valid with `e=1`.

This displays every possible cyclotomic cancellation:

- `X_theta(s_a)=0` exactly when `theta(a)^2=-1`.
- `Y_phi(t_b)=0` exactly when `phi(b)^2=-1`.
- The exceptional unipotent values cannot vanish for `q>=5`: vanishing would
  force `tau=+/-1`, hence `q=1`.
- All other displayed allowed values are visibly nonzero.  For even `q`, the
  two torus orders are odd, so even the order-four cancellation condition cannot
  occur.

Thus cancellation only deletes cells from the support described below; it never
creates support on the opposite torus.

## 4. Central kernel and lift audit

For odd `q`, the scalar by which `-I` acts is:

| row | central scalar | kernel conclusion for a nontrivial row |
|---|---|---|
| `St` | `+1` | factors through `PSL(2,q)` |
| `X_theta` | `theta(-1)` | factors iff `theta(-1)=1`; otherwise faithful |
| `Y_phi` | `phi(-1)` | factors iff `phi(-1)=1`; otherwise faithful |
| `X_alpha^delta` | `alpha(-1)=(-1)^((q-1)/2)` | factors for `q=1 mod 4`, faithful for `q=3 mod 4` |
| `Y_beta^delta` | `beta(-1)=(-1)^((q+1)/2)` | factors for `q=3 mod 4`, faithful for `q=1 mod 4` |

Since a nontrivial normal subgroup of the quasisimple group either lies in the
center or maps onto the simple quotient, these are the complete faithful versus
central-kernel alternatives.  Multiplication by `-I` changes the value only by
the displayed scalar, hence preserves nonvanishing; its exact effect on order is
already included by `a -> -a`, `b -> -b`, and `p -> 2p` in the class audit.

## 5. Six-row support/divisibility matrix

Write `Q_chi=|G|/chi(1)` and recall `|G|=q(q-1)(q+1)`.  Each entry uses exact
orders in `SL(2,q)`.

| irreducible row family | possible nonzero class types | exact possible order source | `Q_chi` | result |
|---|---|---|---:|---|
| `1_G` | all | any element order | `q(q-1)(q+1)` | divides by Lagrange |
| `St` | central, split, nonsplit | `1,2`, divisor of `q-1`, or divisor of `q+1` | `(q-1)(q+1)` | divides |
| `X_theta` | central, unipotent, split | `1,2,p,2p`, or divisor of `q-1` | `q(q-1)` | divides (`p|q`; for odd `q`, `2|q-1`) |
| `Y_phi` | central, unipotent, nonsplit | `1,2,p,2p`, or divisor of `q+1` | `q(q+1)` | divides (`p|q`; for odd `q`, `2|q+1`) |
| `X_alpha^delta` | central, unipotent, split | same support orders as `X_theta` | `2q(q-1)` | divides |
| `Y_beta^delta` | central, unipotent, nonsplit | same support orders as `Y_phi` | `2q(q+1)` | divides |

The displayed ordinary-table derivation therefore gives the candidate
implication at every table cell.

## 6. Small-parameter audit

The generic inventory already includes the endpoints, but they can be checked
without any parameter convention.

- `q=4`: `SL(2,4)=A5`, of order `60`.  Class orders are `1,2,3,5`; degrees are
  `1,4,5,3,3`.  The quotients and supports are respectively: `60` on all;
  `15` on orders `1,3,5`; `12` on orders `1,2,3`; and `20` on orders `1,2,5`
  for each degree-three row.  Every listed order divides its quotient.
- `q=5`: `SL(2,5)=2.A5`, of order `120`.  Central orders are `1,2`, positive
  and negative unipotent orders are `5,10`, split regular order is `4`, and
  nonsplit regular orders are `3,6`.  Degrees are
  `1,5,6,4,4,3,3,2,2`.  Quotients by row family are `120,24,20,30,40,60`;
  the support matrix above gives divisibility for each exact order.  The two
  exceptional pairs have unipotent values `(1+/-sqrt(5))/2` and
  `(-1+/-sqrt(5))/2`, so none of the endpoint cells was lost through an
  unexamined cancellation.
- The exceptional isomorphism `SL(2,9)=2.A6` causes no extra row or class:
  the odd-`q` count gives thirteen rows, the Gauss sum has `tau^2=9`, and its
  exceptional unipotent values are `2,-1` and `1,-2`, all nonzero.  Similarly
  `q=7` has `tau^2=-7`, so its two exceptional pairs are nonzero complex-
  conjugate values.  Thus the only threshold degeneracies are the already
  separated `q=4,5` endpoints.

## 7. Constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / use | evidence | result |
|---|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | every admissible triple | restricted candidate partial: every triple with `G=SL(2,q)`, `q>=4` | complete class and row parametrizations in §§1–3 | pass for the stated family; universal scope not answered |
| `20.115-G-finite` | admissibility | `G` finite | `SL(2,q)` has order `q(q-1)(q+1)` | determinant-one matrices over finite `F_q` | pass |
| `20.115-chi-complex-irreducible` | admissibility | ordinary irreducible complex `chi` | the six row families in §2 | rank-one constructions, class count, and degree-square sum | pass for the family |
| `20.115-x-in-G` | admissibility | `x in G`, exact `o(x)` | all central, unipotent, split and nonsplit classes | Jordan classification and exact calculations in §1 | pass for the family |
| `20.115-character-value-nonzero` | admissibility | exact `chi(x)!=0` | exact supports and cancellation gates in §3 | roots of unity and quadratic Gauss-sum formulas | pass for every retained cell |
| `20.115-order-degree-divisibility` | target conclusion | `o(x)chi(1)| |G|` | equivalent `o(x)|Q_chi` | six-row matrix in §5 | pass for the family |

## Limitations

This is a hand derivation of an infinite quasisimple family, not a finite sample
and not a character-table-library computation.  It does not use any prior
rank-one-family result.  It remains `status/conjectured` pending an independent
reconstruction of the ordinary-table formulas, especially the two exceptional
Gauss-sum rows and the exact negative-unipotent lift order.
