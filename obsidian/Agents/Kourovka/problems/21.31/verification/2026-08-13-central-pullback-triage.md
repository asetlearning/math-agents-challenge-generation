---
title: "Verification triage — Kourovka 21.31 — central pullback refinement"
problem: "21.31"
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Verification triage — Kourovka 21.31 — central pullback refinement

## Claim

Conditional on the previously checked order-2016 structure, every central extension (1\to Z(K)\to C\to T\to1), (T=GL_3(2)), restricts over the order-21 point stabilizer (P\cong C_7:C_3) to (Z(K)\times P); consequently the pair ((H,K)) must be the direct-product pair ((K\times P,K)), eliminating `[252,2]` and `[252,9]` and retaining exactly `[252,17]`, `[252,19]`, `[252,27]`, `[252,29]`, `[252,38]`.

## Target vs witness

The source target (PDF p. 169) is all regular subgroups of holomorphs of finite soluble groups. The witnesses are seven abstract order-252 pairs and central extensions of (GL_3(2)) by the centers of order-12 groups. Witness equals target: false. Any verdict is at most `status/conjectured` and is only a necessary refinement of the hypothetical order-2016 case.

## Sub-claims

1. The target statement and prior seven-pair universe are correct.
2. The centers Z(K) occurring in the seven pairs are identified exactly.
3. All central extensions of perfect T by each trivial T-module Z are controlled by the Schur multiplier, including non-stem kernels and the 3-primary part.
4. Restriction of every such extension to the fixed P < T splits, and centrality makes the pullback Z x P.
5. The resulting pair-preserving central product is isomorphic to (K\times P).
6. Independent GAP checks identify the direct-product pair for every (K), and inspect every existing survivor's (C_H(K)), intersection with (K), quotient, and splitting type.
7. These objects come from external SmallGroups data and standard extension theory, not from assuming the desired five-pair result.

## Tools available

GAP 4.12.1, SmallGrp 1.5.3, Python 3.12.3, and `pdftotext` 24.02.0. Sage and Magma are unavailable. Only sub-30-second GAP checks are authorized.

## Methods inventory

| Sub-claim | Method | A pass proves | A pass does not prove |
|---|---|---|---|
| 1 | Source PDF and prior verification notes | Correct scope and inputs | Any lift exists |
| 2 | GAP centers and IDs | Exact finite center data | Extension classification |
| 3–4 | Universal coefficient theorem for central extensions of perfect groups, plus an independently checked multiplier of (GL_3(2)) | Exhaustion of central extension classes and split restriction, if all hypotheses are met | Correctness of the full order-2016 reduction |
| 5 | Explicit central-product map / quotient argument | Pair is (K\times P) when pullback is (Z\times P) | Regular holomorph compatibility |
| 6 | Independently written GAP enumeration over all seven pairs | Exact SmallGroups pair identifications and a concrete falsifier search | Universal cohomology theorem by computation alone |

## Hard limits

No order-2016 groups, actions, bijective cocycles, or target holomorphs are enumerated. If the multiplier or universal-coefficient step cannot be independently established, the shortcut remains unverified; checking only the seven already-listed groups would not exhaust possible central extensions.

## Recommendation

Proceed with the bounded proof plus light exact pair checks. Retain `status/conjectured` overall regardless of outcome.
