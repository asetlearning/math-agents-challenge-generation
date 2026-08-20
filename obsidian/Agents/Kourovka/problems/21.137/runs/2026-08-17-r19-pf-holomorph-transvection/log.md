---
title: "PF-HOLOMORPH-ONE-TRANSVECTION working log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/power-maps, project/kourovka, status/draft]
---

# PF-HOLOMORPH-ONE-TRANSVECTION log

## 2026-08-17T14:20:53Z — active start

- Scope cumulative active time at start: 460 minutes.
- Exact assignment: add only `B(e)=e`, `B(f)=f+e`, fixing
  `c,z_1,z_2`, to the exact preceding PF closure. Gates: normal form by 10
  minutes, complete cube-set decision by 22, absolute stop at 35.
- Processed and collision-safely archived the sole unread Lead decision.
- No computation, web/history, hidden artifact, or excluded family was used.

## 2026-08-17T14:27:00Z — exact normal form before the 10-minute gate

Retain `P`, `V=<e,f>`, `Z=<c,z_1,z_2>`, `T`, `U=I+T`, and
`K={S_phi:phi in Hom(V,Z)}` from the exact preceding symbolic model. Put
`b=B|V=I+D`, where `D(e)=0`, `D(f)=e`; then `D^2=0`, `b^3=1`, and `B`
preserves `[e,f]=c`.

The map `B` commutes with `U` and normalizes `K` by precomposition on `V`.
Therefore

`A^+=K semidirect (<U> x <B>)`,

`|A^+|=3^(6+2)=3^8`.

Every element has a unique action normal form

`alpha_(chi,i,j)(v+z)=b^jv+U^iz+chi(v)`,

with `chi in Hom(V,Z)` and `i,j in F_3`. Hence
`G^+=P semidirect A^+` is a finite 3-group of order `3^13`.

## 2026-08-17T14:29:00Z — full cube formula

For `q=v+z`, write `v=xe+yf`. Set

`N_i=I+U^i+U^(2i)`,

so `N_0=0` and `N_1=N_2=T^2`. Direct iteration gives

`alpha^3=S_delta`,

`delta=N_i chi+j(U^i-I)chi D`,

and the class-two BCH product gives

`(q,alpha)^3=(eta,S_delta)`,

`eta=N_i z+(2I+U^i)chi(v)+j chi(Dv)+j y^2 c`.

The last term is the full bracket correction: the sum of the three pairwise
brackets of `v,b^jv,b^(2j)v`, multiplied by `1/2=2` in `F_3`, is
`j y^2c`. In particular every cube lies in the elementary abelian subgroup
`Z x K`, so all actual cubes commute and every element of `G^+` has order at
most 9. The old `S_phi U` element with `T^2phi!=0` still has order 9, hence
`exp(G^+)=9` exactly.

## 2026-08-17T14:29:20Z — complete value set and closure defect

For `chi(e)=a_0c+a_1z_1+a_2z_2`, put `r=a_2`. The possible `delta` are:

- the central-shear plane `K_c=Hom(V,<c>)` (the `j=0` rows);
- and, for `r!=0`, the two tilted planes represented by
  `delta_(r,s,k)(e)=rc`,
  `delta_(r,s,k)(f)=sc+krz_1`, with `k=1,2` and `s in F_3`.

The repeated `r=0` rows add nothing beyond `K_c`. Exact fibre calculation in
the displayed formula gives

- `delta=0`: every `eta in Z` (realized already by `i=0,j!=0`);
- `delta in K_c\{0}`: exactly every `eta in <c,z_1>`;
- `delta=delta_(r,s,k)` with `r!=0`, `k=1,2`: every `eta in Z`.

Thus the complete actual cube set has

`27+8*9+12*27=423`

elements. It is not a subgroup. Explicitly, let

`delta_1(e)=c, delta_1(f)=z_1`,

`delta_2(e)=2c, delta_2(f)=z_1`.

Both `(0,S_(delta_1))` and `(0,S_(delta_2))` are actual cubes (use respectively
`i=1,j=1,chi(e)=z_2` and `i=1,j=2,chi(e)=2z_2`, with `q=1`). Their product
has shear `delta_1+delta_2`, which sends `e` to zero and `f` to `2z_1`.
No permitted cube shear with zero value on `e` has a `z_1` component on `f`,
so the product is not a cube.

The construction therefore fails the actual-cube-set subgroup hypothesis and,
independently, all its actual cubes commute. It is not a counterexample.

## 2026-08-17T14:30:23Z — active stop and outcome

- This run used 10 active minutes; scope cumulative active time is now 470
  minutes.
- The exact normal form was obtained before the 10-minute gate, and the complete
  actual cube-set decision was obtained before the 22-minute gate.
- Outcome: `STRATEGY_EXHAUSTED` for exactly the prescribed one-transvection
  group. The unrestricted scope remains unanswered. The solver is
  `awaiting_lead`, not self-parked.
- No computation or compute lease was used.
