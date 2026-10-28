---
type: triage
date: 2026-10-23
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 Phase 0: review of the 5-quotient ladder of G_k (anupq), k = 2..10"
---
# T-028 Phase 0 ladder review: triage

Lead request (2026-10-23). Source: Experimenter-B25 note `2026-10-23-t028-phase0-ladder.md` and `t028-phase0/` (relwords.g, ladder.g, witness.g, logs). Review note: [[2026-10-23-t028-phase0-ladder-review]].

**Asks and method** (read plus local capped runs, capjob 2G / 2 CPUs, one at a time, each far under 2 h):
1. Relator generation: primitive, cyclically reduced, one per rotation+inversion class. Independent count in Python against the note's counts (4, 8, 17, 41, 99, 255, 660, 1752, 4692); independent check that the set generates the same normal closure as all freely reduced v, |v| <= k.
2. Series comparison: layer ranks and orders re-added; the logic "exceeds B" (a class-c quotient of larger order than B/P_c(B) cannot have exponent 5).
3. Claim "equality at 7 implies equality for all k >= 7": sandwich argument.
4. Reading: scope of "no finite 5-group witness at k >= 7"; what "nilpotent" and "witness" cover.
5. Independent tool: GAP library `PQuotient` (not anupq) for k = 6 and k = 7, and a re-run of the note's ladder for k = 6, 7.

No survivor words, job-1 outputs or B outputs are involved. Read-only on the Experimenter's files (my runs write only to the scratchpad).
