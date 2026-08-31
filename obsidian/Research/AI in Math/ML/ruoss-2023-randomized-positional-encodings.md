---
title: "Randomized Positional Encodings Boost Length Generalization of Transformers"
authors:
  - "Anian Ruoss"
  - "Grégoire Delétang"
  - "Tim Genewein"
  - "Jordi Grau-Moya"
  - "Róbert Csordás"
  - "Mehdi Bennani"
  - "Shane Legg"
  - "Joel Veness"
year: 2023
venue: "arXiv:2305.16843 (cs.LG), DeepMind"
url: "https://arxiv.org/abs/2305.16843"
url_translated:
language: en
methodology_type: empirical
domain: ai
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[mehta-2026-randomized-yarn]]"
related:
  - "[[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]"
  - "[[kazemnejad-2023-nope]]"
quality_notes: "Read via ar5iv full text (Deep Round 2 scan, R3). Implementation-level mechanism confirmed: sampling is per-batch (not per-example), the random index set is ORDERED (sorted ascending) before use — this preserves relative token order, it is not a shuffle — and sorting is itself ablated as essential (+15.7% vs. unsorted). Composes with a length curriculum per [[mehta-2026-randomized-yarn]]'s later ablation."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/length-generalization
  - topic/tokenization
  - paper
  - status/draft
status: draft
---

# Randomized Positional Encodings Boost Length Generalization of Transformers

## Abstract

"Transformers have impressive generalization capabilities on tasks with a fixed context length. However, they fail to generalize to sequences of arbitrary length, even for seemingly simple tasks such as duplicating a string. Moreover, simply training on longer sequences is inefficient due to the quadratic computation complexity of the global attention mechanism. In this work, we demonstrate that this failure mode is linked to positional encodings being out-of-distribution for longer sequences (even for relative encodings) and introduce a novel family of positional encodings that can overcome this problem. Concretely, our randomized positional encoding scheme simulates the positions of longer sequences and randomly selects an ordered subset to fit the sequence's length. Our large-scale empirical evaluation of 6000 models across 15 algorithmic reasoning tasks shows that our method allows Transformers to generalize to sequences of unseen length (increasing test accuracy by 12.0% on average)."

## TL;DR

At each training step, sample a target length n uniformly from {1,...,N}, then draw an ordered (sorted-ascending) random subset of size n from a much larger position range L (L ≫ N — e.g. L=2048 vs. training N=40) and use those as the position labels for the actual sequence. This is NOT a shuffle: relative token order is fully preserved, only the absolute position labels are stretched/perturbed to simulate what longer sequences "look like" positionally during training. Across 6000 models / 15 algorithmic benchmarks, this improves length-generalization accuracy by +12.0% on average over standard positional encodings (including relative encodings, which the paper shows are ALSO out-of-distribution for longer sequences, not just absolute ones).

## Problem

Transformers trained at a fixed context length fail to generalize to longer sequences at test time, even for simple tasks (e.g. string duplication). The paper diagnoses this as a positional-encoding distribution-shift problem: whatever position values a model saw during training, it has never seen the LARGER position values that appear in longer test sequences — true for absolute encodings, but the paper shows it's also true for relative encodings in the (out-of-training-range) relative-distance sense.

## Approach

Per training step (not per example): sample target length n ~ Uniform({1,...,N}); sample an index set I of size n from an extended position range {1,...,L} with L ≫ N; **sort I ascending**; assign these sorted positions as the position labels for the n tokens of the actual training sequence, preserving their original left-to-right token order. At test time on a sequence of the true (possibly longer) length, positions are drawn analogously from the same extended range. Ablates the sorting step specifically: unsorted (randomly permuted) index assignment loses relative token order and hurts accuracy substantially relative to the sorted variant.

## Key result

"improving average test accuracy by 12.0%" across 6000 models / 15 algorithmic reasoning tasks, compared to standard (non-randomized) positional encoding schemes. Sorting the sampled index set (vs. leaving it unsorted) contributes +15.7 percentage points on its own (per subagent extraction from ar5iv full text — this specific delta not independently re-verified against primary text by Researcher in this pass, flagged for confidence).

## Assumptions

Decoder or encoder transformers on algorithmic reasoning tasks; the extended position range L must be chosen large enough to cover the true test-time length range; adopts Delétang et al.'s (arXiv:2207.02098) uniform-length-sampling scheme as its length-sampling component, so length-randomization and position-randomization are used together in the source paper, not analyzed as fully separable ablation arms.

## Limitations / scope

Benchmarks are about generalizing to LONGER inputs of the same underlying task (e.g., duplicate a longer string than seen in training) — not about offset-invariant LOCAL pattern recognition within a fixed-length sequence, which is our actual B(2,5) concern (a rule-LHS motif means the same thing regardless of where in a ~1348-char word it starts, independent of whether the word itself is longer than training examples). The paper provides **no direct test** of this distinction; applying it to our rule-firing-alignment problem is an extrapolation, not a result the paper itself establishes.

## Replication evidence

[[mehta-2026-randomized-yarn]] (2026) directly tests this technique (as "Randomized" positional variant) in combination with a length curriculum and finds both components load-bearing (degrading substantially — "up to 18.3%" — without the curriculum) — a genuine, quantified replication-plus-extension in a follow-up paper, not just a citation.

## Why this paper matters

This is the primary source behind the length-generalization / positional-encoding recommendation carried over from Phase A ([[kazemnejad-2023-nope]] synthesis), now read at implementation depth rather than abstract-level. The critical new detail for our design: the technique is an ORDERED subsequence sample, not a shuffle — a naive "just randomize positions" implementation that doesn't sort would likely fail per the paper's own sorting ablation. If Developer implements this for the B(2,5) transformer, the sort-preserving-relative-order step is not optional.

## Quotes

1. > "our randomized positional encoding scheme simulates the positions of longer sequences and randomly selects an ordered subset to fit the sequence's length" — Abstract
2. > "improving average test accuracy by 12.0%" — Abstract

## Open questions surfaced

Whether randomized positional encoding (as opposed to NoPE, [[kazemnejad-2023-nope]]'s recommendation) specifically helps OFFSET-INVARIANT local pattern matching (our actual concern) as opposed to length-of-longer-sequence generalization (this paper's tested concern) — these may or may not be the same underlying mechanism, and no source in this scan tests the offset-invariance framing directly.

## Related material in vault

- Cited by (in this vault): [[mehta-2026-randomized-yarn]] (composes RPE with a length curriculum, quantified)
- Related: [[kazemnejad-2023-nope]] (alternative recommendation — NoPE — for a related but distinct problem framing)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
