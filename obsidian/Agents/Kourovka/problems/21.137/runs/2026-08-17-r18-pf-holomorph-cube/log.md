---
title: "PF-HOLOMORPH-CUBE-CLOSURE working log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/power-maps, project/kourovka, status/draft]
---

# PF-HOLOMORPH-CUBE-CLOSURE log

## 2026-08-17T14:08:19Z — active start

- Scope cumulative active time at start: 449 minutes.
- This run's cap: 55 active minutes, with symbolic-model and closure gates at 15
  and 30 minutes.
- Read the common protocol, problem-agent role, canonical revision-2 scope,
  current roster, and the sole unread controlling decision, in that order. Marked
  the decision done and moved it collision-safely to `bus/archive/`.
- Read only the expressly permitted displayed PF definitions in the linked clean
  PF note. No web/history, hidden scratch, stopped family, enumeration, GAP, or
  other computation was used.

## 2026-08-17T14:12:00Z — exact symbolic model before the 15-minute gate

Work over `F=F_3`. Let

`V=<e,f>`, `Z=<c,z_1,z_2>`, and `L=V direct-sum Z`,

with the only nonzero basic bracket `[e,f]=c`. Give `L` its class-two BCH group
law `x*y=x+y+2[x,y]`. This is
`P=H_3(3) x C_3^2`, of order `3^5` and exponent `3`.

Define `T(c)=0`, `T(z_1)=c`, `T(z_2)=z_1`, and `T(V)=0`; put `U=I+T`.
For `a in V`, let `f_a(v)c=[v,a]`, and let
`R_a(v)=f_a(v)z_2`, `R_a(Z)=0`. More generally, the displayed `w`-variant has
`R_(a,w)(v)=f_a(v)(z_2+w)` for `w in <c,z_1>`. The basic PF map is

`A_a=I+T+R_a=S_(R_a) U`,

where `S_phi(v+z)=v+z+phi(v)` for `phi in Hom(V,Z)`. Both `U` and every
central shear `S_phi` preserve the Lie bracket, hence are automorphisms of `P`.
Also

`A_a^3=S_(f_a(.)c)=Inn(a)`

for the convention `x^a=a^(-1)xa`; this rederives rather than assumes the PF
identity.

Let `A` be the closure of the displayed family. For the `w=0` subfamily, the
elements
`A_a U^(-1)=S_(R_a)` give all shears from `V` into `<z_2>`. Conjugating by
`U` gives targets

`z_2`, `Uz_2=z_2+z_1`, `U^2z_2=z_2+2z_1+c`,

which form a basis of `Z`. If only nonzero root labels are taken as generators,
the result is unchanged: every `a` is `b-d` with nonzero `b,d`, so
`A_b A_d^(-1)=S_(R_a)`, and then `S_(-R_b)A_b=U`. Finally every displayed
`w`-variant already lies in the resulting shear group times `U`. Therefore the
exact closure of either the basic or full displayed PF family is

`A=K semidirect <U>`, `K={S_phi:phi in Hom(V,Z)} congruent C_3^6`,

of order `3^7`. Every element has a unique form `S_phi U^i`, `i in F_3`.
Thus the concrete semidirect product `G=P semidirect A` is a finite 3-group of
order `3^12`.

## 2026-08-17T14:14:00Z — complete cube formula and exact closure defect

Write `q=v+z` with `v in V`, `z in Z`, and `alpha=S_phi U^i`. Directly from
`(q,alpha)^3=(q*alpha(q)*alpha^2(q),alpha^3)`, noting that all three `V`-parts
are the same `v`, one obtains

`i=0: (q,alpha)^3=(0,1)`;

`i=1: (q,alpha)^3=(T^2z+T phi(v), S_(T^2 phi))`;

`i=2: (q,alpha)^3=(T^2z+(2T+T^2)phi(v), S_(T^2 phi))`.

Writing `delta=T^2 phi in Hom(V,<c>)`, this gives the complete actual cube set

`C={ (eta,S_delta): delta=0 and eta in <c>, or delta!=0 and eta in <c,z_1> }`.

The `i=1` row already realizes every displayed pair, so this is equality, not an
upper bound. It has `3+8*9=75` elements. More explicitly, take nonzero
`delta`, choose `phi(e)=z_2, phi(f)=0`, and use `v=e,z=0`; this gives
`(z_1,S_delta)`. With `-phi` and `v=z=0` one gets `(0,S_(-delta))`. Their
product is `(z_1,1)`, which is not in `C`, since the `delta=0` fibre is only
`<c>`. Hence the complete cube set is not a subgroup.

All cubes nevertheless lie in the abelian subgroup
`<c,z_1> x Hom(V,<c>)`; in particular every two actual cubes commute.

Each cube has order dividing `3`, so every element of `G` has order dividing
`9`. Choosing `phi(e)=z_2` makes `(S_phi U)^3=S_(T^2phi)!=1`, so `A`, and
hence `G`, contains an element of order `9`. Therefore `exp(G)=9` exactly.

## 2026-08-17T14:19:28Z — active stop and outcome

- This run used 11 active minutes; scope cumulative active time is now 460 minutes.
- The exact symbolic model was obtained before the 15-minute gate, and exact
  exponent plus complete cube-set closure were decided before the 30-minute gate.
- Outcome: `STRATEGY_EXHAUSTED` for this exact PF-holomorph construction. It is an
  `OUT_OF_SCOPE_EXAMPLE`, not a counterexample, because the actual cube set fails
  the subgroup hypothesis by the explicit product above. The unrestricted scope
  remains unanswered.
- No computation or lease was used.
