---
title: "Bi-interpretability with $\mathbb{Z}$ and models of the complete elementary theories of $\text{SL}_n(\mathcal{O})$, $\text{T}_n(\mathcal{O})$ and $\text{GL}_n(\mathcal{O})$, $n\geq 3$"
authors: Mahmood Sohrabi, Alexei G. Myasnikov
year: 2020
venue: arxiv
url: https://arxiv.org/abs/2004.03585
url_translated:
language: en
domain: math-logic
status: draft
methodology_type: theoretical
citation_count: 3
citation_count_date: 2026-08-22
key_concepts:
  - "[[Concepts/bi-interpretability]]"
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[myasnikov-sohrabi-2024]]"
quality_notes: "arXiv preprint (math.GR primary, math.LO secondary), v1 submitted 2020-04-07, 19 pages, admin note: text overlap with arXiv:1609.09802 (the authors' own earlier paper). Published as Miasnikov, A.G. & Sohrabi, M., 'Complete first-order theories of some classical matrix groups over algebraic integers', Journal of Algebra 582 (2021), 206-231 — citation_count above (3, as of 2026-08-22) is Semantic Scholar's count for that published version, since it had no separate entry for the arXiv preprint. Fourth `#domain/math-logic` paper in the vault, and the first written by Myasnikov alone rather than with Daniyarova — shares the QFA/bi-interpretability-with-ℤ theme of `[[daniyarova-myasnikov-2025]]`, which cites the closely related Nies-Sohrabi QFA literature (same Sohrabi) in its own background section, though no direct citation link between the two papers has been found."
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
  - topic/number-theory
  - paper
  - status/draft
---

# Bi-interpretability with $\mathbb{Z}$ and models of the complete elementary theories of $\text{SL}_n(\mathcal{O})$, $\text{T}_n(\mathcal{O})$ and $\text{GL}_n(\mathcal{O})$, $n\geq 3$

## Abstract

> "Let $\mathcal{O}$ be the ring of integers of a number field, and let $n\geq 3$. This paper studies bi-interpretability of the ring of integers $\mathbb{Z}$ with the special linear group $\text{SL}_n(\mathcal{O})$, the general linear group $\text{GL}_n(\mathcal{O})$ and solvable group of all invertible uppertriangular matrices over $\mathcal{O}$, $\text{T}_n(\mathcal{O})$. For each of these groups we provide a complete characterization of arbitrary models of their complete elementary theories."

*(Verbatim abstract, arXiv:2004.03585v1.)*

## TL;DR

For every ring of integers $\mathcal{O}$ of a number field and every $n \geq 3$, this paper pins down exactly which groups can be elementarily equivalent to $\text{SL}_n(\mathcal{O})$, $\text{GL}_n(\mathcal{O})$, and $\text{T}_n(\mathcal{O})$ (upper-triangular invertible matrices) — by proving bi-interpretability with $\mathbb{Z}$ (for $\text{SL}_n$, unconditionally) and by classifying every model up to a controlled family of "deformations" (for $\text{T}_n$ and $\text{GL}_n$). $\text{SL}_n(\mathcal{O})$ comes out fully rigid (QFA + prime); $\text{T}_n(\mathcal{O})$ can have infinitely many pairwise non-isomorphic elementarily-equivalent models when $\mathcal{O}^\times$ is infinite, classified via a novel "coboundary-on-torsion" 2-cocycle condition.

## Problem

Whether elementary equivalence forces isomorphism for finitely generated groups is, in general, false — but a growing list of examples (nilpotent and polycyclic groups, free metabelian groups, $\mathbb{Z}$, polynomial rings $\mathbb{Z}[x_1,\dots,x_m]$, finitely generated fields of characteristic $\neq 2$) turn out to be **first-order rigid**: any finitely generated group elementarily equivalent to them is isomorphic to them, often via quasi-finite axiomatizability (QFA). Lubotzky, Mok and Rovinsky had proved first-order rigidity for $\text{SL}_n(\mathbb{Z})$, $n \geq 3$, and announced (but did not publish) a QFA proof. This paper asks the sharper structural question for the whole family $\text{SL}_n(\mathcal{O})$, $\text{GL}_n(\mathcal{O})$, $\text{T}_n(\mathcal{O})$ over an arbitrary ring of integers $\mathcal{O}$: not just *are these groups rigid*, but *bi-interpretable with $\mathbb{Z}$*, and — where bi-interpretability fails or is only partial — what exactly do the elementarily-equivalent-but-non-isomorphic models look like?

## Approach

Three parallel case studies, §2-§4:

1. **$\text{SL}_n(\mathcal{O})$** (§2): shows the transvection one-parameter subgroups $T_{ij}$ are definable via centralizer computations (Lemma 2.1), and that the two-sorted module structure $T_{ij}^{\mathcal{O}}$ is interpretable inside the group alone (Lemma 2.3). Uses bounded generation of $\text{SL}_n(\mathcal{O})$ (every element is a bounded-length product of transvections) plus a fixed ordering on transvection products to build a group-definable isomorphism $\varphi: G \to \tilde G$ for any $G \equiv \text{SL}_n(\mathcal{O})$, yielding full bi-interpretability with $\mathcal{O}$ (hence with $\mathbb{Z}$).
2. **$\text{T}_n(\mathcal{O})$** (§3): splits on whether $\mathcal{O}^\times$ is finite or infinite. Finite-units case parallels the $\text{SL}_n$ argument via definable subgroups $d_k(\mathcal{O}^\times)$. Infinite-units case is the paper's most technical: introduces **abelian deformations** $T_n(R, \bar f)$ parametrized by symmetric 2-cocycles on $R^\times$, shows the derived subgroup is uniformly definable, proves every model must be such a deformation with each $f_i$ **coboundary on torsion (CoT)**, and uses ultraproduct/pure-injectivity machinery (Theorem 3.14) to show CoT cocycles collapse to genuine coboundaries in $\aleph_1$-saturated models.
3. **$\text{GL}_n(\mathcal{O})$** (§4): reduces to the $\text{SL}_n$ result via the derived subgroup, defines tori $\Delta_i = d_i(\mathcal{O}^\times)\cdot Z(G)$ from conjugation relations, and rules out any nontrivial torus-splitting cocycle using cross-ratio-type relations between pairs of tori — concluding every model has the un-deformed form $\text{GL}_n(R)$.

## Key result

- **Theorem 2.4**: $\mathcal{O}$ and $(\text{SL}_n(\mathcal{O}), \bar t)$ are bi-interpretable (with the transvection tuple $\bar t$ as parameters); hence $\mathbb{Z}$ and $(\text{SL}_n(\mathcal{O}), \bar t(\bar\beta))$ are bi-interpretable.
- **Corollary 2.5**: $\text{SL}_n(\mathcal{O})$ is QFA and prime, for any ring of integers $\mathcal{O}$ and any $n \geq 3$.
- **Theorem 2.6** (model classification for $\text{SL}_n$): if $H \equiv \text{SL}_n(\mathcal{O})$ in $\mathcal{L}_\text{groups}$, then $H \cong \text{SL}_n(R)$ for some ring $R \equiv \mathcal{O}$.
- **Theorem 3.6** ($\text{T}_n$, finite units): if $H \equiv \text{T}_n(\mathcal{O})$ and $|\mathcal{O}^\times| < \infty$, then $H \cong T_n(R)$ for some $R \equiv \mathcal{O}$.
- **Theorem 3.12** ($\text{T}_n$, infinite units, necessity): if $H \equiv \text{T}_n(\mathcal{O})$, then $H \cong T_n(R, \bar f)$ for some $R \equiv \mathcal{O}$ and coboundary-on-torsion 2-cocycles $\bar f$.
- **Theorem 3.17** ($\text{T}_n$, sufficiency): any $T_n(R, \bar f)$ with $R \equiv \mathcal{O}$ and each $f_i$ CoT is itself elementarily equivalent to $\text{T}_n(\mathcal{O})$ — so Theorem 3.12's classification is exact, not just an upper bound.
- **Theorem 4.5** (model classification for $\text{GL}_n$): if $H \equiv \text{GL}_n(\mathcal{O})$, then $H \cong \text{GL}_n(R)$ for some $R \equiv \mathcal{O}$ (no nontrivial deformation survives, unlike $\text{T}_n$).

## Assumptions

- $\mathcal{O}$ is the ring of integers of a number field $F$ (finite extension of $\mathbb{Q}$); $\beta_1, \dots, \beta_m$ are free $\mathbb{Z}$-module generators of $\mathcal{O}$.
- $n \geq 3$ throughout — needed for bounded generation and the transvection-generation properties the definability arguments rely on; $n = 2$ is explicitly excluded.
- Groups are studied in the first-order language of groups $\mathcal{L}_\text{groups}$; rings in the first-order language of unitary commutative rings $\mathcal{L}_\text{rings}$.
- No restriction on whether $\mathcal{O}^\times$ is finite or infinite, but the $\text{T}_n$ and (implicitly) $\text{GL}_n$ arguments case-split on this.

## Limitations / scope

- Results restricted to $n \geq 3$; the $n = 2$ case is a genuinely different (and unaddressed) problem since bounded generation fails.
- $\text{GL}_n(\mathcal{O})$ with infinite units is **not** bi-interpretable with $\mathbb{Z}$ (Theorem 4.4) even though every model still has the clean form $\text{GL}_n(R)$ — bi-interpretability and full model-classification are shown to come apart here.
- $\text{T}_n(\mathcal{O})$ with infinite units genuinely admits infinitely many pairwise non-isomorphic elementarily-equivalent models (the abelian deformations) — the paper's clean rigidity results for $\text{SL}_n$ do not generalize to the solvable case.
- The integral Heisenberg group $UT_3(\mathbb{Z})$ is noted as QFA but *not* bi-interpretable with $\mathbb{Z}$ — evidence that bi-interpretability is a strictly stronger property than QFA, used by the authors to justify why the paper's stronger bi-interpretability route (rather than a direct QFA argument) is worth the extra machinery.
- Explicitly restricted to $\mathcal{O}$ a ring of integers; the authors state a sequel is planned replacing $\mathcal{O}$ with a field $F$ (number field, general finitely generated field, or algebraically closed field).

## Replication evidence

N/A — a pure model-theoretic/algebraic paper with full proofs (no computational or empirical claims to replicate). The result was subsequently published in peer-reviewed form (Journal of Algebra 582, 2021) under a different title; no independent replication of the theorems by other authors has been surfaced at ingest.

## Why this paper matters

This is the paper Lubotzky-Mok-Rovinsky's earlier first-order-rigidity result for $\text{SL}_n(\mathbb{Z})$ had promised but not delivered: a full bi-interpretability proof, extended from $\mathbb{Z}$ to arbitrary number rings $\mathcal{O}$ and from $\text{SL}_n$ alone to the whole triangle of classical linear groups $\text{SL}_n$/$\text{GL}_n$/$\text{T}_n$. Its central methodological payoff — worked out concretely here rather than left abstract — is that bi-interpretability with $\mathbb{Z}$ is not an all-or-nothing property of a "family" of groups: $\text{SL}_n(\mathcal{O})$ gets it outright, $\text{GL}_n(\mathcal{O})$ loses it exactly when units are infinite (while still keeping a clean model classification), and $\text{T}_n(\mathcal{O})$ loses both, spawning a genuine infinite family of non-isomorphic elementarily-equivalent models classified by a purpose-built cocycle condition (CoT). For a vault already tracking the Daniyarova-Myasnikov "Theory of Interpretations" series and its Concepts hub on bi-interpretability, this paper is the concrete worked case those foundational papers gesture at in the abstract: Daniyarova-Myasnikov's Paper I explicitly cites the Khélif-Nies QFA-bi-interpretability connection and the closely related Nies-Sohrabi QFA literature as motivating background, and this paper (co-authored by the same Sohrabi) is the fullest published execution of that program against a specific, important family of arithmetic groups.

## Quotes

1. > "This paper studies bi-interpretability of the ring of integers $\mathbb{Z}$ with the special linear group $\text{SL}_n(\mathcal{O})$..." — Abstract
2. > "In a sequel to this paper we study the relevant questions, when $\mathcal{O}$ is replaced by a field $F$..." — §1 (future work)

## Open questions surfaced

- The stated sequel direction: extend the bi-interpretability and model-classification results from $\mathcal{O}$ (ring of integers) to a field $F$ — a number field, a general finitely generated field, or an algebraically closed field. **Delivered**: `[[myasnikov-sohrabi-2024]]` carries out exactly this extension, proving *regular* bi-interpretability of $\text{SL}_n(F)$ with $F$ (strengthening this paper's plain bi-interpretability result) and classifying models of $\text{T}_n(F)$/$\text{GL}_n(F)$ via the same cocycle-deformation machinery adapted to fields.
- The $n = 2$ case is left entirely open — bounded generation, the key technical engine here, fails for $\text{SL}_2(\mathcal{O})$ and $\text{GL}_2(\mathcal{O})$, so the paper's methods don't transfer without new ideas.
- Whether the "coboundary-on-torsion" cocycle condition characterizing $\text{T}_n(\mathcal{O})$'s models is itself a special case of a more general deformation-classification framework applicable to other solvable linear groups, or an ad hoc device specific to upper-triangular matrices — not addressed by the paper.

## Related material in vault

- Extends: (none in vault)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: `[[Concepts/bi-interpretability]]` — fourth paper in the vault to substantively engage with bi-interpretability; concept hub updated to include this paper's arithmetic-group worked case alongside the Daniyarova-Myasnikov and D'Arienzo-Pagano-McInnis theoretical treatments.
- Cites: (none confirmed as in-vault papers; the Nies-Sohrabi QFA literature it shares with `[[daniyarova-myasnikov-2025]]`'s background section is not itself a separate vault entry)
- Cited by (in vault): `[[myasnikov-sohrabi-2024]]` — the field-coefficient sequel, extending this paper's ring-of-integers results to arbitrary fields $F$.
- Sibling math-logic notes: `[[myasnikov-sohrabi-2013]]` — same two authors, the methodological predecessor: works out $\mathbb{Z}$-interpretability and an "abelian deformation" elementary-equivalence classification for finitely generated nilpotent groups via second cohomology, the same cohomological-deformation idiom this paper reuses (with a cocycle rather than cohomology-class parametrization) for $\text{T}_n(\mathcal{O})$; `[[kharlampovich-myasnikov-sohrabi-2021]]` — shares two of three authors (Myasnikov, Sohrabi); systematizes this paper's $\text{SL}_n(\mathcal{O})$ bi-interpretability-with-$\mathbb{Z}$ result as one case study inside a broader "richness" framework (bi-interpretability with the hereditary-finite-set superstructure $HF(G)$), locating it in a hyperbolic-vs-nilpotent spectrum of finitely generated groups; `[[daniyarova-myasnikov-2025]]` — cites the same Khélif-Nies QFA-bi-interpretability connection and the related Nies-Sohrabi literature (this paper's co-author Sohrabi) in its own background, though no direct citation link between the two papers has been found; `[[daniyarova-myasnikov-2026]]` and `[[darienzo-pagano-mcinnis-2020]]` — both give abstract categorical characterizations of bi-interpretability that this paper's concrete arithmetic-group construction (transvection definability, bounded generation, cocycle deformations) could in principle be recast through, though neither series references the other.

---

## Notation conventions

Group/ring notation in this note (subscripts, superscripts, $\text{SL}_n$/$\text{GL}_n$/$\text{T}_n$) is rendered in LaTeX inline math and plain Unicode prose; no `[[...]]`-style double-bracket expressions requiring backtick-escaping appear, per `[[paper-summary]]` § Notation conventions.
