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

**After experiment A:** 131 candidates remain. A gave insertion many more attempts on long words and a pool of longer periods (8 ≤ |v| ≤ 12); the long pool did best (4 of the 7 breaks, 0.048 empties per CPU-hour against 0.011–0.018). The analysis of A's data found no pre-insertion feature that beats the baselines (longest common factor, |q|/|w|) at predicting which attempts empty a word (only 20 positives, so no detectable signal rather than none). Next, approved by the owner: a beam over chains of insertions (walking up the peak), with the long pool on the long words; a learned model later on the GPU server.

## Results so far (2026-11-09)

76 verified breaks of benchmark words: 7 in registry revision 4, 62 in revision 5, 7 in revision 7 ([[ds-b25-challenge-candidates]]). Each has a certificate, checked by the bench solver contract, the Lead's replay and the Validator's.

| Experiment | Job | What it does | Result | Cost |
|---|---|---|---|---|
| E1-charge-census | local | χ₆ charge of the 207 words | 139/207 nonzero | — |
| E2-whitehead-solvers | 20261105-015145-e82f23 | Whitehead minimisation, then the standard solver loop | 2 breaks (C1\|16\|3, C3\|4\|17) | ~$1.55 |
| E3-whitehead-loop | 20261105-062128-d106ca | Whitehead step inside the fixpoint loop, after every change | 4 breaks (+ C3\|4\|13, C3\|4\|28: W, R, W, R); 65 words end in an automorphic image (no certificate) | ~$2.0 |
| E0-rebuild-seed-pool | 20261105-081946-f7dadd | seed pools per track; group distance, hybrid score, local search, M2 (R2.5 on w·u⁻¹) on 6 targets | 3 of 6 targets broken on T-blind (C1\|6\|1, C3\|4\|15, C3\|4\|22); T-in and T-out none; formal pass criterion not met | ~$1.4 (+ $3.24 for a first run that timed out) |
| E4-blind-insertion-R | 20261105-154058-23a14c | on all 200: W; loop R, CL, KB, W (no D); M2 insertion with T-blind and v5 pools (n_r 30–1000, local search); shorter words fed back | 60 breaks (51 T-blind, 4 v5, 5 loop after insertion); 66 shortened, 74 unchanged | ~$12.25 |
| E4-mixer | 20261106-030542-31f058 | algo-mixer reducer (b25_gen rules, beam 1024, 300 s) as last stage on the 66 changed words, no feedback | 2 breaks (C3\|6\|21, C3r2\|2,2\|8); 13 shortened (uncertified; e.g. 583 → 156); 5 killed for memory | ~$1.67 |
| A-dense-m2 | 20261106-182636-716a09 | blind-pool insertion only, every attempt recorded (alignment, \|q\|, near-fireable runs, R2.5 step trace) on the 138 registry words + 64 E4 end words; pools T-blind, v5, long (8 ≤ \|v\| ≤ 12, words ≥ 500 letters); 1000 attempts below 600 letters, 1.5 CPU-h per word and pool above; 80% lcf / 20% random | 7 breaks (C1\|16\|2 v5; C1\|12\|14, C1\|16\|17, C1\|12\|1, C1\|12\|25 long; C1\|8\|16 T-blind; C3\|6\|23 from its E4 end word), 20 certificates; verified shortenings on 74 targets | ~$27 |

- **Strongest result:** E4 broke 60 of 200 with the loop plus blind-pool insertion. The v5 control (period ≤ 5) broke the same kind of targets as T-blind (95 283 vs 95 307 M2 reductions; 4 breaks came first from v5), so on the shorter words relators of period 6–7 are not needed. Breaks come mostly from the shorter arms (C1\|6, C1\|8, C3\|4, C3r2\|2,2); the longest broken word has 765 letters.
- **Experiment A:** on longer words longer periods help: the long pool (8 ≤ |v| ≤ 12) broke 4 targets of 615–770 letters, and the 600–800-letter band gave 13 of the 20 empties (long pool there: 0.16 empties per CPU-hour). 19 of 20 empties came from the longest-common-factor selection. Near-fireable-run counts and the other static features did not beat the baselines; the early R2.5 trace separates empties perfectly (a pruning option, not a predictor). Analysis on all 280,381 attempts: Experimenter-B25, private run folder.
- **Earlier:** the E0 move broke half of its six targets, from a pool that never sees the target's recipe. In M2 the R2.5 input is 2–2.5× longer than the target, so the gain is not from a shorter start; the Validator's hypothesis is that the insertion is the uphill move greedy R2.5 cannot make by itself.
- **Validator notes:** [[2026-11-04-b25-solver-e2-whitehead-breaks-check]], [[2026-11-05-b25-solver-e3-whitehead-loop-breaks-check]], [[2026-11-05-b25-solver-c1-6-1-smoke-break-check]], [[2026-11-05-b25-solver-e0-rebuild-seed-pool-breaks-check]], [[2026-11-05-b25-solver-e4-smoke-breaks-check]], [[2026-11-06-b25-solver-e4-blind-insertion-breaks-check]], [[2026-11-07-b25-solver-experiment-a-breaks-check]].
- **Math Expert:** [[2026-11-06-b25-solver-i2-collapse-predictors-review]] (peak framing, candidate features, the test run on A's data).

## Log
- 2026-11-04: project started (owner). Stage-1 plan written; development begins. Model training waits for the GPU server.
- 2026-11-05: E2 and E3 (Whitehead routes) break 4 candidates; E0 (blind-pool insertion + R2.5) breaks 3 more. Owner approves registry revision 4 (200 candidates) and E4 on all 200; no more refactoring of generation code: the effort goes to the solver.
- 2026-11-06: E4 on all 200 breaks 60; the algo-mixer last stage breaks 2 more (one after a certificate fix, b25 ec7f072). All 62 confirmed by bench, Lead and Validator. Owner approves registry revision 5 (138 candidates). Stage-1 cost so far about $24.70.
- 2026-11-09: experiment A (dense insertion data, 280,381 attempts, 25.3 h) breaks 7 more; 20 certificates confirmed by bench, Lead and Validator. Owner approves registry revision 7 (131 candidates) and the beam over insertion chains. Analysis: no static feature beats the baselines. Stage-1 cost so far about $52.
