---
title: Bi-interpretability
author: brett-b
language: en
tags:
  - agent/research
  - user/brett-b
  - domain/math-logic
  - topic/bi-interpretability
  - topic/interpretability-theory
  - topic/model-theory
  - concept
  - status/draft
introduced_in:
  - "[[daniyarova-myasnikov-2025]]"
related_concepts: []
appears_in:
  - "[[daniyarova-myasnikov-2025]]"
  - "[[daniyarova-myasnikov-2026]]"
  - "[[darienzo-pagano-mcinnis-2020]]"
---

# Bi-interpretability

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

Two algebraic structures 𝔸 and 𝔹 are **bi-interpretable** when each is interpretable in the other *and* the two composite interpretations (𝔸 → 𝔹 → 𝔸, and 𝔹 → 𝔸 → 𝔹) are themselves definable isomorphisms back to the original structure — i.e. interpretability is not just mutual but coherently invertible. `[[daniyarova-myasnikov-2025]]` (Paper I) formalizes several strengths of this notion for interpretations-with-parameters, notably **regular bi-interpretability**, built on its regular-interpretability definition (Definition 7, §2.5): a bi-interpretation is regular when both directions' interpretation codes work uniformly across a definable, nonempty set of parameter choices rather than one fixed tuple. `[[daniyarova-myasnikov-2026]]` (Paper II) gives a categorical characterization of the *strong* variant: **Theorem 13** — 𝔸 and 𝔹 are strongly bi-interpretable iff their categories of projective logical sets (𝒫ℒ𝒮(𝔸), 𝒫ℒ𝒮(𝔹)) are equivalent relative to interpretation functors, equivalently iff their categories of projective definable sets (𝒫𝒟𝒮(𝔸), 𝒫𝒟𝒮(𝔹)) are equivalent relative to translation functors.

## Why it matters

Bi-interpretability is the model-theoretic tool for showing two structures are, for logical purposes, "the same" without being isomorphic: it transfers decidability/undecidability, elementary-equivalence classification, and (per the Khélif–Nies connection cited in Paper I) the QFA (quasi-finitely-axiomatizable) property. The Daniyarova–Myasnikov papers approach it from opposite ends — Paper I builds the notion up from explicit interpretation codes and parameter descriptors with worked algebraic examples (Baumslag–Solitar groups, unitriangular matrix groups); Paper II reformulates the strong variant purely categorically, replacing an explicit-code characterization with an equivalence-of-categories criterion (equivalence of categories of *projective logical sets*, built on Plotkin's logical-geometry program). `[[darienzo-pagano-mcinnis-2020]]` proves a structurally analogous categorical characterization by an entirely independent route: bi-interpretability of coherent theories corresponds to equivalence of the *exact completions* of their Makkai–Reyes syntactic categories (its Theorem 5.1), settling a named open problem (Harnik's conjecture) that predates and is unconnected to the Daniyarova–Myasnikov series. Without bi-interpretability, comparing the logical complexity of two structures requires re-deriving transfer arguments from scratch for each pair; with it, the transfer machinery is reusable.

## Where it appears

- Introduced in: `[[daniyarova-myasnikov-2025]]` (regular bi-interpretability, Definition 7 + composition/invertibility machinery, §4)
- Appears in: `[[daniyarova-myasnikov-2025]]`, `[[daniyarova-myasnikov-2026]]` (strong bi-interpretability, Theorem 13 — categorical equivalence criterion), `[[darienzo-pagano-mcinnis-2020]]` (general bi-interpretability, Theorem 5.1 — exact-completion equivalence criterion, and the equality-preserving variant, Theorem 4.27/Corollary 4.28 — syntactic-category equivalence criterion)
- Related concepts: (none yet — candidate future hubs: interpretation-code, projective-logical-geometry, exact-completion, once a second paper engages with any of them)

## Open questions

- Paper I's **Problem 1** (open): is there a *natural algebraic* example (group or ring) that is regularly but not absolutely bi-interpretable with another — separating the two notions with a non-ad-hoc witness?
- Whether Paper II's categorical equivalence criterion for strong bi-interpretability gives a more tractable *test* for bi-interpretability than the explicit-code approach of Paper I, or whether the two are just different presentations of the same difficulty — not addressed by either paper; a natural question for whoever reads both.
- Whether `[[daniyarova-myasnikov-2026]]`'s projective-logical-sets criterion and `[[darienzo-pagano-mcinnis-2020]]`'s exact-completion criterion are two presentations of the same underlying invariant for a strong notion of bi-interpretability, or genuinely different constructions — not addressed by either paper series, which do not appear to cite each other despite the topical overlap.

## References

1. Daniyarova, E., Myasnikov, A. "Theory of Interpretations I. Foundations." arXiv:2511.13810.
2. Daniyarova, E., Myasnikov, A. "Theory of Interpretations II. Categorical equivalence of projective logical geometries." arXiv:2607.23261.
3. D'Arienzo, A., Pagano, V., McInnis, I.M.J. "Bicategories, Biequivalence, and Bi-Interpretability." arXiv:2011.14056.
