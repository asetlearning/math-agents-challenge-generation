---
title: "B0 challenge triviality — 150 words in B_0(2,5)"
date: 2026-09-30
domain: group-theory
project: b25
experiment_type: b0-challenge-triviality
author: asetlearning
status: replicated
tags: [agent/exp-b25, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, project/b25, status/replicated, methodology, experiment]
---

# Methodology: 150 challenge words in B₀(2,5) (2026-09-30)

Validator verdict: `#status/replicated` — [[2026-09-30-b25-b0-challenge-triviality]] (B₀(2,5) only).

Directed task from Lead on behalf of the human (run begun before this note; documented for provenance).

## Working interpretation
\bar{B}(2,5) is read as **B₀(2,5) = R(2,5) = B(2,5)/γ₁₃**, the restricted Burnside group, order 5^34, class 12. If the human meant something else, this result does not cover it.

## Group computed in
**Restricted B₀(2,5)** — NOT the free B(2,5). See [[project-b25]].

## Target words
`/media/psf/math-agents-challenge-generation/data/b25_challenge_original_freelyreduced.json`, sha256 `067977857d88f895f6f643bdb3b569993132365f4afa2cd89e4b1873d6cf3cde`. 150 entries R1..R150, letters ±1,±2 read as 1=a, −1=a⁻¹, 2=b, −2=b⁻¹. Total 2,195,684 letters, max length 41,886. **32 of the 150 words are empty** (R1–R4 among them), so they are trivially the identity and carry no information.

## Hypothesis
Each word maps to the identity of B₀(2,5). Falsified for a word if its image has a nonzero pc exponent vector.

## Method
GAP 4.15.1, ANUPQ 3.3.2, polycyclic 2.17, host ubuntu-gnu-linux-24-04-3. `PqEpimorphism(FreeGroup(2) : Prime:=5, Exponent:=5, ClassBound:=12)`; each word is multiplied out letter by letter over the images of a, b in the pc group and tested with `IsOne`. Non-trivial words would get their pc exponent vector and their weight in the lower exponent-5 central series (`PCentralSeries(P,5)`).

## Mandatory checks (all passed)
- |P| = 5^34; nilpotency class 12; images of a, b generate P; every pcgs element has order dividing 5.
- Controls through the same pipeline: a⁵ and (ab)⁵ trivial; a, a⁴ and [a,b] non-trivial.

## Termination / baselines
Single deterministic pass, no seeds, no tuning. Baseline: the controls above. Anti-pattern check: nothing was tuned on the targets.

## Artifacts
`/media/psf/algo-mixer/runs/b25/b0-challenge-triviality/20260930T200842Z/` — script `b0_challenge_triviality.g`, `results.csv`, `provenance.json`, `gap_stdout.log`.
