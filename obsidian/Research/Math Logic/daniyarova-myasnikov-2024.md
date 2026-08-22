---
title: "Groups elementarily equivalent to metabelian Baumslag-Solitar groups and regular bi-interpretability"
authors: Evelina Daniyarova, Alexei Myasnikov
year: 2024
venue: arxiv
url: https://arxiv.org/abs/2407.00642
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
quality_notes: "arXiv preprint (math.GR primary, math.LO secondary), v1 submitted 2024-06-30, single version. Published as Daniyarova, E. & Myasnikov, A., Annals of Pure and Applied Logic 177(5) (2026), Article 103695. Citation count not verified at ingest — Semantic Scholar's API returned HTTP 429 (rate-limited) on repeated attempts; no count recorded rather than guessed. Seventh `#domain/math-logic` paper in the vault, co-authored by the same Daniyarova-Myasnikov pair as `[[daniyarova-myasnikov-2025]]` (Paper I of the 'Theory of Interpretations' series) and `[[daniyarova-myasnikov-2026]]` (Paper II) — chronologically this paper (submitted 2024-06-30) *predates* both, so it cannot cite them, but Paper I lists Baumslag-Solitar groups BS(1,k) among its worked examples (Example list, §6) using the same regular-interpretability/regular-bi-interpretability terminology this paper develops in full; whether Paper I explicitly cites this paper as the source of that worked example could not be confirmed from the fetched source (bibliography not reachable via the tool used) — flagged for a future closer read rather than asserted as a confirmed citation link."
author: brett-b
tags:
  - agent/research
  - user/brett-b
  - domain/math-logic
  - topic/bi-interpretability
  - topic/model-theory
  - topic/interpretability-theory
  - topic/elementary-equivalence
  - topic/quasi-finite-axiomatizability
  - topic/baumslag-solitar-groups
  - topic/metabelian-groups
  - topic/non-standard-models
  - paper
  - status/draft
---

# Groups elementarily equivalent to metabelian Baumslag-Solitar groups and regular bi-interpretability

## Abstract

> "We prove that metabelian Baumslag$-$Solitar group $BS(1,k)$, $k>1$, is (strongly) regularly bi-interpretable with the ring of integers $\mathbb{Z}$, and describe in algebraic terms all groups that are elementarily equivalent to $BS(1,k)$."

*(Verbatim abstract, arXiv:2407.00642v1.)*

## TL;DR

Solves the first-order classification problem for the metabelian Baumslag-Solitar groups $BS(1,k)$, $k > 1$ — a fundamental, well-studied example in combinatorial/geometric group theory whose elementary theory was already known to be undecidable (Noskov) and QFA. The paper strengthens a known parametrized bi-interpretability (Khélif 2003) to full **regular strong bi-interpretability with $\mathbb{Z}$**, then uses that to prove every group elementarily equivalent to $BS(1,k)$ is a genuine non-standard model $BS(1,k,\tilde{\mathbb{Z}})$ built from some $\tilde{\mathbb{Z}} \equiv \mathbb{Z}$ — an arithmetic-flavored classification (non-standard models of $\mathbb{Z}$, transported into the group) rarely seen this cleanly in group theory outside classical matrix-group settings.

## Problem

$BS(1,k) = \langle a, b \mid b^{-1}ab = a^k \rangle$ is a canonical example of a finitely generated metabelian (solvable) group; its elementary theory is undecidable and it is known to be QFA and prime among its models, but — unlike the non-metabelian Baumslag-Solitar groups (Casals-Ruiz & Kazachkov: elementary equivalence implies isomorphism there) — the metabelian case was not fully classified: which groups can be elementarily equivalent to $BS(1,k)$ without being isomorphic to it? Khélif had shown a weaker, parameter-dependent bi-interpretability with $\mathbb{Z}$; this paper asks whether that can be strengthened to *regular* bi-interpretability (interpretation codes working uniformly across a definable parameter set, per the regular-interpretability framework the same authors develop generally in `[[daniyarova-myasnikov-2025]]`) — and, if so, exactly what algebraic form the resulting classification of elementarily-equivalent models takes.

## Approach

1. **Foundational model theory** (§2): sets up definable-set/interpretation machinery, proves transitivity and composition behavior of interpretations (Lemma 1), and connects regular bi-interpretability directly to elementary-equivalence classification (Theorems 1-2): if $\mathbb{A}$, $\mathbb{B}$ are regularly bi-interpretable, every model of $\text{Th}(\mathbb{A})$ arises as a non-standard model $\Gamma(\tilde{\mathbb{B}}, \bar p)$ for some $\tilde{\mathbb{B}} \equiv \mathbb{B}$.
2. **Commutative-algebra input** (§3): develops divisibility theory for Laurent polynomials and the localized ring $\mathbb{Z}[1/k]$ — e.g. $n \mid m$ in $\mathbb{Z}$ iff $(k^n - 1) \mid (k^m - 1)$ in $\mathbb{Z}[1/k]$ — which becomes the key tool for defining multiplication on $\mathbb{Z}$ inside the group $BS(1,k)$.
3. **The bi-interpretability construction** (§4): represents $BS(1,k)$ as the semidirect product $\mathbb{Z}[1/k] \rtimes \mathbb{Z}$ (action $\varphi_m(x) = x \cdot k^{-m}$), builds an absolute interpretation $\Delta: \mathbb{Z}^3 \to BS(1,k)$, then shows the normal closure $A = \text{ncl}(a)$, the coset $Ab$, and multiplication on $\langle b \rangle \cong \mathbb{Z}$ are all definable — assembling a *regular injective* interpretation $\Gamma$ with parameters ranging over $Ab$, and finally exhibiting explicit formulas $\tau$, $\theta$ that make the two composite interpretations ($\Gamma \circ \Delta$, $\Delta \circ \Gamma$) definably invertible, i.e. strong regular bi-interpretability.
4. **Non-standard models and classification** (§5): for any $\tilde{\mathbb{Z}} \equiv \mathbb{Z}$, constructs the non-standard model $BS(1,k,\tilde{\mathbb{Z}}) = \tilde{\mathbb{Z}}[1/k^{\tilde{\mathbb{Z}}}] \rtimes \tilde{\mathbb{Z}}$ using a definable non-standard exponentiation, shows it is a $\tilde{\mathbb{Z}}$-group (satisfies the Lyndon exponential-group axioms, Theorem 4), and proves the full classification (Theorem 5).

## Key result

- **Theorem 1** (bi-interpretability ⟹ elementary-equivalence classification, general): if $\mathbb{A}$, $\mathbb{B}$ regularly bi-interpretable, then (1) for any $\tilde{\mathbb{B}} \equiv \mathbb{B}$, $\Gamma(\tilde{\mathbb{B}}, \bar p)$ is well-defined and $\mathbb{A} \equiv \Gamma(\tilde{\mathbb{B}}, \bar p)$; (2) every $\tilde{\mathbb{A}} \equiv \mathbb{A}$ is isomorphic to some $\Gamma(\tilde{\mathbb{B}}, \bar p)$; (3) $\Gamma(\mathbb{B}_1, \bar p) \cong \Gamma(\mathbb{B}_2, \bar p) \iff \mathbb{B}_1 \cong \mathbb{B}_2$.
- **Theorem 2** (uniqueness of interpretation choice): if a finitely generated $\mathbb{A}$ is regularly interpretable in $\mathbb{Z}$ via two different interpretations $\Gamma_1$, $\Gamma_2$, the resulting non-standard models are definably isomorphic regardless of which interpretation is used.
- **Theorem 3** (the paper's headline result): for $k > 1$, $BS(1,k)$ is regularly strongly bi-interpretable with $\mathbb{Z}$.
- **Theorem 4**: for every $k > 1$ and $\tilde{\mathbb{Z}} \equiv \mathbb{Z}$, the non-standard model $BS(1,k,\tilde{\mathbb{Z}})$ is a $\tilde{\mathbb{Z}}$-group (satisfies the Lyndon axioms for group exponentiation).
- **Theorem 5** (complete classification): (1) $BS(1,k) \equiv BS(1,k,\tilde{\mathbb{Z}})$ for any $\tilde{\mathbb{Z}} \equiv \mathbb{Z}$; (2) every group elementarily equivalent to $BS(1,k)$ has the form $BS(1,k,\tilde{\mathbb{Z}})$ for some $\tilde{\mathbb{Z}} \equiv \mathbb{Z}$; (3) $BS(1,k,\tilde{\mathbb{Z}}_1) \cong BS(1,k,\tilde{\mathbb{Z}}_2) \iff \tilde{\mathbb{Z}}_1 \cong \tilde{\mathbb{Z}}_2$ — the classification is a genuine bijection with non-standard models of $\mathbb{Z}$.
- **Corollary 1**: for any finitely generated $\mathbb{A}$ regularly bi-interpretable with $\mathbb{Z}$, $\tilde{\mathbb{B}} \equiv \mathbb{A}$ iff $\tilde{\mathbb{B}} \cong \mathbb{A}(\tilde{\mathbb{Z}})$ for a unique (up to isomorphism) $\tilde{\mathbb{Z}} \equiv \mathbb{Z}$ — the general template Theorem 5 instantiates for $BS(1,k)$.

## Assumptions

- $k \in \mathbb{N}$, $k > 1$ throughout ($k = 1$ gives the free abelian group $\mathbb{Z}^2$, excluded as a degenerate case).
- Standard finitary language of groups $\{\cdot, {}^{-1}, e\}$ and rings $\{+, \cdot, 0, 1\}$.
- $BS(1,k)$ is finitely generated (two generators $a$, $b$).
- All non-standard models are indexed by $\tilde{\mathbb{Z}} \equiv \mathbb{Z}$ in the language of rings.

## Limitations / scope

- Restricted to the **metabelian** Baumslag-Solitar groups $BS(1,k)$; the non-metabelian $BS(m,n)$ family ($m, n > 1$, $m \neq n$) is explicitly out of scope — cited as already handled by different techniques (Casals-Ruiz & Kazachkov: elementary equivalence implies isomorphism there, unlike the metabelian case).
- The comparison between this paper's non-standard models $BS(1,k,\tilde{\mathbb{Z}})$ and the pre-existing notion of *tensor completions* $BS(1,k) \otimes_{\mathcal{M}_2} \tilde{\mathbb{Z}}$ in the variety of metabelian groups is explicitly flagged by the authors as unresolved ("it will be very interesting to compare") — the two constructions are not shown to coincide.
- Algorithmic/Turing-machine-interpretation aspects of the non-standard models are noted as a potentially interesting direction but not developed.
- Purely theoretical; no results specific to Burnside groups or this vault's B(2,5) program.

## Replication evidence

N/A — a theoretical model-theory/group-theory paper with full proofs. Published in peer-reviewed form (Annals of Pure and Applied Logic, 2026) alongside the arXiv preprint; no independent replication surfaced at ingest.

## Why this paper matters

This paper takes one of the worked examples that `[[daniyarova-myasnikov-2025]]` (the same authors' later "Theory of Interpretations I" foundations paper) lists in passing — Baumslag-Solitar groups $BS(1,k)$ — and gives it the full dedicated treatment: not just an illustration of regular interpretability, but a complete first-order classification via regular *strong* bi-interpretability with $\mathbb{Z}$. It is also a clean addition to the vault's growing cluster of "elementary-equivalence classification via bi-interpretability with $\mathbb{Z}$" results (alongside `[[sohrabi-myasnikov-2020]]` for $\text{SL}_n(\mathcal{O})$/$\text{GL}_n(\mathcal{O})$/$\text{T}_n(\mathcal{O})$ and `[[myasnikov-sohrabi-2024]]` for the field case): where those papers work with classical linear groups built from bounded generation by transvections, this paper works with a genuinely different algebraic object — a metabelian, non-linear-in-the-same-sense solvable group — using Laurent-polynomial divisibility theory in $\mathbb{Z}[1/k]$ as its core technical engine. The result that elementarily-equivalent models of $BS(1,k)$ are *exactly* the arithmetic non-standard models of $\mathbb{Z}$ transported through the group structure is a striking, clean instance of the "logical complexity of $G$ reduces to logical complexity of $\mathbb{Z}$" phenomenon that runs through this whole cluster of papers.

## Quotes

1. > "We prove that metabelian Baumslag$-$Solitar group $BS(1,k)$, $k>1$, is (strongly) regularly bi-interpretable with the ring of integers $\mathbb{Z}$..." — Abstract
2. > "If $k>1$, then the group $BS(1,k)$ is regularly strongly bi-interpretable with $\mathbb{Z}$." — Theorem 3 (per source extraction)

## Open questions surfaced

- The explicitly flagged comparison between non-standard models $BS(1,k,\tilde{\mathbb{Z}})$ and tensor completions $BS(1,k) \otimes_{\mathcal{M}_2} \tilde{\mathbb{Z}}$ in the metabelian-group variety — stated by the authors as "very interesting to compare" but not carried out here.
- Whether the same regular-strong-bi-interpretability-with-$\mathbb{Z}$ technique extends to other one-relator or metabelian group families beyond $BS(1,k)$.
- Whether $BS(1,k)$'s regular strong bi-interpretability with $\mathbb{Z}$ (this paper) constitutes, or fails to constitute, a natural algebraic witness for `[[daniyarova-myasnikov-2025]]`'s open **Problem 1** (find a group/ring example that is regularly but not absolutely interpretable in another) — the source extracted for this note did not establish whether $BS(1,k)$'s interpretation in $\mathbb{Z}$ is absolute or only regular-but-not-absolute; worth checking on a closer read, since Paper I's own witness (Example 15, Gvozdevsky) was explicitly non-algebraic and the authors were still looking for a natural algebraic one.
- Algorithmic/Turing-machine-interpretation properties of the non-standard models $BS(1,k,\tilde{\mathbb{Z}})$, noted by the authors as independently interesting but undeveloped.

## Related material in vault

- Extends: (none in vault — chronologically predates `[[daniyarova-myasnikov-2025]]`/`[[daniyarova-myasnikov-2026]]` despite sharing both authors, so cannot extend them; possible that Paper I's BS(1,k) worked example cites this paper, but that citation could not be confirmed from the fetched source)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: `[[Concepts/bi-interpretability]]` — seventh paper in the vault to substantively engage with bi-interpretability; the first to apply *regular strong* bi-interpretability to a specific non-linear (metabelian, solvable) group family rather than a classical matrix group or an abstract categorical framework.
- Cites: (none confirmed as in-vault papers; Khélif's 2003 parametrized-bi-interpretability result and Noskov's undecidability result, both cited as prior work, are not yet separate vault entries)
- Cited by (in vault): (none)
- Sibling math-logic notes: `[[daniyarova-myasnikov-2025]]` — same authors, shares the regular-interpretability/regular-bi-interpretability terminology this paper works out in full for $BS(1,k)$, and lists $BS(1,k)$ as one of its own worked examples; `[[sohrabi-myasnikov-2020]]` and `[[myasnikov-sohrabi-2024]]` — the vault's other "elementary-equivalence classification via bi-interpretability with $\mathbb{Z}$" results, for classical linear groups rather than a metabelian Baumslag-Solitar group; `[[kharlampovich-myasnikov-sohrabi-2021]]` — the richness/WSOL framework this paper's regular-bi-interpretability-with-$\mathbb{Z}$ result could plausibly feed into (richness propagates by chaining bi-interpretability with $\mathbb{Z}$), though this paper does not itself invoke richness terminology.

---

## Notation conventions

Group/ring notation in this note ($BS(1,k)$, $\mathbb{Z}[1/k]$, semidirect products, tilde-decorated non-standard structures) is rendered in LaTeX inline math and plain Unicode prose; no `[[...]]`-style double-bracket expressions requiring backtick-escaping appear, per `[[paper-summary]]` § Notation conventions.
