---
title: Quiet Planting
author: asetlearning
language: en
tags:
  - agent/research
  - user/asetlearning
  - domain/cs
  - topic/planted-solutions
  - topic/hard-instance-generation
  - topic/average-case-hardness
  - project/challenge-gen
  - concept
  - status/draft
introduced_in:
  - "[[krzakala-zdeborova-2009-quiet-planting]]"
related_concepts:
  - "[[Concepts/certified-instance-generation]]"
appears_in:
  - "[[krzakala-zdeborova-2009-quiet-planting]]"
  - "[[achlioptas-jia-moore-2004-hiding-assignments]]"
  - "[[2606.15979]]"
---

# Quiet Planting

> **Concept hub.** This note exists as a shared anchor — multiple paper summaries link here via their `key_concepts` frontmatter, so reading this gives the cross-paper view of one idea. Keep it short and authoritative. Long discussions go in paper notes, not here.

## Definition

A **planted** instance ensemble is built around a solution chosen first: draw a hidden assignment σ, then draw constraints conditioned on σ satisfying them. The planting is **quiet** when the planted ensemble is (statistically) indistinguishable from the uniform random ensemble of the same size and density, so that nothing in the instance's distribution betrays where σ is. Krzakala–Zdeborová (2009) show that the natural planting of graph q-colouring is quiet below a computable density, because the belief-propagation fixed point of the random ensemble is uniform. Random k-SAT has a non-uniform BP fixed point, so naive 1-hidden planting there is *not* quiet: the hidden assignment pulls solvers towards it ([[achlioptas-jia-moore-2004-hiding-assignments]]). Hiding a complementary pair (σ, σ̄) cancels the pull by symmetry. [[2606.15979]] gives the formal statistical-query (SQ) version for k-SAT with up to 2^t − 1 solutions of prescribed geometry.

## Why it matters

Planting is the standard way to get instances that are guaranteed solvable *and* come with the answer, while (one hopes) staying as hard as the random ensemble. Quietness is the property that makes the planted instance look generic, so solver performance on it transfers.

**Key caveat: indistinguishable ≠ hard.** Quietness is a statement about distributions, not about every algorithm. [[2606.15979]]'s SQ-quiet instances fall to Gaussian elimination unless noise is added. Achlioptas–Jia–Moore's 2-hidden formulas are shown to be about as hard as *unplanted* random 3-SAT of the same size and density: the symmetry removes the planted solution's bias, but the hardness is inherited from the random ensemble, not created by the planting.

**Generalisation to challenge-gen.** The analogue for `#project/challenge-gen` is a generator of *certified* trivial words (or AC-trivial presentations) whose distribution is close to that of generic hard instances, so a solver cannot exploit the generation process. See [[Concepts/certified-instance-generation]] and [[project-challenge-gen]].

## Where it appears

- Introduced in: [[krzakala-zdeborova-2009-quiet-planting]]
- Appears in: [[krzakala-zdeborova-2009-quiet-planting]], [[achlioptas-jia-moore-2004-hiding-assignments]], [[2606.15979]]
- Related concepts: [[Concepts/certified-instance-generation]]
- MOC: [[_moc-hard-instance-generation]]

## Open questions

- Is there a quiet planting for trivial words in a finitely presented group, i.e. a certified sampler whose output distribution matches the length-uniform law on trivial words of [[elder-2015-random-trivial-words]]?
- Which quiet ensembles stay hard against *all* polynomial-time algorithms, not just SQ / local ones?

## References

1. F. Krzakala, L. Zdeborová, "Hiding quiet solutions in random constraint satisfaction problems", PRL 102 (2009).
2. D. Achlioptas, H. Jia, C. Moore, "Hiding satisfying assignments: two are better than one", AAAI 2004 / JAIR 24 (2005).
3. A. Ahmadi et al., "Quiet planting for k-SAT, multiple solutions of arbitrary geometry", arXiv:2606.15979 (2026).
