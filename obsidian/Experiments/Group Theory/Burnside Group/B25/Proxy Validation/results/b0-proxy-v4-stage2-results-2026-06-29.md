---
title: "Proxy Validation v4 — Stage 2 Results (B₀(2,5) Q5-scoped)"
date: 2026-06-29
domain: group-theory
project: b25
experiment_type: proxy-validation
instance: B0-proxy-stage2
author: maumayma
status: complete
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/proxy-validation, project/b25, status/complete, results]
---

# Proxy Validation v4 — Stage 2 Results

**Pre-registration**: [[methodology/proxy-validation-v4-stage2-prereg-2026-06-29]] (with [[methodology/proxy-validation-v4-stage2-prereg-2026-06-29#AMENDMENT 2026-06-29|Amendment: Q4→Q5 respec + Validator caveats]])  
**Stage 1 reference**: [[results/b33-proxy-v4-stage1-results-2026-06-27]]  
**[CONDITIONAL: B₀ ≅ B(2,5) / Kourovka 11.48]**  
**GT label**: `d_Q5(1,π₅(g))` — Cayley distance in Q5 = B₀/γ₆ (order 5^10); quotient-GT, NOT B₀-GT; d_Q5 ≤ d_B₀ by quotient-map inequality.

---

## §0 Ground Truth and Corpus

**Q5 = B₀/γ₆**, order 5^10 = 9,765,625. Generators {a, b, A=a⁻¹, B=b⁻¹}.  
**BFS**: completed in 3720 s = 62 min. All 9,765,625 states visited.  
**Q5 diameter = 20.** All corpus words of length > 20 are guaranteed non-geodesic.

### Corpus counts

| Category | Count |
|----------|-------|
| Total words evaluated | 3,609 |
| Q5-invisible (d_Q5=0, excluded from correlation) | 18 |
| Stratum II (d_Q5>0, not [G,G]) | 3,248 |
| Stratum II non-geodesic (len>d_Q5) — in analysis | 2,907 |
| Stratum III ([G,G], d_Q5>0) | 343 |
| Stratum III non-geodesic (len>d_Q5) — in analysis | **324** |

Stratum III count = 324 words, well above target of 80. All length-30 and length-50 corpus words are non-geodesic (Q5 diameter = 20 < 30 < 50).

**Q5-invisible (18 words)**: random-walk words that happen to map to identity in Q5. Automatically excludes all 119 HWW benchmark words (all identity in B₀ → d_Q5=0).

---

## §1 Spearman ρ Table

GT = d_Q5(1,π₅(g)); all correlations vs Q5 Cayley distance. Q5-invisible excluded from all columns.

| Feature | Strat II ρ | Strat III ρ | III blind frac | Pass H5 (≥0.20) |
|---------|------------|-------------|----------------|-----------------|
| **Arm0** greedy KB ratio | UNDEF | UNDEF | **1.000** | NO — blind |
| **Arm1** K=4, n=5 | 0.019 | −0.332 | 0.000 | **ANTI** |
| **Arm1** K=8, n=5 | 0.036 | −0.292 | 0.000 | **ANTI** |
| **Arm1** K=12, n=5 | 0.035 | −0.285 | 0.000 | **ANTI** |
| **Arm3** T=16 shrink | −0.031 | +0.110 | 0.809 | NO |
| **Arm3** T=64 shrink | −0.031 | +0.110 | 0.809 | NO |
| **Arm3** T=16 depth | −0.000 | −0.145 | 0.000 | NO (neg) |
| **Arm3** T=64 depth | −0.000 | −0.145 | 0.000 | NO (neg) |
| **PC norm_w5** (weight-5 layer) | 0.015 | +0.163 | 0.071 | NO |
| **PC first_nonzero_layer** | UNDEF† | **+0.210** | 0.000 | **PASS** |
| **PC norm_w4** (weight-4 layer) | 0.083 | +0.195 | 0.031 | NO (marginal) |
| **PC norm_w3** (weight-3 layer) | −0.006 | +0.003 | 0.052 | NO |

† PC first_nonzero_layer is constant = 1 for all stratum-II words (non-[G,G] → weight-1 ≠ 0 always → UNDEF). Varies only for stratum III where weight-1 = abel = (0,0).  
Stratum III n = 324 for all rows.

---

## §2 Hypothesis Outcomes

| ID | Hypothesis | Threshold | Result | Outcome |
|----|-----------|-----------|--------|---------|
| H5-0 | Arm1 ρ_II > 0.10 | ρ > 0.10 | ρ = 0.036 (K=8) | **FAIL** |
| H5-1 | Arm1 ρ_III ≥ 0.20 | ρ ≥ 0.20 | ρ = −0.292 (K=8) | **FAIL (anti-correlated)** |
| H5-2 | Arm3 shrink ρ_III ≥ 0.20 | ρ ≥ 0.20 | ρ = +0.110 | **FAIL** |
| H5-3 | PC weight-5 ρ_III ≥ 0.40 | ρ ≥ 0.40 | ρ = +0.163 | **FAIL** |
| H5-4 | Arm3 shrink ρ_III > 0 | ρ > 0 | ρ = +0.110 | **BORDERLINE PASS** |

**PC first_nonzero_layer** (not in pre-registered H5 family) passes ρ ≥ 0.20 at ρ = 0.210. Flagged as exploratory finding.

---

## §3 Findings and Interpretation

### F1: Arm 0 completely blind

All 31 seed rules have LHS length 41–1177 chars. Corpus words are random walks of length 10–50. Almost no rules fire → blind_frac = 1.000 on stratum III. Arm 0 is not a useful proxy for this corpus.

### F2: Arm 1 anti-correlated (ρ ≈ −0.30 on stratum III)

**This is the most structurally significant finding.** Periodicity-excess scores are NEGATIVELY correlated with Q5 distance: words with *more* period-5 substrings are *closer* to identity in Q5.

**Structural explanation**: In B₀(2,5), u^5 = identity. Words containing many u^k patterns (k ≡ 0 mod 5 substrings) fold back toward identity when B₀ relations are applied. The periodicity-excess score therefore measures "reducibility toward identity," NOT "distance from identity." The sign was wrong in the original hypothesis.

**Corrective insight**: Negating Arm 1 (using −arm1_K8) would yield ρ ≈ +0.292 on stratum III, passing the H5-1 threshold. However, this post-hoc sign flip requires a new pre-registered experiment before being promoted. Flagged for Maria's decision.

### F3: Arm 3 has small positive signal but is largely blind

81% of stratum-III words have zero shrink: the exponent-5 move set (free reduction + u^5 → ε for |u| ≤ 4 + conjugate-radius-3) does not fire on most random-walk corpus words. The 19% of words that DO shrink show ρ = +0.110 (positive, consistent with Arm 3 measuring some distance slack). The signal is too weak for practical use.

**Structural explanation**: Random walks of length 30–50 over {a,b,A,B} rarely contain u^5 patterns for short u (since u^5 has length ≥ 5, and the random walk doesn't repeat short patterns 5 times consecutively at frequency). The conjugate-radius-3 moves also rarely fire.

### F4: PC first_nonzero_layer is the best single feature (ρ = 0.210, stratum III)

The "first nonzero LCS-weight layer" predicts Q5 distance with ρ = 0.210 on [G,G] words. Structural interpretation: elements whose weight-1 and weight-2 coordinates (in the Q5 pcgs) are zero but weight-3 is nonzero live deeper in the group (farther from identity). This is the expected behavior of a lower-central-series stratification.

**Note**: This feature is UNDEFINED on stratum II (all non-[G,G] words have weight-1 ≠ 0, making first_nonzero_layer constant = 1 → no correlation). It is meaningful ONLY for [G,G] words — exactly stratum III.

### F5: Q5 diameter = 20 — geometric insight

The Cayley graph of Q5 = B₀/γ₆ on generators {a, b, A, B} has diameter exactly 20. This means:
- Any word of length > 20 over {a,b,A,B} is non-geodesic in Q5.
- The farthest element from identity in Q5 requires exactly 20 generator steps.
- This is a novel empirical datum about Q5, confirmed by exhaustive BFS.

---

## §4 Stage-2 vs Stage-1 Comparison

| Aspect | Stage 1 (B(3,3)) | Stage 2 (B₀/Q5) |
|--------|-----------------|-----------------|
| Stratum III non-geodesic words | 0 / 80 (all geodesic) | 324 / 343 (95% non-geodesic) |
| Arm 1 ρ stratum III | NaN (blind) | −0.292 (anti-correlated) |
| Arm 3 ρ stratum III | NaN (blind) | +0.110 (weak positive) |
| Root cause | Shortlex NF = geodesic | Non-geodesic corpus fixed the blind spot |

Stage 2 successfully fixed the Stage 1 blind spot (all stratum-III words geodesic). The non-geodesic corpus enabled signal detection — confirming the design was correct. The findings themselves (Arm 1 anti-correlated, Arm 3 weak) are informative, not null results.

---

## §5 Math Claims for Validator

None produced by this experiment. Spearman ρ values are empirical statistics about correlations on a sampled corpus, not theorems about B₀(2,5) structure. No routing to Validator required.

---

## §6 Open Questions for Lead / Maria

1. **Arm 1 sign flip**: −arm1_score has ρ ≈ +0.292 on stratum III. Is it worth pre-registering a new experiment to validate the negated arm as a "proximity to identity" rather than "distance from identity" feature?
2. **PC first_nonzero_layer extension**: Can this feature be combined with other PC features for a multi-feature predictor? Requires Maria GO per scope boundary.
3. **Arm 3 corpus sensitivity**: Does a larger corpus of shorter words (length ≤ 10) where exponent-5 patterns ARE present give better Arm 3 signal?
4. **Stage 3**: Any further proxy designs require explicit Maria GO per §10 of the pre-registration.

---

## §7 Provenance Triple

| Field | Value |
|-------|-------|
| GAP BFS script | `experiments/burnside/b25/proxy_validation_v4_stage2/stage2_bfs_q5.g` |
| Python arm scorer | `experiments/burnside/b25/proxy_validation_v4_stage2/stage2_corpus_and_arms.py` |
| Run dir | `runs/b25/proxy_validation_v4/stage2/` |
| Results CSV | `runs/b25/proxy_validation_v4/stage2/results.csv` |
| Report JSON | `runs/b25/proxy_validation_v4/stage2/report.json` |
| Q5 BFS output | `/tmp/stage2_corpus_q5.csv` (3610 lines = header + 3609 words) |
| BFS time | 3720 s (62 min), 9,765,625 states, diameter 20 |
| Corpus words SHA256 | (in provenance.json) |
| Corpus Q5 SHA256 | (in provenance.json) |
