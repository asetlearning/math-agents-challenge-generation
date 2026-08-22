---
title: "Nonstandard polynomials: algebraic properties and elementary equivalence"
authors: Alexei Myasnikov, Andrey Nikolaev
year: 2024
venue: arxiv
url: https://arxiv.org/abs/2409.14467
url_translated:
language: en
domain: math-logic
status: draft
methodology_type: theoretical
citation_count:
citation_count_date: 2026-08-22
key_concepts:
  - "[[Concepts/bi-interpretability]]"
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "arXiv preprint (math.LO primary, MSC 03H05/03B10/03B16/12L15), v1 submitted 2024-09-22, 45 pages, single version. Published as Myasnikov, A. & Nikolaev, A., Journal of Logical and Algebraic Methods in Programming 146 (2025), Article 101071 (27 pages). Citation count not verified at ingest — Semantic Scholar's API returned HTTP 429 (rate-limited) on all attempts; no count recorded rather than guessed. Eighth `#domain/math-logic` paper in the vault. The paper's introduction explicitly states 'following [16] such structures are termed rich' when defining richness via weak-second-order-logic equivalence — [16] is very likely `[[kharlampovich-myasnikov-sohrabi-2021]]` (same term, same WSOL-equivalence definition, and Myasnikov is a shared author), but the exact bibliography entry could not be confirmed from the fetched source, so the `cites`/`extends` frontmatter link is left unset pending confirmation rather than asserted."
author: brett-b
tags:
  - agent/research
  - user/brett-b
  - domain/math-logic
  - topic/bi-interpretability
  - topic/model-theory
  - topic/interpretability-theory
  - topic/elementary-equivalence
  - topic/second-order-logic
  - topic/non-standard-models
  - topic/polynomial-rings
  - paper
  - status/draft
---

# Nonstandard polynomials: algebraic properties and elementary equivalence

## Abstract

> "We solve the first-order classification problem for rings $R$ of polynomials $F[x_1, \ldots,x_n]$ and Laurent polynomials $F[x_1,x_1^{-1}, \ldots,x_n,x_n^{-1}]$ with coefficients in an infinite field $F$ or the ring of integers $\mathbb{Z}$, that is, we describe the algebraic structure of all rings $S$ that are first-order equivalent to $R$."

*(Verbatim abstract, arXiv:2409.14467v1.)*

## TL;DR

Solves the first-order classification problem for polynomial and Laurent-polynomial rings $F[x_1,\dots,x_n]$ over an infinite field or $\mathbb{Z}$, by proving such rings are regularly bi-interpretable with a **list superstructure** $\mathbb{S}(F,\mathbb{N})$ — a three-sorted structure over the base field/ring $F$, the set of all finite tuples from $F$, and standard arithmetic $\mathbb{N}$. This makes first-order logic over $R = F[x_1,\dots,x_n]$ exactly as expressive as *weak second-order logic* over $F$, i.e. these polynomial rings are **rich** in the sense of `[[kharlampovich-myasnikov-sohrabi-2021]]`. The classification (Corollary 4.2) collapses to a clean statement: $F[X] \equiv L[Y]$ iff $|X|=|Y|$ and $HF(F) \equiv HF(L)$ (equal number of variables, and the hereditary-finite-set superstructures over the coefficient fields are elementarily equivalent).

## Problem

Given a polynomial ring $R = F[x_1,\dots,x_n]$ or its Laurent variant over an infinite field $F$ (or $\mathbb{Z}$), which rings $S$ can be elementarily equivalent to $R$ without being isomorphic to it? The paper approaches this via the general regular-(bi-)interpretability machinery shared across the vault's Myasnikov-adjacent cluster, extending the "richness" program (bi-interpretability with a hereditary-finite/list superstructure, collapsing WSOL to first-order logic) from groups (Kharlampovich-Myasnikov-Sohrabi's classical matrix groups, free metabelian groups, etc.) to a new setting: polynomial rings, where the "second-order" objects that need first-order-definable access are finite tuples of ring elements (polynomial coefficients/exponent vectors) rather than group-theoretic finite subsets.

## Approach

1. **Interpretability foundations** (§2): defines regular interpretations, bi-interpretations, and — the paper's key technical refinement — **regularly invertible interpretations** (Definition 2.9). States the general transfer theorem (Theorem 2.5): $\tilde{\mathbb{A}} \equiv \mathbb{A}$ iff $\tilde{\mathbb{A}} \cong \Gamma(\tilde{\mathbb{B}}, \bar b)$ for some $\tilde{\mathbb{B}} \equiv \mathbb{B}$, given regular invertible bi-interpretability of $\mathbb{A}$ and $\mathbb{B}$.
2. **List superstructures and nonstandard tuples** (§3): defines the list superstructure $\mathbb{S}(\mathbb{A}, \mathbb{N})$ — a three-sorted structure with the base structure $\mathbb{A}$, the set of all finite tuples over $\mathbb{A}$, and standard arithmetic $\mathbb{N}$, with tuple-access and length functions — and develops the theory of non-standard models of arithmetic and non-standard tuples needed to work with them. Proposition 3.1 establishes absolute bi-interpretability of $\mathbb{S}(\mathbb{N},\mathbb{N})$ with $\mathbb{N}$ itself, the base case the polynomial-ring results build on.
3. **Main construction** (§§4-5): shows $F[x_1,\dots,x_n]$ and its Laurent variant are regularly bi-interpretable with the list superstructure $\mathbb{S}(F,\mathbb{N})$ — intuitively, a polynomial is coded as a finite tuple of (coefficient, exponent-vector) pairs, and the list superstructure gives first-order access to arbitrary finite tuples over $F$, exactly what's needed to talk about "the polynomial with these coefficients" without a WSOL-strength quantifier. From this, derives Tarski-style classification corollaries by relating $\mathbb{S}(F,\mathbb{N})$-equivalence back to the more familiar hereditary-finite-superstructure equivalence $HF(F) \equiv HF(L)$ used elsewhere in the richness literature.

## Key result

- **Theorem 4.1** (headline bi-interpretability result): $F[x_1,\dots,x_n]$ and $F[x_1,x_1^{-1},\dots,x_n,x_n^{-1}]$ are regularly bi-interpretable with the list superstructure $\mathbb{S}(F,\mathbb{N})$.
- **Corollary 4.2** (classification, the paper's cleanest statement): for fields $F$, $L$ and finite variable sets $X$, $Y$: $F[X] \equiv L[Y]$ iff $|X| = |Y|$ and $HF(F) \equiv HF(L)$ — elementary equivalence of the polynomial rings reduces exactly to equal variable count plus WSOL-equivalence of the coefficient fields.
- **Corollary 4.3 / 4.4**: when $F$ is itself bi-interpretable with $\mathbb{N}$ (e.g. $\mathbb{Q}$, finitely generated algebraic extensions), the polynomial ring $F[x_1,\dots,x_n]$ is bi-interpretable with $\mathbb{N}$ directly — a sharper, parameter-free-flavored statement for this common case.
- **Richness identification** (Introduction, explicit): "following [16] such structures are termed *rich*" — the paper explicitly frames its main theorem as establishing richness (in the Kharlampovich-Myasnikov-Sohrabi sense) for polynomial and Laurent polynomial rings, since "the first-order logic in $R = F[x_1,\dots,x_n]$... is equivalent to the weak second-order logic in $F$."

## Assumptions

- $F$ is an infinite field, or $F = \mathbb{Z}$; no characteristic restriction stated for the general theorems (characteristic 0 is invoked specifically when the paper discusses Denef's undecidability results as context, not as a blanket assumption).
- Finitely many variables $n$ throughout.
- The list-superstructure machinery presumes standard arithmetic $\mathbb{N}$ as the third sort — the construction is calibrated to finite-tuple/finite-length objects, matching WSOL rather than full second-order logic.

## Limitations / scope

- An explicit open question is flagged (Remark 1, Introduction): when not every $F' \equiv F$ can be realized as some $F_{\mathcal{M}}$ (for $\mathcal{M} \equiv \mathbb{S}(F,\mathbb{N})$), the paper asks "it is an interesting question what this logic is" — i.e. characterizing the exact logical strength governing which field-equivalence classes arise, left open in general.
- The clean classification (Corollary 4.2 and its refinements) is worked out concretely for specific field classes — $\mathbb{Q}$, algebraically closed fields of finite transcendence degree, pure transcendental extensions, algebraic real numbers — with the fully general case (arbitrary infinite $F$) not claimed to be as explicitly resolved.
- Purely theoretical; no results specific to Burnside groups or this vault's B(2,5) program, though the richness/WSOL machinery is the same general-purpose tool used elsewhere in the vault's model-theory cluster.

## Replication evidence

N/A — a theoretical model-theory/ring-theory paper with full proofs. Published in peer-reviewed form (Journal of Logical and Algebraic Methods in Programming, 2025) alongside the arXiv preprint; no independent replication surfaced at ingest.

## Why this paper matters

This paper extends the richness program from groups — where `[[kharlampovich-myasnikov-sohrabi-2021]]` established $\text{SL}_n(\mathbb{Z})$, free metabelian groups, and free group algebras as rich, and hyperbolic/nilpotent groups as not — to a genuinely different algebraic setting: polynomial and Laurent polynomial rings. The list-superstructure device ($\mathbb{S}(F,\mathbb{N})$, three-sorted with a tuple sort) is a clean, reusable technical tool for exactly the situation where "second-order-strength" objects are finite tuples (polynomial coefficient lists) rather than arbitrary finite subsets — worth comparing against the hereditary-finite-set superstructure $HF(G)$ used in the group setting, since both serve the same richness-establishing role via structurally different constructions. Corollary 4.2's clean reduction — elementary equivalence of the polynomial rings reduces to equal variable count plus $HF(F) \equiv HF(L)$ for the coefficient fields — is a genuinely satisfying classification, in the same spirit as the vault's other bi-interpretability-driven classification results (`[[sohrabi-myasnikov-2020]]`, `[[myasnikov-sohrabi-2024]]`, `[[daniyarova-myasnikov-2024]]`) but for a commutative-ring rather than a (semi)linear-group setting.

## Quotes

1. > "We solve the first-order classification problem for rings $R$ of polynomials $F[x_1, \ldots,x_n]$..." — Abstract
2. > "Following [16] such structures are termed *rich*." — Introduction (per source extraction)

## Open questions surfaced

- **Remark 1** (verbatim per extraction): "It is an interesting question what this logic is" — referring to the precise logical strength governing which fields $F' \equiv F$ can be realized as $F_{\mathcal{M}}$ for some $\mathcal{M} \equiv \mathbb{S}(F,\mathbb{N})$, when not all of them can — left open in general.
- Whether the full general-$F$ case of the classification (beyond the specific field classes worked out: $\mathbb{Q}$, algebraically closed of finite transcendence degree, pure transcendental extensions, algebraic reals) admits the same clean treatment, or requires genuinely new ideas.
- Whether reference [16] (cited for the term "rich") is confirmed to be `[[kharlampovich-myasnikov-sohrabi-2021]]` — plausible given identical terminology and a shared author, but not confirmed from the fetched source; worth verifying on a closer read before treating the connection as a citation rather than a topical parallel.

## Related material in vault

- Extends: (none in vault — plausibly extends `[[kharlampovich-myasnikov-sohrabi-2021]]`'s richness program to polynomial rings, but the citation link could not be confirmed; see Open questions)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: `[[Concepts/bi-interpretability]]` — eighth paper in the vault to substantively engage with bi-interpretability; introduces the **list superstructure** $\mathbb{S}(\mathbb{A},\mathbb{N})$ as a new richness-establishing construction, parallel to but distinct from the hereditary-finite-set superstructure $HF(G)$ used for groups.
- Cites: (none confirmed as in-vault papers; the likely reference to `[[kharlampovich-myasnikov-sohrabi-2021]]`'s richness terminology is not confirmed — see `quality_notes`)
- Cited by (in vault): (none)
- Sibling math-logic notes: `[[kharlampovich-myasnikov-sohrabi-2021]]` — shares author Myasnikov and the "richness" terminology/definition (bi-interpretability with a superstructure that collapses WSOL to first-order logic), applied here to a ring rather than group setting; `[[sohrabi-myasnikov-2020]]`, `[[myasnikov-sohrabi-2024]]`, `[[daniyarova-myasnikov-2024]]` — the vault's other elementary-equivalence-classification-via-bi-interpretability results, for classical linear groups and the Baumslag-Solitar group respectively, all sharing Myasnikov as an author and the same general regular-(bi-)interpretability toolkit from `[[daniyarova-myasnikov-2025]]`.

---

## Notation conventions

Ring/logic notation in this note ($F[x_1,\dots,x_n]$, $\mathbb{S}(F,\mathbb{N})$, $HF(F)$) is rendered in LaTeX inline math and plain Unicode prose; no `[[...]]`-style double-bracket expressions requiring backtick-escaping appear, per `[[paper-summary]]` § Notation conventions.
