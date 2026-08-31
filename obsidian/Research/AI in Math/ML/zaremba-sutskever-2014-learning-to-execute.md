---
title: "Learning to Execute"
authors:
  - "Wojciech Zaremba"
  - "Ilya Sutskever"
year: 2014
venue: "arXiv:1410.4615 (cs.NE)"
url: "https://arxiv.org/abs/1410.4615"
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
quality_notes: "Pre-transformer (LSTM) and on arithmetic/program-execution, not group words — but the single most rigorous curriculum-vs-no-curriculum ablation found in this scan, with a load-bearing negative result (naive curriculum can underperform no curriculum) that argues against assuming a short-to-long curriculum for B(2,5) is automatically safe."
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

# Learning to Execute

## Abstract

"Recurrent Neural Networks (RNNs) with Long Short-Term Memory units (LSTM) are widely used because they are expressive and are easy to train. Our interest lies in empirically evaluating the expressiveness and the learnability of LSTMs in the sequence-to-sequence regime by training them to evaluate short computer programs, a domain that has traditionally been seen as too complex for neural networks. We consider a simple class of programs that can be evaluated with a single left-to-right pass using constant memory. Our main result is that LSTMs can learn to map the character-level representations of such programs to their correct outputs. Notably, it was necessary to use curriculum learning, and while conventional curriculum learning proved ineffective, we developed a new variant of curriculum learning that improved our networks' performance in all experimental conditions. The improved curriculum had a dramatic impact on an addition problem, making it possible to train an LSTM to add two 9-digit numbers with 99% accuracy."

## TL;DR

Character-level LSTMs trained to execute short programs / add multi-digit numbers need curriculum learning to succeed at all — but the paper's central methodological finding is that the OBVIOUS curriculum ("naive": train on progressively longer/harder examples only) **sometimes underperforms no curriculum whatsoever**. Their winning strategy ("combined") mixes easy examples in throughout training rather than retiring them once the model has "graduated" to harder ones. This is a direct, rigorous caution against assuming a pure short-to-long B(2,5) length curriculum (256→512→1024→full) will help without a mixed-difficulty safeguard.

## Problem

Can LSTM sequence-to-sequence models learn to execute simple programs (including multi-digit arithmetic) from character-level input, and does curriculum learning (ordering training examples from easy to hard) help or hurt this?

## Approach

Trains character-level LSTMs on program-execution and digit-addition tasks. Compares four training regimes: (1) **baseline** — no curriculum, uniform sampling over all difficulty levels from the start; (2) **naive curriculum** — train on progressively harder (longer) examples only, advancing once a performance threshold is met; (3) **mixed strategy** — sample difficulty randomly per example (no progression) but from a distribution favoring easier examples; (4) **combined strategy** (their contribution) — progress a difficulty "frontier" like the naive curriculum, but continue sampling easier-than-frontier examples throughout training rather than dropping them once passed.

## Key result

"it was necessary to use curriculum learning, and while conventional curriculum learning proved ineffective, we developed a new variant of curriculum learning that improved our networks' performance in all experimental conditions" — i.e. naive/conventional curriculum was NOT sufficient and in some conditions underperformed no-curriculum baselines (per subagent's controlled-ablation extraction); only the "combined" variant (curriculum frontier + retained easy-example sampling) won consistently. "Combined" curriculum enabled 99% accuracy on 9-digit addition, a task the paper frames as otherwise out of reach.

## Assumptions

LSTM, not transformer — the recurrent inductive bias may interact with curriculum differently than self-attention. Task domain is program execution / arithmetic (position-dependent semantics, similar caveat to [[nogueira-2021-arithmetic-limitations]]), not free-group word rewriting (offset-invariant semantics) — the specific difficulty axis (program complexity / digit count) is a length-and-complexity conflation, not a pure length variable.

## Limitations / scope

Pre-transformer architecture (2014); results on curriculum mechanics may not transfer cleanly to self-attention's very different training dynamics. No group-theory or symbolic-rewriting content. The "combined" strategy's specific mechanism (retain easy examples in the sampling pool rather than retiring them after the frontier advances) is a concrete, checkable design detail that a B(2,5) length curriculum (256→512→1024→full) should consider adopting directly, rather than assuming pure progression is safe.

## Replication evidence

Not independently assessed for LSTM tasks in this pass. The broader caution (progressive curricula are not automatically beneficial, and can actively hurt) is echoed by Agarwal et al.'s finding ([[agarwal-2021-polynomial-simplification-curriculum]]) that curriculum benefit is uneven across difficulty tiers (0.68% to 10.8%, not a flat win) on a transformer symbolic-math task — a second, independent data point that curriculum benefit is real but non-uniform/non-guaranteed, not that curricula are inherently unsafe.

## Why this paper matters

This is the load-bearing counter-evidence against treating "256→512→1024→full curriculum" as a safe default for B(2,5) training. It's the earliest and most rigorously-ablated source in the whole curriculum-for-length literature this scan found, and its central finding is a warning, not an endorsement: a naive progressive curriculum can underperform no curriculum at all. Any B(2,5) curriculum design should budget for a "combined"-style safeguard (continue sampling short/easy windows throughout training, not just early on) rather than assuming monotone difficulty progression is free.

## Quotes

1. > "conventional curriculum learning proved ineffective" — Abstract
2. > "we developed a new variant of curriculum learning that improved our networks' performance in all experimental conditions" — Abstract

## Open questions surfaced

Whether the "combined" curriculum strategy (retain easy examples throughout, not just early) transfers from LSTM program-execution to a decoder-only transformer trained on B(2,5) windowed targets (256/512/1024/1348) — untested, but a concrete, cheap design element to adopt by default given the risk this paper documents.

## Related material in vault

- Related: [[agarwal-2021-polynomial-simplification-curriculum]] (transformer, symbolic-math domain, curriculum benefit confirmed but uneven)
- Related: [[mehta-2026-randomized-yarn]] (modern transformer evidence that curriculum is load-bearing when composed with randomized positional encoding)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
