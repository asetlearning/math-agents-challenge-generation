---
title: "Proxy Validation v4 — Stage 2b Results (Confirmatory: −Arm1 K=4 vs braid_reduce_delta)"
date: 2026-06-29
domain: group-theory
project: b25
experiment_type: proxy-validation
instance: B0-proxy-stage2b
author: maumayma
status: complete
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/proxy-validation, project/b25, status/complete, results]
---

# Proxy Validation v4 — Stage 2b Results

**Pre-registration**: [[methodology/proxy-validation-v4-stage2b-prereg-2026-06-29]] (AMENDED 2026-06-29: target respecced from Q5-distance to braid_reduce_delta; K=4 only)  
**Parent**: [[results/b0-proxy-v4-stage2-results-2026-06-29]] (Stage 2: anti-correlation discovery)  
**[CONDITIONAL: B₀ ≅ B(2,5) / Kourovka 11.48]**  
**GT label**: `d_Q5(1,π₅(g))` — Cayley distance in Q5 = B₀/γ₆ (order 5^10); quotient-GT, NOT B₀-GT; d_Q5 ≤ d_B₀ (reported as secondary reference; PRIMARY target = reducer_delta).

---

## §0 Target, Corpus, and Persist

**Primary target**: `reducer_delta = len(input_word) − len(braid_reduce(input_word))`.  
Reducer config: beam_width=4096, beam_secs=5, hard_timeout=20s, 3 concurrent workers.  
Rule bank: 31 GAP-verified seed rules (`b25_seed_rules_2026-06-25.kbprog`) + built-in braid shortenings (u^5=ε, valid in B₀ by definition). Rule provenance: clear (both classes B₀-valid).

**Corpus**: 440 targeted candidates, seed 20260630 (fresh, independent from Stage 2 seed 20260629).
- Category A: 220 [G,G] long words (len=30 or 50, abelianization=(0,0))
- Category B: 110 non-[G,G] long words (len=30 or 50)
- Category C: 110 short words (len=10–20)

**MANDATORY PERSIST (doctrine applied)**:
- 9.77M Q5 distance table: `runs/b25/proxy_validation_v4/stage2b/q5_dist_table.csv` — **214.2 MB**, 9,765,626 lines (header + all entries), BFS time 3780s = 63 min.
- Q5 pcps (power-conjugate presentation): `runs/b25/proxy_validation_v4/stage2b/q5_pcps.json` — 4.3 KB (generator images + all power/conjugate/conjugate-inverse relations, enables Python word evaluation without re-running BFS).
- BFS provenance: `runs/b25/proxy_validation_v4/stage2b/q5_bfs_provenance.json`

**Reducer provenance**: `runs/b25/proxy_validation_v4/stage2b/reducer_deltas_provenance.json`

### Corpus counts after GAP evaluation

| Category | Count |
|----------|-------|
| Total evaluated | 440 |
| Q5-invisible (d_Q5=0, excluded from correlation) | **0** |
| Stratum II (d_Q5>0, not [G,G]) non-geodesic | 198 |
| Stratum III ([G,G], d_Q5>0) non-geodesic — primary | **226** |
| All visible non-geodesic | 424 |
| All visible | 440 |

No Q5-invisible words this corpus (0/440 = 0%). All 440 words have d_Q5 > 0.

### Reducer outcome

| Stratum | n | Blind (Δ=0) | Blind% | Max Δ | Avg Δ |
|---------|---|------------|--------|-------|-------|
| Stratum III NG (primary) | 226 | **0** | **0.0%** | — | — |
| Stratum II NG | 198 | 10 | 5.1% | — | — |
| All visible NG | 424 | 10 | 2.4% | — | — |
| All 440 | 440 | 26 | 5.9% | 29 | 7.19 |

**Pre-run prediction of ~80% blind rate was REFUTED.** braid_reduce's generalized braid shortenings (broader than Arm 3's move set) reduce **94.1% of all words**, including **100% of [G,G] non-geodesic words** (0/226 blind on primary stratum). The target was non-degenerate across the full stratum, not a 20% subset. Reducer time: **0.8s total** for 440 words with 3 workers.

---

## §1 Main Results Table

GT column (secondary reference) = d_Q5(1,π₅(g)) on fresh corpus. Primary target = reducer_delta.

| Feature | Stratum III ρ vs reducer_delta | p-value | Top-decile lift | Pass (ρ≥0.20 OR lift≥1.25) | ρ vs d_Q5 (secondary) |
|---------|--------------------------------|---------|----------------|---------------------------|----------------------|
| **−Arm1 K=4** (periodicity-deficit) | **−0.358** | 3.1×10⁻⁸ | 1.000 | **FAIL** (anti-correlated) | −0.082 |
| **Compound** z(−K4)+0.5·z(first_nz_layer) | **−0.289** | 1.1×10⁻⁵ | 1.000 | **FAIL** (anti-correlated) | — |

Stratum III n = 226 (non-geodesic [G,G]-visible).

---

## §2 Hypothesis Verdicts

| ID | Hypothesis | Threshold | Result | Verdict |
|----|-----------|-----------|--------|---------|
| H6-1 | −Arm1_K4 ρ_III ≥ 0.20 vs reducer_delta | ρ ≥ 0.20 | ρ = **−0.358** (anti-correlated) | **FAIL** |
| H6-3 | Compound ρ_III > max(ρ(arm1b), ρ(pc)) | additive improvement | ρ = −0.289 (also anti-correlated) | **FAIL** |
| H6-2 (secondary, not primary target) | −arm1 ρ_III ≥ 0.30 on independent corpus vs d_Q5 | ρ ≥ 0.30 | ρ = **−0.082** (wrong sign, near zero) | **FAIL** |

---

## §3 Structural Interpretation

### F1: Target-proxy direction conflict

The root cause of both failures is a **structural conflict between proxy direction and target direction**:

- **−Arm1_K4** (periodicity-deficit): words with few u^5 patterns → high score → predicted "far from identity"
- **d_Q5**: Stage 2 confirmed ρ(Arm1, d_Q5) = −0.292 (periodicity-excess predicts LOWER d_Q5 → closer to identity). Sign consistent with −Arm1_K4 predicting farther-from-identity.
- **reducer_delta**: words with MANY u^5 patterns → braid shortenings fire → HIGH delta. So high periodicity-excess → high delta.
- Result: high periodicity-excess → close to identity (low d_Q5) AND easy to reduce (high delta). These are the SAME direction.
- Consequence: **−Arm1_K4 is anti-correlated with reducer_delta** (ρ = −0.358). Words the proxy says are "hard" (far from identity) are actually "easy" for braid_reduce (because braid_reduce is most effective ON words close to identity via braid shortenings).

**In short**: braid_reduce succeeds precisely on words that are CLOSE to identity (periodic structure). Words FAR from identity (no u^5 patterns, no obvious braid shortening) are both hard for braid_reduce AND predicted as "difficult" by −Arm1_K4 — but this means the proxy is correct about difficulty, just measured by the WRONG TARGET.

### F2: Stage 2 in-sample +0.33 does NOT replicate

The Stage 2 in-sample observation (−arm1_K4 ρ_III ≈ +0.33 vs d_Q5, doubly in-sample) is not confirmed on the fresh corpus:
- Fresh corpus: ρ(−Arm1_K4, d_Q5) = **−0.082** (stratum III, n=226)
- Stage 2 in-sample: ρ = +0.33 (on Stage 2 corpus, same data used to choose sign and K)
- These values have opposite sign and the CI for n=226 (±0.13) puts the fresh result consistent with zero, not with +0.33

The Stage 2 in-sample observation was a false positive from the doubly-in-sample design. −Arm1_K4 does NOT reliably predict d_Q5 on an independent corpus.

### F3: braid_reduce is highly effective on [G,G] random walks

0% blind rate on stratum III (226/226 words improved). The generalized braid shortenings in the Rust binary are much more powerful than Arm 3's bounded-descent move set (81% blind in Stage 2). This makes braid_reduce a practically useful reducer for random-walk [G,G] words, but means reducer_delta is NOT a good proxy for Q5 distance (because it measures braid-reduction potential, not identity distance).

### F4: Persisted Q5 table enables direct triage

The 9.77M Q5 distance table is now saved at `runs/b25/proxy_validation_v4/stage2b/q5_dist_table.csv`. For all future corpus words:
1. Load table once (214MB Python dict, ~30s)
2. Build Q5 group from pcps (`q5_pcps.json`, fast)
3. Evaluate each word in Q5 (O(|w|) per word using the collector)
4. Look up d_Q5 instantly

This eliminates the 62-min BFS cost for all future proxy experiments. **Direct d_Q5 triage is now cheaper than any proxy.**

---

## §4 Stage 1 / Stage 2 / Stage 2b Comparison

| Aspect | Stage 1 (B(3,3)) | Stage 2 (B₀/Q5) | Stage 2b (B₀/Q5, fresh) |
|--------|-----------------|-----------------|--------------------------|
| Target | d_Q5 (B(3,3)) | d_Q5 (B₀) | reducer_delta |
| Stratum III NG | 0/80 (all geodesic) | 324/343 | 226/226 |
| Arm 1 (excess) ρ III | NaN | −0.292 | +0.358 (vs delta) |
| Reducer blind % | — | 81% (Arm 3 proxy) | 0% |
| Fresh-corpus: ρ(−arm1, d_Q5) | — | N/A (in-sample) | **−0.082 (does not replicate)** |

---

## §5 Math Claims for Validator

None. Spearman ρ values are empirical statistics; the structural interpretation (braid shortenings effective on periodic words) is well-known B₀ theory, not a new claim. No routing required.

---

## §6 Open Questions → Lead/Maria

1. **Proxy retirement**: −Arm1_K4 as a proxy for d_Q5 is not confirmed. Q5 direct measurement (via persisted table) is more reliable. Should the proxy approach be retired in favor of direct d_Q5 triage?
2. **PatternBoost triage design**: if the goal is to identify "hard" B₀ words for PatternBoost, use d_Q5 directly from the table. But note: d_Q5 is itself a quotient distance (d_Q5 ≤ d_B₀). Farther in Q5 → farther in B₀ (by quotient-map inequality).
3. **Corpus design**: Stage 2b corpus (targeted [G,G] long words) gave different d_Q5 correlations than Stage 2's broader random corpus. Corpus design matters for which correlations appear.
4. **braid_reduce effectiveness**: 100% success on [G,G] random walks suggests braid_reduce (generalized) is a strong first-pass reducer for the PatternBoost loop, independent of any proxy.

---

## §7 Provenance Triple

| Field | Value |
|-------|-------|
| GAP BFS script | `experiments/burnside/b25/proxy_validation_v4_stage2b/stage2b_bfs_persist.g` |
| Reducer script | `experiments/burnside/b25/proxy_validation_v4_stage2b/stage2b_reducer.py` |
| Scorer script | `experiments/burnside/b25/proxy_validation_v4_stage2b/stage2b_score.py` |
| Run dir | `runs/b25/proxy_validation_v4/stage2b/` |
| Results CSV | `runs/b25/proxy_validation_v4/stage2b/results.csv` |
| Report JSON | `runs/b25/proxy_validation_v4/stage2b/report.json` |
| Q5 table (9.77M) | `runs/b25/proxy_validation_v4/stage2b/q5_dist_table.csv` (214.2 MB) |
| Q5 pcps | `runs/b25/proxy_validation_v4/stage2b/q5_pcps.json` |
| Reducer deltas | `runs/b25/proxy_validation_v4/stage2b/reducer_deltas.csv` |
| BFS time | 3780s = 63 min (63 min = 3720s Stage 2 + ~60s table-write overhead) |
| Corpus SHA256 | see `runs/b25/proxy_validation_v4/stage2b/corpus_provenance.json` |
| Corpus words tmp | `/tmp/stage2b_corpus_words.txt` (440 words, seed 20260630) |
| Corpus Q5 tmp | `/tmp/stage2b_corpus_q5.csv` (441 lines) |
