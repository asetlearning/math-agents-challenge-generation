---
title: "Verification — Kourovka 21.31 — counterexample preprint stale match"
problem: 21.31
claim: "arXiv:2607.22795v1 claims a counterexample in exactly the holomorph direction asked by Kourovka 21.31."
claimant: Lead
target_object: "regular subgroups of the holomorph of a finite soluble group"
witness_object: "the paper's map from its insoluble group G into Hol(N), where its additive group N is finite and soluble"
witness_equals_target: proven-with-citation
citation: "Di Matteo–Ferrara–Trombetti, A Counterexample to Byott's Conjecture for Finite Skew Braces, arXiv:2607.22795v1, submitted 2026-07-24, Proposition 2.7 and Theorem 2.8"
verification_method: "source/PDF exact-match comparison and left-holomorph convention audit"
tools_used: ["web retrieval", "pdftotext 24.02.0", "Python 3.12.3"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/replicated]
---

# Verification — Kourovka 21.31

## The claim

The 15-page preprint by Massimiliano Di Matteo, Maria Ferrara, and Marco Trombetti, [`arXiv:2607.22795v1`](https://arxiv.org/abs/2607.22795), is an exact post-Notebook counterexample claim for Problem 21.31, not a result about the converse obtained by swapping the two brace groups.

This verdict certifies the **bibliographic and convention match**. It does not certify every coordinate identity in the construction.

## Target vs witness

Rendered Notebook page 169 states:

> If \(N\) is a finite soluble group, then any regular subgroup in the holomorph \(\operatorname{Hol}(N)\) of \(N\) is also soluble.

The paper uses the same left holomorph \(\operatorname{Hol}(N)=N\rtimes\operatorname{Aut}(N)\) and the same definition of regularity (free and transitive). Its additive group is the ambient group \(N\); its multiplicative/source group is \(G\). The final map is
\[
x\longmapsto (b(x),\lambda_x)\in\operatorname{Hol}(N).
\]
The paper asserts and proves in Proposition 2.7 that \(b:G\to N\) is bijective and
\[
b(xy)=b(x)+\lambda_x(b(y)).
\]
For the standard product \((n,\alpha)(m,\beta)=(n+\alpha(m),\alpha\beta)\), this is exactly the homomorphism condition. Bijectivity makes the orbit of zero all of \(N\), and equal finite cardinalities make the action regular. The ambient \(N\) is soluble, while \(G/H\cong\operatorname{PSL}_2(7)\), so \(G\) is insoluble.

The witness therefore has the exact target orientation. The use of \(N=N_0^{\mathrm{op}}\) reverses the preliminary group law solely to obtain the displayed left-cocycle identity; inversion identifies \(N_0\) with its opposite and preserves solubility. It does not exchange the ambient and embedded groups.

## Sub-claims and what each method proves

| Subclaim | Paper location and check | What the pass proves |
|---|---|---|
| Exact source | Notebook PDF p.169, rendered and visually checked | Correct target and quantifiers |
| Finite soluble ambient group | Printed pp.8–10, equations (17)–(24) | The paper's \(N_0=P\rtimes(W\rtimes E)\) has an abelian-factor normal series; the opposite group remains soluble |
| Insoluble source group | Printed pp.11–12, equations (34)–(36) | \(G=H\rtimes L\) has quotient \(L\cong\operatorname{PSL}_2(7)\) |
| Equal orders and bijective cocycle | Proposition 2.7, printed p.12 | The proposed map has the correct finite size and cocycle identity |
| Correct holomorph direction and regularity | Theorem 2.8 and final paragraph, printed pp.12–13 | The claim is exactly a regular insoluble subgroup of the holomorph of soluble \(N\) |
| Full construction correctness | Proof read through the final map, but coordinate Tables 1–2 were not independently reproduced in full | Not certified by this stale-match review |

## Evidence

### Source

```text
$ source _meta/agents/Kourovka/paths.env
$ pdftotext -f 169 -l 169 -layout "$KOUROVKA_PDF" -
21.31. Conjecture: If N is a finite soluble group, then any regular subgroup in the
holomorph Hol(N) of N is also soluble.                                    N. Byott
```

The page was rendered and inspected visually. PDF SHA-256:

```text
f5a56398ba38e398038500d7a159ea6dfb67c6e4caaa304bb238f86a62080ce2  _meta/sources/Kourovka/kourovka.pdf
```

### Primary preprint

The [arXiv record](https://arxiv.org/abs/2607.22795) reports v1 submitted 24 July 2026, 15 pages. The primary PDF gives:

- printed p.1: the same conjecture, \(\operatorname{Hol}(N)=N\rtimes\operatorname{Aut}(N)\), regular meaning free and transitive, and the bijective-cocycle equivalence;
- printed p.2: Main Theorem—finite skew brace with soluble additive group and insoluble multiplicative group;
- printed p.8, equation (20): \(|N_0|=7^8 3^7 2^3=100860958296\), with an abelian-factor normal series;
- printed pp.9–10, equations (24)–(28): \(N=N_0^{\mathrm{op}}\) and the orientation-corrected maps \(\lambda_g\);
- printed pp.11–12, equations (33)–(39), Proposition 2.7: disjoint cosets, \(G=H\rtimes L\), \(|G|=|N|\), \(G/H\cong\operatorname{PSL}_2(7)\), and the bijective cocycle;
- printed pp.12–13, Theorem 2.8 and the final paragraph: the explicit homomorphism into \(\operatorname{Hol}(N)\) is injective and regular.

### Arithmetic check

```text
$ python3 - <<'PY'
print('N_ORDER=', 7**8 * 3**7 * 2**3, sep='')
print('H_ORDER=', 7**7 * 3**6, sep='')
print('H_TIMES_168=', 7**7 * 3**6 * 168, sep='')
print('ORDERS_EQUAL=', 7**8 * 3**7 * 2**3 == 7**7 * 3**6 * 168, sep='')
PY
N_ORDER=100860958296
H_ORDER=600362847
H_TIMES_168=100860958296
ORDERS_EQUAL=True
```

### Convention calculation

Under the paper's standard left action, \((b(x),\lambda_x)\) sends \(0\) to \(b(x)\). Proposition 2.7 gives
\[
(b(x),\lambda_x)(b(y),\lambda_y)
=(b(x)+\lambda_x(b(y)),\lambda_x\lambda_y)
=(b(xy),\lambda_{xy}).
\]
Thus the image is a subgroup; bijectivity of \(b\) gives a sharply transitive orbit. This is the Notebook's direction. The converse would instead put the insoluble group in the ambient/additive slot, which the paper does not do.

## Verdict

`status/replicated` for the exact stale-match claim. Problem 21.31 should be treated as stale for scheduling, and the internal order-2016 search should stop unless Lead explicitly repurposes it as independent verification of the preprint. Only the human may apply `status/solved`.

## Why this verdict

The Notebook statement, the preprint's opening formulation, Proposition 2.7, Theorem 2.8, and the final holomorph map agree exactly on ambient group, embedded group, action side, regularity, and solubility direction. The opposite-group step removes rather than creates the possible convention reversal.

## What is NOT established

This note does not independently reproduce every matrix entry in Table 1, every exponent in Table 2, or the full coordinate construction of \(b\). It therefore does not assign `status/proven` to the paper's mathematical Main Theorem. It also does not assert peer review or later-version stability.

## What would upgrade it

Independently reproduce all bounded matrix and function identities underlying Lemmas 2.1–2.6 and Proposition 2.7, or complete a line-by-line proof audit with every table entry checked. The human must see such an audit before a `status/proven` treatment.
