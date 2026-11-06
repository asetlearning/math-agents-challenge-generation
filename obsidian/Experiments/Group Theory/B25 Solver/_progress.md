---
title: b25-solver — experiment progress
domain: group-theory
project: b25-solver
instance: B(2,5)
status: draft
author: asetlearning
tags: [agent/lead, user/asetlearning, domain/group-theory, topic/b25, topic/burnside, topic/trivial-words, topic/word-problem, project/b25-solver, status/draft, experiment]
---

# b25-solver — Progress

Project profile: [[project-b25-solver]]. Goal: a solver for trivial words in B(2,5) that adapts to the given word. It is tested first on the benchmark words of [[ds-b25-challenge-candidates]]. Success is one verified break; a verified shortening counts as progress.

## Current question

**After E4:** 138 candidates remain. What breaks the 66 words the loop shortened but did not empty, and the 74 it did not change? Open options: a learned move order (stage-1 framing A/B with the transformer), wider pools or longer insertions, and the algo-mixer reducer inside the loop (it broke 2 of 66 and shortened 13 as a last stage). The next experiment is not chosen yet.

## Results so far (2026-11-06)

69 verified breaks of benchmark words: 7 in registry revision 4, 62 in revision 5 ([[ds-b25-challenge-candidates]]). Each has a certificate, checked by the bench solver contract, the Lead's replay and the Validator's.

| Experiment | Job | What it does | Result | Cost |
|---|---|---|---|---|
| E1-charge-census | local | χ₆ charge of the 207 words | 139/207 nonzero | — |
| E2-whitehead-solvers | 20261105-015145-e82f23 | Whitehead minimisation, then the standard solver loop | 2 breaks (C1\|16\|3, C3\|4\|17) | ~$1.55 |
| E3-whitehead-loop | 20261105-062128-d106ca | Whitehead step inside the fixpoint loop, after every change | 4 breaks (+ C3\|4\|13, C3\|4\|28: W, R, W, R); 65 words end in an automorphic image (no certificate) | ~$2.0 |
| E0-rebuild-seed-pool | 20261105-081946-f7dadd | seed pools per track; group distance, hybrid score, local search, M2 (R2.5 on w·u⁻¹) on 6 targets | 3 of 6 targets broken on T-blind (C1\|6\|1, C3\|4\|15, C3\|4\|22); T-in and T-out none; formal pass criterion not met | ~$1.4 (+ $3.24 for a first run that timed out) |
| E4-blind-insertion-R | 20261105-154058-23a14c | on all 200: W; loop R, CL, KB, W (no D); M2 insertion with T-blind and v5 pools (n_r 30–1000, local search); shorter words fed back | 60 breaks (51 T-blind, 4 v5, 5 loop after insertion); 66 shortened, 74 unchanged | ~$12.25 |
| E4-mixer | 20261106-030542-31f058 | algo-mixer reducer (b25_gen rules, beam 1024, 300 s) as last stage on the 66 changed words, no feedback | 2 breaks (C3\|6\|21, C3r2\|2,2\|8); 13 shortened (uncertified; e.g. 583 → 156); 5 killed for memory | ~$1.67 |

- **Strongest result:** E4 broke 60 of 200 with the loop plus blind-pool insertion. The v5 control (period ≤ 5) broke the same kind of targets as T-blind (95 283 vs 95 307 M2 reductions; 4 breaks came first from v5), so relators of period 6–7 are not needed: any short trivial word seems enough. Breaks come mostly from the shorter arms (C1\|6, C1\|8, C3\|4, C3r2\|2,2); the longest broken word has 765 letters.
- **Earlier:** the E0 move broke half of its six targets, from a pool that never sees the target's recipe. In M2 the R2.5 input is 2–2.5× longer than the target, so the gain is not from a shorter start; the Validator's hypothesis is that the insertion is the uphill move greedy R2.5 cannot make by itself.
- **Validator notes:** [[2026-11-04-b25-solver-e2-whitehead-breaks-check]], [[2026-11-05-b25-solver-e3-whitehead-loop-breaks-check]], [[2026-11-05-b25-solver-c1-6-1-smoke-break-check]], [[2026-11-05-b25-solver-e0-rebuild-seed-pool-breaks-check]], [[2026-11-05-b25-solver-e4-smoke-breaks-check]], [[2026-11-06-b25-solver-e4-blind-insertion-breaks-check]].

## Log
- 2026-11-04: project started (owner). Stage-1 plan written; development begins. Model training waits for the GPU server.
- 2026-11-05: E2 and E3 (Whitehead routes) break 4 candidates; E0 (blind-pool insertion + R2.5) breaks 3 more. Owner approves registry revision 4 (200 candidates) and E4 on all 200; no more refactoring of generation code: the effort goes to the solver.
- 2026-11-06: E4 on all 200 breaks 60; the algo-mixer last stage breaks 2 more (one after a certificate fix, b25 ec7f072). All 62 confirmed by bench, Lead and Validator. Owner approves registry revision 5 (138 candidates). Stage-1 cost so far about $24.70.
