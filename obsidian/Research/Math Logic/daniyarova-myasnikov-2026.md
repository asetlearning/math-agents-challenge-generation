---
title: "Theory of Interpretations II. Categorical equivalence of projective logical geometries"
authors: Evelina Daniyarova, Alexei Myasnikov
year: 2026
venue: arxiv
url: https://arxiv.org/abs/2607.23261
url_translated:
language: en
domain: math-logic
status: draft
methodology_type: theoretical
citation_count:
citation_count_date: 2026-08-15
key_concepts:
  - "[[Concepts/bi-interpretability]]"
extends:
  - "[[daniyarova-myasnikov-2025]]"
contradicts: []
replicates: []
cites:
  - "[[daniyarova-myasnikov-2025]]"
cited_by: []
quality_notes: "arXiv preprint (math.LO primary, math.CT secondary), submitted 2026-07-25 — under a month old at ingest, no citation count yet available/meaningful. Second paper in the planned Daniyarova-Myasnikov interpretation-theory series; builds directly on `[[daniyarova-myasnikov-2025]]` (Paper I). Written in memory of Boris I. Plotkin, whose universal-algebraic-geometry and logical-geometry program this paper extends categorically."
author: brett-b
tags:
  - agent/research
  - user/brett-b
  - domain/math-logic
  - topic/model-theory
  - topic/interpretability-theory
  - topic/bi-interpretability
  - topic/definability
  - topic/category-theory
  - topic/logical-geometry
  - topic/elimination-of-imaginaries
  - topic/first-order-classification
  - topic/diophantine-problems
  - paper
  - status/draft
---

# Theory of Interpretations II. Categorical equivalence of projective logical geometries

## Abstract

> "We introduce projective logical geometry and prove that two algebraic structures are strongly bi-interpretable if and only if their categories of projective logical sets are equivalent relative to the class of interpretation functors, which is also equivalent to their categories of projective definable sets being equivalent relative to the class of translation functors."

*(Verbatim abstract, arXiv:2607.23261v1.)*

## TL;DR

The second installment in the Daniyarova–Myasnikov interpretation-theory series, and a direct sequel to `[[daniyarova-myasnikov-2025]]`. Where Paper I built up interpretability from explicit interpretation codes, Paper II reframes the strongest form — strong bi-interpretability — as a purely categorical statement: it holds iff the two structures' categories of *projective logical sets* (a construction that adds "imaginary elements" to Plotkin's logical sets, echoing the affine-to-projective-variety passage in classical algebraic geometry) are equivalent. The paper is explicitly framed as extending Boris Plotkin's universal-algebraic-geometry and logical-geometry program into a categorical, model-theoretic setting, and is dedicated to his memory.

## Problem

Plotkin's original question — "when do two algebraic structures share the same logical geometry?" — was answered categorically for weaker equivalence notions (geometric equivalence ↔ isomorphic categories of algebraic sets, Theorem 4; logical equivalence ↔ isomorphic categories of absolute logical sets, Theorem 5), both due to Plotkin. This paper asks the analogous question for the strongest and most useful notion in the series' terminology, **strong bi-interpretability**: is there a purely categorical criterion for it, expressed as an equivalence (not isomorphism) of categories associated to each structure, and incorporating "imaginary" definable objects the way projective varieties incorporate points at infinity?

## Approach

Categorical, building directly on Paper I's interpretation-code apparatus (Definitions 1–7 recapped/extended, §1–2):

1. Extend interpretation codes with an explicit embedding component (**Definition 2**, "extended code": a triple (Γ, p̄, γ) pairing an interpretation code Γ with a parameter tuple p̄ and a map γ: A → Bⁿ), then establish transfer machinery for these codes: the **Reduction Theorem** (Theorem 1), the **Extended Reduction Theorem** (Theorem 2, adding elementary embeddings ι: 𝔸 → Ã, κ: 𝔹 → B̃), and the **Inverse Reduction Theorem** (Theorem 3, recovering an elementary embedding 𝔸 → Γ(𝔹, p̄) from an extended code satisfying condition (IRT)).
2. Define **projective logical sets** (**Definition 6**): the quotient X/∼X of a logical set X by a formula-induced equivalence relation ∼X (**Definition 5**), explicitly analogized to passing from affine to projective varieties in classical algebraic geometry, to incorporate imaginary elements.
3. Build the categories 𝒫ℒ𝒮(𝔸) (projective logical sets of 𝔸) and 𝒫𝒟𝒮(𝔸) (projective definable sets of 𝔸), with **interpretation functors** and **translation functors** between such categories for different structures.
4. Prove the two main categorical-equivalence theorems (§3–4, see Key result).
5. Assemble everything into a top-level 2-categorical statement (**Theorem 17**) relating the 2-category of all algebraic structures-with-interpretations to the 2-category of all projective logical geometries.
6. Recap Plotkin's two precedent theorems for weaker equivalence notions (**Theorem 4**, geometric equivalence ↔ isomorphic categories of algebraic sets; **Theorem 5**, logical equivalence ↔ isomorphic categories of absolute logical sets) as the template this paper's Theorem 13 generalizes to bi-interpretability and to categorical *equivalence* (a weaker, more flexible relation than isomorphism).

## Key result

- **Theorem 9** (interpretation functors, §3): 𝔸 is interpretable in 𝔹 iff there exists an interpretation functor 𝒫ℒ𝒮(𝔸) → 𝒫ℒ𝒮(𝔹).
- **Theorem 13** (the paper's headline result, §4): 𝔸 and 𝔹 are strongly bi-interpretable iff 𝒫ℒ𝒮(𝔸) and 𝒫ℒ𝒮(𝔹) are equivalent relative to interpretation functors — equivalently, iff 𝒫𝒟𝒮(𝔸) and 𝒫𝒟𝒮(𝔹) (the categories of projective *definable* sets) are equivalent relative to translation functors. This is the categorical answer to Plotkin's question for the bi-interpretability level of the interpretability hierarchy.
- **Theorem 17** (2-categorical capstone): the 2-category 𝐀𝐒 of all algebraic structures with interpretations between them is isomorphic, as a 2-category, to the 2-category 𝐏𝐋𝐆 of all projective logical geometries.
- Recapped precedent results, both attributed to Plotkin and used as the template Theorem 13 generalizes: **Theorem 4** (geometrically equivalent structures ⟹ isomorphic categories of algebraic sets) and **Theorem 5** (logically equivalent structures ⟹ isomorphic categories of absolute logical sets).

## Assumptions

- Inherits Paper I's setting wholesale: classical (non-fuzzy/continuous) first-order logic, algebraic structures over a fixed relational/functional language, and the interpretation-code apparatus (interpretability with/without parameters, dimension, code composition).
- The categorical machinery assumes familiarity with basic category theory: functors, natural transformations, equivalence vs. isomorphism of categories, 2-categories.
- As in Paper I, worked intuition is drawn mostly from algebra (the affine-vs-projective-variety analogy is explicitly borrowed from classical algebraic geometry to motivate the "logical" vs "projective logical" set distinction), though the general theory is stated for arbitrary algebraic structures.

## Limitations / scope

- Explicitly does not treat interpretations **between elementary theories** (as opposed to between structures) — the paper notes non-equivalence between the structure-level and theory-level notions and defers a unifying framework, stating this "is covered in a later article in this series."
- Omits standard universal-algebraic-geometry constructs such as the category of coordinate algebras of algebraic sets, deferring comprehensive treatment to future installments.
- Purely theoretical/definitional-categorical; no computational, algorithmic, or complexity-theoretic content, and (like Paper I) no results specific to Burnside groups, Knuth–Bendix rewriting, or this vault's B(2,5) program.

## Replication evidence

N/A — a theoretical model-theory/category-theory paper proving structural theorems, not an empirical or computational result subject to replication.

## Why this paper matters

This paper does for **bi-interpretability** what Plotkin had already done for the weaker notions of geometric and logical equivalence: gives it a purely categorical face. That matters because categorical equivalence (unlike code-level interpretability, which requires exhibiting explicit definable maps) is a criterion that composes cleanly and is amenable to the general machinery of category theory (functor composition, natural isomorphism, 2-categorical coherence) — potentially making bi-interpretability arguments more portable across different pairs of structures than re-deriving them from Paper I's explicit-code apparatus each time. The paper is also notable as a deliberate act of mathematical memorial: it is framed throughout as extending Boris Plotkin's specific research program (universal algebraic geometry → logical geometry → this paper's projective logical geometry) and is dedicated to him on the reported occasion of a workshop marking the centenary of his birth. For readers of `[[daniyarova-myasnikov-2025]]`, this is the natural next paper — it doesn't just apply Paper I's definitions, it re-derives the deepest result of the pair (strong bi-interpretability) in a different, more structural idiom.

## Quotes

1. > "In memory of B. I. Plotkin, the founding father of logical geometry." — dedication
2. > "...we pass from the category of logical sets to the category of projective logical sets. This transition has model-theoretic underpinnings and reflects the need to incorporate imaginary elements." — §2

## Open questions surfaced

- The authors flag an explicit unification gap: "it would be interesting to develop a general framework that unifies" structure-level and theory-level interpretations, noting the two notions are not equivalent — stated as future work, with the theory-level treatment promised for "a later article in this series."
- Whether Theorem 13's categorical-equivalence criterion for strong bi-interpretability gives a more tractable *test* in practice than Paper I's explicit-code characterization, or whether the two are just different presentations of the same underlying difficulty — not addressed by either paper (see also `[[Concepts/bi-interpretability]]` § Open questions).
- The series is still incomplete: Paper III (or later) is explicitly forward-referenced for the interpretations-of-theories material; the full comparison between the code-level (Paper I) and categorical (Paper II) approaches to bi-interpretability remains to be drawn out explicitly by the authors or a future reader.

## Related material in vault

- Extends: [[daniyarova-myasnikov-2025]] — Paper I of this series; Paper II reuses its interpretation-code definitions and extends its bi-interpretability apparatus categorically.
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: [[Concepts/bi-interpretability]] — created at this paper's ingest, now that 2 papers ([[daniyarova-myasnikov-2025]] and this one) substantively engage with it.
- Cites: [[daniyarova-myasnikov-2025]]
- Cited by (in vault): (none)
- Sibling math-logic note: [[pakhomov-solda-2025-generalized-higman]] — the vault's third `#domain/math-logic` paper is this one; connection to the other two is field-level (order theory/reverse mathematics for Pakhomov–Soldà vs. model theory of interpretations here), not a direct citation link.

---

## Notation conventions

No bracket-nesting or commutator notation requiring backtick-escaping appears in this note; category-theoretic notation (𝒫ℒ𝒮, 𝒫𝒟𝒮, functor arrows) is rendered as plain Unicode/prose rather than LaTeX double-bracket forms, per `[[paper-summary]]` § Notation conventions.
