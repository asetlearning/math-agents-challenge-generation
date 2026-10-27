---
type: triage
date: 2026-10-27
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 fix12 (12 words) independent check"
---
# fix12 check: triage

Lead request (2026-10-27). Report `runs/t028-fix12/REPORT-2026-10-27.md` (claims only; its self-check is not reused); private words in `outputs/fix12/fix_<id>.json`; code b25 t028-r-variants 13e8c68 (`fix12.py`). Review note: [[2026-10-27-t028-fix12-check]].

**Asks**
1. C1|24|29 and C3r2|2,3|19 reach the empty word: replay the KB step (image map-back) and the R step.
2. The 10 fixpoint words: trivial in B0(2,5); every R and KB step replays; the KB map-back from non-identity images is correct.
3. Spot-check: kbmag (rec, slx) shortens none of the 16 images of the 10 final words.

**Step 2.5.** Tools: my own string replay (R: cells + rotation as literal fifth powers; KB: rebuild the image from the letter automorphism, check the stored image_in/out, prove image_in ~ image_out by `wordreduce` on image_in-rotation times inverse(image_out) reducing to IdWord, then map back with the inverse automorphism); GAP 5^34 quotient for B0 triviality (necessary only); `wordreduce` with ho_rec / ho_slx for the spot-check (non-reduction proves nothing, a reduction is constructive). The certificate chain W = P g^-1 word g is checked as a free-group identity in cells that are literal fifth powers (it does not depend on kbmag). No D re-run. Words stay private; structural prints only. Local runs under capjob 2G / 2 CPUs, one at a time.
