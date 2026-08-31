---
title: "Solving semidecidable problems in group theory"
authors:
  - "Giles Gardam"
year: 2021
venue: "SMRI – Algebra and Geometry Online, talk slides, 5 October 2021"
url: ""
source_path: "~/Downloads/kaplansky/gardam-semidecidable-problems.pdf"
language: en
domain: group-theory
methodology_type: computational
relevance: 1
key_concepts:
  - "[[Concepts/kaplansky-unit-conjecture]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[gardam-2023-kaplansky-survey]]"
  - "[[kaplansky-zero-divisors]]"
cited_by: []
quality_notes: "17-slide talk presented at SMRI Algebra and Geometry Online, 5 October 2021. Presents the SAT-encoding approach used to find the unit conjecture counterexample. Not a journal paper — slides only. No arXiv identifier found. Content extracted from PDF via pypdf. FLAG: the semidecidability framing of the unit-conjecture search is a methodological bridge to PatternBoost-style computational search; see 'Relevance to Mixer' section."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/group-rings
  - topic/kaplansky-unit-conjecture
  - topic/unique-product-property
  - topic/computational-search-group-theory
  - topic/cdcl
  - paper
  - status/draft
status: draft
---

# Solving semidecidable problems in group theory

> **FLAG — methodological bridge.** The semidecidability framing in this talk is a direct conceptual bridge to PatternBoost-style computational search: any YES instance (a non-trivial unit exists, a group is not left-orderable) is eventually found by enumerating finite ball-searches. This is precisely the search paradigm underlying the Mixer experiment framework. See [[charton-2024-patternboost]].

## Abstract

Talk slides presenting the SAT-based approach to finding counterexamples to algebraic conjectures in group theory. Frames the unit conjecture, zero-divisor conjecture, orderability, and unique product property as semidecidable problems — YES instances are recursively enumerable. The main result: SAT encoding discovers a non-trivial unit in F₂[P] for the Hantzsche-Wendt group P, disproving the unit conjecture.

## TL;DR

Gardam frames Kaplansky's unit conjecture as a semidecidable problem: the existence of a non-trivial unit in K[G] is recursively enumerable (you will eventually find one if it exists). He then encodes the unit search as Boolean SAT over B(n) (ball of radius n in the Cayley graph), solves it with a modern CDCL SAT solver, and finds the unit at n=5 for the Hantzsche-Wendt group P over F₂.

## Semidecidability Framing (§3–5)

**Definition (slide 3):** A decision problem is semidecidable if there is an algorithm that terminates with YES when given a YES input, but runs forever (or answers NO) otherwise. Equivalently, the YES instances form a recursively enumerable language.

**Classical examples in group theory (slide 4):**
- Word problem: w = 1 in G is semidecidable (enumerate all products of relators).
- Triviality problem for group presentations: non-triviality is semidecidable (enumerate non-trivial finite quotients).

**The unit conjecture as a semidecidable problem (slide 5):** Let G have solvable word problem and K be a finite field. The set of non-trivial units in K[G] is recursively enumerable: for each n, check all pairs α, β ∈ K[B(n)] (all elements of support in B(n)) for αβ = 1. If G has a non-trivial unit, this search will eventually find it at some finite n.

> "For simplicity, say K is finite. If G has solvable word problem then the set of non-trivial units in K[G] is recursively enumerable. The existence of non-trivial units is semidecidable modulo the word problem." — slide 5

## SAT Encoding (§7–9)

**Key idea (slide 6):** Turn the infinite search into an infinite sequence of finite NP problems. For each n, consider the ball B(n) of radius n in the Cayley graph.

**The Hantzsche-Wendt group P (slide 7):**
$$P = \langle a, b \mid b^{-1}a^2b = a^{-2},\; a^{-1}b^2a = b^{-2} \rangle$$
Smallest ball B(n) supporting a non-trivial unit over F₂: n = 5, |B(5)| = 147 elements.

**Boolean encoding (slides 8–9):** Let α = Σ_{g ∈ B(n)} a_g·g and β = Σ_{g ∈ B(n)} b_g·g with a_g, b_g ∈ {0,1}. The product equation αβ = 1 is:
- For each k ∈ G: Σ_{gh=k} a_g · b_h = δ_{1,k} (mod 2)
- Introduce auxiliary variables x_{g,h} := a_g · b_h via Tseytin transformation
- Each product equation breaks into small sums, each asserted with auxiliary variables
- Non-triviality: assert α has support not contained in any single coset

**Why SAT is effective (slide 11):** The system has a helpful sparsity property — certain products force others (a_g b_h = 1 implies a_{g'} b_{h'} = 1), creating propagation chains that CDCL can exploit.

## SAT for Related Problems (slide 12)

Beyond the unit conjecture, the same SAT framework applies to:
- Left-orderability / diffuseness (encode as 3-SAT per Orlef)
- Non-unique-product property (cardinality constraints via Frisch-Peugniez)
- Zero-divisor conjecture (same encoding, "αβ = 0" instead of "αβ = 1")

**Theorem (Gardam 2021, slide 14):** The torsion-free group ⟨a,b|aba²b⁻¹a²b⁻², ab³ab⁴a⁻¹b⟩ does not have the unique product property. (Note: different group from the unit conjecture counterexample group P.)

## Additional Counterexample (slide 16)

**Soelberg's group:** S = ⟨x,y|x⁻¹y²xy², x⁻²yx⁻²y³⟩ (torsion-free polycyclic, virtually the Heisenberg group). Two 8-element sets fail UP (current world record at time of writing).

**Theorem (Gardam 2021):** There are non-trivial units in F₂[S], with support of size 29:
> "1 + y + y⁻¹ + x² + xy⁻¹ + x⁻¹y + x⁻¹y⁻¹ + yx + y⁻² + xyx + xy⁻¹x + x⁻²y + yx⁻¹y + y⁻³ + x²yx + x²y⁻¹x + x²y⁻² + xyx⁻¹y + xy⁻³ + yxyx + yxy⁻² + yx⁻²y⁻¹ + y⁻⁴ + x³y⁻¹x + xyxyx + xyxy⁻² + xyx⁻²y⁻¹ + xy⁻⁴ + x⁻¹y⁻⁴" — slide 16

This is a SECONDARY result from the talk, distinct from Gardam's primary 2021 Annals paper (which uses group P with 21-element support over F₂).

## Assumptions

- G must have solvable word problem for the SAT encoding to be effective.
- K finite (the slides focus on F₂; other finite fields are mentioned as possible).

## Limitations / Scope

- Semidecidability only guarantees finding YES instances — a negative result from any finite ball-search does NOT mean no unit exists (you just haven't found it yet).
- The approach does not scale to ZDC search due to a shortage of "candidate groups" (slide 13): groups where ZDC might fail are less well-characterized than groups without UP.

## Relevance to Mixer/B(2,5)

**METHODOLOGICAL BRIDGE** (flagged per task brief): The semidecidability framing (enumerate B(n) for increasing n, encode as NP problem, solve with heuristic solver) is directly analogous to the Mixer's architecture: enumerate rule-injection strategies, encode convergence as a scoring problem, use heuristic search. PatternBoost ([[charton-2024-patternboost]]) uses the same "local search + global reseeding" pattern. The conceptual shift "this is semidecidable — put a computer to work on it" is the right stance for any Mixer domain problem.

B(2,5) is a torsion group; Kaplansky conjectures are not directly applicable. Relevance is methodology-only.

## Related material in vault

- Extends: (none)
- Key concept hub: [[Concepts/kaplansky-unit-conjecture]]
- Survey context: [[gardam-2023-kaplansky-survey]] (§1.6 covers the same counterexample in detail)
- Char-p extension: [[murray-2021-kaplansky-char-p]]
- Char-0 extension: [[gardam-2024-kaplansky-char-zero]]
- Methodological bridge: [[charton-2024-patternboost]] (PatternBoost: same local-enumerate + global-reseed paradigm)
- Existing vault: [[kaplansky-zero-divisors]] (Open problems note)
- MOC: [[_moc-word-problem]] (adjacent open problems — Kaplansky cluster)
