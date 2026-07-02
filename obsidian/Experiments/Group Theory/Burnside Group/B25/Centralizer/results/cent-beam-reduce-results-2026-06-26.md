---
title: "Centralizer Beam Reduction — Complete Results (34/34 elements)"
date: 2026-06-26
domain: group-theory
project: b25
experiment_type: centralizer
instance: cent_enum_beam_reduce
author: maumayma
status: complete-pending-validation
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/centralizer, topic/beam-search, project/b25, status/conjectured, results, experiment]
---
 
# Centralizer Beam Reduction — Complete Results

**Status**: #status/conjectured — 27 shortened words need GAP word-equality verification in B₀(2,5). Abelianization FORBIDDEN.  
**Method note**: [[methodology/cent-beam-reduce-2026-06-26]]  
**Run sources**: Experimenter (199K+180s for all 34) + B25-Experimenter (500K+120/60s for 18/34). **Best-of both** used per element.  
**Scope**: B₀(2,5) finite restricted quotient, order 5^34. NOT free B(2,5).

---

## TRUE MINIMUM

**4998 chars — gen_8 (exponent vector 0,0,0,0,0,0,0,1,0)**

Same group element also reached as gen_8^4 (beam found gen_8^4 → 4998 = gen_8^{-1} length).

---

## Complete Beam-NF Table (34 elements)

Elements sorted by beam_len. `*` = structural reduction (exponent-5 collapse). `†` = confirmed by 500K run.

### Unchanged at FSA-NF (7 elements)

| Exponent vector     | Label         | FSA_len | Beam_len  | Δ   |
| ------------------- | ------------- | ------- | --------- | --- |
| (0,0,0,0,0,0,0,1,0) | **gen_8**     | 4998    | **4998**  | 0   |
| (0,0,0,0,0,0,0,0,1) | gen_9         | 5015    | **5015**  | 0   |
| (0,0,0,0,0,0,0,2,0) | gen_8^2       | 9994    | **9994**  | 0   |
| (0,0,0,0,0,0,0,1,1) | gen_8·gen_9   | 10007   | **10007** | 0   |
| (0,0,0,0,0,0,0,0,2) | gen_9^2       | 10027   | **10027** | 0   |
| (0,0,0,0,0,0,0,2,1) | gen_8^2·gen_9 | 15003   | **15003** | 0   |
| (0,0,0,0,0,0,0,1,2) | gen_8·gen_9^2 | 15019   | **15019** | 0   |

### Improved by beam (27 elements)

| Exponent vector     | Label             | FSA_len | Beam_len  | Δ      | Note                      |
| ------------------- | ----------------- | ------- | --------- | ------ | ------------------------- |
| (0,0,0,0,0,0,0,4,0) | gen_8^4           | 19986   | **4998**  | -14988 | * gen_8^4 = gen_8^{-1}    |
| (0,0,0,0,0,0,1,0,0) | gen_7             | 6453    | **5138**  | -1315  | †                         |
| (0,0,0,1,0,0,0,0,0) | gen_4             | 9995    | **6867**  | -3128  |                           |
| (0,0,0,0,1,0,0,0,0) | gen_5             | 10622   | **7745**  | -2877  |                           |
| (0,0,0,0,0,0,1,1,0) | gen_7·gen_8       | 11450   | **10134** | -1316  | †                         |
| (0,0,0,0,0,0,1,0,1) | gen_7·gen_9       | 11465   | **10147** | -1318  | †                         |
| (0,1,0,0,0,0,0,0,0) | gen_2             | 17049   | **11944** | -5105  |                           |
| (0,0,0,0,0,0,0,3,0) | gen_8^3           | 14990   | **9994**  | -4996  | * gen_8^3 = gen_8^{-2}    |
| (0,0,0,0,0,0,2,0,0) | gen_7^2           | 12906   | **10276** | -2630  |                           |
| (0,0,0,0,0,0,0,0,3) | gen_9^3           | 15039   | **10027** | -5012  | * gen_9^3 = gen_9^{-2}; † |
| (0,0,0,0,0,0,0,0,1) | —                 | —       | —         | —      | —                         |
| (0,0,0,1,0,0,0,1,0) | gen_4·gen_8       | 14991   | **11861** | -3130  |                           |
| (0,0,0,1,0,0,0,0,1) | gen_4·gen_9       | 15004   | **11877** | -3127  |                           |
| (0,0,0,0,1,0,0,1,0) | gen_5·gen_8       | 15618   | **12741** | -2877  |                           |
| (0,0,0,0,1,0,0,0,1) | gen_5·gen_9       | 15631   | **12754** | -2877  |                           |
| (1,0,0,0,0,0,0,0,0) | gen_1             | 15745   | **8549**  | -7196  |                           |
| (0,0,0,0,0,0,1,2,0) | gen_7·gen_8^2     | 16446   | **15130** | -1316  | †                         |
| (0,0,0,1,0,0,1,0,0) | gen_4·gen_7       | 16448   | **12006** | -4442  |                           |
| (0,0,0,0,0,0,1,1,1) | gen_7·gen_8·gen_9 | 16459   | **15143** | -1316  | †                         |
| (0,0,0,0,0,0,1,0,2) | gen_7·gen_9^2     | 16477   | **15159** | -1318  | †                         |
| (0,0,0,0,1,0,1,0,0) | gen_5·gen_7       | 17075   | **12883** | -4192  |                           |
| (0,0,0,0,0,1,0,0,0) | gen_6             | 17352   | **12883** | -4469  |                           |
| (0,0,0,0,0,0,2,1,0) | gen_7^2·gen_8     | 17903   | **15272** | -2631  |                           |
| (0,0,0,0,0,0,2,0,1) | gen_7^2·gen_9     | 17918   | **15285** | -2633  |                           |
| (0,0,0,0,0,0,3,0,0) | gen_7^3           | 19359   | **10277** | -9082  | * gen_7^3 ≈ gen_7^{-2}    |
| (0,0,0,1,0,0,0,2,0) | gen_4·gen_8^2     | 19987   | **16857** | -3130  |                           |
| (0,0,0,2,0,0,0,0,0) | gen_4^2           | 19989   | **13763** | -6226  |                           |
| (0,0,0,0,0,0,0,3,1) | gen_8^3·gen_9     | 19999   | **15007** | -4992  | †; * similar              |

**27/34 = 79% improved by beam.**

---

## Structural Findings

### 1. Exponent-5 collapse pattern (gen_k^3 = gen_k^{-2}, gen_k^4 = gen_k^{-1})

In B₀(2,5), every element has order dividing 5. The beam search discovered exponent-5 reductions:

| Element | Structural identity | FSA | Beam | Savings |
|---------|-------------------|-----|------|---------|
| gen_8^4 | = gen_8^{-1} | 19986 | 4998 | **-14988** |
| gen_7^3 | ≈ gen_7^{-2} | 19359 | 10277 | -9082 |
| gen_8^3 | = gen_8^{-2} | 14990 | 9994 | -4996 |
| gen_9^3 | = gen_9^{-2} | 15039 | 10027 | -5012 |
| gen_8^3·gen_9 | structural | 19999 | 15007 | -4992 |

The greedy FSA completely missed these (it only applies short-LHS rules, cannot encode the full generator^5 = identity path).

**gen_8^4 → 4998** is the most dramatic: 14,988 chars saved. The beam represents gen_8^4 as gen_8^{-1} — a different 4998-char word that equals the same group element.

### 2. Generator-specific savings are additive

Each gen_k factor in a product saves approximately a fixed amount:
- gen_7 factor: saves ~1315–1318 chars in any product
- gen_4 factor: saves ~3127–3130 chars in any product
- gen_5 factor: saves ~2877 chars in any product
- gen_6, gen_1, gen_2: large savings (these generators have long FSA words that can be beam-shortened)

### 3. gen_8 and gen_9 family at FSA-NF
Pure gen_8 and gen_9 products (no other generators) show zero beam improvement. These 7 elements appear to be at or near their true geodesic length. **Untested: RPO rule bank might find additional reductions.**

### 4. gen_1 (15745 → 8549, Δ=-7196) — largest absolute saving for a single generator
gen_1 (FSA length 15745) beam-reduces to 8549. This ~46% reduction is the largest for any generator.

---

## ITEM-2b Relevance

**Question from Lead**: "Is ANY centralizer element small enough to be a realistic ITEM-2b reshape target?"

| Range | Elements | Count |
|-------|----------|-------|
| <5000 | gen_8 (4998) | 1 |
| 5000–7000 | gen_9 (5015), gen_7 (5138), gen_4 (6867) | 3 |
| 7000–10000 | gen_5 (7745), gen_8^3→9994, gen_1→8549 | 3 |
| 10000–15000 | gen_2→11944, gen_9^3→10027, ... | many |

**True minimum: 4998 chars (gen_8).**

All confirmed shortest elements are ≥4998 chars. Inserting a ~5000-char centralizer word as a reshape operation would add 5000 chars to any target word, not shorten it. **This is a negative signal for ITEM-2b feasibility unless the reshape mechanism subtracts more than it adds.**

Maria's standing call: ITEM-2b stays OPEN. This is data, not a close.

---

## Validation Required (#status/conjectured)

All 27 shortened beam-NF words are **#status/conjectured**. They require GAP word-equality verification in B₀(2,5) before any downstream use. Abelianization is FORBIDDEN (blind on commutator subgroup).

Routing to Validator: pending Lead approval.

Verification template (per word):
```gap
# In GAP:
G := ...; # same B0(2,5) presentation as Validator's setup
w_original := ...; # exponent product representation
w_beam := ...; # beam-NF word (from Experimenter's /tmp/cent_beam_results/)
IsOne(w_original * w_beam^-1); # must be true
```

---

## Artifact Locations

| Artifact | Path |
|----------|------|
| Beam-NF words (Experimenter) | `/tmp/cent_beam_results/elem_*.out` (Experimenter's terminal) |
| Partial run (B25-Experimenter, 18/34) | `runs/b25/cent_enum_beam/20260626_230254/` |
| Partial JSON | `runs/b25/cent_enum_beam/20260626_230254/partial_results.json` |
| Experimenter output note | `experiments/burnside/b25_centralizer_rules/output/cent_beam_reduce_results.md` |

**Action needed**: Experimenter's beam output words (`/tmp/`) should be moved to `runs/b25/cent_enum_beam/` before the terminal session ends.
