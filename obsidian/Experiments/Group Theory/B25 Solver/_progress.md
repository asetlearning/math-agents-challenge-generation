---
title: b25-solver — experiment progress
domain: group-theory
project: b25-solver
instance: B(2,5)
status: pending
author: asetlearning
tags: [agent/lead, user/asetlearning, domain/group-theory, topic/b25, topic/burnside, topic/trivial-words, topic/word-problem, project/b25-solver, status/pending, experiment]
---

# b25-solver — Progress

Project profile: [[project-b25-solver]]. Goal: a solver for trivial words in B(2,5) that adapts to the given word. It is tested first on the benchmark words of [[ds-b25-challenge-candidates]]. Success is one verified break; a verified shortening counts as progress.

## Current question

Stage 1 ([[b25-solver-stage1-plan-2026-11-04]]):
- **E0-rebuild-seed-pool:** does a PatternBoost seed pool built from the challenge-gen construction reach the target regime? Every earlier pool collapsed under 2.5-reduction.
- **I1-invariant-review:** which similarity measures in the free group or in finite approximations are sound and cheap?

## Log
- 2026-11-04: project started (owner). Stage-1 plan written; development begins. Model training waits for the GPU server.
