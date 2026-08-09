---
title: "Learning to Unknot"
authors:
  - "Sergei Gukov"
  - "James Halverson"
  - "Fabian Ruehle"
  - "Piotr Sułkowski"
year: 2020
venue: "arXiv:2010.16263 (math.GT)"
url: "https://arxiv.org/abs/2010.16263"
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
  - "[[Research/AI in Math/ML/petschack-2025-symmetric-group]]"
quality_notes: "Closest literature analog found to the B(2,5) task shape: RL over generator-string-encoded words in an infinite discrete algebraic structure (braid group), with the goal of reaching a canonical simplified form (the unknot) via a sequence of word-rewriting moves. Read via ar5iv/direct fetch by research subagent; representation comparison (braid-word vs Dowker-Thistlethwaite encoding) reported at abstract/summary level, not independently verified against full paper text in this pass."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/tokenization
  - topic/braid-groups
  - topic/reinforcement-learning
  - paper
  - status/draft
---

# Learning to Unknot

## Abstract

"We introduce natural language processing into the study of knot theory, as made natural by the braid word representation of knots. We study the UNKNOT problem of determining whether or not a given knot is the unknot." [Abstract truncated in source fetch — full abstract not independently re-verified in this pass; the rest of the paper's contribution per the fetched summary: binary classification of unknot-or-not via Reformer/shared-QK transformer architectures (which outperform fully-connected networks, with accuracy improving as braid word length increases), plus a TRPO (RL) agent that finds sequences of braid-word moves simplifying a knot to the unknot, finding braid relations more effective than certain Markov moves.]

## TL;DR

Braid-group words (generators σᵢ±, i.e. a signed-integer analog of {a,b,A,B}) are fed to both a classifier (is this the unknot?) and an RL policy (TRPO) that learns a sequence of word-rewriting moves to *simplify* the word to a canonical trivial form. This is structurally the closest published analog to the B(2,5) word-shortening task: a variable-length string over a small generator alphabet, an infinite discrete algebraic structure, and a learned policy that emits *rewrite moves* rather than the raw simplified string directly.

## Problem

(1) Classify whether a given braid word represents the unknot. (2) Given a braid word, find a sequence of moves that simplifies it toward a canonical (trivial) representative.

## Approach

Represents knots via braid words (sequence of signed generator indices). For classification: feeds the raw generator-index sequence (via an embedding + positional encoding layer that handles variable length without a fixed padding scheme, per subagent extraction) to Reformer / shared-QK transformer architectures, compared against fully-connected baselines. For simplification: TRPO (policy-gradient RL) learns a policy over a composite action space of braid-word moves (not raw character edits — the action space is itself a small set of algebraic rewrite operations), rewarded for reducing word length / reaching the unknot.

## Key result

Reformer / shared-QK transformers outperform fully-connected networks on the classification task, with accuracy improving as braid word length increases (i.e. the architecture and representation scale favorably with longer words, not unfavorably — a positive data point against the intuition that longer sequences are strictly harder to learn). On the simplification side, braid-relation moves proved more effective than certain Markov moves for the RL policy. Per subagent's extraction (not independently re-verified against primary text in this pass): switching from the raw braid-word/generator encoding to an alternative structured encoding (Dowker-Thistlethwaite, a different canonical knot encoding) cost roughly 5 percentage points of accuracy — i.e. the "obvious" raw generator-string representation outperformed a more compressed/structured alternative for this task.

## Assumptions

Braid words are the input representation (not raw knot diagrams); the generator alphabet is small and fixed (signed integers, structurally analogous to {a,b,A,B} for B(2,5)); action space for the RL simplifier is a curated set of braid moves, not arbitrary character edits.

## Limitations / scope

Braid groups B_n are a different algebraic structure from Burnside groups B(2,5) — braid groups are torsion-free and have a decidable word problem via Garside normal form (see [[Research/AI in Math/ML/_synthesis-ml-for-math]] topic registry `#topic/braid-groups`), whereas B(2,5)'s free-group word problem is the harder open case. The RL action space (braid moves) is problem-specific and does not directly transfer to KB rewrite-rule application. The 5-percentage-point representation-comparison figure was extracted by a research subagent from a summary pass, not independently confirmed against the primary paper text — treat as approximate, not verbatim.

## Replication evidence

Not independently assessed in this pass.

## Why this paper matters

This is the one paper in the entire scan that combines (a) a variable-length string over a small discrete generator alphabet, (b) an infinite algebraic structure, and (c) a learned system that must find a *sequence of algebraic moves* to reach a simpler canonical form — i.e., it is doing for braid groups almost exactly the shape of thing we want to do for B(2,5) certificate words. The finding that raw generator-string representation beat a structured alternative (Dowker-Thistlethwaite), combined with the classifier's accuracy *improving* with braid-word length, is a mild point of evidence against over-engineering a compressed/structured tokenization for B(2,5) and in favor of trusting the raw {a,b,A,B} representation more than intuition might suggest — though this needs treating cautiously given the extraction wasn't independently verified against primary text.

## Quotes

1. > "We introduce natural language processing into the study of knot theory, as made natural by the braid word representation of knots." — Abstract

## Open questions surfaced

Whether an RL/PatternBoost-style policy over B(2,5) KB-rule applications (rather than raw character generation) would show the same "structured moves > raw generation, but raw string representation > structured compressed encoding" pattern found here for braid moves — untested, but this paper is the nearest available precedent and worth a closer full-text read if the edit/action-sequence representation family is shortlisted.

## Related material in vault

- Related: [[Research/AI in Math/ML/petschack-2025-symmetric-group]] (another group-theory + transformer paper from the same scan)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
