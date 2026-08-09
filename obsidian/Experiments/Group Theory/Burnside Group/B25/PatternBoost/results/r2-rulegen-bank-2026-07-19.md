---
title: "R2 Rulegen — Delivered Rule Bank (kbprog, 2026-07-19)"
date: 2026-07-19
domain: group-theory
project: b25
instance: b25-loop-v1
experiment_type: patternboost
author: maumayma
status: pending
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/knuth-bendix, project/b25, status/pending, results]
---

# R2 Rule-bank Generation — Delivered Bank

Executed locked spec [[R2_rulegen_param_sheet]] (Lead-authorized, Maria-signed axplorer v1 verdict).
Provenance: [[r2-rulegen-launch-2026-07-19]]. Run dir `runs/b25/patternboost_rulegen/20260719_193749/`.
Bank artifacts under `.../bank/`. **No commit** (Lead + Maria gate).

## Headline (for the Lead → Maria decision)

- **Primary scoring bank: 378 rules** admitted (Δ<0, LHS≤12, deduped over 3 shortlex orderings, 2.77M raw eqns).
- **368 distinct rules FIRE on the 12k held-out pool → BELOW the ≥500 pre-registered GO floor (§5).**
  This is a REAL supply finding, not engineered around: under the locked LHS≤12 shortlex constraint the
  short-rule supply saturates at ~378. Per Lead's framework this is a proceed-with-sub-floor-bank vs
  adjust-strategy decision for Maria (pre-reg deviation, her gate).
- **Size-cap is NON-BINDING:** braid_reduce per-call latency is **flat 19 ms at N=31/100/200/378** — 378
  rules is 3 orders of magnitude below the ~250k-pattern / 6 s AC-rebuild regime. Recommend using the
  **full 378-rule bank** (no latency penalty, no coverage loss).
- **Enabler bucket: 15 §7-validated** grow-to-shrink rules (of 707 candidates); **scorer ∩ enabler = ∅ ✓.**
- vs the 31-rule seed bank: 378 primary (368 firing) is >10× richer; whether it BEATS the seed bank on
  reduction is the v1a A/B (Developer). Even sub-floor, this bank + 15 enablers gives v1a real material.

## 1. Generation & halt

4 kbprog at cap (3 biased shortlex PRIMARY + 1 RPO diagnostic). **Plateau-halt at ~1h** (Lead latitude):
the Δ<0 LHS≤12 count was flat 263→264 per ordering from t≈7min to t≈56min while eqns nearly doubled
(730k→1.3M) — **short rules saturate within ~7 min; they do NOT accrue late.** Running to the 4h wall
would have added ~0 short rules. Graceful SIGINT halt, all output written.

| run | final eqns | len≤12 | Δ<0 | Δ=0 |
|---|--:|--:|--:|--:|
| slex_aAbB_k5 | 1.30M | 475 | 265 | 210 |
| slex_bBaA_k5 | 1.33M | 474 | 265 | 209 |
| slex_aAbB_k6 | 0.94M | 462 | 261 | 201 |
| **union (deduped)** | 2.77M | — | **378** | 329 |

## 2. Primary bank (Δ<0, LHS≤12, deduped, firing-ranked)

- Admitted: **378**. Distinct-firing on held-out: **368** (10 non-firing → secondary tier).
- Firing distribution: 51 rules fire ≥100×, 168 ≥10×, 368 ≥1×. Top firers are power/short rules
  (`bbb→BB` 11 100×, `aaa→AA` 10 492×, `abbabbab→BBABBAB` 2 683×).
- **LHS length distribution — INVERTED vs §6.9 targets:**

| LHS len | 3 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|--:|--:|--:|--:|--:|--:|--:|
| count (union) | ~4 | — | — | — | — | — | (bulk) |
| pct in 5–8 | **10.6%** (target 70%) | | pct ≤10 | **29.6%** (target 90%) | | pct ≤12 | 100% ✓ |

  The admitted rules cluster at the len-11/12 cap; genuine short (5–8) algebraic rules are scarce. Real
  structural finding — the short-rule supply is both LIMITED (378) and LONG-skewed.

Files: `bank/primary_bank_ranked.rules` (378, firing-annotated), `bank/clean_top{31,100,200,378}.rules`
(comment-free, for the reducer), `bank/secondary_tier_nonfiring.rules` (10 non-firing, kept not deleted).

## 3. Latency tradeoff (braid_reduce --no-beam, 513-char sample word, min of 3)

| N (rules) | 31 | 100 | 200 | 378 (full) |
|---|--:|--:|--:|--:|
| per-call wall | 0.019s | 0.019s | 0.019s | 0.019s |

**Flat.** AC construction for ≤378 patterns is sub-ms; the 19 ms is process+reduction, not rule-file size.
The size-cap concern only bites at ~250k patterns. **Recommendation: ship the full 378-rule bank.**

## 4. Enabler bucket (§7 grow-to-shrink, separate from scorer)

- Candidates (Δ=0 length-preserving + reversed Δ<0 giving Δ≤+4): 707.
- **§7-validated: 15** (delivered figure). Examples: `aa→AAA` (a²=a⁻³), `bb→BBB`, `bbabbab→ABBABBAB`,
  `ABABA→babab`.
- **scorer ∩ enabler = ∅** (verified on the delivered files). Enablers NEVER enter the scoring bank.
- File: `bank/enabler_bucket_s7.rules`.

> **PINNED HARNESS CORRECTION (Validator flag, 2026-07-19).** The §7 net-shrinkage cleanup **MUST run
> WITH the primary bank** — `braid_reduce --no-beam --rules-file <primary bank>` (or, in the Python
> harness, `bank_cleanup(w, primary)`). An enabler's job is to **unlock a primary-bank firing**, so a
> **bankless** cleanup shows 0 shrink and wrongly rejects valid enablers. The delivered **15** was
> computed with a bankless cleanup (free+braid/power only) → it is a **conservative LOWER BOUND**; the
> bank-aware count is ≥15. Validator confirmed all 3 spot-checked enablers clear §7 **with the bank**.
> `admit_rank.py` is now bank-aware (`bank_cleanup`); a bank-aware recount is folded into Part C
> (no standalone re-run per Lead). Bank soundness: **#status/replicated** — all 393 rules independently
> GAP-verified (Validator Part B).

## 5. RPO diagnostic (SEPARATE — never in scoring/enabler bank)

`rpo_aAbB_diag` (`-rec`, **unbiased** — biased+`-rec` crashes, flagged collision): 1.49M eqns but only
**12 rules with LHS≤12** (2 Δ<0, 4 Δ=0, 6 Δ>0). Recursive ordering yields almost no short rules and some
length-increasing ones — structurally unlike shortlex. Diagnostic only.

## 6. Soundness

- **KB-soundness (airtight):** kbprog derives only consequences of the exp-5 relators, so every rule is a
  valid B0(2,5) identity BY CONSTRUCTION — a theorem about KB, not a conjecture.
- **GAP spot-check (receipt):** built B0(2,5) via `EpimorphismPGroup(G,5,12)` (order **5³⁴** confirmed);
  6 sample rules spanning LHS lengths {3,7,8,10,11,12} all verify EQ_OK. Script `bank/spot_check.g`.
- **Validator** independently re-verifies the full delivered bank against its registered B0-object /
  finite-pc-group checklist (Lead-confirmed). Nothing looked off; no rule routed as suspect.

## Open decision for Maria (via Lead)
368 distinct-firing < 500 GO floor. Options: (a) proceed with the 378-rule sub-floor bank for v1a
(measure improvement-over-31-rule-seed-bank), or (b) adjust generation strategy. Locked caps (LHS≤12,
no excluded orderings) NOT relaxed — the limited supply is a genuine finding.
