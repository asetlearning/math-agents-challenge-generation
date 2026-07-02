---
title: Code Review — BurnsideDataPoint (feat/burnside-datapoint, revision 2)
branch: feat/burnside-datapoint
verdict: MERGE (DataPoint skeleton, calc_score stubbed)
date: 2026-06-15
reviewer: Lead Dev
author: maumayma
tags: [agent/lead, user/maumayma, domain/group-theory, project/b25-patternboost, status/approved, review]
---

# Code Review — BurnsideDataPoint (revision 2)

Branch: `feat/burnside-datapoint`  
HEAD at review: 2db2727 (nothing committed; patch is working-tree only)  
Files reviewed: `experiments/burnside/b25_patternboost/datapoint.py` (422 lines), `_vendor/axplorer_environment.py` (172 lines), `tests/test_burnside_datapoint.py` (315 lines)  
Tests run: `uv run pytest experiments/burnside/b25_patternboost/tests/ -v` → **46 passed in 0.15s**

Math-layer verdict: see [[2026-06-15-patternboost-datapoint-math-review]]

---

## Doctrine Pass (P1–P7)

### P1 — Data structure is the design ✅

DataPoint contract is clear: `word: str`, `score: float` (−1 = unscored), `features: str` (canonical dedup key). The three abstract methods (calc_score, calc_features, local_search) all mutate self; no return values. `_batch_generate_and_score` returns empty list while score is always −1 (stub active) — this is correct and documented; replaced by the `generate()` classmethod for STEP 1. No mixer protocol touched.

### P2 — Boring code is usually correct ✅

`_free_reduce`: simple stack-based inverse cancellation. `_power_reduce`: string replacement fixpoint. `_braid_reduce`: sliding window over alternating runs, single non-trivial but necessary formula. `_single_rust_reduce`: subprocess with tempfiles (unavoidable for the binary's `--word-file` interface). `BurnsideEnvironment`: one-liner `data_class = BurnsideDataPoint` — correct for STEP 1 (DataPoint only).

One note: `local_search(improve_with_local_search: bool = False)` adds a default the ABC lacks. Compatible (axplorer calls it with explicit keyword); makes no-arg calls safe. Not a violation.

### P3 — Hardware truth ✅

Hot path here is training throughput. Python reducer: <1ms/word. Rust subprocess: 19–500ms/word. Neither is in the KB inner loop — this is training-phase batch cost. Temp-file-per-call pattern is the correct approach for the current binary (no batch mode; source confirmed at `braid_reduce.rs:496–497`). No per-tick allocations in the mixer scheduler.

### P4 — Surgical changes only ✅ (with one note)

All new files are under `experiments/burnside/b25_patternboost/`. Zero touch to existing code. Clean.

**One note (not Developer's doing):** `pyproject.toml` has uncommitted additions of `torch==2.10.0`, `numba`, `numpy`, `psutil`, `matplotlib`. These are pre-existing working-tree changes (Maria's env provisioning, confirmed). They must NOT be staged in the STEP 1 DataPoint commit — they require a separate human-gated dep-gate commit. See commit boundary decision below.

### P5 — Show me the code, show me the numbers ✅

No cooperation-gain claim made. `calc_score()` is explicitly stubbed (`NotImplementedError`). Candidate proxy `reduction_ratio()` is labeled "NOT wired into calc_score(), provided for Validator evaluation." Parity characterization test documents the divergence with actual numbers (3/20 random words agree on reduced length; mean Δ = −4.40 chars favoring Rust). This is the correct approach for an unresolved math question.

### P6 — Don't break userspace ✅

- `mixer_core.Agent` Python ABC: not touched
- JSON-lines protocol: not touched
- pyo3 bindings: not touched
- `Scheduler`/`Transform` Python API: not touched
- `runs/` layout: not touched
- KBMAG file formats: not touched

All new; nothing modified.

### P7 — Bogus-shit detector ✅

No enterprise sludge, no brain-damaged API, no voodoo. `tokenize()`/`detokenize()` on DataPoint is noted as "experiment extension" with clear comment that it belongs in `tokenizers.py` in full axplorer integration — acceptable for STEP 1, correctly labeled. Subprocess timeout 30s is conservative (cited max ~500ms/word), harmless for prototype.

---

## Validator verdict summary

From [[2026-06-15-patternboost-datapoint-math-review]]:

| Item | Verdict | Blocks STEP 1 commit? |
|------|---------|----------------------|
| Score proxy Option B ↔ proximity to identity | #status/disproven | No — calc_score() already stubs to NotImplementedError; proxy is gated |
| Python coverage gap ("slightly less accurate") | #status/disproven | No — documented as known limitation; code uses Rust for final scores |
| Non-abelian inverse formula | #status/proven | n/a |
| Tokenization {a,b,A,B}→{0,1,2,3} | #status/proven | n/a |

Score proxy (Item 1) blocks the proxy implementation PR (STEP 1.5), not this DataPoint skeleton commit. B25 sent a narrower question: "does Option B produce a training signal correlated with further KB progress on genuine B(2,5) commutator words?" — Validator responded during this review session:

**#status/conjectured** for Option B (Rust backend) on genuine commutator words. No counterexample known. Validator: "No math-layer reason to block Step 1." Practical guard: log Rust vs Python score divergence for actual training words during data collection. Python-path scoring remains an additional uncertainty layer; Rust backend is required for training signal.

Both math-layer verdicts are now positive for STEP 1 DataPoint commit.

---

## Required before staging (pre-commit checklist)

1. **Pin axplorer commit SHA in `_vendor/axplorer_environment.py` header.** Currently says "Fetched: 2026-06-15 from branch `main`" with a TODO. Run `git ls-remote https://github.com/AxiomMath/axplorer HEAD` or equivalent to get the exact SHA and fill in the TODO comment. Reproducibility requires it.
2. **Exclude `pyproject.toml` and `uv.lock` from STEP 1 staging.** Those go in a separate dep-gate commit (see below).

Both are trivial (one shell command + one line edit). Lead handles #1 at commit ritual time.

---

## Commit boundary recommendation (for Maria)

**STEP 1 commit** — DataPoint skeleton only:
```
experiments/burnside/b25_patternboost/__init__.py
experiments/burnside/b25_patternboost/datapoint.py
experiments/burnside/b25_patternboost/_vendor/axplorer_environment.py
experiments/burnside/b25_patternboost/tests/test_burnside_datapoint.py
experiments/burnside/b25_patternboost/tests/__init__.py  (if present)
```

**Separate dep-gate commit** (human gate, after Maria approves):
```
pyproject.toml   (+torch==2.10.0, numba, numpy, psutil, matplotlib)
uv.lock
```

Rationale: the dep additions are not needed to run the current tests (torch is not imported by datapoint.py or its tests). They belong in their own commit with explicit Maria approval so the dep history stays traceable.

---

## Outstanding gates (not blocking STEP 1 DataPoint commit)

- B25 proxy narrow question → Validator (in-flight)
- B25 max_len lock (blocked on Developer confirming input alphabet and initial word set — B25's current recommendation is 2048; needs Developer confirmation)
- Binary batch mode decision (needed before training loop, not before DataPoint commit)
- STEP 1.5 (proxy implementation) → separate PR after B25 + Validator sign-off

---

## Verdict block

```
VERDICT: MERGE (DataPoint skeleton — calc_score stubbed, proxy gated)

Patch summary:       BurnsideDataPoint subclassing real axplorer DataPoint ABC
                     (vendored from AxiomMath/axplorer, stdlib-only, zero new
                     deps). calc_score() raises NotImplementedError — proxy
                     decision correctly gated on B25 + Validator. Python and
                     Rust reduction paths both present; divergence documented
                     in tests. 46/46 tests pass.

Data model verdict:  sound — word/score/features contract clean; ABC mutations
                     correct; _batch_generate_and_score empty-list behavior
                     while stub active is documented and replaced by generate()

Tests verdict:       PASS — 46 tests in 0.15s; includes ABC parity, tokenize
                     round-trip, stub assertion, parity characterization

Doctrine violations: none

Validator math items:
  - Score proxy (Option B ↔ proximity to identity): #status/disproven
    → NOT a blocker here (calc_score is stubbed); blocks STEP 1.5 proxy PR
  - Python "slightly less accurate" description: #status/disproven
    → documented; not a blocker (Rust used for final scores)
  - Non-abelian inverse formula: #status/proven
  - Tokenization: #status/proven

Unverified claims:   none remaining (all claims either proven, disproven with
                     correct code response, or explicitly deferred)

Userspace impact:    none — no existing surface touched

Scope leakage:       pyproject.toml (+torch/numba/numpy/psutil/matplotlib)
                     NOT Developer's; must be staged in a separate dep-gate
                     commit

Required before staging:
  1. Pin axplorer upstream commit SHA in _vendor/axplorer_environment.py
     header (trivial: one git ls-remote + one line edit)
  2. Exclude pyproject.toml + uv.lock from STEP 1 staging

Review note: [[2026-06-15-burnside-datapoint-patternboost]]
Math note:   [[2026-06-15-patternboost-datapoint-math-review]]
```
