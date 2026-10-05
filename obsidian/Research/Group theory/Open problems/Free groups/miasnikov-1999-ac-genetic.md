---
title: "Genetic algorithms and the Andrews-Curtis conjecture"
authors:
  - "Alexei D. Miasnikov"
year: 1999
venue: "Internat. J. Algebra Comput. 9 (1999), 671–686; doi:10.1142/S0218196799000370 (arXiv:math/0304306, posted 2003)"
url: "https://arxiv.org/abs/math/0304306"
url_translated:
language: en
domain: group-theory
status: draft
methodology_type: empirical
citation_count: 38
citation_count_date: 2026-10-05
key_concepts:
  - "[[Concepts/andrews-curtis-moves]]"
  - "[[Concepts/certified-instance-generation]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[andrews-curtis-conjecture]]"
cited_by:
  - "[[shehper-2024-ac-hardness]]"
quality_notes: "Full arXiv text read (19 pp.). Citation count from Semantic Scholar (IJAC record). The broader claim that every two-generator balanced presentation of the trivial group of total length ≤ 12 is AC-trivialisable is credited in later literature (e.g. Carreras 2026 [11]) to the companion paper Miasnikov–Myasnikov, arXiv:math/0304305, not to this paper; this paper's Theorem 1 covers only the AK and Miller–Schupp series."
author: asetlearning
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/andrews-curtis
  - topic/proof-search
  - topic/computational-search-group-theory
  - topic/hard-instance-generation
  - topic/proof-certificates
  - project/challenge-gen
  - paper
  - status/draft
project: challenge-gen
---

# Genetic algorithms and the Andrews-Curtis conjecture

## Abstract

> "The Andrews-Curtis conjecture claims that every balanced presentation of the trivial group can be transformed into the trivial presentation by a finite sequence of "elementary transformations" which are Nielsen transformations together with an arbitrary conjugation of a relator. It is believed that the Andrews-Curtis conjecture is false; however, not so many possible counterexamples are known. It is not a trivial matter to verify whether the conjecture holds for a given balanced presentation or not. The purpose of this paper is to describe some non-deterministic methods, called Genetic Algorithms, designed to test the validity of the Andrews-Curtis conjecture. Using such algorithm we have been able to prove that all known (to us) balanced presentations of the trivial group where the total length of the relators is at most 12 satisfy the conjecture. In particular, the Andrews-Curtis conjecture holds for the presentation <x,y|x y x = y x y, x^2 = y^3> which was one of the well known potential counterexamples."

## TL;DR

This is the first heuristic-search attack on AC-trivialisation. A genetic algorithm evolves sequences of AC moves, Whitehead automorphisms and auxiliary conjugations, with relator length as the fitness. It finds a 21-move AC-trivialisation of AK(2) = ⟨x, y | xyx = yxy, x² = y³⟩ and verifies all AK and Miller–Schupp presentations of total length ≤ 12. Every solution is printed as an explicit move chain. The testing section also generates benchmark instances by random AC moves from the trivial presentation, an early "known-solution" generator.

## Problem

Is a given balanced presentation of the trivial group AC-equivalent to the trivial presentation? Exhaustive enumeration is hopeless: there are 3n² elementary moves, and (3n²)^k sequences of length k. For the 21-move AK(2) solution that means "12²¹ ≈ 4.6∗10²² sequences of transformations" (§1). Meet-in-the-middle cuts this to ≈ 12¹¹ but needs "more than 60 Gb" of fast memory. Plain enumeration on a 500 MHz Alpha reached only length 7 in two days (§1).

## Approach

- **Search space (§3.1).** Population members are finite sequences over T′, a set of 8n² − 2n transformations: AC1–AC3, Whitehead automorphisms, conjugation by a single generator x_j^{±1}, and random cyclic permutation of a relator. **Lemma 1** shows that any T-sequence reaching (x₁, …, x_n) can be converted into a pure AC1–AC3 sequence, so Whitehead moves are a sound shortcut.
- **Fitness (§3.2).** Three variants. Fit1 = sum of lengths of the n − 1 shortest relators; it terminates when these are primitive (checked by Whitehead's algorithm), since for n = 2 one primitive relator suffices. Fit2 = total relator length; it terminates at total length n. Fit3 = Fit2 + k/m, which penalises the sequence length k to obtain shorter solutions.
- **Operators (§3.3–3.4).** One-point crossover. Mutations M1–M4 (append, insert, delete, change), biased toward M1. Roulette-wheel selection on squared fitness. Replacement of everything except the fittest member; elitist replacement suffered "premature convergence".
- **Parameters (§4).** Population 50, mutation probability 95%, crossover probability 85%.
- **Tests (§4).** Known AC-trivial families from Burns–Macedońska, plus "automatically generated presentations ... obtained by transforming the trivial presentation < x, y; x, y > by a random sequence of transformations (AC1)-(AC3)".

## Key result

- **Theorem 1 (§5).** "All presentations from the series (3) and (4) with the total length of relators at most 12 satisfy the Andrews-Curtis conjecture." Series (3) is ⟨x, y; xⁿ = yⁿ⁺¹, xyx = yxy⟩, n ≥ 2 (Akbulut–Kirby). Series (4) is ⟨x, y; x⁻¹yⁿx = yⁿ⁺¹, x = w⟩ (Miller–Schupp). "Altogether there are 273 presentations with the total length ≤ 12 in these series."
- **AK(2) is AC-trivial (§5).** A 19-step chain (21 elementary moves once step 9 is expanded into AC3′/AC3″) reduces ⟨a, b; aba = bab, a² = b³⟩ to the trivial presentation. The chain is printed in full.
- **Hardest MS cases (§5).** ⟨x, y; x⁻¹y²x = y³, x = y^{±1}xy^{±1}x⁻¹⟩ are "the most interesting and hard to crack in the series (4)". An explicit 19-step chain is given for G₂, and an explicit reduction of G₃ to G₁ (= AK(2)).
- **AK(n), n > 2 (§5, Remark).** "No positive results have been obtained for presentations of the series (3) with n > 2. In all tested cases (n = 3, 4, 7, 11) the least length of a relator was 5 but the total length of the relators never was reduced."
- **Table 1 (§4), generated instances (random AC1–AC3 walks from ⟨x, y; x, y⟩, 50 examples per row):**

  | Length of generating sequence | Avg. sum of relator lengths | Avg. generations to solve | Examples |
  |---|---|---|---|
  | 10 | 13 | 20 | 50 |
  | 20 | 32 | 300 | 50 |
  | 30 | 78 | 2208 | 50 |

- **Planting on a hard seed (§4).** Random T-sequences were applied to a potential counterexample G_t ("more often ... < a, b; aba = bab, a³ = b⁴ >"), producing longer AC-equivalent presentations. "It is interesting to mention that in all cases the algorithm converged to the original presentation G_t."
- **Proposition 1 (§6).** If G = ⟨a, b; r, s⟩ and H = ⟨a, b; u, v⟩ present the trivial group and G is AC-trivial, then G(H) = ⟨a, b; r(u, v), s(u, v)⟩ is AC-equivalent to H. The proof is constructive: the AC sequence for G is transported by substituting w(u, v) for conjugators. With the 13-move trivialisation of ⟨a, b; b⁻¹ab = a², a⁻¹ba = b²⟩ (written a^b = a², b^a = b²; relators r₀ = b⁻¹aba⁻², r₁ = a⁻¹bab⁻²), this recovers B. H. Neumann's trick ⟨a, b; r^s = r², s^r = s²⟩ ∼_AC H.

## Assumptions

- Only the strong form of AC is used (AC1–AC4, no stabilisation AC5). The author found that adding AC5 did not help (§1).
- "All known (to us)" in the abstract refers to the two named presentations and the AK and MS series. The paper does not enumerate all balanced presentations of length ≤ 12.
- GA hyperparameters were hand-tuned and are "very sensitive" (§4).

## Limitations / scope

- The method is a semi-decision procedure: success yields a certificate, while failure says nothing about AC-nontriviality.
- The paper gives no wall-clock or generation counts for the §5 hard cases, only for the synthetic Table 1.
- No progress on AK(3) or larger AK(n).

## Replication evidence

Partial. AK(2)'s AC-triviality was confirmed independently by breadth-first search (Havas–Ramsay 2003, as cited in Shehper et al. §2), and Shehper et al. cite this paper as the source of the result. The length-≤ 12 frontier statement is now attributed to Miasnikov–Myasnikov (math/0304305) and paired with Havas–Ramsay's length-13 result (see [[carreras-2026-ac-certificates]] §1).

## Why this paper matters

This is the origin of the computational-search line on AC: GA (here), then BFS (Havas–Ramsay), then automated deduction (Lisitsa), then RL (Shehper et al. 2024), then certified search (Carreras 2026). It established the "length as fitness / heuristic" paradigm that all later engines inherit, and AK(2) is now a standard sanity check. Proposition 1 is a clean, constructive way to propagate a single certificate into an infinite family.

**Relevance to challenge-gen:** This paper contains the earliest explicit instance generator with a built-in certificate in this literature. Table 1 generates AC-trivial presentations by random AC walks from the trivial presentation, and difficulty for the GA grows steeply with walk length: 20 → 300 → 2208 generations for 10/20/30 moves. It also gives a cautionary result: padding a hard seed (an AK-type presentation) with random moves produced instances the GA always undid back to the seed. Random scrambling of a seed is therefore easily reversed by a length-greedy solver, and does not by itself create new hardness. Proposition 1's substitution G(H) is a provably correct composition operator for building certified families of instances.

## Quotes

1. > "in all cases the algorithm converged to the original presentation G_t." — §4
2. > "we do not know of any example of a presentation which is AC-equivalent to the trivial presentation where our genetic algorithms failed to work." — §4

## Open questions surfaced

- AK(n) for n ≥ 3: is the total length reducible at all? Shehper et al. 2024 later showed it is for n ≥ 5 (to n + 11). AK(3) remains open.
- Can GA hyperparameters be self-adjusted at run time? The author says he was "unable to come up with effective methods for doing so" (§4).
- How does Table 1's solver effort scale beyond 30 random moves, and with solvers other than the GA?

## Related material

- Parent: [[andrews-curtis-conjecture]] (problem statement, AK(n) candidates)
- MOC: [[_moc-hard-instance-generation]], [[_moc-word-problem]]
- Cited by (in vault): [[shehper-2024-ac-hardness]] (RL successor; cites this as [Mia03] for AK(2) and GA search)
- Later certified search on the same frontier: [[carreras-2026-ac-certificates]] (cites the companion paper math/0304305 for the length-12 frontier)
- Open-problem context: [[open-problems-catalog]]
- Hard-instance generation siblings: [[elder-2015-random-trivial-words]] (sampling trivial words with known triviality), [[kapovich-2003-generic-case-complexity]] (why random instances are easy)
- Batch synthesis: [[_synthesis-hard-instance-generation]]
- Project: [[project-challenge-gen]]
