---
title: "Non-trivial units of complex group rings"
authors:
  - "Giles Gardam"
year: 2024
venue: "arXiv preprint (math.GR)"
url: "https://arxiv.org/abs/2312.05240"
source_path: "~/Downloads/kaplansky/Kaplansky unit conj zero char.pdf"
language: en
domain: group-theory
methodology_type: theoretical
relevance: 1
key_concepts:
  - "[[Concepts/kaplansky-unit-conjecture]]"
extends:
  - "[[gardam-2023-kaplansky-survey]]"
  - "[[murray-2021-kaplansky-char-p]]"
contradicts: []
replicates: []
cites:
  - "[[gardam-2023-kaplansky-survey]]"
  - "[[murray-2021-kaplansky-char-p]]"
cited_by: []
quality_notes: "arXiv:2312.05240v2, October 2024. 7 pages. Completes the refutation of the unit conjecture by extending the counterexample to characteristic 0, including C[P] and Z[ζ₈][P]. The proof is by direct algebraic construction; a 2-parameter family of solutions is given. Companion code available at the zenodo repository [Gar24]. PDF extracted with pypdf."
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

# Non-trivial units of complex group rings

## Abstract

"The Kaplansky unit conjecture for group rings is false in characteristic zero." The same group P = ⟨a,b|b⁻¹a²b=a⁻², a⁻¹b²a=b⁻²⟩ used by Gardam in char 2 and by Murray in char p yields a non-trivial unit in ℂ[P], completing the refutation of the unit conjecture across all field characteristics.

## TL;DR

Gardam closes the loop: the Kaplansky unit conjecture fails not just in positive characteristic (2021–2021) but also in characteristic 0. The unit in ℂ[P] is supported on the same 21-element subset as the char-2 unit (after a minor symmetry transformation), with coefficients in Z[ζ₈] (8th roots of unity). This is significant because the topological motivation for the conjecture (Higman's thesis, Atiyah conjecture) lives in char 0.

## Problem

After Gardam's char-2 result and Murray's extension to all prime characteristics, it remained open whether the unit conjecture fails in characteristic 0 (e.g., in Q[P] or ℂ[P]). Murray's construction relied on the Frobenius endomorphism, which is specific to positive characteristic, strongly hinting (but not proving) that char 0 might behave differently.

## Key Result

**Theorem A.** Let P = ⟨a,b|b⁻¹a²b=a⁻², a⁻¹b²a=b⁻²⟩. Then ℂ[P] has non-trivial units.

**Explicit unit:** Set x = a², y = b², z = (ab)², let ζ₈ be a primitive 8th root of unity and i = ζ₈². Then an explicit unit is given by:
$$1 + i(x - x^{-1} - y + y^{-1})z^{-1} + \zeta_8(\ldots)a + \zeta_8(\ldots)b + i(\ldots)ab$$

(full 21-term expression given in the paper; support is the same 21-element subset as the char-2 unit, modulo the transformation: multiply on right by (ab)⁻¹ and apply automorphism a↦a, b↦a⁻²b).

**2-parameter family:** The result gives a 2-parameter family over R = Z[s,t]/⟨s⁴+1, t⁴+1⟩:
- α = α₁ + sα_a·a + tα_b·b + stα_{ab}·ab ∈ R[P] is a unit with explicit components (given in §2)
- Specialising s = t = ζ₈ gives the ℂ[P] unit of Theorem A

**Corollary.** For any field K containing a root of t⁴+1, K[P] has non-trivial units. In particular, this holds for Fₚₖ when 8 | (pᵏ - 1), covering infinitely many characteristics.

## Mechanism

- Direct verification by computer algebra (Sage/singular). The system of 121 quadratic equations in 42 variables (21 support elements of α and 21 of β⁻¹) was solved in seconds using algebraic geometry software.
- The same 21-element support works because the char-2 F₂[P] unit already determines which products ai·bj = 1 (17 pairs); the char-0 solution must respect this combinatorial structure with non-zero coefficients.
- The coefficients require an 8th root of unity — there is no unit in Z[P] (no square root of -1 in Z₂), though the coefficients are algebraic integers.

## Relationship to the Atiyah Conjecture

One motivation for char-0 results: a counterexample to the Atiyah conjecture on integrality of L²-Betti numbers would require a group G such that ℂ[G] has zero-divisors, which in turn requires ℂ[G] to have non-trivial units. This paper gives non-trivial units in ℂ[P] but does NOT give zero-divisors (a unit is invertible, hence not a zero-divisor).

## Significance

This result completes the refutation of the unit conjecture across all field characteristics:
- Char 2: Gardam 2021 (F₂[P], 21-element unit)
- Char p: Murray 2021 (F_d[P], growing support)
- Char 0: Gardam 2024 (ℂ[P], Z[ζ₈][P], 21-element unit)

The zero-divisor and idempotent conjectures remain open. P remains a candidate for ZDC study.

## Assumptions

- G = P = Hantzsche-Wendt group (torsion-free, proved in [Gar21]).
- K = ℂ or any field with a root of t⁴+1.

## Relevance to Mixer/B(2,5)

Methodological note only. B(2,5) is torsion; Kaplansky does not apply. The significance for the Mixer context: the same SAT-derived 21-element support structure found computationally over F₂ turns out to be an intrinsic algebraic feature of P's group ring, valid over ℂ. This validates the power of SAT-based search (like the Mixer's heuristic search) to find genuine structural features, not just char-specific accidents.

## Related material in vault

- Extends: [[gardam-2023-kaplansky-survey]] (§1.6 background), [[murray-2021-kaplansky-char-p]] (char-p predecessor)
- Concept hub: [[Concepts/kaplansky-unit-conjecture]]
- Full lineage: [[gardam-semidecidable-2021]] → [[murray-2021-kaplansky-char-p]] → this paper
- Companion topology approach: [[mineyev-2024-kaplansky-origami]]
