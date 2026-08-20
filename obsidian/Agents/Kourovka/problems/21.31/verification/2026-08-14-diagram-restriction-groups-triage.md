---
title: "Verification triage — Kourovka 21.31 — diagram restriction groups A_i"
problem: "21.31"
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Verification triage — Kourovka 21.31 — diagram restriction groups A_i

## Claim

For the overgroup class represented by (z\in Z(K)[2]), the diagram-induced restriction group on (H=K\times P) is

\[
A_i\cong Stab_{Aut(K)}(z)\times Aut(P),
\]

with the nine claimed orders and explicit factorwise generator actions.

## Target vs witness

The target is the universal holomorph conjecture. The witnesses are automorphism groups attached to nine conditional order-2016 quotient blocks. Witness equals target: false; this design claim remains `status/conjectured` overall.

## Sub-claims

1. Compatible automorphisms of the extension are parametrized exactly by pairs `(a,tau)` preserving the cohomology class.
2. The kernel of this parametrization is `H^1(T,Z(K))=0`, so no global central twist factor is omitted.
3. `Aut(T)_P` restricts isomorphically to `Aut(P)`.
4. Restriction to the split pullback (H=K\times P) introduces no extra `Hom(P,Z(K))` twist from a global lift.
5. The resulting actions are exactly factorwise, the two factors commute and intersect trivially, and their generated permutation/mapping group has the claimed product order.
6. For `K=C6 x C2`, the nonsplit stabilizer has order 4; all other nonzero classes have full `Aut(K)` stabilizer.
7. The nine explicit generator lists consist of valid automorphisms and generate the full claimed (A_i), not only a subgroup of it.

## Methods inventory

- Extension-cohomology proof: establishes exhaustion if naturality, kernel, and restriction are handled correctly.
- Independent GAP 4.12.1 calculation: compute `Aut(T)_P`, its restriction kernel/image, all five involution stabilizers, and the orders of generated factorwise action groups on concrete direct products.
- What a pass does not prove: any regular embedding, restriction-map elimination, compatible additive extension, or target result.

## Hard limits and recommendation

Only small automorphism groups and groups of order 252 will be handled. Proceed with a fresh independent script; retain `status/conjectured` regardless of agreement.
