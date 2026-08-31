---
title: "Learning the symmetric group: large from small"
authors:
  - "Max Petschack"
  - "Alexandr Garbali"
  - "Jan de Gier"
year: 2025
venue: "Advances in Theoretical and Mathematical Physics, Vol. 30 (2026), pp. 65-81; arXiv:2502.12717"
url: "https://arxiv.org/abs/2502.12717"
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
cited_by: []
related:
  - "[[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]"
  - "[[Research/AI in Math/ML/gukov-2020-learning-to-unknot]]"
quality_notes: "The only paper found in this scan that trains a transformer directly on group WORDS (sequences of generators) with the explicit goal of length/size generalization. Read via ar5iv full text by research subagent."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/tokenization
  - topic/length-generalization
  - paper
  - status/draft
status: draft
---

# Learning the symmetric group: large from small

## Abstract

"Machine learning explorations can make significant inroads into solving difficult problems in pure mathematics. One advantage of this approach is that mathematical datasets do not suffer from noise, but a challenge is the amount of data required to train these models and that this data can be computationally expensive to generate. Key challenges further comprise difficulty in a posteriori interpretation of statistical models and the implementation of deep and abstract mathematical problems. We propose a method for scalable tasks, by which models trained on simpler versions of a task can then generalize to the full task. Specifically, we demonstrate that a transformer neural-network trained on predicting permutations from words formed by general transpositions in the symmetric group S₁₀ can generalize to the symmetric group S₂₅ with near 100% accuracy. We also show that S₁₀ generalizes to S₁₆ with similar performance if we only use adjacent transpositions. We employ identity augmentation as a key tool to manage variable word lengths, and partitioned windows for training on adjacent transpositions. Finally we compare variations of the method used and discuss potential challenges with extending the method to other tasks."

## TL;DR

A transformer trained on words (sequences of transposition generators) in the symmetric group S₁₀ generalizes to S₂₅ with near-100% accuracy, using **identity augmentation** (padding shorter words with relation-preserving no-op transpositions to a fixed length) to handle variable-length input rather than ragged sequences or padding tokens, and **partitioned windows** for the adjacent-transposition variant. Output is a fixed-size object (one-line permutation notation), generated one token at a time.

## Problem

Whether a transformer trained on group words for a small symmetric group can generalize to a much larger symmetric group without retraining from scratch on the larger group's data (which is expensive to generate).

## Approach

Each generator-pair (a transposition) is packed into a single integer token (vocabulary 652 for general transpositions, 34 for adjacent-only transpositions). Variable-length input words are handled via **identity augmentation**: since inserting a transposition-of-itself (τ·τ = identity) or certain relation-preserving pairs doesn't change the represented permutation, shorter words are padded to a fixed target length N using such relation-preserving insertions rather than a generic pad token — i.e. the padding itself remains a valid, meaningful sequence in the group's generator alphabet. Output (a permutation) is fixed-size, generated autoregressively one token at a time.

## Key result

Near-100% accuracy generalizing S₁₀→S₂₅ (general transpositions) and S₁₀→S₁₆ (adjacent transpositions only), i.e. models trained on short words for a small group correctly predict the resulting permutation for much longer words in a much larger group.

## Assumptions

Output is a fixed-size object (permutation in one-line notation) even though input word length varies — this is a different shape from our task, where the *output itself* is a variable-length shortened word, not a fixed-size summary of the input.

## Limitations / scope

The paper's own explicit caveat: "there are other possible ways [the word] could be tokenized, but we observed the one here works best" — i.e. no systematic tokenization ablation is reported, this is an empirical best-found choice, not a swept comparison (contrast with [[charton-2022-linear-algebra-transformers]], which does report a controlled sweep). Identity augmentation is specific to groups where relation-preserving no-op insertions exist and are cheap to construct — B(2,5)'s relations (order-5 torsion + free generation) would need their own analog, not a direct port.

**Implementation-level detail (confirmed via ar5iv full text, Deep Round 2 scan, §3 "Variable word length and identity augmentation"):** words of reduced length ℓ < N are "augmented with sufficiently many transpositions that amount to identities under group relations" to reach a fixed target length N. The paper does **not** specify which specific relations generate the no-op insertions, does not describe placement (random vs. structured within the word), does not say whether the augmentation is refreshed per epoch or fixed per example, and explicitly punts on distributional side-effects: their own framing is that "the transformer will need to learn the group relations" from the augmented data, not that augmentation is representationally neutral. **This means identity augmentation is a design note, not an ablated technique** — the paper reports it works end-to-end but gives no controlled comparison against a generic pad token, and no B(2,5)-specific analog (e.g. inserting `aA`/`Bb` free-cancellation pairs, or an order-5 relator cycle) has any precedent-level implementation detail to copy. Any B(2,5) analog would be extrapolating past what this source actually specifies, not applying a validated recipe.

## Replication evidence

Not independently assessed in this pass.

## Why this paper matters

It is the only source in this scan where a transformer operates directly on **group-generator words** (not adjacency matrices, not numbers, not knot diagrams) — closest in object-type to a B(2,5) word over {a,b,A,B}, even though the *task* (predict a fixed-size resultant permutation) differs sharply from ours (produce a shorter word in the same alphabet). The "identity augmentation" trick — using relation-preserving generator insertions instead of a generic padding token — is a reusable idea worth flagging to Developer/Math-expert: an analogous B(2,5)-specific padding scheme (e.g., inserting genuinely-trivial subwords like `aA` or a full order-5 relator cycle) could keep training-batch padding "on-distribution" rather than introducing an out-of-alphabet pad symbol.

## Quotes

1. > "there are other possible ways w could be tokenized, but we observed the one here works best" — on tokenization choice, no ablation reported

## Open questions surfaced

Whether an identity-augmentation-style padding scheme (using B(2,5)-relation-preserving generator insertions rather than a null pad token) would help or hurt a decoder-only GPT trained on variable-length B(2,5) words — untested, but a concrete, cheap idea to route to Developer if the raw-character-tokenization family is chosen.

## Related material in vault

- Related: [[Research/AI in Math/ML/gukov-2020-learning-to-unknot]] (closer task-shape analog: word simplification, not word→fixed-object prediction)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-value-scoring-curriculum-auxchannel]] (Deep Round 2 — re-reads this paper for the padding/curriculum threads)
