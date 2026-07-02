---
title: "The topology and geometry of units and zero-divisors: origami"
authors:
  - "Igor Mineyev"
year: 2024
venue: "Preprint (last revised July 2025)"
url: ""
source_path: "~/Downloads/kaplansky/minyev-kaplansky.pdf"
language: en
domain: group-theory
methodology_type: theoretical
relevance: 2
key_concepts:
  - "[[Concepts/kaplansky-unit-conjecture]]"
  - "[[Concepts/kaplansky-zero-divisors]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[gardam-2023-kaplansky-survey]]"
  - "[[gardam-semidecidable-2021]]"
  - "[[kaplansky-zero-divisors]]"
cited_by: []
quality_notes: "32-page preprint, April 2024, minor revisions July 2025. Introduces a topological/geometric framework ('product structures', 'taikos', 'origami cell complexes') for the systematic construction of candidate counterexamples to both the unit and zero-divisor conjectures. No arXiv identifier found in PDF; check arxiv.org/search for Mineyev 2024 group rings. The computational search component is flagged as future work in this paper; follow-up articles are referenced as [26]. Content extracted from PDF via pypdf."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/group-rings
  - topic/kaplansky-unit-conjecture
  - topic/computational-search-group-theory
  - paper
  - status/draft
---

# The topology and geometry of units and zero-divisors: origami

## Abstract

"We define a product structure Π, its corresponding 2-dimensional cell complexes X_Π and Y_Π, associate to them the universal groups G_Π and Ḡ_Π, and a pair (a_Π, b_Π) of elements in the group algebra Z₂Ḡ_Π or in the group ring RḠ_Π for any ring R with unity. We give lists of sufficient combinatorial conditions on a product structure Π implying that G_Π and Ḡ_Π are torsion-free and that the associated a_Π and b_Π are either nontrivial units or nontrivial zero-divisors. The proofs use graphs and geometry of cell complexes in a substantial way. These results allow using computer-based search to look for counterexamples to the Kaplansky unit and zero-divisor conjectures."

## TL;DR

Mineyev proposes a new framework for generating candidate counterexamples to Kaplansky's unit AND zero-divisor conjectures: encode the combinatorial structure of a desired unit (or zero-divisor) as a "product structure" Π, associate a 2-complex Y_Π whose fundamental group Ḡ_Π is (conjecturally) torsion-free, and obtain group ring elements a_Π, b_Π that are (provably) units or zero-divisors if the complex has nonpositive curvature (CAT(0)). The hard part is proving torsion-freeness; CAT(0) provides a geometric certificate.

## Core Objects

### Product Structures (§2.1)

A **product structure** Π = (A, B, P) consists of:
- Finite sets A = {a₁,...,aₘ}, B = {b₁,...,bₙ}
- P: a partition of A × B (the set of "vertical edges" in the complete bipartite graph G(A,B)) into cells of size ≥ 2, where any two edges in the same cell share no common vertices

The **size** of Π is (m,n). If mn is ODD, the associated group ring elements are units; if mn is EVEN, they are zero-divisors (§2.3, key distinction).

### Taikos (§2.6)

The **taiko** (product graph) for Π is a visual representation: A on the bottom, B on the top, vertical edges for each (a,b) in a 2-cell of P, colored by 2-cell membership. Taikos visually encode the structure and allow pattern recognition.

### Cell Complexes (§3.1–3.4)

For each product structure Π, define:
- **X_Π**: 2-complex with 3 vertices (x_A, x_1, x_B), edges labeled by a₁,...,aₘ (x_A to x_1) and b₁,...,bₙ (x_1 to x_B), and one square 2-cell for each 2-cell {(a_i,b_j),(a_i',b_j')} of P attached along the loop a_i b_j b_{j'}⁻¹ a_{i'}⁻¹.
- **G_Π** = π₁(X_Π, x_1): the "universal group" of Π.
- **Y_Π**: obtained from X_Π by "2-foldings" (origami) — gluing middle edges and folding triangles. G̃_Π = π₁(Ȳ_Π) is the "full universal group."

The associated group ring elements a_Π = Σ aᵢ and b_Π = Σ bⱼ in Z₂Ḡ_Π are defined by the construction in §3.5.

### Key Theorem (§3.5–3.6, §6)

**Theorem 23 (Nonpositive curvature implies nondegeneracy):** If Y_Π admits a CAT(0) piecewise-Euclidean metric, then:
1. Ḡ_Π is torsion-free (CAT(0) groups are torsion-free by Cartan-Hadamard).
2. a_Π and b_Π are nontrivial (i.e., neither is a scalar times a single group element).

Together with the product structure encoding, this gives: if Y_Π is CAT(0) and mn is odd, then a_Π · b_Π = 1 is a non-trivial unit in Z₂Ḡ_Π; if mn is even, it's a zero-divisor.

## The Research Program (§7.2)

The paper proposes:
1. Enumerate product structures Π of small size (m,n).
2. Check combinatorial conditions for CAT(0) (sufficient conditions given in §7.1 — conditions on "link graphs" of the complex).
3. For those passing the CAT(0) test: the associated (a_Π, b_Π) give a genuine counterexample to UC (if mn odd) or ZDC (if mn even) for the torsion-free group Ḡ_Π.

**Status at time of writing:** The paper presents the theoretical framework. Computational search for product structures satisfying the conditions is described as ongoing in future articles [26].

## Connection to Gardam's Result

The Gardam counterexample fits this framework: the 21-element support of the unit in F₂[P] corresponds to a product structure Π of size (21,21) (or a substructure thereof). Mineyev's paper provides a CAT(0)-geometry language to explain why P admits this unit.

## Significance

This paper proposes:
1. A systematic way to search for ZDC counterexamples (not just UC) — the zero-divisor conjecture is much less explored computationally.
2. A geometric certificate (CAT(0)) for torsion-freeness — the hardest part of verifying candidate counterexamples.
3. A scalable enumeration target: small (m,n) product structures are accessible to computer search.

## Limitations / Scope

- The torsion-freeness question for Ḡ_Π is hard in general; CAT(0) provides a sufficient but not necessary condition.
- The paper's main results are theoretical; all computational work is deferred to [26].
- No new counterexample is presented; the paper is a framework paper.

## Relevance to Mixer/B(2,5)

Methodological note only. B(2,5) is torsion; Kaplansky does not apply directly. However, the research program described (enumerate product structures, check a combinatorial condition, get a counterexample) is a template for Mixer-style search: enumerate mixing strategies, check a criterion (e.g., overlap score), get a faster KB run. The CAT(0) curvature condition as a "proof certificate" is analogous to confluence as a convergence certificate in KB.

## Related material in vault

- Cites: [[gardam-2023-kaplansky-survey]] (the counterexample this framework explains), [[gardam-semidecidable-2021]] (the SAT-search paper)
- Related: [[kaplansky-zero-divisors]] (ZDC hub — Mineyev targets both UC and ZDC)
- Concept hub: [[Concepts/kaplansky-unit-conjecture]]
- Companion papers: [[gardam-2024-kaplansky-char-zero]], [[murray-2021-kaplansky-char-p]]
