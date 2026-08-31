---
title: "Theory of Interpretations I. Foundations"
authors: Evelina Daniyarova, Alexei Myasnikov
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2511.13810v2
url_translated:
language: en
domain: math-logic
status: draft
methodology_type: theoretical
citation_count:
citation_count_date: 2026-08-15
key_concepts:
  - "[[Concepts/bi-interpretability]]"
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[daniyarova-myasnikov-2026]]"
quality_notes: "arXiv preprint (math.LO primary, math.GR secondary), v1 submitted 2025-11-17, v2 revised 2026-07-25. First paper in a planned series. Citation count not verified at ingest — Semantic Scholar API rate-limited during the ingest session; too recent for a meaningful count regardless. Second #domain/math-logic paper in the vault, after `[[pakhomov-solda-2025-generalized-higman]]`."
author: brett-b
tags:
  - agent/research
  - user/brett-b
  - domain/math-logic
  - topic/model-theory
  - topic/interpretability-theory
  - topic/bi-interpretability
  - topic/definability
  - topic/elimination-of-imaginaries
  - topic/diophantine-problems
  - topic/decidability
  - topic/finitely-presented-groups
  - topic/first-order-classification
  - paper
  - status/draft
---

# Theory of Interpretations I. Foundations

## Abstract

> "This is the first paper in a series in which we lay down the foundations of the theory of interpretations. We systematically study different types of interpretations and their properties. Some of these interpretations are known, while others are new. Each of them serves different purposes. In the last section, we describe applications of interpretations to Diophantine problems, first-order classification, isotypeness, definability of structures by types, elimination of imaginaries, richness, logical categories, and bi-interpretations with Z or N. Additionally, throughout the text, we pose some open questions that naturally arise in this context and provide the most typical examples, usually from algebra. The current literature is plagued by discrepancies and inconsistencies in definitions, concepts, and fundamental applications of interpretations. To address this, we thoroughly examine various principal notions, definitions, and arguments, bringing order to the existing theory. Simultaneously, we develop several key concepts, such as regular interpretations, regular bi-interpretations, and invertible interpretations, and outline their main applications."

*(Verbatim abstract, arXiv:2511.13810v2.)*

## TL;DR

A foundational, house-cleaning paper on the model-theoretic notion of "interpretation" (one algebraic structure realized definably inside another). It standardizes clashing definitions in the literature, introduces a new middle-ground notion — **regular interpretability** — that combines the strengths of parameter-free ("absolute") and parametrized interpretations, and surveys applications: transferring undecidability, classifying elementary equivalence classes, elimination of imaginaries, and bi-interpretability with ℤ/ℕ (which connects to the QFA — quasi-finitely-axiomatizable — property). Worked examples are drawn mostly from group theory (quotient groups, Baumslag–Solitar groups BS(1,k), unitriangular and classical matrix groups).

## Problem

The paper addresses a **terminological and foundational** problem rather than an open technical conjecture: the notion of "interpretation" of one structure in another has accumulated inconsistent definitions and conflated variants across the model theory literature (absolute interpretations, interpretations with parameters, bi-interpretations, and various strong/weak forms), which obscures which properties each variant actually transfers. Absolute (parameter-free) interpretations are rare but transfer elementary equivalence cleanly; interpretations with parameters are common and good for transferring undecidability and stability, but fail to transfer elementary equivalence or support elimination of imaginaries. The paper sets out to unify the definitions and identify a notion — regular interpretability — that captures the advantages of both.

## Approach

Definitional and expository, built from first principles up through worked algebraic examples:

1. Fix a common formal apparatus: languages, P-definable sets, and **Definition 2** — interpretability with parameters — requiring a finite parameter set P, a P-definable domain A\* ⊆ Bⁿ, a P-definable equivalence relation, and P-definable operations making the quotient A\*/~ isomorphic to the target structure 𝔸 (§2.3).
2. Formalize interpretations as explicit **codes** Γ (triples of formulas U_Γ, E_Γ, Q_Γ defining domain, equivalence, and operations/predicates) with associated notions of dimension, injectivity, computability, and being Diophantine (§2.4).
3. Introduce **regular interpretability** (**Definition 7**, §2.5): 𝔸 is regularly interpretable in 𝔹 if there is a code Γ and a "parameter descriptor" formula ϕ(y₁,…,yₖ) such that ϕ(𝔹) ≠ ∅ and every tuple satisfying ϕ gives a valid interpretation — i.e., the interpretation works uniformly across a definable, nonempty set of parameter choices rather than one fixed tuple.
4. Build up composition of interpretations, invertibility, and bi-interpretability (absolute vs. regular, weak vs. strong) in §4.
5. Survey applications in §5: undecidability transfer, Diophantine problems, first-order classification via elementary equivalence, stability/saturation, isotypeness, richness/i-rigidity, logical categories, and bi-interpretability with ℤ.
6. Ground every abstract notion in worked algebraic examples (Examples 1–15), most from group theory: quotient groups via normal subgroups, ℕ inside ℤ (via Lagrange's four-square theorem), ℤ inside ℚ (Robinson's formula), Baumslag–Solitar groups BS(1,k), unitriangular matrix groups UT₃(R), and classical matrix groups.

## Key result

The paper's "results" are principally new/clarified definitions plus a worked regularization lemma and one open problem, rather than a single headline theorem:

- **Definition 2 (interpretability with parameters)**, verbatim: "An algebraic structure 𝔸=⟨A;f,…,R,…,c,…⟩ is interpretable with parameters in an algebraic structure 𝔹=⟨B;L(𝔹)⟩ if the following conditions hold: 1) there is a finite subset P⊆B, 2) for some integer n there is a subset A\*⊆Bⁿ P-definable in 𝔹, 3) there is an equivalence relation ~ on A\* P-definable in 𝔹, 4) there are interpretations f_A,…,R_A,…,c_A,… of the symbols on the quotient set A\*/~, all P-definable in 𝔹, 5) the structure 𝔸\*=⟨A\*/~;f_A,…,R_A,…,c_A,…⟩ is L(𝔸)-isomorphic to 𝔸."
- **Definition 7 (regular interpretability)**, verbatim: "We say that 𝔸 is regularly interpretable in 𝔹 if there exists a code Γ: L(𝔸)→L(𝔹) and an L(𝔹)-formula ϕ(y₁,…,y_k), k = dim_par Γ (called a parameter descriptor), such that ϕ(𝔹) ≠ ∅ and for each p̄=(p₁,…,p_k) ∈ ϕ(𝔹) the pair (Γ,p̄) gives an interpretation 𝔸 ≃ Γ(𝔹,p̄)." (§2.5)
- **Lemma 1**: an explicit regularization of the interpretation R ↝ UT₃(R) (the ring R interpreted in the unitriangular 3×3 matrix group over R) via a descriptor formula ϕ(y₁,y₂) characterizing pairs satisfying `[[y1,y2]] != e` together with centralizer/commutator conditions.
- **Elementary-equivalence transfer property**: for absolute interpretations, "if 𝔸 is absolutely interpretable in 𝔹 by a set of formulas Γ ... and if 𝔹̃ ≡ 𝔹, then 𝔸̃ ≃ Γ(𝔹̃)" and consequently 𝔸̃ ≡ 𝔸 — the key property parametrized interpretations lack in general.
- **QFA connection** (Introduction, citing Khélif–Nies): "Khélif and Nies linked the QFA property of a structure 𝔸 with bi-interpretability of 𝔸 and ℕ or ℤ," and structures regularly bi-interpretable with ℕ are *rich*.
- **Example 10** (§2.3): BS(1,k), k>1, presented as ℤ[1/k] ⋊ ℤ, is shown **absolutely interpretable in ℤ** — elements (zkⁱ, m) and the group operations are given by Diophantine formulas, making the interpretation both computable and Diophantine.
- **Example 15** (attributed to Gvozdevsky): an explicit structure that is regularly but not absolutely interpretable — witnessing that the two notions genuinely differ.
- **Problem 1** (§2.5), verbatim: "Find an example of algebraic structures 𝔸 and 𝔹 in the class of groups or rings such that there exists a regular interpretation 𝔸↝𝔹, but 𝔸 is not absolutely interpretable in 𝔹."

## Assumptions

- Standard first-order model-theoretic setting: algebraic structures in a fixed relational/functional language, classical (not fuzzy/continuous) logic.
- Examples and applications are largely restricted to algebra (groups, rings, ℕ/ℤ/ℚ/ℝ/ℂ in the ring language) — the general theory is language-agnostic but the paper's worked cases are algebraic.
- Assumes familiarity with basic model theory (elementary equivalence, definability, types) and, for the applications section, with stability theory and QFA-property background from prior literature (Khélif–Nies, Nies–Sohrabi).

## Limitations / scope

- This is a **foundations/definitions paper**, explicitly the first in a planned series — it does not itself resolve Problem 1 or push through the deepest applications; those are deferred to later papers in the series.
- No computational or experimental content — purely definitional/expository with algebraic worked examples; no complexity bounds or algorithmic contributions.
- No new results specific to Burnside groups, Knuth–Bendix rewriting, or the B(2,5) program — its connection to this vault's group-theory work is indirect, via general interpretability of finitely presented groups (BS(1,k), matrix groups) rather than anything B25-specific.

## Replication evidence

N/A — a definitional/model-theoretic foundations paper, not an empirical or computational result subject to replication.

## Why this paper matters

This is a rare **standardization** paper: rather than proving a new theorem, it inventories and reconciles a genuinely inconsistent corner of model-theory terminology (the authors state outright that "the current literature is plagued by discrepancies and inconsistencies in definitions"). The introduced middle-ground notion — regular interpretability — is the paper's main conceptual contribution: it is meant to combine the good elementary-equivalence-transfer behavior of absolute interpretations with the practical flexibility (existence, ubiquity) of parametrized interpretations. Because interpretability is the standard tool for transferring undecidability and classifying elementary-equivalence classes between algebraic structures (here mostly groups and rings), this paper is a candidate reference point for anyone in the vault's group-theory work who later needs to reason rigorously about decidability transfer, definability, or bi-interpretability arguments for finitely presented groups — the machinery is general-purpose even though this first installment doesn't apply it to Burnside groups specifically.

## Quotes

1. > "The current literature is plagued by discrepancies and inconsistencies in definitions, concepts, and fundamental applications of interpretations." — Abstract
2. > "Regular interpretability combines useful properties of both [absolute and parametrized interpretations]." — §2.5

## Open questions surfaced

- **Problem 1** (verbatim above, §2.5): find a group- or ring-theoretic example that is regularly but not absolutely interpretable in the other — i.e., a *natural* (algebraic, not ad hoc) witness that the two notions separate. The paper's own witness (Example 15, Gvozdevsky) is not from "algebra" in the paper's stated sense, so a natural algebraic example remains open per the authors. Candidate to check: [[daniyarova-myasnikov-2024]] (same authors, predates this paper) proves the metabelian Baumslag-Solitar group $BS(1,k)$ is regularly *strongly* bi-interpretable with $\mathbb{Z}$ — whether that interpretation is absolute or only regular was not confirmed at this paper's ingest, worth checking against Problem 1.
- Whether the regular-interpretability / bi-interpretability machinery developed here yields any decidability-transfer tool applicable to finitely presented groups closer to the vault's live interests (Burnside groups, word-problem-adjacent structures) — not addressed by this paper, a candidate follow-up question for whoever picks up the later papers in this series.
- The series is explicitly incomplete: this is paper I of a planned sequence, so several forward-referenced results (deeper bi-interpretability theorems, the full applications program of §5) are not yet available to cite.

## Related material in vault

- Extends: (none in vault)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: [[Concepts/bi-interpretability]] — hub created at the ingest of [[daniyarova-myasnikov-2026]] (Paper II), which builds directly on this paper's bi-interpretability apparatus; `interpretation` and `regular interpretability` remain candidate future hubs (singleton so far).
- Cites (in vault): (none)
- Cited by (in vault): [[daniyarova-myasnikov-2026]] — Paper II of this series, which extends and re-derives this paper's bi-interpretability notion categorically.
- Sibling math-logic note: [[pakhomov-solda-2025-generalized-higman]] — the vault's other non-series `#domain/math-logic` paper; both are foundations-of-logic papers with only an indirect, field-level connection (order theory / reverse mathematics vs. model theory of interpretations) rather than a direct citation link. [[daniyarova-myasnikov-2024]] — same authors, predates this paper (submitted 2024 vs. 2025), works out regular strong bi-interpretability in full for the metabelian Baumslag-Solitar group $BS(1,k)$ using the same regular-interpretability terminology this paper (Definition 7) formalizes generally; this paper lists $BS(1,k)$ among its own worked examples but a direct citation to the 2024 paper was not confirmed at ingest.
- Adjacent group-theory work: [[decidability-landscape]] (`Research/Group theory/Word Problem/decidability-landscape.md`) — this paper's undecidability-via-interpretation technique (transferring undecidability of Th(ℕ)/Th(ℤ)) is a general-purpose analogue of the decidability questions catalogued there for the word problem specifically.
- MOC: [[_moc-word-problem]] (`Research/Group theory/_MOCs/_moc-word-problem.md`) — nearest existing decidability-themed MOC in the vault; `Research/Math Logic/` has no MOC of its own yet (only two papers so far).

---

## Notation conventions

Commutator/bracket expressions in this note that could be mistaken for wikilink syntax are wrapped in backticks (e.g. `` `[[y1,y2]]` ``) per vault convention — see `[[paper-summary]]` § Notation conventions.
