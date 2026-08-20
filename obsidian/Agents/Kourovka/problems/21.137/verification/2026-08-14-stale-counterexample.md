---
title: "Verification — Kourovka 21.137 — stale counterexample"
problem: 21.137
claim: "The April 2026 Lean artifact gives an exact counterexample to the exponent-8 clause of Kourovka 21.137."
claimant: Problem-21.137
target_object: "finite 2-groups of exponent 8 whose squares form a subgroup"
witness_object: "the swap wreath product W=(D8 x D8) semidirect C2"
witness_equals_target: proven-with-citation
citation: "Elias Judin / Aristotle (Harmonic), 21_137.lean, immutable revision e48497e41a6838c4fedf6153c1e6986bd14ada2b, created 2026-04-14"
verification_method: "rendered-source comparison; two independent complete finite models; elementary proof"
tools_used: ["GAP 4.12.1", "Python 3.12.3", "pdftotext 24.02.0", "web retrieval"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/replicated]
---

# Verification — Kourovka 21.137

## The claim

The public file [`21_137.lean`](https://gist.github.com/eliasjudin/3e74b54004d82cb86651a14ecf082463), created 14 April 2026, defines \(W=(D_8\times D_8)\rtimes_{\rm swap}C_2\) and supplies an exact negative instance of the even-prime clause of Problem 21.137.

## Target vs witness

The configured Notebook PDF, rendered and visually checked at page 184, asks:

> For a 2-group of exponent 8, if the squares form a subgroup, must that subgroup be abelian?

The artifact's `DihedralGroup 4` has order 8 by its cited Mathlib cardinality theorem. Its `WreathD4` is transported from `(DihedralGroup 4 × DihedralGroup 4) semidirect ZMod 2`, with the nonzero element swapping the factors. This is the ordinary regular wreath product \(D_8\wr C_2\), exactly the independently checked witness—not a quotient or an object built by assuming the desired properties.

Thus the witness belongs to the class quantified over by the source statement. It violates the proposed conclusion.

## Sub-claims and what each method proves

| Subclaim | Evidence | Result |
|---|---|---|
| Exact source and convention | Visual PDF inspection plus artifact definitions | Exact match to the exponent-8 clause; Mathlib's parameter 4 denotes the order-8 dihedral group |
| Finite 2-group | Both independent finite models | Order \(128=2^7\) |
| Exponent exactly 8 | Exhaustive checks and an explicit order-8 element | Passed |
| Squares form a subgroup | Exhaustive all-pair closure, identity and inverse checks; elementary kernel proof | Passed |
| Squares are nonabelian | Explicit noncommuting square witnesses in both models | Passed |
| Artifact itself compiles | Lean was probed but is absent | Not checked locally |

## Evidence

### Source extraction

```text
$ source _meta/agents/Kourovka/paths.env
$ pdftotext -f 184 -l 184 -layout "$KOUROVKA_PDF" -
21.137. If the p-th powers in a finite p-group form a subgroup, must that subgroup
be powerful? That is, for p != 2, if the p-th powers in a p-group of exponent p^2 form a
subgroup, must that subgroup be abelian? For a 2-group of exponent 8, if the squares
form a subgroup, must that subgroup be abelian?
```

The rendered page was also inspected; the exponent is visibly \(p^2\), and the item has no answer marker or attached comment. PDF SHA-256:

```text
f5a56398ba38e398038500d7a159ea6dfb67c6e4caaa304bb238f86a62080ce2  _meta/sources/Kourovka/kourovka.pdf
```

### Artifact inspection

The immutable revision `e48497e41a6838c4fedf6153c1e6986bd14ada2b` contains:

- the swap action and semidirect model at rendered lines 276–380;
- cardinality 128 at lines 383–393;
- exponent dividing 8 and an element whose fourth power is nonidentity at lines 430–436;
- exhaustive square closure at lines 438–442;
- noncommuting square witnesses and the final negative theorem at lines 444–461.

`lean`, `lake`, and `elan` were not installed, so no local Lean replay is claimed.

### Independent GAP model

Script SHA-256:

```text
8830683d20f164c4e8494ae97a7ac25ff457e1b4b35508bb7e1993fbc02cc277  Agents/Kourovka/problems/21.137/verification/scratch/independent_wreath_counterexample.g
```

Command and complete output:

```text
$ timeout 30s gap -q Agents/Kourovka/problems/21.137/verification/scratch/independent_wreath_counterexample.g
GAP_VERSION=4.12.1
D_SIZE=8 C_SIZE=2 W_SIZE=128
W_EXPONENT=8 IS_2_GROUP=true PRIME_P=2
W_ID=[ 128, 928 ]
SQUARE_SET_SIZE=16 IDENTITY_IN=true MUL_CLOSED=true INV_CLOSED=true
SQUARE_GENERATED_GROUP_SIZE=
16 SQUARE_SUBGROUP_NONABELIAN=true S_EQUALS_SQUARE_SET=true
S_ID=[ 16, 11 ] S_STRUCTURE=C2 x D8
NONCOMMUTING_PAIR_FOUND=true
A_SQUARED=(2,4)(6,8)
B_SQUARED=(1,2)(3,4)(5,6)(7,8)
AB_SQUARES_COMMUTE=false
RUN_COMPLETE=true
EXIT_STATUS=0
```

### Independent tuple model

This second implementation uses tuples \(r^i s^j\) and directly implements the swap semidirect-product law; it does not call GAP's wreath-product constructor. Script SHA-256:

```text
1a3dc750f5aa1000629bcbc9f7541f28ce1ab3b61703d83cd0bf248df6858870  Agents/Kourovka/problems/21.137/verification/scratch/independent_tuple_model.py
```

Command and complete output:

```text
$ timeout 30s python3 Agents/Kourovka/problems/21.137/verification/scratch/independent_tuple_model.py
MODEL=D8_TUPLES_SEMIDIRECT_SWAP_C2
D_SIZE=8 W_SIZE=128
SQUARE_SET_SIZE=16 MUL_CLOSED=true
EXPONENT_DIVIDES_8=true
ORDER_8_WITNESS=((0, 0), (1, 0), 1)
ORDER_8_WITNESS_FOURTH=((2, 0), (2, 0), 0)
NONCOMMUTING_SQUARES=(((3, 0), (3, 0), 0), ((0, 1), (0, 1), 0))
RUN_COMPLETE=true
EXIT_STATUS=0
```

### Elementary cross-check

Write \(D_8=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\), \(D_8'=\langle r^2\rangle\), and let \(t\) swap the two factors of \(D_8^2\). Even-coset squares have the form \((a^2,b^2)\); odd-coset squares satisfy
\[
((a,b)t)^2=(ab,ba).
\]
Consequently every square lies in
\[
S=\{(x,y):xD_8'=yD_8'\},
\]
the kernel of \((x,y)\mapsto xD_8'(yD_8')^{-1}\). Conversely, pairs in the identity coset are componentwise squares. In each nonidentity coset of \(D_8'\), the two elements are conjugate; hence every remaining pair is \((ab,ba)) for suitable \(a,b\). Thus the square set is exactly the subgroup \(S\). The squares \((r,r)=((r,1)t)^2\) and \((s,s)=((s,1)t)^2\) do not commute. Every element has eighth power one, while \(((r,1)t)^4=(r^2,r^2)\ne1\), so the exponent is exactly 8.

## Verdict

`status/replicated` for the exact stale-match claim. The public artifact and two independent complete finite implementations agree, and the elementary calculation checks the logical bridge to the source statement. Mathematical work on 21.137 should stop as stale/already answered; only the human may apply `status/solved`.

## Why this verdict

All defining properties of the concrete finite witness were checked exhaustively in two separately implemented models. The object and exponent conventions match the source exactly, and no hypothesis was imposed by construction except the definition of the wreath product itself.

## What is NOT established

The public Lean file was not compiled locally because Lean is absent. This note does not assert peer review, publication in a journal, or an answer to the separate odd-prime clause. None of those limitations affects the exhibited negative answer to the overall universal question.

## What would upgrade it

A local replay under the artifact's pinned Lean/Mathlib environment would replicate that formal artifact specifically. A `status/proven` tag remains gated on the human seeing and accepting the written finite proof.
