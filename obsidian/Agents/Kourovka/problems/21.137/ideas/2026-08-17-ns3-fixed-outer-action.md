---
title: "MathExpert route — 21.137 — NS3-FIXED-OUTER-ACTION"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: NS3-FIXED-OUTER-ACTION
direction: counterexample
active_assignment_answered: no
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - project/kourovka
  - status/conjectured
---

# One selected experiment: `NS3-FIXED-OUTER-ACTION`

## Decision and scope lock

Select the **counterexample direction** for one 60-active-minute increment.  The
scope is exactly `21.137/odd-prime-exponent-p2`, revision `2`: `p>2`, finite
same-`p` group, exponent exactly `p^2`, the actual `p`th-power value set itself a
subgroup, and the question whether that set is abelian.

This experiment fixes `p=3`.  It does not use the general powerfulness clause,
`p=2`, exponent `8`, wreath-shaped or quarantined material, a catalogue, any
enlargement of the `UT_7(F_3)` template, or another pointwise affine-cover count.

All new assertions below are **general mathematical knowledge, unverified**, or
explicit proposals to be checked.  The fixed actions themselves come from the
authorized current-run record cited at the end.  No web or solution-bearing
history was used.

## Why this ranks above abstract `C4` alone

The reviewed `C4` equation says that a particular scalar 3-cochain is a
coboundary.  The current record supplies no canonical 3-cycle on which closure
and `beta != 0` force a nonzero evaluation, so an unrestricted transgression
attempt risks merely renaming the exhausted compatibility bottleneck.

The present route freezes that bottleneck at the least reviewed `p=3` tuple and
asks a finite, genuinely nonsplit abstract-kernel question.  It uses the full
factor equations, including `C4`, and then tests the actual cube set of every
surviving model.

## Frozen kernel, quotient, and four actions

Use BCH coordinates for the class-two exponent-three group

`Q = H_3(3) x C_3^2`

on the ordered basis `(a,b,u,v,z)`, with only nonzero bracket `[a,b]=z` and
`Z(Q)=<u,v,z>`.  Thus `|Q|=3^5` and `Q'=<z>`.

Define `A=I+N_A` and `B=I+N_B` by

`N_A(b)=-u, N_A(u)=v, N_A(v)=z`,

`N_B(a)= u, N_B(u)=v, N_B(v)=z`,

and let both maps kill every basis vector not displayed.  Put

`C=[A,B]` and `T=I`,

using the same commutator convention throughout.  The authorized calculation
records `A^3=Inn(a)`, `B^3=Inn(b)`, `C^3=I`, while `[C,A]` and `[C,B]` are inner.
The first gate must rederive these identities and check that the outer classes
of `A,B,C,T` give the quotient

`H=<x,y,c,t | x^3=y^3=c^3=t^3=1, [y,x]=c, c and t central>
   ~= H_3(3) x C_3`,

of order `3^4`.  The frozen outer action is

`rho(x)=[A], rho(y)=[B], rho(c)=[C], rho(t)=1`.

Let `q_X,q_Y` be the unique BCH representatives with zero `(u,v,z)`
coordinates whose inner automorphisms are `[C,A]` and `[C,B]`, respectively.
This convention fixes their signs mechanically; no `up to sign` representative
is allowed in the computation.

## The exact `3^10` factor family

Use lifts `X,Y,K,T0` of `x,y,c,t`.  Freeze every noncentral correction as above
and allow only the following ten independent `N=<z>` coordinates:

`X^3       = a z^e_X`,

`Y^3       = b z^e_Y`,

`K^3       = z^e_K`,

`T0^3      = z^e_T`,

`[Y,X]     = K z^e_YX`,

`[K,X]     = q_X z^e_KX`,

`[K,Y]     = q_Y z^e_KY`,

`[T0,X]    = z^e_TX`,

`[T0,Y]    = z^e_TY`,

`[T0,K]    = z^e_TK`,

where

`e=(e_X,e_Y,e_K,e_T,e_YX,e_KX,e_KY,e_TX,e_TY,e_TK) in F_3^10`.

This is the complete frozen search family: exactly `3^10=59,049` labelled
factor rows.  Corrections in `<u,v>` are deliberately fixed to zero; a failure
therefore exhausts only this named family, not all extensions inducing `rho`.

## Exact consistency equations

Write every `h in H` uniquely as `x^i y^j c^k t^l`, `0<=i,j,k,l<3`, and use
the section

`s_e(h)=X^i Y^j K^k T0^l`.

Collect the ten displayed relations to obtain, for all `h,j in H`,

`alpha_h in Aut(Q)` and `u_e(h,j) in Q` from

`s_e(h)s_e(j)=s_e(hj)u_e(h,j)`.

A row is admitted exactly when the following finite identities hold with the
reviewed right-action convention:

`alpha_j alpha_h = Inn(u_e(h,j)) alpha_(hj)` for all `81^2` pairs, and

`u_e(hj,k) alpha_k(u_e(h,j)) = u_e(h,jk)u_e(j,k)`

for all `81^3` triples.  In class-two coordinates these are precisely the full
`(C1)--(C4)` equations; no projected `(C3)`-only pass is sufficient.  Also check
the `p=3` specialization of `(C5)` for all `81` elements and the ten displayed
power/commutator relators.

Because the ten variables occur only as central powers of `z`, every coordinate
condition is affine-linear in `e`.  Build the single exact system `M e=b` over
`F_3` from the zero row and ten unit rows, and defensively confirm affine
linearity on every pair of unit rows before relying on it.  A row-reduced
inconsistency `0=1`, or the complete affine solution description, is the
confluence/associativity certificate.  This is a problem-specific finite factor
system, not a general cohomology solver.

For every solution `e`, multiplication on the explicit set `Q x H` defined by
`alpha,u_e` is associative by the displayed equations and has exactly
`3^5*3^4=3^9=19,683` elements.  Preserve the normal-form collector and all
critical-equation hashes.

## Target-facing observable

For each consistent row, compute exactly

`Pow_3(G_e)={g^3:g in G_e}`

either by all `19,683` normal forms or, equivalently, as the union of the exact
`81` coset supports, each evaluated on all `243` kernel elements.  Do not replace
this set by the subgroup it generates.

Record the deterministic tuple

`(|Pow_3(G_e)|, subgroup?, abelian?, first closure defect, first noncommuting pair)`.

Every cube lies in `Q` because `H` has exponent three.  Every consistent model
has exponent dividing nine because `Q` has exponent three; it has exponent
exactly nine because `X^3=a z^e_X` is nontrivial and noncentral.  These two
claims must still be checked in the saved normal form.

## Exact success certificate

Stop on the first row for which the enumerated actual cube set is a subgroup and
is nonabelian.  The preferred sharp pass is `Pow_3(G_e)=Q`, in which case
`[a,b]=z!=1` supplies the nonabelian pair.  A smaller nonabelian actual-value
subgroup is also a target candidate and must not be discarded.

Preserve: the ten-coordinate row; the affine consistency certificate; the
confluent `Q x H` multiplication/normal form of order `3^9`; exact exponent
`9`; the complete 19,683-element cube manifest or exact 81-support equivalent;
actual-set subgroup closure; two noncommuting actual cubes with roots; and all
seven canonical constraint rows.  This would be a candidate `CLAIM`, never a
certification.

## Exact failure certificate

Failure means one of only two complete outcomes:

1. `M e=b` is inconsistent, with a row-reduction certificate, so none of the
   `59,049` frozen factor rows defines the required extension; or
2. every consistent row is processed and has either a saved direct product of
   two actual cubes outside the actual set, or an exact actual-set subgroup
   together with a commuting generating set.

That exhausts only `NS3-FIXED-OUTER-ACTION/F_3^10`.  If the clock stops before
one of these certificates is complete, report the exact unprocessed affine rows
and do **not** call the family exhausted.

## One-hour allocation, compute gate, and hard kill

- minutes `0--8`: rederive `A,B,C,T`, the inner defects, `|H|=81`, and all signs;
- minutes `8--22`: collect the zero/unit factor tables, build and row-reduce
  `M e=b`, and determine the exact consistent-row count;
- minutes `22--40`: enumerate the exact 81-support cube unions for every
  consistent row, using symbolic batching if the affine family is large;
- minutes `40--48`: replay the first candidate or finish the complete
  all-failure certificates;
- minutes `48--60`: no research or search; package the outcome and stop.

Any categorical row or element enumeration requires a Lead-issued heavy-compute
lease.  The proposed bounded command is

`timeout 600s python3 Agents/Kourovka/problems/21.137/scratch/ns3_fixed_outer_action.py`

with estimated RAM below `1 GB`.  Search hard-kills at active minute `48`, even
if the affine family is incomplete.  Do not add `<u,v>` corrections, change the
outer action, inspect a catalogue, add quotient generators, or continue into a
second extension family.

## Likely failure and truth estimate

The likeliest failure is that the fixed abstract kernel is obstructed by `C4`,
or that every realizable central correction retains the same actual-cube closure
defect seen in earlier constructions.  The `N`-only factor restriction may also
be too narrow.  Those are honest family failures, not evidence for the universal
assertion.

Scheduling judgement only: lower the probability that the universal assertion
is true from `0.55` to `0.52`.  The reviewed affirmative bounded families remain
weak evidence for truth, while the explicit individually consistent root actions
make one sharp nonsplit counterexample experiment worth the hour.  No
mathematical claim is attached to this estimate.

## Authorized refs only

- `Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json`
- `Agents/Kourovka/problems/21.137/runs/2026-08-16-r2-odd-counterexample/log.md`
- `Agents/Kourovka/problems/21.137/verification/2026-08-16T181302Z-minimal-central-obstruction.md`
- `Agents/Kourovka/problems/21.137/verification/2026-08-17T053718Z-mco-affine-norm-cover.md`
- the five other Validator refs in Lead's `2026-08-17T054204Z` request

No web, solution history, quarantined file, experiment, computation, catalogue,
or delegation was used in selecting this route.
