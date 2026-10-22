---
type: code-review
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-027: code review of the solvers harness (b25 worktree b25-t027, branch t027-candidates-solvers, untracked: experiments/challenge_gen/solvers/ 13 files, kb_reduce_words.py, b0_challenge_triviality.g)"
verdict: "SOUND for what it was used for: every stage's 'broken' and 'invalid' is a valid proof in the stated group, the kbcert certificates are L0-checked before they are attached, the reproduction blocks are complete, there are no machine paths in the registry, and the 9 tests pass. Registry revision 1 is unaffected (I verified its contents independently). TWO LOGIC BUGS must be fixed before T-028 builds on it, both demonstrated: (A) r25_min16 runs on R's output, not on the original word, so rho_min16 (the L1-r25 measure) is inflated whenever R shortens (shown: 1.0 reported, 0.875 true); (B) the S1-each level counts 'resilient' stages that SHORTENED the word, so S1-each can be granted wrongly (shown). Root cause: the verdict set has no SHORTER. Five smaller issues."
re_review: "2026-10-20, b25-t027fix (harness sha256 588c8334…aac31): CONFIRMED. A, B, SHORTER and items 1-5 fixed; 21/21 tests pass; the A and B tests fail on 6b813d9; the rebuild diff is exactly as claimed (17 differences). Small, before or with the commit: a test for d_r_iter SHORTER (mutation uncaught), the cwd=REPO comment (it does not defeat the venv hook; add a runner guard), the conjugator convention in the core.py docstring."
---
# T-027 solvers harness: code review

This is a Lead request (2026-10-20). The code is in `~/Research/challenge-gen/b25-t027`, branch `t027-candidates-solvers` on d1b5d0f, all files untracked:
- `experiments/challenge_gen/solvers/`: 13 source files plus tests;
- `kb_reduce_words.py`;
- `b0_challenge_triviality.g`.

`build_candidates.py` has sha256 `63118b08…`, as stated. The two support scripts are **byte-identical** to the 2026-10-07 originals (kb-verify and challenges-nonempty-verify).

**Method.**
- I read all of it (about 1,100 lines).
- I ran the test suite under capjob (2 GB / 2 CPUs), with tcgraph_ext from my clean d1b5d0f build, GAP + anupq, kbmag, and the kb-verify systems: **9 passed**, none skipped.
- Note: the t018 venv's editable-install hook shadows the worktree's `experiments` package in the harness's child processes. The tests pass with a hook-free Python 3.12 and PYTHONPATH. That is an environment issue, not a code issue, but the Developer's run instructions should say so.
- I wrote two demonstration scripts for the bugs (my `t027/` scratch).

## Soundness of each stage

| stage | verdict meaning | review |
|---|---|---|
| `reduce` | broken iff the cyclic reduction is empty | sound (free group) |
| `abelian` | invalid iff the exponent sums are not both ≡ 0 mod 5; pass proves nothing | sound |
| `b0_gap` | invalid iff the word is non-trivial in B₀(2,5) (a quotient of B), so then it is non-trivial in B; pass proves nothing | sound. **But** see issue 3 |
| `r25` | broken iff R reaches the empty word | sound. R is conjugacy-preserving, so emptiness proves triviality |
| `r25_min16` | broken iff some image empties; ρ_min16 | sound as a proof. **The measure is wrong after a shortening (bug A)** |
| `kbmag_rec` / `kbmag_slx` | broken iff IdWord, which is an equality in G_7 (every kbprog rule follows from b25_full); NONE proves nothing | sound. The certificate is attached only with `l0: true`, checked by `expand(core table) == word`, independently of kbcert's path |
| `closure_bfs` | broken iff the 2.5-closure (periods ≤ 7) reaches the empty word or a conjugate of an R7 relator | sound in G_7. A cap hit and an exhausted search both read "resilient"; record which (issue 5) |
| `d_r_iter` | broken iff the empty word is reached or D returns TRUE; D's FALSE is recorded and **not** read as invalid (non-trivial in G_k only) | sound. A D shortening is an equality in G_k, k = the throw stage (`throw_stage` re-runs D at rml 1..k, my method); R steps are conjugacies |

- **Pipeline (`check.run_word`):** an error is never read as resilience, and the run stops at the first proof unless `--all`. Correct.
- **Builder:** the originals' certificates are replayed (raises if not L0); a residual's certificate is attached only if `l0` is true; `candidates` is always []. Correct.
- **Reproduction blocks:** every D and R step is recorded in order, with in/out words, parameters and the throw stage; the builder adds the leading R step (original → R(original)). Complete for the registry.
- **Budgets:** every stage record carries its budget, time and peak RSS.
- **No machine paths in the registry:** tools come from environment variable names; the registry keeps only selected detail fields. (The *reports* can contain paths in error tracebacks; see issue 4.)
- **Headers:** present on every source file.

## Bugs (fix before T-028 uses the harness)

**A. `r25_min16` runs on R's output, not on the original word.**
- The stages run in cost order: r25 (20), then r25_min16 (25).
- When r25 shortens the word, it sets `next_word`, so r25_min16 computes ρ over the images of **R(w)** and divides by **|R(w)|**.
- The L1-r25 measure is ρ_min16 of the original word.
- **Demonstrated:** a 16-letter word with R(w) of 14 letters; the harness reports ρ = **1.0**, the true ρ_min16 is **0.875**.
- For T-028 (R rewrites almost every W, per my probe), this would inflate L1-r25 across the board.
- The registry is not affected: R did not shorten any of the 7 words. ds519's R was length-neutral, so its ρ was computed on the rewritten word; it reads 1.0 either way.
- **Fix:** r25_min16 always takes the original word; or give it cost < 20.

**B. S1-each counts shortenings as resilience.**
- `levels()` grants S1-each if R, CL, KB (rec, slx) and `d_r_iter` all have harness verdict "resilient".
- But r25 and d_r_iter return "resilient" **with `next_word`** when they shorten without deciding.
- S1-each requires NONE.
- **Demonstrated:** a certified word that R shortened (40 → 10) and D↔R shortened (to 5) gets `{"L": "L1-r25", "S": "S1-each"}`.
- Also, S1-each's D is **D1 = one call of D(20M, rml 5)**, while `levels()` uses `d_r_iter` (the D↔R chain). r6 records the D1 deviation, but the builder should use a D1 stage, or say which it used.
- The registry is not affected: S is "none" because KB breaks every word.
- **Root cause and fix:** the verdict set {broken, resilient, invalid, error} has no **SHORTER**. Add a `shorter` verdict (with in/out lengths and the conjugator for cyclic solvers). Then `levels()` and T-028's S1-each read it directly, and the builder's `label()` patch becomes unnecessary.

## Smaller issues

1. **The reproduction block starts at the d_r_iter input, not at W.** The builder stitches in the r25 step for the registry. For T-028, the harness itself should emit one block from the original word through every stage that changed it (r25, kbmag outputs, D, R), as r5 requires ("from W to w").
2. **kbmag outputs in kbmag syntax.** `reduced_to` is the kbmag word (`a*b^2…`), and a shorter non-identity output is not passed on. T-028's in-loop KB steps need it converted to aAbB and used as `next_word`. That is an equality in G_7, so the conjugator is 1.
3. **`b0_gap` does not check its own controls.** It records `order_is_5_34` and the class, but returns a verdict even if they are wrong. It ignores `GENERATED_BY_IMAGES`, `EXPONENT5_ON_PCGS` and the 5 CONTROL lines. **Fix:** verdict = error unless the order is 5³⁴, the class is 12 and all controls are as expected. This matters more now that B0 runs on every residual as a harness-bug stop.
4. **Provenance and paths in reports.**
   - `code_versions()` reports `b25_dirty: false` because it ignores untracked files, while the harness itself was untracked. Add the harness hash (as the builder does) or count untracked files.
   - Error details (`trace`, `log_tail`) can contain absolute paths. The registry does not copy them, but scrub them if reports are ever committed.
   - The builder hard-codes `"b25": "d1b5d0f"` and `revision: 1`. Take them from the reports and an argument.
5. **Small robustness points.**
   - `closure_bfs`: record "cap hit" versus "space exhausted".
   - `throw_stage` returns None silently if D does not re-throw the same word: treat that as a non-reproducibility error (a T-028 stop).
   - `relators.setdefault(k, core_table[k-1])` in the builder: assert equality when k already exists. I checked all 65 entries; they are equal.
   - `idx.table[:1630]`: assert the size rather than truncate.
   - `mem_gb` uses RLIMIT_AS (virtual memory), which can kill D before its RSS reaches the cap. Prefer capjob for memory.

## Tests

- **What they cover:** the cheap stages; a⁵ broken; a D↔R control; the step chain linked; the isolated runner (crash, kill, timeout, resources); the stop-at-first-proof pipeline; error ≠ resilient; no paths in a report; the builder (L0 raise, `candidates` empty, labels, levels); B0 (a⁵ / aaaab); kbmag with an L0 certificate.
- **What is missing:** a test that would have caught A (ρ_min16 on a word R shortens) and B (levels with a shortening stage); `throw_stage`; a kbcert certificate whose L0 fails being rejected; B0's control checks.
- **A small error:** the comment in `test_d_r_steps_are_recorded_in_order` says "length 10", but the word has 12 letters.

## Verdict

- **CONFIRMED for registry revision 1:** its contents were verified independently, and neither bug touches its 7 records.
- **Not yet ready as the base for T-028:**
  - fix A and B, ideally with a `shorter` verdict;
  - fix issues 1–3;
  - add the missing tests.

  Issues 4–5 are cleanups. Lead can commit the harness as it is, with this note, since it produced the registry, provided the A/B fixes come before any T-028 run.

## Re-review after the Developer's fixes (2026-10-20)

**Code.** b25 worktree `b25-t027fix`, detached at 6b813d9: 15 modified files plus the new `solvers/provenance.py`. The harness sha256 is `588c8334…aac31` over 14 files, as stated; I recomputed it with `provenance.harness_hash()`. The Developer's report is `Developer/2026-10-20-t027-solvers-fix-report.md`.

**Method.**
- I read the whole diff.
- I ran the suite under capjob (2 GB / 2 CPUs) with a hook-free Python 3.12, tcgraph_ext, GAP + anupq, kbmag and the kb-verify systems: **21 passed**, none skipped.
- I ran the new tests against a copy of 6b813d9 (git archive plus the new test files).
- I mutated a copy of the fixed tree, putting back one old behaviour at a time, to see which test catches each.
- I re-ran my bug demonstrations on the fixed code.
- I diffed the Developer's rebuilt registry against the committed revision 1.

### The two bugs

| item | result |
|---|---|
| **A** (ρ_min16 on R's output) | **fixed.** `r25_min16` is registered `original=True`, and `run_word` hands it the original word. My demonstration word now gives r25 `shorter` (16 → 14) and r25_min16 `input_len` 16, ρ = **0.875** (it was 1.0). Mutation M1 (`original=True` removed) is caught by `test_rho_min16_always_sees_the_original_word`. |
| **B** (S1-each from shortened stages) | **fixed.** `levels()` needs the verdict to be exactly "resilient" from r25, closure_bfs, kbmag_rec, kbmag_slx and the new **`d1`** stage. `d_r_iter` no longer counts. My demonstration word now gets `S: none`; it got `S1-each` before. Mutation M3 (r25 shortening read as resilient) is caught by 2 tests. |

### The SHORTER verdict

- **Semantics are correct.** "Shorter" means not decided, but the stage found a strictly shorter word, equal to the input in the stated group. A word that was only shortened has final verdict `shorter` and is never read as resilient. Mutation M4, which drops `shorter` from the final verdict, is caught.
- **Conjugator, in = c·out·c⁻¹:**
  - **reduce:** c = the cancelled prefix u, an equality in the free group. Checked: `baB` → `a` with c = `b`.
  - **KB and D1:** c = "", an equality of the linear words, in G_7 and in G_k (k = the throw stage).
  - **R and d_r_iter:** c = None. R's conjugator is not exposed at the tcgraph pin; `greedy_reduce_cyclic_exhaustive2_5` returns only the word. This is acceptable: the R steps are recorded with their in/out words and labelled as conjugacies.
- **d1 = one call of D(20M, rml 5)**, as S1-each requires.
  - A throw gives `shorter` with its stage.
  - A throw of the empty word gives `broken`.
  - D's "nontrivial" is kept in the detail and is not a verdict.
  - d1 is a probe: it passes no next_word and adds no step.
- **A D throw that does not reproduce is now an error**, in both d1 and `d_r_iterate`. This was issue 5.
- **Doc inconsistency (one line):** the `core.py` module docstring says "word = c⁻¹ out c". The README, `shorter_info` and the test all use in = c·out·c⁻¹, which is the convention the code implements.

### Items 1–5

1. **Reproduction block from W: fixed.**
   - `run_word` collects the steps of every stage except `original=True` stages, in cost order. The block starts at the original word, and the R step always comes first.
   - Checked on my word: the steps are R, D, and they are linked step to step.
   - The builder now takes the harness block. Its old stitching is kept only for old reports.
2. **kbmag output: fixed.**
   - A shorter normal form is converted to aAbB and passed on as next_word, as a KB step with c = "".
   - The Developer also found and fixed a real bug in `kb_reduce_words.reduce_words`: it kept only the first line of wordreduce's wrapped output.
   - **Check:** random words of length 40 to 300 through slx. Every shorter output was idempotent, and w·nf⁻¹ reduced to IdWord, so no letters are lost. rec's normal forms are longer than the input, so they are correctly not passed on.
   - Revision 1 is unaffected, because all its kbmag verdicts are IdWord.
   - `kb_reduce_words.py` is no longer byte-identical to the 2026-10-07 original. That is fine; the kb-verify provenance still names the old file.
3. **B0 controls: fixed.**
   - `check_script_output` makes the stage an error unless the size is 5³⁴, the class is 12, the group is generated by the images, exponent 5 holds on the pcgs, and all 5 controls hold.
   - Tested on mutated outputs. The real GAP test (a⁵ / aaaab) passes through the check.
4. **Provenance and paths: fixed.**
   - `b25_dirty` now counts untracked files.
   - The harness hash is always given.
   - Errors (`reason`, `trace`, `log_tail`) are scrubbed of absolute paths.
   - The builder takes b25 from the reports or `--b25`, and the revision from `--revision`.
5. **Robustness: fixed.**
   - closure_bfs records `cap_hit` / `exhausted` / `states`.
   - A D throw that does not reproduce is an error.
   - Relator equality is asserted.
   - The R7 size is asserted (1,630).
   - `mem_gb` is now a limit on resident memory polled from /proc, and it is tested.

### The venv note: the README is right, the code comment is not

- `core.run_isolated` now starts the child with `cwd=REPO`, with the comment "the checkout's package, not an editable hook's". **That does not defeat the hook.**
- With the t018 venv Python and cwd = `b25-t027fix`, `import experiments` still resolves to the **t018** tree. It does the same with PYTHONPATH set to the fix tree. The hook is a meta-path finder, so it is consulted before sys.path, which includes the cwd.
- The README's note ("can shadow it: check with …") is correct.
- **Suggested fix:** in `runner.py`, error out unless `experiments.__file__` lies under REPO. That turns the silent run of old code into a visible error. Otherwise, drop the claim from the comment.

### Tests

- **Counts:** 21 pass on the fix: 9 old and 12 new.
- **On 6b813d9:** 13 fail and 8 pass. The A and B tests do fail there, as claimed.
  - The A test fails on `core.SHORTER`, which is missing, before it reaches the ρ assertion. Mutation M1 shows the ρ assertion itself catches A.
  - The B test fails on the `d1` name. Its own claim (S1-each needs "resilient", so "shorter" counts as not NONE) does hold.
- **Gap: mutation M2 is not caught.** M2 makes `d_r_iter` read a shortening without a decision as "resilient". That is exactly revision 1's mislabel, and **all 21 tests still pass**.
  - Add one line, e.g. `stage("d_r_iter", "aaaaab")["verdict"] == core.SHORTER`. On the fix it returns `shorter` (status undecided, final word `b`).
- **Weak test:** `test_closure_reports_cap_hit_versus_exhausted` only asserts its cap-hit half under an `if`, so it can pass while asserting nothing. Assert `cap_hit is True` for cap = 1 on a word whose closure is not trivial at once.

### The rebuild diff claim: confirmed

- **File compared:** the Developer's rebuilt file (`rev1_fixed.json`, sha256 `75163360…`), against the committed `754f582c…`.
- **Method:** a structured diff that ignores only `seconds` and `peak_rss_mb`. It found **exactly 17 differences**, all as stated:
  - code.b25, builder_sha256, harness, harness_files and harness_sha256;
  - the third report hash;
  - `d1` added to all 7 records: "shorter" on the 4 originals, "resilient" on R1–R3;
  - `d_r_iter.harness_verdict` resilient → shorter on the 4 originals.
- **No other differences:** none in the levels (L1-r25, S none), ρ (1.0), the certificates, the kbmag, B0, closure and R verdicts, or the reproduction blocks.
- **Cosmetic:** the registry's `d1` record keeps no throw stage or shortened length (`KEEP` has no `d1` entry). Add `stage` and `shorter_len` if d1 is shown in a later revision.

### One pin for T-028 (not a defect)

After a **length-neutral** R rewrite (ds519), the S1-each probes kbmag, closure_bfs and d1 see R(W), not W. The report records this (`input_word`). T3u defines R, CL and KB on the 16 images of W, so the T-028 screen layer should hand those probes W, or state the deviation.

### Result

**CONFIRMED.**
- A, B, the SHORTER verdict and items 1–5 are fixed and correct.
- The tests pass, and the A and B tests fail on 6b813d9.
- The rebuild diff is exactly as claimed.

**Before or with the commit (small):**
- (i) add the `d_r_iter` SHORTER test, since mutation M2 is uncaught;
- (ii) fix the `cwd=REPO` comment, or better, add the runner guard;
- (iii) fix the one-line conjugator convention in the `core.py` docstring.

**Optional:**
- tighten the closure cap test;
- keep `d1`'s stage and length in the registry;
- the T-028 pin on length-neutral rewrites.
