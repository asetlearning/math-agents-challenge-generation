---
title: "Verification — Kourovka 21.31 — order-2016 nine-pair reduction"
problem: "21.31"
claim: "Any order-2016 counterexample yields the stated radical-centraliser structure and one of nine necessary order-252/order-12 SmallGroups pairs."
claimant: Problem-21.31
target_object: "All regular subgroups G of Hol(N), for arbitrary finite soluble groups N"
witness_object: "The five SmallGroups types of order 12 and 46 SmallGroups types of order 252"
witness_equals_target: false
citation: "N. P. Byott, J. Algebra 638 (2024), Theorem 3.2 and its proof; arXiv:2205.13464v4"
verification_method: "source comparison, line-by-line conditional group argument, and two independent GAP 4.12.1 scripts"
tools_used: ["GAP 4.12.1", "pdftotext"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.31

## The claim

Conditional on an order-2016 counterexample, the claimant reduces its insoluble regular group to a soluble radical (K\) of order 12, a centraliser factor above (\mathrm{GL}_3(2)\), and one of nine necessary order-252 subgroup/radical isomorphism-type pairs.

## Target vs witness

The configured Kourovka PDF, p. 169, asks whether every regular subgroup of (\operatorname{Hol}(N)\) is soluble whenever (N\) is finite and soluble. The computed witnesses are only all groups of orders 12 and 252 satisfying a quotient filter. They are not regular subgroups of holomorphs and are not equal to the target.

The witness-equals-target sub-claim is therefore false. Under the Validator protocol this caps the overall verdict at `status/conjectured`, even though the bounded subcomputations were independently reproduced.

## Sub-claims and what each method proves

1. Byott Theorem 3.2(i) gives, for a minimal counterexample, a soluble normal (K\) with quotient (T\cong\mathrm{GL}_3(2)\), and every maximal normal subgroup of (N\) has index 2. The published theorem states this explicitly.
2. The proof of Theorem 3.2 constructs a maximal proper (G\)-invariant normal subgroup (M\) and quotient (N/M\cong C_2^3\) in the minimal case; its quotient action has the soluble point stabiliser of order 21 used by the claimant.
3. If (|G|=2016\), then (|K|=12\). Since (G/K\) is nonabelian simple and (K\) is soluble, the soluble radical is exactly (K\).
4. Conjugation induces (G/K\to\operatorname{Out}(K)\). Since the independently computed outer automorphism group orders are all less than 168, simplicity forces the map to be trivial. Then (G=K C_G(K)\), (K\cap C_G(K)=Z(K)\), and (C_G(K)/Z(K)\cong G/K\).
5. The natural degree-8 action of (\mathrm{GL}_3(2)\) has point stabiliser of order 21; it is nonabelian and hence is `SmallGroup(21,1)`, (C_7:C_3\).
6. An independent exhaustive GAP enumeration reproduces exactly nine order-252/order-12 isomorphism-type pairs with that quotient.
7. None of these checks proves a regular embedding or a lift to order 2016.

## Circularity check

The SmallGroups objects are library representatives independent of the claim. The quotient predicate is imposed because the theorem says it is necessary, so passing the predicate cannot prove a counterexample exists. The claimant labels it only as a necessary reduction, avoiding that circular inference.

## Evidence

Authoritative paper inspected: N. P. Byott, *On Insoluble Transitive Subgroups in the Holomorph of a Finite Soluble Group*, arXiv:2205.13464v4, especially Definition 3.1, Theorem 3.2, and the proof of Theorem 3.2.

Independent scripts:

- `Agents/Kourovka/problems/21.31/verification/scratch/independent_order12.g`
- `Agents/Kourovka/problems/21.31/verification/scratch/independent_order252.g`

Verbatim command and output:

```text
$ timeout 30s gap -q Agents/Kourovka/problems/21.31/verification/scratch/independent_order12.g
GAP_VERSION=4.12.1
NUMBER_SMALL_GROUPS_12=5
K_ID=[ 12, 1 ] CENTER_ORDER=2 AUT_ORDER=12 INNER_ORDER=6 OUT_ORDER=2
K_ID=[ 12, 2 ] CENTER_ORDER=12 AUT_ORDER=4 INNER_ORDER=1 OUT_ORDER=4
K_ID=[ 12, 3 ] CENTER_ORDER=1 AUT_ORDER=24 INNER_ORDER=12 OUT_ORDER=2
K_ID=[ 12, 4 ] CENTER_ORDER=2 AUT_ORDER=12 INNER_ORDER=6 OUT_ORDER=2
K_ID=[ 12, 5 ] CENTER_ORDER=12 AUT_ORDER=12 INNER_ORDER=1 OUT_ORDER=12

$ timeout 60s gap -q Agents/Kourovka/problems/21.31/verification/scratch/independent_order252.g
GAP_VERSION=4.12.1
NUMBER_SMALL_GROUPS_252=46
PAIR=[ [ 252, 2 ], [ 12, 2 ] ] QUOTIENT_ID=[ 21, 1 ]
PAIR=[ [ 252, 9 ], [ 12, 5 ] ] QUOTIENT_ID=[ 21, 1 ]
PAIR=[ [ 252, 11 ], [ 12, 5 ] ] QUOTIENT_ID=[ 21, 1 ]
PAIR=[ [ 252, 17 ], [ 12, 1 ] ] QUOTIENT_ID=[ 21, 1 ]
PAIR=[ [ 252, 19 ], [ 12, 2 ] ] QUOTIENT_ID=[ 21, 1 ]
PAIR=[ [ 252, 27 ], [ 12, 3 ] ] QUOTIENT_ID=[ 21, 1 ]
PAIR=[ [ 252, 29 ], [ 12, 4 ] ] QUOTIENT_ID=[ 21, 1 ]
PAIR=[ [ 252, 38 ], [ 12, 5 ] ] QUOTIENT_ID=[ 21, 1 ]
PAIR=[ [ 252, 40 ], [ 12, 5 ] ] QUOTIENT_ID=[ 21, 1 ]
PAIR_COUNT=9
DISTINCT_PAIR_COUNT=9
PAIRS=[ [ [ 252, 2 ], [ 12, 2 ] ], [ [ 252, 9 ], [ 12, 5 ] ],
  [ [ 252, 11 ], [ 12, 5 ] ], [ [ 252, 17 ], [ 12, 1 ] ],
  [ [ 252, 19 ], [ 12, 2 ] ], [ [ 252, 27 ], [ 12, 3 ] ],
  [ [ 252, 29 ], [ 12, 4 ] ], [ [ 252, 38 ], [ 12, 5 ] ],
  [ [ 252, 40 ], [ 12, 5 ] ] ]
```

## Verdict

`status/conjectured` for the overall conditional reduction. The two bounded finite enumerations were independently reproduced and agree exactly, but the computed witnesses are not the Kourovka target.

## Why this verdict

The theorem-dependent deductions are coherent and the finite filters reproduce. Nevertheless, this is a necessary-condition reduction about hypothetical subobjects, not a verification in the target holomorph. Protocol requires the lower verdict whenever witness and target differ.

## What is NOT established

No counterexample exists; no order-2016 case is excluded; no (H\) is shown regular in any (\operatorname{Hol}(M)\); no pair is lifted through (M\trianglelefteq N\); no group (N\) of order 2016 is classified; and Kourovka 21.31 is neither proved nor disproved.

The SmallGroups result classifies isomorphism-type pairs satisfying one necessary quotient condition. It does not classify embeddings or extension data.

## What would upgrade it

Construct and completely check a concrete regular embedding giving a counterexample, or prove that every one of the nine necessary pairs cannot occur in the full Byott lift and that all remaining orders are covered by a complete argument. Either route must operate in, or be proved equivalent to, the actual holomorph target.
