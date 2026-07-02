---
title: "Group rings of infinite groups (Kaplansky survey)"
authors:
  - "Giles Gardam"
year: 2024
venue: "Lecture notes, University of Bonn, winter semester 2023/2024"
url: "https://github.com/gilesgardam/lectures"
source_path: "~/Downloads/kaplansky/gardam-kaplansky-survey.pdf"
language: en
domain: group-theory
methodology_type: theoretical
relevance: 1
key_concepts:
  - "[[Concepts/kaplansky-unit-conjecture]]"
  - "[[Concepts/kaplansky-zero-divisors]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[gardam-2024-kaplansky-char-zero]]"
  - "[[murray-2021-kaplansky-char-p]]"
  - "[[kaplansky-zero-divisors]]"
cited_by: []
quality_notes: "Lecture notes from Gardam's winter 2023/2024 course at Bonn. 55 pages, comprehensive coverage of all three Kaplansky conjectures plus ordered group theory, traces, and bi-orderability. Available at https://github.com/gilesgardam/lectures. Not a journal article but the most complete single-source treatment of the unit conjecture counterexample and its context. PDF extracted with pypdf."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/group-rings
  - topic/kaplansky-unit-conjecture
  - topic/kaplansky-idempotent-conjecture
  - topic/unique-product-property
  - topic/computational-search-group-theory
  - paper
  - status/draft
---

# Group rings of infinite groups (Kaplansky survey)

> **Primary reference.** This is the authoritative single-source treatment of all three Kaplansky conjectures through the Gardam 2021 counterexample and its extensions. Read alongside [[gardam-2024-kaplansky-char-zero]] (the char-0 result) and [[murray-2021-kaplansky-char-p]] (the char-p extension).

## Abstract

Lecture notes from Gardam's winter semester 2023/2024 course at the University of Bonn. Covers the Kaplansky conjectures on group rings of infinite groups — unit conjecture, zero-divisor conjecture, idempotent conjecture — and their proofs for specific group families (locally indicable, orderable, hyperbolic), culminating in the 2021 counterexample to the unit conjecture. Also covers traces, bi-orderability, the Malcev-Neumann skew field embedding, and amenability.

## TL;DR

Gardam's lecture notes: 55 pages covering the three Kaplansky conjectures from scratch through the SAT-based 2021 counterexample to the unit conjecture. The unit conjecture is FALSE (for the Hantzsche-Wendt group P over any field). The zero-divisor and idempotent conjectures remain open.

## The Three Kaplansky Conjectures

**Definition (Group ring):** For a ring R and group G, the group ring R[G] consists of finite formal R-linear sums Σ r_g·g with pointwise addition and multiplication (r_g·g)(s_h·h) = (r_g s_h)·(gh). When R = K is a field, K[G] is the group algebra.

**Conjecture 1.5 (Kaplansky conjectures, §1.1).** Let G be torsion-free and K a field. Then K[G] has:
1. **Unit conjecture (UC):** no non-trivial units — αβ = βα = 1 =⇒ α = kg for some k ∈ K×, g ∈ G.
2. **Zero-divisor conjecture (ZDC):** no non-zero zero-divisors — αβ = 0 =⇒ α = 0 or β = 0.
3. **Idempotent conjecture (IC):** no non-trivial idempotents — α² = α =⇒ α = 0 or α = 1.

**For any G (with or without torsion):** K[G] is directly finite — αβ = 1 =⇒ βα = 1. This is PROVED for all group rings (not a conjecture).

**Historical attribution:** The unit conjecture was first stated in Higman's 1940 thesis [Hig40, p.77]. It became widely known as "Kaplansky's" conjecture after Kaplansky popularized it around 1970.

## Implication Chain

$$\text{UC} \implies \text{ZDC} \implies \text{IC}$$

- **UC → ZDC:** Passman [Pas85, Lemma 13.1.2]. If K[G] satisfies the unit conjecture, it is an integral domain.
- **ZDC → IC:** Trivial — if K[G] has no zero-divisors, then e(1-e) = 0 implies e = 0 or 1.
- **UC is FALSE** (Gardam 2021): the Hantzsche-Wendt group P has non-trivial units in F₂[P]. This does NOT give a counterexample to ZDC or IC (the counterpositive: UC false tells us nothing about ZDC).
- **ZDC and IC remain OPEN** in full generality.
- **Directly finite** is a theorem for all group rings — weaker than any of the conjectures.

## Group Families Where Conjectures Are Proved

### Proving the Unit Conjecture (§1.2)

The main proof strategy: show G has the **unique product property (UP)**.

**Definition 1.15:** G has UP if for all finite non-empty A, B ⊆ G there exists g ∈ G uniquely expressible as ab (a ∈ A, b ∈ B).

**Corollary 1.21 (from §1.2):** A group with UP satisfies the unit conjecture.

**Proposition 1.24:** A left-orderable group has UP.

**Corollary 1.31 (Higman, 1940):** Locally indicable groups satisfy the unit and zero-divisor conjectures. (Locally indicable =⇒ left-orderable =⇒ UP.)

Groups satisfying the unit conjecture via UP/orderability (Example 1.32 and §1.2):
- Free groups (locally indicable via Nielsen-Schreier)
- Fundamental groups of surfaces with χ < 0
- Torsion-free nilpotent groups
- Torsion-free one-relator groups
- Orderable groups

**Definition 1.36 (Diffuse):** A finite subset A is diffuse if every a ∈ A is extremal. G is diffuse if every finite A ⊆ G is diffuse.

**Proposition 1.39:** Left-orderable =⇒ diffuse =⇒ UP.

### Proving the Zero-Divisor Conjecture

- **Hyperbolic groups** (char 0): via Delzant's theorem (§1.3). Residually finite hyperbolic groups are virtually diffuse (Corollary 1.54).

### Proving the Idempotent Conjecture

**Theorem 1.120 (Zalesskii):** For any G and idempotent e ∈ K[G], tr(e) lies in the prime subfield of K.

**Theorem 1.122 (Formanek):** Let G be torsion-free and N_G = {primes p | ∃ g ∈ G\{1}, n ∈ Z⁺ s.t. g ~ gᵖⁿ}.
- If char(K) = p > 0 and p ∉ N_G, then tr(e) = 0 or 1 for any idempotent e ∈ K[G].
- If char(K) = 0 and p ∉ N_G for infinitely many p, then e = 0 or 1.

**Corollary 1.125:** Groups with |N_G| < ∞ satisfy the idempotent conjecture in characteristic 0. This includes: finitely generated subgroups of GL_n(F) (any field), hyperbolic groups, CAT(0) groups, subgroups of Out(Fₙ) or mapping class groups.

## The Unit Conjecture Counterexample (§1.6)

### The Group P

**Definition:** The Hantzsche-Wendt crystallographic group (Promislow's group):
$$P = \langle a, b \mid b^{-1}a^2b = a^{-2},\; a^{-1}b^2a = b^{-2} \rangle$$

Set x = a², y = b², z = (ab)². Then ⟨x,y,z⟩ ≅ Z³ is a normal subgroup of P with quotient Z/2 ⊕ Z/2.

**Corollary 1.129:** P is torsion-free. (Proved via the faithful representation φ: P → D_∞ × D_∞ × D_∞.)

**Theorem 1.135 (Promislow, 1988):** P is NOT a UP group. The witness is a 14-element set S = E₀ ∪ E₁ ∪ E₂ such that S·S has no unique product. (P was the smallest known non-UP torsion-free group at the time.)

### The Counterexample

**Theorem 1.148 (Gardam, [Gar21]):** There exists α ∈ (F₂[P])× with |supp(α)| = 21. That is, the Kaplansky unit conjecture is FALSE.

**How found (§1.6 + [Gar21]):** SAT encoding. For field K = F₂ and ball B(n) = {elements of P of word-length ≤ n in generators a, b}, the existence of a non-trivial unit α = Σ_{g ∈ B(n)} a_g·g, β = Σ_{g ∈ B(n)} b_g·g with αβ = 1 is an instance of Boolean satisfiability:
- Variables: a_g, b_g ∈ {0,1} for each g ∈ B(n)
- Non-triviality clauses: assert α is not a scalar multiple of a single group element
- Product equations: each coefficient of αβ at k is Σ_{gh=k} a_g b_h = δ_{1,k} (mod 2)
- Encoded in CNF; solved by modern CDCL SAT solvers

For n = 5: B(5) has 147 elements, problem has ~2^147 ≈ 10^44 states. SAT solver finds the 21-element support unit.

**Corollary 1.149 ([Gar21]):** (F₂[P])× contains free subgroups and is not finitely generated.

**Bartholdi's symmetry analysis (Theorem 1.150 [Bar23]):** The unit α_d exhibits a twisted-unitary symmetry: there exist non-trivial automorphisms θ₀, θ₁ ∈ Aut(K[P]) such that θ₀(α_d) = α_d and θ₁(α_d)* = α_d⁻¹.

### Extensions

- **Char p (Murray [Mur21]):** Gardam's construction generalized to a unit α_d ∈ F_d[P] for every prime d, with |supp(α_d)| → ∞ as d → ∞. See [[murray-2021-kaplansky-char-p]].
- **Char 0 (Gardam [Gar24]):** The same 21-element support (after minor symmetry transformation) carries a non-trivial unit over ℂ with coefficients in Z[ζ₈]. See [[gardam-2024-kaplansky-char-zero]].

## Ordered Group Theory and the Conjectures

The survey develops ordered group theory as a proof strategy for the conjectures:

**Bi-ordered groups (§1.9):** G is bi-orderable if it admits a total order invariant under both left and right multiplication. **Proposition 1.178:** Bi-orderable groups are locally indicable. Combined with earlier results: bi-orderable =⇒ locally indicable =⇒ left-orderable =⇒ UP =⇒ UC.

**Torsion-free nilpotent groups are bi-orderable (Proposition 1.172):** By induction on nilpotency class, using that torsion-free abelian groups are bi-orderable.

**Malcev-Neumann theorem (Theorem 1.184):** If G is bi-orderable, K[G] embeds in a skew field D (formal sums with well-ordered support).

## Appendix A: Overview of Implications (full diagram)

From Appendix A of the course (all implications are one-directional unless noted):
```
G bi-orderable → K[G] embeds in skew field
G bi-orderable → G locally indicable (1.178)
G locally indicable ← G left-orderable (Burns-Hale 1.29)
G left-orderable ← G diffuse (1.39)
G diffuse ← G acts on hyperbolic space (Delzant 1.53)
G has UP ← G diffuse (1.39)
K[G] satisfies UC ← G has UP (1.21)
K[G] satisfies ZDC ← K[G] satisfies UC (Passman, 1.9)
K[G] satisfies IC ← K[G] satisfies ZDC (trivial, 1.9)
K[G] directly finite ← K[G] satisfies IC (and: proved directly for all G)
{primes}\N_G infinite → K[G] satisfies IC (Formanek 1.122)
e² = e → tr(e) ∈ Fₚ or Q (Zalesskii 1.120)
K = C, G residually finite → K[G] stably finite
G surjunctive → K[G] directly finite
G sofic → G surjunctive
```

## Key Verbatim Theorem Statements

**Conjecture 1.5** (§1.1, p.1): "If G is torsion-free, then K[G] has no non-trivial units, no non-zero zero divisors, and no non-trivial idempotents."

**Theorem 1.148** (§1.6, p.36): "There exists α ∈ (F₂[P])× with |supp(α)| = 21. That is, the Kaplansky unit conjecture is false."

**Corollary 1.31** (§1.2, p.5): "Locally indicable groups satisfy the conjectures on units and zero divisors."

**Theorem 1.122(ii)** (Formanek, §1.5, p.28): "If char(K) = 0 and p ∉ N_G for infinitely many primes p, then e = 0 or 1 [for any idempotent e ∈ K[G]]."

## What Remains Open

1. **Zero-divisor conjecture** for torsion-free groups not in the proved families (hyperbolic char 0, locally indicable, etc.). The Gardam counterexample does NOT give a ZDC counterexample.
2. **Idempotent conjecture** beyond the Formanek families.
3. Whether P itself satisfies ZDC and IC (the counterexample group has non-trivial units but may still have no zero-divisors or non-trivial idempotents).
4. The embedding conjecture (Conjecture 1.183): whether K[G] embeds in a skew field for all torsion-free G satisfying ZDC.

## Assumptions

- G is torsion-free (all three conjectures require this; torsion groups have trivial zero-divisors (1+g+...+gⁿ⁻¹)(g-1) = 0).
- K is a field.

## Relevance to Mixer/B(2,5)

Methodological bridge only. B(2,5) is a torsion group (every element has order dividing 5); Kaplansky conjectures require torsion-free groups. Relevance is via the SAT-encoding method (§1.6): encoding an algebraic existence problem as Boolean SAT and using CDCL solvers is directly analogous to the computational-search approach explored in the Mixer context. The semidecidability framing (any YES instance is eventually found) is a model for how to structure search in the Mixer framework.

## Related material in vault

- Extends: (none directly — new addition to the vault)
- Concept hubs: [[Concepts/kaplansky-unit-conjecture]] (unit conjecture hub), [[Concepts/kaplansky-zero-divisors]] (zero-divisor hub)
- Companion papers: [[gardam-semidecidable-2021]] (SAT encoding methodology), [[murray-2021-kaplansky-char-p]] (char p extension), [[gardam-2024-kaplansky-char-zero]] (char 0 extension), [[mineyev-2024-kaplansky-origami]] (topology/geometry approach)
- Existing vault context: [[kaplansky-zero-divisors]] (Open problems note — was the only Kaplansky note before this batch)
- MOC: [[Research/Group theory/_MOCs/_moc-word-problem]] (word problem and group ring decidability)
