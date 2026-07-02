---
tags: [agent/lead, user/maumayma, domain/group-theory, project/b25, topic/word-reduction, topic/reductions-ledger, reference, status/ready-for-review]
author: maumayma
date: 2026-06-26
type: reference-ledger
title: B(2,5) Reductions Ledger — every reduction achieved to date
audience: maumayma
scope: All 119 B(2,5) commutator target words; every reduction method used to date.
authoritative_source: experiments/b25_reduce_core/runs/b25-reduce-core-benchmark-0001/data/best_words/*.txt (stored reduced words — reproducible by re-measurement)
provenance:
  git_sha: 5aeee6a
  benchmark_snapshot: ui/benchmarks_data.json
  seed_rules_run: runs/b25/fragment_seed_rules/20260625_235828/
  seed_rules_sha256: 341c64bc…002499
corpus_totals_reproducible:
  words: 119
  sum_raw_len: 2219014
  sum_best_len: 1504034
  chars_removed: 714980
  aggregate_pct: 32.2
reduction_bands:
  ge_50pct: 15
  band_10_50pct: 67
  lt_10pct: 37
verification:
  word_equality_VERIFIED_chars: 648   # the 31 GAP-verified seed rules, on 37 words
  word_equality_CONJECTURED: "all benchmark best_len reductions (abelianization + lift-KB evidence; GAP KB does not complete on B(2,5))"
  comm_12_9_status: conjectured        # 28652→7245, abelianization-preserved, NOT GAP-proven
data_integrity:
  json_best_len_overclaims: 42         # of 119; JSON best_len < stored reproducible word by 1–24 chars
  rule: "use reproducible best_words/ length (== JSON multipass_len), NOT JSON best_len"
invalidated_excluded: [word_4882, word_3732, word_3707]   # braid_reduce_fast non-abelian-inverse bug; abel (4,4)≠(0,0)
---

# B(2,5) Reductions Ledger — every reduction achieved to date

**One durable record of which target words have been reduced, by how much, how, with which rules — and where the wall still stands.** Built from the reproducible stored words, not from unreproducible JSON records. Reviewed by Maria; future work + external readers build on this.

> [!danger] RETRACTED / UNDER REVIEW — the "119 words proved trivial in B(2,5)" claim is likely CIRCULAR (2026-06-26)
> An earlier annotation here claimed "119/119 GAP-proven = 1 in B(2,5)" and "comm_12_9 upgraded to word-equality proven." **Both are RETRACTED.** The GAP run (`Agents/Validator/scratch/b25_all119_trivial.g`) builds the **finite** group presented by the b25_gen 4372 relators (the exponent-5 law imposed only on words of length ≤ 7) and shows the targets = 1 *in that finite group*. That does **NOT** prove = identity in the **real** B(2,5) (FreeGroup(2) mod w⁵=e for **all** words — the hard, infinite presentation), because: **(a)** the length-≤7 relator set is not established here as a *proven complete* presentation of B(2,5) (no citation yet); and **(b)** if the target commutators are themselves *built from* these relators, then "product of relators = 1" is true **by construction** and proves nothing about the open problem.
> **Proving these commutators = identity in B(2,5) is the OPEN problem** (HWW / Kuznetsov lineage — *conjectured*, not proved; read the source paper). What the GAP run *does* establish: "= 1 in the finite group presented by b25_gen's length-≤7 relators" — pending Validator confirming whether that group is provably B(2,5). The `#status/disproven` proxy-quotient verdict rests on the same computation and is **also under re-examination**. Provisional consequences below are CONTINGENT on the triviality being real:
> 1. **Cayley distance from identity = 0 for all 119.** The proxy-quotient / quotient-as-distance approach is `#status/disproven` for this benchmark (no quotient gives nonzero distance to a trivial element). This is *why* the Q2/Q3/Q4 pilot saw d=0 — correct answer, not artifact.
> 2. **What "reduction" means here:** these are **relator-length / Dehn-complexity** compressions of identity-words — NOT shorter Cayley paths to a non-trivial element.
> 3. **Verification — RETRACTED upgrade:** the earlier claim that `comm_12_9`'s reduction is "word-equality proven (both endpoints = 1)" is withdrawn — it rested on the possibly-circular finite-group computation above. Reduction-path validity was never independently verified either. **Treat all reductions as word-equality CONJECTURED** (the [§ Verification](#verification-status-what-is-actually-proven) section's original "conjectured" framing stands), pending Validator settling the presentation question. See [[b25-q5-feasibility-verdict]] (under re-examination).
>
> [!warning] Two things to read before trusting any number
> 1. **Reproducible vs JSON.** The authoritative best length for each word is the **stored reduced word** in `best_words/*.txt` (you can re-measure and re-verify it). The benchmark JSON's `best_len` column **over-claims on 42/119 words** (by 1–24 chars) — no stored word achieves those lengths. This ledger uses the reproducible stored lengths throughout (which equal the JSON's `multipass_len` field, not its `best_len`). See [§ Data-integrity](#data-integrity-the-json-best_len-over-claim).
> 2. **Verified vs conjectured.** Almost the entire 32.2% aggregate reduction is **word-equality CONJECTURED** — preserved under abelianization and consistent with the lift-KB chain, but **not** proven equal to the original element in B(2,5) (GAP Knuth–Bendix does not complete on B(2,5)). The **only** word-equality-VERIFIED reductions are the **648 chars** from the 31 seed rules on 37 words. See [§ Verification](#verification-status-what-is-actually-proven).

## Headline numbers (reproducible)

| | |
|---|---|
| Target words | 119 B(2,5) commutators `comm_i_j` (Havas–Wall–Wamsley 1974 presentation) |
| Σ original length | 2,219,014 chars |
| Σ best length (reproducible) | 1,504,034 chars |
| Chars removed | **714,980 (32.2% aggregate)** |
| Words reduced ≥50% | 15 |
| Words reduced 10–50% | 67 |
| Words reduced <10% (near floor) | 37 |
| Best single word | `comm_12_9`: 28,652 → 7,245 (**74.7%**) — *conjectured* |
| Word-equality VERIFIED reduction | **648 chars** (31 seed rules, 37 words) — the only proven sliver |
| word_7245 (`comm_12_9`) under verified seed rules | **0** (the standing wall) |

## Verification status — what is actually proven

This is the honest core of the ledger:

- **CONJECTURED (not proven):** every benchmark `best_len` reduction — including the 74.7% on `comm_12_9` — is supported only by (a) abelianization preserved at `(0,0) mod 5` through the pipeline, and (b) the lifted-alphabet KB chain. Abelianization is *necessary not sufficient* (it is blind on the commutator subgroup — the exact failure mode of the [[braid_reduce]] bug). GAP KB does **not** complete on B(2,5), so full word-equality is unavailable for these. Status for `comm_12_9`: `#status/conjectured` (2026-05-22).
- **VERIFIED (GAP word-equality, φ(u)=φ(v)):** only the **31 seed-rule** increments — a further **648 chars** removed from 37 words *below* their benchmark best. These are junction-level rules `CoreA·F·CoreB → shorter`, each individually GAP-verified. They are the only reductions in this corpus proven equal in the group.
- **EXCLUDED (invalidated):** `word_4882`, `word_3732`, `word_3707` and all rule banks derived from them — poisoned by the `braid_reduce_fast` non-abelian-inverse bug (abelianization diverged to `(4,4) mod 5`; wrong group elements). Not counted anywhere here.

**Takeaway for Maria:** we have large *conjectured* reductions and a tiny *verified* one. Closing the verified/conjectured gap (a working B(2,5) word-equality oracle) is the highest-leverage missing capability — every headline number above is conjectured until then.

## Data-integrity — the JSON `best_len` over-claim

`ui/benchmarks_data.json` carries two length fields: `best_len` and `multipass_len`. On **42 of 119 words**, `best_len` is **smaller than the actual stored word** (`best_words/*.txt`) by 1–24 chars, while `multipass_len` matches the stored word exactly. So `best_len` is an **unreproducible record** — a claim no stored word backs. Per the standing data-integrity rule, this ledger uses the stored reproducible length. The 42 over-claims (sorted by gap):

| word | JSON best_len | reproducible | gap |
|---|---|---|---|
| comm_16_2 | 22397 | 22421 | 24 |
| comm_6_3 | 16836 | 16853 | 17 |
| comm_9_8 | 20246 | 20261 | 15 |
| comm_8_5 | 21069 | 21083 | 14 |
| comm_14_3 | 22373 | 22386 | 13 |
| comm_8_6 | 20143 | 20156 | 13 |
| comm_15_2 | 22137 | 22150 | 13 |
| comm_6_1 | 21019 | 21031 | 12 |
| comm_10_9 | 9634 | 9644 | 10 |
| comm_15_5 | 20432 | 20442 | 10 |
| comm_17_4 | 14549 | 14558 | 9 |
| comm_12_3 | 15027 | 15036 | 9 |
| comm_17_2 | 20167 | 20174 | 7 |
| comm_6_5 | 23705 | 23711 | 6 |
| (28 more, gap 1–4) | … | … | … |

**Recommended fix (your call, not done):** repoint `benchmarks_data.json` headline `best_len` to `multipass_len` (or re-run the missing passes to actually produce the claimed shorter words and store them). Until then, treat the stored-word lengths in this ledger as truth.

## Full per-word table (119 words, reproducible best, sorted by % reduction)

Method is the pipeline recorded in the benchmark snapshot. `JSON over-claim` flags words where the JSON `best_len` is unreproducibly shorter than the stored word.

| word | raw_len | best (repro) | % red | method | JSON over-claim |
|---|---|---|---|---|---|
| comm_12_9 | 28652 | 7245 | 74.71 | rust beam 4-pass |  |
| comm_13_6 | 24246 | 6191 | 74.47 | Rust beam + 7M historical rules | json=6188 (−3) |
| comm_20_4 | 29156 | 7743 | 73.44 | rust beam 4-pass |  |
| comm_20_5 | 19680 | 5390 | 72.61 | Rust beam + 7M historical rules | json=5389 (−1) |
| comm_26_4 | 20248 | 5947 | 70.63 | rust beam 4-pass |  |
| comm_11_10 | 21620 | 7314 | 66.17 | rust beam 4-pass |  |
| comm_23_2 | 32286 | 11830 | 63.36 | Rust beam + 7M historical rules | json=11827 (−3) |
| comm_21_4 | 24384 | 10058 | 58.75 | rust beam 4-pass |  |
| comm_9_6 | 27334 | 11358 | 58.45 | rust beam 4-pass |  |
| comm_12_7 | 8456 | 3698 | 56.27 | rust beam 4-pass |  |
| comm_4_3 | 27796 | 13016 | 53.17 | rust beam 4-pass |  |
| comm_8_7 | 27390 | 13063 | 52.31 | rust beam 4-pass |  |
| comm_12_4 | 22302 | 10910 | 51.08 | rust beam 4-pass |  |
| comm_17_3 | 17538 | 8610 | 50.91 | Rust beam + 7M historical rules | json=8609 (−1) |
| comm_25_2 | 14236 | 7098 | 50.14 | rust beam 4-pass |  |
| comm_24_2 | 14302 | 7171 | 49.86 | rust beam 4-pass |  |
| comm_16_3 | 17050 | 8618 | 49.45 | rust beam 4-pass |  |
| comm_7_4 | 41228 | 20930 | 49.23 | rust beam 4-pass |  |
| comm_5_4 | 29390 | 15135 | 48.5 | rust beam 4-pass |  |
| comm_7_5 | 17932 | 9544 | 46.78 | rust beam 4-pass |  |
| comm_14_5 | 19196 | 10258 | 46.56 | Rust beam + 7M historical rules | json=10256 (−2) |
| comm_16_2 | 41886 | 22421 | 46.47 | Multi-pass Rust beam + 25M biased rules (new record) | json=22397 (−24) |
| comm_11_8 | 15616 | 8435 | 45.98 | rust beam 4-pass |  |
| comm_20_3 | 16074 | 8886 | 44.72 | rust beam 4-pass |  |
| comm_11_2 | 29578 | 16408 | 44.53 | rust beam 4-pass |  |
| comm_10_7 | 24442 | 13727 | 43.84 | rust beam 4-pass |  |
| comm_11_3 | 20840 | 11717 | 43.78 | rust beam 4-pass |  |
| comm_26_2 | 8340 | 4761 | 42.91 | rust beam 4-pass |  |
| comm_15_3 | 25444 | 14610 | 42.58 | rust beam 4-pass |  |
| comm_29_2 | 16758 | 9627 | 42.55 | rust beam 4-pass |  |
| comm_15_8 | 16970 | 9812 | 42.18 | Rust beam + 7M historical rules | json=9808 (−4) |
| comm_18_7 | 16984 | 9825 | 42.15 | Rust beam + 7M historical rules | json=9822 (−3) |
| comm_17_7 | 17004 | 9846 | 42.1 | rust beam 4-pass |  |
| comm_16_8 | 17012 | 9852 | 42.09 | Rust beam + 7M historical rules | json=9851 (−1) |
| comm_17_2 | 34770 | 20174 | 41.98 | Rust beam + 7M historical rules | json=20167 (−7) |
| comm_8_2 | 20796 | 12258 | 41.06 | rust beam 4-pass |  |
| comm_6_5 | 39410 | 23711 | 39.84 | Rust beam + 7M historical rules | json=23705 (−6) |
| comm_10_6 | 18834 | 11520 | 38.83 | rust beam 4-pass |  |
| comm_7_3 | 28750 | 17726 | 38.34 | Rust beam + 7M historical rules | json=17725 (−1) |
| comm_7_2 | 37070 | 23001 | 37.95 | Rust beam + 7M historical rules | json=23000 (−1) |
| comm_9_5 | 18818 | 11678 | 37.94 | rust beam 4-pass |  |
| comm_6_3 | 26962 | 16853 | 37.49 | Rust beam + 7M historical rules | json=16836 (−17) |
| comm_8_6 | 32200 | 20156 | 37.4 | Rust beam + 7M historical rules | json=20143 (−13) |
| comm_10_5 | 14062 | 8991 | 36.06 | rust beam 4-pass |  |
| comm_18_3 | 28224 | 18086 | 35.92 | rust beam 4-pass |  |
| comm_25_3 | 20192 | 13050 | 35.37 | rust beam 4-pass |  |
| comm_12_6 | 20414 | 13270 | 35.0 | rust beam 4-pass |  |
| comm_13_4 | 29508 | 19309 | 34.56 | rust beam 4-pass |  |
| comm_6_2 | 26852 | 17798 | 33.72 | Rust beam + 7M historical rules | json=17797 (−1) |
| comm_12_5 | 14416 | 9623 | 33.25 | rust beam 4-pass |  |
| comm_15_2 | 32720 | 22150 | 32.3 | Rust beam + 7M historical rules | json=22137 (−13) |
| comm_27_2 | 15468 | 10682 | 30.94 | rust beam 4-pass |  |
| comm_27_4 | 15480 | 10690 | 30.94 | rust beam 4-pass |  |
| comm_25_5 | 15488 | 10704 | 30.89 | rust beam 4-pass |  |
| comm_9_4 | 18574 | 13075 | 29.61 | Rust beam + 7M historical rules | json=13072 (−3) |
| comm_9_8 | 28614 | 20261 | 29.19 | Rust beam + 7M historical rules | json=20246 (−15) |
| comm_11_4 | 19266 | 13807 | 28.33 | Rust beam + 7M historical rules | json=13803 (−4) |
| comm_8_4 | 22674 | 16257 | 28.3 | rust beam 4-pass |  |
| comm_13_5 | 19204 | 13802 | 28.13 | rust beam 4-pass |  |
| comm_16_4 | 21970 | 15790 | 28.13 | rust beam 4-pass |  |
| comm_9_7 | 24052 | 17406 | 27.63 | rust beam 4-pass |  |
| comm_6_4 | 16408 | 11878 | 27.61 | rust beam 4-pass |  |
| comm_4_2 | 23298 | 16901 | 27.46 | Rust beam + 7M historical rules | json=16897 (−4) |
| comm_8_3 | 23420 | 17678 | 24.52 | Rust beam + 7M historical rules | json=17677 (−1) |
| comm_10_8 | 17922 | 13738 | 23.35 | rust beam 4-pass |  |
| comm_12_3 | 19560 | 15036 | 23.13 | Lift→coreless→beam (new pipeline) | json=15027 (−9) |
| comm_6_1 | 27204 | 21031 | 22.69 | Rust beam + 7M historical rules | json=21019 (−12) |
| comm_10_3 | 31546 | 24636 | 21.9 | rust beam 4-pass |  |
| comm_14_7 | 16830 | 13238 | 21.34 | Rust beam + 7M historical rules | json=13236 (−2) |
| comm_12_8 | 16834 | 13242 | 21.34 | rust beam 4-pass |  |
| comm_9_3 | 25798 | 20524 | 20.44 | rust beam 4-pass |  |
| comm_14_3 | 28058 | 22386 | 20.22 | Rust beam + 7M historical rules | json=22373 (−13) |
| comm_13_3 | 33328 | 27340 | 17.97 | rust beam 4-pass |  |
| comm_19_3 | 13682 | 11275 | 17.59 | Rust beam + 7M historical rules | json=11271 (−4) |
| comm_12_2 | 32250 | 26644 | 17.38 | Rust beam + 7M historical rules | json=26643 (−1) |
| comm_8_5 | 24974 | 21083 | 15.58 | Rust beam + 7M historical rules | json=21069 (−14) |
| comm_15_4 | 8820 | 7551 | 14.39 | Rust beam + 7M historical rules | json=7550 (−1) |
| comm_18_6 | 16954 | 14537 | 14.26 | rust beam 4-pass |  |
| comm_17_6 | 16966 | 14548 | 14.25 | rust beam 4-pass |  |
| comm_5_3 | 23520 | 20307 | 13.66 | Rust beam + 7M historical rules | json=20304 (−3) |
| comm_14_2 | 18856 | 16432 | 12.86 | rust beam 4-pass |  |
| comm_7_6 | 18228 | 16379 | 10.14 | Rust beam + 7M historical rules | json=16377 (−2) |
| comm_10_4 | 17156 | 15586 | 9.15 | rust beam 4-pass |  |
| comm_19_2 | 10712 | 10074 | 5.96 | rust beam 4-pass |  |
| comm_11_5 | 15766 | 15141 | 3.96 | rust beam 4-pass |  |
| comm_14_6 | 9666 | 9618 | 0.5 | rust beam 4-pass |  |
| comm_11_7 | 3792 | 3777 | 0.4 | rust beam 4-pass |  |
| comm_20_2 | 10716 | 10673 | 0.4 | rust beam 4-pass |  |
| comm_16_7 | 9840 | 9803 | 0.38 | rust beam 4-pass |  |
| comm_15_7 | 9802 | 9767 | 0.36 | rust beam 4-pass |  |
| comm_16_5 | 5072 | 5054 | 0.35 | rust beam 4-pass |  |
| comm_11_1 | 3756 | 3744 | 0.32 | rust beam 4-pass |  |
| comm_32_2 | 14270 | 14225 | 0.32 | rust beam 4-pass |  |
| comm_21_3 | 11294 | 11259 | 0.31 | rust beam 4-pass |  |
| comm_19_5 | 14826 | 14781 | 0.3 | rust beam 4-pass |  |
| comm_30_2 | 14278 | 14239 | 0.27 | rust beam 4-pass |  |
| comm_13_9 | 12104 | 12073 | 0.26 | rust beam 4-pass |  |
| comm_26_1 | 3576 | 3567 | 0.25 | rust beam 4-pass |  |
| comm_17_4 | 14592 | 14558 | 0.23 | Lift→coreless→beam (new pipeline) | json=14549 (−9) |
| comm_13_7 | 16836 | 16798 | 0.23 | rust beam 4-pass |  |
| comm_15_5 | 20490 | 20442 | 0.23 | Lift→coreless→beam (new pipeline) | json=20432 (−10) |
| comm_27_3 | 10710 | 10686 | 0.22 | rust beam 4-pass |  |
| comm_14_4 | 12650 | 12623 | 0.21 | rust beam 4-pass |  |
| comm_21_5 | 5370 | 5359 | 0.2 | rust beam 4-pass |  |
| comm_26_3 | 8340 | 8323 | 0.2 | rust beam 4-pass |  |
| comm_14_9 | 4966 | 4957 | 0.18 | rust beam 4-pass |  |
| comm_16_10 | 9908 | 9890 | 0.18 | Power + braid + greedy rules | json=9887 (−3) |
| comm_10_9 | 9660 | 9644 | 0.17 | Power + braid + greedy rules | json=9634 (−10) |
| comm_16_1 | 9828 | 9811 | 0.17 | Power + braid + greedy rules | json=9808 (−3) |
| comm_18_9 | 9876 | 9859 | 0.17 | Power + braid + greedy rules | json=9858 (−1) |
| comm_17_5 | 13424 | 13401 | 0.17 | Power + braid + greedy rules | json=13399 (−2) |
| comm_13_10 | 2500 | 2496 | 0.16 | Power + braid + greedy rules | json=2494 (−2) |
| comm_12_10 | 4972 | 4964 | 0.16 | rust beam 4-pass |  |
| comm_13_8 | 6144 | 6134 | 0.16 | rust beam 4-pass |  |
| comm_18_4 | 7452 | 7440 | 0.16 | Power + braid + greedy rules | json=7438 (−2) |
| comm_15_10 | 9872 | 9856 | 0.16 | Power + braid + greedy rules | json=9854 (−2) |
| comm_17_9 | 9896 | 9880 | 0.16 | rust beam 4-pass |  |
| comm_22_4 | 10126 | 10110 | 0.16 | rust beam 4-pass |  |
| comm_22_3 | 4162 | 4156 | 0.14 | rust beam 4-pass |  |

### The wall — 37 words at <10% (near floor)

Everything below `comm_10_4` (9.15%) sits at ≤6% and most at ~0.1–0.5%. These are short or already-tight words where the beam + historical rules barely move the needle. **They are not "irreducible"** — they are "no further shortening found at the bank/beam budget tested" (upper-bound). The shortest-fragment seed rules (below) reach some of them.

## How the headline reduction was achieved — `comm_12_9` → 7,245 (74.7%, conjectured)

The deepest single reduction, documented chain (`experiments/b25_reduce_core/corrected/README.md`):

```
[c12,c9] original (Havas relator-verified input)   28,652
lift to {a,b,m}                                        544
coreless {a,b}                                      15,328
power reduction                                     10,624
fixed braid_reduce                                   8,402
Python KB rules                                      8,394
Rust braid_reduce                                    8,388
Rust beam search (FINAL, stored)                     7,245   ← best_words/comm_12_9.txt
```

Abelianization `(0,0) mod 5` preserved at every stage. **Word-equality: conjectured** (`#status/conjectured`) — sub-claim "input is a B(2,5) identity" is relator-verified; "final = original element" is *not* proven beyond abelianization (GAP KB non-completion). Under the **verified** 31 seed rules, `comm_12_9` reduces by **0** further — it is the standing hard target ("word_7245").

## Rules that participated

### A. The 31 seed rules (the only GAP-word-equality-VERIFIED reductions)

Junction-level rules `CoreA·F·CoreB → shorter`, discovered by the complete fragment enumeration (318 connectors + 326 junctions across all 119 words; 500K shortlex KB + braid_reduce beam). **31 of 31 fired**, across **37 distinct words**, removing **648 chars** net (649 gross firings; 1-char overlap). Ranked by chars saved:

| rank | fragment | orient | Δ/match | times fired | chars saved | words helped |
|---|---|---|---|---|---|---|
| 1 | `abABA` | A→B | −1 | 245 | 245 | 37 |
| 2 | `abaBA` | A→B | −1 | 233 | 233 | 34 |
| 3 | `ababABABA` | A→B | −2 | 28 | 56 | 12 |
| 4 | `ababaBABA` | A→B | −2 | 21 | 42 | 12 |
| 5 | `ababABAA` | A→B | −1 | 11 | 11 | 11 |
| 6 | `ababAABA` | A→B | −1 | 11 | 11 | 11 |
| 7 | `aabaaBABA` | A→B | −1 | 9 | 9 | 9 |
| 10 | `ababaaBBABA` | A→B | −2 | 2 | 4 | 2 |
| 8 | `aabaBABA` | A→B | −1 | 4 | 4 | 4 |
| 9 | `abaabAAABA` | A→B | −1 | 4 | 4 | 4 |
| 11 | `ababAABAA` | A→B | −1 | 3 | 3 | 3 |
| 12–16 | (short frags, len 8–12) | A→B | −1/−2 | 1 each | 2 each | 1 each |
| 17–31 | (long junction frags, len 39–1107) | A→B / PREFIX / SUFFIX | −1 | 1 each | 1–2 each | 1 each |

**Structural reading:** two short fragments — `abABA` and `abaBA` — do **96% of the work** (478 of 649 firings). Reduction here is dominated by a couple of high-frequency short junction patterns; the 15 long-fragment rules (ranks 17–31) are essentially word-specific one-shots. Full rule LHS→RHS in `runs/b25/fragment_seed_rules/20260625_235828/seed_rules.json`.

### B. Benchmark pipeline methods (conjectured reductions)

How the 119-word best lengths were reached (method distribution):

| method | words | verified? |
|---|---|---|
| rust beam 4-pass | 77 | conjectured |
| Rust beam + 7M historical rules | 30 | conjectured |
| Power + braid + greedy rules | 8 | conjectured |
| Lift→coreless→beam (new pipeline) | 3 | conjectured |
| Multi-pass Rust beam + 25M biased rules (record) | 1 (`comm_16_2`) | conjectured |

A separate `rule_analysis.json` records the benchmark KB top rules by breadth (e.g. `babbabABAB→BABBABaba`, fired in 96/119 words, 792 matches) — but these are aggregate KB-bank rules, not individually word-equality-verified; they belong to the conjectured tier.

## Provenance & reproduction

- **Authoritative lengths:** `wc`-style char count of `experiments/b25_reduce_core/runs/b25-reduce-core-benchmark-0001/data/best_words/comm_*.txt` (strip trailing newline). Originals: `…/data/words/comm_*.txt`.
- **Seed rules + per-word firings:** `runs/b25/fragment_seed_rules/20260625_235828/` (`seed_rules.json`, `per_word_results.json`, `provenance.json`); git `5aeee6a`; rules sha256 `341c64bc…`.
- **`comm_12_9` chain:** `experiments/b25_reduce_core/corrected/` (README + stage files + `final_beam.txt`).
- **Benchmark snapshot (with the over-claiming `best_len`):** `ui/benchmarks_data.json` — use its `multipass_len`, not `best_len`.

## Open / not closed (per the no-premature-close rule)

This ledger documents the **state**, it does not close any line. Untested / open:
1. **Word-equality oracle** — the dominant gap; nearly all reductions are conjectured. A working B(2,5) equality check would promote (or refute) every headline number.
2. **`best_len` reconciliation** — repoint to `multipass_len` or produce+store the claimed shorter words (42 words).
3. **word_7245 / `comm_12_9`** — 0 under verified rules; live leads are the centralizer-reshape mechanism (ITEM 2b, pending the full 1.95M enumeration) and a fresh RL harness (later).
4. **Seed-rule promotion** — the 648 verified chars are a family toolkit; a pre-registered biased-KB + beam family run is the natural next step.

---
*Lead-authored consolidation, 2026-06-26. Numbers reproducible from the stored words; verification tier stated per reduction. Routed to Maria for review; math-verification claims remain Validator's verdict.*
