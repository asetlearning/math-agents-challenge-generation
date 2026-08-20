---
title: "Verification triage — Kourovka 21.137 — stale counterexample"
problem: 21.137
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Claim

The public Lean artifact `21_137.lean` exhibits the regular wreath product
\(D_8\wr C_2=(D_8\times D_8)\rtimes C_2\) as a finite 2-group of exponent exactly 8 whose set of squares is a nonabelian subgroup, giving an already-existing negative answer to Kourovka 21.137.

# Target versus witness

- **Target:** PDF page 184 asks, in its even-prime clause, whether the squares of a finite 2-group of exponent 8 must be abelian when they form a subgroup.
- **Artifact witness:** the explicitly defined swap wreath product `WreathD4`, with Mathlib's `DihedralGroup 4` of order 8.
- **Independent witness:** the same abstract wreath product constructed independently in GAP.
- **Witness equals target:** this is a counterexample witness rather than a model of a fixed target object. It must be proved to be a finite 2-group, have exponent exactly 8, have its set of squares closed, and have two noncommuting squares. The notation convention `DihedralGroup 4` must be checked to mean order 8.

# Subclaims

1. The rendered source statement has been transcribed without changing quantifiers or exponent conventions.
2. The artifact defines \(D_8\wr C_2\), not a quotient or an assumed object.
3. The group is finite of order \(128=2^7\).
4. Its exponent is exactly 8.
5. Its set of squares is closed under multiplication and hence is a subgroup.
6. Two actual squares fail to commute.
7. Therefore the artifact exactly answers the even-prime clause negatively and predates this assignment.

# Tools available

- GAP 4.12.1: available.
- Python 3.12.3: available.
- Lean/Lake: not yet observed and must be probed before citing a local replay.
- `pdftotext` 24.02.0 and `pdftoppm`: available; PDF page 184 rendered and visually checked.
- Sage and Magma: unavailable.

# Methods inventory

| Subclaim | Method | What a pass proves | What it does not prove |
|---|---|---|---|
| 1 | PDF text extraction plus rendered-page inspection | Exact source clause and notation | Truth of a proposed witness |
| 2 | Read definitions and action in the public Lean source | Artifact object/provenance and swap convention | That Lean compiled locally |
| 3–6 | New GAP script, exhaustive over all 128 elements and all products of squares | Complete finite verification for an independently constructed isomorphic wreath product | Reproducibility of the Lean environment itself |
| 7 | Direct logical matching | The verified witness negates the exact universal clause | Publication or peer-review status |

# Hard limits and recommendation

If Lean is absent, do not reimplement it; record that the public file was inspected but not locally compiled. GAP can still give a complete independent finite check of the counterexample. Recommendation: full finite verification and exact stale-match review.
