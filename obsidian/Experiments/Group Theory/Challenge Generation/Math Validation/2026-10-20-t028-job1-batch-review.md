---
type: validation-verdict
date: 2026-10-20
completed: 2026-10-21
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 job 1: review of the batch before job 1 (hard caps, gate and early stop, C++ CL in the gate, recovery-attack fix, R-trace wiring, canonical R tie-break)"
verdict: "NOT READY for job 1: 3 blockers. (B1) the recovery attack declares a break when kbmag empties any one window's preimage t', without requiring phi'(t') = the segment or coverage of the word, so held-out T4u breaks can be false; (B2) a word killed in phase B gets a capped record without its t1/t3u verdicts, so a T3u survivor drops out of the T3u count; (B3) the soft chain cap equals the phase-A hard cap (3600 s), so a soft-capped chain is never gated. One gate question for Lead: S1-each's KB component counts a shortening by KB as resilient. CONFIRMED: the R-trace equivalence and identity on f4b7771 (27,328 words, 0 mismatches), the tie-break is deterministic, the one-byte closure store is a bijection, R3's kbcert certificate is unchanged, the early stop changes no verdict. The canonical tie-break is not verdict-neutral: on my substitution set R empties 39 words fewer and 5 more than at 63564c3."
---
# T-028 job 1 batch: review

Developer request, handed over at Lead's request (2026-10-20); replies via Lead. Triage: [[2026-10-20-t028-job1-batch-review-triage]]. Brief: `Developer/2026-10-20-t028-job1-review-handoff.md`.

**Code reviewed:**
- b25 `t028-pilot`: de13bee, 07866e3, 8753a23, plus 138fa4a (the pin of tcgraph f4b7771).
- tcgraph `feat/t028-pilot-cpp`: 5cd134f, f94150f, bc6b97f, f4b7771.

**Terms.**
- *Hard cap*: the per-phase wall-time limit after which the parent kills the word's process group (`caps.py`: phase A 3600 s, phase B 9000 s).
- *Soft chain cap*: the screen chain's own time budget (`pilot.CHAIN_CAP_S`), after which the chain stops with outcome "capped" and the residual should still be gated (§3 step 6).
- *A_R*: the R-aware recovery attack of pre-registration r9 §7.0d (see [[2026-10-20-t028-preregistration-r9-ar-review]]).
- *Changed output*: R's output word differs between tcgraph 63564c3 (the T-027 pin) and f4b7771.

## Blockers (fix before job 1)

**B1. The recovery attack accepts unproven breaks** (`recovery.py`, `attack()`; item 4).
- `success` is set as soon as kbmag reduces to IdWord the preimage t′ of **any single window** (≥ 15 tokens, with ±1-letter completions).
- `phi_t_equals_window` is computed and recorded, but not required. Coverage of the whole word by the windows is not required either.
- `heldout.t4u` then sets `broken=True, stopped_at="recovery"`. So a T3u residual can be counted as broken without a proof that it is trivial in B. That would remove survivors without proof, the one error a rare-event pilot cannot afford.
- **Fix:** success requires (i) kbmag reduces t′ to IdWord, and (ii) φ′(t′) equals the **whole cyclic word**, up to conjugation with a logged conjugator (r9 pins F1/F2), or the remainder Δ reduces by kbmag. A window-only hit is logged as a lead, never as a break.
- **Also missing** (should fix; these are r9 requirements):
  - no conjugation or cyclic wrap;
  - nondegeneracy is not implemented: `stallings_rank == 2` does not exclude ⟨x′, y′⟩ = F; there is no |t′| ≤ |w|/2 check and no "kbmag-dominated" label;
  - stage 2 is a token parse, not Stallings membership;
  - the fresh-sample indices 10–14 are not logged;
  - the 10 s kbmag cap is checked after the call; no timeout is passed to `kb.screen`;
  - the unit test checks only the flag.

**B2. A phase-B kill loses the gate verdict** (`pilot.capped_record`; item 1).
- The capped record carries only `verdicts={"capped_in": …}`, with no `t1` or `t3u`.
- `report.py` counts T3u from the verdicts, so a word that passed the T3u gate in phase A and was killed in phase B (held-out solvers) **disappears from the T3u count**.
- **Fix:** carry phase A's verdicts into the capped record; T4u = "capped (pending re-run)".

**B3. The soft chain cap equals the hard cap** (`pilot.CHAIN_CAP_S = 3600` = `caps.PHASE_A_CAP_S = 3600`; item 1).
- A chain that runs to its soft cap leaves no time for the gate, so the hard cap kills the word. §3 step 6 says a soft-capped chain is gated.
- **Fix:** CHAIN_CAP_S well below PHASE_A_CAP_S (e.g. half), or a separate hard cap for the gate.

## Lead's decision needed

**G1. KB in S1-each counts a shortening as resilient** (`gates.py`; item 2).
- `comps["KB"] = not any(kb_hits)`, with `kb_hits` from `screen(...)["empty"]` only. A KB result that is shorter but not IdWord therefore counts as resilient.
- The T-027 definition of S1-each is "strictly resilient": a solver that returns SHORTER is not resilient (the same point as issue 1 of [[2026-10-20-t027-registry-rev1-vet]]).
- This is pre-existing (since f4fff9c), not new in this batch. Lead decides which definition the pre-registration uses, and the report names it.

## Should fix

1. **Capped rows in N** (`report.py`): capped is counted only through `chain_outcome == "capped"`. A hard-capped row counts in N as a non-survivor. Hard-capped rows should be counted as capped and excluded from the denominator until re-run (the archive rule).
2. **t1 = True on every non-emptied residual**, including soft-capped chains. A capped chain is "T1 (capped)", not a plain T1.
3. **The 2^25 rung** is used at budget factor 2 without §5's ≤ 1.9 GB memory check.

## Minor

- A phase-A kill is labelled "gated".
- A race: the child may append to the archive before the parent's kill, giving a double record. `Archive.read` crashes on a partial last line; it should skip it, as the StageLog does.
- `dr_ladder` reports "censored" when the shared cap runs out; it should say "capped".
- T4u's label for A_R: see the addendum (A_R is now staged).
- `replay_block` skips KB "unchanged" steps. That is harmless, but the replay count should say so.
- `test_cl_cpp.py`'s "stops at first break" test does not pass the stop flag; it tests the ordering only.

## Confirmed

**Item 1, hard caps.**
- The kill targets the process group.
- The StageLog fsyncs and drops a partial line.
- A killed word's residual is the word at the last stage start, and no unfinished step is logged as done.

**Item 2, gate and early stop.**
- S1-each is `all(v is True)`, so a None (not run) never passes.
- T3u = L1-r25 + S1-each. L1's "undecided" never passes. S2-chain runs only after S1-each.
- The early stop changes no verdict: later stages are "not run", never "resilient".
- `identity_known` is valid.
- Reuse in (b) takes only finished non-breaks.
- The verification order is c, a, b.

**Item 3, C++ CL in the gate** (code read; tcgraph tests).
- `packWord` maps −2, −1, 1, 2 to 0..3, a bijection. States are compared packed, and the hash is that of the unpacked word, so lookup is unchanged.
- `closure_run` walks the JSON in sorted key order. The Python side zero-pads the names (`w%05d`), so the order agrees. `closure_breaks_many_cpp` checks the name prefix and raises on a count mismatch.
- `breaks` means a path was found. `cap_hit` and `exhausted` both count as not broken, as in the Python reference.
- On f4b7771 the C++ kbcert reproduces R3's registry certificate cell for cell (2,364 cells, L0 over R7 true).
- **Not done:** a verdict comparison of `closure_run` against the Python closure on a word set.

**Item 5, R-trace wiring** (code read).
- `verify.r_step_check` checks the exact free-group identity cells·H·out·H⁻¹ = cyclic(in), that each core is literally u⁵, and runs kbmag on the cores (reported).
- `loops_check` accepts an R step from another platform by its trace, and `replay_block` skips it. That is the platform rule as stated. It is sound because the trace is itself a proof of conjugacy in B.
- **Not done:** an independent replay of `r_step_check` on a traced chain.

**Item 6, canonical tie-break** (run on f4b7771 under capjob 2 GB / 2 CPUs).
- The code is deterministic. Square bases are sorted short-lex, and the first base with a strictly greater score wins. `findMaximalPowers` is a linear scan.
- The tcgraph tests pass: 53/53.
- **Equivalence and identity:**
  - traced and untraced outputs are equal on all 27,328 words (6 sets);
  - the identity cells·H·out·H⁻¹ = cyclic(in) holds on every word;
  - every core is u⁵ with u not a proper power.
- **Speed:** traced ≈ untraced, within 1 %. I did not re-time against the pin; the Developer measured +2 %.
- **Note:** the score p·L − (5−p)·L is computed in doubles. Exact integer arithmetic (2·run letters − 5L) would remove any risk from compiler-dependent floating-point contraction. The Mac and VM hashes agree, so this is optional.

## The tie-break changes R's verdicts

Changed outputs, 63564c3 → f4b7771, on my private word sets (no words in this note):

| set | words | changed | shorter / longer | emptied by the pin only / by f4b7771 only |
|---|---|---|---|---|
| T-024 originals (12) | 12 | 2 | 0 / 0 | 0 / 0 |
| T-027 chain words | 35 | 6 | 0 / 0 | 0 / 0 |
| pool (50–80 letters) | 351 | 0 | — | 0 / 0 |
| planted | 19,998 | 393 | 4 / 6 | 0 / 0 |
| random | 5,000 | 718 | 8 / 52 | 0 / 0 |
| substitution | 1,932 | 274 | 13 / 101 | **39 / 5** |

- The tie-break is not verdict-neutral. On the substitution set, R at f4b7771 empties **34 fewer** words (856 vs 890) and leaves longer outputs more often than shorter ones.
- Both versions are valid conjugacy reducers, so nothing is unsound. But R is a screen solver: a weaker R yields more T1 residuals. T-027 results (pin 63564c3) and T-028 results (f4b7771) are therefore not directly comparable for R.
- **One of the two changed T-024 words is the approved original ds519 L3.** Its R output changes at the same length. The registry's reproduction chain is pinned to 63564c3 and stays valid there, but it **does not replay under f4b7771**. Replays must use the registry's pin, or the chain must be regenerated as a new revision.
- **For Lead:** the pre-registration should name f4b7771 as R's version, and the report should note the change against T-027.

## Scope

- **Verified by run:** item 6 (equivalence, identity and changed outputs) and R3's kbcert certificate on f4b7771.
- **Verified by reading the code:** items 1–5. For items 1, 2 and 4, a fork sub-review found the issues; I re-read the code for every blocker and for G1.
- **Not done:** a closure_run vs Python verdict comparison; an independent replay of `r_step_check`; timing against the pin.

## Verdict

**NOT READY for job 1.**
- Fix B1–B3.
- Lead decides G1.
- After the fixes, I re-check B1–B3 only.

## Addendum 2026-10-21: section 7, A_R (r10, staged in b25 `t028-pilot`)

The Developer added section 7 to the handoff after my verdict. My verdict's "A_R is not built" is superseded by this section. Scope: a code read of `ar.py`, `ar_control.py`, `ar_tune.py`, `tests/test_ar.py` and the staged diffs of `heldout.py`, `seeds.py` and `construct.py`, against r10 §7.0d. No runs. The C++ `approx/` kernels only propose candidates and were not reviewed.

**Confirmed (code read).**
- **Acceptance is exactly (i) + (ii)** (`ar.verify`).
  - (i): kbmag reduces some rotation of t′ (x → a, y → b) to IdWord. A rotation is a conjugate, so this proves t′ = 1 in G₇, hence φ′(t′) ∈ F⁵.
  - (ii-exact): a literal free equality g⁻¹φ′(t′)g = w·∏cells.
  - (ii-Δ): kbmag on the linear word Δ = w·(g⁻¹φ′(t′)g)⁻¹.
  - "Membership found, kbmag failed" is its own outcome, never a break.
  - `kb.run_wordreduce` raises on a result-count mismatch, so a crash cannot produce a false "IdWord".
- **The frames compose.**
  - A_R1: g = g₁·u₀⁻¹ gives g⁻¹hg = u₀cu₀⁻¹ = w.
  - A_R3: each move is v_i = κ_i v_{i−1} with κ_i = a_i r_i⁻¹ a_i⁻¹ and r_i = Q_i⁵. The logged cells (core r_i⁻¹, conj a_i⁻¹·c·u₀⁻¹), taken in reversed order, telescope to w·∏cells = u₀ v_k u₀⁻¹, which is the A_R1 image of v_k.
  - A_R4: g = c[:o]⁻¹·u₀⁻¹ matches the rotation the parse reads.
  - In any case, a frame error can only turn (ii-exact) into a (ii-Δ) attempt or a failure. It cannot produce a false break.
- **Nondegeneracy matches r10 and P3.**
  - The Euler rank of the folded flower graph is 2 exactly when x′, y′ is a free basis.
  - "Not the one-vertex bouquet" is exactly ⟨x′, y′⟩ ≠ F: a rank-2 subgroup of F₂ of finite index n has rank n + 1, so it is either F itself or of infinite index, and its core graph is the bouquet only when it is F.
  - The bounds |x′|, |y′| ≥ 2, |t′| ≤ |w|/2 and |Δ| ≤ |w|/4 (after free reduction) are as written.
- **Blind mode** reads only w and the kbmag systems. `run_control` passes the true pair in blind mode too, but `attack` reads it only when `mode == "oracle"`, so this is harmless.
- **The reuse rule at the double budget** is sound. A_R is reused only when it ended by exhaustion, and the kbmag caps of 10 s and 60 s are part of r10's definition of acceptance, not of the budget.
- **The control summary** applies the rule per stratum, counts breaks as r10 says, and excludes the tuned-on word and the residuals equal to W.

**The blockers stand.**
- **B1:** `heldout.t4u` still runs `recovery.attack` before A_R, and still declares a break on its window-only acceptance. `ar.verify` now exists; route §4's candidates through it.
- **B2 and B3:** `pilot.py` and `caps.py` are not in the staged set, so both are unchanged.

**Should fix, or record as a deviation from the frozen r10.**
1. **A_R1 re-parses instead of reading t′ off the closed path.**
   - r10 says t′ is read off the path. The code conjugates into H and then runs `recovery.parse`, and returns None when that greedy parse fails.
   - For a Nielsen-reduced pair the junction rule need not hold, so true members are dropped.
   - This affects sensitivity, not soundness, and may explain part of oracle mode's weak tune-set result.
2. **A_R3's move set differs from r10 §3.**
   - The code allows any primitive period ≤ 120 with exponent in [1.2, 2.5], anywhere in the word.
   - r10 specifies cells at the seams, from primitive u with |u| ≤ 7 and from products of ≤ 3 blocks.
   - This is sound by construction, but it is a change to a frozen text.
3. **A_R4 filters |t′| ≤ |w|/2 before verifying.** A candidate that would be a kbmag-dominated break is never tried, although r10 counts such a success as a break. This is conservative, but it is a change.
4. **`verify` does not check that each cell core is literally u^{±5}.** It is true by construction in `undo_move`, but acceptance is the proof step, and `r_step_check` applies the same literal test to R cells. One line.

**Minor.**
- The tests build pilot-label words (`construct.build("C1", 8, 1, …)`, and `depth_items` defaults to `tune=False`). They should use tune-set words.
- The `ar_tune` clash check:
  - omits the CTRL cells, although its docstring includes them;
  - checks indices 0–29 instead of the first 30 non-degenerate indices;
  - uses `canon`, which is not rotation-canonical above 4,000 letters.
- **The depth-series label** (Developer's point 4; checked by run on f4b7771, capjob 2 GB / 2 CPUs).
  - "R stopped after k rewrites" is computed as the cyclic reduction of (cells[:k])⁻¹·c. That word is a valid, trivial control item whatever the cell order.
  - **Does the trace list cells in application order?** I took 1,139 words with ≥ 2 cells (up to 400 from each of the planted, random and substitution sets, plus the T-027 chain words) and tracked the length of the prefix word as k grows.
  - **Forward order:** the prefix length grows at some step on 47 words (4 %): 16/390 planted, 1/370 random, 27/361 substitution, 3/18 chain. At k = n the length always equals R's result.
  - **Reversed order:** it grows on 1,069 of the 1,139 words (94 %).
  - **So the cells are in application order.** But in about 4 % of words, a prefix word is longer than the one before it, so it is not literally one of R's intermediate states. The likely cause is a length-neutral or batched rewrite in R; I did not look into it.
  - Fine for a control; label the series "R prefix depth k" and say so in the report.
- **For Lead:** if the second calibration survivor's residual was used while developing A_R, it belongs in `TUNED_ON` too.
- **T4u labels:** "not broken" requires A_R to have run. A word capped before A_R reads "A_R pending", not T4u.

**The Developer's four points (request of 2026-10-21):**
1. Acceptance is sound. A wrong pair or a wrong insertion cannot produce a break, because acceptance is literal (i) + (ii).
2. `undo_move` and the cell frames are correct, as computed above.
3. The budget_limited reuse is sound.
4. The R-depth series is valid, with the labelling caveat above. The exclusions are applied as r10 says.

**Addendum verdict.** A_R's acceptance is **sound**, with the cores-literal check as a one-line pin. The four deviations from the frozen text need either a fix or a recorded deviation, which is Lead's decision. **Job 1 is still NOT READY, because of B1–B3.**

## Re-check of the fixes (2026-10-21)

b25 df02191 (Lead's commit of the Developer's fixes; tcgraph pin 3673013). Method: a code read of the diff 138fa4a..df02191, plus one scratch run.

**Blockers: all fixed.**
- **B1.** `heldout.t4u` and `pilot` now call `ar.section4_attack`.
  - `recovery.attack` returns leads only. Each lead goes through `ar.verify` against the whole word: g⁻¹ = u₀·(the prefix before the window), and the rest of the word is the Δ that kbmag must reduce.
  - `broken` is set only on a verified break. A window-only hit stays a lead, and is reported as such (`recovery_on_W` is now the lead; `recovery_break_on_W` is the proof).
  - The kbmag cap is now a real timeout in `kb.screen`. A timed-out system gives no result, never IdWord.
- **B2.** `capped_record` keeps phase A's verdicts: t1 and T1 (capped) from the chain's done event, t3u from the gate's done event, and t4u = "capped (pending re-run)". `report.tally` counts hard-capped rows outside N, with `hard_capped_t3u`.
- **B3.** `CHAIN_CAP_S` = `PHASE_A_CAP_S`/2 = 1,800 s.
  - Note: the gate on long residuals can itself take long (the Developer measured 984 s for CL alone on 16 m = 24 images). A word can still hit the hard cap during the gate. That is now recorded correctly as capped and re-run, so it is not an issue.
- **G1 (Lead: strict).** KB in S1-each now fails on IdWord **or** a shorter output on any image, with `kb_image_shorter` logged. This is T-027's definition.

**Deviations from r10, and the pin: all fixed.**
1. **A_R1 reads t′ off the closed path** with `PairDecoder`: a spanning tree, the two Schreier generators, and their expression in p, q found by a Nielsen search.
   - `decode` self-checks φ′(t′) = h, so a decoding error can only lose a candidate, never produce a false one.
   - **My run:** on 292 random free bases (|p|, |q| from 2 to 19), the Nielsen expression was found for all 292, and decode(φ(t)) returned t itself for 1,460/1,460 random t.
2. **A_R3 moves** now start at seam positions (within 3 letters of an uncovered letter). The period Q is primitive and either |Q| ≤ 7 or a rotation of a cyclically reduced product of ≤ 3 blocks. This matches r10 §3.
3. **A_R4** no longer filters on |t′|. A long t′ becomes a kbmag-dominated break through `verify`.
- **The cores pin:** `verify` now rejects a cell whose core is not literally u^{±5}.

**Also checked:**
- `dr_ladder` now reports "capped" separately from "censored".
- The `ru_maxrss` unit is right: kilobytes on Linux, bytes on macOS.

**Should fix (not blocking job 1's screen):** `heldout.rung25_allowed` projects the 2^25 peak as twice the peak of the **last rung run** at the 1× budget.
- If the 1× ladder hit its shared 900 s cap before 2^24, the last rung is lower, say 2^22. The projection then needs 2^(25 − log₂ bound) × peak, not 2×.
- As written, it can allow 2^25 when the projected peak is above 1.9 GB.
- **Fix:** allow it only if the last rung is 2^24 and finished, or scale by the bound ratio.
- It matters only in verification (b), after job 1's screen.

**Minor:** `report.main`'s totals leave out `hard_capped_t3u`, although it is counted per cell. Add it, so that a T3u survivor killed in phase B is visible in the headline totals.

**Re-check verdict: CONFIRMED.** B1–B3 and G1 are fixed, the three deviations are fixed, and so is the cores pin. From the mathematics side, **job 1 is READY**. The `rung25_allowed` fix is needed before verification (b).
