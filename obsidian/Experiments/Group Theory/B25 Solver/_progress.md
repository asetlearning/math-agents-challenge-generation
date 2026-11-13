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

**After B4:** 103 candidates remain. B3 (re-rooting) and B4 (starts from B3's saved words, a greedy shortening step on the longest words) broke 13 more, up to C3\|6\|13 at 1109 letters. Length still decides: 24 of the 103 have at least 1000 letters, and 13 of those never got shorter in any run. A study of the T-028 generation ([[t028-generation-stats-vs-solver-fate-2026-11-13]]) finds no construction feature beyond length that predicts which words stay unbroken. Next (owner to decide): a beam run from the shortest saved words of the long words that came down, a new first step for words of at least 1000 letters, and the 34 T-028 words that timed out in generation.

## Results so far (2026-11-13)

104 verified breaks of benchmark words: 7 in registry revision 4, 62 in revision 5, 7 in revision 7, 4 in revision 8, 11 in revision 9, 13 in revision 10 ([[ds-b25-challenge-candidates]]). Each has a certificate, checked by the bench solver contract, the Lead's replay and the Validator's.

| Experiment | Job | What it does | Result | Cost |
|---|---|---|---|---|
| E1-charge-census | local | χ₆ charge of the 207 words | 139/207 nonzero | — |
| E2-whitehead-solvers | 20261105-015145-e82f23 | Whitehead minimisation, then the standard solver loop | 2 breaks (C1\|16\|3, C3\|4\|17) | ~$1.55 |
| E3-whitehead-loop | 20261105-062128-d106ca | Whitehead step inside the fixpoint loop, after every change | 4 breaks (+ C3\|4\|13, C3\|4\|28: W, R, W, R); 65 words end in an automorphic image (no certificate) | ~$2.0 |
| E0-rebuild-seed-pool | 20261105-081946-f7dadd | seed pools per track; group distance, hybrid score, local search, M2 (R2.5 on w·u⁻¹) on 6 targets | 3 of 6 targets broken on T-blind (C1\|6\|1, C3\|4\|15, C3\|4\|22); T-in and T-out none; formal pass criterion not met | ~$1.4 (+ $3.24 for a first run that timed out) |
| E4-blind-insertion-R | 20261105-154058-23a14c | on all 200: W; loop R, CL, KB, W (no D); M2 insertion with T-blind and v5 pools (n_r 30–1000, local search); shorter words fed back | 60 breaks (51 T-blind, 4 v5, 5 loop after insertion); 66 shortened, 74 unchanged | ~$12.25 |
| E4-mixer | 20261106-030542-31f058 | algo-mixer reducer (b25_gen rules, beam 1024, 300 s) as last stage on the 66 changed words, no feedback | 2 breaks (C3\|6\|21, C3r2\|2,2\|8); 13 shortened (uncertified; e.g. 583 → 156); 5 killed for memory | ~$1.67 |
| A-dense-m2 | 20261106-182636-716a09 | blind-pool insertion only, every attempt recorded (alignment, \|q\|, near-fireable runs, R2.5 step trace) on the 138 registry words + 64 E4 end words; pools T-blind, v5, long (8 ≤ \|v\| ≤ 12, words ≥ 500 letters); 1000 attempts below 600 letters, 1.5 CPU-h per word and pool above; 80% lcf / 20% random | 7 breaks (C1\|16\|2 v5; C1\|12\|14, C1\|16\|17, C1\|12\|1, C1\|12\|25 long; C1\|8\|16 T-blind; C3\|6\|23 from its E4 end word), 20 certificates; verified shortenings on 74 targets | ~$27 |
| B1-beam-pilot | 20261109-183503-e326b6 | beam over chains of blind-pool insertions (children = best unseen R2.5 trace states; width 16, depth ≤ 6) on 10 unbroken candidates of 519–796 letters; roots = registry word, E4 end word, A's shortest shortening; arms B (score = length), M (new letters weighted 0.5), control C (single insertions as in A) | 4 breaks (C3\|9\|25 B, M; C3\|4\|18 B; C1\|16\|29 B, M, C; C1\|12\|20 B, M, C), 9 certificates; at the CPU of B the control empties 0 of 10, B 4, M 3 | ~$27.6 |
| B2-beam-long-words | 20261111-021531-a885ac | beam arm B (score = length; width 12, depth ≤ 4, 6 CPU-h per word) on the 104 candidates of ≥ 500 letters; control C on 10 of them | 11 breaks (571–1017 letters; C3\|6\|7 at 1017 is the longest so far); none on the 10 control targets; C3\|4\|2 reached the empty word 43 times but is not certified (an uncertified kbmag step in its E4 end word) | ~$24 |
| B3-beam-reroot | 20261112-033029-51091b | beam arm B with re-rooting (a new beam from any state ≤ 0.75 × its root, at most 3 times; 6 CPU-h per word) on the 23 unbroken candidates < 500 letters and 20 B2 targets that came down; saves the 8 shortest words per target | 10 breaks (402–1100 letters; 7 of the 20 long words, all after a re-root; 3 of the 23 short); C3\|4\|2 down to 56 letters, not empty; the one-step kbmag certification job for C3\|4\|2 failed at caps 10⁷ and 2·10⁷ | ~$7 |
| B4-beam-dump-starts | 20261112-140433-c93577 | beam from the 2 shortest B3-saved words per target (chains kept), re-rooting; arm B on the 29 B3 targets without a break (6 CPU-h), arm BS on the 4 longest (greedy width-1 shortening step, then the beam; 12 CPU-h) | 3 breaks (C1\|8\|24, C1\|8\|11; C3\|6\|13 at 1109 letters, the longest so far, after the shortening step took it 705 → 381); the shortening step stalled on the other 3 long words | ~$12 |

- **Strongest result:** E4 broke 60 of 200 with the loop plus blind-pool insertion. The v5 control (period ≤ 5) broke the same kind of targets as T-blind (95 283 vs 95 307 M2 reductions; 4 breaks came first from v5), so on the shorter words relators of period 6–7 are not needed. Breaks come mostly from the shorter arms (C1\|6, C1\|8, C3\|4, C3r2\|2,2); the longest broken word has 765 letters.
- **Experiment A:** on longer words longer periods help: the long pool (8 ≤ |v| ≤ 12) broke 4 targets of 615–770 letters, and the 600–800-letter band gave 13 of the 20 empties (long pool there: 0.16 empties per CPU-hour). 19 of 20 empties came from the longest-common-factor selection. Near-fireable-run counts and the other static features did not beat the baselines; the early R2.5 trace separates empties perfectly (a pruning option, not a predictor). Analysis on all 280,381 attempts: Experimenter-B25, private run folder.
- **Earlier:** the E0 move broke half of its six targets, from a pool that never sees the target's recipe. In M2 the R2.5 input is 2–2.5× longer than the target, so the gain is not from a shorter start; the Validator's hypothesis is that the insertion is the uphill move greedy R2.5 cannot make by itself.
- **Beam pilot:** chaining insertions breaks words that single insertions do not reach at equal CPU: C3\|9\|25 (796 letters) and C3\|4\|18 fell only to the beam. Only 2 of the 7 breaking chains went above the word's length (by ≤ 5%); all are 3–4 insertions deep, and layers 5–6 (about 20% of the CPU) gave nothing. M never beat B. An early-trace cut that keeps every breaking attempt saves under 1% of CPU, so it stays off. Analysis: Experimenter-B25, private run folder.
- **B2:** the shortest start word decides: 9 of 27 targets with a start below 500 letters broke, 2 of 77 with longer starts; 40 targets without a shortened start, none broke. All breaks came within the first 7000 CPU-seconds of their run; 40 of the 59 runs that hit the cap never got below their start. Analysis: Experimenter-B25, private run folder.
- **B3 and B4:** re-rooting is what breaks long words: all 7 long-word breaks in B3 re-rooted at least once. Starting from saved words broke 2 of 29 more; the greedy shortening step reached its goal on 1 of 4 long words, and that word broke. 13 of the 24 candidates of ≥ 1000 letters never got shorter: at about 70 CPU-seconds per insertion attempt, 6 CPU-h is only about 300 attempts.
- **Generation study:** [[t028-generation-stats-vs-solver-fate-2026-11-13]]: of the 330 T-028 words, unbroken share rises with length within every arm (C1 ≥ 800 letters: 24 of 25); the t-words, signs, conjugators and the residual/W ratio show no effect.
- **Validator notes:** [[2026-11-04-b25-solver-e2-whitehead-breaks-check]], [[2026-11-05-b25-solver-e3-whitehead-loop-breaks-check]], [[2026-11-05-b25-solver-c1-6-1-smoke-break-check]], [[2026-11-05-b25-solver-e0-rebuild-seed-pool-breaks-check]], [[2026-11-05-b25-solver-e4-smoke-breaks-check]], [[2026-11-06-b25-solver-e4-blind-insertion-breaks-check]], [[2026-11-07-b25-solver-experiment-a-breaks-check]], [[2026-11-09-b25-solver-beam-pilot-partial-breaks-check]], [[2026-11-12-b25-solver-beam-b2-breaks-check]], [[2026-11-12-b25-solver-beam-b3-breaks-check]], [[2026-11-13-b25-solver-beam-b4-breaks-check]].
- **Math Expert:** [[2026-11-06-b25-solver-i2-collapse-predictors-review]] (peak framing, candidate features, the test run on A's data).

## Log
- 2026-11-04: project started (owner). Stage-1 plan written; development begins. Model training waits for the GPU server.
- 2026-11-05: E2 and E3 (Whitehead routes) break 4 candidates; E0 (blind-pool insertion + R2.5) breaks 3 more. Owner approves registry revision 4 (200 candidates) and E4 on all 200; no more refactoring of generation code: the effort goes to the solver.
- 2026-11-06: E4 on all 200 breaks 60; the algo-mixer last stage breaks 2 more (one after a certificate fix, b25 ec7f072). All 62 confirmed by bench, Lead and Validator. Owner approves registry revision 5 (138 candidates). Stage-1 cost so far about $24.70.
- 2026-11-09: experiment A (dense insertion data, 280,381 attempts, 25.3 h) breaks 7 more; 20 certificates confirmed by bench, Lead and Validator. Owner approves registry revision 7 (131 candidates) and the beam over insertion chains. Analysis: no static feature beats the baselines. Stage-1 cost so far about $52.
- 2026-11-10: the beam pilot (25.5 h) breaks 4 more; 9 certificates confirmed by bench, Lead and Validator. Owner approves registry revision 8 (127 candidates) and a beam run on the 104 remaining words of at least 500 letters. Stage-1 cost so far about $80.
- 2026-11-12: B2 (22.1 h) breaks 11 more; certificates confirmed by bench, Lead and Validator. Owner approves registry revision 9 (116 candidates) and the next beam run (short candidates + re-rooting). Stage-1 cost so far about $104.
- 2026-11-13: B3 (6.0 h) and B4 (10.7 h) break 13 more, up to 1109 letters; certificates confirmed by bench, Lead and Validator. Owner approves registry revision 10 (103 candidates). Generation study: only length predicts unbroken words. Stage-1 cost so far about $123.
