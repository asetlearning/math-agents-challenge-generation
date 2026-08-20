---
title: "PF-JORDAN-CAPACITY — common-flag observable saturates locally"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/power-maps, project/kourovka, status/conjectured]
---

# PF-JORDAN-CAPACITY outcome

## Active target

For every odd prime p and finite p-group G of exact exponent p^2, if the complete
actual pth-power value set P is a subgroup, prove P abelian.

The active assignment is not answered.

## Outcome

`STRATEGY_EXHAUSTED` for `PF-JORDAN-CAPACITY` as presently defined. The common
flag and full Jordan-rank data recover the reviewed `J_(p+1)` block and
`dim Z(P)>=p` bounds, but do not force the admissible labels into a proper
subspace. A prime-uniform local saturation calculation below shows that every
label can occupy exactly the same flag/Jordan cell. It also leaves many
independent per-label root operators, so a strict capacity deficit cannot be
obtained from the flag, rank tuple, fixed-space row, and separate label equations
alone.

This is a method-failure certificate, not a proof, group construction, or
counterexample.

## Reviewed conditional inputs

Assume a quotient-minimal counterexample and write its nonabelian actual power
subgroup as the class-two exponent-p Lie algebra L. The reviewed reductions give

- `C=L'` one-dimensional and fixed pointwise by the root-action p-group;
- `V=L/Z(L)` with its nondegenerate alternating form `omega`, where
  `D_a(v)=omega(v,a)c` for `c` spanning C;
- a complete common flag lowered by every `N=A-I`;
- for every nonzero label `a in V`, a root action satisfying
  `N^p=D_a` and fixing a representative of a.

These are used only conditionally. They do not assert that a counterexample
exists.

## What the flag actually forces

Refine the common flag so that `F_1=C`. Since `N^p=D_a` for every label and
`N^p F_p=0`, simultaneous label-surjectivity gives `F_p<=Z(L)`, the reviewed
center bound.

For a nonzero label, `rank N^p=1`. Also `N^(p+1)=N D_a=0`, since `D_a` has image
in the pointwise fixed line C. Hence N has exactly one Jordan block `J_(p+1)`
and all its other blocks have size at most p. Because the label a is a fixed
noncentral vector, at least one further block is present. Thus
`dim L>=p+2`. This is exactly the existing dimension mechanism; it has not yet
restricted a to any proper subspace of V.

## Prime-uniform local saturation calculation

The limitation is not just a failure to choose the flag cleverly. Fix any odd p
and any symplectic space `(V,omega)` of dimension `2d>=2`. Let

`Z=<c,z_1,...,z_(p-1)>`,

and form the class-two Lie algebra `L=V direct-sum Z` with

`[v,w]=omega(v,w)c`, `Z=Z(L)`, and `L'=<c>`.

Define `T` by `T(c)=0`, `T(z_i)=z_(i-1)` with `z_0=c`, and `T(V)=0`. For a
nonzero `a in V`, write `f_a(v)=omega(v,a)`. For every

`w in Z_-:=<c,z_1,...,z_(p-2)>`,

define an endomorphism N on L by

`N|_Z=T`, and `N(v)=f_a(v)(z_(p-1)+w)` for `v in V`.

Then:

1. `A=I+N` is a Lie automorphism: it fixes c, acts on V only by adding central
   vectors, and therefore preserves `[v_1,v_2]=omega(v_1,v_2)c`.
2. All these N lower one common complete flag obtained by listing
   `c,z_1,...,z_(p-1)` before a basis of V.
3. Because `z_(p-1)+w` is a cyclic vector for T,
   `N^p(v)=f_a(v)c=D_a(v)` and `N^p(Z)=0`.
4. `N(a)=0` by alternation of omega.
5. N has the identical full rank/Jordan profile
   `J_(p+1) direct-sum J_1^(2d-1)` for every nonzero a and every w.

Thus every nonzero label in V occurs in exactly the same flag/Jordan cell, with
at least `|Z_-|=p^(p-1)` distinct ambient root operators per label. Taking
`w=0` and all labels a, the common fixed space of this simultaneous family is
exactly C: `A_0=I+T` forces the central part into `ker T=C`, and nondegeneracy of
omega forces the V-part to vanish when every a is imposed.

Consequently the span of the local label union is all of V (`delta=0`), even
after retaining the sharp center dimension, the full rank tuple, the exact
fixed-label equation, and the minimal fixed-space line.

## Essential limitation of the certificate

The displayed automorphisms are an ambient simultaneous family. I have not
asserted that the family is closed under multiplication, realized by one group
extension, or compatible with the complete actual power map. In particular it
is not a witness and it does not refute a future lemma that uses cross-root
multiplication or extension coherence. Closing or realizing this family was not
attempted because the present assignment excludes the construction class into
which that step would lead.

What the calculation does establish is narrower and exact: no proper-label
subspace or strict per-label capacity lemma follows from the PF observable's
common flag, rank tuple, fixed-space positions, and individual equations alone.
The missing information is a relation between different roots. No such
prime-uniform relation survived this run before the method hard kill.

## Scope matrix

| constraint_id | role in this outcome | result |
|---|---|---|
| 21.137-odd-forall-p-G | local obstruction is uniform for every odd p, but is not a proof for every G | not established |
| 21.137-odd-p-not-2 | only odd p is used | pass |
| 21.137-odd-finite-p-group | no candidate finite group is asserted | not applicable to method certificate |
| 21.137-odd-exponent-p2 | no candidate group is asserted | not established |
| 21.137-odd-power-set-definition | no actual power set is asserted | not established |
| 21.137-odd-power-set-subgroup | no subgroup closure is asserted | not established |
| 21.137-odd-P-abelian | the target conclusion remains open | not established |

## Recommended alternatives for Lead

1. A genuinely new proof route would have to add a cross-root multiplication or
   extension-coherence invariant; another refinement of individual Jordan ranks
   or common-flag positions will repeat the saturation above.
2. The recorded order-3^10 equivariant-label screen is qualitatively different
   but only a bounded p=3 layer, so it cannot convert this failure into a
   prime-uniform result.

