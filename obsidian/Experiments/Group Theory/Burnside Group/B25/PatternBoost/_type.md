---
title: "PatternBoost on B(2,5) — experiment type root"
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: patternboost
status: pending
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/word-problem, project/b25, status/pending, experiment-type]
---

# PatternBoost on B(2,5)

PatternBoost is an alternating search loop in which a transformer and a local search engine collaborate to discover short representatives of group words. The transformer learns from local-search successes (word reductions) and proposes candidate patterns; the local search applies these candidates and scores results; the scores become new training signal. Described in [[charton-2024-patternboost]] and implemented in [[axplorer]].

## Why this technique for B(2,5)

Beam search (Reduce Core) and KB mixing (KBMag) have plateaued: `comm_12_9` is stuck at 7,245 chars after extensive multi-pass beam search on 25.7M rules. PatternBoost offers a complementary route — the transformer may discover structural patterns in commutator words that pure KB enumeration cannot find in reasonable time. The technique is purely heuristic (no math claims), so it runs in parallel to KB without creating proof obligations.

## What this folder contains

- `methodology/` — pre-registration notes and methodology descriptions for each experiment phase
- `data/` — training word lists, constants, scorer calibration data
- `results/` — results tables for completed phases (one row per parameter-variant run)

## Experiment phases (planned)

| Phase | Name | Status |
|---|---|---|
| STEP 1 | Proxy correlation study (deliverable #1) | `#status/pending` |
| STEP 1.5 | Wire `calc_score()`, first training run | Blocked on STEP 1 outcome + commit gate |
| STEP 2 | Full PatternBoost loop on 54 training words | Blocked on STEP 1.5 |

## Scope

This folder covers only the PatternBoost methodology applied to B(2,5). It does not cover KB mixing (→ [[KBMag/_type]]), beam search (→ [[Reduce Core/_type]]), or bidirectional search (→ [[Rust Bidirectional/_type]]).

## Related material

- [[_progress|B(2,5) Progress Note]] — standing progress note for all B(2,5) experiment types
- [[charton-2024-patternboost]] — primary reference for the PatternBoost alternating-search framework
- [[axplorer]] — axplorer implementation; `DataPoint` ABC is the extension point for `BurnsideDataPoint`
- [[Reduce Core/_type]] — plateau that motivated this experiment type (comm_12_9 at 7,245 chars)
- [[b25-benchmark-snapshot-2026-06-09]] — source of the 54 training word selections
