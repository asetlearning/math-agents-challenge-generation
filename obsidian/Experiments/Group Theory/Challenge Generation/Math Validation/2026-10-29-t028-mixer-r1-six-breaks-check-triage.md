---
type: triage
date: 2026-10-29
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 mixer R1: six new break certificates"
---
# Mixer R1, six breaks: triage

Lead request (2026-10-29). Ids C1|6|9, C3|4|19, C1|6|0, C1|8|0, C1|8|7, C1|16|22 (plus C3r2|2,2|1, already confirmed in [[2026-10-28-t028-mixer-c3r2-2-2-1-check]]). Files `runs/t028-mixer/r1/replay/<id>.{word,json,cert.json}` and path files in `r1/outputs/mixer/paths/` (private); report `REPORT-2026-10-29-R1.md` (claims only). Review note: [[2026-10-29-t028-mixer-r1-six-breaks-check]].

**Asks, per id**
1. The certificate's W rebuilds from the public registry construction (and equals the registry word).
2. The product of cells free-reduces to W; every cell is a conjugate of a literal fifth power.
3. Flag any rule or generalized-braid step with period > 7.

**Step 2.5.** The L0 certificate is a free-group identity in conjugates of literal fifth powers: it proves triviality in B(2,5) by definition, independent of the mixer and kbmag. Rebuilding W from the registry recipe (conjugator, phi rounds, sign, cyclic reduction) is done with my own code from `data/b25_challenge_candidates.json`; the link registry word to construction W goes through the rev-4 certificate chain where one exists. Path replay is a consistency check on the recording; rule validity by `wordreduce` (G_7 equality, modulo kbmag). Words private; numbers only.
