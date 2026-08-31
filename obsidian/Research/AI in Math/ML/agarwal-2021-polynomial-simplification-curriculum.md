---
title: "Analyzing the Nuances of Transformers' Polynomial Simplification Abilities"
authors:
  - "Vishesh Agarwal"
  - "Somak Aditya"
  - "Navin Goyal"
year: 2021
venue: "ICLR 2021 MathAI Workshop; arXiv:2104.14095"
url: "https://arxiv.org/abs/2104.14095"
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
  - "[[zaremba-sutskever-2014-learning-to-execute]]"
quality_notes: "Closest curriculum-learning analog found to our setting: a transformer, on a genuinely symbolic/algebraic task (polynomial simplification toward normal form via an ordered sequence of steps), with curriculum ordered by task-complexity rather than raw token length. Read via subagent WebFetch extraction, abstract + summary level, not full-text verified by Researcher in this pass."
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

# Analyzing the Nuances of Transformers' Polynomial Simplification Abilities

## Abstract

"Symbolic Mathematical tasks such as integration often require multiple well-defined steps and understanding of sub-tasks to reach a solution. In order to understand transformer models' abilities on these problems, we investigate transformers' abilities on polynomial simplification, requiring multi-step reasoning that involves recognition and execution of a finite set of transformation rules, ensuring that a normal form is reached." [Abstract as extracted by research subagent from ar5iv/arXiv fetch — not independently re-verified verbatim against primary source by Researcher in this pass; treat as close paraphrase pending direct confirmation.]

## TL;DR

A transformer trained to simplify polynomials toward normal form — a task that, like B(2,5) word shortening, is a **rule-application/rewriting process with a well-defined sequence of transformation steps** — was evaluated step-wise rather than end-to-end. The model struggles specifically with numeric multiplication sub-steps across configurations. Curriculum learning (ordered by task complexity, not raw sequence length) and offloading numeric calculation to an external symbolic calculator both gave "substantial improvements" over baseline, but the reported gains are **uneven across difficulty tiers (roughly +0.68% to +10.8%)** — i.e. curriculum benefit is real but not uniform, largest on the hardest configurations.

## Problem

Whether transformers can learn multi-step symbolic simplification (polynomial → normal form via a defined rule-application sequence), evaluated at the level of individual reasoning steps rather than only final-answer accuracy, and whether curriculum learning or external-tool offloading improves this.

## Approach

Constructs a synthetic dataset of polynomials with labeled step-wise simplification sequences (each step applies a rule moving the expression closer to normal form — structurally close to a KB-style rewrite trajectory). Evaluates transformer performance step-by-step, not just on the final simplified form. Tests two interventions: (1) curriculum learning ordered by problem/task complexity; (2) offloading numeric multiplication to an external symbolic calculator rather than requiring the transformer to compute it internally.

## Key result

Transformers "struggle with numeric multiplication" as a specific sub-step failure mode, regardless of overall task setup. Curriculum learning and calculator-offloading "both achiev[e] substantial improvements over baseline transformer performance" — per subagent extraction, the reported curriculum gains range from roughly +0.68% to +10.8% depending on difficulty tier, with the largest gains concentrated on the hardest configurations (i.e. curriculum helps most exactly where the task is hardest, not uniformly).

## Assumptions

Curriculum axis is task/step COMPLEXITY (number of simplification steps, structural difficulty of the rule application), not raw token/sequence LENGTH per se — a meaningfully different curriculum variable than the length-window curriculum (256→512→1024→full) under consideration for B(2,5), though the two are likely correlated in practice (longer B(2,5) words plausibly require more reduction steps).

## Limitations / scope

Domain is polynomial algebra (commutative, numeric coefficients), a very different algebraic structure from B(2,5) (non-commutative, order-5 torsion, no numeric coefficients) — transfers as evidence-shape (curriculum helps unevenly, biggest wins on hard cases; internal-arithmetic sub-steps are a specific weak point transformers have) rather than a directly portable recipe. Abstract/summary extracted by subagent, not independently re-verified by Researcher against primary ar5iv text in this pass — flag for a closer read if this becomes decision-relevant.

## Replication evidence

Directionally consistent with [[zaremba-sutskever-2014-learning-to-execute]] (curriculum benefit is real but conditional, not automatic) and with [[mehta-2026-randomized-yarn]] (curriculum is load-bearing, degrades substantially without it, in a modern transformer long-context setting) — three independent sources across three different eras/architectures/domains all agree curriculum-for-difficulty/length is a real, non-trivial lever, not a minor detail.

## Why this paper matters

This is the closest available analog to "does curriculum learning help a transformer on a genuinely symbolic REWRITING task" — closer in spirit to B(2,5) than either the arithmetic-curriculum literature (Zaremba & Sutskever, position-dependent semantics) or the long-context-recall literature (Mehta et al., not a rewriting task at all). The finding that curriculum benefit concentrates on the HARDEST configurations is a useful prior: if a B(2,5) length curriculum is adopted, the biggest expected payoff is on the longest/hardest words (near 1348 chars), not the short windows — which argues for NOT skimping on curriculum design at the high-length end even if it's tempting to treat the full-length stage as "just more of the same."

## Open questions surfaced

Whether curriculum ordered by REDUCTION-STEP COUNT (steps needed to reach the reducer's normal form) rather than by raw character length would be a better B(2,5) curriculum axis than the currently-planned window-size progression (256→512→1024→full) — this paper's framing suggests step-complexity may be the more load-bearing variable, untested directly for B(2,5).

## Related material in vault

- Related: [[zaremba-sutskever-2014-learning-to-execute]] (curriculum-for-length caution, different architecture/domain)
- Related: [[mehta-2026-randomized-yarn]] (curriculum + randomized PE composition, modern transformer)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
