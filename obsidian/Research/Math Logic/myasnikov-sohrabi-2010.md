---
title: "Groups elementarily equivalent to a free nilpotent group of finite rank"
authors: A.G. Myasnikov, Mahmood Sohrabi
year: 2010
venue: arxiv
url: https://arxiv.org/abs/1006.0290
url_translated:
language: en
domain: math-logic
status: draft
methodology_type: theoretical
citation_count:
citation_count_date: 2026-08-22
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[myasnikov-sohrabi-2013]]"
quality_notes: "arXiv preprint (math.GR primary, math.LO secondary, MSC 03C60/20F18), v1 submitted 2010-06-02, single version, 24KB. Published as Myasnikov, A.G. & Sohrabi, M., Annals of Pure and Applied Logic 162(11) (2011), 916-933 (DOI 10.1016/j.apal.2011.04.003). Citation count not verified at ingest — Semantic Scholar's API returned HTTP 429 (rate-limited) on all attempts; no count recorded rather than guessed. Tenth `#domain/math-logic` paper in the vault, and — together with `[[myasnikov-sohrabi-2013]]` — the earliest pair in the vault's Myasnikov/Sohrabi cluster: this paper (2010) covers free nilpotent groups of arbitrary finite rank $r$ and class $c$, generalizing the authors' own still-earlier paper on free 2-nilpotent groups ($r=2$, $c=2$; published separately in Algebra and Logic, not yet in this vault); `[[myasnikov-sohrabi-2013]]` then generalizes the technique from free nilpotent groups to arbitrary finitely generated nilpotent groups, reusing this paper's 'abelian deformation' terminology and central-series/interpretability machinery almost verbatim. The `extends`/`cites` link to the 2013 paper is inferred from shared authors, shared distinctive terminology, and direct technical generalization rather than a confirmed in-text citation quote — flagged as strongly plausible, not verbatim-confirmed."
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

# Groups elementarily equivalent to a free nilpotent group of finite rank

## Abstract

> "In this paper we give a complete algebraic description of groups elementarily equivalent to a given free nilpotent group of finite rank."

*(Verbatim abstract, arXiv:1006.0290v1.)*

## TL;DR

Gives a complete classification of all groups elementarily equivalent to a P. Hall completion $N_{r,c}(R)$ of a free nilpotent group of rank $r \geq 2$, class $c \geq 2$, over a binomial domain $R$ (e.g. $R = \mathbb{Z}$): every such group $H$ is an **abelian deformation** $N_{r,c}(S, \bar f)$, built by replacing the group's product-on-the-center with a symmetric-2-cocycle-modified version, for some ring $S \equiv R$ (Theorem 1.1), and conversely every abelian deformation of $N_{r,c}(S)$ for $S \equiv R$ actually *is* elementarily equivalent to $N_{r,c}(R)$ (Theorem 1.2) — a genuine if-and-only-if classification. Theorem 1.3 shows this is not vacuous: explicit abelian deformations exist that are elementarily equivalent to, but not isomorphic to, any Hall completion of the free group itself.

## Problem

Mal'cev showed free solvable/nilpotent groups of finite rank are elementarily rigid (elementary equivalence implies isomorphism), because the abelianization $G/[G,G]$ is first-order definable. Kargapolov's conjecture that this holds for *all* finitely generated nilpotent groups was refuted by Zilber; Myasnikov-Remeslennikov later showed the conjecture holds "essentially" for nilpotent $\mathbb{Q}$-groups; Oger gave a characterization for general finitely generated nilpotent groups via $G \times \mathbb{Z} \cong H \times \mathbb{Z}$ ("essential isomorphism"); Belegradek fully characterized the elementary-equivalence class of $UT_n(\mathbb{Z})$ for $n \geq 3$. This paper asks the sharper structural question, in the spirit of Belegradek but via a different, more global technique: for a *free* nilpotent group of finite rank and class, what exactly are the groups elementarily equivalent to it, described algebraically rather than merely characterized by an equivalence relation?

## Approach

1. **Lazard Lie-ring interpretation** (§2.1): builds the Lie ring $\text{Lie}(G)$ from $G$'s lower central series and the commutator bracket, giving a bilinear map $f_G: \mathcal{N}/Z(\mathcal{N}) \times \mathcal{N}/Z(\mathcal{N}) \to \mathcal{N}^2$; shows $\text{Lie}(G)$ is *absolutely* interpretable in $G$ (Lemma 2.9) — a stronger, parameter-free interpretability than the "uniform with respect to Th(G)" interpretability used in the authors' later, more general 2013 paper.
2. **Ring recovery via bilinear-map theory** (Theorem 2.6/2.7): applies the general theorem that a bilinear map $f$ has a *largest ring of scalars* $P(f)$ with respect to which $f$ stays bilinear, and that the resulting scalar-structure is absolutely interpretable in the bilinear-map structure; shows $R \cong P(f_{\text{Lie}(G)})$, recovering the coefficient ring from the group.
3. **Module-action recovery and basic sequences** (Theorem 2.11, Corollaries 2.13-2.14): proves $R$'s action on each successive lower-central-series quotient $\Gamma_i(G)/\Gamma_{i+1}(G)$ is absolutely interpretable in $G$, and that Hall basic sequences (and their defining relations) are first-order expressible.
4. **Abelian-deformation reconstruction and sufficiency** (§2.2, §3): reconstructs $G$ as a central extension parametrized by symmetric 2-cocycles $f^1,\dots,f^r: R^+ \times R^+ \to \bigoplus R^+$ acting only on the highest-weight relations, then uses ultrapowers/saturation to show every abelian deformation of $N_{r,c}(S)$ for $S \equiv R$ is genuinely elementarily equivalent to $N_{r,c}(R)$ — the converse direction completing the classification.
5. **Explicit non-triviality witness** (§4): constructs, using a ring due to Belegradek with $\text{Ext}(R^+,R^+) \neq 0$, an abelian deformation that is elementarily equivalent to but not isomorphic to any Hall completion of the free nilpotent group.

## Key result

- **Theorem 1.1** (necessity, the classification's main direction): if $G = N_{r,c}(R)$ and $H \equiv G$, then $H$ is an abelian deformation of $N_{r,c}(S)$ for some ring $S \equiv R$.
- **Theorem 1.2** (sufficiency): if $S \equiv R$, then any abelian deformation of $N_{r,c}(S)$ is elementarily equivalent to $N_{r,c}(R)$ — together with Theorem 1.1, a full if-and-only-if characterization.
- **Theorem 1.3** (genuine non-triviality): there exists a binomial domain $R \equiv \mathbb{Z}$ and, for every $r,c \geq 2$, an abelian deformation $H$ of $N_{r,c}(R)$ not isomorphic to any Hall completion of $N_{r,c}(\mathbb{Z})$ — the classification produces real, non-isomorphic elementarily-equivalent models, not just a formally-possible-but-empty class.
- **Lemma 2.9 / Theorem 2.7**: $\text{Lie}(G)$ is absolutely interpretable in $G$, and the coefficient ring $R$ is recovered as $P(f_{\text{Lie}(G)})$ (the largest ring of scalars for the Lie bracket's bilinear map).
- **Theorem 2.11**: $R$'s action on each lower-central-series quotient $\Gamma_i(G)/\Gamma_{i+1}(G)$ is absolutely interpretable in $G$.

## Assumptions

- $R$ is a **binomial domain**: a characteristic-0 integral domain in which $\binom{a}{k}$ is uniquely defined in $R$ for every $a \in R$, $k \geq 0$ (needed for Hall's canonical polynomials to be well-defined over $R$).
- Rank $r \geq 2$, nilpotency class $c \geq 2$; the special case $r=2,c=2$ was already covered by the authors' earlier, separate paper on free 2-nilpotent groups.
- Groups are finitely generated as $R$-groups.
- $G = N_{r,c}(R)$ specifically denotes the **P. Hall completion** of the free $R$-nilpotent group of rank $r$, class $c$ — not an arbitrary finitely generated nilpotent group (that generalization is left to the authors' later `[[myasnikov-sohrabi-2013]]`).

## Limitations / scope

- Restricted to *free* nilpotent groups (Hall completions thereof), not arbitrary finitely generated nilpotent groups — the authors explicitly flag that "the full classification problem for finitely generated nilpotent groups is currently wide open," addressed only later and only partially (via a different, more general coordinatization technique) in `[[myasnikov-sohrabi-2013]]`.
- The interpretability results here are **absolute** (parameter-free) rather than merely "uniform with respect to Th(G)" — a stronger property than the later, more general nilpotent-group paper achieves, but only because the free-nilpotent setting is more structured.
- Does not discuss or claim bi-interpretability; the ring $R$ is shown definable/interpretable in $G$, but no two-way, definably-invertible bi-interpretation is established or claimed.
- New results only for $r > 2$ or $c > 2$; the authors state the $r=2,c=2$ case was already known from their earlier work.

## Replication evidence

N/A — a theoretical model-theory/group-theory paper with full proofs. Published in peer-reviewed form (Annals of Pure and Applied Logic, 2011) alongside the arXiv preprint; no independent replication of the specific theorems surfaced at ingest.

## Why this paper matters

This is the direct technical predecessor to `[[myasnikov-sohrabi-2013]]`: the same authors, the same "abelian deformation via symmetric 2-cocycle" classification idiom, and largely the same Lie-ring/bilinear-map interpretability machinery, here worked out for the cleaner special case of *free* nilpotent groups (where interpretability is absolute) before being generalized — with a genuinely more difficult "uniform w.r.t. Th(G)" interpretability argument and an explicit "special gap" obstruction — to arbitrary finitely generated nilpotent groups in the 2013 paper. Read together, the two papers show a clear research arc: solve the clean case completely and constructively (this paper), then push the same cohomological-deformation idea as far as it will go into the general case (2013), accepting a weaker interpretability guarantee and an explicit obstruction (the special gap) as the price of generality. Theorem 1.3's explicit construction — genuine non-isomorphic elementarily-equivalent models of a free nilpotent group — is also independently useful as a concrete counterexample resource for anyone reasoning about how much elementary equivalence actually constrains nilpotent-group structure.

## Quotes

1. > "In this paper we give a complete algebraic description of groups elementarily equivalent to a given free nilpotent group of finite rank." — Abstract
2. > "The action of R on each of the quotients $\Gamma_i(G)/\Gamma_{i+1}(G)$ is absolutely interpretable in G." — Theorem 2.11 (per source extraction)

## Open questions surfaced

- The full classification problem for **arbitrary** finitely generated nilpotent groups (not just free ones) — explicitly flagged by the authors as "currently wide open" at the time of this paper; substantially, though not completely, addressed later in `[[myasnikov-sohrabi-2013]]`.
- Which abelian deformations of $N_{r,c}(S)$ (for $S \equiv R$) are actually *realizable* as genuine groups versus merely formal constructions, and — separately — which pairs of realizable deformations are themselves isomorphic to each other: the authors note the classification has these two distinct sub-problems, not fully disentangled here.
- Whether the absolute (parameter-free) interpretability achieved here for free nilpotent groups can be preserved, rather than weakened to "uniform w.r.t. Th(G)," in some broader subclass of general finitely generated nilpotent groups.

## Related material in vault

- Extends: (none in vault — earliest full paper by submission date in the vault's Myasnikov/Sohrabi nilpotent-group sub-cluster; itself extends an even earlier free-2-nilpotent-group paper, published in Algebra and Logic, not yet in this vault)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (none — does not engage with bi-interpretability; interpretability here is one-directional and absolute, see `quality_notes`)
- Cites: (none confirmed as in-vault papers; cites Mal'cev, Zilber, Myasnikov-Remeslennikov, Oger, Belegradek, none of which are separate vault entries)
- Cited by (in vault): `[[myasnikov-sohrabi-2013]]` — generalizes this paper's free-nilpotent-group classification and "abelian deformation" terminology to arbitrary finitely generated nilpotent groups (link inferred from shared authors/terminology/technique, not a confirmed in-text citation — see `quality_notes`).
- Sibling math-logic notes: `[[sohrabi-myasnikov-2020]]` — shares author Myasnikov (and Sohrabi), and reuses "abelian deformation" terminology for a structurally different setting ($\text{T}_n(\mathcal{O})$'s cocycle-parametrized models); `[[kharlampovich-myasnikov-sohrabi-2021]]` — the richness framework that later situates nilpotent groups (this paper's subject) as explicitly *not* rich, consistent with this paper's interpretability results being absolute-but-one-directional rather than bi-interpretable.

---

## Notation conventions

Group/Lie-ring notation in this note ($N_{r,c}(R)$, $\text{Lie}(G)$, lower-central-series terms $\Gamma_i(G)$, bilinear maps $f_G$) is rendered in LaTeX inline math and plain Unicode prose; no `[[...]]`-style double-bracket expressions requiring backtick-escaping appear, per `[[paper-summary]]` § Notation conventions.
