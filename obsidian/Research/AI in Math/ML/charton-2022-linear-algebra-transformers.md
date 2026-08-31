---
title: "Linear algebra with transformers"
authors: "François Charton"
year: 2022
venue: "Transactions on Machine Learning Research (TMLR); arXiv:2112.01898, first posted Dec 2021"
url: "https://arxiv.org/abs/2112.01898"
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
  - "[[charton-2024-patternboost]]"
related:
  - "[[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]"
quality_notes: "Same first author as PatternBoost — this is Charton's own controlled ablation of number-encoding schemes, the most directly load-bearing evidence for 'representation choice measurably changes accuracy' cited in the B25 tokenization synthesis. Read via ar5iv full text by research subagent, not just abstract."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/tokenization
  - topic/patternboost
  - paper
  - status/draft
status: draft
---

# Linear algebra with transformers

## Abstract

"Transformers can learn to perform numerical computations from examples only. I study nine problems of linear algebra, from basic matrix operations to eigenvalue decomposition and inversion, and introduce and discuss four encoding schemes to represent real numbers. On all problems, transformers trained on sets of random matrices achieve high accuracies (over 90%). The models are robust to noise, and can generalize out of their training distribution. In particular, models trained to predict Laplace-distributed eigenvalues generalize to different classes of matrices: Wigner matrices or matrices with positive eigenvalues. The reverse is not true."

## TL;DR

Charton directly ablates four numeric-encoding schemes (P10, P1000, B1999, floating-point FP15) for transformers doing linear algebra, and finds accuracy depends heavily on the encoding: "high accuracy is only achieved with P10 or P1000... P1000 performing better on average" for multiplication, while harder tasks favor asymmetric encodings. This is a controlled, quantified instance of the same phenomenon PatternBoost later states qualitatively ("choices like this really can make a difference in performance").

## Problem

Whether — and how — the surface representation of numbers fed to a transformer affects its ability to learn linear-algebra operations (transpose, addition, multiplication, eigenvalues, inversion).

## Approach

Trains encoder-only/seq2seq transformers on nine linear-algebra tasks over randomly generated matrices, holding architecture fixed and varying only the number-encoding scheme (P10: base-10 positional; P1000: base-1000 positional, fewer tokens; B1999: balanced base; FP15: fixed-precision floating point). Reports per-task, per-encoding accuracy.

## Key result

"high accuracy is only achieved with P10 or P1000... P1000 performing better on average" for matrix multiplication; for harder tasks (eigendecomposition, inversion) "asymmetric encodings... achieve the best results." Encoding choice produces accuracy swings large enough to change which tasks are solvable at all, not just fine-tuning-scale differences (per subagent extraction from ar5iv full text — exact percentage table not independently re-verified in this pass).

## Assumptions

Random matrices as training/test distribution; fixed transformer architecture across the encoding ablation (isolates the encoding variable). Numeric domain (real-number matrices), not a discrete/symbolic alphabet — the encoding question here is about digit/place-value representation, not character-vs-subword tokenization of a fixed small alphabet.

## Limitations / scope

Domain is numeric linear algebra, not symbolic/string rewriting. The specific encodings (P10, P1000, B1999, FP15) are number-representation schemes with no direct analog for a 4-letter alphabet {a,b,A,B} — transfers as *evidence that representation matters*, not as a specific recipe for the B(2,5) case.

## Replication evidence

Not independently assessed in this pass; not required to establish the "representation matters" claim, which is Charton's own controlled within-paper ablation.

## Why this paper matters

This is the strongest evidence in the whole B25-tokenization scan that a fixed model architecture, run only differing in how the *same* mathematical objects are surface-encoded, produces materially different learnability. It is also the same author as PatternBoost, so it is reasonable to read PatternBoost's informal "tokenization can make a difference" line as backed by this paper's earlier quantified result, not just a hunch.

## Quotes

1. > "high accuracy is only achieved with P10 or P1000" — on matrix multiplication encoding ablation
2. > "asymmetric encodings... achieve the best results" — on harder tasks (eigendecomposition/inversion)

## Open questions surfaced

Whether the same "representation choice dominates accuracy" pattern holds for discrete symbolic sequences over a tiny fixed alphabet (our B(2,5) case) rather than numeric encodings — untested here, this paper only covers numbers.

## Related material in vault

- Cited by: [[charton-2024-patternboost]] (same author, informal restatement of the same finding)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
- Related: [[singh-strouse-2024-tokenization-counts]] (same representation-dominates-arithmetic-learnability finding, from the tokenization-boundary side)
