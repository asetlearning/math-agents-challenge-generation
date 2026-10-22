---
type: validation-verdict
date: 2026-10-18
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "tcgraph PR #8 (t024-onion-cpp @ 4390614, stacked on #7 5eb03be; b25 t018-diagram-search @ 5fbf9f7): junction filter, strictDepthFlip, inverseCellReduce speed-up"
verdict: "(1) junction filter NOT PROVEN EXACT (argument gap; usable as a filtered heuristic with the final gate); (2) strictDepthFlip port CONFIRMED vs Python, definition deviates from 'exactly 2.5|v|'; (3) inverseCellReduce speed-up CONFIRMED behaviour-preserving within the tested range"
---
# tcgraph PR #8 (onion port): math-layer review

Triage: [[2026-10-17-tcgraph-pr8-onion-triage]]. This was a Lead request (2026-10-17): verdicts on three items, due before any claim from the level-2 pilot.

Build: a clean archive of b25 5fbf9f7 plus tcgraph 4390614 in the scratchpad; ctest 20/20 passed. The old inverseCellReduce came from the PR #6 build, since `certificate_reduction.cpp` is unchanged between f2cb8a1 and 5eb03be. Every run used `python -S` with explicit paths and capjob (2G, 1 CPU), one job at a time. The printed module paths confirm the scratch `.so` was loaded. Scripts and outputs are in `Agents/asetlearning/Validator/scratch/onion/`.

Terms used below:
- **Piece t**: the word a tile contributes, t = r'[l:] with r' a rotation of the tile's relator u.
- **Inner part p**: p = t[1:-1].
- **Junction**: the join of two consecutive pieces. The designed rule is that exactly one letter cancels there.
- **Window z**: the filter's test word at a junction, z = tail₂₅(p_prev) + head₂₅(p_next), freely reduced. The filter rejects the join if z contains a run of period q and length m with 2m > 5q, i.e. exponent > 2.5. The run may touch the window edge.
- **Gate B**: the final exact 2.5-reduced check (`power_gates`) that the orchestrator applies to finals.

## (1) Junction-aware DP filter: is it exact?

**VERDICT: NOT PROVEN EXACT.** The argument has a gap, and its premise is false on about 11% of passed junctions. Empirically there were no wrong rejections. Scope: `pairOk_` / `run_` read, plus my own Python port of the window test, on the pilot's tiles.

- **Accept side: safe.** The filter only rejects, and every final passes through gate B. So an invalid tiling can never be reported as valid.
- **Reject side: the premise fails.** The Developer's argument, including the extension to runs that touch the window edge, is "a run in z is a factor of w1, so w1 has the power". That needs z to be a contiguous factor of the cyclic w1, and it is not always one.
  - `pairOk_` freely reduces z beyond the one designed letter.
  - At the *other* junction of a short piece (|p| ≤ 25), extra cancellation can eat window letters. Those letters are then absent from w1.
  - Measured with tagged reduction (each letter carries its piece and position). On junctions that the filter passed, z was **not** a factor of w1 in:
    - L1 words: 1,332 of 12,359 junctions;
    - L2 words: 3,261 of 29,702 junctions.
  - Extra cancellation (more than one letter at some junction) is the common case: 2,250 of 2,480 L1 tilings and all 2,480 L2 tilings have it.
  - Example (L2): piece bAAbABaaB followed by bAAB…. The cancellation continues past the designed letter ("aa" cancels as well), so the last two letters of the previous window are not in w1.
  - A rejection of z is justified only if the offending run survives into w1. Without the factor property, that is not guaranteed.
- **Empirical:**
  - Runs: `junction_check.out` (30 words × 21) and `junction_check2.out` (80 words × 31), over plain DP tilings with noise and the unfiltered junction DP.
  - **0 unjustified rejections** among 13,906 rejected junctions, i.e. in no case did w1 end up 2.5-reduced while a junction had been rejected.
  - 0 rejections among the 815 tilings that pass gate B.
  - My reconstruction of w1 equals `tilingWord` on every tiling.
- **Sufficient condition for exactness:** exactly one letter cancels at every junction. Then each window is a factor of w1, and the Developer's argument, including the edge-touching departure, goes through.
- **Options:**
  - (a) Reject or defer joins with extra cancellation.
  - (b) Carry the cancellation depth in the DP state, and test the window on the letters that actually survive.
  - (c) Keep it, documented as a heuristic filter.
- **Consequence for the pilot:**
  - "The filtered DP found no tiling" is **not** a proof of non-existence. K-best = 64 makes it a heuristic anyway.
  - Positive results that pass gate B are unaffected.
  - Do not claim the filter is exact.
- **Not checked:**
  - DP optimality among the tilings the filter passes (the Developer's exhaustive check; I did not re-run it).
  - A direct comparison of the C++ `pairOk_` with my port: there is no binding for it. My port follows the source line by line. An output-level check (every junction of a `JunctionTiler.tile` output passes my port) is a cheap follow-up if wanted.

## (2) strictDepthFlip

**VERDICT: the port is CONFIRMED equal to the Python reference. The definition DEVIATES from the Math Expert's.** Scope: C++ vs `t018/scripts/strict_depth_flip.py:analyse_flip` at 5fbf9f7.

Terms: a **flip cell** is a cell with an even root length |v| ≥ 2 whose exposed boundary run is at least 2.5|v|. It is absorbed at peel time, like |v| = 1 cells. A side is **exposed** if no other cell that has not been removed shares its edge.

- **Equivalence:** `fuzz_flip.out` and `flip_deep.py`. Whole-result equality of both the flip result and the S2 strict depth:

  | Input set | Certificates | Equal | With N_flip > 0 |
  |---|---|---|---|
  | Restart-derived | 1,496 | 1,496 | 1,259 |
  | Random small-table | 5,493 | 5,493 | 5,002 |
  | Derived from depth-2/3 certificates (restart `cert_*.json`, area7 `best_line*.json`) | 172 | 172 | 169 |

  - Total failures: 0.
  - S2 strictDepth is unchanged by the peel refactor.
  - The flip changes depth in practice. The (S2, flip) maxdepth pairs include (1,0), and the depth-2/3 set has (2,2).
- **Definition:** the Math Expert's text ([[2026-10-17-threshold-revision-exact-half-allowed]] item 3) says the exposed run is *exactly* 2.5|v|. Both the C++ and the Python use **≥ 2.5|v|**.
  - The test runs at every inner layer, relative to cells already peeled, not only on the original boundary.
  - So it absorbs a superset of the cells the Math Expert describes. As a control this is conservative: it can only lower depth. But it can erase depth that is genuine under the exact-2.5 definition.
  - The Math Expert or Lead must confirm which definition is intended before any claim relies on flip depth.

## (3) inverseCellReduce speed-up

**VERDICT: CONFIRMED behaviour-preserving within the tested range.**

- **Code reading** (new vs old):
  - The reductions are stack-based.
  - The length shortcut 2|a|+|x|−2c₁−2c₂ is used only as an early reject. It is exact when c₁ < min(|a|,|x|) and c₂ < |x|−c₁; otherwise the code does the full comparison.
  - classKey (least rotation of the cyclic core) is invariant under conjugation, so carrying it through rewrites is sound.
  - The incremental rb for the suffix form is correct.
  - The scan order is unchanged.
  - Factors that do not move keep their exps.
- **Spot-check** (`icr.out`, `icr_make.py`, `icr_drive.py`):
  - Inputs: 14 stored certificates of 151–1,197 cells, all from the skipped >150 range.
  - Each was run as stored and as a "planted4" copy, which adds 4 inverse pairs at prefix and suffix.
  - Comparison: whole output certificate.
  - Timeout: 900 s per run. Python was run only up to 400 cells, within a 45-minute total budget.

  | Cells in | Cells out | new = old | new = Python | new (s) | old (s) | Python (s) |
  |---|---|---|---|---|---|---|
  | 151 / 159 | 125 | ✓ ✓ | ✓ ✓ | 0.4 / 0.6 | 6 / 8 | 195 / 252 |
  | 174 / 182 | 144 | ✓ ✓ | ✓ ✓ | 1.2 / 1.7 | 18 / 25 | 590 / 808 |
  | 192 / 200 | 160 | ✓ ✓ | timeout / budget | 2.0 / 3.4 | 30 / 55 | — |
  | 199–316 (5 certs × 2) | 161–261 | 10 / 10 ✓ | budget | 2.8–25.8 | 51–657 | — |
  | 378–637 (3 certs × 2) | 324–541 | old timed out | budget | 72–510 | > 900 | — |
  | 1,197 / 1,205 | — | both timed out | — | > 900 | > 900 | — |

  - **new = old on 20 of 20 compared runs** (151–316 cells).
  - **new = Python on 4 of 4** (151–182 cells).
  - Every certificate shrinks, so the inputs are not already reduced and the test has teeth.
  - The speed-up over old is about 15–25×.
  - Above 316 cells the new code runs but has no reference to compare against.
- **Not checked:**
  - Python equivalence above 182 cells. It runs at about 200–800 s per case at this size, so larger cases need rjob.
  - Any equivalence above 316 cells.
  - The 1,197-cell certificate: the new code also exceeds 900 s on it.

## Summary for the pilot

- The junction DP is a filtered **heuristic**. Positive finals are valid by gate B. A negative "no tiling" is not a proof.
- Flip depth uses ≥ 2.5|v|. Confirm the definition before quoting it.
- inverseCellReduce output can be trusted to equal the old code up to 316 cells, and the Python up to 182 cells.
