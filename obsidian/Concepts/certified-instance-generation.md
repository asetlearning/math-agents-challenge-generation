---
title: Certified Instance Generation
author: asetlearning
language: en
tags:
  - agent/research
  - user/asetlearning
  - domain/methodology
  - topic/hard-instance-generation
  - topic/planted-solutions
  - topic/trivial-words
  - topic/andrews-curtis
  - topic/curriculum-learning
  - project/challenge-gen
  - concept
  - status/draft
introduced_in:
  - "[[miasnikov-1999-ac-genetic]]"
related_concepts:
  - "[[Concepts/quiet-planting]]"
  - "[[Concepts/andrews-curtis-moves]]"
appears_in:
  - "[[miasnikov-1999-ac-genetic]]"
  - "[[shehper-2024-ac-hardness]]"
  - "[[elder-2015-random-trivial-words]]"
  - "[[2607.26241]]"
  - "[[krzakala-zdeborova-2009-quiet-planting]]"
  - "[[achlioptas-jia-moore-2004-hiding-assignments]]"
  - "[[2606.15979]]"
  - "[[dennis-2020-paired]]"
---

# Certified Instance Generation

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

**Certified instance generation** produces problem instances by a process whose trace *is* the proof that the instance has the target property (solvable, trivial, AC-trivial). The generator never has to solve the instance; it builds the instance and its certificate together. This is the core idea of [[project-challenge-gen]]: hard instances that ship with a built-in proof.

Patterns in the vault:

- **Random walk from a known solution, reversed.** Apply random moves to a solved object; the reversed walk certifies the result. [[miasnikov-1999-ac-genetic]] (Table 1: random AC1–AC3 walks from ⟨x, y; x, y⟩) and [[shehper-2024-ac-hardness]] (App. D / Algorithm 6: random AC′ walks from 1190 Miller–Schupp seeds, about 1.8M presentations, each certified AC-equivalent to its seed). See [[Concepts/andrews-curtis-moves]].
- **Markov chain over certified moves.** [[elder-2015-random-trivial-words]]: a Metropolis chain on trivial words moving by conjugation and relator insertion. Every state is trivial by construction, and a trajectory from the empty word is a product-of-conjugates derivation (Lemma 2.3).
- **Tangling.** [[2607.26241]] (WPNet): trivial training words built by inserting free pairs and relators, at most 150 operations, so area ≤ 150.
- **Planting.** [[krzakala-zdeborova-2009-quiet-planting]], [[achlioptas-jia-moore-2004-hiding-assignments]], [[2606.15979]]: choose the solution first, then draw constraints it satisfies. See [[Concepts/quiet-planting]].
- **Regret-witnessed solvability.** [[dennis-2020-paired]] (PAIRED): an adversary generates environments, and solvability is witnessed empirically by an antagonist agent that solves them. This is a weaker, empirical certificate.

## Why it matters

Benchmarks and training sets for search algorithms need instances whose answer is known, and they are only useful if the instances are hard. Generic random instances are almost always easy or have a trivially-decided answer: [[kapovich-2003-generic-case-complexity]] shows trivial words have density zero, so a random word is almost surely non-trivial and quickly certified so. Certified generation sidesteps the need for a solver, but leaves hardness to be engineered.

**Recurring failure mode.** Naive certified generators produce either generic, easy instances or shallow scrambles that a greedy solver undoes. [[miasnikov-1999-ac-genetic]] §4: padding a hard seed with random moves produced presentations the GA always reduced back to the seed. [[elder-2015-random-trivial-words]]'s stationary law is length-uniform, the trivial-word analogue of "generic". [[2607.26241]]'s tangled words have bounded area, so the exponential Dehn function cited as motivation is never exercised. On the SAT side, quiet planting can still be easy ([[2606.15979]] falls to Gaussian elimination without noise). Learned samplers such as [[sato-2019-hisampler]] do maximise solver cost, but give no certificate.

## Where it appears

- Introduced in: [[miasnikov-1999-ac-genetic]] (earliest explicit certified generator in this literature)
- Appears in: [[miasnikov-1999-ac-genetic]], [[shehper-2024-ac-hardness]], [[elder-2015-random-trivial-words]], [[2607.26241]], [[krzakala-zdeborova-2009-quiet-planting]], [[achlioptas-jia-moore-2004-hiding-assignments]], [[2606.15979]], [[dennis-2020-paired]]
- Related concepts: [[Concepts/quiet-planting]], [[Concepts/andrews-curtis-moves]]
- Project and reading path: [[project-challenge-gen]], [[_moc-hard-instance-generation]]

## Open questions

- Can a certified generator be biased towards hard instances (by certified area, solver cost, or learned hardness à la HiSampler/PAIRED) without the bias becoming a shortcut a solver can learn?
- Does hardness of a seed survive random certified moves (Shehper et al. §6.3 suggests yes for AC; Miasnikov §4 suggests random padding is undone)?

## References

1. A. D. Miasnikov, "Genetic algorithms and the Andrews–Curtis conjecture", IJAC 9 (1999).
2. M. Elder, A. Rechnitzer, E. J. Janse van Rensburg, "Random sampling of trivial words in finitely presented groups", Experimental Mathematics 24 (2015).
3. F. Krzakala, L. Zdeborová, "Hiding quiet solutions in random constraint satisfaction problems", PRL 102 (2009).
4. M. Dennis et al., "Emergent complexity and zero-shot transfer via unsupervised environment design", NeurIPS 2020.
