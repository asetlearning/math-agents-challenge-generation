---
type: validation-triage
date: 2026-10-18
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-024: verify the best level-2 onion finals (rjob 20261018-000601-9e5902): L0, 2.5-reduced gate, S2 under flip rule (d) + bouquet control, cheaper certificate"
---
# Triage: verifying the best level-2 onion words

This is a Lead task (2026-10-18; the owner approved the T-024 next steps).

**Targets.** From `pilot_50.json` (b25 `3db063d`, section 10.3 of the T-024 note): the finals that are L1, pass the bouquet control, and have S2 depth 3–4.
- 9 B finals and 8 A finals, which are **12 distinct words** (5 seeds have the same word as their A and B final).
- Seeds (ds): 368(A), 160(B), 512(B), 566(B), 547(A,B), 781(B), 125(A,B), 665(A,B), 145(A), 94(A), 764(A,B), 707(A,B).
- Depth 4: ds 160 (B) and ds 665. ds 160's own cheap pipeline gives S2 depth 2, so it is the first word to watch.

**Blocker.** `pilot_50.json` stores the words and measures but **not the certificates**: neither the assembled level-2 cells nor the compressed cells.
- (b), the gate, and L1 need only the word, so they can be checked now.
- (a) L0, (c) depth under rule (d) plus the bouquet control, and (d) a cheaper certificate all need the certificate.
- Getting it means re-running the pilot's `run_seed` path (b25 `90bc1cb` + tcgraph `4390614`, seeded `default_rng(ds)`), checking that the reproduced word equals the stored one, and saving the cells. That needs a small driver.
- Cost: about 5.2 CPU-hours for the 12 seeds (the per-seed `sec` values), so it needs an rjob.
- Asked Lead (code needs approval; run over 2 h needs a plan).

**Plan once the certificates exist:**
- (a) Expand the certificate and compare with the word, with my own expander as well as the binding.
- (b) Two detectors: `power_gates` B, and my independent `pw.c` (`cyc_has_power_gt`, threshold > 2.5).
- (c) S2 and flip rule (d) with tcgraph `ca2ceb9`, plus the Python reference `strict_depth_flip.analyse_flip(rule='d')`; then the bouquet control (components' maximum depth).
- (d) `inverseCellReduce` and the certificate_reduction pipeline on the full certificate, then S2 / flip (d) / bouquet on the reduced one. The depth counts only if it survives.

Scope limits: these are depths of our certificates after our reductions, not of minimal diagrams. A cheaper certificate that the reducers do not find is not excluded.
