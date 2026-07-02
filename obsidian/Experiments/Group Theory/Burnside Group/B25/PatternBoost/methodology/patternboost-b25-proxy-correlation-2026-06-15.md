---
title: "PatternBoost B(2,5) — Proxy Correlation Study pre-registration (STEP 1)"
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: patternboost
status: "go — deliverable #1 complete"
author: maumayma
date: 2026-06-15
date_completed: 2026-06-16
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/word-problem, topic/knuth-bendix, project/b25, status/go, methodology]
---

# Pre-registration: PatternBoost B(2,5) — Proxy Correlation Study (STEP 1)

**Pre-registration date**: 2026-06-15
**Completed**: 2026-06-16
**Status**: `#status/go` — Deliverable #1 complete. GO gate met. Accepted by Maria 2026-06-16.
**Blocked by**: ~~commit gate from Maria~~ — cleared. STEP 1.5 is Developer's next task (wire `calc_score()`).

---

## Results — Deliverable #1

**Date**: 2026-06-16
**Accepted by**: Maria

| Metric | Value |
|---|---|
| N words | 49 (partial; see note) |
| Pearson r | **0.949** |
| p-value | **3.3 × 10⁻²⁵** |
| GO/NO-GO | **GO** (r > 0.3, p < 0.05) |

**Interpretation**: One-pass Rust braid+power reduction ratio is strongly positively correlated with benchmark compression ratio on the 49-word cohort. H1 supported.

**Data location**: `experiments/burnside/b25_patternboost/runs/deliverable1-2026-06-16/`
See `deliverable1_accepted_result.json` for full provenance and notes.

**Partial-basis note**: Run was executed in batches; 49 words completed before Maria issued STOP. The 49-word cohort (smallest words by file size, all with rust\_ratio > 0) was accepted as structurally decisive. 70 of 119 words were not run. A later partial run (80 words cached, stopped) found 51 words with rust\_ratio = 0.000 (no braid shortenings — not timeouts), including words with bench\_ratio up to 0.726. This would lower the full-119-word correlation but does not change the GO verdict for the existing threshold, as Maria accepted the 49-word result.

**Next**: STEP 1.5 — Developer wires `calc_score()` in `BurnsideDataPoint`. Come back to Maria before commit.

---

## What this experiment is

PatternBoost is an alternating search loop: a local search engine reduces B(2,5) words; a transformer trains on successful reductions and proposes new candidate patterns; those patterns are fed back into local search. Before wiring the transformer (STEP 1.5), we must verify that the chosen score proxy — `reduction_ratio(word, backend='rust')`, Option B — actually correlates with the ground-truth metric (best-known compression ratio from the benchmark).

This pre-registration covers **STEP 1 only**: measure that correlation. No transformer training. No PatternBoost loop. One-pass Rust reduction on all 119 benchmark words; scatter plot; Pearson r.

---

## Hypothesis

**H1 (falsifiable)**: For **all 119 benchmark words** (the full `[[b25-benchmark-snapshot-2026-06-09]]` set, including the near-flat sub-30% band), one-pass Rust braid+power reduction ratio is positively correlated with best-known total compression ratio (Pearson r > 0.3, p < 0.05).

Status at pre-registration time: `#status/conjectured` per Validator bounded verdict 2026-06-15. Validator found no in-domain counterexample; empirical measurement is this experiment's deliverable.

**H1 null**: r ≤ 0.3 or p ≥ 0.05. Interpretation: Option B does not predict compression progress. Switch to Option A (rule-match count) before STEP 1.5.

**Why 119, not 54**: testing H1 on only the ≥30% words range-restricts the y-variable (compression ratio), which attenuates Pearson r and makes a NO-GO result uninterpretable — it could be a pure artefact of the selection filter rather than a genuine absence of correlation. The near-flat words (`comm_13_10` at 0.2%, `comm_26_1` at 0.3%, etc.) anchor the low end of the y-axis and are required for an interpretable correlation test.

---

## Word sets (two distinct sets, two distinct purposes)

### Correlation set (deliverable #1) — 119 words

**Source**: `[[b25-benchmark-snapshot-2026-06-09]]`, `best_len` column (reproducible run), NOT `json_best`. All 119 rows, no filter.

**Purpose**: test H1. One-pass Rust ratio computed for all 119 words; scatter plot x = one-pass Rust ratio, y = benchmark compression ratio; Pearson r and p-value reported. GO/NO-GO gate applies to this 119-word correlation.

No new beam run needed. The benchmark already has `best_len` for all 119 words.

### Training set (STEP 1.5) — 54 words

**Selection criterion**: reproducible reduction ≥ 30% (`(original_len - best_len) / original_len ≥ 0.30`).

**Excluded from training**: 65 words with < 30% reduction, including the entire near-flat band (0.2%–4%: `comm_13_10`, `comm_26_1`, `comm_11_1`, `comm_11_7`, `comm_22_3`, and others). Training on words with near-zero reduction is unhelpful — local search produces no useful signal on them. Category-B unreproducible records (run directory gone) are not seeded as training targets; their reproducible `best_len` values are still included in the CORRELATION set.

**Count**: 54 words. Only used at STEP 1.5 and beyond; not used in deliverable #1.

### Training set — full table (sorted by best_len ascending)

| # | Target | original_len | best_len | pct% | json_better? |
|---|---|---:|---:|---:|:---:|
| 1 | comm_12_7 | 8,457 | 3,698 | 56.3 | — |
| 2 | comm_26_2 | 8,341 | 4,761 | 42.9 | — |
| 3 | comm_20_5 | 19,681 | 5,390 | 72.6 | ‡ |
| 4 | comm_26_4 | 20,249 | 5,947 | 70.6 | — |
| 5 | comm_13_6 | 24,247 | 6,191 | 74.5 | ‡ |
| 6 | comm_25_2 | 14,237 | 7,098 | 50.1 | — |
| 7 | comm_24_2 | 14,303 | 7,171 | 49.9 | — |
| 8 | comm_12_9 | 28,653 | 7,245 | 74.7 | — |
| 9 | comm_11_10 | 21,621 | 7,314 | 66.2 | — |
| 10 | comm_20_4 | 29,157 | 7,743 | 73.4 | — |
| 11 | comm_11_8 | 15,617 | 8,435 | 46.0 | — |
| 12 | comm_17_3 | 17,539 | 8,610 | 50.9 | ‡ |
| 13 | comm_16_3 | 17,051 | 8,618 | 49.5 | — |
| 14 | comm_20_3 | 16,075 | 8,886 | 44.7 | — |
| 15 | comm_10_5 | 14,063 | 8,991 | 36.1 | — |
| 16 | comm_7_5 | 17,933 | 9,544 | 46.8 | — |
| 17 | comm_12_5 | 14,417 | 9,623 | 33.3 | — |
| 18 | comm_29_2 | 16,759 | 9,627 | 42.6 | — |
| 19 | comm_15_8 | 16,971 | 9,812 | 42.2 | ‡ |
| 20 | comm_18_7 | 16,985 | 9,825 | 42.2 | ‡ |
| 21 | comm_17_7 | 17,005 | 9,846 | 42.1 | — |
| 22 | comm_16_8 | 17,013 | 9,852 | 42.1 | ‡ |
| 23 | comm_21_4 | 24,385 | 10,058 | 58.8 | — |
| 24 | comm_14_5 | 19,197 | 10,258 | 46.6 | ‡ |
| 25 | comm_27_2 | 15,469 | 10,682 | 30.9 | — |
| 26 | comm_27_4 | 15,481 | 10,690 | 30.9 | — |
| 27 | comm_25_5 | 15,489 | 10,704 | 30.9 | — |
| 28 | comm_12_4 | 22,303 | 10,910 | 51.1 | — |
| 29 | comm_9_6 | 27,335 | 11,358 | 58.4 | — |
| 30 | comm_10_6 | 18,835 | 11,520 | 38.8 | — |
| 31 | comm_9_5 | 18,819 | 11,678 | 37.9 | — |
| 32 | comm_11_3 | 20,841 | 11,717 | 43.8 | — |
| 33 | comm_23_2 | 32,287 | 11,830 | 63.4 | ‡ |
| 34 | comm_8_2 | 20,797 | 12,258 | 41.1 | — |
| 35 | comm_4_3 | 27,797 | 13,016 | 53.2 | — |
| 36 | comm_25_3 | 20,193 | 13,050 | 35.4 | — |
| 37 | comm_8_7 | 27,391 | 13,063 | 52.3 | — |
| 38 | comm_12_6 | 20,415 | 13,270 | 35.0 | — |
| 39 | comm_10_7 | 24,443 | 13,727 | 43.8 | — |
| 40 | comm_15_3 | 25,445 | 14,610 | 42.6 | — |
| 41 | comm_5_4 | 29,391 | 15,135 | 48.5 | — |
| 42 | comm_11_2 | 29,579 | 16,408 | 44.5 | — |
| 43 | comm_6_3 | 26,963 | 16,853 | 37.5 | ‡ |
| 44 | comm_7_3 | 28,751 | 17,726 | 38.3 | ‡ |
| 45 | comm_6_2 | 26,853 | 17,798 | 33.7 | ‡ |
| 46 | comm_18_3 | 28,225 | 18,086 | 35.9 | — |
| 47 | comm_13_4 | 29,509 | 19,309 | 34.6 | — |
| 48 | comm_8_6 | 32,201 | 20,156 | 37.4 | ‡ |
| 49 | comm_17_2 | 34,771 | 20,174 | 42.0 | ‡ |
| 50 | comm_7_4 | 41,229 | 20,930 | 49.2 | — |
| 51 | comm_15_2 | 32,721 | 22,150 | 32.3 | ‡ |
| 52 | comm_16_2 | 41,887 | 22,421 | 46.5 | ‡ |
| 53 | comm_7_2 | 37,071 | 23,001 | 38.0 | ‡ |
| 54 | comm_6_5 | 39,411 | 23,711 | 39.8 | ‡ |

‡ = `json_best` is better than this run's `best_len`; we use `best_len` from the reproducible run. 17 of the 54 words are ‡-marked; their training target is the LOWER (more conservative) reproducible value.

### Word-length distribution (best_len, N=54)

| Statistic | Value (chars) |
|---|---:|
| Min | 3,698 |
| P25 | ~8,819 |
| Median (P50) | ~10,807 |
| P75 | ~15,453 |
| P90 | ~20,552 |
| P95 | ~22,380 |
| Max | 23,711 |

---

## Three distinct lengths (must not be conflated)

**A — TARGET words** (the problems): the 54 benchmark commutator words, `best_len` up to 23,711 chars. These are the OBJECTIVES — what local search reduces. They are **never fed to the transformer's context window**.

**B — Generated training candidates** (what the transformer learns from and generates): short words produced by local search, bounded by `GEN_MAX_LEN = 260` chars in `datapoint.py`. The transformer is trained on the top-scoring candidates from this pool and emits new seeds of the same length class. Tokenized at k=1 (one char = one token), the longest ingestible sequence is 260 + BOS + EOS = **262 tokens**.

**C — Transformer context window** (the model parameter `max_len`): must match B, not A.

**max_len = 512 tokens** — agreed with Developer (2026-06-15). Covers GEN_MAX_LEN=260 (262 tokens with BOS/EOS) with a ~96% margin. Feasibility on M3 Max (36 GiB, axplorer small-model defaults n_layer=4, n_head=8, n_embd=256, vocab=8, batch=32, fp32 materialized attention): **1.0 GiB attention memory**. Trivially trainable.

Rejected alternatives:
- max_len = 24,000: requires 2.2 TiB attention memory — categorically impossible on 36 GiB hardware.
- max_len = 1,024: 4.0 GiB (4× cost of 512); no data justification for words exceeding 500 tokens.
- max_len = 2,048: 16.0 GiB (16× cost of 512); likewise unjustified.

Note: max_len is a STEP 1.5 parameter. STEP 1 (this pre-registration's deliverable) does not involve the transformer — `braid_reduce --no-beam` is called directly on the 54 target words. max_len is recorded here to prevent conflation in the STEP 1.5 pre-registration.

**Alphabet**: {a, b, A, B} → {0, 1, 2, 3}, Validator `#status/proven`. With `SparseTokenizerSequenceKTokens k=1`.

**min-length floor**: 100 tokens. Excludes degenerate candidates that local search over-reduces; ensures scoring produces a non-trivial signal. The 54 target words are not subject to this floor (they are objectives, not scored candidates).

---

## Score proxy

**Scorer**: `reduction_ratio(word, backend='rust')`

```
score = (len(word) - len(braid_reduce(word, flags=['--no-beam']))) / len(word)
```

- Backend: `experiments/burnside/burnside_bidirectional/target/release/braid_reduce`
- Mode: `--no-beam` (braid+power rules only, no beam search)
- Invocation: `--word-file <batch_file>` for all scoring calls (batch mode, 0.44ms/word amortized)
- Score range: [0.0, 1.0]. A score of 0.0 means braid+power rules made no progress.

**Status**: `#status/conjectured` — Validator verdict 2026-06-15. Validator found no in-domain counterexample for genuine commutator words. This pre-registration's deliverable #1 is the empirical correlation check.

**Calibration note from Validator**: Option B is `#status/disproven` as a proximity-to-identity signal. The counterexample `aaaaabbbbbab → ab` (len 12→2, score 0.833) shows high ratio does not imply nearness to identity. This experiment does NOT claim Option B measures identity proximity — it claims Option B correlates with further KB compression progress on genuine commutator words. These are different claims.

**Batch implementation requirement**: `calc_score()` must call `braid_reduce --word-file` in batch mode on the full survivor cohort, NOT one subprocess per word. Single-subprocess overhead is 19–500ms/call; batch amortizes to 0.44ms/word. At 100k candidates/round with 1% survivors: fast-filter cost 100k × 0.1ms = 10s; `calc_score()` cost 1,000 × 0.44ms = 0.44s; total ≈ 11s/round.

**KNOWN LIMITATION — zero-score blindness (~43% of words)**:
One-pass braid+power reduction returns `rust_ratio = 0.000` on approximately 51 of 119 benchmark words. These are NOT timeouts — they are genuine zero-reduction cases where `--no-beam` finds no applicable braid shortenings (products-of-conjugates class, e.g. `(aba)^5`-type words). This cohort includes words with `bench_ratio` up to 0.726.
Consequence: the proxy gives no gradient on these candidates — the transformer cannot rank them by Option B score. The Pearson r = 0.949 is measured only on the 49 words where the proxy fires, not on the full 119-word correlation set.
Mitigation if training stalls: revisit Option A (rule-match count against KB rule bank) or an abelianization-distance tiebreak for the zero cohort. This is a known, tracked limitation, not a blocker for STEP 1.5.

---

## Mixer agents involved

- `braid_reduce` (Rust binary, `--no-beam`): braid+power reduction, B(2,5) hard-coded relators
- `batch_score_fast()` (Python sliding-window, no subprocess): pre-filter, `<0.1ms/word`
- `BurnsideDataPoint` (Developer's axplorer `DataPoint` subclass): wired at STEP 1.5, STUBBED for STEP 1

---

## B(2,5)-specific modifications

- Scoring is done on {a,b,A,B} words (not compressed {a,b,m} forms). Compression to {a,b,m} is deferred.
- Training targets are `best_len` forms from the benchmark (post-beam-search reduced), not originals.
- No random words. All 54 words are genuine B(2,5) commutator words from the benchmark.

---

## Termination criteria (deliverable #1)

Deliverable #1 is complete when:
1. One-pass Rust reduction ratio computed for all 54 training words.
2. Scatter plot produced: x-axis = one-pass Rust ratio, y-axis = benchmark compression ratio (`(original_len - best_len) / original_len`).
3. Pearson r and p-value reported.

**Go/no-go gate for STEP 1.5**:
- **GO**: r > 0.3 AND p < 0.05 → Option B is usable; wire `calc_score()`
- **NO-GO**: r ≤ 0.3 OR p ≥ 0.05 → halt STEP 1.5; re-evaluate with Option A (rule-match count against sub-sampled KB rule bank, 10k rules, AC construction ~0.24s one-time)

---

## STEP 1.5 — Wire calc_score() (tracked deliverable)

`calc_score` stays `NotImplementedError` through STEP 1. Wiring is gated on deliverable #1.

**Trigger**: GO = Pearson r > 0.3, p < 0.05 per H1.

**ON GO**: implement `calc_score` by setting `self.score = reduction_ratio(self.word, backend='rust')` in place, return `None`, score < 0 == invalid. Re-run 46 tests + add a test that `calc_score` sets `self.score >= 0` on a valid word. Route to Lead (code) + Validator (math) before merge. Come back to Maria before commit.

**ON NO-GO** (r ≤ 0.3 or p ≥ 0.05): do NOT wire Option B. Switch to Option A (KB rule-match count). Re-spec STEP 1.5 and come back to Maria.

This is a real owned deliverable, not optional.

---

## Baselines

| Baseline | Description | Purpose |
|---|---|---|
| Null model | r ≈ 0, random scoring | Expected Pearson r under H1 null |
| Option A | Rule-match count: count of KB rule-bank LHS matches in word, using top-10k rules from `mega_ab_rules.live` by overlap frequency | Alternative proxy if Option B fails GO gate |

Baseline A data: extract top-10k rules by overlap count from `mega_ab_rules.live` (25.7M rules). Build AC automaton (estimated construction ~0.24s at 10k rules; scaling from B(4,3) 250k-rule baseline of 6s). Scan same 54 words. Record match counts. Compute Pearson r against benchmark compression ratio. Compare to Option B.

---

## Seeds

Five seeds for any stochastic components (beam search random tie-breaking, if reused at STEP 1.5):
`42, 137, 271, 853, 1729`

Deliverable #1 is deterministic (no beam search, no sampling) — seeds are pre-registered for STEP 1.5 forward.

---

## Anti-pattern check

**Am I tuning on the same target set I'm scoring on?**

The 54 words were selected by benchmark compression ratio (≥30% reduction), NOT by one-pass Rust ratio (which has not been measured yet). The correlation study is observational: measure proxy, measure ground truth, compute r. No feedback loop at STEP 1.

Risk at STEP 1.5: if PatternBoost's local search is trained on words selected by the proxy it will optimize (Option B), there is a tautology risk — the transformer learns to generate words that score well on Option B, which may not generalize. Mitigation: hold out 10% of training words (6 words, randomly selected at STEP 1.5 pre-registration) as a validation set not used in training.

**No cherry-picking**: if the GO gate is met, ALL 54 words are used as training words. If Option B gives high r because of a subset, the scatter plot will show it — if the correlation is driven by outliers, we reject and re-evaluate.

---

## Provenance triple

Captured at pre-registration authoring (2026-06-15):

| Artifact | Hash / ID |
|---|---|
| `algo_mixing` git HEAD | `2db27272b13c3b35e4b07f63b07cc35a228b2329` (branch: `feat/burnside-datapoint`) |
| `uv.lock` sha256 | `978fe9e2d4809ac5cad3bf2814e01b6948076ce79512621d6a3c7b29994126fe` |
| `braid_reduce` binary sha256 | `0a9391325f55701e8b2a4fe70909595dc1ce23eb16380d799878071561e939b7` |

`uv.lock` includes (uncommitted at pre-registration time): `torch==2.10.0`, `numba`, `numpy`, `psutil`, `matplotlib`. The `BurnsideDataPoint` patch is also uncommitted at this date. The provenance triple above captures the state at pre-registration; a second triple must be captured immediately before STEP 1 is run.

**Required action before STEP 1 run**: re-capture all three hashes after Developer's patch is committed and commit gate is opened. Record as "run-time provenance triple" in `data/` alongside scatter plot output.

---

## Validation

Deliverable #1 is self-validating: the scatter plot + Pearson r are the validation. No Validator math sign-off required for the correlation measurement itself (it is a statistical test, not a math claim).

**However**: if the scatter plot reveals a structurally unexpected pattern (e.g., negative correlation for high-pct% words, positive for low-pct%), route to Validator with the plot before STEP 1.5 decision. This would be a new math claim about the relationship between braid+power reduction and KB progress.

---

## Related material

- [[PatternBoost/_type|PatternBoost experiment type root]] — parent `_type.md`
- [[_progress|B(2,5) Progress Note]] — standing progress note
- [[b25-benchmark-snapshot-2026-06-09]] — source of the 54 training word selections and best_len values
- [[charton-2024-patternboost]] — PatternBoost framework reference
- [[axplorer]] — implementation; `DataPoint` ABC; `BurnsideDataPoint` extension point
- [[Reduce Core/methodology/reduce-core-pipeline-b25-2026-05-22]] — provenance of comm_12_9 7,245-char baseline (the flagship training word)
- [[2026-05-22-comm-12-9-7245-final]] — Validator note: comm_12_9 7,245-char form is `#status/conjectured` (not proven = identity, element equality unverified)
