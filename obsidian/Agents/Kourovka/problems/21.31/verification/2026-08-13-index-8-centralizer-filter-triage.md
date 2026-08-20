---
title: "Verification triage — Kourovka 21.31 — index-8 centralizer filter"
problem: "21.31"
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Verification triage — Kourovka 21.31 — index-8 centralizer filter

## Claim

Conditional on the previously checked order-2016 reduction, the forced subgroup (H) satisfies (H=K C_H(K)), and exhaustive checking of the nine SmallGroups isomorphism-type pairs eliminates `[252,11]` and `[252,40]` while retaining seven pairs.

## Target vs witness

The source target is every regular subgroup of `Hol(N)` for finite soluble `N` (PDF p. 169). The witnesses are order-252 SmallGroups representatives and their normal order-12 subgroups. Witness equals target: false. The result can only be a conditional necessary filter and is capped at `status/conjectured` overall.

## Sub-claims

1. The source target is transcribed correctly.
2. From (G=K C_G(K)) and (H/K\le G/K), one obtains (H=K C_H(K)).
3. The prior nine isomorphism-type pairs are exactly the bounded input universe.
4. For every normal subgroup (K\trianglelefteq H) with the prescribed IDs and quotient—not merely one arbitrarily selected representative—the centralizer condition is evaluated correctly.
5. Exactly the claimed two `H` types have no compatible `K`; seven retain at least one compatible `K`.
6. The library groups are external to the claim, so the check is not circular; passing remains only necessary.

## Tools and methods inventory

- GAP 4.12.1 with SmallGrp: independently enumerate every qualifying normal `K` in each of the nine `H` types. A pass proves the bounded isomorphism-type filter, not an order-2016 lift or the conjecture.
- Hand proof: intersect the centralizer factorization with `H`. A pass proves the necessary identity under the prior hypothesis, not that the prior hypothesis holds for any actual counterexample.
- `pdftotext` 24.02.0: confirms the target statement only.
- Sage and Magma are unavailable and unnecessary for this bounded check.

## Hard limit and recommendation

The computation does not construct the target holomorph, extension data, or regular embedding. Proceed with partial verification only; maximum overall verdict `status/conjectured`.
