---
title: "Elementary coordinatization of finitely generated nilpotent groups"
authors: A.G. Myasnikov, Mahmood Sohrabi
year: 2013
venue: arxiv
url: https://arxiv.org/abs/1311.1391
url_translated:
language: en
domain: math-logic
status: draft
methodology_type: theoretical
citation_count: 11
citation_count_date: 2026-08-22
key_concepts: []
extends:
  - "[[myasnikov-sohrabi-2010]]"
contradicts: []
replicates: []
cites:
  - "[[myasnikov-sohrabi-2010]]"
cited_by: []
quality_notes: "arXiv preprint (math.GR primary, math.LO secondary); v1 submitted 2013-11-06, v2 2014-10-08, v3 2016-05-17 (this summary covers v3). No journal venue found — appears to remain an arXiv-only preprint despite 11 citations (Semantic Scholar, 2026-08-22) and over a decade of circulation. Ninth `#domain/math-logic` paper in the vault at its own ingest; `[[myasnikov-sohrabi-2010]]` (the authors' 'Groups elementarily equivalent to a free nilpotent group of finite rank', published in Annals of Pure and Applied Logic 162(11), 2011, 916-933) was ingested afterward and is chronologically earlier (submitted 2010 vs. 2013) — this paper generalizes that one's free-nilpotent-group classification and 'abelian deformation' terminology to arbitrary finitely generated nilpotent groups; the `extends`/`cites` link is inferred from shared authors, shared distinctive terminology, and direct technical generalization rather than a confirmed in-text citation quote. This paper proves ℤ is *interpretable* (uniformly, w.r.t. Th(G)) in finitely generated non-abelian-by-finite nilpotent groups, but does NOT prove or claim bi-interpretability, and does not discuss QFA or richness — `key_concepts` deliberately omits `[[Concepts/bi-interpretability]]` since the paper stops short of that stronger property; see 'Why this paper matters' for the connection to `[[kharlampovich-myasnikov-sohrabi-2021]]`'s later finding that nilpotent groups are NOT rich."
author: brett-b
tags:
  - agent/research
  - user/brett-b
  - domain/math-logic
  - topic/model-theory
  - topic/interpretability-theory
  - topic/elementary-equivalence
  - topic/nilpotent-groups
  - topic/definability
  - topic/group-cohomology
  - paper
  - status/draft
---

# Elementary coordinatization of finitely generated nilpotent groups

## Abstract

> "This paper has two main parts. In the first part we develop an elementary coordinatization for any nilpotent group G taking exponents in a binomial principal ideal domain (PID) A. In case that the additive group $A^+$ of A is finitely generated we prove using a classical result of Julia Robinson that one can obtain a central series for G where the action of the ring of integers $\mathbb{Z}$ on the quotients of each of the consecutive terms of the series except for one very specific gap, called the special gap, is interpretable in G. Then we use a refinement of this central series to give a criterion for elementary equivalence of finitely generated nilpotent groups in terms of the relationship between group extensions and the second cohomology group."

*(Verbatim abstract, arXiv:1311.1391v3.)*

## TL;DR

Builds a general-purpose technical toolkit — "elementary coordinatization" — for recovering ring-scalar structure from a nilpotent group purely by first-order-definable means, then uses it to give a complete algebraic answer to when two finitely generated nilpotent groups are elementarily equivalent (Kargapolov's 1969 question, already known false in the naive form via Zilber's 1971 counterexample). The headline mechanism is cohomological: elementarily-equivalent nilpotent groups are classified as **abelian deformations** of one another (Theorem 2.16), built by re-parametrizing the second-cohomology extension class that presents $G$ as a central extension. For the special subclass of **regular** groups, elementary equivalence collapses all the way to isomorphism (Theorem 2.14) — a QFA-flavored rigidity result, though the paper does not use QFA terminology.

## Problem

The paper states four open problems in §1 for finitely generated nilpotent groups: (1) explain algebraically when two are elementarily equivalent; (2) characterize algebraically *all* groups elementarily equivalent to a given one; (3) characterize which nilpotent groups have $\omega$-stable or finite-Morley-rank elementary theory; (4) describe axioms for $\text{Th}(G)$ algebraically. Prior work had shown free nilpotent groups are rigid (Tarski: isomorphic iff elementarily equivalent), Kargapolov (1969) asked whether this held generally, and Zilber (1971) answered no by constructing non-isomorphic elementarily-equivalent 2-nilpotent groups; Oger later gave an algebraic characterization via direct products with $\mathbb{Z}$, using different techniques. This paper addresses Problem 1 fully (and gives partial machinery toward 2), leaving Problems 2 (in full generality), 3, and 4 explicitly for future work.

## Approach

1. **Central series and the special gap** (§2): for a central series $G = G_1 \geq \dots \geq G_{n+1} = 1$, constructs the **upper associated series** ($R_i^u = \{x \in G : [x,G] \subseteq [R_i,G]\}$, bottoming out at $Z(G)$) and **lower associated series** ($R_i^l = [R_{i-1},G]$, bottoming out at $G'$). A ring of scalars acts on the quotients of a refined version of these series *except* at one unavoidable gap — the **special gap** ($Z(G) \geq G' \cap Z(G)$ upstairs, $Z(G)\cdot G' \geq G'$ downstairs) — which is "tame" precisely when $Z(G) = \text{Is}(G') \cap Z(G)$ ($\text{Is}$ = isolator).
2. **Bilinearization** (§3): builds a non-degenerate bilinear map $F_R: G/V_R \times R^u \to R^l$ from the commutation structure on the series, then constructs the **largest ring of scalars** $P(F_R)$ via symmetric endomorphisms satisfying explicit conditions, refining the series to minimize where the ring action is undefined.
3. **Interpretability via first-order logic** (§4): proves every term of the refined upper/lower central series, and the acting ring itself, is *uniformly definable in $G$ with respect to $\text{Th}(G)$* — using that finite-width verbal subgroups are definable (Prop. 4.30) and that commutator subgroups of definable subgroups have bounded width (Lemma 4.32). Combined with Julia Robinson's classical definability-of-$\mathbb{Z}$-in-characteristic-0-domains theorem (invoked via Prop. 2.7), this yields definable/interpretable $\mathbb{Z}$-action on (almost) the whole series.
4. **Second-cohomology classification** (§9, culminating in Theorem 2.16): presents $G$ as a central extension $1 \to N(G) \to G \to \bar G \to 1$ (with $N(G) = \text{Is}(G')\cdot Z(G)$), identifies equivalence classes of such extensions with a fixed coupling $\chi$ with elements of $H^2(\bar G, Z(N(G)))$, decomposes this cohomology group as $H^2(\bar G, N_1(G)) \oplus \text{Ext}(M(G)/N(G), G_0)$, and defines **abelian deformations** $\text{Abdef}(G,\bar d,\bar c)$ by re-parametrizing the $\text{Ext}$-summand via explicit integer tuples/matrices.

## Key result

- **Proposition 2.8**: for finitely generated non-abelian-by-finite nilpotent $G$, $\mathbb{Z}$ and its action are interpretable in $G$, uniformly with respect to $\text{Th}(G)$, on all infinite quotients of the refined central series except possibly the special gap.
- **Theorem 2.9 / Corollary 2.10-2.11**: modules and rings with finitely generated additive group are finitely axiomatizable up to isomorphism within their class — the ring-theoretic engine feeding the group-theoretic classification.
- **Theorem 2.12**: an analogous finite-axiomatizability statement for two-sorted algebras $\langle C, A \rangle$ with $C$ finitely generated as an $A$-module.
- **Theorem 2.13** (elementary-equivalence criterion, necessary conditions): if $G \equiv H$ are finitely generated nilpotent, then $G$ embeds in $H$ as a finite-index subgroup, additions correspond ($G_0 \cong H_0$, $G/G_0 \cong H/H_0$), and several isolator-quotient invariants agree ($\text{Is}(G') \cong \text{Is}(H')$, etc.).
- **Theorem 2.14** (regularity ⟹ rigidity): if $G$ is a finitely generated **regular** nilpotent group (i.e. $\text{Is}(G'\cdot Z(G)) = \text{Is}(G')\cdot Z(G)$, equivalently $G \cong G/G_0 \times G_0$ for an addition $G_0$) and $G \equiv H$, then $G \cong H$ — full elementary rigidity for this subclass, first announced without proof in earlier work and proved here.
- **Theorem 2.16** (main classification theorem): if $G$ is finitely generated nilpotent and $H \equiv G$, then $H \cong \text{Abdef}(G, \bar d, \bar c)$ for some tuples $\bar d$, $\bar c$ satisfying the explicit cohomological parametrization of Definition 2.15 — every elementarily-equivalent group is an abelian deformation of $G$.

## Assumptions

- $A$ is a **binomial principal ideal domain**: a characteristic-0 integral domain where $\binom{a}{k}$ is well-defined and unique in $A$ for all $a \in A$, $k \geq 0$ — a first-order property; $\mathbb{Z}$, $\mathbb{Q}$, and any characteristic-0 field qualify.
- $G$ is a finitely generated nilpotent $A$-group (equipped with an exponentiation function $G \times A \to G$ satisfying the Hall-Petresco identities); the paper's main results specialize to $A = \mathbb{Z}$ (ordinary torsion-free finitely generated nilpotent groups).
- $A^+$ (the additive group of $A$) is finitely generated, needed to invoke Julia Robinson's definability-of-$\mathbb{Z}$ theorem.
- Theorem 2.14's rigidity conclusion is restricted to the **regular** subclass; general nilpotent groups exhibit genuine abelian deformations (Theorem 2.16).

## Limitations / scope

- Only Problem 1 (the elementary-equivalence criterion) is fully resolved; Problems 2 (fully general algebraic characterization of the equivalence class), 3 ($\omega$-stability/Morley rank characterization), and 4 (algebraic axiom description) are explicitly left for future work.
- The special gap is a genuine obstruction: the ring action is *not* interpretable there in general, only when the gap is "tame."
- Does not discuss or claim bi-interpretability of nilpotent groups with $\mathbb{Z}$, QFA, or richness (WSOL-equivalence) — the paper's interpretability results are one-directional (interpreting $\mathbb{Z}$-structure in $G$) and stop short of the two-way, definably-invertible bi-interpretability property; `[[kharlampovich-myasnikov-sohrabi-2021]]` (2021, not cited here since it postdates this paper) later establishes that nilpotent groups are in fact *not* rich, consistent with this paper's results not reaching bi-interpretability.
- Restricted to finitely generated nilpotent groups; no claims about general solvable or polycyclic groups.

## Replication evidence

N/A — a theoretical model-theory/group-theory paper with full proofs (11 citations per Semantic Scholar as of ingest, suggesting the results have been used/built on by others, though no explicit independent replication of the theorems was surfaced).

## Why this paper matters

This is the technical foundation the vault's later Myasnikov/Sohrabi bi-interpretability-with-$\mathbb{Z}$ results (`[[sohrabi-myasnikov-2020]]`, `[[myasnikov-sohrabi-2024]]`) build on methodologically, even though it predates and does not itself claim bi-interpretability: the same core move — extract a definable $\mathbb{Z}$-action from a group via careful central-series/interpretability arguments, then classify elementarily-equivalent models via that extracted arithmetic structure — recurs across the whole cluster, here worked out in full technical detail for the nilpotent case via an explicit second-cohomology parametrization (abelian deformations) rather than the transvection/bounded-generation route used for classical linear groups. It also settles a long-open, named question (Kargapolov 1969) with a genuinely satisfying classification (not just a rigidity-or-not dichotomy, but an explicit description of *every* elementarily-equivalent model as a cohomological deformation) — directly analogous in spirit to the "abelian deformation" terminology `[[sohrabi-myasnikov-2020]]` later reuses for $\text{T}_n(\mathcal{O})$, suggesting the authors carried the cohomological-deformation idiom from this nilpotent-group paper into their later classical-matrix-group work. For a vault tracking why some group families are rich (bi-interpretable with a WSOL-collapsing superstructure) and others are not — `[[kharlampovich-myasnikov-sohrabi-2021]]` places nilpotent groups firmly on the "not rich" side of that dichotomy — this paper is the detailed technical evidence for *why*: interpretability of $\mathbb{Z}$ in nilpotent $G$ is real but partial (blocked at the special gap), falling short of the full bi-interpretability that richness requires.

## Quotes

1. > "This paper has two main parts. In the first part we develop an elementary coordinatization for any nilpotent group G taking exponents in a binomial principal ideal domain (PID) A." — Abstract
2. > "...to what extent $G_{\mathbb{Z}}$ can be recovered from $G$" — §1 (per source extraction, paraphrasing the paper's own framing of the coordinatization problem)

## Open questions surfaced

- **Problem 2** (verbatim framing, §1): algebraic characterization of *all* groups elementarily equivalent to an arbitrary finitely generated nilpotent group, in full generality — Theorem 2.16 gives a classification via abelian deformations, but the authors explicitly flag further work remains.
- **Problem 3**: which nilpotent groups have $\omega$-stable or finite-Morley-rank elementary theory — left entirely open here.
- **Problem 4**: an algebraic description of the axiom set for $\text{Th}(G)$ — left entirely open here.
- Whether the interpretability-of-$\mathbb{Z}$-modulo-the-special-gap result here can be strengthened to full bi-interpretability for some sub-class of nilpotent groups (beyond the regular subclass, which already gets full rigidity) — not addressed by this paper or, per its abstract, by `[[kharlampovich-myasnikov-sohrabi-2021]]`, which instead shows nilpotent groups generally are not rich.

## Related material in vault

- Extends: `[[myasnikov-sohrabi-2010]]` — generalizes that paper's free-nilpotent-group classification and "abelian deformation" terminology to arbitrary finitely generated nilpotent groups (link inferred from shared authors/terminology/technique, not a confirmed in-text citation).
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (none — deliberately does not link `[[Concepts/bi-interpretability]]`; see `quality_notes` for why)
- Cites: `[[myasnikov-sohrabi-2010]]`; also cites Tarski, Kargapolov, Zilber, Oger, and Julia Robinson's classical definability theorem, none of which are separate vault entries.
- Cited by (in vault): (none)
- Sibling math-logic notes: `[[sohrabi-myasnikov-2020]]` — shares author Myasnikov and Sohrabi, reuses "abelian deformation" terminology for a structurally different setting ($\text{T}_n(\mathcal{O})$'s cocycle-parametrized models rather than nilpotent groups' cohomology-parametrized models), and is the paper's methodological successor in the bi-interpretability-with-$\mathbb{Z}$ program this paper's interpretability results feed into; `[[kharlampovich-myasnikov-sohrabi-2021]]` — states nilpotent groups are not rich, the natural "so what happens beyond mere interpretability" follow-up to this paper's partial ($\mathbb{Z}$-interpretable-but-not-bi-interpretable) result; `[[myasnikov-sohrabi-2024]]` and `[[daniyarova-myasnikov-2024]]` — the vault's other elementary-equivalence-classification-via-interpretability results, for classical linear groups and the Baumslag-Solitar group respectively.

---

## Notation conventions

Group/cohomology notation in this note ($H^2(\bar G, Z(N(G)))$, central-series subscripts/superscripts, isolator notation $\text{Is}(\cdot)$) is rendered in LaTeX inline math and plain Unicode prose; no `[[...]]`-style double-bracket expressions requiring backtick-escaping appear, per `[[paper-summary]]` § Notation conventions.
