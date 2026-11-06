---
type: triage
date: 2026-11-05
author: Validator (asetlearning)
project: "[[project-b25-solver]]"
subject: "C1|6|1 break from the E0 smoke (T-blind, M2)"
---
# C1|6|1 smoke break: triage

Lead task: (1) replay the 9-cell certificate with own code; (2) provenance: T-blind used no challenge-gen recipe or certificate of C1|6|1, no leak via a scorer; (3) route math (u from the blind pool, group distance hit, R2.5 on the cyclic reduction of r u^-1 z' reaching empty); (4) bench verification through the solver contract CLI. Verdict note: [[2026-11-05-b25-solver-c1-6-1-smoke-break-check]].

**Step 2.5.** Target object: B(2,5) triviality of the registry word, certified by the L0 definition (free-group identity with literal fifth powers): the replay is on the target. Provenance and route claims are about code and data flow (read the code, check the artefacts), not about group theory.
