---
type: validation-triage
date: 2026-10-17
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "tcgraph PR #8 (t024-onion-cpp @ 4390614; b25 t018-diagram-search @ 5fbf9f7): junction filter, strictDepthFlip, inverseCellReduce speed-up"
---
# Triage: tcgraph PR #8 (onion port), math layer

This is a Lead request (2026-10-17), to be finished before any claim from the level-2 pilot. One verdict per item.

1. **Junction filter exactness.** Code reading of `JunctionTiler::pairOk_` and `run_`. The rejection argument needs the junction window z (tail of p_prev + head of p_next, freely reduced) to be a contiguous factor of the final cyclic w1.
   - Suspected gap: a short inner piece (|p| ≤ window) together with cancellation beyond the designed one letter at its *other* junction. Then window letters are cancelled in w1, and a rejection could be unjustified.
   - Empirical test on the pilot's tiles: many tilings (plain DP with noise, and the unfiltered junction DP), my own Python port of the window test, a check of whether z is a factor of w1, and a check for any rejected junction in a tiling whose w1 is 2.5-reduced.
   - The edge-of-window departure itself is sound if the factor property holds: a truncated run is a factor.
   - Accept side: the orchestrator selects finals by gate B (`power_gates`).
2. **strictDepthFlip.** Compare against the Math Expert's definition ([[2026-10-17-threshold-revision-exact-half-allowed]] item 3: exposed run *exactly* 2.5|v|, |v| even) and the Python `strict_depth_flip.py` (≥ 2.5|v|). Then a fuzz of C++ against Python, reusing `fuzz_eq.py` A/B, plus a check that S2 `strictDepth` is unchanged by the peel refactor.
3. **inverseCellReduce speed-up.** Diff reading against the reference copy in the test file, plus a spot-check of large stored certificates (> 150 cells, among the 325 skipped), C++ against Python. Capjob, one job at a time; rjob if too big.

Out of scope: the pilot's results, the K-best default (a heuristic by design), and performance.
