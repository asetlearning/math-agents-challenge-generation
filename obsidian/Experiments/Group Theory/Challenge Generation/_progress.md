---
title: Challenge generation — experiment progress
domain: group-theory
project: challenge-gen
instance: B(2,5) (phase 1)
status: pending
author: asetlearning
tags: [agent/human, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, project/challenge-gen, status/pending, experiment]
---

# Challenge Generation — Progress

Project profile: [[project-challenge-gen]]. Goal: generate **hard** problem instances that come with a **certificate** proving they have a solution. These are for benchmarking and training search algorithms. Phase 1 is hard trivial words ("challenges") in **B(2,5)**. Later candidates include Andrews–Curtis.

> Created 2026-10-05. Experiment-type folders go under per-problem instance folders, e.g. `B25/<Experiment type>/{methodology,data,results}/`, per [[experiment-folder-convention]]. Instance folders are created with their first experiment.

## Current question

**Updated 2026-10-05:** Can we generate certified trivial words that pass L1 (2.5-reduction resistant), and then L2 (Dehn proxy ≥ 1)? The original question follows.


How can we generate words that are provably trivial in B(2,5), with the proof produced by the generator itself, and that resemble the rare "hard" instances rather than generic random ones?

## Definitions and metrics (owner, 2026-10-05)

See [[challenge-gen-success-metrics]].
- **Challenge:** a word w̄ in free B(2,5) with a certificate F, i.e. a factor word over relators trivial in free B(2,5), with expand(F) = w̄.
- **Hard (L1):** 2.5 reduction leaves ρ = |R₂.₅(w)|/|w̄| ≥ 0.5 and does not reach 1. Every random factor word fails this; it reduces to 1.
- **High filling (L2):** D = |F*|/|w̄| ≥ 1 on the minimised certificate F*. This is an upper-bound proxy for the Dehn function.
- **Great (L3):** a family with |F*| ≈ c·n², i.e. quadratic area.

## Prior work in the vault

- [[2026-09-30-b25-b0-challenge-triviality]]: all 150 human challenge words (118 non-empty, 32 empty) are the identity in the **restricted** B₀(2,5) (5^34, class 12, GAP/Pq). This says nothing about the free B(2,5). It is a natural first benchmark set. Experiment folder: [[B25/B0 Challenge Triviality/_type|B0 Challenge Triviality]] (lives in the `#project/b25` tree).

## Instances and experiment types
- **B25** → [[B25/PatternBoost Generation/_type|PatternBoost Generation]]. A PatternBoost loop over certified factor words. The baseline steers onto random certified targets with up to 100% success, but generates no hard words yet. See [[patternboost-generation-results]].

## Log

### 2026-10-05 — project registered
`#project/challenge-gen` registered, with its profile and this progress note. A literature scan on hard-instance generation is pending. Writeups, plans and the first experiments will follow from asetlearning.

### 2026-10-05 — literature scan
The scan ingested 12 papers: generic-case complexity, certified trivial-word and Andrews–Curtis generators, quiet planting in SAT/CSP, and learned/adversarial instance generators. Synthesis: [[_synthesis-hard-instance-generation]]. Its recommendation has three steps: (1) build a baseline certified generator with an independent checker; (2) fix the hardness metrics on baseline output and on the human challenge words; (3) do adversarial generation over certified moves, rewarded against a solver portfolio. The key open theory question: is the **witness** version of the word problem generically hard ([[kapovich-2003-generic-case-complexity]] §4)?

### 2026-10-05: PatternBoost generator ingested
Ingested the owner's PatternBoost implementation: the design writeup, the baseline sweep dashboard (24 combos × 50 trials), and both code repos.
- The code repos are registered as [[dep-b25-pyproject-agentic]] and [[dep-tcgraph-agentic]], and the profile is updated.
- **Key facts:**
  - Triviality is certified by construction, given trivial relators.
  - Baseline success is driven by local-search steps; the cheapest setting at ≥ 90% is w1.s10.p100 (96%, 96 s).
  - Early candidates were all 2.5-reducible to 1, so hardness is not yet addressed.
- **Known issues, documented, not fixed:**
  - b25's submodule URL points at gt-computations/tcgraph, and the pin is stale.
  - tcgraph_agentic main fails to build `test_pb_local_search`; verified, ctest 8/9.
  - No provenance or seeds are logged.
- Next: the owner will supply new ideas, goals and metrics for actual challenge generation.

### 2026-10-05: new goals and metrics
The owner defined the difficulty metrics: ρ (2.5-reduction resistance, pass at ≥ 0.5) and the Dehn proxy D on a minimised certificate (pass at ≥ 1; quadratic family is the great outcome). Challenge similarity becomes secondary. See [[challenge-gen-success-metrics]].

### 2026-10-05: Dehn-proxy maximisation run analysed (run of 2026-07-23)
PatternBoost maximising the raw D, with 2.5-reduced KB relators, over 20 iterations and about 300k candidates: **every candidate 2.5-reduces to 1** (L1: 0). Best D = 0.344 (11 factors / 32 letters), flat from iteration 3. The search raised D by shrinking words (mean length 1159 → 52) rather than adding factors. Lesson: D alone pushes toward short, easy words, so the objective needs a Metric-1 gate or a length floor. See [[patternboost-generation-results]] § Dehn-proxy run.

## Related material
- [[project-challenge-gen]]: project profile
- [[B25/_progress]]: B(2,5) progress (the group itself)
- [[andrews-curtis-conjecture]]: candidate phase-2 problem
- [[projects-and-dependencies-convention]]
- [[_synthesis-hard-instance-generation]]
- [[_moc-hard-instance-generation]]
- [[challenge-gen-success-metrics]]
