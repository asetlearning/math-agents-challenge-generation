---
type: validation-verdict
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: confirmation of pre-registration r4 (rare-event framing, archive rule, stop conditions) and r5 (tiers in the owner's chosen scope)"
verdict: "CONFIRMED on the mathematics: the rare-event framing and all rule-of-three bounds are correct, the archive and stop rules are sound, T1/T3u/T4u are well defined, and T4u's 'trivial in B by a reproducible chain from a certified W' is sound. The scope alignment is NOT complete. (1) The B probe is costed for C++, but the scope says no C++: in Python (x50) it is about 30 CPU-h greedy plus about 400 CPU-h beam, so its denominators or language must be decided. (2) The Developer's plan still has 10 words per cell and 'drop the arm if F1/F2 fire', which contradicts r4's 30 per cell and no-drop framing. Four small pins: T4u should require T3u; define 'verified' for a T4u survivor; F0/F1 on residuals as a stop; the arms and cells actually in scope."
---
# T-028 pre-registration r4 + r5: confirmation

This is a Lead request (2026-10-20). It covers `MathExpert/proposals/2026-10-20-t028-pilot-preregistration-draft.md` (r4 §7 and §7.1; r5 §7.0), checked against the Developer's plan `Developer/2026-10-20-t028-pilot-implementation-plan.md` and the owner's scope: "minimal + recovery attack + B probe", using existing tools, with no certified distillation and no C++ now.

## Confirmed

**The rare-event framing (r4 §7).** "0 of N means yield < 3/N at 95 %" is the rule of three, and every figure in the text is correct:

| N | bound |
|---|---|
| 30 per cell | < 10 % |
| 90 (C3, C3r2) | < 3.3 % |
| 150 (C1) | < 2 % |
| 300 | < 1 % |
| 3,000 | < 0.1 % |
| B greedy 1,000 / beam 200 per setting | < 0.3 % / < 1.5 % |
| B pooled over 36 settings: greedy 36,000 / beam 7,200 | < 0.008 % / < 0.04 % |

- The withdrawn ≥ 90 % thresholds are kept as reported rates.
- "Zero survivors means no evidence at this N" is the right reading.
- The cheap-screen costs (about 20 CPU-s per word, giving about 1.7 and 17 CPU-h) follow from the stated per-step costs.

**The archive rule.** No residual is discarded, and capped words are re-run (doubled cap, then rjob) and never counted as failures. This is sound, and r5 extends it correctly to T1, T3u and T4u.

**Stop conditions (§7.1).**
- The correctness stops (L0 failure, CTRL R_P < 100 %, a filter contradiction, an unexplained solver–certificate conflict, a non-reproducible result) and the budget stops are complete for this scope.
- r5 adapts them correctly: the L0 stop applies to W, and a reproduction block that fails to replay is a harness-bug stop.

**The tiers (r5 §7.0).**
- **T1:** well defined. Dropping CL from the screen-mode chain is a **recorded deviation**, which is right.
- **T3u:** well defined. D1 at the identity image only is a **recorded deviation**, while R, CL and KB stay on the 16 images. The CL gate uses the existing closure BFS (the T-027 harness), so no new code is needed.
- **T4u: sound.** Every in-loop step is valid in B(2,5):
  - R is a conjugacy;
  - KB is an equality in G_7, because every kbprog rule follows from b25_full;
  - D is an equality in G_k, where k is the throw stage.

  This is the T-027 chain argument. So a T4u residual is trivial in B(2,5) whenever the logged tool steps are what they claim to be. It is reproducible, and it is correctly **not** L0-cert. Keeping T4u out of `candidates` until certified is right.

## Issues

**1. The B probe does not fit the scope (budget, not mathematics).**
- §9.5 costs the probe for C++: about 0.6 CPU-h greedy and about 8 CPU-h beam, over 43,200 products.
- §9.5 itself says Python costs about 50× more. That is about **30 CPU-h greedy and about 400 CPU-h beam**, which is infeasible.
- The scope says "no C++ now", but the Developer's mid variant writes the probe in C++ (1.5 days).
- **One of these must be decided:**
  - a C++ exception for the probe only;
  - a vectorised (numpy) probe, with a measured per-product cost before the run;
  - smaller denominators, with the rule-of-three bounds restated to match. For example, greedy 200 and beam 50 per setting give pooled bounds < 0.04 % and < 0.17 %.
- The B outcome text ("0 hits excludes …") has to quote whichever denominators are chosen.

**2. The Developer's plan contradicts r4.**
- The minimal plan uses **10 words per cell** (150 words; C3r2 as one cell), while r4/r5 keep **30 per cell** and every arm.
- It still frames F1 and F2 as "the arm is dropped", which r4 withdrew.
- **Pin, in r5 or in the plan:**
  - the cells and N this pilot actually runs (r4's 30 per cell, or the plan's 10, stated as a deviation together with the resulting bounds: 10 per cell gives < 30 % per cell);
  - that the Developer implements r4's report-only rule.

**3. T4u should require T3u.**
- r5 lists T4u's conditions as: certified W, a reproduction block, and not broken by a held-out solver.
- In r4, T4 ⊇ T3. Unless it is stated, a residual failing L1-r25 or S1-each could be called a held-out survivor.
- **Pin:** T4u = T3u + not broken.

**4. "Verified" T4u survivor.**
- r4 calls "≥ 1 verified T4 survivor" a success, but "verified" is not defined for T4u. **Suggested definition:**
  - (a) an exact replay of the reproduction block from the committed code;
  - (b) the held-out solvers re-run once at a doubled budget;
  - (c) an independent check of each KB and D step loop w_i u_i⁻¹ by kbmag (rec or slx) reduction to IdWord, which proves each step in G_7 without a certificate. This is how I checked the 16 T-027 D steps.
- Also, report each survivor's length beside its budgets. At fixed budgets, long words can survive just by being long, and the escalation is the real test.

**5. Filters on residuals.**
- The §7.1 "filter contradiction" stop names certified words.
- Residuals are trivial by the chain, so an abelianization or B₀ "non-trivial" on a residual is also a harness bug.
- **Pin:** apply F0/F1 to every residual, and stop on a contradiction.

## Verdict

- **CONFIRMED** on the rare-event framing, the bounds, the archive rule, the stop conditions and the r5 tiers.
- **Before it goes to the owner:**
  - decide issue 1 (the B probe's language or denominators);
  - align the Developer's plan with r4 (issue 2);
  - add pins 3–5.
- None of these needs a further mathematical judgement once decided.
