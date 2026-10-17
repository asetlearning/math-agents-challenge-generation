---
type: validation-triage
date: 2026-10-16
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
---
# Triage: T-018 restart negative (H2) and tcgraph PRs #5 / #6

**Asked (Lead, owner-approved):** (2) independently check "no state of the four restart arms (374 states) has strict maxdepth ≥ 2 under S2", so "H2 falsified"; (1) math-layer review of tcgraph PR #5 (2c264fd) and PR #6 (f2cb8a1, stacked) before merge. GO / NO-GO per PR.

**Plan.**
- (2) Recompute S2 on **all** 374 states, not a sample (they are small). Use my own kbmag parse, my own raw→core conversion, the Python reference fold, and my own peeling. Compare field by field with `strict_rescore.json`. Then a certificate-dependence probe: my subset merge plus closure on the max-D_c,≥2 states (L34 B0N-greedy steps 12–16), the L48 lineage, and the best-candidate states, with S2 recomputed. Known risk: line 48 has S2 maxdepth 2 on my 55-cell certificate, but the restart seed certificate has 56 cells.
- (1) Read the math layer against the Python reference: fold, core_factor, depth, strict depth, and expandFactor (#6). Build both PR heads in isolation with b25 03da2f7. Then my own fuzz equivalence: strict depth and diagram statistics on restart states, sub-certificates, planted a⁵/b⁵ shields, empty conjugators and a small table; expandFactor/expand; the guard on every restart word. Run their pytest and ctest under capjob.

**Scope limits.** The fold and its correctness are the reviewed Python reference (PR #17 review); my S2 code shares that fold. Certificates are upper bounds, so a "no depth ≥ 2" result is a statement about the certificates examined, not about all diagrams of a word.
