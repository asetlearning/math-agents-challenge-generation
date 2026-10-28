---
type: triage
date: 2026-10-22
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 follow-up screen: quick check of the sample deviation, escalation ladder, decision rule and r11 freeze"
---
# T-028 follow-up screen: triage

Lead request (2026-10-22), quick check (about 30 min), not a full review. Source: Lead's plan `Agents/asetlearning/Lead/notes/2026-10-22-t028-follow-up-screen-plan.md` (private), pre-registration r10 §5 and §7.0a, r11.1 §5. Review note: [[2026-10-22-t028-follow-up-screen-check]].

**Asks and method** (argument only, no runs; job-1 data not opened):
1. **Sample deviation.** 55 words at residual-length quantiles instead of "5 longest residuals per arm". Sound?
2. **Escalation ladder.** D<->R rml 7 at 2^26..2^28; kbmag held-out systems at 4x then 16x maxeqns. Does it separate budget-limited from hard, and does it stand in for the growth signal?
3. **Decision rule.** All 55 break -> budget-limited; any top-rung survivor -> stage C.
4. **r11 freeze.** Is the "post-hoc" reading of r11.1 §5 2a correct?

Scope: the plan text as written. I did not open the job-1 archive, so facts about termination reasons and memory are listed as checks for the Developer.
