---
title: "T-028 benchmark words: generation parameters vs solver fate"
domain: group-theory
project: challenge-gen
instance: B(2,5)
experiment_type: hardness-evaluation
status: draft
author: asetlearning
date: 2026-11-13
todo: T-028
tags: [agent/lead, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/benchmark-design, project/challenge-gen, status/draft, results]
---

# T-028 benchmark words: generation parameters vs solver fate

**Question (owner, 2026-11-13).** How were the T-028 words generated? Which parts of the construction lead to words our solvers still cannot break, and which lead to words they break?

**Answer.** Only **length** predicts hardness. Long substitution words and three factors make W long, and the long words are the ones still unbroken. The choice of factor words t, the signs, the conjugators and how much the T-028 chain shortened W show no detectable effect. So the benchmark's hardness, as measured by our solvers, is a length effect, not a structural one.

**Data.**
- All 330 words of T-028 job 1 (11 cells × 30; the 30 CTRL words are left out), with their fate up to the [[ds-b25-challenge-candidates]] revision 10 draft (2026-11-13: 103 candidates).
- The draws (t, signs, x/y) were re-made from each word's seed, and match the stored construction on all 220 survivors.
- The conjugators and the junction cancellation come from the survivor records only.
- Scripts and outputs are in Lead's private run folder `t028-generation-stats-20261113`: `gen_stats.py`, `gen_report.py`, `gen_ttest.py`, and their outputs.

## 1. Generation procedure

- **The word:** W = cyclic_reduce(∏ⱼ cⱼ⁻¹ φⱼ(tⱼ)^{sⱼ} cⱼ). The registry word is the end word of the T-028 chain R → KB → D on W.
- **Factor words tⱼ.** Drawn uniformly, with replacement, from a pool of 351 words: the words of the 820-word dataset [[ds-b25-trivial-2-5reduced-aut8-20261014]] that have 50–80 letters and an R7 certificate (T-018).
  - The dataset words come from the owner's Knuth–Bendix rewrite rules on `b25_full`, under RPO and shortlex orderings. Each is trivial, 2.5-reduced (no subword vᵖ with p ≥ 2.5, so no literal fifth power) and unique up to rotation, inversion and letter automorphisms.
  - 300 of the 351 were used, in 690 picks; no t appears in more than 6 words.
- **The relators behind the t's are simple fifth powers.**
  - Each t's certificate is a product of 118–199 conjugates c⁻¹x⁵c over the R7 table.
  - All 1,630 entries of the table are literal fifth powers x⁵ with 1 ≤ |x| ≤ 7. By period: 1: 108, 2: 104, 3: 236, 4: 194, 5: 540, 6: 132, 7: 316.
  - The substitution sends x⁵ to φ(x)⁵, so every T-028 word is a heavily cancelled product of conjugated fifth powers of period at most 7·∏m.
- **Substitution φ: a → x, b → y.**
  - x and y are uniform random freely reduced words of length m.
  - They are rejection-sampled under the junction rule: last(x), last(y), first(x)⁻¹ and first(y)⁻¹ must be distinct. Then φ(w) is freely and cyclically reduced for every reduced w.
  - x and y must also freely generate a rank-2 subgroup (Stallings folding), so φ is injective; otherwise the index is skipped.
  - C3r2 composes two rounds, φ = φ₂ ∘ φ₁, each with its own (x, y).
- **Signs:** sⱼ = ±1, uniform.
- **Conjugators.**
  - Per factor, 16 random reduced candidates with length uniform in 0..2·∏m; c₁ is empty.
  - The builder keeps the candidate with the most cancellation where factors meet, provided |W| ≥ 0.6 × the uncancelled length.
  - In practice only 0–12 of about 1,700 letters cancel.
- **Seed:** the first 8 bytes of sha256(`20261020|arm|m|index`), with all draws from one PCG64 stream, so every word can be regenerated.
- **CTRL arm (control):** 8–12 conjugated u^{±5} with |u| in 20–30, built to satisfy C′(1/6). Under that condition Dehn's algorithm provably empties every word, and all 30 were emptied as designed.

| Cell | Factors k | Rounds | \|x\| = \|y\| | Conjugator length: allowed / chosen (median, max) | W length (min, median, max) |
|---|---|---|---|---|---|
| C1\|6 | 1 | 1 | 6 | — | 312, 384, 480 |
| C1\|8 | 1 | 1 | 8 | — | 424, 484, 640 |
| C1\|12 | 1 | 1 | 12 | — | 600, 732, 912 |
| C1\|16 | 1 | 1 | 16 | — | 848, 968, 1152 |
| C1\|24 | 1 | 1 | 24 | — | 1224, 1464, 1896 |
| C3\|4 | 3 | 1 | 4 | 0–8 / 4, 8 | 692, 763, 872 |
| C3\|6 | 3 | 1 | 6 | 0–12 / 5, 12 | 1024, 1151, 1290 |
| C3\|9 | 3 | 1 | 9 | 0–18 / 9, 17 | 1531, 1724, 2044 |
| C3r2\|2,2 | 3 | 2 | 2, 2 | 0–8 / 4, 8 | 674, 755, 910 |
| C3r2\|2,3 | 3 | 2 | 2, 3 | 0–12 / 6, 12 | 992, 1151, 1330 |
| C3r2\|3,3 | 3 | 2 | 3, 3 | 0–18 / 8, 18 | 1582, 1690, 1871 |

## 2. Fate per cell

Of the 30 words per cell:
- **Timed out:** hit the phase-A hard cap and were never evaluated.
- **Emptied:** emptied by the T-028 chain.
- **Failed T3u:** a standard solver shortened the end word at the gate.
- **Held-out:** broken by the held-out solvers (T4u).
- **Survivors** split into **broken since**, by any later solver (rev 3–10), and **unbroken** (the 103 candidates).

| Cell | Timed out | Emptied | Failed T3u | Held-out | Survivors | Broken since | **Unbroken** | Unbroken / evaluated |
|---|---|---|---|---|---|---|---|---|
| C1\|6 | 0 | 2 | 4 | 3 | 21 | 18 | **3** | 10% |
| C1\|8 | 0 | 7 | 0 | 2 | 21 | 16 | **5** | 17% |
| C1\|12 | 0 | 0 | 2 | 6 | 22 | 11 | **11** | 37% |
| C1\|16 | 0 | 2 | 0 | 4 | 24 | 7 | **17** | 57% |
| C1\|24 | 11 | 1 | 0 | 3 | 15 | 1 | **14** | 74% |
| C3\|4 | 0 | 0 | 5 | 0 | 25 | 20 | **5** | 17% |
| C3\|6 | 3 | 0 | 2 | 0 | 25 | 14 | **11** | 41% |
| C3\|9 | 16 | 0 | 2 | 0 | 12 | 1 | **11** | 79% |
| C3r2\|2,2 | 0 | 3 | 5 | 7 | 15 | 15 | **0** | 0% |
| C3r2\|2,3 | 0 | 3 | 8 | 0 | 19 | 9 | **10** | 33% |
| C3r2\|3,3 | 4 | 1 | 4 | 0 | 21 | 5 | **16** | 62% |
| **Total** | **34** | **19** | **32** | **25** | **220** | **117** | **103** | 35% |

- **Broken in practice:** C3r2\|2,2 (none left), C1\|6, C1\|8, C3\|4 and CTRL. This rests on our solvers' results; it is not a proof of breakability.
- **Hardest:** C3\|9, C1\|24, C3r2\|3,3 and C1\|16, the cells with the longest W.
- **Never evaluated:** 34 words, 16 of them in C3\|9 and 11 in C1\|24. They are probably among the hardest and are not in the registry.
- **How the 117 survivors broke since:**

  | Route | Breaks |
  |---|---|
  | E4 solver loop with blind-pool insertion | 61 |
  | Beam over insertion chains | 30 |
  | Blind-pool insertion: experiment A, E0 | 9 |
  | algo-mixer | 8 |
  | T-028 fixpoint loops (rev 2) | 5 |
  | Whitehead | 4 |

## 3. Correlations among the 220 survivors

**Length: the only strong predictor.** It holds within every arm.

| Arm | Registry word < 500 letters | 500–799 | ≥ 800 |
|---|---|---|---|
| C1 | 10/46 unbroken | 16/32 | **24/25** |
| C3 | 2/14 | 9/25 | 16/23 |
| C3r2 | 4/18 | 13/26 | 9/11 |

Over all arms, by registry word length:

| Letters | 0–199 | 200–399 | 400–599 | 600–799 | 800–999 | 1000–1199 | 1200–1399 |
|---|---|---|---|---|---|---|---|
| Unbroken | 14% | 14% | 36% | 49% | 81% | 81% | 100% |

**Medians, broken vs unbroken survivors:**

| Feature | Broken | Unbroken | Reading |
|---|---|---|---|
| W length | 774 | 1184 | length |
| Registry word length | 488 | 774 | length |
| Registry word length ÷ W length | 0.7 | 0.7 | **no effect**; also by band and within arms |
| Total t certificate cells | 444 | 338 | no effect within arms (C1 186 vs 167, C3 662 vs 669, C3r2 569 vs 620) |
| Mean t length | 62 | 62 | no effect |
| Total conjugator length | 4 | 6 | weak, confounded (the allowed length grows with m) |
| Letters cancelled where factors meet | 4 | 4 | no effect |

- **Signs (C3, C3r2):** 0, 1, 2 or 3 negative signs give 58%, 41%, 48% and 42% unbroken. No effect.
- **Max period L of the W certificate:** L ≈ 20 gives 13% unbroken, L ≥ 60 gives 78–92%. This is the same effect as m, hence length.
- **Factor word t.**
  - Single t's look striking: line 445 appears in 4 survivors and all are unbroken; line 529 in 5 and all broke.
  - A stratified permutation test (outcomes shuffled within cell × 200-letter band; statistic = variance of the outcome among the words sharing a t; 2,000 shuffles) gives P = 0.085. That is no evidence of a t effect beyond length.
- **Origin of t (RPO vs shortlex rules):** 44% vs 52% unbroken. No effect.
- **C1 words whose t has ≥ 70 letters:** 2 of 15 unbroken. This is confounded: 11 of the 15 are in C1\|6 and C1\|8.

## Caveats

- "Unbroken" means not broken by any solver we have run so far. The solvers favour short words: one insertion step costs about 70 CPU-seconds on a 1,300-letter word. So the length effect is partly a solver-budget effect.
- The 34 timed-out words are left out of every rate; their fate is unknown.
- Only 46 t's appear in 3 or more survivors, so the t test has little power. A t effect smaller than the length effect cannot be ruled out.

## Open questions

1. Are the 34 timed-out words harder than the 103 candidates? Running them through the current solvers would answer it.
2. Does a construction that is not driven by length produce harder words at the same length? For example, a new arm with products of short-period powers (|x| ≤ 7) and heavy overlap, chosen directly rather than through Knuth–Bendix words, matched to C3 in length, signs and conjugators.

## Related material

- [[ds-b25-challenge-candidates]]: the registry; candidates, tested words, certificates.
- [[ds-b25-trivial-2-5reduced-aut8-20261014]]: the 820-word dataset the t-pool comes from.
- [[t028-stage-c-fresh-batch-2026-10-23]]: the T-028 pilot follow-up design.
- [[t002-dataset-relator-products-results]]: the earlier products-of-dataset-words experiment.
- [[challenge-gen-candidate-workflow]]: the gates (T3u, held-out solvers) behind the funnel.
- [[Experiments/Group Theory/B25 Solver/_progress|b25-solver progress]]: the solver experiments that broke the 117 later words.
