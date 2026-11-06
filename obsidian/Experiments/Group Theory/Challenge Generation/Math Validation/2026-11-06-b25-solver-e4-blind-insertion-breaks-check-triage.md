---
type: validation-triage
date: 2026-11-06
agent: Validator
---
# Triage: E4-blind-insertion-R breaks (60) and the algo-mixer break C3|6|21
Claim: 61 L0 certificates (free-reduced product of conjugates of literal fifth powers) of rev-4 registry words; 60 from the E4 run (51 M2 T-blind, 4 M2 v5, 5 loop after M2 R_emptied), 1 from the algo-mixer stage (certified row).
Model check (step 2.5): pure-Python free reduction in F_2 (the target object). No finite quotient.
Plan: (1) replay all 61 with own code against the registry-rev4-draft words; (2) ids are open candidates and not among the 7 rev-4 breaks; (3) bulk source integrity of the 8263 attack lines against m2_inputs (T-blind/v5 pool shape); (4) note scope. Not planned: re-running E4 or the mixer (compiled tcgraph_ext / reducer not here).
