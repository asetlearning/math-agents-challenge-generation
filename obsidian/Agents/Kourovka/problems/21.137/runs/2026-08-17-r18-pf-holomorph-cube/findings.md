---
title: "PF-HOLOMORPH-CUBE-CLOSURE — exact closure gives a 75-value non-subgroup"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/power-maps, project/kourovka, status/conjectured]
---

# PF-HOLOMORPH-CUBE-CLOSURE outcome

## Outcome

`STRATEGY_EXHAUSTED` for the exact displayed PF-holomorph construction. Closing
the PF automorphisms produces a finite 3-group `G` of order `3^12` and exact
exponent `9`, but its complete actual cube set has 75 elements and is not a
subgroup. In fact all its cube values commute. Thus this is a reconstructible
`OUT_OF_SCOPE_EXAMPLE`, not a counterexample, and the unrestricted revision-2
scope remains unanswered.

## Reconstructible finite model

Work over `F=F_3`. Let

`V=<e,f>`, `Z=<c,z_1,z_2>`, `L=V direct-sum Z`,

with `[e,f]=c` and all other basic brackets zero. Under the class-two BCH law
`x*y=x+y+2[x,y]`, `L` is the exponent-three group
`P=H_3(3) x C_3^2` of order `3^5`.

Let

`T(c)=0`, `T(z_1)=c`, `T(z_2)=z_1`, `T(V)=0`, and `U=I+T`.

For `a in V`, define `f_a` by `[v,a]=f_a(v)c`, and put
`R_a(v)=f_a(v)z_2`, `R_a(Z)=0`. The full displayed variant replaces this by
`R_(a,w)(v)=f_a(v)(z_2+w)` for `w in <c,z_1>`. For any
`phi in Hom(V,Z)`, write

`S_phi(v+z)=v+z+phi(v)`.

The displayed PF automorphism is

`A_a=I+T+R_a=S_(R_a)U`.

It preserves the bracket, and a direct calculation gives

`A_a^3=S_(f_a(.)c)=Inn(a)`.

The exact finite closure of all displayed PF maps (including all `w`-variants) is

`A=K semidirect <U>`, where
`K={S_phi:phi in Hom(V,Z)} congruent C_3^6`.

Indeed, the `w=0` maps already suffice. If `A_0=U` is included, the differences
`A_aU^(-1)` give every shear into `<z_2>`. If only nonzero labels are called
root maps, the same conclusion follows because every `a in V` is `b-d` for
nonzero `b,d`, whence `A_bA_d^(-1)=S_(R_a)` and then
`S_(-R_b)A_b=U`. Conjugating these shears by `U` gives the three targets

`z_2`, `Uz_2=z_2+z_1`, `U^2z_2=z_2+2z_1+c`

which form a basis of `Z`. Every `w`-variant is already a shear followed by `U`,
so it enlarges nothing. Hence `|A|=3^7`. Every element of `A` has a unique form
`S_phi U^i`, `i in F_3`. Define the concrete left semidirect product

`G=P semidirect A`.

Then `|G|=3^12`.

## Full cube formula

Write `q=v+z`, with `v in V`, `z in Z`, and write
`alpha=S_phi U^i`. Since `alpha` is the identity on `P/Z(P)`, the three factors
in the `P`-component of

`(q,alpha)^3=(q*alpha(q)*alpha^2(q),alpha^3)`

have the same `V`-part. Their pairwise brackets vanish. Using
`I+U+U^2=T^2` in characteristic three gives

| `i` | `P`-component | automorphism component |
|---|---|---|
| `0` | `0` | `1` |
| `1` | `T^2z+T phi(v)` | `S_(T^2phi)` |
| `2` | `T^2z+(2T+T^2)phi(v)` | `S_(T^2phi)` |

This is the full semidirect cube, including the automorphism component.

## Complete actual cube-value set

Put `delta=T^2phi in Hom(V,<c>)`. In the `i=1` row the `z_1` coefficient of
the `P`-component is the scalar `delta(v)/c`, while `T^2z` makes the
`c`-coefficient arbitrary. The `i=2` row gives the same support. Therefore

`Cubes(G)={ (eta,S_delta):`

- `delta=0` and `eta in <c>`; or
- `delta!=0` and `eta in <c,z_1>`.

Every displayed pair is attained already with `i=1`, so this is the complete
actual value set, not its generated subgroup. Its size is

`3+8*9=75`.

For an explicit closure defect, take `delta(e)=c`, `delta(f)=0` and
`phi(e)=z_2`, `phi(f)=0`. The `i=1`, `q=e` cube is
`(z_1,S_delta)`. Replacing `phi` by `-phi` and taking `q=1` gives the cube
`(0,S_(-delta))`. Their product is `(z_1,1)`, which is not a cube because the
`delta=0` fibre is exactly `<c>`. Thus the actual cube set is not a subgroup.

All cubes lie in the abelian subgroup

`<c,z_1> x {S_delta:delta in Hom(V,<c>)}`,

so every pair of actual cubes commutes.

## Exact exponent

The full formula places every cube in an elementary abelian subgroup, hence
`g^9=1` for every `g in G`. On the other hand, for
`phi(e)=z_2`, `phi(f)=0`,

`(S_phi U)^3=S_(T^2phi)!=1`.

Thus `G` contains an element of order `9` and `exp(G)=9` exactly.

## Constraint-and-conclusion matrix

| constraint_id | role | candidate value / evidence | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | One explicit `p=3` construction cannot establish or refute the universal assertion without all remaining rows. | not established |
| `21.137-odd-p-not-2` | admissibility | `p=3`. | pass |
| `21.137-odd-finite-p-group` | admissibility | `G=P semidirect A`, `|G|=3^12`. | pass |
| `21.137-odd-exponent-p2` | admissibility | The cube formula gives exponent at most 9 and `S_phi U` above has order 9. | pass |
| `21.137-odd-power-set-definition` | admissibility | The formula and fibre analysis enumerate the complete actual set `{g^3:g in G}`, of size 75. | pass |
| `21.137-odd-power-set-subgroup` | admissibility | Two displayed actual cubes multiply to `(z_1,1)`, which is not an actual cube. | **fail** |
| `21.137-odd-P-abelian` | target conclusion | The hypothesis fails; moreover all actual cube values commute, so the desired conclusion is not violated. | not violated |

## What this does not establish

This does not answer the unrestricted odd-prime scope, rule out other holomorph
constructions, or prove the target assertion. It exactly exhausts only the
semidirect product obtained by closing the displayed PF automorphisms on
`H_3(3) x C_3^2`.

## Reproducibility and resource use

The model, closure, cube formula, and defect are symbolic and finite as displayed.
No enumeration, GAP, script, hidden scratch artifact, web/history, or compute lease
was used. The complete derivation is also recorded in `log.md` in this run dir.
