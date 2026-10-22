---
type: validation-verdict
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: confirmation of pre-registration r6 together with the Developer's updated implementation plan"
verdict: "CONFIRMED with 4 pins. r6 writes Lead's 5 decisions correctly, and the plan matches them: 12 cells, 360 words, report-only F1/F2, T4u = T3u + not broken, verification (a)-(c), filters on every residual, B denominators 200/50. Pins: (1) the ladder word sets: the plan's 'step 3' is the filters, not the gate, and the W series must not depend on gate survivors (in a rare-event pilot, few or none pass); (2) the beam probe: the measured cost (about 60 CPU-h) supersedes r6's '2.5 CPU-h', so r6 must name the cut settings and the restated bound (< 1.5% pooled), and pre-selection is a sampler change needing Math Expert; (3) B0 needs GAP, which the Mac lacks, so pin where the filters run; (4) state that a loop failing check (c) means 'not verified'. Optional: also kbmag-check the R-step loops."
---
# T-028 r6 and the updated plan: confirmation

This is a Lead request (2026-10-20). It covers `MathExpert/proposals/2026-10-20-t028-pilot-preregistration-draft.md` (r6, §7.0a and §B) and `Developer/2026-10-20-t028-pilot-implementation-plan.md` (updated 14:35), checked against Lead's decisions and [[2026-10-20-t028-preregistration-r4-r5-confirm]].

## Lead's decisions in r6 and in the plan

| decision | r6 | plan |
|---|---|---|
| 1. B denominators: greedy 200 and beam 50; restated bounds; above about 10 CPU-h, cut settings, not the rule | yes (§B). Per setting: 3/200 = 1.5 % and 3/50 = 6 %; pooled: 3/7,200 = 0.042 % and 3/1,800 = 0.167 %. "< 0.04 %" should read **≈ 0.042 %**, a rounding that slightly overstates the bound | yes, and **measured**: beam about 60 CPU-h, so it proposes cutting to 4 settings (200 products, pooled < 1.5 %). See pin 2 |
| 2. Cells and N: 30 per cell, C3r2 as 3 cells, survivors counted on all 30, ladders on the first 10 passing step 3, F1/F2 report-only | yes (§7.0a.1) | yes: 12 cells, **360 words** (11 × 30 + CTRL 30); F1–F4 report-only; no arm dropped. See pin 1 on the ladder sets |
| 3. T4u = T3u + not broken | yes | yes (step 6) |
| 4. Verified T4u (a)–(c), length and ratio to W | yes | yes. See pin 4 |
| 5. Abelianization and B0 on every residual; harness-bug stop | yes | yes (step 3). See pin 3 |

**Also consistent:**
- the screen chain R → KB → D(20M, rml 3), with CL left out as a recorded deviation;
- T3u with D1 at the identity image only;
- the archive with outcome labels and the re-run of capped words;
- the ladders with D first and R-emptied W excluded;
- τ-b, with censored values tied at the top rung + 1;
- the stops.

**CPU.** About 60 CPU-h central (range 35–110) on the Mac, with 9 workers and about 7 h of wall time. The parts add up to the stated figures. This is above the 2 h threshold, so it needs Lead's or the owner's approval of the rjob plan (plan question 2).

## Pins

**1. The ladder word sets.**
- Lead's decision says "the first 10 words per cell by index that pass step 3", meaning the pre-registration's step 3, the **gate** (L0, L1-r25, S1-each).
- In the plan's numbering, step 3 is the **filters** and step 4 is the gate. Plan step 8 ("pass step 3") is therefore ambiguous.
- More importantly, in a rare-event pilot very few words, possibly none, will pass the gate. F3's **C1 W series** would then have no data.
- **Pin:**
  - the **W series** (which F3 uses) = the first 10 W per cell by index, whatever happens downstream. This is the r3 pin 4 rule.
  - the **residual series** = the first 10 residuals by index that pass the T3u gate, possibly fewer, with the count reported.

**2. The beam probe.**
- r6 §9.5 still estimates "about 1 CPU-h greedy and about 2.5 CPU-h beam" in Python. The Developer's measurement (window exponent about 300 µs per candidate; about 125 s per beam product) gives about 60 CPU-h for 1,800 beam products. The measurement supersedes the estimate.
- Under Lead's rule, the cut must be written into r6: which settings are kept (the Developer proposes ℓ = 30, k ∈ {4, 6}, d ∈ {1, 3}), and the bounds that result: per setting < 6 %, pooled < 1.5 %.
- The plan's alternative, pre-selecting the 64 best candidates by junction cancellation, **changes the sampler**. It is acceptable only as a declared variant agreed with Math Expert, and the bound statements then refer to that sampler.
- Greedy at 7,200 products (about 0.5 CPU-h) is unaffected.

**3. B0 on the Mac.**
- The plan's finding 5 says the Mac has no GAP, but step 3 runs B0 (GAP + anupq) on every residual. Pin one of:
  - run the filters on the VM, with residuals staged back;
  - or stage GAP and anupq on the Mac.
- Abelianization is trivial anywhere. B0 takes about 1 s per word after the class-12 quotient is built (about 3 s in my T-027 run).

**4. Check (c) wording.**
- The plan says "a loop that does not reduce is reported, not hidden". Under Lead's decision, such a survivor is then **not verified**. A non-reducing loop proves nothing either way, because kbmag is non-confluent.
- **Pin:** the record says "T4u, verification (c) incomplete" and gives the loop.
- **Optional:** run the same kbmag check on the **R-step** loops as well (rotation-adjusted, with c from the block). R is also a tool, and the check is cheap.

## Verdict

**CONFIRMED** with pins 1–4. Pin 2 needs Math Expert to add one line to r6 (the cut settings and bound, or the declared sampler variant). The others are Developer pins. None needs a further math judgement. Lead can commit the pre-registration with the code once the pins are in.
