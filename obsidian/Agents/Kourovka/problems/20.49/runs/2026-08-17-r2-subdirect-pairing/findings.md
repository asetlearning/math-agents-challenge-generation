---
title: "Partial reduction — exact fibre-product lift profiles for Problem 20.49"
problem: "20.49"
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
direction: proof
outcome: PARTIAL_RESULT
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/exponent
  - topic/subdirect-product
  - topic/nielsen-equivalence
  - project/kourovka
  - status/conjectured
---

# Exact subdirect-pairing criterion and residual obstruction

## Active target

Scope: `20.49/two-generated-same-exponent`  
Assignment revision: 1  
Target: every finite group `G` contains an at-most-two-generated subgroup `H`
with `exp(H)=exp(G)`.

This note is a candidate partial reduction only. It does not answer the universal
target.

## Setup inherited from the reviewed package

Assume `G` is a least-order counterexample, and let `M,N` be distinct minimal
normal subgroups. Then

```text
M cap N = 1,                 [M,N]=1,
A=G/M,  B=G/N,  C=G/MN.
```

The canonical map identifies `G` with the full fibre product

```text
A x_C B = {(a,b) in A x B : alpha(a)=beta(b)},
```

where `alpha:A->C` and `beta:B->C` are the natural maps. Surjectivity onto the
fibre product follows either directly or by the order calculation

```text
|A x_C B|=|A||B|/|C|=|G|
```

using `|MN|=|M||N|`. The reviewed direct indecomposability of `G` also gives
`MN<G`: if `MN=G`, then `[M,N]=1` and `M cap N=1` would give `G=M x N`.
Consequently `C` is a nontrivial proper common quotient.

Put

```text
e=exp(G), e_A=exp(A), e_B=exp(B).
```

The embedding and the two quotient maps give the exact equality

```text
e = lcm(e_A,e_B).                                      (1)
```

Indeed, `e_A,e_B` divide `e`, while every element order in the embedded copy of
`G` divides `lcm(e_A,e_B)`.

## Simultaneous-lift lemma

Let `F=F(s,t)` be the free group of rank two. Suppose homomorphisms

```text
phi:F->A,  psi:F->B
```

satisfy

```text
alpha phi = beta psi.                                  (2)
```

Then `(phi,psi)` has image in `A x_C B=G`, and, writing `rho:F->G` for the
resulting homomorphism,

```text
exp(rho(F)) = lcm(exp(phi(F)), exp(psi(F))).             (3)
```

For (3), each projected exponent divides `exp(rho(F))`; conversely the image is a
subgroup of `phi(F) x psi(F)`.

It follows that if `phi(F)` and `psi(F)` have exponents `e_A` and `e_B`,
respectively, then their two generator pairs give a two-generated subgroup of `G`
of exponent `e` by (1). More generally, it is enough that the two projected
exponents have least common multiple `e`.

There is a useful Nielsen formulation. If the two base maps `alpha phi` and
`beta psi` lie in the same `Aut(F)` orbit in `Hom(F,C)`, Nielsen transformations
of the two generator pairs make (2) hold. Nielsen transformations preserve the
generated subgroups, so they preserve both projected exponents. Thus:

> Full-exponent witness pairs in `A` and `B` pair simultaneously whenever their
> induced ordered pairs in `C` are Nielsen-equivalent.

This is an exact sufficient theorem, not an existence theorem for such compatible
witnesses.

## Exact Goursat obstruction

For a Nielsen orbit `O` in `Hom(F,C)`, define the attainable exponent profile

```text
E_A(O) = { exp(phi(F)) : phi:F->A and [alpha phi]=O },
E_B(O) = { exp(psi(F)) : psi:F->B and [beta psi]=O }.
```

These are well-defined on Nielsen orbits because precomposition by an automorphism
of `F` does not change the image subgroup. Freeness of `F` and surjectivity of
`alpha,beta` ensure that every base map has lifts to both factors.

Equations (1)--(3) give the exact equivalence

```text
G has a two-generated subgroup of exponent e

iff

there are O, r in E_A(O), s in E_B(O) with lcm(r,s)=e.   (4)
```

For the full-factor witnesses supplied by minimality, put

```text
W_A={O : e_A in E_A(O)},
W_B={O : e_B in E_B(O)}.
```

Minimality applied separately to the proper quotients `A` and `B` proves only

```text
W_A != empty,  W_B != empty.
```

The desired simultaneous choice is exactly `W_A cap W_B != empty`. In a
hypothetical counterexample one must therefore have

```text
W_A cap W_B = empty.                                    (5)
```

This is the precise fibre/Goursat obstruction hidden by the phrase “choose the
quotient pairs compatibly.” Separate nonemptiness does not identify a common base
map or even a common Nielsen orbit.

There is a second, necessary caution: (5) is stronger than needed for the proof
route but weaker than the full counterexample obstruction. A pair upstairs may
have exponent `e` even when neither projected subgroup has the full exponent of
its whole factor; the two projections can carry complementary prime-power maxima.
The exact residual obstruction is the negation of (4):

```text
for every O, every r in E_A(O), and every s in E_B(O),
lcm(r,s)<e.                                              (6)
```

Primewise, if `a_p=v_p(e)`, condition (6) says that for every such `O,r,s` there
is a prime `p` (allowed to depend on the choices) with

```text
max(v_p(r),v_p(s)) < a_p.                               (7)
```

Thus the exponent effect of the fibre obstruction is not merely failure to make
both factor projections full: every compatible lift profile must have a common
missing maximal prime power.

Finally, if the common base map has image `D<C`, every corresponding subgroup
upstairs lies in the proper subgroup `G_D`, the inverse image of `D`. Reviewed
proper-subgroup exponent-criticality gives `exp(G_D)<e`. Hence only Nielsen orbits
of epimorphisms `F->C` can possibly satisfy (4). If `d(C)>2`, there are no such
orbits, and this subdirect route has no contradiction available without additional
structure.

## Why the proposed monolithicity inference stops here

The reviewed hypotheses “nonsoluble,” `d(G)=3`, proper-subgroup exponent drop, and
proper-quotient exponent drop establish (1) and restrict a successful base map to
an epimorphism. They do not, by themselves, prove an intersection of `W_A,W_B` or
the stronger prime-cover condition in (4). In particular, the two quotient
applications of minimality return witnesses in possibly different Nielsen fibres.

Therefore the proposed choice of compatible quotient generators is unsupported
unless one adds a new theorem forcing a common Nielsen lift profile (or forcing
complementary exponent profiles over one common orbit). The exact next target is:

```text
prove, from the least-counterexample hypotheses, that some epimorphism orbit
O in Epi(F_2,C)/Aut(F_2) admits r in E_A(O), s in E_B(O) with lcm(r,s)=e.
```

Without that new input, distinct minimal normal subgroups have not been excluded.

## What this does not establish

- It does not prove `G` is monolithic.
- It does not prove that the disjoint profiles (5)--(6) are realizable by a least
  counterexample.
- It does not turn separate quotient witnesses into compatible witnesses.
- It does not answer the universal revision-1 scope.
