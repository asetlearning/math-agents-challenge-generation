---
title: "Proxy Validation v4 — Stage 2b Pre-Registration (Negated Arm 1: periodicity-deficit)"
date: 2026-06-29
domain: group-theory
project: b25
experiment_type: proxy-validation
instance: B0-proxy-stage2b
author: maumayma
status: complete
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/proxy-validation, project/b25, status/pending, methodology, experiment]
---

# Proxy Validation v4 — Stage 2b Pre-Registration

**Status**: RUNNING (2026-06-29). GO+BUDGET from Lead/Maria: 4 procs max, 3h hard ceiling.  
**Scope**: B₀(2,5)-scoped. Negated Arm 1 (periodicity-deficit) + PC first_nonzero_layer combined.  
**Parent**: [[methodology/proxy-validation-v4-stage2-prereg-2026-06-29]] (Stage 2: negation was post-hoc finding)  
**Binding constraint**: All further proxy extensions still require Maria GO per Stage 2 §10.

> **AMENDMENT 2026-06-29 (Lead/Maria respec)**: Target changed from Q5-distance (d_Q5) to **actual bounded reducer improvement** (reducer_delta = len(input) - len(braid_reduce(input))). Confirmatory scope: −Arm1 K=4 ONLY (no K8/K12 in this corpus). Pass criteria: ρ ≥ 0.20 OR top-decile lift ≥ 1.25. Corpus: 440 targeted candidates (seed 20260630), quota: 200 non-geodesic [G,G]-visible + 100 non-geodesic non-[G,G] + 140 other. Reducer config: beam_width=4096, beam_secs=5, timeout=20s, 3 workers. Rule bank: 31 GAP-verified seed rules (b25_seed_rules_2026-06-25.kbprog) + built-in braid shortenings (u^5=ε, B₀-valid by definition).

> **METHODOLOGY WARNING (Lead/Maria, 2026-06-29)**: The Stage 2 re-analysis values below (§0) are DOUBLY IN-SAMPLE: (1) the sign was chosen post-hoc after observing anti-correlation on the Stage 2 corpus; (2) K=4 was selected because it gave the highest |ρ| on that same corpus. The p-values are INVALID — they cannot be reported as significance claims for a hypothesis that came from the same data. This is an UNVALIDATED working hypothesis until a fresh independent corpus confirms it.

---

## §0 Motivation

Stage 2 found Arm 1 (periodicity-excess, n=5) **anti-correlated** with d_Q5 on stratum III: ρ = −0.292 (K=8). Structural interpretation: words with many u^5 patterns are *closer* to identity in Q5 because those patterns collapse under B₀ relations (u^5=1). The feature was measuring "proximity to identity," not "distance from identity."

**Negation**: define `periodicity_deficit = −periodicity_excess`. This should be POSITIVELY correlated with d_Q5.

**In-sample observation on Stage 2 corpus** (DOUBLY IN-SAMPLE — not a result, not reportable as significant; for motivation only):
- −arm1_K4: ρ_III ≈ +0.33 [sign + K chosen from this data; p-value invalid]
- −arm1_K8: ρ_III ≈ +0.29 [same caveat]
- Combined (−arm1 + pc_first_nonzero_layer): ρ_III ≈ +0.35 [same caveat]

Stage 2b is the formal independent-corpus validation. NONE of the above values are results until fresh-corpus replication.

---

## §1 Research Question

Does **periodicity-deficit** (−arm1_score, exponent-5) positively predict Cayley distance in Q5 = B₀/γ₆ for stratum-III ([G,G]) words, on an **independent corpus** (different random seed from Stage 2)?

---

## §2 Ground Truth

Identical to Stage 2: **d_Q5(1,π₅(g))** — Cayley distance in Q5 = B₀/γ₆ (order 5^10, diameter 20).  
Label: quotient-GT, NOT B₀-GT. d_Q5 ≤ d_B₀.  
[CONDITIONAL: B₀ ≅ B(2,5) / Kourovka 11.48]

**Note on fresh corpus**: A fresh corpus requires a new GAP BFS run (~62 min, same Q5 BFS cost as Stage 2). If budget does not allow a second BFS run, Stage 2b can be reported using the Stage 2 corpus with an explicit "preliminary / same-corpus" caveat. Lead to decide.

---

## §3 New Feature

**Periodicity-deficit** (negated Arm 1):

```
periodicity_deficit(w, K, n) = −periodicity_excess(w, K, n)
                             = −(Σ_excess / |w|)
```

where `excess = |u| × (k mod n)` for each u^k match with |u| ≤ K, k ≥ 2, n=5 (B₀ exponent).

**Parameter**: Report ALL K ∈ {4, 8, 12}. DO NOT pre-select K=4 as "primary" — K was selected in-sample from Stage 2 and that selection must not be carried forward. All three K values have equal status in Stage 2b.

**Structural interpretation**: low periodicity-excess (high periodicity-deficit) = word lacks u^5 patterns = word does not fold back toward identity = farther from identity. ✓

---

## §4 Arm Roster

| Arm | Feature | Change from Stage 2 |
|-----|---------|---------------------|
| Arm 0 | greedy KB reduction | unchanged (will remain blind if corpus similar) |
| Arm 1b | −arm1_K4 (periodicity-deficit) | **NEW: sign flipped** |
| Arm 3 | bounded-descent shrink | unchanged |
| PC | pc_first_nonzero_layer | unchanged |
| PC combo | −arm1_K4 + pc_first_nonzero_layer (standardized) | NEW: combined score |

---

## §5 Hypotheses

| ID | Hypothesis | Stratum | Threshold | Falsification |
|----|-----------|---------|-----------|---------------|
| H6-1 | −arm1_K4 ρ_III ≥ 0.20 | III | ρ ≥ 0.20 | ρ < 0.20 |
| H6-2 | −arm1 (ANY K ∈ {4,8,12}) ρ_III ≥ 0.30 on independent corpus | III | ρ ≥ 0.30 for at least one K | fails for all K |
| H6-3 | Combined (−arm1_K4 + pc_first_nonzero_layer) ρ_III > max(ρ(arm1b), ρ(pc)) | III | additive improvement | no improvement |

**H6-2** is the critical test: does the fresh corpus replicate the ρ ≈ 0.33 post-hoc result?

---

## §6 Anti-pattern Guards

1. **Independent corpus**: fresh random seed (≠ 20260629 used in Stage 2). If same corpus used, label as "preliminary / same-corpus" explicitly.
2. **Same stratification and non-geodesic filter**: same as Stage 2 (Validator mandate still binding).
3. **Q5-invisible excluded from correlation**: d_Q5=0 words still excluded.
4. **No cherry-picking K**: report all three K=4,8,12 values, not just K=4.

---

## §7 Provenance

Fresh BFS corpus if run:
- Script: `experiments/burnside/b25/proxy_validation_v4_stage2/stage2_corpus_and_arms.py` (with new seed)
- New seed: 20260630
- Run dir: `runs/b25/proxy_validation_v4/stage2b/`
- Estimated BFS time: ~62 min (same Q5 setup)

If Stage 2 corpus reused:
- Label result: "preliminary / same-corpus post-hoc re-analysis"
- Confirm label appears in all artifacts and report

---

## §8 MANDATORY PERSIST REQUIREMENT (Lead/Maria doctrine, 2026-06-29)

The Stage 2 Q5 BFS took 62 minutes and was DISCARDED at session end. This was waste. The canonical doctrine (now in `_meta/agents/_common.md`) applies:

> **Any expensive corpus-independent artifact (BFS distance tables, PcGroup builds, rule banks) MUST be persisted to runs/ with provenance before the session ends.**

On the Stage 2b BFS run, BEFORE running any analysis:

1. **Save B₀ PcGroup to disk**: after `phi12 := EpimorphismPGroup(G, 5, 12)` and `B25 := Image(phi12)`, write the pcgs generator images to a file (GAP `PrintTo` with exponent vectors of all pcgs generators in B25, sufficient to reconstruct Q5 maps in a later session).

2. **Save Q5 distance table to disk**: after the BFS completes, write every (element → distance) pair to `runs/b25/proxy_validation_v4/stage2b/q5_dist_table.csv` (format: `pcgs_1,...,pcgs_10,q5_dist`). This is the 9.77M-entry table. Estimated size: ~600 MB uncompressed, ~120 MB gzip. Save both; keep local per data policy.

3. **Provenance record**: write `runs/b25/proxy_validation_v4/stage2b/q5_bfs_provenance.json` with: GAP version, B0 relator count, LCS depth (6), Q5 order, diameter, BFS time, sha256 of the distance table file.

4. **Evaluate new corpus words via table lookup**: load the distance table into a dict (Python); for each new corpus word, evaluate it in Q5 (letter-by-letter generator application using saved generator images), then look up the distance. O(|w|) per word, no GAP required.

This turns all future Q5 proxy experiments into cheap lookups, not 62-min recomputes.

**Do not proceed with Stage 2b BFS unless this persist plan is executed.**
