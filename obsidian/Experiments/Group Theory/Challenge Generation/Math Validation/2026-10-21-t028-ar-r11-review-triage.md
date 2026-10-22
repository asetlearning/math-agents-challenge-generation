---
type: triage
date: 2026-10-21
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: review of the A_R r11 proposal (follow-up screen of archived survivors only)"
---
# T-028 A_R r11: triage

This is a Lead request (2026-10-21), low priority, taken after the job-1 batch addendum. The proposal is `MathExpert/proposals/2026-10-21-t028-ar-r11-proposal.md`. Review note: [[2026-10-21-t028-ar-r11-review]].

**Asks and method** (argument and arithmetic only, no runs):
1. **N, the short-run normal form.** Is it sound? Is it well defined (base point, strategy, confluence)? Compare it with R's rule for |u| ≤ 2.
2. **(ii-local).** Check that the substitution argument proves w = 1 in B, and what the implementation must check literally. Assess the attribution bounds as a measure of recovery against kbmag doing the work.
3. **Control design.** Check the seed label, calibration only on the tune set, the per-stratum 50 % line with Wilson intervals, the oracle diagnostic below 80 %, the cost against the 4 CPU-h pause, and whether the control strata can be populated at all.
4. **Leakage.** Look for any path by which pilot words, survivors or job-1 A_R outputs could inform r11's settings.

Context: r10 §7.0d (frozen), my r9 review ([[2026-10-20-t028-preregistration-r9-ar-review]]), and the job-1 A_R addendum ([[2026-10-20-t028-job1-batch-review]]).

## Re-check of r11.1 (2026-10-21)

This is a Math Expert request, routed by Lead. r11.1 was rewritten in place, with [r11.1] marking the changes.

**Method:**
- Check each of my 2 issues and 6 pins against the new text.
- Re-check the arithmetic of the ceilings.
- Look for new inconsistencies.
- No runs.
