---
title: Fragment Shortening Hunt — Results
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: fragment-shortening-hunt
date: 2026-06-25
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, project/b25, status/complete, results]
---

# Fragment Shortening Hunt — Results

**Status**: complete. All 119 words tested. 31 seed rules confirmed + applied.

**Methodology**: [[Fragment Shortening Hunt/methodology/fragment-shortening-hunt-b25-2026-06-25]]
**Data**: [[Fragment Shortening Hunt/data/fragment-shortening-hunt-data]]
**Run dir**: `runs/b25/fragment_seed_rules/20260625_235828/`
**Provenance**: git `5aeee6a`, rules SHA `341c64bc...`

---

## Summary

| Metric | Value |
|--------|-------|
| Corpus size | 119 words |
| Distinct fragments enumerated | 318 |
| Junction tests run | 326 |
| Seed rules found (GAP verified) | 31 |
| Words reduced | 37 / 119 |
| Words unaffected | 82 / 119 (including word_7245) |
| Total chars saved | 648 |
| word_7245 savings | **0** (upper bound at bank + beam tested) |

---

## Per-word reduction table — affected words (37/119)

Application method: leftmost fixed-point string rewrite, longest-LHS-first ordering, max 200 iterations. All 31 rules applied simultaneously.

| word_id | before | after | delta | % saved | primary rules |
|---------|--------|-------|-------|---------|---------------|
| comm_16_2 | 22,421 | 22,380 | −41 | 0.18% | #1,#2,#3,#4,#5 |
| comm_8_6 | 20,156 | 20,118 | −38 | 0.19% | #1,#2,#3,#4,#5 |
| comm_7_3 | 17,726 | 17,695 | −31 | 0.17% | #1,#2,#3,#4,#5 |
| comm_6_3 | 16,853 | 16,823 | −30 | 0.18% | #1,#2,#3,#4,#12 |
| comm_14_3 | 22,386 | 22,358 | −28 | 0.13% | #1,#2,#3,#4,#15 |
| comm_6_1 | 21,031 | 21,003 | −28 | 0.13% | #1,#2,#3,#4,#5 |
| comm_8_5 | 21,083 | 21,055 | −28 | 0.13% | #1,#2,#3,#4 |
| comm_5_3 | 20,307 | 20,280 | −27 | 0.13% | #1,#2,#6,#8,#9 |
| comm_7_4 | 20,930 | 20,904 | −26 | 0.12% | #1,#2,#3,#4,#8 |
| comm_12_2 | 26,644 | 26,620 | −24 | 0.09% | #1,#2,#5,#6,#9 |
| comm_17_2 | 20,174 | 20,150 | −24 | 0.12% | #1,#2,#3,#4,#6 |
| comm_18_3 | 18,086 | 18,064 | −22 | 0.12% | #1,#2,#3,#4,#6 |
| comm_11_2 | 16,408 | 16,387 | −21 | 0.13% | #1,#2,#5,#7 |
| comm_6_5 | 23,711 | 23,690 | −21 | 0.09% | #1,#2,#3,#4,#5 |
| comm_15_2 | 22,150 | 22,130 | −20 | 0.09% | #1,#2,#5,#6,#13 |
| comm_9_8 | 20,261 | 20,241 | −20 | 0.10% | #1,#2,#3,#4 |
| comm_13_3 | 27,340 | 27,321 | −19 | 0.07% | #1,#2,#8 |
| comm_8_3 | 17,678 | 17,659 | −19 | 0.11% | #1,#2,#7,#9 |
| comm_12_3 | 15,036 | 15,019 | −17 | 0.11% | #1,#2,#6,#11 |
| comm_4_2 | 16,901 | 16,885 | −16 | 0.09% | #1,#2,#6,#19,#24 |
| comm_10_3 | 24,636 | 24,621 | −15 | 0.06% | #1,#2,#5,#7 |
| comm_5_4 | 15,135 | 15,120 | −15 | 0.10% | #1,#2,#9,#17 |
| comm_7_2 | 23,001 | 22,986 | −15 | 0.07% | #1,#2,#7,#11,#23 |
| comm_9_4 | 13,075 | 13,061 | −14 | 0.11% | #1,#2,#5 |
| comm_14_2 | 16,432 | 16,419 | −13 | 0.08% | #1,#2,#6 |
| comm_9_3 | 20,524 | 20,511 | −13 | 0.06% | #1,#2,#7,#22 |
| comm_4_3 | 13,016 | 13,004 | −12 | 0.09% | #1,#2,#7,#26 |
| comm_6_2 | 17,798 | 17,786 | −12 | 0.07% | #1,#2,#6,#7,#28 |
| comm_15_5 | 20,442 | 20,432 | −10 | 0.05% | #1,#2,#29 |
| comm_13_4 | 19,309 | 19,302 | −7 | 0.04% | #1,#2 |
| comm_8_4 | 16,257 | 16,252 | −5 | 0.03% | #1,#2,#6 |
| comm_9_7 | 17,406 | 17,401 | −5 | 0.03% | #1,#2 |
| comm_10_6 | 11,520 | 11,516 | −4 | 0.03% | #1,#2,#5 |
| comm_8_2 | 12,258 | 12,255 | −3 | 0.02% | #1,#8 |
| comm_10_7 | 13,727 | 13,725 | −2 | 0.01% | #1,#2 |
| comm_16_4 | 15,790 | 15,788 | −2 | 0.01% | #1,#18 |
| comm_8_7 | 13,063 | 13,062 | −1 | 0.01% | #1 |

**Primary rules column**: top rules by (|delta_per_application| × count_in_original_word), up to 5 shown.

---

## word_7245 — explicit null result

word_7245 (comm_12_9, 7,245 chars) returns **delta=0** under all methods tested:

| Method | Budget | Result |
|--------|--------|--------|
| 500K shortlex KB (leftmost) | — | delta=0 |
| k=12 BFS (exact for len ≤ 12) | — | all 9 fragments confirmed in shortlex NF |
| braid_reduce beam, junction words | 60s each (9 junctions) | delta=0 at all |
| braid_reduce beam, full word_7245 | 3 passes × 300s | delta=0 at all passes |

**This is an upper bound, not an irreducibility claim.** Specifically: "no shortening found at 499,864-rule shortlex bank + braid_reduce beam (width 16384, ≤300s per pass)". Untested variants that could still find reductions are listed in the methodology note.

---

## Key findings

### Rules #1 and #2 dominate

- Rule #1 (`abABA`, A→B, delta=−1): applies in 245 junction positions across the corpus; fires in 36 of 37 reduced words.
- Rule #2 (`abaBA`, A→B, delta=−1): applies in 233 junction positions; fires in 35 of 37 reduced words.
- Together they account for the majority of the 648-char savings. Rules #3–31 provide additional savings but are not the primary mechanism.

### The reduced words are not word_7245's family

word_7245 (comm_12_9) is NOT among the 37 reduced words. The words that benefit most (comm_16_2: −41, comm_8_6: −38, comm_7_3: −31) are different commutator pairs. This is consistent with word_7245's specific connector fragments (`a, A, aBA, abA, abaBABA, ababABA, ababbABBABA, ababbaBABA, ababbaBBABA`) not matching the junction patterns that reduce.

### 50K vs 500K bank: no additional rules from the larger bank

Running the same enumeration with 499,864 rules vs. 49,576 rules produces identical results (31/326 reductions). The 450K additional rules contribute 0 new junction reductions. This suggests the applicable rules are concentrated in the lower-frequency tail of the shortlex ordering and the larger bank provides no additional coverage for these junction patterns.

### No beam-only reductions

The braid_reduce beam (width 16384, up to 300s) found 0 reductions not already in the KB bank. All 31 rules were found by the 500K bank; beam added nothing. This could indicate: (a) the junction reductions are shallow (reachable in 1–2 rule applications from the bank), or (b) the beam width/time budget was insufficient for deeper reductions.

---

## Unaffected words (82/119) — not closures

The following 82 words show delta=0 under the 31 rules. These are upper bounds at the methods tested, not claims of irreducibility:

comm_10_4, comm_10_5, comm_10_8, comm_10_9, comm_11_1, comm_11_10, comm_11_3, comm_11_4, comm_11_5, comm_11_7, comm_11_8, comm_12_10, comm_12_4, comm_12_5, comm_12_6, comm_12_7, comm_12_8, **comm_12_9** (word_7245), comm_13_10, comm_13_5, comm_13_6, comm_13_7, comm_13_8, comm_13_9, comm_14_4, comm_14_5, comm_14_6, comm_14_7, comm_14_9, comm_15_10, comm_15_3, comm_15_4, comm_15_7, comm_15_8, comm_16_1, comm_16_10, comm_16_3, comm_16_5, comm_16_7, comm_16_8, comm_17_3, comm_17_4, comm_17_5, comm_17_6, comm_17_7, comm_17_9, comm_18_4, comm_18_6, comm_18_7, comm_18_9, comm_19_2, comm_19_3, comm_19_5, comm_20_2, comm_20_3, comm_20_4, comm_20_5, comm_21_3, comm_21_4, comm_21_5, comm_22_3, comm_22_4, comm_23_2, comm_24_2, comm_25_2, comm_25_3, comm_25_5, comm_26_1, comm_26_2, comm_26_3, comm_26_4, comm_27_2, comm_27_3, comm_27_4, comm_29_2, comm_30_2, comm_32_2, comm_6_4, comm_7_5, comm_7_6, comm_9_5, comm_9_6

---

## Math claims

No new math claims generated. All 31 seed rules are direct outputs of the shortlex KB (a sound rewriting system for B(2,5)): their correctness is guaranteed by KB soundness (rules fire only when LHS = RHS in the group). GAP verification was run as belt-and-suspenders confirmation.

No Validator routing needed for the rules themselves. The aggregate result (37 words shortened, 648 chars saved) is a computational fact, not a math claim requiring verification.

---

## Next steps (not closed)

- The 37 reduced words could be used as new seeds for a biased kbprog run (pre-registration needed; not started).
- The 31 rules could be incorporated into the braid_reduce binary's forward rule set for future beam runs (requires Developer lane work — file requirement to Lead).
- word_7245's connectors remain untested at larger beam widths, more passes, or RPO/wtlex rule banks. None of these are exhausted.
