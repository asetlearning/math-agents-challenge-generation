---
title: "B0 challenge triviality — results"
date: 2026-09-30
domain: group-theory
project: b25
experiment_type: b0-challenge-triviality
author: asetlearning
status: replicated
tags: [agent/exp-b25, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, project/b25, status/replicated, results, experiment]
---

# Results: 150 challenge words in B₀(2,5)

Methodology: [[b0-challenge-triviality-2026-09-30]]. Validator verdict: `#status/replicated` (independent nq 2.5.11 oracle, 150/150 agree) — [[2026-09-30-b25-b0-challenge-triviality]]. Applies to B₀(2,5) only.

| Quantity | Value |
|---|---|
| Words trivial in B₀(2,5) | **150 / 150** |
| Non-trivial | 0 |
| Empty words (trivial by definition) | 32 (R1–R4 and others; ids in `empty_ids.txt`) |
| Non-empty words trivial | 118 / 118 |
| |B₀(2,5)|, class | 5^34, 12 |
| Runtime | 2m50s wall, single GAP process |
| results.csv sha256 | `5de0d1faed20174bdd014e592d61957e9f7a54a464d1aebd9c22186144265951` |

## What this does and does not show
Each word lies in γ₁₃(B(2,5)), the kernel of B(2,5) → B₀(2,5). It says **nothing** about triviality in the free B(2,5), which is the open problem (Kourovka 11.48). Because ker = γ₁₃, B(2,5) is infinite iff γ₁₃ ≠ 1; these words are candidates that could still be non-trivial there.

Artifacts: `/media/psf/algo-mixer/runs/b25/b0-challenge-triviality/20260930T200842Z/`.
