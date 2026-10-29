---
type: triage
date: 2026-10-28
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 algo-mixer beam break of C3r2|2,2|1: independent check"
---
# Mixer break of C3r2|2,2|1: triage

Lead request (2026-10-28). Report `runs/t028-mixer/REPORT-2026-10-28-path.md` (claims only), certificate `replay_C3r2_2-2_1.cert.json` (43 cells, private), path files in `runs/t028-mixer/paths/`. Review note: [[2026-10-28-t028-mixer-c3r2-2-2-1-check]].

**Asks.** With my own code: (a) the certificate expands to the word in the free group (L0), and that word equals the public registry word (`data/b25_challenge_candidates.json` rev 2) and the rev-4 word; (b) the path steps reproduce; (c) every rule used is a valid equality (kbmag rec/slx).

**Step 2.5.** The certificate is a free-group identity in conjugates of literal fifth powers, so it proves triviality in B(2,5) by definition, independent of the mixer and of kbmag. Path replay is a consistency check on the mixer's recording (rules applied at positions; braid moves local). Rule validity: `wordreduce` of lhs*rhs^-1 to IdWord (equality in G_7 modulo kbmag), plus the free-group fifth-power decomposition if the cert provides it. Words stay private; structural prints only.
