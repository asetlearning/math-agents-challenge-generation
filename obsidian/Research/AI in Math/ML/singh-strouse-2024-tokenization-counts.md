---
title: "Tokenization counts: the impact of tokenization on arithmetic in frontier LLMs"
authors:
  - "Aaditya K. Singh"
  - "DJ Strouse"
year: 2024
venue: "arXiv:2402.14903 (cs.CL)"
url: "https://arxiv.org/abs/2402.14903"
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
  - "[[nogueira-2021-arithmetic-limitations]]"
quality_notes: "Direct evidence that WHERE token boundaries fall relative to meaningful substructure changes model behavior in a systematic, not random, way — the closest published analog to our 'does BPE misalign with length-5-12 rewrite-rule motifs' concern, though the domain (digit grouping in frontier LLMs) is numeric, not a custom-trained small transformer on a 4-symbol alphabet."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/tokenization
  - paper
  - status/draft
---

# Tokenization counts: the impact of tokenization on arithmetic in frontier LLMs

## Abstract

"Tokenization, the division of input text into input tokens, is an often overlooked aspect of the large language model (LLM) pipeline and could be the source of useful or harmful inductive biases. Historically, LLMs have relied on byte pair encoding, without care to specific input domains. With the increased use of LLMs for reasoning, various number-specific tokenization schemes have been adopted, with popular models like LLaMa and PaLM opting for single-digit tokenization while GPT-3.5 and GPT-4 have separate tokens for each 1-, 2-, and 3-digit numbers. In this work, we study the effect this choice has on numerical reasoning through the use of arithmetic tasks. We consider left-to-right and right-to-left tokenization for GPT-3.5 and -4, finding that right-to-left tokenization (enforced by comma separating numbers at inference time) leads to largely improved performance. Furthermore, we find that model errors when using standard left-to-right tokenization follow stereotyped error patterns, suggesting that model computations are systematic rather than approximate. We show that the model is able to convert between tokenizations easily, thus allowing chain-of-thought-inspired approaches to recover performance on left-to-right tokenized inputs. We also find the gap between tokenization directions decreases when models are scaled, possibly indicating that larger models are better able to override this tokenization-dependent inductive bias. In summary, our work performs the first study of how number tokenization choices lead to differences in model performance on arithmetic tasks, accompanied by a thorough analysis of error patterns. We hope this work inspires practitioners to more carefully ablate number tokenization-related choices when working towards general models of numerical reasoning."

## TL;DR

BPE tokenizes multi-digit numbers left-to-right by default, which — because BPE's merge boundaries are frequency-driven, not semantically driven — produces *systematic*, direction-dependent error patterns in arithmetic: forcing right-to-left grouping (comma-separating digits) measurably improves accuracy on the exact same numbers. This is direct evidence that data-driven BPE token boundaries can misalign with the semantically-meaningful grouping of a sequence, and that the misalignment is not random noise but a reproducible, structured bias.

## Problem

Does the *direction* in which BPE groups digits into tokens (left-to-right vs. right-to-left) affect frontier LLMs' arithmetic accuracy, given that BPE's merge process is inherently left-to-right/frequency-driven and has no built-in awareness of place value?

## Approach

Compares GPT-3.5 and GPT-4 arithmetic accuracy under standard (left-to-right) BPE tokenization of numbers vs. a forced right-to-left tokenization (achieved by comma-separating digits before tokenization, which changes where BPE merge boundaries fall). Analyzes error patterns for systematicity, and tests whether chain-of-thought prompting can recover the gap under the "wrong" (left-to-right) tokenization. Also checks whether the gap shrinks with model scale.

## Key result

"right-to-left tokenization... leads to largely improved performance" over standard left-to-right; "model errors when using standard left-to-right tokenization follow stereotyped error patterns, suggesting that model computations are systematic rather than approximate" — i.e. the errors are a direct, traceable consequence of boundary placement, not generic noise. The tokenization-direction gap "decreases when models are scaled."

## Assumptions

Frontier LLMs with fixed, pre-trained BPE vocabularies (not a custom-trained-from-scratch tokenizer for a narrow domain) — this paper studies a *general-purpose* tokenizer applied to a numeric sub-task, not a domain-specific vocabulary trained on the target corpus itself. A BPE vocabulary trained directly on B(2,5) words (rather than reused from a general-purpose LLM) might exhibit different, though likely still context-dependent, boundary behavior — this paper doesn't test that scenario directly.

## Limitations / scope

Domain is numeric digit-grouping in large pretrained LLMs, not a small custom transformer trained on a 4-symbol algebraic alphabet. The mechanism (BPE boundaries drift with context, causing systematic errors) is the transferable claim; the specific direction-dependent recipe (right-to-left comma-separation) has no direct analog for {a,b,A,B} words, which don't have an inherent left/right "significant end" the way place-value numbers do.

## Replication evidence

Not independently assessed in this pass. Directionally consistent with [[nogueira-2021-arithmetic-limitations]] (subword tokenization fails on 5-digit addition) and the PatternBoost §3.1.2 delimiter fix (naive BPE on flattened adjacency matrices gave ~33% invalid predictions; adding row delimiters before BPE dropped that to 5-10% — a structural boundary-alignment fix, same mechanism class).

## Why this paper matters

This is the cleanest available demonstration that BPE boundary placement is not a cosmetic detail — it changes *where the model's errors systematically occur*, which is exactly the failure mode flagged as a risk in Lead's `AXPLORER_REPRESENTATION_NOTES.md` §6.3 for a fixed k-mer or BPE tokenizer over B(2,5) words: "the model would have to relearn that block 'abAB' and block 'baBA' share structure" if a rewrite-rule pattern gets tokenized differently depending on its offset. This paper is direct, though domain-adjacent (numeric, not algebraic-word), confirmation that this specific failure mode is real and reproducible in practice, not merely a hypothetical concern.

## Quotes

1. > "right-to-left tokenization... leads to largely improved performance" — Abstract
2. > "model errors when using standard left-to-right tokenization follow stereotyped error patterns, suggesting that model computations are systematic rather than approximate" — Abstract

## Open questions surfaced

Whether training a BPE vocabulary directly on a B(2,5)-word corpus (rather than reusing a general-purpose tokenizer, as this paper's LLMs do) would still exhibit offset-dependent boundary drift on length-5–12 rewrite-rule motifs — this is the concrete empirical test Math-expert/Developer would need to run if BPE remains a candidate representation family.

## Related material in vault

- Related: [[nogueira-2021-arithmetic-limitations]] (same general finding — surface tokenization changes arithmetic learnability — different specific mechanism)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
