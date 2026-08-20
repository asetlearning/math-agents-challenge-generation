---
title: "Verification triage — Kourovka 21.31 — order-2016 nine-pair reduction"
problem: "21.31"
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/holomorphs
  - project/kourovka
  - status/draft
---

# Verification triage — Kourovka 21.31

## Claim, restated

For any counterexample to Kourovka 21.31 of order 2016 to which Byott's minimal-counterexample theorem applies, the insoluble regular group has soluble radical of order 12 and yields an order-252 subgroup/radical pair isomorphic to exactly one of nine enumerated SmallGroups pairs.

## Target versus witness

- Target: the source PDF asks whether every regular subgroup of the holomorph of every finite soluble group is soluble.
- Witnesses computed: all five SmallGroups isomorphism types of order 12 and all 46 SmallGroups isomorphism types of order 252, filtered by existence of a normal order-12 subgroup with quotient `SmallGroup(21,1)`.
- Witness equals target: false. The finite enumerations test only proposed necessary subobjects of a hypothetical counterexample of one order. They neither construct nor exclude a regular subgroup of a holomorph.

## Sub-claims

1. The source target is transcribed correctly.
2. Byott's theorem applies with the claimed minimality hypotheses and forces a soluble normal subgroup (K\) with quotient (\mathrm{GL}_3(2)\), plus the asserted degree-8 quotient construction.
3. At order 2016, (K=R(G)\) and has order 12.
4. Triviality of (G/K\to\operatorname{Out}(K)\) implies (G=K C_G(K)\), with (C_G(K)/Z(K)\cong\mathrm{GL}_3(2)\).
5. The point stabiliser in the relevant degree-8 action is the nonabelian group `SmallGroup(21,1)`.
6. GAP's order-12 enumeration gives the claimed outer-automorphism orders.
7. GAP's order-252 enumeration is exhaustive and returns exactly the nine stated isomorphism-type pairs.
8. These conditions are necessary only; no lift to a regular subgroup of a holomorph is established.

## Tools available

- GAP 4.12.1 at `/usr/bin/gap`.
- Python 3.12.3 at `/usr/bin/python3`.
- Sage: unavailable.
- Magma: unavailable.

## Methods inventory

| Sub-claim | Method | What a pass proves | What a pass does not prove |
|---|---|---|---|
| 1 | Read configured source PDF, p. 169 | Exact problem target | Any mathematical reduction |
| 2, 5 | Read Byott Theorem 3.2 and its proof/context | Whether the cited theorem really supplies the asserted objects/action | Existence of an order-2016 counterexample |
| 3, 4 | Line-by-line group-theoretic proof check | Conditional structural deductions if hypotheses hold | The Kourovka conjecture or a counterexample |
| 6 | Independent GAP script over all order-12 SmallGroups | Listed finite invariants, subject to GAP library correctness | Any holomorph embedding claim |
| 7 | Independent GAP script over all 46 order-252 SmallGroups | Exact isomorphism-type filter for the stated quotient condition | Uniqueness of embedded subgroups within an isomorphism-type pair; regularity; lifting |
| 8 | Scope comparison | Prevents overclaiming | A positive result on the conjecture |

## Hard limits

The configured source directory contains the Kourovka PDF but not Byott's cited paper. Full verification of the theorem-dependent reduction requires obtaining and reading the cited paper. GAP can independently reproduce the two bounded library computations. Sage and Magma are unavailable but are not needed for those reproductions.

## Recommendation

Proceed with partial/full conditional-reduction verification: independently reproduce both bounded GAP computations and inspect the cited theorem from an authoritative copy. The maximum possible verdict concerns the conditional reduction, not Kourovka 21.31 itself.
