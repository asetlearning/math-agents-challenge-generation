---
title: "Investigating the Limitations of Transformers with Simple Arithmetic Tasks"
authors:
  - "Rodrigo Nogueira"
  - "Zhiying Jiang"
  - "Jimmy Lin"
year: 2021
venue: "arXiv:2102.13019 (cs.CL)"
url: "https://arxiv.org/abs/2102.13019"
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
  - "[[singh-strouse-2024-tokenization-counts]]"
quality_notes: "Rigorous ablation across subword/character/position-token surface forms for a precision-critical symbolic task. Directly evidences that naive character-level tokenization is NOT automatically sufficient for precise symbolic manipulation — a caveat against assuming char-level tokenization solves the B(2,5) rule-alignment problem by default."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/tokenization
  - paper
  - status/draft
---

# Investigating the Limitations of Transformers with Simple Arithmetic Tasks

## Abstract

"The ability to perform arithmetic tasks is a remarkable trait of human intelligence and might form a critical component of more complex reasoning tasks. In this work, we investigate if the surface form of a number has any influence on how sequence-to-sequence language models learn simple arithmetic tasks such as addition and subtraction across a wide range of values. We find that how a number is represented in its surface form has a strong influence on the model's accuracy. In particular, the model fails to learn addition of five-digit numbers when using subwords (e.g., "32"), and it struggles to learn with character-level representations (e.g., "3 2"). By introducing position tokens (e.g., "3 10e1 2"), the model learns to accurately add and subtract numbers up to 60 digits. We conclude that modern pretrained language models can easily learn arithmetic from very few examples, as long as we use the proper surface representation. This result bolsters evidence that subword tokenizers and positional encodings are components in current transformer designs that might need improvement. Moreover, we show that regardless of the number of parameters and training examples, models cannot learn addition rules that are independent of the length of the numbers seen during training."

## TL;DR

For 5-digit addition, subword (BPE-style) tokenization fails outright, but plain character-level tokenization *also* struggles — only explicit place-value/position tokens (e.g. "3 10e1 2") let the model learn addition robustly up to 60 digits. The load-bearing caveat for our decision: **character-level tokenization is not automatically sufficient** for precise symbolic manipulation just because it avoids BPE's boundary problem; structure-aware tokenization (encoding *what role* each character plays, not just which character it is) can matter independently of granularity.

## Problem

Whether the surface form (subword vs. character vs. position-annotated) in which a number is presented to a transformer affects its ability to learn exact arithmetic (addition/subtraction) across a wide range of digit-counts.

## Approach

Trains/fine-tunes seq2seq language models on addition and subtraction with three number surface forms: subword tokenization (default BPE-style, e.g. "32" as one or few tokens), character-level ("3 2", one token per digit), and position-tokens ("3 10e1 2", each digit annotated with its place value). Evaluates accuracy across digit counts from small to 60 digits, including generalization beyond training-length digit counts.

## Key result

"the model fails to learn addition of five-digit numbers when using subwords... and it struggles to learn with character-level representations"; "By introducing position tokens... the model learns to accurately add and subtract numbers up to 60 digits." Also: "models cannot learn addition rules that are independent of the length of the numbers seen during training" — i.e. length generalization failed even with the best-performing representation, unless training covered the relevant length range.

## Assumptions

Numeric domain (base-10 digit strings) with position-dependent semantics (place value) — the "correct" answer depends on which digit is in which position, a structurally different requirement from B(2,5) rewrite-rule matching, where the same substring pattern (e.g. "abAB") means the same thing regardless of its position in the word (offset-invariance, not position-dependence).

## Limitations / scope

This is a numeric/place-value task, the opposite structural regime from ours: arithmetic *needs* strong positional/place-value awareness (hence position tokens winning), while B(2,5) rule-firing needs offset-invariant local pattern matching (hence [[kazemnejad-2023-nope]]'s NoPE/relative-position finding pointing the other direction). The two papers are not in tension — they're evidence for opposite representational needs in opposite task structures, and both point away from "just use whatever's default" for our specific offset-invariant case.

## Replication evidence

Not independently assessed in this pass. Consistent in direction (representation dominates accuracy for precision-critical symbolic tasks) with [[charton-2022-linear-algebra-transformers]] and [[singh-strouse-2024-tokenization-counts]] — three independent groups on three different symbolic tasks all found representation/tokenization choice materially changes learnability.

## Why this paper matters

The clean counter-argument against treating "character-level = safe default" as a free pass: character-level tokenization alone was NOT enough for exact arithmetic here. For B(2,5), this means char-level tokenization should be paired with a positional scheme suited to the task's actual structure (offset-invariant local motifs → favor NoPE/relative per [[kazemnejad-2023-nope]], not favor place-value-style position tokens as this paper's task needed) — the representation choice has two independent axes (token granularity AND positional encoding), and this paper is evidence that getting only one of them right isn't sufficient.

## Quotes

1. > "the model fails to learn addition of five-digit numbers when using subwords... and it struggles to learn with character-level representations" — Abstract
2. > "models cannot learn addition rules that are independent of the length of the numbers seen during training" — Abstract

## Open questions surfaced

Whether B(2,5) rewrite-rule firing (offset-invariant, unlike place-value arithmetic) needs any analog of "position tokens," or whether plain character-level + NoPE/relative-PE is sufficient precisely because the task doesn't have arithmetic's position-dependent semantics — this is the key structural distinction that should be validated empirically before assuming char-level tokenization is enough.

## Related material in vault

- Related: [[singh-strouse-2024-tokenization-counts]] (same domain — number tokenization — different specific finding: boundary direction, not granularity)
- Related: [[kazemnejad-2023-nope]] (opposite positional-encoding recommendation, for the opposite reason — task-structure-dependent, not contradictory)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
