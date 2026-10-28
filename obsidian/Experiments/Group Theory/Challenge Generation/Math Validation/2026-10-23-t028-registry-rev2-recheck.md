---
type: validation
date: 2026-10-23
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 registry rev 2 DRAFT re-check"
status: CONFIRMED, one wording fix (G1)
---
# Registry rev 2 re-check

Triage: [[2026-10-23-t028-registry-rev2-recheck-triage]]. Draft sha256 4e6849b2... (private).

- **Replay: 9/9 pass** with my own code (L0 product of conjugated fifth powers over the per-word table frees to the word; chain W = P g^-1 word g; L = largest primitive-root period; cell counts). The first 7 records equal rev 1.
- **Diff vs rev 1:** only revision, code (+t028_note), solver_identity (+t028_r_variants), change_log (old entries preserved, +1) and tested (+10). Nothing else changed.
- **F1:** every C1 record carries "construction-aware attacks attack-limited (r11 control failed in every stratum; oracle diagnostic fired)"; every C3 / C3r2 record carries "attack-limited (single-pair A_R); never toward the clean claim". Matches the owner rule.
- **F2 / F3:** per-record `code`, gate_deviations (D1 and S2-chain on the identity image; plain R in the gate; per-word table) and escalation_note present. B / B-ext counts match the escalation outputs (4 B, 5 B-ext among the 9). "13x" = 2^28 / 20M = 13.4. "16x" is scoped to the kbmag rungs.
- **F4:** the selection rule (the 10 shortest residuals, lengths 96..249; the removed record at 159 sits inside the range) and the private-only note are in the change_log. No machine paths.
- **R-variant evidence:** `runs/t028-rvar-old-out` (tcgraph bc6b97f) and `runs/t028-rvar-rnd-out` (seeds 1-5, 998fe9c): all 9 ids are "unchanged" in all variants; C3r2|2,3|9 is "emptied" in all six. The 4 shortened words in the sidecar are not among the 9. So the label "unchanged ... on all 16 images" is true for the 9.
- **Removed record:** keys are id, kind, length, levels (none), note, origins, status; no word, certificate or reproduction.

**G1 (fix).** The broken record's note says R "empties all 16 images". The rows only record the class: `classify` returns "emptied" at the first image that R empties (the code stops there). Reword to "empties at least one of the 16 images (the run stops at the first)". The conclusion (word broken by R, trivial) is unaffected.

**Scope reminders (no change needed).** L1-r25 for these words holds for R at f4b7771 and later; the other tie-breaks tested are the old order and 5 random seeds, not all tie-breaks. The ladder verdict (B / B-ext) was obtained with the canonical R; the broken word shows the ladder alone was not enough, which the R-variant label records.
