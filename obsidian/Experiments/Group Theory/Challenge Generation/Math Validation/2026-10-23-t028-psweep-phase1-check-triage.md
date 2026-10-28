---
type: triage
date: 2026-10-23
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 period sweep Phase 1: the p=9 break and the reading of p=8 and above"
---
# T-028 period sweep Phase 1 check: triage

Lead request (2026-10-23). Run: rjob 20261023-153651-014aa2, code b25 0a5cff2, outputs `runs/t028-psweep-f0-out` (ids and outcomes only are needed). Review note: [[2026-10-23-t028-psweep-phase1-check]].

**Asks and method** (capjob 2G / 2 CPUs, one job at a time, each short):
1. F0|9|2: rebuild the word from its definition (g u^5 g^-1, |u| = 9) if the inputs allow, re-run kbmag wordreduce with the ho_rec system at 1x, check the result is IdWord and the output replays. Is "u^5 follows from fifth powers of period <= 7" sound?
2. The p = 8 and above reading: what 0/3 at p=8, 0/21 at p=10..28 and "kbmag exhausted 1x/4x/16x" may and may not support; D 'shortened' on 17 of 27 words means D untested.

Not touched: survivor words, A_R outputs, B/B0 outputs.
