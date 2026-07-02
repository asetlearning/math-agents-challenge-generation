---
title: "Kaplansky Unit Conjecture — Refuted"
domain: group-theory
project: none
status: draft
author: maumayma
related:
  - "[[Concepts/kaplansky-zero-divisors]]"
introduced_in:
  - "[[Research/Group theory/Open problems/Group rings/gardam-2023-kaplansky-survey]]"
appears_in:
  - "[[Research/Group theory/Open problems/Group rings/gardam-2023-kaplansky-survey]]"
  - "[[Research/Group theory/Open problems/Group rings/gardam-semidecidable-2021]]"
  - "[[Research/Group theory/Open problems/Group rings/murray-2021-kaplansky-char-p]]"
  - "[[Research/Group theory/Open problems/Group rings/gardam-2024-kaplansky-char-zero]]"
  - "[[Research/Group theory/Open problems/Group rings/mineyev-2024-kaplansky-origami]]"
  - "[[Research/Group theory/Open problems/Group rings/kaplansky-zero-divisors]]"
related_concepts:
  - "[[Concepts/kaplansky-zero-divisors]]"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/group-rings
  - topic/kaplansky-unit-conjecture
  - concept
  - status/draft
---

# Kaplansky Unit Conjecture — Refuted

> The unit conjecture is FALSE. Gardam 2021 (char 2), Murray 2021 (all prime char), Gardam 2024 (char 0). The zero-divisor and idempotent conjectures remain OPEN.

**See also:** [[Concepts/kaplansky-zero-divisors]] for the zero-divisor conjecture hub.

## The Conjecture (Higman 1940 / Kaplansky 1970)

For a **torsion-free group** G and a **field** K:

> **The only units in K[G] are the trivial units** — elements of the form kg where k ∈ K× and g ∈ G.

Formally: if α, β ∈ K[G] with αβ = βα = 1, then α = kg for some k ∈ K×, g ∈ G.

First stated by Higman in his 1940 thesis. Popularized by Kaplansky around 1970. Open for ~80 years before Gardam's 2021 counterexample.

## The Three Kaplansky Conjectures and Their Implication Chain

For torsion-free G and field K:

| Conjecture | Statement | Status |
|---|---|---|
| **Unit (UC)** | Only trivial units in K[G] | **FALSE** — Gardam 2021 |
| **Zero-divisor (ZDC)** | No zero-divisors in K[G] | **OPEN** |
| **Idempotent (IC)** | No non-trivial idempotents in K[G] | **OPEN** |

**Implication chain:** UC → ZDC → IC (Passman; trivial for ZDC→IC)

- UC → ZDC: Passman [Pas85, Lemma 13.1.2]. If K[G] satisfies UC, it has no zero-divisors.
- ZDC → IC: e(1-e) = 0 for any idempotent e, so no zero-divisors forces e = 0 or 1.
- UC is STRONGEST; IC is WEAKEST.
- **Gardam's counterexample to UC does NOT give a counterexample to ZDC or IC.**

**Directly finite** (αβ = 1 =⇒ βα = 1): proved for ALL group rings, not a conjecture.

## The Counterexample

**Group:** The Hantzsche-Wendt crystallographic group (also called Promislow's group):
$$P = \langle a, b \mid b^{-1}a^2b = a^{-2},\; a^{-1}b^2a = b^{-2} \rangle$$

P is torsion-free (Gardam 2021). P does NOT have the unique product property (Promislow 1988). The index-4 subgroup ⟨x,y,z⟩ with x = a², y = b², z = (ab)² is isomorphic to Z³.

**Field and unit:**
- Char 2: non-trivial unit in F₂[P] with support of **21 elements** — Gardam, *Annals of Mathematics* 2021
- Char p: non-trivial unit in F_d[P] for every prime d — Murray, arXiv 2021
- Char 0: non-trivial unit in ℂ[P] with coefficients in Z[ζ₈] — Gardam, arXiv 2024

**How found:** Boolean satisfiability. Encoded αβ = 1 over F₂[B(n)] as CNF. At n=5 (|B(5)| = 147 elements), CDCL SAT solver found the 21-element support unit. See [[Research/Group theory/Open problems/Group rings/gardam-semidecidable-2021]] for the SAT methodology.

## Group Families Where UC (and ZDC) Are Proved

UC follows from the unique product property (UP). Groups with UP:
- **Locally indicable groups:** free groups, fundamental groups of surfaces χ<0, torsion-free nilpotent, torsion-free one-relator — Higman 1940, Brodskii, Howie
- **Left-orderable groups:** locally indicable =⇒ left-orderable =⇒ UP
- **Diffuse groups:** left-orderable =⇒ diffuse =⇒ UP (Delzant/Bowditch)
- **Residually finite hyperbolic groups** (virtually diffuse)
- **Bi-orderable groups** (=⇒ locally indicable)

ZDC additionally proved for hyperbolic groups in char 0 (via Delzant's theorem), CAT(0) groups (via Formanek's idempotent theorem).

## What Remains Open (2026)

1. **ZDC** for general torsion-free groups, including P itself (the Gardam counterexample group).
2. **IC** for general torsion-free groups beyond Formanek's families.
3. Whether ZDC/IC hold for ALL orderable groups, hyperbolic groups in char p, etc.
4. The **embedding conjecture**: K[G] embeds in a skew field for torsion-free G satisfying ZDC.
5. Whether there exists a torsion-free group with zero-divisors in its group ring.

## Idempotent Conjecture — Partial Results

No separate concept hub created; IC coverage lives here.

The IC is proved for groups with |N_G| < ∞ where N_G = {primes p | ∃g ∈ G\{1}, n ∈ Z⁺ s.t. g ~ gᵖⁿ} (Formanek's theorem, 1973). This covers:
- Finitely generated subgroups of GL_n(F)
- Hyperbolic groups
- CAT(0) groups
- Mapping class groups and Out(Fₙ) (torsion-free subgroups)

The trace method (Zalesskii's theorem: tr(e) ∈ prime subfield for any idempotent e) + Formanek's theorem is the standard approach.

## Topological/Geometric Search Framework

Mineyev's "origami" paper ([[Research/Group theory/Open problems/Group rings/mineyev-2024-kaplansky-origami]]) proposes a systematic framework: encode candidate counterexample support structure as a "product structure" Π, build a 2-complex Y_Π, check CAT(0) geometry (which proves torsion-freeness), and read off units/zero-divisors. This directly targets ZDC as well as UC.

## Relevance to Mixer/B(2,5)

**METHODOLOGICAL ONLY.** B(2,5) is torsion (exponent 5); Kaplansky conjectures require torsion-free groups. No direct Mixer target.

The Mixer-relevant insight: the SAT-based search that found the counterexample is a model for computational search in the Mixer context. Encoding an algebraic existence problem as NP (SAT) and solving with CDCL is analogous to the Mixer's KB rule-injection search. See [[Research/AI in Math/ML/charton-2024-patternboost]] for the PatternBoost paradigm, which is the closest ML analog.

## Cross-links

- Zero-divisor conjecture hub: [[Concepts/kaplansky-zero-divisors]]
- Primary survey: [[Research/Group theory/Open problems/Group rings/gardam-2023-kaplansky-survey]]
- SAT methodology: [[Research/Group theory/Open problems/Group rings/gardam-semidecidable-2021]]
- Char-p extension: [[Research/Group theory/Open problems/Group rings/murray-2021-kaplansky-char-p]]
- Char-0 extension: [[Research/Group theory/Open problems/Group rings/gardam-2024-kaplansky-char-zero]]
- Topology approach: [[Research/Group theory/Open problems/Group rings/mineyev-2024-kaplansky-origami]]
- Original open-problems note: [[Research/Group theory/Open problems/Group rings/kaplansky-zero-divisors]]
