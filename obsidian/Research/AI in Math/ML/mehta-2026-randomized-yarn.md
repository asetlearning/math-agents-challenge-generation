---
title: "Randomized YaRN Improves Length Generalization for Long-Context Reasoning"
authors:
  - "Manas Mehta"
  - "Fangcong Yin"
  - "Greg Durrett"
year: 2026
venue: "arXiv:2606.23687 (cs.CL)"
url: "https://arxiv.org/abs/2606.23687"
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
cites:
  - "[[ruoss-2023-randomized-positional-encodings]]"
cited_by: []
related:
  - "[[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]"
quality_notes: "Directly answers R3.4 (does length curriculum compose with randomized positional encoding, or conflict?): they compose well, and the curriculum is independently load-bearing (degrades up to 18.3% without it). Read via ar5iv full text + abstract by research subagent; Table 3 figures per subagent extraction, not independently re-verified by Researcher against primary source in this pass."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/length-generalization
  - paper
  - status/draft
status: draft
---

# Randomized YaRN Improves Length Generalization for Long-Context Reasoning

## Abstract

"Large language models (LLMs) are typically pretrained on short sequences and then extended to work on longer sequences with additional training. However, such LLMs still struggle to further generalize to very long sequences. We propose Randomized YaRN, a training method that improves length generalization by combining YaRN-based positional extrapolation with randomized positional encoding and a length curriculum."

## TL;DR

Combines three techniques — YaRN (a RoPE-extrapolation method), randomized positional encoding (per [[ruoss-2023-randomized-positional-encodings]]), and an explicit length curriculum — and directly ablates whether the curriculum component is necessary when randomized positional encoding is already in play. Answer: yes, necessary and load-bearing. Both randomized-PE-alone and Randomized-YaRN-alone "degrade substantially without the length curriculum by up to 18.3%" per the paper's own framing — i.e. curriculum and randomized positional schemes are complementary, not redundant or competing techniques.

## Problem

Whether combining positional-extrapolation techniques (YaRN) with randomized positional encoding (Ruoss et al. 2023) and a length curriculum improves long-context length generalization beyond what any one technique achieves alone — and specifically whether the curriculum component remains necessary once randomized positional encoding is already providing some length-robustness.

## Approach

Trains models under several combinations: {RPE, Randomized-YaRN} × {with curriculum, without curriculum}, training on contexts under 8K tokens and evaluating generalization to 16K–128K token lengths on BABILong and Multi-Round Coreference Resolution benchmarks. Table 3 (per subagent extraction) reports MRCR/Qwen2.5 results specifically.

## Key result

Per subagent's extraction of Table 3 (MRCR/Qwen2.5): RPE without curriculum 56.8% → RPE with curriculum 75.1%; Randomized-YaRN without curriculum 69.4% → with curriculum 77.3%. The paper's own stated framing: both methods "degrade substantially without the length curriculum by up to 18.3%." This is a direct, quantified answer to whether curriculum and randomized-positional techniques compose (they do) or whether one makes the other redundant (it does not — curriculum remains independently necessary).

## Assumptions

Long-context LLM setting (pretrained models extended to longer contexts via additional training), not training-from-scratch on a narrow symbolic domain like B(2,5) — the specific numbers (8K→16-128K) are far larger scale than our ~1348-character target, but the qualitative composition finding (curriculum + randomized-PE are complementary, not substitutes) is architecture-and-scale-agnostic in principle.

## Limitations / scope

Domain is natural-language long-context reasoning (BABILong, coreference), not symbolic/algebraic sequence rewriting — no B(2,5) or group-theory content. Table 3 figures were extracted by a research subagent from ar5iv full text and have not been independently re-verified by Researcher against the primary source in this pass; treat the specific percentages as approximately right, not verbatim-confirmed, pending a closer read if this becomes decision-relevant.

## Replication evidence

Not independently assessed. This paper is itself framed as a controlled follow-up/extension of [[ruoss-2023-randomized-positional-encodings]]'s technique, adding the curriculum ablation that the original 2023 paper didn't isolate as a separate variable.

## Why this paper matters

This is the single most directly on-point answer to R3's fourth ask (does curriculum-over-length compose with or conflict with randomized positional encoding). The finding removes a design worry: adopting BOTH a windowed length curriculum (256→512→1024→full, already built via `seed_window.py`) AND a randomized/relative positional scheme (per [[kazemnejad-2023-nope]] / [[ruoss-2023-randomized-positional-encodings]]) for the B(2,5) transformer is evidence-backed as complementary, not conflicting — and dropping the curriculum while keeping only the positional trick would leave real performance on the table (up to 18.3% per this paper's numbers, in its own long-context domain).

## Quotes

1. > "We propose Randomized YaRN, a training method that improves length generalization by combining YaRN-based positional extrapolation with randomized positional encoding and a length curriculum." — Abstract
2. > "degrade substantially without the length curriculum by up to 18.3%" — per subagent extraction, Results/Table 3 discussion

## Open questions surfaced

Whether the same curriculum-is-load-bearing-even-with-randomized-PE finding holds at B(2,5)'s much smaller scale (hundreds to ~1348 characters, not 8K–128K tokens) and in a symbolic-rewriting rather than long-context-recall task — untested, but this is the strongest available evidence that curriculum shouldn't be dropped as "redundant" once a positional-encoding fix is adopted.

## Related material in vault

- Cites: [[ruoss-2023-randomized-positional-encodings]] (the randomized-PE technique this paper extends)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-value-scoring-curriculum-auxchannel]] (Deep Round 2 — synthesizes this paper's curriculum thread)
- Related: [[kazemnejad-2023-nope]] (the NoPE positional-encoding result in the same length-generalization cluster)
