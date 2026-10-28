---
type: triage
date: 2026-10-22
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: code review of A_R r11.2 and the fresh batch, before the pin"
---
# T-028 r11 code review: triage

Lead request (2026-10-22). Uncommitted b25 t028-pilot worktree on top of 627b58a. Its commit becomes the r11 pin, so my verdict comes first. Review note: [[2026-10-22-t028-r11-code-review]].

**Asks and method** (read and probe; nothing from job-1 A_R outputs or B/B0 outputs):
1. r11 code against the frozen texts: r11.1/r11.2 (hash ce7e25a0), addendum rev 3 (90295c85).
2. The freeze record: order of items and the Developer's disclosure.
3. r10 unchanged: diffs of ar.py, ar_control.py, construct.py, pilot.py, seeds.py.
4. Clean = C1 + control-passed stratum + length range.
5. Stage-C clash (label), dirty-tree refusal, pauses.
6. Soundness of any new acceptance path (a break must be proved, as for r10).

Order of reading: diffs of the modified files, the freeze record, ar_r11.py, control, tests, jobs.

**Outcome:** NOT READY TO PIN, R1-R5 small; details in [[2026-10-22-t028-r11-code-review]]. I could not run the two break tests (my tcgraph extension is older than the traced R); the evidence is requested at the pin commit.
