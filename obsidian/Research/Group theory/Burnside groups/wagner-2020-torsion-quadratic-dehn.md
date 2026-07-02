---
title: "Torsion Subgroups of Groups with Quadratic Dehn Function"
authors: Francis Wagner
year: 2020
venue: arxiv
url: https://arxiv.org/abs/2010.05381
url_translated:
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count:
citation_count_date:
key_concepts:
  - "`[[Concepts/dehn-function]]`"
  - "`[[Concepts/burnside-groups]]`"
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "arXiv preprint (math.GR), submitted 2020-10-12. Citation count not verified at ingest. Relevance flagged by Alexei as possibly applicable to B(2,5) — the connection is via the free Burnside group embedding result and the Dehn-function (isoperimetric / word-problem-complexity) machinery, NOT a direct B(2,5) reduction technique. Exponent condition (n ≥ 2^48) excludes the small exponents like 5 we care about — see Limitations."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/dehn-function
  - topic/torsion-groups
  - topic/finitely-presented-groups
  - topic/word-problem
  - topic/quasi-isometry
  - paper
  - status/draft
project: b25
---

# Torsion Subgroups of Groups with Quadratic Dehn Function

## Abstract

> "We construct the first examples of finitely presented groups with quadratic Dehn function containing a finitely generated infinite torsion subgroup. These examples are 'optimal' in the sense that the Dehn function of any such finitely presented group must be at least quadratic. Moreover, we show that for any $n\geq2^{48}$ such that $n$ is either odd or divisible by $2^9$, any infinite free Burnside group with exponent $n$ is a quasi-isometrically embedded subgroup of a finitely presented group with quadratic Dehn function satisfying the Congruence Extension Property."

## TL;DR

Constructs the first finitely-presented groups that have a quadratic Dehn function (the lowest possible above linear) while still containing an infinite finitely-generated torsion subgroup — and shows large-exponent free Burnside groups embed quasi-isometrically into such groups. Relevant to B(2,5) only by analogy: it is about the *geometric/isoperimetric complexity* (Dehn function) of Burnside-containing groups, not a word-reduction algorithm, and its exponent bound (n ≥ 2^48) excludes exponent 5.

## Problem

The **Dehn function** of a finitely presented group measures the *isoperimetric* complexity of its word problem: for a word of length L that equals the identity, how many relator-applications (area of a van Kampen diagram) are needed to reduce it to the empty word, as a function of L. A quadratic Dehn function is the smallest super-linear class (linear ⟺ hyperbolic, which excludes infinite torsion subgroups).

Open question this engages: can a finitely presented group with a *quadratic* (hence near-minimal) Dehn function contain an infinite finitely-generated **torsion** subgroup? Torsion subgroups (every element of finite order) are the Burnside-group regime; hyperbolic (linear-Dehn) groups cannot contain infinite torsion subgroups, so quadratic is the natural target.

## Approach

Explicit group construction plus analysis of Dehn functions and embedding properties (geometric group theory). The construction embeds a free Burnside group quasi-isometrically into a finitely presented group whose Dehn function is controlled to be quadratic, while preserving the Congruence Extension Property (CEP). The optimality (≥ quadratic) follows from the fact that infinite torsion subgroups force the Dehn function above linear.

## Key result

**Theorem (informal):** There exist finitely presented groups with **quadratic** Dehn function containing a finitely generated **infinite torsion** subgroup; quadratic is optimal (any such group has Dehn function at least quadratic).

**Embedding theorem (verbatim condition):** For any $n \geq 2^{48}$ such that $n$ is either odd or divisible by $2^9$, any infinite free Burnside group of exponent $n$ is a **quasi-isometrically embedded** subgroup of a finitely presented group with quadratic Dehn function satisfying the **Congruence Extension Property**.

## Assumptions

- Groups are finitely presented.
- The exponent bound $n \geq 2^{48}$, with $n$ odd or divisible by $2^9$ — a strong constraint inherited from the available infinite-free-Burnside machinery (Ol'shanskii / Lysenok-type results hold only for large exponents).
- Free Burnside group of that exponent is infinite (true for the stated $n$).

## Limitations / scope

- **The exponent condition excludes B(2,5).** $n \geq 2^{48}$ rules out exponent 5 entirely. B(2,5) is a *small-exponent, finite or near-finite* regime; this paper's results live in the *large-exponent, infinite* regime. So the embedding theorem does **not** directly apply to B(2,5).
- It is a **structural / geometric** result about isoperimetric complexity, **not** a word-reduction algorithm or a Knuth-Bendix technique. It says something about *how hard* the word problem is geometrically, not *how to solve it* computationally.
- The construction is existential; no explicit small presentation or algorithm is given for computation.

## Replication evidence

N/A — a constructive existence theorem in geometric group theory; not an experiment. Not independently re-verified in this vault.

## Why this paper matters

For the B(2,5) program, the value is **conceptual, not directly applicable** — and the relevance should be stated honestly. Alexei flagged it as possibly applicable; the genuine connection is that the **Dehn function** is exactly the kind of *isoperimetric / word-problem-complexity* measure that came up as a candidate angle for thinking about the difficulty of B(2,5) word reduction (how much "area" a reduction needs). This paper shows that the geometry of Burnside-containing groups can be tightly controlled (quadratic Dehn), which is a positive structural fact about the family.

However, the exponent gap ($n \geq 2^{48}$ vs. our exponent 5) and the existential/non-algorithmic nature mean it does **not** give a reduction method for B(2,5). Its most useful role is as background for any future "Dehn-function / isoperimetric proxy" idea: it establishes what is known about the isoperimetric geometry of free Burnside groups (in the large-exponent regime) and would need a separate small-exponent analogue to bear on B(2,5) directly.

## Quotes

1. > "the first examples of finitely presented groups with quadratic Dehn function containing a finitely generated infinite torsion subgroup" — Abstract
2. > "These examples are 'optimal' in the sense that the Dehn function ... must be at least quadratic" — Abstract

## Open questions surfaced

- Is there a **small-exponent** (e.g. exponent 5) analogue of the embedding, or does the $n \geq 2^{48}$ bound reflect a genuine obstruction rather than a limitation of current technique?
- Does the Dehn function (isoperimetric area of reductions) give any *computable* signal about B(2,5) word reducibility — i.e. could an isoperimetric measure serve as the kind of word-metric-aware proxy the PatternBoost program is looking for? (Speculative; needs Validator/Math-expert assessment — flagged as a candidate, not a claim.)
- What is the Dehn function of B(2,5) itself (finite group regime), and does it carry any information relevant to the core-factorization structure of the B(2,5) target words?

## Related material in vault

- Extends: (none in vault)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: `[[Concepts/dehn-function]]`, `[[Concepts/burnside-groups]]` (stubs may need creation)
- Cites (in vault): (none yet)
- Cited by (in vault): (none yet)
- Adjacent vault work: the B(2,5) Burnside research notes under `Research/Group theory/Burnside groups/B25/` (Kuznetsov et al.); the PatternBoost proxy program (`[[charton-2024-patternboost]]`, B25 Proxy Validation experiments) where isoperimetric/word-metric proxies are an open line.
