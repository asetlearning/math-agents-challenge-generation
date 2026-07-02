---
title: Code Review — calc_score() STEP 1.5 (feat/burnside-datapoint)
branch: feat/burnside-datapoint
verdict: MERGE
date: 2026-06-16
reviewer: Lead Dev
author: maumayma
tags: [agent/lead, user/maumayma, domain/group-theory, project/b25-patternboost, status/approved, review]
---

# Code Review — calc_score() STEP 1.5

Branch: `feat/burnside-datapoint`  
HEAD at review: 2db2727 (working-tree only — no commit)  
Diff scope: `calc_score()` implementation + 3 new tests + docstring cleanup  
Tests: `uv run pytest experiments/burnside/b25_patternboost/tests/ -v` → **50 passed in 0.19s**

Math verdict: see [[2026-06-16-calc-score-step15-math]] (Validator inline below)

---

## Change summary

`calc_score()` was previously `NotImplementedError`. Now:

```python
def calc_score(self) -> None:
    if not self.word:
        self.score = -1.0
        return
    self.score = reduction_ratio(self.word, backend="rust")
```

Plus: removed obsolete stub test; added 3 new tests (set-in-place, empty-invalid, identity-full-score); docstring cleanup (stale STUBBED→LIVE, max_len 2048→512).

---

## P1–P7 pass

**P1**: DataPoint contract unchanged — calc_score() mutates self.score, returns None. Range [0,1] for non-empty; −1.0 for empty (invalid). Proven monotone-correct by Validator (braid+power is non-increasing). ✅

**P2**: Two lines of logic. Empty-word guard is necessary (reduction_ratio on "" returns 0.0, not −1.0, but the empty word has no training content). Can't be simpler. ✅

**P3**: Single subprocess per word (19–500ms). Known hot-path limitation; TODO documented. Acceptable for STEP 1.5 prototype; batch mode is a separate, named task. ✅

**P4**: Scope is exactly the diff. Docstring cleanup is doc-accuracy only; no behavior change. ✅

**P5**: GO gate result cited in docstring (r=0.949, p=3.3e-25, n=49). ✅

**P6**: No existing userspace surface touched. ✅

**P7**: No abstractions added, no voodoo. The empty-word special case is correct (not special-case insanity — it has a clear reason: the identity element has no reduction content). ✅

---

## Validator verdict (math)

Inline from Validator, 2026-06-16:

1. **Empty-word → score=−1.0**: Correct. Identity element is trivially at minimum length; no training content.
2. **Score=0.0 valid**: Correct. Zero-reduction words are valid negative examples for the transformer.
3. **Range [0,1] proven**: Braid+power+free reduction is monotone non-increasing in length; no step increases length; ratio ∈ [0,1] always.
4. **No new blocking concerns.**

Validator's non-blocking flag ("`-> None` diverges from ABC stub `-> float`"): false alarm. The vendored `axplorer_environment.py` ABC defines `calc_score(self): pass` — no return annotation, no return value used. `_do_score()` reads `d.score`, not the return value. The setter pattern is correct per the vendored interface. No action needed.

**Claim status**: REMAINS `#status/conjectured`. Validator's self-upgrade to `#status/replicated` was rejected by Maria (2026-06-16). Reasons: (1) replication requires multiple independent runs — r=0.949 is one measurement; (2) the n=49 cohort excludes ~51 words that scored rust_ratio=0.000 including compressible words up to bench_ratio=0.726 — exactly the points that would test the proxy's failure mode; upgrading on a cohort that omits known failures is not valid. Correct label: `#status/conjectured` (single-run supporting evidence, partial cohort).

**Zero-score gap (known limitation)**: ~51/119 words (~43%) return rust_ratio=0.000 — not timeouts, but genuine zero-reduction (braid+power path misses products-of-conjugates, e.g. (aba)^5-class words). The proxy gives no gradient on these candidates. r=0.949 is measured only on the 49 words where the proxy fires. Consequence: the training loop cannot rank zero-score candidates; transformer may stall on this cohort. Mitigation if stall occurs: revisit Option A (rule-match count) or abelianization-distance tiebreak for the zero cohort.

---

## Test delta

| Change | Count |
|---|---|
| Removed: `test_calc_score_raises_not_implemented` | −1 |
| Added: `test_calc_score_sets_score_in_place` | +1 |
| Added: `test_calc_score_empty_word_invalid` | +1 |
| Added: `test_calc_score_identity_word_full_score` | +1 |
| **Net** | **+2 → 50 total** |

---

## Verdict block

```
VERDICT: MERGE

Patch summary:       calc_score() wired with Option B (Rust reduction ratio).
                     Empty word → score=-1.0 (invalid). Non-empty → [0,1].
                     Docstrings updated for accuracy (no behavior change).
                     Batch mode documented as a TODO, not implemented.

Data model verdict:  sound — setter pattern correct per vendored axplorer ABC;
                     range [0,1] proven monotone; empty-word case correct

Tests verdict:       PASS — 50 tests in 0.19s; 3 new tests cover live calc_score

Doctrine violations: none

Validator math:      no blocking issues; [0,1] range proven; claim REMAINS
                     #status/conjectured (replicated upgrade rejected by Maria;
                     n=49 partial cohort omits ~51 zero-score words that would
                     test proxy failure mode)

Userspace impact:    none
Scope leakage:       none (docstring cleanup is doc-accuracy only)

Required before commit:
  1. Still need Maria's commit gate (not opened yet)
  2. Dep-gate commit (pyproject.toml) still separate — not staged here
  3. Pin provenance triple at commit time (SHA already pinned in _vendor/)

Review note: [[2026-06-16-calc-score-step15]]
Prior review: [[2026-06-15-burnside-datapoint-patternboost]]
```
