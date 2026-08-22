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
  - "[[sohrabi-myasnikov-2020]]"
  - "[[kharlampovich-myasnikov-sohrabi-2021]]"
  - "[[myasnikov-sohrabi-2024]]"
  - "[[daniyarova-myasnikov-2024]]"
  - "[[myasnikov-nikolaev-2024]]"
---

# Bi-interpretability

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

Two algebraic structures 𝔸 and 𝔹 are **bi-interpretable** when each is interpretable in the other *and* the two composite interpretations (𝔸 → 𝔹 → 𝔸, and 𝔹 → 𝔸 → 𝔹) are themselves definable isomorphisms back to the original structure — i.e. interpretability is not just mutual but coherently invertible. `[[daniyarova-myasnikov-2025]]` (Paper I) formalizes several strengths of this notion for interpretations-with-parameters, notably **regular bi-interpretability**, built on its regular-interpretability definition (Definition 7, §2.5): a bi-interpretation is regular when both directions' interpretation codes work uniformly across a definable, nonempty set of parameter choices rather than one fixed tuple. `[[daniyarova-myasnikov-2026]]` (Paper II) gives a categorical characterization of the *strong* variant: **Theorem 13** — 𝔸 and 𝔹 are strongly bi-interpretable iff their categories of projective logical sets (𝒫ℒ𝒮(𝔸), 𝒫ℒ𝒮(𝔹)) are equivalent relative to interpretation functors, equivalently iff their categories of projective definable sets (𝒫𝒟𝒮(𝔸), 𝒫𝒟𝒮(𝔹)) are equivalent relative to translation functors.

## Why it matters

Bi-interpretability is the model-theoretic tool for showing two structures are, for logical purposes, "the same" without being isomorphic: it transfers decidability/undecidability, elementary-equivalence classification, and (per the Khélif–Nies connection cited in Paper I) the QFA (quasi-finitely-axiomatizable) property. The Daniyarova–Myasnikov papers approach it from opposite ends — Paper I builds the notion up from explicit interpretation codes and parameter descriptors with worked algebraic examples (Baumslag–Solitar groups, unitriangular matrix groups); Paper II reformulates the strong variant purely categorically, replacing an explicit-code characterization with an equivalence-of-categories criterion (equivalence of categories of *projective logical sets*, built on Plotkin's logical-geometry program). `[[darienzo-pagano-mcinnis-2020]]` proves a structurally analogous categorical characterization by an entirely independent route: bi-interpretability of coherent theories corresponds to equivalence of the *exact completions* of their Makkai–Reyes syntactic categories (its Theorem 5.1), settling a named open problem (Harnik's conjecture) that predates and is unconnected to the Daniyarova–Myasnikov series. `[[sohrabi-myasnikov-2020]]` supplies the concrete worked case the other three treat abstractly: it proves bi-interpretability of $\mathbb{Z}$ with $\text{SL}_n(\mathcal{O})$ outright (transvection definability + bounded generation), shows it fails for $\text{GL}_n(\mathcal{O})$ with infinite units even though model classification still holds, and shows it fails more severely for $\text{T}_n(\mathcal{O})$, which then requires a purpose-built cocycle classification (coboundary-on-torsion) of its many non-isomorphic elementarily-equivalent models — direct evidence that bi-interpretability with $\mathbb{Z}$/$\mathbb{N}$ is not all-or-nothing across a family of structurally related groups. `[[kharlampovich-myasnikov-sohrabi-2021]]` names and systematizes the umbrella property behind this pattern — **richness**: $G$ is rich when it is bi-interpretable with $HF(G)$ (the hereditary-finite-set superstructure over $G$), which collapses weak second-order logic over $G$ to first-order logic over $G$. Since bi-interpretability composes transitively and $\mathbb{Z}$ is itself rich, richness is mostly established by chaining bi-interpretability with $\mathbb{Z}$ — making `[[sohrabi-myasnikov-2020]]`'s $\text{SL}_n(\mathcal{O})$ result one specific case study inside this broader program, and locating richness precisely between hyperbolicity and nilpotency in the landscape of finitely generated groups. `[[myasnikov-sohrabi-2024]]` completes the ring-to-field generalization `[[sohrabi-myasnikov-2020]]` promised: $\text{SL}_n(F)$ is *regularly* bi-interpretable with $F$ for any field $F$, $n \geq 3$ — a uniform-over-parameters strengthening of the plain bi-interpretability the ring case established — while $\text{T}_n(F)$ again produces genuine non-isomorphic elementarily-equivalent "abelian deformation" models (explicitly witnessed for $T_n(\mathbb{Q})$, Theorem 5.15), confirming the same $\text{SL}_n$/$\text{GL}_n$/$\text{T}_n$ trichotomy holds identically whether the coefficient structure is a ring of integers or a field. `[[daniyarova-myasnikov-2024]]` gives the same authors' worked example of *regular strong* bi-interpretability applied to a structurally different object — the metabelian Baumslag-Solitar group $BS(1,k)$ — proving it bi-interpretable with $\mathbb{Z}$ and, via that, classifying every group elementarily equivalent to $BS(1,k)$ as precisely a non-standard model $BS(1,k,\tilde{\mathbb{Z}})$ built from a non-standard model $\tilde{\mathbb{Z}} \equiv \mathbb{Z}$; chronologically this paper predates `[[daniyarova-myasnikov-2025]]` (Paper I lists $BS(1,k)$ as a worked example using the same terminology this paper develops in full). `[[myasnikov-nikolaev-2024]]` extends the richness program from groups to commutative rings: polynomial and Laurent polynomial rings $F[x_1,\dots,x_n]$ over an infinite field or $\mathbb{Z}$ are regularly bi-interpretable with a **list superstructure** $\mathbb{S}(F,\mathbb{N})$ — a construction parallel to but distinct from the hereditary-finite-set superstructure $HF(G)$ used for groups — making them rich in the same WSOL-collapse sense, with the classification collapsing to a clean statement: $F[X] \equiv L[Y]$ iff $|X|=|Y|$ and $HF(F) \equiv HF(L)$. Without bi-interpretability, comparing the logical complexity of two structures requires re-deriving transfer arguments from scratch for each pair; with it, the transfer machinery is reusable.

## Where it appears

- Introduced in: `[[daniyarova-myasnikov-2025]]` (regular bi-interpretability, Definition 7 + composition/invertibility machinery, §4)
- Appears in: `[[daniyarova-myasnikov-2025]]`, `[[daniyarova-myasnikov-2026]]` (strong bi-interpretability, Theorem 13 — categorical equivalence criterion), `[[darienzo-pagano-mcinnis-2020]]` (general bi-interpretability, Theorem 5.1 — exact-completion equivalence criterion, and the equality-preserving variant, Theorem 4.27/Corollary 4.28 — syntactic-category equivalence criterion), `[[sohrabi-myasnikov-2020]]` (concrete bi-interpretability with $\mathbb{Z}$ for $\text{SL}_n(\mathcal{O})$, $n \geq 3$ — Theorem 2.4 — plus the model-classification consequences when bi-interpretability partially or fully fails for $\text{GL}_n(\mathcal{O})$/$\text{T}_n(\mathcal{O})$), `[[kharlampovich-myasnikov-sohrabi-2021]]` (richness — bi-interpretability with $HF(G)$ — as the umbrella property unifying the classical-linear-group bi-interpretability results with a wider class: non-uniform lattices, free metabelian groups, free group algebras), `[[myasnikov-sohrabi-2024]]` (field-coefficient sequel — *regular* bi-interpretability of $\text{SL}_n(F)$ with $F$, Theorem A1 — plus the field-setting $\text{T}_n(F)$/$\text{GL}_n(F)$ classifications), `[[daniyarova-myasnikov-2024]]` (regular strong bi-interpretability of the metabelian Baumslag-Solitar group $BS(1,k)$ with $\mathbb{Z}$, Theorem 3 — plus the full non-standard-model classification, Theorem 5), `[[myasnikov-nikolaev-2024]]` (regular bi-interpretability of polynomial/Laurent-polynomial rings $F[x_1,\dots,x_n]$ with the list superstructure $\mathbb{S}(F,\mathbb{N})$, Theorem 4.1 — richness extended to a ring rather than group setting)
- Related concepts: (none yet — candidate future hubs: interpretation-code, projective-logical-geometry, exact-completion, quasi-finite-axiomatizability, richness, once a second paper engages with any of them)

## Open questions

- Paper I's **Problem 1** (open): is there a *natural algebraic* example (group or ring) that is regularly but not absolutely bi-interpretable with another — separating the two notions with a non-ad-hoc witness? `[[daniyarova-myasnikov-2024]]`'s $BS(1,k)$ result is a candidate to check against this: it is unclear from that paper's extracted content whether $BS(1,k)$'s interpretation in $\mathbb{Z}$ is absolute or only regular — worth a closer read.
- Whether Paper II's categorical equivalence criterion for strong bi-interpretability gives a more tractable *test* for bi-interpretability than the explicit-code approach of Paper I, or whether the two are just different presentations of the same difficulty — not addressed by either paper; a natural question for whoever reads both.
- Whether `[[daniyarova-myasnikov-2026]]`'s projective-logical-sets criterion and `[[darienzo-pagano-mcinnis-2020]]`'s exact-completion criterion are two presentations of the same underlying invariant for a strong notion of bi-interpretability, or genuinely different constructions — not addressed by either paper series, which do not appear to cite each other despite the topical overlap.

## References

1. Daniyarova, E., Myasnikov, A. "Theory of Interpretations I. Foundations." arXiv:2511.13810.
2. Daniyarova, E., Myasnikov, A. "Theory of Interpretations II. Categorical equivalence of projective logical geometries." arXiv:2607.23261.
3. D'Arienzo, A., Pagano, V., McInnis, I.M.J. "Bicategories, Biequivalence, and Bi-Interpretability." arXiv:2011.14056.
4. Sohrabi, M., Myasnikov, A.G. "Bi-interpretability with ℤ and models of the complete elementary theories of SLₙ(𝒪), Tₙ(𝒪) and GLₙ(𝒪), n≥3." arXiv:2004.03585 (published as Miasnikov & Sohrabi, *Journal of Algebra* 582 (2021), 206-231).
5. Kharlampovich, O., Myasnikov, A., Sohrabi, M. "Rich groups, weak second order logic, and applications." arXiv:2109.13133 (published as Ch. 4, pp. 127-192, in *Groups and Model Theory: GAGTA Book 2*, de Gruyter, 2021).
6. Myasnikov, A.G., Sohrabi, M. "Groups elementarily equivalent to the classical matrix groups." arXiv:2405.14476 (published as Ch. 4, pp. 53-86, in *Finitely Presented Groups: With Applications in Post-Quantum Cryptography and Artificial Intelligence*, de Gruyter, 2024).
7. Daniyarova, E., Myasnikov, A. "Groups elementarily equivalent to metabelian Baumslag-Solitar groups and regular bi-interpretability." arXiv:2407.00642 (published in *Annals of Pure and Applied Logic* 177(5) (2026), Article 103695).
8. Myasnikov, A., Nikolaev, A. "Nonstandard polynomials: algebraic properties and elementary equivalence." arXiv:2409.14467 (published in *Journal of Logical and Algebraic Methods in Programming* 146 (2025), Article 101071).
