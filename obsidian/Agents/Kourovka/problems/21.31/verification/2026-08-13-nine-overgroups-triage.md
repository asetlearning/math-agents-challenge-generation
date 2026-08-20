---
title: "Verification triage — Kourovka 21.31 — nine overgroups and quotient-action kernel"
problem: "21.31"
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Verification triage — Kourovka 21.31 — nine overgroups and quotient-action kernel

## Claim

Conditional on the previously checked order-2016 reduction, the five possible radical types K yield exactly nine pair-isomorphism classes (G,K) satisfying G/K isomorphic to T=GL(3,2) and G=K C_G(K), and the quotient automorphism action Theta has kernel exactly K.

## Target vs witness

The PDF target is every regular subgroup of `Hol(N)` for arbitrary finite soluble `N`. The witnesses are central products of five order-12 groups with central extensions of `GL(3,2)`, plus a quotient action attached to a hypothetical order-2016 counterexample. Witness equals target: false. The result is conditional and remains `status/conjectured` overall.

## Sub-claims

1. Every relevant (G) is a central product of (K) and a central extension of (T) by (Z(K)).
2. Fixed-kernel/fixed-quotient extension classes are `Hom(M(T),Z(K))`, with no omitted `Ext` term.
3. Passing to pair isomorphism uses the correct `Aut(K) x Aut(T)` action; no further classes or collapses occur.
4. The five center-involution orbit counts are `2,2,1,2,2`, including one nonzero orbit for `C6 x C2`.
5. Split and nonsplit classes do not collapse, and every nonsplit pushout exists, has order 2016, quotient (T), and radical exactly (K).
6. The total nine counts pair-isomorphism classes, not merely marked extension classes or abstract groups.
7. The quotient linear action defining `Theta` is faithful, so its pullback kernel in (G) is (K); affine faithfulness alone is not sufficient.
8. The construction and orbit data are external to the asserted count and therefore noncircular.

## Tools available and methods inventory

- GAP 4.12.1 / SmallGrp 1.5.3: independently recompute perfectness, multiplier, center-involution automorphism orbits, Schur cover, representative orders, quotients, radicals where feasible, and invariants separating split/nonsplit. A pass proves bounded construction facts, not the target conjecture.
- Hand cohomology proof: universal coefficient sequence and natural automorphism action. A pass proves completeness only if the equivalence relation is identified correctly.
- Hand quotient-action proof using the exact crossed-map quotient. A pass proves `ker(Theta)=K` only if the descended linear homomorphism (T\to GL_3(2)) is shown nontrivial/faithful.
- `pdftotext` 24.02.0 confirms target scope only. Sage and Magma are unavailable.

## Hard limits

No order-2016 SmallGroups library is installed, and no heavy enumeration is authorized. Explicit representatives will be constructed only within short caps. If the derivation of the quotient linear action is absent from the cited Byott construction, `ker(Theta)=K` must remain unverified even if the nine-class count passes.

## Recommendation

Proceed with independent light computations and line-by-line proofs. Maximum overall status: `conjectured`.
