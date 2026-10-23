---
title: "T-028 stage C: fresh-batch addendum to the pilot pre-registration (clean A_R r11 verdicts)"
author: asetlearning
date: 2026-10-22
source: Math Expert draft for Lead (pre-registration addendum; owner approves)
status: conjectured
tags: [agent/math-expert, user/asetlearning, domain/group-theory, topic/b25, topic/hard-instance-generation, topic/preregistration, project/challenge-gen, status/conjectured]
---

> [!note] Public copy
> Verbatim copy of the Math Expert's private proposal `2026-10-22-t028-stage-c-fresh-batch-addendum.md` (sha256 `90295c85e5d9255e1cc4ae82cbb220bf6df44e1d22b3fb68bd21125ce0026461`), the stage-C fresh-batch addendum (rev 3), as confirmed by the Validator on 2026-10-23. Everything below this box is the original text; links to private notes resolve only for their owner.

TYPE: REPORT
FROM: Math Expert
TOPIC: T-028 stage C: the fresh-batch spec for clean A_R r11 verdicts (rev 2: the Validator's F1–F5 applied, the r11.2 control, and the owner's 4-cell design)
PROJECT: [[project-challenge-gen]]
CONTEXT: [[2026-10-20-t028-pilot-preregistration-draft]] (the r10 pipeline); [[2026-10-21-t028-ar-r11-proposal]] (r11.1, plus amendment r11.2 §6); [[2026-10-22-t028-follow-up-screen-plan]] (stages B and C); the Validator's check [[2026-10-22-t028-stage-c-fresh-batch-addendum-check]] (CONFIRMED WITH FIXES); the owner's decision via Lead (2026-10-23: r11 runs on job-1 survivors as post-hoc, **and** on a fresh batch, where its verdicts are clean; the host is cpuserver); Lead's decisions on Q1–Q3 (2026-10-22).
STATUS: rev 3, the Validator's G1–G3 and V1–V4 applied; final. **[rev1]**–**[rev3]** mark changes. Labels: **argued**, **conjectured**, **open**. Every number is a proposal.

**Provenance** [rev1, F4]:
- **No A_R-specific field was read for this note:** no ar_control file, no traces, no verdicts. **No r11 number depends on one.**
- Sizing used job 1's per-word T4u status (which includes the r10 A_R verdict as one input), residual length, CPU seconds, and the kinds of the shortening steps.
- The 2.5–4 CPU-min per failing blind A_R run is the Developer's figure as quoted in [[2026-10-21-t028-ar-r11-review]] §3. A cost figure informs the budget, never a cap.
- The generator, the solvers, the gates and every budget are as in job 1. The cells were chosen from job-1 aggregate rates, and nothing was *tuned*.

**Terms.**
- **T4u / verified T4u:** as in §7.0 and §7.0a.3.
- **Stratum:** R-only, contains KB, or contains D, from the steps that **shortened** the residual. **One function computes it, for the control and for the survivors** [rev1, F3].
- **Top rung:** the last rung of the stage-B ladder.
- **Clean:** a verdict whose code was pinned before any output for those words existed.

## 1. Inputs, seeds and code

- **Seed label:** "20261022|stageC|arm|m|index" (sha256 → PCG64), never used before.
  - It is checked against every label used so far (pilot, tune, arctl, calibration).
  - Every fresh W is checked against every W of job 1 (CTRL included), the tune set, the arctl control and the calibration words. The check is recorded.
  - Sharing t-pool words with job 1 is fine: W differs.
- **Same generator and screen pipeline as job 1**, with the canonical-tie-break R (§7.0e).
- [rev1] **A dirty tree is refused:** the driver will not start if b25 or tcgraph has uncommitted or untracked files. The manifest records **b25_dirty: False**, the b25 sha and the **tcgraph sha**. (Job 1's manifest has b25_dirty: True, with 1 untracked file.)
- **No tuning on job-1 outcomes.**
- **Host:** cpuserver, via rjob, with the rjob plan (naming the host and cost) to Lead first.

## 2. Cells and N [rev2: the owner keeps all 4 cells, 2026-10-23]

**The cells (owner's decision): C1|6 × 40, C1|8 × 40, C3|4 × 30, C3r2|2,3 × 30, i.e. 140 words.**

| cell | words | expected T4u (job-1 rate) | expected R / KB / D | CPU-h (job-1 rate) |
|---|---|---|---|---|
| C1\|6 | 40 | 28 | 17 / 11 / 0 | 1.5 |
| C1\|8 | 40 | 28 | 21 / 5 / 1 | 1.5 |
| C3\|4 | 30 | 25 | 6 / 19 / 0 | 3.9 |
| C3r2\|2,3 | 30 | 19 | 3 / 15 / 1 | 5.2 |
| **total** | **140** | **≈ 100** | **≈ 47 / 50 / 2** | **≈ 12** |

**Single-pair limit (argued; owner's ruling).**
- A_R (r9–r11.2) is single-pair: success is w = g⁻¹ φ′(t′) g for one (x′, y′).
- A C3 or C3r2 word is a product of three conjugated images in three different rank-2 subgroups. So an r11 "no break" on such a survivor reflects a structural limit of the attack.
- **C3|4 and C3r2|2,3 survivors are reported as "attack-limited (single-pair A_R)", and never count toward the clean r11 recovery-resilient claim** [rev3, V4: this is the meaning of "never a success claim", as confirmed by Lead].
- **r11 still runs on them** (it can still break them, as a kbmag-dominated break or a partial-window proof), and **an r11 break removes them**.
- They are **never ladder words** (§5.1, F2).
- They are reported because they include the shortest survivors (job 1's shortest was 96 letters, in C3r2|2,3), the benchmark-grade candidates at pilot budgets.

**Clean-eligible survivors: the C1 cells only.**
- Expected about 56 T4u, with R / KB / D ≈ 38 / 16 / 1.
- Expected residual lengths about 140–430, inside the r11.2 control's expected range of about 140–900 (§3).
- **Strata (conjectured):** a C1 stratum with fewer than 10 clean-eligible survivors is "not assessed". There is **no top-up**.
- **Contains D: "not assessed" by design** (Lead's decision Q2).

## 3. The r11 control: r11.2 (Lead's decision Q1)

- See [[2026-10-21-t028-ar-r11-proposal]] §6: **70 C1 arctl W, with m ∈ {6, 8, 12, 16} and 18 / 17 / 17 / 18 words; N fixed, no top-up.**
- [rev3, G3] Expected KB ≈ 13.6 (source: job-1 KB counts among T4u per C1 cell, over all 30 words; see r11.2 §6) and R-only ≈ 45. The chance of KB < 10 is about 10 %, accepted.
- Expected cost about 10–11 CPU-h, with a **hard pause at 16 CPU-h**, chain included.
- No control output exists yet. The amendment rests only on non-A_R-specific counts.
- [rev3, G2] **Selection effect.** Fresh survivors are T4u, so r10 A_R did not break them, while the control words are unselected.
  - The control's blind rate is also reported on the **subset of control words that r10 A_R does not break**, if the control's run records r10's verdict at no extra cost.
  - If it does not, the report says that this subset rate is unavailable.
  - The effect is expected to be mild (conjectured): about 70 % of control words would be T4u at job-1 rates.
- [rev1, F3] **The control is reported per stratum with its residual-length range** [min, max]. A survivor's r11 "no break" is clean **only if its residual length lies within the control's range for its stratum**.

## 4. Order, pins and the freeze record

1. **Pin before submit.** The committed r11.2 code (the arctl and tune label code included), the stage-B escalate code and the ladder constants are pinned by repo@sha. They are recorded in the fresh batch's manifest **before submit**, so before any fresh A_R output (r10 or r11) exists.
2. **Freeze record** [rev1, F4], kept by Lead, in time order:
   1. the r11.1 text hash, c6e6eadb7af96573f587e3ac7d1b34c284e3b307f9005e0007e57afea0d121db (2026-10-21);
   2. Lead's 2026-10-21 read of `ar_control/control_summary.json` (date and time);
   3. **the Developer's disclosure, verbatim:** before r11 work began, for Lead's job-1 tally, the Developer read the A_R outcome, stage, kind and attribution fields of the 25 T3u-not-T4u words, and the summed control seconds;
   4. the start of the r11 code (the Developer's first commit, with its date);
   5. the r11.2 text hash, ce7e25a097cd30571994de566745079558fcb00fd9e89a008dfedf2e4a8dd21c (2026-10-22, final, with the G3 wording fix). The first r11.2 version was 37e673f1676ebac481e848289618246b70bf85a9ca2374bf5ad7b3b713ced11c; the only change since is the stated source of the expected KB rates;
   6. the pin (repo@sha, with its date);
   7. the Developer's statement that **no r11 parameter derives from any job-1 A_R figure**.

   [rev3, G1] The fresh batch is clean for four reasons:
   - the r11.1 text (1) predates the reads (2) and (3);
   - r11.2 (5) changes only the control size, from non-A_R-specific counts (argued; r11.2 §6);
   - no r11 parameter derives from the reads (7);
   - the pin (6) predates every fresh output.
3. **Per word, stop early:**
   1. screen → T3u gate → held-out solvers (A_R r10 included) → verification (a)–(c). This fixes the verified T4u set;
   2. **A_R r11** at 15 CPU-min. A break stops the word;
   3. **r11 verification at 30 CPU-min**, on the r11-unbroken words only;
   4. the ladder (§5.1), on the selected words only;
   5. kbcert (§5.2).
4. **The control runs once, from the pinned code.** No fresh r11 verdict is interpreted before the control's pass line exists. The same control serves the job-1 post-hoc verdicts.

## 5. Stage-C items

### 5.1 Top-rung ladder and replay

- **Gate (Lead's decision Q3):** the fresh ladder runs only if stage B on job-1 survivors finds **at least one top-rung survivor**.
- [rev1, F1] **A success claim always needs the ladder.** If the gate is off, fresh r11-unbroken survivors are reported as **"r11-resilient at pilot budgets, budget-limited class"**. That is not a success.
- [rev1, F2] **Choosing the ladder words.**
  - Words are chosen **only among r11-unbroken verified T4u of the C1 cells** [rev3, V3] **that lie in a stratum the control passed, and within its length range**. The choice is made **after the pass line is computed**.
  - At most 10 words, shortest residual first, ties by index, split as evenly as possible across the passed strata.
  - **The list is hashed before the ladder runs.**
- **Same committed escalate code and registered constants as stage B.**
  - Rung outcomes are broke / exhausted / timeout / OOM. Only "exhausted" counts as survival.
  - A word exhausted at every rung is **replayed at the top rung** (same platform) before it is called "verified at the top rung".
- **Cost:** from B0, on its own rjob plan to Lead, outside the total in §7.

### 5.2 Certification by kbcert

- For each word verified at the top rung: cert(residual) = cert(W) composed with the step fragments.
  - The R steps come from the R trace.
  - The KB steps go through kbcert (measured at 0.01 s per KB step, about 30–108 cells per word).
  - The D loops go through kbcert at the §9.1 cap.
- The result must be **L0-cert over U_L**, with L recorded. Then the official **T2–T3**, then the registry's `tested` log. The human decides on `candidates`.
- Cost: under 1 CPU-min per word, apart from building the R trace.

## 6. What is counted, and how outcomes are read

**Counted, per cell and per stratum:**
- the fresh verified T4u count, with residual lengths (min, Q1, median; and the count with residual ≤ 300);
- the A_R r11 verdict: **break-recovery**, **break-kbmag-dominated**, **candidate kbmag failed** (not a break), or **no break**;
- the ladder outcomes, with the first breaker, rung, CPU-s and RSS;
- the certification outcome.

**Reading the outcomes:**
- **Clean "no break"**: [rev3, V1] **the arm is C1**, the stratum passed the control (≥ 50 % blind recoveries, n ≥ 10), **and** the residual length is in the control's range for that stratum.
- [rev3, V1] **Every C3 or C3r2 "no break" is attack-limited, whatever its length or stratum.**
- **Every other "no break" is "attack-limited"**: the word stays unbroken and the tiers are unchanged.
- **An r11 break is a break in every stratum.**

**The success claim** (the existence framing). It needs a fresh word that meets all of:
- it is a verified T4u;
- it has a clean r11 "no break";
- it is exhausted at every ladder rung and confirmed by the top-rung replay;
- it is L0-cert by kbcert, and passes T2–T3.

[rev3] **The clean recovery-resilient claim is C1-only.**
- [rev3, V4] C3 and C3r2 survivors stay **open to certification (kbcert, L0 over U_L), the official T2–T3, and the registry route** (`tested`, then the owner's decision on `candidates`), via stages B and C, **without the recovery-resilient part**.
- [rev3, V2] The assessed counts and the zero-survivor bounds below are C1-only: R ≈ 38 gives < 7.9 %, and KB ≈ 16 gives < 19 %.
- Their record says "attack-limited (single-pair A_R)".

**Job-1 words:** their r11 verdicts are post-hoc, kept in their own column, and never pooled. C1|16|0 and C3|9|0 are also labelled "tuned on".

[rev1, F5] **Zero clean survivors** means "no evidence at this N". The bound is given **per assessed stratum only**, by the rule of three (3/n at 95 %):
- [rev2] R-only, C1 cells only, n ≈ 38: < 7.9 %;
- [rev2] contains-KB, C1 cells only, n ≈ 16: < 19 %.

The C3 and C3r2 survivors never enter these bounds.

The n used is the **number of verified T4u in the stratum that reached a clean reading**, i.e. those inside the control's length range.

## 7. Budget (cpuserver)

| item | expected (conjectured) | ceiling |
|---|---|---|
| batch, 140 words | ≈ 12 CPU-h | the job-1 per-word caps |
| A_R r11 on about 100 T4u (all 4 cells) | ≈ 4–6.5 CPU-h | 25 CPU-h |
| r11 verification on the r11-unbroken | ≈ 4–6.5 CPU-h | 50 CPU-h |
| the r11.2 control | ≈ 10–11 CPU-h | hard pause at 16 CPU-h |
| kbcert | < 1 CPU-h | — |
| **total** | **≈ 31–37 CPU-h** | ≈ 100 CPU-h |

- **The pause at 40 CPU-h in total (the ladder excluded) is the real control**, since the ceilings add up to about 100 CPU-h.
- Cost: about $0.55/h × the wall hours. At 15 slots, about 2–3 wall-hours for the batch and r11, plus the control.

## Open questions

None. The cells were decided by the owner on 2026-10-23.
