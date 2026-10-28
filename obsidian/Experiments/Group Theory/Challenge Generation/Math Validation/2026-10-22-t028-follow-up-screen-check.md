---
type: validation
date: 2026-10-22
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 follow-up screen: deviations, ladder, decision rule, r11 freeze"
status: verdict sent to Lead
---
# T-028 follow-up screen: quick check

**Verdict: CONFIRMED WITH FIXES.** Items 1 and 4 are fine (item 1 with pins). Items 2 and 3 need 5 fixes before the Developer builds the driver. Scope: the plan text only; no runs, no job-1 data opened.

Terms. **T4u**: a survivor that no held-out solver breaks at the stated budgets. **D<->R rml 7**: the Todd-Coxeter-style solver with redundancy limit 7, budget = coset-table bound 2^k. **maxeqns**: kbmag's cap on stored equations. **Top rung**: 2^28 for D<->R, 16x maxeqns for kbmag. **Break**: TRUE or the empty word, accepted exactly as in job 1.

## 1. Sample deviation: sound, with pins

Quantile sampling is a fair stand-in for "5 longest" because the selection uses residual length only, never an outcome. It gives a length series and cheap benchmarks. Pins:
- **P1. Deterministic rule, recorded first.** Index at rank round(q(n-1)) for q in {0, .25, .5, .75, 1}, ties by word index. Cells with fewer than 5 T4u survivors give all of them, so "55" becomes "all sampled". The list of word ids goes into the manifest, hashed, before B0 starts.
- **P2. It is not a random sample.** A zero-survivor result covers the sampled words only. Do not quote a rule-of-three bound on the 220. This matters because of the rare-event doctrine: one unbroken word is a success, and 165 words stay untested.
- **P3. Selection effect in the long cells.** The 34 hard-capped words sit mostly in C3|9 and C1|24, so the survivors of those cells are conditional on finishing within the cap. Say so in the report.
- **P4. Calibration words** (C1|16|0, C3|9|0) stay labelled "tuned on". Nothing about the ladder is tuned on them, so they count in the 55 where they are quantile picks; report the result with and without them.

## 2. Escalation ladder: measures budget-limited vs hard only after 4 fixes

What it can show: whether T4u status in job 1 depended on structure size. What it cannot show: hardness in any absolute sense; "survives the top rung" is a statement about 2^28 and 16x.

- **F1. Rung outcomes must be 4-valued.** Per rung: broke / exhausted (finished, no break) / timeout / OOM. Only "exhausted" counts as surviving. A word with timeout or OOM at any rung is **undetermined**, not a survivor and not a break. D<->R needs about 29 GB at 2^28, and the memory scaling is extrapolated from one measurement (1.83 GB at 2^24); record the peak RSS at every rung. Set an explicit per-rung time cap before B; job 1's 15-min cap was never binding, and 2^28 may be.
- **F2. Binding check for kbmag.** In job 1 the held-out kbmag runs "finished without IdWord". If they stopped on a limit other than maxeqns (time, stored length, a halt condition), raising maxeqns changes nothing and every word will "survive" the kbmag ladder for free. Before B: record the termination reason of each of the 55 in job 1, and at each rung record whether the run actually used more equations than the previous rung. A non-binding rung is reported as non-binding and does not count as an exhausted rung.
- **F3. Where the ladder starts.** "Above job 1's verified (2x) budgets" is correct only if the 2x verification really ran D<->R at 2^25 and kbmag at 2x for all 220. The local rule allows 2^25 only after a memory check (rung25_allowed), and the should-fix I raised there was open. If 2^25 was skipped, start the ladder at the first rung not run, or the 2^24 -> 2^26 gap hides breaks at 2^25. D<->R must also be a pure cap (monotone: a break at B implies a break at larger B). Developer confirms; the ladder then may skip rungs.
- **F4. Two solvers, two units.** "Minimum breaking budget" mixes 2^k and kbmag multiples, and stop-at-first-break loses the other solver's value. Record, per word, the first breaker, its rung, and CPU-s and peak RSS at the break. Use CPU-s as the common axis. Order the rungs by cost, cheapest first.

**As a stand-in for the growth signal: only partly.** B measures the upper tail (the pre-registered clause "the budgets of every T3/T4 survivor, per m"). It does not replace the median test of §5, for two reasons: it is conditioned on surviving 2^24, so the series is left-truncated and says nothing about the median word; and it has no W series, which the pre-registration also measures. With 3 rungs the resolution is a factor 2 to 4, so use ranks within cell, not a fitted slope. Keep the owed W-series ladder (C1, 10 words per m, local, cheap) as a separate run; do not report B as F3.

## 3. Decision rule: three changes

- **D1. Three outcomes, not two.** All sampled words break -> budget-limited. At least one word exhausted at every rung -> stage C for those words. Any undetermined word blocks the negative reading until it is re-run (larger cap, or the rjob plan for more memory).
- **D2. Scope of the negative wording.** "Negative result for substitution at these sizes" is too strong. Write: "none of the N sampled T4u words survived the ladder (N of 220, stratified); the other words are untested and archived." The rare-event doctrine says zero is "no evidence at this N", never "failed", and survivors are never discarded.
- **D3. Stage C needs no r11.** A top-rung survivor can go to certification (kbcert, then T2 and T3) and to the registry route without r11. Only the r11 recovery verdict on job-1 words is post-hoc (see 4). Say that in the rule, so a post-hoc A_R failure is never read as the success evidence. Add: a top-rung survivor must be re-run at the top rung (deterministic replay) before it is called verified, since doubling is not available.
- Register the rule, the ladder constants and the sample list with a hash in the manifest before B0 runs. B0's results may change the cost plan only, never the rule.

## 4. r11 freeze: reading confirmed

r11.1 §5 2a asks for the repo@sha pin before anyone reads job-1 A_R outputs, and names "traces, verdicts or failure statistics". `ar_control/control_summary.json` is such an output (it holds the failure statistics), Lead read it on 2026-10-21, and no repo@sha was pinned. So the label applies: r11 verdicts on job-1 survivors are **post-hoc**, reported, not counted toward a success claim. Notes:
- The "tuned on" label of 2b for C1|16|0 and C3|9|0 stays, in addition.
- The r11.1 text freeze (hash c6e6eadb7af96573...) predates the read, and the control runs on fresh seeds with its own tune set, so the control rates themselves are not tainted. Only the survivor verdicts are.
- My notes record no read of job-1 A_R outputs by me.
- Clean verdicts need a fresh batch, with the pin made before any A_R output on that batch is read. Do not use the batch's own survivors to pick r11 settings.

## Open for the Developer
1. Termination reason of each sampled word's kbmag runs in job 1 (F2).
2. Whether the 2x verification ran 2^25 for all 220 (F3).
3. Per-rung time cap and OOM handling in the driver (F1).
