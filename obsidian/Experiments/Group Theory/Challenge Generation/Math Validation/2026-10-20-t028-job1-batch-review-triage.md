---
type: triage
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 job 1: review of the batch before job 1 (hard caps, gate and early stop, C++ CL in the gate, recovery-attack fix, R-trace wiring, canonical R tie-break)"
---
# T-028 job 1 batch: triage

Developer request, handed over at Lead's request (2026-10-20); replies via Lead. Brief: `Developer/2026-10-20-t028-job1-review-handoff.md`. Review note: [[2026-10-20-t028-job1-batch-review]].

**Code:** b25 `t028-pilot` (de13bee, 07866e3, 8753a23; pin commit 138fa4a = tcgraph f4b7771), tcgraph `feat/t028-pilot-cpp` (5cd134f, f94150f, bc6b97f, f4b7771).

**Asks and method:**
1. **Hard caps:** read `caps.py`, `pilot.py`; can a killed word leave a wrong archive record?
2. **Gate and early stop:** read `gates.py`, `chain.py`, `heldout.py`, `verify.py`, `ladders.py`; check that no verdict or level definition changed (S1-each all-or-nothing, T3u = L1-r25 + S1-each, S2-chain only after S1-each), and that early stop cannot turn "not run" into "resilient".
3. **C++ CL in the gate:** read `closure_run.cpp` and the one-byte store; compare verdicts with the Python closure on my own words.
4. **Recovery-attack fix:** read `recovery.py`; soundness of acceptance (verification is independent of ranking).
5. **R-trace wiring:** read the binding and `verify.r_step_check`; replay the identity independently on chain words; the platform rule (an R step from another platform accepted by its trace).
6. **Canonical tie-break:** read the diff; rerun my 27,328-word R-trace equivalence and identity on f4b7771; count changed outputs against 63564c3; speed.

Runs under capjob (2 GB / 2 CPUs), one at a time; Python with `-I -S` or the bare uv interpreter (the t018 venv hook).

## Addendum 2026-10-21: handoff section 7 (A_R, r10 frozen)

The handoff gained section 7 at 02:19 on 2026-10-21, after my verdict, which said "A_R is not built". This addendum corrects that. Lead's request of 2026-10-21 puts this section ahead of the r11 review.

**Method.**
- Read `ar.py`, `ar_control.py`, `ar_tune.py`, `tests/test_ar.py` and the staged diffs of `heldout.py`, `seeds.py` and `construct.py`, against r10 §7.0d.
- The acceptance is the proof step, so the review centres on `verify` and the frames of g and the cells.
- The C++ `approx/` kernels only propose candidates and are not on the soundness path. I did not review them.
- No runs.

## Re-check of the fixes (2026-10-21)

Developer request. The fixes are in b25 df02191 (Lead's commit; tcgraph pin 3673013).

**Method.**
- Read the diff 138fa4a..df02191 for `pilot.py`, `report.py`, `heldout.py`, `gates.py`, `recovery.py`, `ar.py` and `solvers/core.py`.
- Test `PairDecoder` (scratch, capjob 2 GB / 1 CPU, `python -I`) on random free bases. Recovering t from φ(t) checks the fix for deviation 1 directly.
