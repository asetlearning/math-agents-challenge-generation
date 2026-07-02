---
title: B(5,3) Proxy Validation — Step C Results
date: 2026-06-17
domain: group-theory
project: b25
experiment_type: proxy-validation
instance: B(5,3)
author: maumayma
status: inconclusive
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, project/b25, status/inconclusive, results]
---

# B(5,3) Proxy Validation — Step C Results

**Pre-registration**: [[methodology/b53-proxy-validation-study-2026-06-17]]
**Date**: 2026-06-17
**Provenance**: `runs/b53/20260617_120259/kb_shortlex/input.kbprog.live` (98,210 rules, sha256 of run confirmed via Step A log)
**Script**: `experiments/burnside/b53_bidir/script/b53_proxy_validation.py`
**Output files**: `experiments/burnside/b53_bidir/proxy_validation_output/b53-proxy-corpus-v2-2026-06-17.csv`, `b53-proxy-results-v2-2026-06-17.txt`

---

## METHODOLOGICAL DEVIATION (from pre-registration)

**Pre-registered**: ground truth = continuous geodesic distance via exhaustive greedy reduction on the 98K shortlex rule bank.

**Actual**: the KB run is `#confluent=false` (interrupted after all 153 relators proved; `_ExitCode=2`). Greedy reduction on a non-confluent system gives arbitrary fixed points — 57/153 relators were assigned y>0 (incorrect). Continuous-y analysis is not available.

**Correction**: binary oracle ground truth from `kb_mixer --bootstrap` run (45s timeout). Proved in ≤45s → y=0 (identity). Not proved → y=1 (non-identity). Oracle confirmed: exactly indices 0–152 (153 relators) proved; 0 of 800 random words proved.

**Consequence**: Pre-registered H1/H2 thresholds (r≥0.60 on y>0 slice, Steiger's Z on y>0) cannot be applied as specified. Adapted analysis uses binary y on full corpus. H1/H2 analogs applied with same numerical thresholds.

---

## Corpus

| | Count |
|---|---|
| Total words | 953 |
| Identity (relators, y=0) | 153 |
| Non-identity (random, y=1) | 800 |
| Seed | 20260617 |
| Max word length | 30 |

**y-distribution**: binary only (no continuous distance). All 153 relators = y=0, all 800 random = y=1.

**Achieved bin counts** (adapted): y=0: 153, y=1: 800.

---

## Results

### Group Means

| Proxy | identity mean | non-identity mean | diff |
|---|---|---|---|
| A: reduction_ratio | 0.0354 | 0.0927 | +0.0573 |
| B: abelianization_dist | 0.0000 | 3.2113 | +3.2113 |
| C: combined (α=β=0.5) | 0.0177 | 1.6520 | +1.6343 |

### Full Corpus Correlations (y binary, n=953)

| Proxy | Pearson r | 95% CI | p | Spearman ρ | 95% CI | p |
|---|---|---|---|---|---|---|
| A: reduction_ratio | 0.2476 | [0.187, 0.306] | 8.77e-15 | 0.2989 | [0.240, 0.356] | 3.99e-21 |
| B: abelianization_dist | **0.7521** | [0.723, 0.778] | 2.30e-174 | **0.6474** | [0.609, 0.683] | 2.65e-114 |
| C: combined | **0.7567** | [0.728, 0.783] | 1.01e-177 | **0.6345** | [0.595, 0.671] | 1.67e-108 |

### AUC / Blind-spot (non-identity words, n=800)

| Proxy | Mann-Whitney AUC | AUC p | Blind-spot (proxy=0) |
|---|---|---|---|
| A: reduction_ratio | 0.2703 | 2.88e-20 | **28.0%** (224/800) |
| B: abelianization_dist | 0.0025 | 9.10e-89 | 0.5% (4/800) |
| C: combined | **0.0017** | 2.41e-85 | **0.2%** (2/800) |

*AUC < 0.5 means identity has LOWER proxy values (correct — proxy is a distance-like score).*

### Steiger's Z (combined vs reduction_ratio, binary y)

| Quantity | Value |
|---|---|
| r(combined, y) | 0.7567 |
| r(reduction_ratio, y) | 0.2476 |
| r(combined, reduction_ratio) | 0.2397 |
| delta r | **0.5090** |
| Steiger's Z | **19.57** |
| p (two-tailed) | **6.59e-72** |

---

## H1 / H2 Verdicts

**STATUS: INCONCLUSIVE — pre-registered study could not be executed.**

Three fatal problems (per Lead verdict 2026-06-17):

### Problem 1 (FATAL for stated goal): Combined proxy is blind on the motivating class

Products-of-conjugates like `(aba)^5` live in the **commutator subgroup** of B(5,3). These have:
- abelianization = 0 (commutator-subgroup words always have abelization 0 mod exponent)
- reduction_ratio ≈ 0 (they don't reduce under KB rules — that's the 43%-blind class from B(2,5))
- → combined = 0.5×0 + 0.5×0 = **0** on the motivating hard class

The uniform-random corpus hit commutator-subgroup words only **4/800 times**. The r=0.757 result is carried entirely by words with non-zero abelianization (easy to score). On a commutator-subgroup corpus, Proxy C blind-spot approaches ~100%.

**Example**: `(aba)^5` abelianizes to `(10,5) = (0,0) mod 5` → lies in [G,G] → abel_dist=0.

### Problem 2 (INVALIDATES DESIGN): Pre-registered ground truth does not exist

Run17 KB is `#confluent=false`. Greedy reduction on non-confluent system gave wrong canonical forms (57/153 relators stuck at non-empty). The pre-registered y-axis (shortlex normal-form length) was never computable. Pre-registration gate (a) hardener was not actually met.

### Problem 3 (POST-HOC + UNROUTED MATH): Binary oracle substitution changes DV

Substituting binary oracle for continuous distance:
- Collapses the y>0 slice required by pre-registration (non-identity words all have y=1 → degenerate)
- Reduces to restating Validator gate (b) ("abelianization detects non-identity"), not new gradient evidence
- Is a math-soundness claim (kb_mixer --bootstrap is false-negative-free identity decider) that must route to Validator, not be self-certified

Adapting both the DV and the thresholds post-hoc means H1/H2 cannot be claimed satisfied.

---

## Transfer Decision

**DECISION: NO TRANSFER. Option B stays as-is. Do not wire combined proxy into PatternBoost calc_score().**

---

## Useful Nugget (do not oversell)

On **uniform-random words** (not commutator subgroup): abelianization is a near-perfect non-identity **detector** (blind-spot 0.5% vs reduction_ratio 28%). But detector ≠ gradient, and it scores exactly 0 on the hard class. This is not new evidence about a distance gradient.

---

## Known Limitations

1. **Binary GT only**: continuous geodesic distance not available. Full convergent B(5,3) KB requires millions of rules and hours of compute. GAP coset enumeration is the cleaner alternative.
2. **Proxy A shares KB with oracle** (mechanical correlation): proxy A was computed using the same 98K rule bank the oracle bootstrapped from. This inflates proxy A's correlation with oracle results. However, since proxy C = 0.5×A + 0.5×B, and B is purely algebraic (no KB dependency), the combined proxy's performance is mostly driven by B. This caveat does not change the transfer decision.
3. **H1/H2 thresholds not directly applicable to binary y** — adapted analysis only.

---

## Path Forward (per Lead verdict 2026-06-17)

Before re-running: route to Validator (is GAP/BFS geodesic distance the correct GT? is binary --bootstrap oracle sound for all 953 words?).

1. **TRUE DISTANCE GROUND TRUTH**: B(5,3) has order 2187 — exact Cayley-graph BFS or GAP coset enumeration gives geodesic distance-to-identity for every word. This is the y-axis the study needs (continuous gradient, not just identity/non-identity).
2. **STRATIFIED CORPUS**: deliberately include commutator-subgroup words (B(5,3) analogs of `(aba)^5`) at a meaningful fraction so the motivating blind class is actually tested.
3. **RE-REGISTER (v2 dated pre-reg)** before re-running. Keep y>0 slice as decision basis — now computable with continuous distance.
4. **ROUTE TO VALIDATOR FIRST**: is GAP/BFS geodesic distance the correct GT for B(5,3)? Is binary --bootstrap oracle sound as a check?

**Developer task NOT filed**: Option B stays as-is in PatternBoost calc_score().
