---
type: triage
date: 2026-10-22
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 follow-up: code review of the escalation driver (b25 t028-pilot 01312f0)"
---
# T-028 escalation driver: triage

Lead request (2026-10-22). Code: `escalate.py`, `escalate_stages.py`, `tests/test_escalate.py`, the `heldout.dr_ladder` change, `jobs/t028_escalation_b0.toml` and the run script. Review note: [[2026-10-22-t028-escalation-driver-review]].

**Asks and method:** check the code against my follow-up check ([[2026-10-22-t028-follow-up-screen-check]]): sample pins P1-P4, ladder fixes F1-F4, decision rule D1-D3, registration before B0.
- Read the code and the tests.
- One probe run of `word_summary` on synthetic rows under capjob (2 GB, 2 CPUs).
- **Not opened:** survivor words, B0 outputs, the job-1 archive.

## Re-check of R1-R4 and S1-S4 (2026-10-22)
Developer request via Lead. Method: diff against c2a9699, 23 tests under capjob, two synthetic probes of `summarize`/`word_summary`; no data opened. Result in [[2026-10-22-t028-escalation-driver-review]].
