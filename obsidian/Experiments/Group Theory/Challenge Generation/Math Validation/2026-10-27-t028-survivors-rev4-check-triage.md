---
type: triage
date: 2026-10-27
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 survivors rev 4 (220 words) independent check"
---
# Survivors rev 4 check: triage

Lead request (2026-10-27). Private file `t028_survivors_220_rev4.json` (sha256 c0e22bb0...), built from rev 3 (7ee63c66...) + fix12 + fix215 (job 20261027-205703-f5c5f2), builder t028-pilot 0c8cd68. Review note: [[2026-10-27-t028-survivors-rev4-check]]. Earlier: [[2026-10-27-t028-fix12-check]], [[2026-10-26-t028-survivors-rev3-recheck]].

**Asks**
1. The 15 changed records carry the fix12/fix215 fixpoint final words; history keeps the rev-3 word; no old escalation/ladder labels.
2. The 3 fix215 changes (C3|4|1 492>418 R, C3r2|2,3|22 568>565 R, C1|6|0 288>286 D): R steps replay, trivial in B0(2,5), the 2 certificates replay, C1|6|0 correctly uncertified.
3. Counts: 5 broken, 215 T3u, 204 certified.
4. The 202 unchanged records equal rev 3 except the `fixpoint` block.

**Step 2.5.** Tools: my own string replay (R traces and certificate chains as free-group identities in literal fifth-power cells), GAP 5^34 quotient for B0 triviality (necessary only), JSON diff against rev 3 and the fix12/fix215 output files for the word match. D steps are equalities in G_k and are not re-run. Words stay private; structural prints only. Local runs under capjob 2G / 2 CPUs.
