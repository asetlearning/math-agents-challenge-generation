---
type: triage
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: review of pre-registration r9, the R-aware recovery attack A_R (§7.0d, with edits to §3, 4, 7, 7.1, 8, 9.6)"
---
# T-028 r9 (A_R): triage

Lead request (2026-10-20). Review note: [[2026-10-20-t028-preregistration-r9-ar-review]].

**Asks:**
1. The block-aligned lemma (argued): re-derive it and find the hypotheses it needs.
2. Success criteria (i) and (ii) (exact or via kbmag on Δ): does a success prove w = 1 in B?
3. Soundness of A_R1–A_R4: A_R2 proposal-only; A_R3 sound by construction.
4. The nondegeneracy rule.
5. Budgets: 15 / 30 CPU-min, and the control pause at 4 CPU-h.
6. The positive control (150 C1 residuals + R-depth series, oracle and blind) and the 50 % "attack-limited" rule.
7. Held-out discipline: the tune set with the 849-letter calibration residual; what blind mode reads.

**Method:** a document review with my own derivations; no runs. Sources: the draft (r9), my earlier T-028 notes and my R-trace data from the tcgraph review.
