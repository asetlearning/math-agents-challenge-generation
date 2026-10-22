---
type: code-review
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: code review of tcgraph branch feat/t028-pilot-cpp (worktree tcgraph-t028, from main 63564c3, uncommitted): the R trace in reduction2_5, the new probe_b/ (B-probe sampler) and the new kbcert/ (C++ port of t018/kbcert.py)"
verdict: "CONFIRMED on correctness for all three. R trace: same result as the untraced reducer on 27,328 words (incl. the 351 pool words, the 12 T-024 originals and the 35 T-027 chain words); the free-group identity c = cells * H * result * H^-1 holds on every word; every cell is a literal u^5 with u cyclically reduced and primitive; the untraced path is unchanged in output and speed (pin 63564c3 vs branch: identical, within 0.2 %). probe_b: cell products, the cyclic split, max window exponent and the 2.5-reduced decision agree with an independent brute force on 368 patches; closed = 2.5-reduced and rho >= 0.5 as pre-registered; deterministic. kbcert: rule parsing equals Python's (97,483 rules, 0 mismatches); the golden test reproduces R1 and R2 cell for cell; R3 at cap 1e6 reproduces the registry's 2,364-cell certificate exactly; ds665 certified (3,915 cells); L0 re-checked independently. ISSUES: (1) beam width: the pre-registration says 64, the code default and the Developer's plan use 50 (needs Lead's decision); (2) R-trace cells have periods up to 39 (5 % of the cells on substitution words have |u| > 7): they are relators of B(2,5) but not R7 cells, so the R-step fragments are not L0 over R7 without a further certification step; (3) the probe JSON lacks seed, code version and instance indices, and archives at most 3 closed patches per setting; (4) reuse and style: duplicated word helpers in probe_b and kbcert, a third hash scheme in kbcert, output-pointer parameters, two cell types (PowerCell, ExponentCell) with opposite composition orders, and changes to existing functions (approval rule)."
re_check: "CONFIRMED after the Developer's fixes. R trace: 27,328 words again 0 mismatches and 0 identity failures (same cell counts), the library cellsProduct agrees on every word, untraced speed equal to the 63564c3 pin. probe_b: beam 64 default, distinct mutation positions, JSON with seed, revision, per-index max exponents, rhos and every closed patch; deterministic and prefix-stable in n. kbcert: golden test passes as its own ctest entry; R3 identical to the registry again (2,364 cells, L0 true). PowerCellCertifier: sound (independent L0 over my R7 table on 43 words, 0 failures) and honest (only cells with |u| > 7 reported uncertified). Finding for T-028: on C1-like substitution words it certifies only 21 of 147 long cells (14 %) at cap 2e5 with the rec rules, so most R-step fragments stay L0 over U. Not unifying ExponentCell and PowerCell is acceptable."
---
# T-028 tcgraph branch: R trace, probe_b, kbcert

These are three Lead requests (2026-10-20), covered in one note for the whole branch. The triage note is [[2026-10-20-t028-cpp-rtrace-probe-b-review-triage]].

**Code reviewed** (worktree `tcgraph-t028`, branch `feat/t028-pilot-cpp` from 63564c3, uncommitted):
- the R-trace diff (greedy_reduction.h/.cpp, plus 2 tests);
- `probe_b/` (290 lines, plus app and 6 tests);
- `kbcert/` (460 lines, plus app and 6 tests);
- the b25 binding patch the Developer keeps aside.

**Method.**
- I read all the code.
- I built my own out-of-tree copies under capjob (2 GB / 2 CPUs, Release): the branch, and the 63564c3 pin for the timing.
- I wrote three independent drivers in my scratchpad:
  - `rtrace`: equivalence, the free-group identity, cell shape and timing;
  - `pbcheck`: brute-force window exponents and cell products for `samplePatch`;
  - `kbrules`: C++ rule set vs Python `load_rules`.

  An independent Python L0 check covered the kbcert output, using my R7 core table built with b25's `kbcert.core_table`.
- The word sets stayed in scratch, because the T-024 words are private:

  | set | words | what |
  |---|---|---|
  | pool | 351 | the t-pool (certified, length 50–80) |
  | T-024 originals | 12 | |
  | T-027 chain words | 35 | |
  | planted powers | 19,998 | words with planted powers v^e, \|v\| ≤ 9, e 2–12 |
  | random | 5,000 | random reduced words, length 20–300 |
  | substitution images | 1,932 | images of pool words under random substitutions with \|x\|, \|y\| from 4 to 8 (C1-like W) |

## 1. The R trace (`greedyReduceCyclicExhaustiveTraced`)

**The algebra (read).**
- **One replacement** x·lhs·y → x·rhs·y records the cell (core lhs·rhs⁻¹, conjugator x⁻¹). Then old = cell · new, and the core is the literal (base)⁵. That is true for both rules (u^p → u^{-(5-p)}, and u⁵ → empty).
- **Commit order.** Cells are committed only when the loop accepts the rewrite. A rewrite rejected by `explored` is not recorded.
- **One shift.** w = g·perm·g⁻¹, perm = cells·v, v = u·result·u⁻¹.
- **Composition across iterations.** The conjugator is c·g⁻¹·H⁻¹ and the rotation is H·g·u. The comment in the code derives this, and I re-derived it.

**Checked (27,328 words):**

| set | n | traced ≠ untraced | identity fails | bad cores | words R changed | cells | cells with \|u\| > 7 | max \|u\| |
|---|---|---|---|---|---|---|---|---|
| pool | 351 | 0 | 0 | 0 | 0 (2.5-reduced) | 0 | 0 | – |
| T-024 originals | 12 | 0 | 0 | 0 | 5 | 6 | 0 | 6 |
| T-027 chain words | 35 | 0 | 0 | 0 | 24 | 869 | 1 | 8 |
| planted powers | 19,998 | 0 | 0 | 0 | 19,886 | 194,021 | 2,659 | 9 |
| random | 5,000 | 0 | 0 | 0 | 4,883 | 43,697 | 1 | 8 |
| substitution images | 1,932 | 0 | 0 | 0 | 1,845 | 45,910 | **2,339** | **39** |

- **Identity:** c = cells[0]⋯cells[n−1]·H·result·H⁻¹, freely reduced, where c is the cyclic reduction of the input.
- **Bad cores:** a core counts as bad if it is not a literal u⁵ with u cyclically reduced. No cell had u a proper power. 8,355 words had a non-empty rotation H.
- **The branch's own tests:** `test_greedy_reduction` passed 51/51.

**(3) Untraced path unchanged.**
- **Output:** identical (the equivalence above, and the same checksum of result lengths).
- **Speed:** the same 3,300 words, two alternating runs per build, with the same compiler and flags:

  | set | pin 63564c3 | branch |
  |---|---|---|
  | planted | 53.76 s | 53.70 / 53.76 s |
  | random | 23.32 / 23.34 s | 23.32 / 23.35 s |
  | substitution | 30.25 s | 30.21 / 30.23 s |

  No measurable change. The traced call costs about 1 % more than the untraced one.

**Issue R1: cells longer than R7 (matters for certification).**
- The trace's cells are u⁵ for **any** period. On the C1-like substitution words, 5 % of the cells have |u| > 7, with periods up to 39.
- These are relators of B(2,5) (L0 over U_∞, the set of all u⁵), but **not R7 cells**.
- r7 says the R trace "supplies the R-step fragments" of a certificate composed with cert(W). Each long cell then needs its own R7 certificate, for example `kbcert::certifyCyclicWord` on u⁵. That certificate may fail or be large.
- **Pin:** the T-028 certification step must say how a cell with |u| > 7 is handled. Otherwise the composite is "L0 over U" and **not L0-cert** in the registry's sense.

**Issue R2: reuse and style (`tcgraph/CLAUDE.md`).**
- **Existing functions are modified:** `greedyReduceImpl`, `applyRule` and `greedyReduceCyclic` now route through recorded variants. Behaviour and speed are unchanged (above), but the rule "modifying existing code needs approval" applies, so Lead or the owner must approve.
- **Output-pointer parameters:** `cells*`, `prefixes*` and `trace*` in the internal functions, against "No output parameters". This is acceptable for internal helpers if it is noted.
- **Two cell types in one header,** with opposite composition orders:
  - `PowerCell` (core u⁵), with c = cells·H·result·H⁻¹;
  - the existing `ExponentCell` (x^{±5}), with w = rot·word·rot⁻¹·cells.

  An ExponentCell is a PowerCell with |u| = 1. Unify them, or at least document the two orders side by side.
- **A test helper duplicates library code:** the test's `powerCellsProduct` duplicates `cellsProduct`. Add a `cellsProduct(const std::vector<PowerCell>&)` overload in the library.
- **A muddled test:** `EmptiesAFifthPowerWithOneCell` builds its input through a convoluted ternary and does not assert that there is one cell.

## 2. probe_b (the B-probe sampler)

**Against §B, r6, r7 and §9.5.**
- **Object:** a k-cell product, cells c⁻¹·(rotation of u_i)^{±5}·c with c the suffix S, so P′ = A·x·S = P·S⁻¹xS. Correct.
- **Closed** = non-empty, 2.5-reduced (cyclic and linear, `is2p5Reduced`) and ρ ≥ 0.5 over the 16 images, with R = `greedyReduceCyclicExhaustive`. Correct.
- **Move set:** both signs, all |u| distinct rotations of u^{±5} (the same set as "5|u| rotations"), depth δ ∈ [0, ℓ]. Correct.
- **Greedy:** picks the shortest P′ (the most cancellation), with random ties. Correct.
- **Beam:** ranks by the maximum window exponent of the cyclic word (`reduction2_5::runs`, which is the reuse asked for), with ties by length; distinct products. Correct.
- **Roots:** a seed uniform over cyclically reduced primitive words of length ℓ, and d mutations per root.

**Checked.**
- **`test_probe_b`:** 6/6 passed.
- **`pbcheck`:** 368 patches (greedy and beam; ℓ 20 and 30; k 3 and 4; d 1 and 3). For every patch:
  - the cell product equals P;
  - the cores are literal primitive u⁵;
  - P = unconj·C·unconj⁻¹;
  - the max window exponent equals a brute-force scan (cyclic, windows ≤ n);
  - the 2.5-reduced flag equals a brute-force test (cyclic and linear).

  There were 0 mismatches. None of the patches was 2.5-reduced, and the best max exponent was 4.1, in line with the Developer's 4.27–5.0.
- **Determinism:** `samplePatch(params, i)` gave the same patch twice, and the app's JSON (without `seconds`) was byte-identical over two runs. Instance i uses its own stream from (seed, i), so it does not depend on n or on other instances. Greedy and beam share the roots of instance i, which makes them a paired comparison.

**Issues.**
- **P1, beam width (needs Lead's decision).**
  - §B pre-registers **beam width 64**. The code's default is 50, and the Developer's cost note calls "beam width 50 without preselection" "the pre-registered sampler". The 50 in r6 is the per-setting **denominator** (50 beam products), not the width.
  - Either run with `--beam-width 64`, or record 50 as a deviation. At 64, the beam CPU rises by about 30 % (roughly 15–26 CPU-h, from the Developer's 12–20).
  - The app runs fine at 64.
- **P2, what the JSON needs for the drop/pause rule.**
  - It already has the per-setting counts: products, 2.5-reduced, closed, min max exponent, mean length.
  - **Missing:** the seed, the tcgraph revision or binary hash, and the instance index of each example.
  - **Archive:** examples are capped at `--examples` 3. The rule is "any closed patch is archived and escalated", so write **every** closed patch, with its index.
  - **Optional:** a near-miss summary. The distribution of max exponents, and ρ of the 2.5-reduced but not closed patches, would help the "pause" decision.
  - **Small:** `min_max_exponent` prints 1e9 when every product is empty.
- **P3, mutations.** The d mutation positions can repeat, so fewer than d letters may change. Draw d distinct positions.
- **P4, reuse and style.**
  - `inverse`, `rotated`, `power5`, `cyclicallyReduced` and `randomLetters` re-implement `Word` operations (`-w`, `<<`, `^`, `isCyclicallyReduced`, `Word::random(…, rng)`) on `std::vector<int>`.
  - The public `insertAt` takes and returns `std::vector<int>`, while CLAUDE.md says "std::vector<int> is not a word in an API". Keeping it as a local buffer is fine; use `Word` in the API.
  - `expand` takes an unused `rng`.
  - Duplicates are dropped by hash only (`unordered_set<size_t>`), so a WordHash collision would drop a distinct candidate. This is negligible, but a set of `Word` is exact.

## 3. kbcert (the C++ port of `t018/kbcert.py`)

**Soundness.**
- **L0 in `certifyWord`.** The final check re-expands the composed cells over the RelatorMap and compares the result with the freely reduced input. If they differ, it throws `std::logic_error`. The check is independent of the path.
- **The closure:**
  - every move has period m ≤ 7 (`kMaxPeriod`);
  - each cell is v⁵ matched through `RelatorClassIndex::match`, and a non-match is a failure, not a cell;
  - the end state is the empty word or a table class.

  So every cell is an R7 cell.
- **Port fidelity:** the move order, the BFS FIFO and the cap check (after the hit test) follow `_moves` and `closure_path` line for line. `canonRot` uses `leastRotationIndex` with the same letter order as Python's `_canon_rot` (−2 < −1 < 1 < 2).
- **Small:** `certifyCyclicWord` is public but does no L0 of its own. Only `certifyWord` checks. Add the check there too, or document that callers must check.

**Identity with Python.**

| check | result |
|---|---|
| rule parsing: `RuleSet::load` vs Python `load_rules` on rec.kbprog | **97,483 = 97,483** rules, every (lhs, rhs) equal. The file has 97,484 equations: one lhs repeats, and both keep the later one. |
| core table: `onion/tests/data/core_table_r7.json` vs my R7 core table | equal, 1,630 entries |
| golden test, run with `KBCERT_RULES` and `KBCERT_REGISTRY` set | R1 (199 cells) and R2 (325 cells) **identical** to the registry, cell for cell; 6/6 passed |
| **R3** at cap 10⁶ (my run of `kbcert.kbcert_run`) | **2,364 cells, identical to the registry certificate**, L0 true, 43 s |
| ds665_L2 at cap 10⁶ | certified, 3,915 cells, L0 true (my Python check), 28 s. The registry keeps the original 618-cell certificate from a different method, so they are expected to differ. |

**Note on the "23/23".** The golden test is skipped unless both environment variables are set, so a plain `ctest` does not run it. It passes when they are set (above). Consider adding R3 to the golden test, as an opt-in at about 45 s.

**The `rewritePath` fix (restart position).**
- After a rewrite at `hi`, the scan restarts at min(hi, common − max_len + 1), where `common` is the first changed position.
- A window starting at i is unchanged for every rule length if i + max_len ≤ common. Positions below `hi` had no match in the old word. So no match can start before the restart point. The fix is correct.
- The differential test against the naive leftmost-shortest rewrite (300 random systems) passes, and the R1/R2/R3 identity confirms it on the real system.
- I did not mutation-test the old bug.

**Issues.**
- **K1, a third hash scheme.** `hashLetters` is an FNV hash, against CLAUDE.md's "WordHash or RollingHash … Don't write a third scheme". Use `WordHash`.
- **K2, duplicated helpers.** `inverse`, `concat`, `freeReduce` and `cyclicReduce` on `std::vector<int>` duplicate `Word`'s members. `inverse` now exists twice in the new code, once in probe_b and once in kbcert. If speed is the reason, put one letter-buffer utility in `word.h`.
- **K3, negative exponents.** `parseKbmagWord` accepts `a^-1` through `std::stoul`, which wraps around and requests an enormous allocation. Reject negative exponents. The rec and slx systems use `A` and `B`, so this does not happen today.
- **K4, the test data path.** `KBCERT_TEST_DATA_DIR` uses `CMAKE_SOURCE_DIR`, the existing surgery pattern, so the test finds no data when tcgraph is built as a subproject. This happened in my out-of-tree wrapper build. b25 builds tcgraph with `EXCLUDE_FROM_ALL`, so it does not bite there. `PROJECT_SOURCE_DIR` would be more robust.
- **K5:** `ClosureStats*` is an output parameter; returning a struct is the house style.
- **The app:** the conjugators are printed as integer lists (`toCellsJson`), while the registry uses aAbB strings. Convert one of them when composing.

## Verdict

**CONFIRMED on correctness** for all three components:
- the R trace is exactly equivalent and its identity holds;
- probe_b decides "2.5-reduced" and "closed" correctly and is deterministic;
- kbcert is sound (L0, R7 cells only) and identical to the Python port, including R3.

**Before the T-028 runs:**
- **P1:** decide the beam width, 64 as pre-registered or 50 as a recorded deviation.
- **P2:** add the seed, the revision and the index to the JSON, and archive every closed patch.
- **R1:** decide how R-trace cells with |u| > 7 are certified over R7 before a composite is called L0-cert.

**Before or with the commit (reuse and style):**
- R2: approval of the changes to existing functions; one cell type, or the composition orders documented; a library `cellsProduct` for `PowerCell`.
- P4: probe_b on `Word`.
- K1/K2: `WordHash` and no duplicated helpers.
- K3: reject negative exponents.
- P3: distinct mutation positions.

The tests and the identity checks do not depend on these changes, but each change must keep them passing.

## Re-check after the Developer's fixes (2026-10-20)

Lead request: re-check only the touched parts. Triage: [[2026-10-20-t028-cpp-rtrace-probe-b-review-triage]]. I rebuilt my out-of-tree copy of the branch (still uncommitted, from 63564c3) and reran my scratch drivers, all under capjob (2 GB / 2 CPUs), one job at a time.

**1. R trace after the refactor** (internal helpers `applyRuleImpl`, `greedyReduceImpl`, `greedyReduceCyclicImpl` now return `RuleApplication`, `GreedyRun`, `CyclicRun`; no output pointers; library `cellsProduct(std::vector<PowerCell>)`).
- **Equivalence and identity:** the same 27,328 words. 0 mismatches between traced and untraced, 0 identity failures, 0 bad cores, in every set. The cell counts are the same as before the refactor (for example 194,021 on planted powers and 45,910 on substitution images, max period 39). My driver now also compares the library `cellsProduct` with its own product: equal on every word.
- **Speed of the untraced path**, 3,300 words, two alternating runs per build:

  | set | pin 63564c3 | branch |
  |---|---|---|
  | planted | 54.41 / 53.84 s | 53.85 / 53.92 s |
  | random | 23.45 / 23.53 s | 23.55 / 23.43 s |
  | substitution | 30.29 / 30.58 s | 30.39 / 30.39 s |

  No measurable change; the checksum of result lengths is the same (125,923).
- **Tests:** `test_greedy_reduction` 52/52. `EmptiesAFifthPowerWithOneCell` now asserts exactly one cell, and the tests use the library `cellsProduct`.
- R2 is resolved, apart from the approval of the change to existing functions, which is the owner's (Lead has asked).

**2. probe_b.**
- **Beam width** 64 is the default and is recorded in the JSON (`beam_width`, `preselect` 0). P1 is resolved as pre-registered.
- **Mutations:** `mutatedRoot` draws d distinct positions. My check on 1,225 roots (d = 1, 2, 3, 5): each is a rotation of the seed with exactly d letters changed, cyclically reduced and primitive. P3 resolved.
- **JSON (P2):** `seed`, `tcgraph_revision`, per-index `max_exponents` (the near-miss profile), `rhos` as (index, ρ) for every 2.5-reduced patch, and `closed_patches` with index, cyclic word, ρ, cells and unconj, all of them. `min_max_exponent` is null when every product is empty.
  - My check: `runProbe`'s per-index fields equal `samplePatch(params, i)` for every index (greedy 40, beam 4), and the counts match the lists.
  - **Determinism:** greedy (n 100) and beam (n 3) JSON identical over two runs, without `seconds`. Running n = 40 gives exactly the first 40 entries of the n = 100 run, so instance i does not depend on n.
  - **Untested path:** none of my samples gave a closed or even a 2.5-reduced patch (best max exponent 4.1), so the `closed_patches` and `rhos` output has only the unit test's coverage (`closed_patches.size() == closed`).
  - **Small:** `--revision` defaults to "unknown". The T-028 runner must pass the commit hash (the run is from committed code), or the app should refuse to run without it.
- **Reuse (P4):** probe_b now works on `Word` (`<<`, `^`, `-`, `Word::random(…, rng)`); duplicates are dropped by an exact `unordered_set<Word, WordHash>`; `insertAt` takes and returns `Word`.
- `pbcheck` (368 patches against brute force) again 0 mismatches; `test_probe_b` passes.

**3. kbcert.**
- **Golden test:** `test_kbcert_golden` is its own ctest entry, Skipped without `KBCERT_RULES`/`KBCERT_REGISTRY`. With them set, R1 and R2 are reproduced (pass, 5.3 s). `test_kbcert` 8/8 with the environment set.
- **R3 at cap 10⁶:** 2,364 cells, **identical to the registry certificate**, L0 true in my independent Python check (40 s). ds665_L2: 3,915 cells, L0 true, as before.
- **Rules:** 97,483 rules, 0 mismatches with Python `load_rules`; core table equal (1,630).
- **Fixes:** no FNV hash (the closure table uses `WordHash`), no duplicated letter helpers in kbcert or probe_b, `ClosureResult` returned instead of a stats pointer, `parseKbmagWord` rejects a non-digit exponent such as `a^-1`, and the test data path uses `PROJECT_SOURCE_DIR`. K1–K5 resolved.

**4. The new `PowerCellCertifier`.**
- **Read.** For each trace cell c⁻¹·u⁵·c, the core u⁵ is certified as a word: first the closure search (`certifyCyclicWord`, periods ≤ 7), then, if rules are given, the kbmag rewriting path (`certifyWord`, itself L0-checked). The core's cells (c_j, R_j) become (c_j·c, R_j), which is right for c⁻¹(∏ c_j⁻¹R_jc_j)c. A core that is not certified within the cap is listed in `uncertified` and contributes no cells. At the end the R7 cells are expanded over the RelatorMap and compared with the product of the certified trace cells, and a mismatch throws. Every output cell comes from a closure move of period ≤ 7 or a table class, so it is an R7 cell. **Sound.**
- **Run** (my driver `pccheck`, then my Python L0 over my own R7 table from b25 `kbcert.core_table`, independent of the C++ RelatorMap):

  | run | words | trace cells | cells with \|u\| > 7 | uncertified | R7 cells out | independent L0 |
  |---|---|---|---|---|---|---|
  | closure only, cap 2·10⁴ | 3 | 72 | 13 | 9 | 98 | 3/3 |
  | closure + rec rules, cap 2·10⁵ | 40 | 1,234 | 147 | 126 | 1,281 | 40/40 |

  The words are the first substitution images (C1-like) with a long cell. Every short cell (|u| ≤ 7) was certified; every uncertified cell is a long one. **Honest:** nothing is guessed, and nothing uncertified is counted.
- **Finding for T-028 (not a code issue).** Only **21 of 147** long cells (14 %) were certified: periods 8–12 sometimes, none of period ≥ 13 (up to 34 in this sample). In the closure-only pilot the failures took under 1 ms, which suggests that u⁵ for such u has no non-increasing move of period ≤ 7, so the closure stops at once; the rec rules do not certify them within the cap either (I did not separate why). So on C1-like W the **R-step fragments will mostly be "L0 over U", not L0 over R7.** The T-028 report must give that label, as the header comment says, and should not expect the composite certificates of residuals to be L0-cert. A larger cap, or a dedicated certification of u⁵ for long u, would be separate work.
- **Small (C1):** `PowerCellCertificate.cells` concatenates the certified cells' R7 cells in trace order, with no boundaries. When some cells are uncertified, a caller who wants to splice the uncertified cells back in (to write the composite "L0 over U" certificate) cannot tell where they go. Record, for each trace cell, the range of its R7 cells (or return one certificate per trace cell). The L0 check itself is correct as it stands.

**5. Not unifying `ExponentCell` and `PowerCell`: acceptable.**
- An ExponentCell is the one-letter case of a PowerCell, but the two traces compose in opposite orders (`NormalizedExponents`: cells last; the R trace: cells first), and `ExponentCell`/`normalizeExponents` are used outside the module (`search/src/expand.cpp`). Unifying would change an existing API, which needs approval and gains nothing for T-028.
- The header now documents both orders side by side at `PowerCell`, and `cellsProduct` has an overload for each, so a caller cannot mix them up silently.

**Result: CONFIRMED.** Every item from the first review is resolved, apart from the owner's approval of the change to existing functions. Open, none blocking the commit:
- C1: per-cell boundaries in `PowerCellCertificate`;
- `--revision` must be passed by the runner;
- the T-028 report labels R-step fragments with uncertified cells "L0 over U" (expected for most residuals of C1-like words).
