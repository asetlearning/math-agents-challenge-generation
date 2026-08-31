---
title: "More counterexamples to the unit conjecture for group rings"
authors:
  - "Alan G. Murray"
year: 2021
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2106.02147"
source_path: "~/Downloads/kaplansky/Kaplansky unit conj char p.pdf"
language: en
domain: group-theory
methodology_type: theoretical
relevance: 1
key_concepts:
  - "[[Concepts/kaplansky-unit-conjecture]]"
extends:
  - "[[gardam-2023-kaplansky-survey]]"
contradicts: []
replicates: []
cites:
  - "[[gardam-2023-kaplansky-survey]]"
cited_by:
  - "[[gardam-2024-kaplansky-char-zero]]"
quality_notes: "arXiv:2106.02147v1, June 2021. 4 pages. Direct extension of Gardam's char-2 result to all prime characteristics. Uses the same group P; the key technical input is that the Frobenius endomorphism allows lifting the char-2 symmetry to char-p. Straightforward reading; PDF extracted with pypdf."
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
status: draft
---

# More counterexamples to the unit conjecture for group rings

## Abstract

"Extending the discovery by Giles Gardam of a concrete counterexample to Kaplansky's unit conjecture in characteristic 2, a family of counterexamples for every prime characteristic is presented."

## TL;DR

Murray extends Gardam's F₂[P] counterexample to F_p[P] for every prime p, using the same group P = ⟨a,b|b⁻¹a²b=a⁻², a⁻¹b²a=b⁻²⟩. The construction is algebraic (not another SAT search): it uses the symmetry of Gardam's unit and the Frobenius automorphism to transport the char-2 solution to all prime characteristics. Unit support size |supp(α_d)| grows with d.

## Problem

Gardam's 2021 counterexample gives a non-trivial unit in F₂[P]. Is the unit conjecture also false in characteristic p for other primes? Is it characteristic-specific?

## Group and Notation

Same group P as Gardam:
$$P = \langle a, b \mid b^{-1}a^2b = a^{-2},\; a^{-1}b^2a = b^{-2} \rangle$$

Set x = a², y = b², z = (ab)². Any element of P is uniquely of the form f(x,y,z)g where g ∈ {1, a, b, ab}. For functions f(x,y,z), inversions of variables: f_x(x,y,z) = f(x⁻¹, y, z), f_xy(x,y,z) = f(x⁻¹, y⁻¹, z), etc.

Relations: a·f = f_{yz}·a, b·f = f_{xz}·b, ab·f = f_{xy}·ab.

## Key Result

**Theorem:** For each prime d, there is a non-trivial unit α_d ∈ F_d[P].

**Construction:** Using Gardam's selection (p', q', r', s') = (x⁻¹pyz, -x⁻¹q, -y⁻¹r, z⁻¹syz), the system αβ = 1 reduces to a system of equations in polynomials p, q, r, s over F_d[⟨x,y,z⟩]. The char-2 solution (where -1 = 1) gives a particular solution structure that can be lifted to char p via the Frobenius endomorphism and the symmetry of the system.

**Support growth:** |supp(α_d)| → ∞ as d → ∞. The unit support size increases with the prime characteristic; the char-2 unit has 21 elements but this is not representative of other characteristics.

**Corollary:** The unit conjecture fails over F_d[P] for every prime d. Combined with Gardam's char-0 result [[gardam-2024-kaplansky-char-zero]], the unit conjecture fails over K[P] for every field K.

## Mechanism

The key algebraic insight (Murray §1): Gardam's selection of the inverse (p', q', r', s') reduces the 4-component unitality condition to 4 polynomial equations in (p, q, r, s) over F[⟨x,y,z⟩] ≅ F[x^{±1}, y^{±1}, z^{±1}]. In char 2, symmetry collapses the system. For char p, one uses the relation (Frobenius): the Frobenius automorphism of F_p[⟨x,y,z⟩] sends x ↦ xᵖ, y ↦ yᵖ, z ↦ zᵖ and commutes with the group action. This allows lifting the char-2 symmetry solution.

## Assumptions

- Same group P as Gardam (torsion-free, Hantzsche-Wendt crystallographic group).
- K = F_d for a prime d.

## Limitations

- Does not address char 0 (handled by Gardam in [[gardam-2024-kaplansky-char-zero]]).
- Does not address the zero-divisor or idempotent conjectures.
- No new group: the same P is used. A counterexample for more "natural" torsion-free groups (e.g., fundamental groups of 3-manifolds) remains open.

## Relevance to Mixer/B(2,5)

Methodological note only. B(2,5) is a torsion group; unit conjecture does not apply. This paper's contribution to the Mixer context is indirect: it confirms that the Gardam counterexample is not a char-2 accident but a genuine algebraic phenomenon in P across all characteristics, strengthening the case that the SAT-search method found a real structural feature of P's group ring.

## Related material in vault

- Extends: [[gardam-2023-kaplansky-survey]] (§1.6 context)
- Cited by: [[gardam-2024-kaplansky-char-zero]] (references Murray as motivating the char-0 question)
- Concept hub: [[Concepts/kaplansky-unit-conjecture]]
- Companion: [[gardam-semidecidable-2021]] (the SAT method that found the original unit)
- Companion: [[gardam-2024-kaplansky-char-zero]] (char-0 extension)
- Lineage context: [[gardam-2023-kaplansky-survey]] (survey covering all three conjectures)
- MOC: [[_moc-word-problem]] (adjacent open problems — Kaplansky cluster)
