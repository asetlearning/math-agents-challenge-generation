---
type: validation
date: 2026-10-22
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 stage C fresh-batch addendum: check"
status: verdict sent to Lead
---
# Stage-C fresh-batch addendum: check

**Verdict: CONFIRMED WITH FIXES.** The design is sound and the arithmetic is right. Five fixes (F1-F5) and answers to the three open questions. Scope: the addendum text and the job-1 figures it quotes; no runs, no A_R data, no B0 outputs.

Terms. **Control**: the r11.1 blind-recovery check on fresh arctl words, with a pass line of at least 50 % blind recoveries per stratum, n at least 10. **Stratum**: R-only, contains KB, contains D (from the steps that shortened the residual). **Clean**: a verdict whose code was pinned before any output for those words existed.

## Arithmetic: all correct
- Strata columns sum to 220 T4u (R 105, KB 106, D 9); the 4 % for D is 9/220.
- Expected T4u: 28, 28, 25, 19 = 100; strata 17+21+6+3 = 47 R, 11+5+19+15 = 50 KB, 0+1+0+1 = 2 D; CPU-h 1.47, 1.52, 3.90, 5.18 = 12.1.
- Budget lines add to 27-34 CPU-h. Ceilings add to about 105 CPU-h, so the pause at 40 is the real control (say so).

## Findings
- **F1. The success claim "at pilot budgets" when the ladder is gated off.** If stage B finds every sampled word broken, T4u at pilot budgets is budget-limited, so a fresh word that is r11-resilient at pilot budgets is not a hardness success. Keep the gate (stop early), but a success claim always needs the ladder. Without it, report "r11-resilient at pilot budgets, budget-limited class", not a success. Open question 3: keep the gate as proposed with this wording.
- **F2. Ladder words are chosen from the wrong pool.** "5 R-only + 5 KB" can include a KB word from a stratum the control did not pass, which can never become a success. Choose ladder words among r11-unbroken words in control-passed strata, after the pass line is computed; hash the list before the ladder runs. Use the same committed escalate code and registered constants as stage B.
- **F3. Control and survivors differ in arm, not only in stratum.** The control is C1; the KB stratum of the fresh batch comes from C3 and C3r2 cells (34 of the 50 expected). A pass in C1's KB stratum transfers by chain composition only. Report the control by stratum with its residual-length range, and read a "no break" as clean only for survivors whose residual length is within the control's range for that stratum. The stratum rule must be the same code for both.
- **F4. Provenance statements.**
  - "No A_R output was read" is too strong: T4u status includes the r10 A_R verdict, and the estimate "2.5-4 min per failing run" looks like a job-1 A_R timing. State the source. Say instead: no A_R-specific field (ar_control, traces, verdicts) was read, and no r11 number depends on one. A cost figure may inform the budget, never a cap.
  - The freeze record must give the order in time: the r11.1 text hash, Lead's 2026-10-21 read of control_summary.json, the Developer's start of the r11 code, and the pin. Cleanliness of the fresh batch rests on the text hash predating anything that tuned r11, and on the pin predating fresh outputs. If the Developer saw the job-1 A_R figures before writing the code, say so and confirm no r11 parameter derives from them.
- **F5. Rule of three.** "< 3 %" uses all 100 T4u, but only assessed strata count. R-only alone (n about 47) gives < 6.4 %; with the KB stratum assessed (n about 50) each stratum gets its own bound.

## Confirmed
- **Seeds and code.** The label is fresh; check it against every label and every W (job 1, CTRL, tune, arctl, calibration). The fresh words may share seed words with job 1 (same t-pool): fine, W differs. Add a hard refusal to start when the tree is dirty, and record b25_dirty False and the tcgraph sha.
- **Cells.** Chosen from non-A_R fields; no tuning of the generator, solvers or budgets. The 4-cell choice and N are sound; no top-up after outcomes.
- **Order.** Pin before submit, verified T4u fixed before any r11 run, stop early per word, no fresh r11 verdict read before the pass line.
- **Job-1 verdicts** post-hoc, in their own column, never pooled.
- **Contains-D** "not assessed" by design: agreed (recommended answer to question 2).

## Open question 1: enlarge the control?
**Yes, but decide now and size it properly.**
- It is legitimate before the control has run: no control output exists, and the size rests on non-A_R counts. Record it as an amendment (r11.2) with a new text hash, dated, stating that no output was seen.
- **45 is not enough.** KB at 6-8 per 30 words is a rate of 0.20-0.27, so 45 words give a mean of 9-12, and the chance of n below 10 is about 40 %. Use about 60-70 (mean 12-16), fixed N, no top-up; the cost (about 10-12 CPU-h) is inside the 16 CPU-h ceiling.
- Better still, if the planted structure is known for C3 words, draw the KB-rich part from C3 arctl words, which also fixes F3. Math Expert to say whether that is possible.

## Re-check of rev 1 and r11.2 (2026-10-22)

Lead request. Files read with the hashes quoted: r11 proposal 37e673f1... and addendum 3272dd9b... (both match). Argument and arithmetic only; no data opened.

**Verdict: CONFIRMED, with 3 wording/scope fixes (G1-G3). I recommend the C1-only batch.** F1-F5 are applied correctly.

## r11.2 (control 70 C1 W, 18/17/17/18, N fixed)
- Arithmetic: 18(.27) + 17(.13) + 17(.14) + 18(.33) = 15.4 KB, so R-only about 55 of 70 (the note says about 45: check which it means; the KB figure is what matters). Binomial(70, 0.2): mean 14, sd 3.35, P(KB <= 9) about 9 %. Correct.
- **G3 (minor).** The per-m KB rates 0.14 (m=12) and 0.33 (m=16) do not match the T4u counts quoted (3/30 = 0.10; 8/30 = 0.27); with those, the mean is 13.6 and P(KB < 10) about 11 %. They may come from non-T4u residuals; name the source. Either way the risk is about 10 %, accepted.
- The change rests on non-A_R counts and no control output exists; the pause at 16 CPU-h includes the chain. Fine.

## The C3 argument
- **The argument is sound as a statement about A_R as specified.** Success and acceptance need one pair (x', y'), and (ii) bounds the difference |Delta| by |w|/4. With three conjugated images, one pair covers about a third, so Delta is about 2/3 of w, above the bound. This is a property of the acceptance rule, not a theorem about recovery: a K-pair attack (r12) would not have it. It is argued, not measured.
- **The conclusion does not depend on the argument.** The control is C1 only, so under F3 a C3 or C3r2 "no break" is outside the control's coverage and is not clean anyway.
- **Consequence for the owner.** The clean success claim is C1-only by construction. C3 survivors (the shortest job-1 survivor, 96 letters, is C3r2) can still be certified and proposed to `tested` through stages B and C without r11; they just cannot carry the "recovery-resilient" part. State this in the claim.

## The two variants
- **C1-only (C1|6 x70, C1|8 x70): recommended.** Table re-derived: T4u 49 + 49, strata 30/19/0 and 37/9/2 (R 67-68, KB 28, D 2), CPU-h 2.57 + 2.66 = 5.2. Residuals about 140-430 are inside the control's expected range. The arm mismatch of F3 disappears, and stop-early says not to spend on words that cannot be clean. Rule of three: R-only < 4.4 %, KB < 10.7 % (right).
- **Four cells (about 12 CPU-h):** adds 60 words that can only be "attack-limited". The cost difference is small (about 7 CPU-h); the loss is only that C3 words get no new T4u evidence, and 220 job-1 survivors already exist. Choose it only if the owner wants more C3 pilot-level T4u counts.
- Both variants hold the control at C1.

## Fixes
- **G1. The cleanliness sentence is wrong as written.** §4.2 says "(1) and (5) predate anything that could tune r11". Item (5), the r11.2 hash (2026-10-22), comes **after** Lead's read (2) and the Developer's reading of job-1 A_R fields (3). Only (1) predates them. Reword: the fresh batch is clean because the r11.1 text (1) predates the reads, r11.2 changes only the control size from non-A_R counts (argued, §6 of the proposal), no r11 parameter derives from the reads (7), and the pin (6) predates every fresh output.
- **G2. Selection effect, report it.** Fresh survivors are T4u, so r10 A_R did not break them, while the control words are unselected. About 70 % of the control words would be T4u by job-1 rates, so the effect should be mild; still, report the control's blind rate on the subset that r10 does not break, if r10's verdict is available for the control words at no extra cost. If it is not, say so in the report.
- **G3.** As above (name the source of the per-m KB rates).

## Owner keeps the 4-cell batch (2026-10-23): check against that variant

Lead decision; the reverted file is not yet written, so this is a check of the variant against rev 1, to be repeated on the new file and hash.

**Verdict: the 4-cell variant is acceptable**, with four items the reverted text must carry.
- **V1. Clean needs "arm is C1".** F3 reads "clean only if the residual length lies in the control's range for its stratum". A C3 or C3r2 word can lie in that range (C3|4 residuals start at 192), so it could be misread as clean. Add the arm as an explicit condition: the control covers C1 only, and every C3 or C3r2 "no break" is attack-limited whatever its length.
- **V2. Counts for the bounds.** The 47 R-only and 50 KB include C3 words. Assessed counts are C1 only: R-only about 17 + 21 = 38 (rule of three < 7.9 %), KB about 11 + 5 = 16 (< 19 %). Restate them.
- **V3. Ladder words from C1 only** (F2 already says control-passed strata; make the arm explicit).
- **V4. Wording of "never a success claim".** The owner's text excludes C3 words from the clean success claim. Say that the certification and registry route (`tested`, then the owner's `candidates`) is unaffected, otherwise a C3 survivor of the top rung could be wrongly blocked from kbcert.
- Arithmetic of the original cells re-checked: T4u 28+28+25+19 = 100, strata 47/50/2, 12.1 CPU-h, budget lines 24-30 total, pause 40.

## Final check of rev 3 (2026-10-22)

Lead request. Hashes match: addendum 90295c85..., r11 proposal ce7e25a0.... Read in full; argument and arithmetic only.

**Verdict: CONFIRMED. G1-G3 and V1-V4 are all in.**
- G1: §4.2 now gives four reasons and no longer claims item (5) predates the reads. G2: control rate on the r10-unbroken subset, or "unavailable", reported. G3: source of the KB rates stated (8/4/3/8 of 30; 13.6; about 10 %). The hash change from 37e673f1 is recorded in the freeze list.
- V1: clean needs arm C1; every C3/C3r2 "no break" is attack-limited. V2: bounds C1-only (R about 38 gives < 7.9 %, KB about 16 gives < 19 %). V3: ladder words from the C1 cells. V4: certification and registry route stay open.
- Budget: 12 + 4-6.5 + 4-6.5 + 10-11 + under 1 = about 30-37; the high end is close to the pause at 40, which stays the control.
- Cosmetic: (a) r11.2 and the addendum still say R-only about 45 for the control; the same source gives 37 (13+... per cell: 18(.43)+17(.53)+17(.63)+18(.53)); irrelevant to the n >= 10 rule. (b) The TOPIC line says rev 2, the status line rev 3.
