---
type: validation
date: 2026-10-22
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 escalation driver, b25 01312f0"
status: verdict sent to Lead
---
# T-028 escalation driver: code review

**Verdict: NOT READY for the 55-word B; 4 required fixes. B0 (cost calibration) is fine to run as it is**, because B0 reads only seconds and sizes, and the defects below change status labels, not costs. Scope: code and tests read, one synthetic probe; no data opened.

Terms. **Rung**: one solver at one budget on one word. **Binding rung**: a rung whose raised limit was actually reached, so a larger limit could change the result. **Survived**: the status that triggers stage C.

## Matches the check
- **P1/P2 sample.** `select_sample` uses ranks round(q(n-1)), Python half-to-even, ties by (length, index); a cell with fewer than 5 survivors gives all. The manifest holds ids and a canonical hash, no words. `run` re-derives the manifest from the archive and stops on a mismatch; a staged subset must equal the registered sample.
- **P4.** `tuned_on` is carried in the picks.
- **F1.** Four outcomes plus `error`; timeout and oom exact via `core.run_isolated` reasons; `heldout.dr_ladder` keeps the reason (job-1 records unchanged; `mem_gb=None` is the old default). Per-rung caps are registered (D 900 s, kb 3600 s).
- **F3.** Ladder starts at 2^25; the code states job 1 and its 2x verification stopped at 2^24. Not checked against data.
- **F4.** First breaker in registered order, with seconds, CPU-s and peak size; cost-ordered rungs. (D's `cpu_s` is wall time of one thread: rename or note.)
- **Stop-at-first-break, resume, retry** work as designed (tests).

## Required fixes
- **R1. `not_run` counts as survived.** `run_d` returns `not_run` when the projected size exceeds the memory limit, but `not_run` is in neither `OUTCOMES` nor `UNDETERMINED`, and `word_summary` has no binding flag for it, so the default `True` applies. **Probe:** a word with five exhausted rungs and `not_run` at 2^28 gets status `survived`. At `--mem-gb 38` the 2^28 rung runs (about 25 GB), so B0 is not affected, but any smaller limit silently produces survivors. Fix: `not_run` is undetermined; add a test.
- **R2. F2 (kbmag binding) is not implemented.** The summary sets `binding` for D rungs only, and the default `True` covers kb rungs; the probe shows `survived` with an unchecked kb rung. The stage records `best_len`, but nothing uses it. What is needed is cheap and system-level: at registration, assert for the 4x and 16x system manifests that `maxeqns` recorded = 4 and 16 times 100,000, that `kbprog_exit` is the equation-limit halt (exit 2, as for 1x, so the limit was reached), and that the rule counts strictly increase 1x < 4x < 16x. A system that did not hit its limit, or has the same rules as the one before, makes that kb rung non-binding. Put the result in the manifest and make `survived` require it.
- **R3. Registered systems are not enforced at run time.** The manifest stores the sha256 of the 4x and 16x files, but `run_kb` takes the directories from the environment and never compares them. Check the system `manifest.json` and file hashes against the registered ones before the first rung, and stop on a mismatch. The job script writes `inputs.sha256` after the fact, which records but does not enforce.
- **R4. Disposition of `partial` and the D baseline.** A non-binding exhausted D rung (RSS below 1.5 times the previous one) gives `partial`, which is neither survived nor broke, but the decision rule has no row for it. Define it: the D table was not full, so raising the bound is moot; the word stays "partial: D completed under the round limit", reported separately, and it blocks the negative reading as undetermined does. Prefer the solver's own status (table overflow) over the RSS ratio where available. Also assert `bound24 == 2^24` for the baseline (`rss24` is taken from the last job-1 rung, whatever its bound).

## Should fix
- **S1. Register the decision rule.** The manifest has `survives_only_if` but not the stage-C trigger, the partial/undetermined rows, or the top-rung replay of D3. Add the rule text (or the hash of Lead's note section) to `registered()`. `ORDER` is registered: if B0 changes it, re-hash before B and say so.
- **S2.** Pass `mem_mb` to `core.run_isolated` for kb rungs (it only reaches the label function now); the 4x/16x systems are small, so this is a guard.
- **S3.** Record `final_len` of exhausted D rungs against the input length in the summary, since SHORTER counts as exhausted and a progressing word is worth a flag.
- **S4. Monotonicity of D in the bound** (F3) is assumed from `coset_bound` being a cap in `attempt_to_decide_if_trivial`; I did not test it. The ladder does not depend on it for correctness, only for skipping rungs, and it skips none.

## Data handling (Lead's decision)
`stage` copies the full archive records of the 55 sampled survivors, words included, to a staged folder for the rjob host. The outputs hold ids, outcomes, seconds and sizes only. Sending private survivor words to cpuserver is Lead's/owner's call (job 1 already ran on a remote host); I flag it, not block it.

## To clear before B
R1-R4 fixed, tests for R1, R2 and R3 added, re-registered manifest hash recorded, then my re-check.

## Re-check of R1-R4 and S1-S4 (2026-10-22, uncommitted tree on c2a9699)

Developer request, routed by Lead. Method: diff read against c2a9699, 23 tests run under capjob (all pass), two synthetic probes. No data, archive or B0 outputs opened.

**Verdict: R1-R4 and S1-S4 are fixed as asked, with ONE new required fix (N1) and two small pins. B stays blocked until N1 is fixed; B0 is unaffected.**

| Item | Result |
|---|---|
| R1 | Fixed: `not_run` is in `UNDETERMINED`. |
| R2 | Fixed: `check_binding` at manifest build (flags `-me k x 100,000`, exit 2, rules in [0.99 x limit, limit], strictly increasing); stored as `manifest['binding']`; `survived` needs `systems_ok`. |
| R3 | Fixed: `verify_inputs` runs before any rung, compares each `manifest.json` and the source and `.kbprog` hashes. The `.kbprog` hash is taken after the builder's maxeqns rewrite, so it is the file `wordreduce` loads. |
| R4 | Fixed: `partial` defined and registered; `bound24 == 2^24` asserted in `load_survivors`; RSS ratio kept (D has no overflow status; accepted). |
| S1-S4 | Done. Replay of D breaks added (D3), registered. |

**N1 (required). `negative_reading_allowed` ignores words that were never run.** The summary builds its word list from the rung rows, so a word with no rows is absent. **Probe:** one word, one broke row, `systems_ok=True` gives `negative_reading_allowed = True` (n_words = 1 of 55). Fix: `summarize` takes the expected ids (the manifest's sample, or its B0 list) and counts a missing word as `not run`, which blocks the reading; also require `n_words == expected`.
- **N2 (pin).** The registered wording "none of N survived" is attached to `negative_reading_allowed`, which is true also when some words survived (the set test is `<= {broke, survived}`). Split it: `negative_reading` only if the survived count is 0; otherwise the stage-C trigger.
- **N3 (pin).** My D3 asked for a top-rung replay of a **survivor** before it is called verified; the registered `d3_replay` covers breaks only. Add the survivor replay to `stage_c_trigger` (it can run in stage C, not in B).
- **Note.** The 1x system manifests now carry `kbprog_flags`, added after job 1. The builder's default and the rule counts (99,864 and 99,894 of 100,000) agree with `-me 100000`, so I accept it, but it is an amended record: say so in the report.
- The new manifest hash 6a261976... was not recomputed by me (it needs the archive). Re-registering after N1-N3 changes it again.

## Re-check of N1-N3 (2026-10-22)

Method: diff read, 24 tests under capjob (pass), probe of `summarize` with one broke row. No data opened.

**Verdict: CONFIRMED. From the math side, the 55-word B may start**, once the driver is committed and the job pins that commit.
- **N1:** expected ids without rows get status `not_run`; `negative_reading_allowed` needs the ids, an equal count, verified systems and every status `broke`. Probe: expected [a] gives True; expected [a, b] gives False (`not_run` 1); no ids gives False.
- **N2:** the negative reading needs zero survivors; `stage_c_trigger` lists the survived ids.
- **N3:** the registered text now has the survivor replay in stage C. Registered text only; stage C is not built.
- The run script passes `--b0` through to the summary, so a B0 run is judged against the B0 list.
- Pin: the manifest hash e1fa833f... was not recomputed by me (it needs the archive). B must run from a committed head whose code sha is recorded with that hash.

## Ruling: binding rule amended after B0 (2026-10-22)

Lead request. Method: read `word_summary` in the uncommitted tree and the registered text; no B0 outputs opened.

**Ruling: ACCEPTED WITH A LABEL ("binding rule amended post-B0"), plus one wording fix.**
- **Why acceptable.** The change moves only the partial/survived labels, never broke/exhausted. The reason is a measurement (bytes per coset 61 B on x86 against 98 B on the Mac), which makes the job-1 2^24 peak a wrong baseline. The new ratios are platform independent, so it holds if a word runs on either host.
- **Direction.** The old rule blocked (partial); the new one is more permissive toward `survived`, and it was changed after B0 showed the old rule mislabelling 2^25. The cost of a false `survived` is a stage-C run, whose first step is the replay and then certification, so it cannot create a counted success alone. Record in the report: old and new manifest hashes, the date, the reason, and that B0's 4 words showed the problem. B0 labels are recomputed under the new rule.
- **Top rung.** In the code the top rung is not affected by "no successor": for k >= 1 the test is peak >= 1.5 x the previous D rung's peak, so 2^28 can count as survived. The "no successor" clause only bites a ladder with a single finished D rung (the first-rung test has nothing to compare). The registered sentence "A D rung with no successor to compare is not binding" reads as if the top rung were excluded, which would make `survived` unreachable. **Reword it** to "the first D rung, when it is the only finished D rung".
- **Weak point, optional.** The first-rung test (next peak >= 1.9 x its own) shows proportional growth, not strictly that the table filled. A stronger complement, available from B0's cost calibration: the absolute check peak >= 0.9 x (61 B x bound) on x86. Add it as a second condition if cheap.
