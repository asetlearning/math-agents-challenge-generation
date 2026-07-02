---
title: "B(3,3) Proxy Validation — Stage 1, v4 Results"
date: 2026-06-27
domain: group-theory
project: b25
experiment_type: proxy-validation
instance: b33_proxy_v4_stage1
author: maumayma
status: complete
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/proxy-validation, topic/b33, project/b25, status/conjectured, results, experiment]
---

# B(3,3) Proxy Validation — Stage 1, v4 Results

**Method note**: [[methodology/proxy-validation-v4-prereg-2026-06-26]]  
**Scope**: B(3,3) proxy arms only (Stage 1). Stage 2 (B(2,5) B0-scoped) not released.  
**GT source**: Exact Cayley geodesic distance from `corpus.csv` (Cayley-BFS, pre-verified).  
**Artifacts verified**: `b33_metadata.txt` SHA256 `0c4b4e11...` ✓, `b33.kbprog` SHA256 `a81167ff...` ✓

---

## Key Finding: Stratum III Blind Spot Confirmed (All Arms)

**All 80 stratum III ([G,G] non-identity) corpus words are already at geodesic length** (len = dist for 80/80 words). This is not a limitation of the individual arms — it is a corpus structure fact.

Consequence: **no reduction-based proxy can detect variation in d among words already at minimum length.** Arms 0, 1, and 3 all score 0 on every stratum III word. Spearman ρ = NaN (constant input).

---

## Spearman ρ Table

| Feature | Stratum I ρ | Stratum II ρ | Stratum III ρ | III blind frac | III unique vals |
|---------|------------|-------------|--------------|----------------|-----------------|
| Arm0 (greedy KB ratio) | NaN* | **0.104** | NaN | 1.000 | 1 |
| Arm1 K=4 (period-excess) | NaN* | **0.204** | NaN | 1.000 | 1 |
| **Arm1 K=8 (period-excess)** | NaN* | **0.205** | NaN | 1.000 | 1 |
| Arm1 K=12 (period-excess) | NaN* | **0.205** | NaN | 1.000 | 1 |
| Arm3 T=16 shrink | NaN* | 0.085 | NaN | 1.000 | 1 |
| Arm3 T=64 shrink | NaN* | 0.085 | NaN | 1.000 | 1 |
| Arm3 T=16 depth | NaN* | −0.115 | NaN | 0.000 | 1 |
| Arm3 T=64 depth | NaN* | −0.115 | NaN | 0.000 | 1 |

*Stratum I NaN: all 258 words have d=0 (constant → Spearman undefined), not a bug.

**Arm1 K=8 on stratum II: ρ=0.205** — passes the ≥0.20 threshold on stratum II random words.  
**Arm1 K=8 on stratum III: ρ=NaN** — blind spot confirmed.

---

## Hypothesis Assessment

| Hypothesis | Target | Result | Verdict |
|------------|--------|--------|---------|
| H4-1: total_shrink_T16 ρ ≥ 0.20 on stratum III | Stratum III | NaN (blind) | **FALSIFIED** |
| H_supplemental: arm1 ρ ≥ 0.20 on stratum II | Stratum II | 0.205 ✓ | **CONFIRMED** |

---

## Root Cause Analysis

### Why stratum III is blind

The 80 [G,G] non-identity words in the B(3,3) corpus are the **shortlex normal forms** of those group elements. They are already geodesic representatives. No move in the B(3,3) C3 move set (free reduction, period-3, conjugate-radius-3) can shorten them — by construction, shortlex NF is the shortest word for that group element.

Arms 0, 1, 3 are all defined by what they can CUT from the word. None can "see" the internal algebraic difficulty of [G,G] elements. The blind spot is structural, not a feature implementation issue.

### What would help

To predict d among [G,G] geodesics, a feature would need to measure algebraic depth WITHOUT reference to the word's reducibility. Candidates:
- LCS weight of the word (in a free group or in B(3,3)) — might vary among [G,G] elements at same length
- Cayley-distance in a quotient group
- Coset-based features in [G,G] \ B(3,3)

None of these are implemented. This closes Arms 0, 1, 3 as proxy features for stratum III.

---

## Stratum III Sample (first 10 words)

| word | dist | len | arm1_K8 | arm3_T16_shrink | arm3_T16_depth |
|------|------|-----|---------|-----------------|----------------|
| aBAb | 4 | 4 | 0.0000 | 0.0000 | 16 |
| bABcaC | 6 | 6 | 0.0000 | 0.0000 | 16 |
| abCaBac | 7 | 7 | 0.0000 | 0.0000 | 16 |
| abacbAcAbc | 10 | 10 | 0.0000 | 0.0000 | 16 |
| abAB | 4 | 4 | 0.0000 | 0.0000 | 16 |
| aCAc | 4 | 4 | 0.0000 | 0.0000 | 16 |
| aBcabCa | 7 | 7 | 0.0000 | 0.0000 | 16 |
| CaBAbc | 6 | 6 | 0.0000 | 0.0000 | 16 |
| baBcAC | 6 | 6 | 0.0000 | 0.0000 | 16 |
| acAbCB | 6 | 6 | 0.0000 | 0.0000 | 16 |

All: arm1=0, arm3_shrink=0, arm3_depth=16 (=T, never descended).

---

## Stratum II Signal (arm1 positive result)

Arm1 (periodicity-excess, K=8) achieves ρ=0.205 on stratum II (500 random words, 89% have len > dist). Interpretation: words with higher periodicity-excess tend to be **further from identity** (higher d). This makes algebraic sense: if a word has many partial-period repetitions that don't fully cancel, the residual is at a higher Cayley distance from identity.

K=8 and K=12 give identical results (ρ=0.205). K=4 gives ρ=0.204. No K-sensitivity above K=4.

Arm3 (bounded-descent) on stratum II: weak (shrink ρ=0.085, depth ρ=−0.115). Arm0 (greedy KB) also weak (ρ=0.104).

**Rank on stratum II**: Arm1 > Arm0 > Arm3.

---

## Implications for B(2,5) Stage 2

Stage 2 is NOT released (awaiting Lead direction). The B(3,3) Stage 1 results suggest:
- Arm1 might give signal on B(2,5) words that are NOT at geodesic length (random/generated candidates longer than their B₀-geodesic)
- Arm3 (bounded-descent) is unlikely to be useful as a standalone proxy
- The blind spot on stratum III is a hard structural limit — any proxy corpus for B(2,5) should NOT include words already at geodesic length (otherwise the proxy will be blind by construction)

Stage 2 conditions (when GO arrives): B₀-scope, generated candidates only (not 119 benchmark words), Cayley distance in B₀ as GT.

---

## Artifact Locations

| Artifact | Path |
|----------|------|
| Stage 1 script | `experiments/burnside/b25/proxy_validation_v4_stage1/b33_proxy_v4_stage1.py` |
| Results CSV | `runs/b25/proxy_validation_v4/stage1_results.csv` |
| Report JSON | `runs/b25/proxy_validation_v4/stage1_report.json` |
| Provenance | `runs/b25/proxy_validation_v4/stage1_provenance.json` |
| Pre-reg | [[methodology/proxy-validation-v4-prereg-2026-06-26]] |
