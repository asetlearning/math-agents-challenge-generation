---
title: "Groups elementarily equivalent to the classical matrix groups"
authors: Alexei G. Myasnikov, Mahmood Sohrabi
year: 2024
venue: arxiv
url: https://arxiv.org/abs/2405.14476
url_translated:
language: en
domain: math-logic
status: draft
methodology_type: theoretical
citation_count: 1
citation_count_date: 2026-08-22
key_concepts:
  - "[[Concepts/bi-interpretability]]"
extends:
  - "[[sohrabi-myasnikov-2020]]"
contradicts: []
replicates: []
cites:
  - "[[sohrabi-myasnikov-2020]]"
cited_by: []
quality_notes: "arXiv preprint (math.GR primary, math.LO secondary), v1 submitted 2024-05-23, 36 pages. Published as Ch. 4, pp. 53-86, in Diekert, V. & Kreuzer, M. (eds.), *Finitely Presented Groups: With Applications in Post-Quantum Cryptography and Artificial Intelligence*, de Gruyter, 2024 (DOI 10.1515/9783111473574-004). Citation count 1 (Semantic Scholar, 2026-08-22). Sixth `#domain/math-logic` paper in the vault; direct sequel to `[[sohrabi-myasnikov-2020]]`, replacing the ring-of-integers setting $\mathcal{O}$ with an arbitrary field $F$ — the exact extension `[[sohrabi-myasnikov-2020]]`'s Open questions section flagged as promised future work ('a sequel to this paper we study the relevant questions, when $\mathcal{O}$ is replaced by a field $F$'). The paper cites the earlier ring-of-integers paper as prior work (reference [31] in its bibliography per the fetched source) but the fetched extraction did not find language explicitly announcing itself as *the* promised sequel — treat the `extends`/`cites` link above as topically and technically confirmed (same authors, same theorem shapes, explicit citation), not as a verbatim self-declared-sequel claim."
author: brett-b
tags:
  - agent/research
  - user/brett-b
  - domain/math-logic
  - topic/bi-interpretability
  - topic/model-theory
  - topic/interpretability-theory
  - topic/elementary-equivalence
  - topic/linear-groups
  - topic/first-order-rigidity
  - topic/quasi-finite-axiomatizability
  - paper
  - status/draft
---

# Groups elementarily equivalent to the classical matrix groups

## Abstract

> "We describe all groups that are first-order (elementarily) equivalent to the classical matrix groups such as $\text{GL}_n(F)$, $\text{SL}_n(F)$ and $\text{T}_n(F)$ over a field $F$ provided $n \geq 3$."

*(Verbatim abstract, arXiv:2405.14476v1.)*

## TL;DR

The field-coefficient counterpart to `[[sohrabi-myasnikov-2020]]`'s ring-of-integers results: for $n \geq 3$ and any field $F$, $\text{SL}_n(F)$ turns out to be *regularly* bi-interpretable with $F$ itself (a strictly stronger and uniform version of the earlier bi-interpretability result), which pins down every group elementarily equivalent to $\text{SL}_n(F)$ as exactly $\text{SL}_n(L)$ for some $L \equiv F$. $\text{T}_n(F)$ again spawns non-isomorphic elementarily-equivalent "abelian deformation" models — classified in general (necessity) and, for a broad field class (NFT-fields — includes number fields), fully classified both directions — while $\text{GL}_n(F)$ sits in between, with an explicit extension description rather than a clean bi-interpretability statement. Malcev's classical rigidity theorems for these groups (elementary equivalence of $\text{GL}_n(F)$ and $\text{GL}_m(L)$ forces $n=m$, $F \equiv L$) are generalized and sharpened throughout.

## Problem

Malcev's classical theorems established that $\text{GL}_n(F) \equiv \text{GL}_m(L)$ forces $n = m$ and $F \equiv L$, but left open the finer question: given only that $H \equiv \text{GL}_n(F)$ (or $\text{SL}_n(F)$, $\text{T}_n(F)$), what can $H$ actually *be*, up to isomorphism? This paper solves that first-order classification problem completely for $n \geq 3$ over an arbitrary field $F$ — the natural field-coefficient analogue of `[[sohrabi-myasnikov-2020]]`'s ring-of-integers classification, and the direction that paper's own "Open questions" section flagged as future work.

## Approach

1. **Diophantine interpretability in large subgroups** (§§1-3): establishes mutual Diophantine (existentially-definable) interpretability between the classical matrix groups and their underlying rings/fields. Key technical result (Theorem 3.1): for $1 \leq k \neq m \leq n$, the elementary subgroup $T_{km}$ is Diophantine-definable in $G$. Shows the ring $R$ is $e$-interpretable in $\text{GL}_n(R)$ and conversely (Theorem 3.7, Proposition 3.10), giving Karp-equivalence of the two structures' Diophantine problems (Theorem 3.11).
2. **$\text{SL}_n(F)$** (§4): proves $F$ is regularly bi-interpretable with $\text{SL}_n(F)$ — regularity meaning the interpretation codes work uniformly over a definable set of parameters rather than one fixed tuple, a strictly stronger statement than plain bi-interpretability. Uses bounded elementary generation of $\text{SL}_n(F)$ by transvections (automatic over any field, unlike the ring case where it required a hard theorem) to interpret $F$ inside large subgroups, then constructs $\text{SL}_n(F)$ back inside $F$ via the standard matrix construction.
3. **$\text{T}_n(F)$** (§5): works with the quotient core $\text{PT}_n(F) = T_n(F)/Z(T_n(F))$, then classifies models via **abelian deformations** $T_n(L, f, Z)$ parametrized by a 2-cocycle $f \in S^2(B_n(L), Z)$ — the direct field-setting analogue of the ring case's cocycle deformations. Splits into algebraically closed fields, real closed fields, and a new class the authors call **NFT-fields** (includes number fields), proving necessity in general (Theorem A3/5.x) and full necessity-plus-sufficiency for NFT-fields (Theorem 5.12) and for real-closed/algebraically-closed fields (Theorem 5.13).
4. **$\text{GL}_n(F)$** (§6): exploits $\text{GL}_n(F) \cong \text{SL}_n(F) \rtimes d_1(F^\times)$ and that $\text{SL}_n(F) = G'$ (the derived subgroup) is absolutely definable, then applies abstract-isomorphism-theorem machinery to recover $F$ from any $H \equiv \text{GL}_n(F)$, with characteristic-0-algebraically-closed and real-closed cases (Theorems 6.1, 6.3) worked out explicitly.

## Key result

- **Theorem A1**: for any field $F$ and $n \geq 3$, $\text{SL}_n(F)$ is *regularly* bi-interpretable with $F$.
- **Theorem A2** ($\text{SL}_n$ classification, the paper's cleanest result): $H \equiv \text{SL}_n(F)$ iff $H \cong \text{SL}_n(L)$ for some field $L \equiv F$.
- **Theorem A3** ($\text{T}_n$ classification, necessity): for $F$ infinite of characteristic $\neq 2$, if $H \equiv T_n(F)$ then $H \cong T_n(L, f, Z)$ for some $L \equiv F$, 2-cocycle $f \in S^2(B_n(L), Z)$, and abelian group $Z = Z(H) \equiv F^\times$.
- **Theorem A4** ($\text{GL}_n$ structure): if $H \equiv \text{GL}_n(F)$, then $H$ fits an explicit extension $1 \to H' \cdot Z(H) \to H \to L^\times/(L^\times)^n \to 1$ with $H' \cong \text{SL}_n(L)$, $L \equiv F$, $Z(H) \equiv F^\times$.
- **Theorem 5.12** (NFT-field sufficiency): if $H = T_n(F, f, Z)$ with $F$ an NFT-field and $f$ coboundary-on-torsion (CoT), then $H \equiv T_n(F)$ — the reverse direction completing Theorem A3's necessity for this field class, exactly mirroring `[[sohrabi-myasnikov-2020]]`'s Theorem 3.17 for the ring case.
- **Theorem 5.13** (real-closed / algebraically-closed $\text{T}_n$): for $F$ real closed or algebraically closed, $H \equiv T_n(F)$ iff $H \cong \text{PT}_n(L) \times Z(H)$ for $L \equiv F$, $Z(H) \equiv F^\times$.
- **Theorem 5.15** (a genuine non-classification witness): there exist $H \equiv T_n(\mathbb{Q})$ that are *not* isomorphic to $T_n(L)$ for any field $L$ — real abelian-deformation models exist, not just a theoretical possibility.
- **Theorem 6.1 / 6.3** ($\text{GL}_n$ over algebraically-closed / real-closed $F$): explicit isomorphism-type descriptions for $H \equiv \text{GL}_n(F)$ in these two field classes.

## Assumptions

- $F$ is an infinite field, generally assumed characteristic $\neq 2$ (a recurring restriction across the $\text{T}_n$/$\text{GL}_n$ results; the $\text{SL}_n$ bi-interpretability result appears to hold without a characteristic restriction).
- $n \geq 3$ throughout, for the same bounded-generation reasons as the ring-of-integers paper.
- The $\text{T}_n$/$\text{GL}_n$ results split by field type for their strongest (necessity + sufficiency) form: NFT-fields (a class the paper introduces, including number fields), real closed fields, algebraically closed fields. General infinite fields of characteristic $\neq 2$ get only the necessity direction (Theorem A3) without the matching sufficiency.

## Limitations / scope

- For general (non-NFT, non-real-closed, non-algebraically-closed) fields, only the *necessity* direction of the $\text{T}_n$ classification is proved (Theorem A3); full sufficiency is left open outside the specific field classes covered.
- Theorem 5.15 shows the abelian-deformation phenomenon is not a vacuous technicality: genuine non-isomorphic-but-elementarily-equivalent models of $T_n(\mathbb{Q})$ exist.
- The authors flag, rather than resolve, a broader research direction — "there might be a general approach to the first-order classification problem of algebraic groups," gesturing at an "emerging unified model theory of algebraic groups" (abstract isomorphism theorems as the common tool) without developing it here.
- As with the ring-of-integers paper, purely theoretical: no computational, algorithmic, or Burnside/Knuth-Bendix content relevant to this vault's B(2,5) program.

## Replication evidence

N/A — a theoretical model-theory/group-theory paper with full proofs. Published in peer-reviewed book form (de Gruyter, 2024) alongside the arXiv preprint; no independent replication of the theorems by other authors surfaced at ingest (citation count 1).

## Why this paper matters

This paper closes the loop `[[sohrabi-myasnikov-2020]]` opened: where that paper handled $\mathcal{O}$ (rings of integers of number fields) and explicitly deferred the field case to a sequel, this paper delivers it — and sharpens the bi-interpretability result along the way (*regular* bi-interpretability for $\text{SL}_n(F)$, a uniform-over-parameters strengthening the ring-of-integers paper's plain bi-interpretability). The structural pattern across both papers is now visible as a genuine trichotomy rather than a coincidence: $\text{SL}_n$ is always the clean, fully-rigid case; $\text{GL}_n$ sits in between (bi-interpretability fails once units are non-finite/non-trivial, but the model structure stays tractable); $\text{T}_n$ is where deformation phenomena genuinely proliferate, requiring purpose-built cocycle machinery (CoT cocycles) in both the ring and field settings. Theorem 5.15's explicit witness — real, non-isomorphic elementarily-equivalent models of $T_n(\mathbb{Q})$ — turns what could have been a purely formal possibility (non-uniqueness of models) into a concrete mathematical fact worth knowing on its own. For readers of the vault's Myasnikov/Sohrabi bi-interpretability cluster, this paper is the natural next read after `[[sohrabi-myasnikov-2020]]`, completing the promised ring-to-field generalization and generalizing Malcev's original rigidity theorems for these groups substantially beyond their original scope.

## Quotes

1. > "We describe all groups that are first-order (elementarily) equivalent to the classical matrix groups such as $\text{GL}_n(F)$, $\text{SL}_n(F)$ and $\text{T}_n(F)$ over a field $F$ provided $n \geq 3$." — Abstract
2. > "The ring $R$ is $e$-interpretable in $\text{GL}_n(R)$" — §3 (Diophantine-interpretability mechanism underlying the paper's classification theorems)

## Open questions surfaced

- Full sufficiency for the $\text{T}_n(F)$ classification over general infinite fields of characteristic $\neq 2$ (beyond NFT-fields, real closed, and algebraically closed) — currently only necessity (Theorem A3) is established.
- The authors' own gestured-at future direction: "a general approach to the first-order classification problem of algebraic groups" — an "emerging unified model theory of algebraic groups" built on abstract isomorphism theorems, not developed in this paper.
- Whether the NFT-field class (introduced here for the field-sufficiency argument) has independent model-theoretic interest beyond this application, or a natural characterization connecting it to more standard field-theoretic classes.
- Not addressed by either paper: whether the trichotomy structure ($\text{SL}_n$ clean / $\text{GL}_n$ intermediate / $\text{T}_n$ deformation-rich) that holds identically over both rings-of-integers and fields is itself provable as a single unified theorem, or is a coincidence of two independently-executed but structurally parallel proofs.

## Related material in vault

- Extends: `[[sohrabi-myasnikov-2020]]` — direct field-coefficient sequel to the ring-of-integers paper; same three-group trichotomy ($\text{SL}_n$/$\text{GL}_n$/$\text{T}_n$), same cocycle-deformation classification machinery for $\text{T}_n$, explicitly cited as prior work.
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: `[[Concepts/bi-interpretability]]` — sixth paper in the vault to substantively engage with bi-interpretability; strengthens the ring-case result to *regular* bi-interpretability for $\text{SL}_n(F)$.
- Cites: `[[sohrabi-myasnikov-2020]]`
- Cited by (in vault): (none)
- Sibling math-logic notes: `[[kharlampovich-myasnikov-sohrabi-2021]]` — shares author Myasnikov and Sohrabi's richness/bi-interpretability-with-$\mathbb{Z}$ program; the $\text{SL}_n(F)$ result here is a natural candidate for a future richness argument (bi-interpretability with $F$, and if $F \equiv \mathbb{Z}$-rich, richness of $\text{SL}_n(F)$) though this paper does not itself invoke the richness terminology; `[[daniyarova-myasnikov-2025]]` / `[[daniyarova-myasnikov-2026]]` / `[[darienzo-pagano-mcinnis-2020]]` — the vault's other bi-interpretability papers, connected at the concept level via the shared `[[Concepts/bi-interpretability]]` hub rather than direct citation.

---

## Notation conventions

Group/field notation in this note ($\text{SL}_n$, $\text{GL}_n$, $\text{T}_n$, cocycle expressions $S^2(B_n(L), Z)$) is rendered in LaTeX inline math and plain Unicode prose; no `[[...]]`-style double-bracket expressions requiring backtick-escaping appear, per `[[paper-summary]]` § Notation conventions.
