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

How can we generate words that are provably trivial in B(2,5), with the proof produced by the generator itself, and that resemble the rare "hard" instances rather than generic random ones?

## Definitions (to be filled)

- **Challenge**: TBD
- **Hard**: TBD (relative to which solvers / metrics?)
- **Certificate**: TBD (what is attached, how it is checked, in which group)

## Hardness metrics

TBD. Baselines to compare against:
- random (generic) trivial words from a simple generator
- the 150 human challenge words (below)

## Prior work in the vault

- [[2026-09-30-b25-b0-challenge-triviality]]: all 150 human challenge words (118 non-empty, 32 empty) are the identity in the **restricted** B₀(2,5) (5^34, class 12, GAP/Pq). This says nothing about the free B(2,5). It is a natural first benchmark set. Experiment folder: [[B25/B0 Challenge Triviality/_type|B0 Challenge Triviality]] (lives in the `#project/b25` tree).

## Log

### 2026-10-05 — project registered
`#project/challenge-gen` registered, with its profile and this progress note. A literature scan on hard-instance generation is pending. Writeups, plans and the first experiments will follow from asetlearning.

### 2026-10-05 — literature scan
The scan ingested 12 papers: generic-case complexity, certified trivial-word and Andrews–Curtis generators, quiet planting in SAT/CSP, and learned/adversarial instance generators. Synthesis: [[_synthesis-hard-instance-generation]]. Its recommendation has three steps: (1) build a baseline certified generator with an independent checker; (2) fix the hardness metrics on baseline output and on the human challenge words; (3) do adversarial generation over certified moves, rewarded against a solver portfolio. The key open theory question: is the **witness** version of the word problem generically hard ([[kapovich-2003-generic-case-complexity]] §4)?

## Related material
- [[project-challenge-gen]]: project profile
- [[B25/_progress]]: B(2,5) progress (the group itself)
- [[andrews-curtis-conjecture]]: candidate phase-2 problem
- [[projects-and-dependencies-convention]]
- [[_synthesis-hard-instance-generation]]
- [[_moc-hard-instance-generation]]
