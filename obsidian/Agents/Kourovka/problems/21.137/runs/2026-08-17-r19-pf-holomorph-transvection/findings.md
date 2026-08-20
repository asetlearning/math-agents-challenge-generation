---
title: "PF-HOLOMORPH-ONE-TRANSVECTION — exact 423-cube closure defect"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/power-maps, project/kourovka, status/conjectured]
---

# PF-HOLOMORPH-ONE-TRANSVECTION outcome

## Outcome

`STRATEGY_EXHAUSTED` for the one authorized transvection repair. The exact group
`G^+` is a finite 3-group of order `3^13` and exponent exactly `9`, but its
complete actual cube set has 423 elements and is not a subgroup. Moreover every
actual cube lies in one elementary abelian subgroup. Thus this fixed group is an
`OUT_OF_SCOPE_EXAMPLE`, not a counterexample, and the unrestricted revision-2
scope remains unanswered.

## Base model and the added transvection

Work over `F=F_3`. Retain the preceding exact model

`P=H_3(3) x C_3^2`

on the class-two BCH Lie algebra

`L=V direct-sum Z`, `V=<e,f>`, `Z=<c,z_1,z_2>`, `[e,f]=c`,

with `T(c)=0`, `T(z_1)=c`, `T(z_2)=z_1`, `T(V)=0`, and `U=I+T`.
The exact PF closure was

`A=K semidirect <U>`,
`K={S_phi:phi in Hom(V,Z)}`,
`S_phi(v+z)=v+z+phi(v)`.

Add exactly the prescribed map `B`, fixing `Z` and satisfying

`B(e)=e`, `B(f)=f+e`.

Writing `b=B|V=I+D`, one has `D(e)=0`, `D(f)=e`, `D^2=0`, so `B^3=1`.
Also `[B(e),B(f)]=[e,f+e]=c`, hence `B` is a bracket-preserving
automorphism of `P`.

## Exact normal form and order

The map `B` commutes with `U`, since they act on complementary summands, and it
normalizes `K` by precomposition on `V`. Its image on `V` is not represented by
`KU`, so the intersections are trivial. Consequently

`A^+=<A,B>=K semidirect (<U> x <B>)`

and `|A^+|=3^8`.

Equivalently, every element of `A^+` has a unique action normal form

`alpha_(chi,i,j)(v+z)=b^jv+U^iz+chi(v)`,

where `chi in Hom(V,Z)` and `i,j in F_3`. This is directly reconstructible as
a subgroup of `Aut(P)`. The left semidirect product

`G^+=P semidirect A^+`

therefore has order `3^13`.

## Full cube formula

Let `q=v+z`, where `v=xe+yf`, and put

`N_i=I+U^i+U^(2i)`.

In characteristic three, `N_0=0` and `N_1=N_2=T^2`. Directly iterating the
normal-form action gives

`alpha^3=S_delta`,

`delta=N_i chi+j(U^i-I)chi D`.

The three `V`-parts in the `P`-norm are `v,b^jv,b^(2j)v`; their sum is zero.
Their class-two BCH bracket correction is `j y^2c`. Thus the complete
semidirect cube formula is

`(q,alpha)^3=(eta,S_delta)`,

`eta=N_i z+(2I+U^i)chi(v)+j chi(Dv)+j y^2c`.

This retains both the `P` and automorphism components.

## Complete actual cube-value set

Define `K_c=Hom(V,<c>)`. For `r,s in F_3` and `k in {1,2}`, define

`delta_(r,s,k)(e)=rc`,

`delta_(r,s,k)(f)=sc+krz_1`.

Expanding the full formula for all nine pairs `(i,j)` gives exactly the following
disjoint description:

1. `delta=0`, with arbitrary `eta in Z`;
2. `delta in K_c\{0}`, with arbitrary `eta in <c,z_1>`;
3. `delta=delta_(r,s,k)` with `r!=0`, `s in F_3`, `k=1,2`, with arbitrary
   `eta in Z`.

For completeness, the support calculation is as follows. If `j=0`, then
`delta=T^2chi`, giving precisely `K_c`. If `i=1` and `j!=0`, then

`delta(e)=a_2c`,
`delta(f)=(b_2+ja_1)c+ja_2z_1`.

If `i=2` and `j!=0`, then

`delta(e)=a_2c`,
`delta(f)=(b_2+j(2a_1+a_2))c+2ja_2z_1`.

These give the two tilted values `k=1,2`; the `r=0` cases coincide with
`K_c`. The `eta` formula shows: the zero shear gets all of `Z` from the
`i=0,j!=0` row; a nonzero `K_c` shear gets exactly `<c,z_1>`; and a tilted
shear with `r!=0` gets all of `Z` because its `z_1,z_2` coefficient map in
`v=(x,y)` has nonzero determinant.

Therefore

`|Cubes(G^+)|=|Z|+(|K_c|-1)|<c,z_1>|+12|Z|`

`=27+8*9+12*27=423`.

This is the complete actual value set, not the subgroup it generates.

## Explicit failure of closure

Let

`delta_1(e)=c`, `delta_1(f)=z_1`,

`delta_2(e)=2c`, `delta_2(f)=z_1`.

The value `(0,S_(delta_1))` is the cube with
`q=1`, `i=1`, `j=1`, `chi(e)=z_2`, `chi(f)=0`. The value
`(0,S_(delta_2))` is the cube with
`q=1`, `i=1`, `j=2`, `chi(e)=2z_2`, `chi(f)=0`.
Their product is `(0,S_(delta_1+delta_2))`, whose shear sends

`e -> 0`, `f -> 2z_1`.

It is absent from the exact support above: every supported shear that kills `e`
maps `f` into `<c>`. Hence the complete cube set is not a subgroup.

## Exact exponent and commutativity

Every displayed cube belongs to

`E=Z x K <= G^+`.

Central shears fix `Z` pointwise, so `E` is elementary abelian. Hence every
element of `G^+` has ninth power one and every pair of actual cubes commutes.
The preceding PF element `S_phi U` with `T^2phi!=0` remains in `A^+` and has
order `9`. Therefore `exp(G^+)=9` exactly.

## Constraint-and-conclusion matrix

| constraint_id | role | candidate value / evidence | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | One fixed `p=3` group cannot answer the universal assertion after another row fails. | not established |
| `21.137-odd-p-not-2` | admissibility | `p=3`. | pass |
| `21.137-odd-finite-p-group` | admissibility | `G^+=P semidirect A^+`, `|G^+|=3^13`. | pass |
| `21.137-odd-exponent-p2` | admissibility | Full cube formula gives exponent at most 9; an inherited PF element has order 9. | pass |
| `21.137-odd-power-set-definition` | admissibility | The complete actual cube set is the exact three-row fibre family above, of size 423. | pass |
| `21.137-odd-power-set-subgroup` | admissibility | The two explicit actual cubes above multiply to a value outside the set. | **fail** |
| `21.137-odd-P-abelian` | target conclusion | The hypothesis fails; independently, all actual cube values commute. | not violated |

## What this does not establish

This does not answer the unrestricted scope or rule out other finite
constructions. It exactly exhausts only the one fixed group obtained by adding
the prescribed canonical transvection to the exact PF closure. No conjugate
transvection, generator subset, Sylow layer, or alternate family was considered.

## Resource use

The normal form, cube formula, complete fibres, count, exponent, and closure
defect were derived symbolically. No enumeration, GAP, script, compute lease,
web/history, hidden material, or excluded family was used.

