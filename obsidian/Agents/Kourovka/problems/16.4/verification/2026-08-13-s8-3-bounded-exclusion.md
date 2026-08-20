---
title: "Verification — Kourovka 16.4 — S8(3) bounded exclusion"
problem: "16.4"
claim: "In the finite simple group PSp_8(3), no product of two nonidentity conjugacy classes is one conjugacy class."
claimant: Problem-16.4
target_object: "For the bounded claim, PSp_8(3); Kourovka 16.4 itself quantifies over arbitrary finite nonabelian simple groups."
witness_object: "The ordinary character table CharacterTable(\"S8(3)\") in GAP CTblLib 1.3.7."
witness_equals_target: proven-with-citation
citation: "CTblLib uses Atlas notation S_d(q)=PSp(d,q); the ATLAS S8(3) page gives the matching order 65784756654489600."
verification_method: "Independent exhaustive GAP 4.12.1 exact character-column enumeration"
tools_used: ["GAP 4.12.1", "CTblLib 1.3.7", "pdftotext 24.02.0"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/conjugacy-classes, project/kourovka, status/replicated]
---

# Verification — Kourovka 16.4

## The claim

In the specific finite simple group (PSp_8(3)), no ordered pair of nonidentity conjugacy classes has a product equal to one conjugacy class.

This is a bounded group-specific statement, not a solution of Kourovka 16.4.

## Target vs witness

The configured source PDF, page 95, states:

> **16.4.** Let (G) be a finite group with (C,D) two nontrivial conjugacy classes such that (CD) is also a conjugacy class. Can (G) be a non-abelian simple group? — Z. Arad

The bounded target is (PSp_8(3)). The witness is CTblLib 1.3.7's ordinary character table with identifier `S8(3)`. CTblLib's documented Atlas notation says `S_d(q)` denotes `PSp(d,q)`: <https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/doc2/chap11.html>. The ATLAS page identifies the symplectic group `S8(3)` and gives order 65,784,756,654,489,600, exactly matching the table: <https://brauer.maths.qmul.ac.uk/Atlas/clas/S83/>. The table also reports `IsSimple=true`. Thus the table witness is identified with the bounded target, not with a cover or automorphism group.

It is not equal to the universal target class of all finite nonabelian simple groups. No family-wide or universal conclusion follows.

## Sub-claims and what each method proves

1. Source statement: checked directly in the configured PDF.
2. Witness identity: checked from CTblLib's documented notation, exact identifier and order, and the independent ATLAS entry.
3. Class indexing: the table has 278 classes; class 1 is the unique class of element order 1 and has size 1. Hence indices 2–278 are exactly the 277 nonidentity classes.
4. Necessary identity: if (K_iK_j=K_k), then every pair (x\in K_i,y\in K_j) has (xy\in K_k). For a representation affording an irreducible character \(\chi\), averaging the matrices over each class and applying Schur's lemma gives
   \[
   \frac{\chi(g_i)}{\chi(1)}I\;\frac{\chi(g_j)}{\chi(1)}I
   =\frac{\chi(g_k)}{\chi(1)}I,
   \]
   hence \(\chi(g_i)\chi(g_j)=\chi(1)\chi(g_k)\). This is necessary, not sufficient.
5. Pair counting/divisibility: conjugation acts transitively on (K_k), so the number of factorizations of each element of (K_k) is constant; therefore (|K_k|\mid |K_i||K_j|). This necessary filter does not assume the Szep reduction or strict class-size lemma.
6. Exhaustion: an independently written script tested all (277^2=76{,}729) ordered input pairs, all 278 output indices subject only to the elementary divisibility condition, and exact cyclotomic character equality. No compatible triple survived.
7. Circularity: the CTblLib table, its character rows, class sizes, and element orders are external library data not constructed from the desired exclusion. The predicate tested is derived independently from the assumption of a singleton product.

## Evidence

Source command and relevant output:

```text
source _meta/agents/Kourovka/paths.env
pdftotext -f 95 -l 95 -layout "$KOUROVKA_PDF" -

16.4. Let G be a finite group with C, D two nontrivial conjugacy classes such that
CD is also a conjugacy class. Can G be a non-abelian simple group?         Z. Arad
```

Independent computation command:

```text
timeout 55s gap -q Agents/Kourovka/problems/16.4/verification/scratch/independent_s8_3_columns.g > Agents/Kourovka/problems/16.4/verification/scratch/independent_s8_3_columns.out 2>&1
```

Verbatim output:

```text
GAP_VERSION=4.12.1
CTBLLIB_VERSION=1.3.7
TABLE_IDENTIFIER=S8(3)
TABLE_SIZE=65784756654489600
TABLE_IS_SIMPLE=true
NUMBER_CLASSES=278
NUMBER_IRREDUCIBLES=278
IDENTITY_INDEX_DATA=size:1,order:1,number_order_one:1
ORDERED_NONIDENTITY_PAIRS=76729
DIVISIBLE_CANDIDATE_TRIPLES=20167957
EXACT_CHARACTER_COMPARISONS=41049934
COMPATIBLE_TRIPLES=[  ]
FINAL_COMPATIBLE_COUNT=0
```

Process result and artifact hashes:

```text
RUN_EXIT=0
1de8b2012ffc0de6d41888a62a9a6b3f7026924533ecb3a35b36d913a31c9854  Agents/Kourovka/problems/16.4/verification/scratch/independent_s8_3_columns.g
288b3ad4a37f5ffc787dfe11a93f48cdf2b854f1902fa3fac682ec88dc1f65da  Agents/Kourovka/problems/16.4/verification/scratch/independent_s8_3_columns.out
```

This run is structurally independent of the claimant's script: it does not read it, does not use its strict-size filter, does not use the multiplicity-one/Szep filter, and does not call class multiplication coefficients. The claimant's separate run also exited 0 with 76,729 rejected pairs and zero compatible pairs. The two computations agree.

## Verdict

`status/replicated`

## Why this verdict

There are multiple agreeing computations, including a newly written independent exhaustive computation. The independent run checks a necessary condition for every possible singleton class product and finds none, which excludes such a product in the named table. The witness is identified with (PSp_8(3)).

The threshold remains `replicated`, following the program's rule for concrete finite character-table computations. It is not promoted to `proven`.

## What is NOT established

- Kourovka 16.4 is not solved.
- No assertion is established for (PSp_8(q)) with (q\ne3), for any other family, or for arbitrary finite simple groups.
- The character table was not reconstructed independently from an explicit presentation or representation; the verification relies on CTblLib's table data and identification.
- The Szep multiplicity-one reduction and strict-size lemma are not needed by this verification and receive no verdict here.

## What would upgrade it

For this bounded finite statement, a complete hand-checkable certificate derived from an explicit model of (PSp_8(3)), or an independently reconstructed character table with proof of identification, would reduce reliance on CTblLib. A universal upgrade would require a separate gap-free proof covering every finite nonabelian simple group and human review; this computation cannot supply it.
