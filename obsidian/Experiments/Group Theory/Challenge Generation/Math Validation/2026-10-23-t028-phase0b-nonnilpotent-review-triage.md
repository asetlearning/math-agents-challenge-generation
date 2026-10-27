---
type: triage
date: 2026-10-23
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 Phase 0b: review of the non-nilpotent witness search for G_7 (pair search, low index)"
---
# T-028 Phase 0b review: triage

Lead request (2026-10-23). Source: Experimenter-B25 note `t028-phase0/2026-10-23-t028-phase0b-nonnilpotent-search.md`, `pairs.g`, `lowindex.g`, `relwords.g`, logs `out/p_*.txt`, `out/li*.txt`. Review note: [[2026-10-23-t028-phase0b-nonnilpotent-review]].

**Asks**
1. Is the pair search equivalent to `GQuotients` onto the targets (Aut / automorphism classes, generating pairs only)?
2. The maxL logic (profile, `L>=maxL` shortcut, 5-group filter).
3. The scope wording: what "no witness in the target list" supports for G_7 as a whole.

**Step 2.5 (does the tool's model equal the target?)** The target claim is "G_7 has no finite quotient of order not a power of 5". The pair search computes quotients of G_7 inside specific groups H; low index computes quotients with a faithful-or-not action on <= N points. Neither enumerates all finite groups, so the reading must be scoped to the list. I will also check whether the list covers the minimal-counterexample types (monolithic quotient with abelian or nonabelian socle).

**Plan** (read plus local capped runs, capjob 2G / 2 CPUs, one at a time, each far under 2 h; scratch only):
- A. Cross-check the pair search against `GQuotients(G_K, H)` for K = 2..4 on small H (existence and Aut-orbit counts of generating pairs).
- B. Independent re-implementation of the profile for a few H, with my own word enumeration.
- C. Check the low-index output (7 subgroups = G plus six of index 5?) and what it implies.
- D. Check the minimal-counterexample reduction against the target list; probe the abelian-socle case (abelianization of the index-5 / 25 / 125 subgroups).

No survivor words, job-1 outputs or B outputs involved.
