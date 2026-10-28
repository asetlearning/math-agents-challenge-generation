---
type: triage
date: 2026-10-26
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 survivors rev 3 (220 words) independent re-check"
---
# Survivors rev 3 re-check: triage

Lead request (2026-10-26). File (private) `t028_survivors_220_rev3.json`, sha256 7ee63c66...; old file sha 5939a1e7... Developer report `runs/t028-item3b/REPORT-2026-10-26.md` (read for the claims only; its self-check is not reused). Review note: [[2026-10-26-t028-survivors-rev3-recheck]].

**Asks**
1. The 3 emptied words (C3r2|2,3|1, |3, |9): replay W -> empty from the R cells + rotations only.
2. The 18 changed non-empty words: the new word is trivial in B0(2,5) (5^34 quotient); each certificate chain W -> new word replays (12 certified); for the 9 uncertified ones the R steps replay and the D steps are listed.
3. The 12 T3u failures: kbmag really shortens one image of each new word (S1-each), so the label is right.
4. The 199 unchanged records equal the old file except the added fields.

**Step 2.5.** Tools: my own string replay (L0 product of conjugated fifth powers over the per-word table; chain W = P g^-1 new g), GAP 5^34 quotient for B0 triviality (necessary only, and cannot distinguish W from another B0-trivial word), the project's kbmag `wordreduce` with the ho_rec / ho_slx systems for S1-each (a reduction by the rules is a proof of equality in G_7, modulo kbmag; for the label it only needs a shorter image, which is constructive). No D re-run (D steps are equalities in G_k and not certifiable; I only check they are listed). Words stay private: structural prints only. Local runs under capjob 2G / 2 CPUs, one at a time.
