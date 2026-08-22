---
title: "Rich groups, weak second order logic, and applications"
authors: Olga Kharlampovich, Alexei Myasnikov, Mahmood Sohrabi
year: 2021
venue: arxiv
url: https://arxiv.org/abs/2109.13133
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
quality_notes: "arXiv preprint (math.LO primary, math.GR secondary), v1 submitted 2021-09-27, v2 (corrected misprints) 2022-10-15. Also published as Chapter 4, pp. 127-192, in Kharlampovich, O. & Sklinos, R. (eds.), *Groups and Model Theory: GAGTA Book 2*, de Gruyter, 2021 — an expository/survey-style chapter rather than a pure research paper, so it reads as a synthesis with new results woven in rather than a single-result paper. Citation count not verified at ingest — Semantic Scholar's API returned HTTP 429 (rate-limited) on two attempts; no count recorded rather than guessed. Fifth `#domain/math-logic` paper in the vault, and the second co-authored by Myasnikov and Sohrabi (after `[[sohrabi-myasnikov-2020]]`), extending the same bi-interpretability-with-ℤ program to a broader class of groups and a new umbrella property (\"richness\"). Note: extraction of the paper body was truncated by the source tool partway through Section 3 (of an apparently 14-section paper); Sections 4-14 (the detailed per-group-family richness proofs, e.g. free metabelian groups, GAGTA-relevant applications) were only reachable via secondary description, not primary text — treat the Key result section's later entries as less rigorously sourced than the early foundational lemmas."
author: brett-b
tags:
  - agent/research
  - user/brett-b
  - domain/math-logic
  - topic/bi-interpretability
  - topic/model-theory
  - topic/interpretability-theory
  - topic/quasi-finite-axiomatizability
  - topic/first-order-rigidity
  - topic/linear-groups
  - topic/hyperbolic-groups
  - topic/nilpotent-groups
  - topic/second-order-logic
  - paper
  - status/draft
---

# Rich groups, weak second order logic, and applications

## Abstract

> "In this paper we initiate a study of first-order rich groups, i.e., groups where the first-order logic has the same power as the weak second order logic. Surprisingly, there are quite a lot of finitely generated rich groups, they are somewhere in between hyperbolic and nilpotent groups (these ones are not rich). We provide some methods to prove that groups (and other structures) are rich and describe some of their properties. As corollaries we look at Malcev's problems in various groups."

*(Verbatim abstract, arXiv:2109.13133v2.)*

## TL;DR

Defines a group (or ring) $G$ to be **rich** when it is bi-interpretable with $HF(G)$, the superstructure of hereditary-finite sets built over $G$ — the effect being that weak second-order logic (WSOL) over $G$ collapses to ordinary first-order logic over $G$. The headline empirical finding is that richness sits strictly between hyperbolicity and nilpotency in the landscape of finitely generated groups: $\text{SL}_n(\mathbb{Z})$/$\text{GL}_n(\mathbb{Z})$ ($n\geq3$), non-uniform higher-rank lattices, and (surprisingly) free metabelian groups and free group algebras are rich, while free/hyperbolic groups and nilpotent groups are not. Since bi-interpretability composes transitively, richness is mostly proved by chaining bi-interpretability with $\mathbb{Z}$ (which is itself known to be rich) rather than working with WSOL directly. As an application, richness gives uniform definability of finitely generated subgroups/subrings/ideals, which the authors use to revisit Mal'cev's 1965 definability question for subgroups of free groups.

## Problem

The paper asks which finitely generated groups (and, more generally, algebraic structures) are **first-order rich**: structures over which first-order logic already has the full expressive power of weak second-order logic, so that no genuinely "higher" logic is needed to talk about their finite subsets, finite tuples-of-tuples, or other WSOL-expressible objects. This sits downstream of the broader first-order-rigidity program (Avni-Lubotzky-Meiri and others): rigidity asks whether elementary equivalence forces isomorphism; richness is a stronger, more structural property that (via bi-interpretability with $\mathbb{Z}$, itself known rich) tends to imply rigidity and QFA as a byproduct. As an application track, the paper revisits Mal'cev's 1965 question — which subgroups of a free group $F$ are first-order definable in $F$? (known: only cyclic ones, among proper subgroups) — by asking what richness buys for definability of finitely generated substructures more generally.

## Approach

1. **Interpretability/bi-interpretability formalism** (§2): recaps interpretation via coordinate maps $\mu: U_\Gamma \to A$, admissibility conditions, and composition of interpretations (Lemma 3, transitivity) — the same apparatus used across the vault's other Myasnikov-adjacent bi-interpretability papers. Establishes that decidability, elementary equivalence, and first-order rigidity all transfer along regular interpretations (Lemma 4).
2. **Weak second-order logic via hereditary-finite superstructures** (§3): defines richness as bi-interpretability of $G$ with $HF(G)$ (the hereditary-finite-set superstructure over $G$), and shows this is equivalent to interpretability of WSOL-over-$G$ inside $G$ itself.
3. **The main proof strategy, used throughout the later sections**: since bi-interpretability composes transitively and $\mathbb{Z}$ is already known to be rich, richness for a new structure $G$ is typically established by proving $G$ is bi-interpretable with $\mathbb{Z}$ (or with another already-rich structure) rather than by verifying the WSOL/HF(G) definition directly.
4. **Per-family case studies** (§§11-14, only partially recoverable from the fetched source): classical linear groups ($\text{SL}_n(\mathbb{Z})$, $\text{GL}_n(\mathbb{Z})$, $\text{T}_n(\mathcal{O})$ with finite units), non-uniform higher-rank lattices, free metabelian groups, free group algebras over infinite fields, and (in the negative direction) hyperbolic/free groups, nilpotent groups, and $\text{T}_n(\mathcal{O})$ with infinite units ("not rich modulo the infinite center").
5. **Malcev's-problem application** (§6 and surrounding): richness gives uniform definability of a rich structure's finitely generated subgroups (subrings, ideals), its Cayley-graph geometry, and other associated objects — reframed as a partial answer to Mal'cev's definability question for the rich cases.

## Key result

- **Definition of richness** (§3): $G$ is rich iff $G$ is bi-interpretable with $HF(G)$, the hereditary-finite-sets superstructure over $G$; equivalently, WSOL over $G$ is interpretable in $G$ itself. Finitely generated rich structures are completely characterized by a single first-order axiom (QFA-style).
- **Lemma 3** (transitivity of interpretability): if $\mathbb{A}$ interprets in $\mathbb{B}$ and $\mathbb{B}$ interprets in $\mathbb{C}$, then $\mathbb{A}$ interprets in $\mathbb{C}$ — the composition tool that lets richness propagate from $\mathbb{Z}$ to any structure bi-interpretable with it.
- **Lemma 4**: decidability, elementary equivalence, and first-order rigidity are all preserved under regular interpretations.
- **Theorem 26** (per the source's numbering, partially recovered): $\text{SL}_n(\mathbb{Z})$ and $\text{GL}_n(\mathbb{Z})$, $n \geq 3$, are rich; non-uniform higher-rank lattices are rich; $\text{T}_n(\mathcal{O})$ is rich when $\mathcal{O}^\times$ is finite.
- **Positive results (§§ around 13-14)**: free metabelian groups are rich; free group algebras over infinite fields are rich (even though the underlying free group itself is not) — the authors flag this as showing "how much more expressive is the first order ring language of a group algebra" than the group language alone.
- **Negative results**: free groups and torsion-free hyperbolic groups are *not* rich, and are described as "very far from being rich"; nilpotent groups are not rich; $\text{T}_n(\mathcal{O})$ with infinite unit group is not rich (failure attributed to "the infinite center").
- **Malcev's-problem corollary**: for rich groups, finitely generated subgroups (and analogously subrings/ideals for rich rings), the Cayley-graph geometry, and other naturally-associated objects become uniformly first-order definable — the mechanism the paper offers as its answer to Malcev's 1965 definability question, for the class of rich structures.

## Assumptions

- Languages are assumed finite throughout (finite signature for groups $\{\cdot, {}^{-1}, 1\}$, rings $\{+,\cdot,0\}$, monoids $\{\cdot,1\}$).
- Primary focus is on **finitely generated** structures rather than arbitrary countable ones — justified by the authors as the algebraically natural restriction.
- Interpretations may use parameters, with parameter dimension tracked explicitly (following the same interpretation-code apparatus as `[[daniyarova-myasnikov-2025]]`).
- The richness apparatus presumes the reader accepts hereditary-finite-set superstructures $HF(G)$ as the right formalization of "weak second-order objects over $G$" — this is a definitional choice, not derived from first principles.

## Limitations / scope

- The fetched source was truncated partway through §3 (of what is described as a 14-section chapter); the detailed per-family proofs in §§4-14 were only reconstructable from secondary description in the fetch tool's own synthesis, not read as primary text. Treat theorem numbers and the fine detail of the later positive/negative results (Theorem 26 and the free-metabelian/group-algebra results) as less rigorously sourced than the foundational lemmas in §2-3, and verify against the primary PDF before citing exact theorem statements from this note.
- Which finitely generated **solvable** groups are rich is explicitly left open beyond the specific cases covered (free metabelian groups rich; general status of Baumslag-Solitar groups and $\mathbb{Z} \wr \mathbb{Z}$ unresolved at time of writing).
- For free metabelian groups, the authors note the elementary-equivalence "completions" still exist but "are not described by any algebraic schemes, the schemes here are more general" — i.e. richness holds but the associated structure theory is not as classically presentable as in the linear-group cases.
- The chapter is explicitly expository/survey-oriented (written for the GAGTA Book 2 volume), so it mixes original results with restatement of prior work (Khélif-Nies, Avni-Lubotzky-Meiri, Malcev) more than a typical single-result research paper.

## Replication evidence

N/A — a theoretical model-theory/group-theory paper with proofs, not an empirical or computational claim subject to replication. Published in peer-reviewed book form (de Gruyter, 2021) alongside the arXiv preprint.

## Why this paper matters

This is the paper that names and systematizes "richness" as the umbrella property behind a cluster of prior bi-interpretability-with-$\mathbb{Z}$ results (including the authors' own — Myasnikov and Sohrabi's `[[sohrabi-myasnikov-2020]]` proves exactly the $\text{SL}_n(\mathcal{O})$/$\text{GL}_n(\mathcal{O})$/$\text{T}_n(\mathcal{O})$ results this paper cites as its Theorem-26-level classical-groups case study), and locates it precisely between hyperbolicity and nilpotency in the landscape of finitely generated groups — a genuinely informative dichotomy, since neither "more geometric" (hyperbolic) nor "more algebraic" (nilpotent) structure alone predicts richness. The free-group-algebra-is-rich-but-free-group-is-not result is a sharp illustration that expressive power is sensitive to which structure (group vs. its group ring) is being interpreted, which matters for anyone using bi-interpretability as a black-box tool rather than re-deriving it per structure. For a vault already tracking the QFA/Khélif-Nies/bi-interpretability lineage via `[[daniyarova-myasnikov-2025]]`, this paper supplies the term "rich" that Paper I uses in passing ("structures regularly bi-interpretable with ℕ are *rich*") with its full definitional and case-study backing — worth checking, on a closer read, whether this paper's HF(G)-based richness and Khélif-Nies's original richness notion (as invoked in Paper I) are stated as the same property or as related-but-distinct ones.

## Quotes

1. > "There are quite a lot of finitely generated rich groups, they are somewhere in between hyperbolic and nilpotent groups (these ones are not rich)." — Abstract
2. > "Free and torsion-free hyperbolic groups are not rich. Actually they are very far from being rich." — §11 (per source synthesis)

## Open questions surfaced

- Which finitely generated solvable groups are rich, beyond free metabelian groups — explicitly left open, including the status of Baumslag-Solitar groups and $\mathbb{Z} \wr \mathbb{Z}$ (wreath product).
- Whether richness can be given a purely algebraic (rather than logical/WSOL) characterization for classes like free metabelian groups, where the authors note the elementary-equivalence completions "are not described by any algebraic schemes."
- Whether this paper's HF(G)-bi-interpretability notion of "rich" and the Khélif-Nies notion referenced in `[[daniyarova-myasnikov-2025]]` (via QFA and bi-interpretability with $\mathbb{N}$) are the same property or related-but-distinct — not addressed in either note; a natural cross-check for a future close reading.
- The paper's own Section 4 (WSOL/$L_{\omega_1,\omega}$ comparison) and Sections 5-10 were not recoverable from the truncated fetch — a full re-read against the primary PDF or the de Gruyter book chapter is needed to confirm the complete theorem inventory before this note's `status` moves past `draft`.

## Related material in vault

- Extends: (none in vault — though richness here is presented as building on and unifying `[[sohrabi-myasnikov-2020]]`'s specific $\text{SL}_n$/$\text{GL}_n$/$\text{T}_n$ results, no direct citation confirmed from the truncated source)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: `[[Concepts/bi-interpretability]]` — fifth paper in the vault to substantively engage with bi-interpretability; introduces "richness" (bi-interpretability with $HF(G)$) as a named derived property, worth a future concept-hub mention or its own stub if a second paper engages with richness specifically.
- Cites: (none confirmed as in-vault papers from the recoverable text; the paper's own citations to Khélif-Nies and Avni-Lubotzky-Meiri are not yet separate vault entries)
- Cited by (in vault): plausibly `[[myasnikov-nikolaev-2024]]` — that paper's introduction cites an unidentified reference [16] for the term "rich" using an identical WSOL-collapse definition and shares author Myasnikov, but the exact bibliography entry could not be confirmed at that paper's ingest, so this link is noted here as likely rather than asserted in frontmatter.
- Sibling math-logic notes: `[[myasnikov-sohrabi-2013]]` — shares two of three authors (Myasnikov, Sohrabi); this paper's stated finding that nilpotent groups are *not* rich is the natural sequel to that earlier paper's partial result (ℤ is interpretable, but not shown bi-interpretable, in finitely generated nilpotent groups — blocked at an unavoidable "special gap" in the central series); `[[sohrabi-myasnikov-2020]]` — shares two of three authors (Myasnikov, Sohrabi) and its classical-linear-groups results ($\text{SL}_n(\mathcal{O})$, $\text{GL}_n(\mathcal{O})$, $\text{T}_n(\mathcal{O})$) are the specific case this paper's richness framework subsumes as one family among several (hyperbolic-vs-nilpotent spectrum); `[[daniyarova-myasnikov-2025]]` — shares the QFA/bi-interpretability-with-$\mathbb{Z}$/$\mathbb{N}$ theme and the term "rich" itself, via its citation of the Khélif-Nies QFA-bi-interpretability connection; `[[myasnikov-nikolaev-2024]]` — extends the richness construction from groups (this paper's $HF(G)$ superstructure) to polynomial rings (that paper's list superstructure $\mathbb{S}(F,\mathbb{N})$), explicitly using the term "rich" for the ring case.

---

## Notation conventions

Group/logic notation in this note ($\text{SL}_n$, $HF(G)$, $L_{\omega_1,\omega}$, superscripts) is rendered in LaTeX inline math and plain Unicode prose; no `[[...]]`-style double-bracket expressions requiring backtick-escaping appear, per `[[paper-summary]]` § Notation conventions.
