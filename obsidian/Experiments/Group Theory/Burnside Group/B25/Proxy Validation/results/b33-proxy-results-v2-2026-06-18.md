---
title: B(3,3) Proxy Validation Study v2 — Results
date: 2026-06-18
domain: group-theory
project: b25
experiment_type: proxy-validation
instance: B(3,3)
author: maumayma
status: completed
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, project/b25, status/completed, results]
---

# B(3,3) Proxy Validation Study v2 — Results

**Status**: COMPLETED 2026-06-18  
**Pre-registration**: [[methodology/b33-proxy-validation-v2-2026-06-17]]  
**Verdict**: H1 NOT SUPPORTED, H2 NOT SUPPORTED → Keep Option B; LCS-weight-2 is not a valid proxy for [G,G] distance  
**Runs directory**: `runs/b25/proxy_validation_v2/2026-06-18/`

---

## Provenance

| Artifact | Value |
|---|---|
| GAP version | 4.15.1 |
| Corpus script | `b33_corpus_builder.g` (sha256: `e2f2d519...`) |
| Distance table | `b33_metadata.txt` (sha256: `0c4b4e11...`) |
| KB rule bank | `kbmag/b33.kbprog` (sha256: `a81167ff...`) confluent, 1974 rules |
| Corpus seed | 20260617 |
| Analysis script | `b33_proxy_analysis.py` |
| Full results log | `b33-proxy-results-v2-2026-06-18.txt` |

---

## Corpus

| Stratum | Description | Count |
|---|---|---|
| I | Relators (d=0) | 258 |
| II | Random non-identity | 500 |
| III | [G,G]\{1} census | 80 |
| **Total** | | **838** |

**[G,G] distance distribution (stratum III)**:

| d | Count | of which γ₃ |
|---|---|---|
| 4 | 6 | 0 |
| 6 | 64 | 0 |
| 7 | 8 | 0 |
| 10 | 2 | 2 |

**γ₃ confirmation** (Validator prediction verified): both non-identity γ₃ elements ARE at d=10. Words: `abacbAcAbc`, `abacAbcbAc`. Both have lcs2_dist=0.

**D-FIX-1 assertion guard**: PASSED (pcgs[4,5,6] ∈ γ₂\γ₃; pcgs[7] ∈ γ₃; confirmed before any proxy-D computation).

**kbprog**: confluent (`#System is confluent.`), 1974 rules, exit code 0.

---

## Results

### Full corpus (n=838)

| Proxy | Spearman ρ | p | Pearson r | 95% CI |
|---|---|---|---|---|
| A (reduction_ratio) | 0.083 | 0.017 | -0.010 | [-0.078, 0.058] |
| B (abelianization) | 0.490 | 6.2×10⁻⁵² | 0.548 | [0.499, 0.594] |
| D (lcs2_dist) | **0.697** | 7.2×10⁻¹²³ | 0.740 | [0.708, 0.769] |
| E (B+D) | 0.659 | 1.4×10⁻¹⁰⁵ | 0.736 | [0.703, 0.765] |

Note: D has the highest full-corpus ρ, but this is driven by stratum I/II separation (d=0 vs d>0), not gradient within [G,G].

### Stratum II — random non-identity (n=500)

| Proxy | Spearman ρ | p |
|---|---|---|
| A | 0.200 | 6.3×10⁻⁶ |
| B | 0.029 | 0.517 |
| D | 0.182 | 4.2×10⁻⁵ |
| E | 0.124 | 0.006 |

Interesting: D slightly outperforms B on random non-identity words. B is nearly uncorrelated with distance on stratum II (ρ=0.029), which is surprising (random words should have nonzero abelianization and it should correlate with distance).

Blind-spot fractions (stratum II): A=0.652, B=0.032, D=0.104, E=0.000.

### Stratum III — [G,G] (all 80)

| Proxy | Spearman ρ | p | Notes |
|---|---|---|---|
| A | NaN | — | Blind-spot = 1.000 (completely blind) |
| B | NaN | — | Constant 0 by definition (theorem) |
| D | -0.043 | 0.706 | Essentially zero |
| E | -0.043 | 0.706 | Same as D (B contributes nothing) |

Proxy A = 0.000 on ALL 80 [G,G] words — confirmed the motivating hypothesis.  
Proxy B = 0.000 on ALL 80 [G,G] words — confirmed theorem.

### Stratum III — γ₂\γ₃ only (n=78) — **H2 DECISION BASIS**

| Proxy | Spearman ρ | p |
|---|---|---|
| D (lcs2_dist) | **0.079** | 0.492 |
| E (B+D) | 0.079 | 0.492 |

**H2 threshold: ρ > 0.40. Observed: ρ = 0.079. H2 NOT SUPPORTED.**

### y>0 slice — Steiger's Z (H1)

| | Spearman ρ | p |
|---|---|---|
| Proxy A | 0.100 | 0.016 |
| Proxy E | -0.026 | 0.530 |
| ρ(A, E) | 0.126 | — |
| Steiger's Z (E vs A) | Z = -2.314 | p = 0.021 |

E is **significantly worse** than A on the y>0 slice (Steiger's Z p=0.021). H1 NOT SUPPORTED.

---

## Transfer Decision

Per pre-registration §8:

**H1**: NOT SUPPORTED (delta = -0.127, rho_E = -0.026, Z_p = 0.021)  
**H2**: NOT SUPPORTED (rho_D on γ₂\γ₃ = 0.079, threshold 0.40)  

**→ Keep Option B. LCS-weight-2 is NOT a valid proxy for [G,G] distance. File new design.**

---

## Analysis

**Why did D fail within [G,G]?** The lcs2_dist (pcgs f4/f5/f6 exponents) measures coset membership in γ₂/γ₃ — it labels which of the 27 cosets of γ₃ in γ₂ an element belongs to. But within [G,G], geodesic distance does NOT segregate by coset: elements at d=4, d=6, and d=7 all appear in the same cosets. The weight-2 invariant is structurally 0 for γ₃ elements (distance-10 pair) and non-zero for γ₂\γ₃ elements (distances 4, 6, 7), but within those non-zero cosets, distance is essentially random with respect to the coset label.

**What D does capture**: D provides an excellent full-corpus gradient (ρ=0.697) because it perfectly separates stratum I (all d=0) from stratum II/III (d>0 with nonzero D for γ₁\γ₂ words). This is a coset-separation signal, not a within-[G,G] distance gradient.

**The problem remains**: Neither abelianization (B) nor LCS-weight-2 (D) gives a gradient within [G,G]. The [G,G] blind class is genuinely hard. A proxy for this class would need to capture something about commutator depth or geodesic structure within the commutator subgroup — a fundamentally harder invariant.

---

## Process Hygiene

Run complete. All processes killed; clean verified:
```
pgrep -al gap → (empty, exit 1)
pgrep -al nq  → (empty, exit 1)
pgrep -al kbprog → (empty, exit 1)
```
