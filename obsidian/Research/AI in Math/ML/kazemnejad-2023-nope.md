---
title: "The Impact of Positional Encoding on Length Generalization in Transformers"
authors:
  - "Amirhossein Kazemnejad"
  - "Inkit Padhi"
  - "Karthikeyan Natesan Ramamurthy"
  - "Payel Das"
  - "Siva Reddy"
year: 2023
venue: "NeurIPS 2023; arXiv:2305.19466"
url: "https://arxiv.org/abs/2305.19466"
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
quality_notes: "Rigorous multi-scheme ablation (APE, T5 relative, ALiBi, RoPE, NoPE) across reasoning/math tasks. Strongest single source in this scan against learned absolute positional embeddings for local, offset-invariant pattern tasks — directly relevant since axplorer's model.py uses learned absolute wpe embeddings with a hard block_size cap."
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

# The Impact of Positional Encoding on Length Generalization in Transformers

## Abstract

"Length generalization, the ability to generalize from small training context sizes to larger ones, is a critical challenge in the development of Transformer-based language models. Positional encoding (PE) has been identified as a major factor influencing length generalization, but the exact impact of different PE schemes on extrapolation in downstream tasks remains unclear. In this paper, we conduct a systematic empirical study comparing the length generalization performance of decoder-only Transformers with five different position encoding approaches including Absolute Position Embedding (APE), T5's Relative PE, ALiBi, and Rotary, in addition to Transformers without positional encoding (NoPE). Our evaluation encompasses a battery of reasoning and mathematical tasks. Our findings reveal that the most commonly used positional encoding methods, such as ALiBi, Rotary, and APE, are not well suited for length generalization in downstream tasks. More importantly, NoPE outperforms other explicit positional encoding methods while requiring no additional computation. We theoretically demonstrate that NoPE can represent both absolute and relative PEs, but when trained with SGD, it mostly resembles T5's relative PE attention patterns. Finally, we find that scratchpad is not always helpful to solve length generalization and its format highly impacts the model's performance. Overall, our work suggests that explicit position embeddings are not essential for decoder-only Transformers to generalize well to longer sequences."

## TL;DR

A systematic, controlled ablation across five positional-encoding schemes on algorithmic/math reasoning tasks finds that NoPE (no explicit positional encoding at all) beats APE, T5-relative, ALiBi, and RoPE on length generalization, and that NoPE implicitly learns relative-position-like attention via gradient descent. Directly bears on whether a B(2,5) word transformer should use learned absolute positional embeddings (as axplorer's `model.py` does) for a task where the meaningful patterns (rewrite-rule LHS matches) are offset-invariant local motifs, not position-anchored ones.

## Problem

Which positional encoding scheme, if any, best supports decoder-only transformers generalizing to sequence lengths beyond (or different from) what they were trained on.

## Approach

Controlled empirical comparison: same decoder-only architecture, same training data, varying only the positional-encoding mechanism (APE, T5 relative, ALiBi, RoPE, NoPE), evaluated across a battery of reasoning/mathematical tasks including out-of-training-length test cases. Includes a theoretical argument for why NoPE can, in principle, represent both absolute and relative position information.

## Key result

"the most commonly used positional encoding methods, such as ALiBi, Rotary, and APE, are not well suited for length generalization"; "NoPE outperforms other explicit positional encoding methods while requiring no additional computation"; NoPE trained with SGD "mostly resembles T5's relative PE attention patterns" — i.e. it learns something functionally like relative position without being told to.

## Assumptions

Decoder-only architecture; tasks are algorithmic/mathematical reasoning (not natural language); "length generalization" here means train-short/test-long, which is a related but not identical concern to our case (we don't need to generalize beyond a fixed max length, but we do want offset-invariant local pattern recognition — the paper's finding that NoPE ≈ learned relative-position bias is the relevant mechanism, not the length-extrapolation framing per se).

## Limitations / scope

Doesn't test a fixed 4-symbol alphabet or a rewrite-rule-firing task specifically. "Explicit position embeddings are not essential" is stated for their task battery; whether it holds for a KB-rule-pattern-matching task is untested, this is transfer-by-analogy not a direct result.

## Replication evidence

Not independently assessed in this pass. Findings are consistent with a broader cluster of length-generalization papers surfaced in the same scan (Ruoss et al. 2023 "Randomized Positional Encodings," arXiv:2305.16843, DeepMind, found relative-position randomization gives +12.0% average accuracy on 15 algorithmic benchmarks; Jelassi et al. 2023, arXiv:2306.15400, found relative PE — not absolute — enables 5-digit→15-digit addition generalization). The convergent direction across three independent groups (avoid rigid absolute position) is stronger evidence than any single paper alone.

## Why this paper matters

axplorer's `model.py` (per Lead's `AXPLORER_REPRESENTATION_NOTES.md` code-grounding read) uses learned absolute positional embeddings (`wpe = Embedding(block_size, ...)`) with `block_size` as a hard cap — the opposite of what this cluster of evidence recommends for offset-invariant pattern tasks. This is a concrete, actionable finding for the representation-gate decision, independent of the tokenization-vocabulary question.

## Quotes

1. > "NoPE outperforms other explicit positional encoding methods while requiring no additional computation" — Abstract
2. > "mostly resembles T5's relative PE attention patterns" — Abstract, on NoPE trained with SGD

## Open questions surfaced

Whether NoPE (or relative PE) specifically helps a decoder-only GPT recognize a length-5–12 rewrite-rule LHS motif regardless of the character offset it appears at in a ~1348-char B(2,5) word — this exact task shape (offset-invariant local substring matching in a symbolic-rewriting context) is not tested by any paper in this scan.

## Related material in vault

- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
- Related: [[ruoss-2023-randomized-positional-encodings]] (the randomized-PE result discussed under Replication evidence above)
- Related: [[mehta-2026-randomized-yarn]] (extends randomized PE with a length curriculum; same length-generalization cluster)
- Cross-reference (not vault notes, cited inline in synthesis only): Jelassi et al. 2023 (arXiv:2306.15400), Zhou et al. 2024 (arXiv:2402.09371, caveats length-generalization fragility/seed-dependence even with the "right" PE choice)
