---
title: Andrews–Curtis Moves
author: asetlearning
language: en
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/andrews-curtis
  - topic/computational-search-group-theory
  - topic/hard-instance-generation
  - project/challenge-gen
  - concept
  - status/draft
introduced_in:
  - "[[andrews-curtis-conjecture]]"
related_concepts:
  - "[[Concepts/certified-instance-generation]]"
appears_in:
  - "[[andrews-curtis-conjecture]]"
  - "[[miasnikov-1999-ac-genetic]]"
  - "[[shehper-2024-ac-hardness]]"
  - "[[carreras-2026-ac-certificates]]"
---

# Andrews–Curtis Moves

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

Let ⟨x₁, …, xₙ | r₁, …, rₙ⟩ be a **balanced** presentation (as many relators as generators). The **AC moves** on the relator tuple are:

- **AC1:** replace rᵢ by rᵢ rⱼ (j ≠ i);
- **AC2:** replace rᵢ by rᵢ⁻¹;
- **AC3:** replace rᵢ by g rᵢ g⁻¹, with g a generator or its inverse (equivalently any word, by iterating).

Some formulations add automorphisms of the free group (Nielsen moves on the generators) and the **stabilisation** moves (add or delete a generator xₙ₊₁ with relator xₙ₊₁), giving *stable* AC-equivalence. Two presentations are **AC-equivalent** if a finite sequence of moves connects them. A presentation is **AC-trivial** if it is AC-equivalent to ⟨x₁, …, xₙ | x₁, …, xₙ⟩. The Andrews–Curtis conjecture ([[andrews-curtis-conjecture]]) says every balanced presentation of the trivial group is AC-trivial.

**AC′ variant.** [[shehper-2024-ac-hardness]] uses AC′ moves: rᵢ → rᵢ rⱼ^{±1} (i ≠ j) and rᵢ → g rᵢ g⁻¹. Inversion is folded into concatenation; the move set generates the same transformations as AC1–AC3 (§2 there). [[miasnikov-1999-ac-genetic]] searches over a larger set T′ (AC1–AC3 plus Whitehead automorphisms and cyclic permutations) and proves (Lemma 1) that any T-sequence to the trivial presentation converts to a pure AC1–AC3 sequence.

## Why it matters

An AC-trivialisation is a **certificate**: a finite move sequence that anyone can replay to check the claim, with no group-theoretic oracle needed. That makes AC-triviality a natural "search-reducible" problem: hard to find, cheap to verify. [[carreras-2026-ac-certificates]] turns this into a publishing standard (replayable move ledgers plus a small independent verifier).

Running random moves *forwards* from the trivial presentation (or from a known seed) produces presentations whose AC-triviality is certified by the reversed walk. This is the AC case of [[Concepts/certified-instance-generation]], used by [[miasnikov-1999-ac-genetic]] (Table 1) and [[shehper-2024-ac-hardness]] (App. D).

## Where it appears

- Introduced in: [[andrews-curtis-conjecture]]
- Appears in: [[andrews-curtis-conjecture]], [[miasnikov-1999-ac-genetic]], [[shehper-2024-ac-hardness]], [[carreras-2026-ac-certificates]]
- Related concepts: [[Concepts/certified-instance-generation]]
- MOCs: [[_moc-hard-instance-generation]], [[_moc-word-problem]]

## Open questions

- How does the hardness of a random AC walk from a seed depend on walk length and length caps? Miasnikov's GA undid random padding of a hard seed back to the seed; Shehper et al. report that a seed's hardness signal survives thousands of moves.
- Which hardness measure on AC-trivial presentations (solver budget, path length, maximal length increase, barcode) is most stable across solvers?

## References

1. J. J. Andrews, M. L. Curtis, "Free groups and handlebodies", Proc. AMS 16 (1965), 192–195.
2. A. D. Miasnikov, "Genetic algorithms and the Andrews–Curtis conjecture", IJAC (1999).
3. A. Shehper et al., "What makes math problems hard for reinforcement learning: a case study" (2024).
