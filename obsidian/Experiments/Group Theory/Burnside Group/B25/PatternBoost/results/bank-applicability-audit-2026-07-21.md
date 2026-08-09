---
title: "Rule-Bank Applicability Audit — 378 bank vs benchmark words (Maria item 4, 2026-07-21)"
date: 2026-07-21
domain: group-theory
project: b25
instance: b25-loop-v1
experiment_type: patternboost
author: maumayma
status: pending
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, project/b25, status/pending, results]
---

# Rule-Bank Applicability Audit — why axplorer gets 0 reductions

Diagnoses (with numbers) why v1a (0/345) and v1b (0 on all words) get 0 reductions. Audits the 378-rule
primary bank (`runs/b25/patternboost_rulegen/20260719_193749/bank/clean_top378.rules`) against all 119
benchmark words (best_words = beam-reduced targets; originals = raw). Offline. No commit.

## (2) LHS-length scope
- **378 rules, LHS len: min 3, median 11, max 12, mean 10.8.** Histogram: `{3:4, 7:16, 8:24, 9:8, 10:60,
  11:96, 12:170}` — concentrated at the **11–12 cap** by design (locked LHS≤12).
- cf. old 31-rule bank: min-LHS **41** chars. So the 378 bank is deliberately SHORT-LHS.

## (1) Firing counts

| set | rules firing on ≥1 word | never-fire (dead weight) | firing/word (median) | positions/word (median) | words with ZERO firing |
|---|--:|--:|--:|--:|--:|
| **best_words** (reduction targets) | **9/378** | **369/378** | **0** | 0 | **82/119** |
| originals (raw) | 17/378 | 361/378 | 4 | 14 | 11/119 |
| **any benchmark word** | **17/378** | **361/378 (95.5%)** | — | — | — |

Per-word sample (best_word len | rules fired/378 | fire positions) — **the flagship targets fire NOTHING:**

| word | best_len | rules fired | positions |
|---|--:|--:|--:|
| comm_12_9 | 7245 | **0**/378 | 0 |
| comm_13_6 | 6191 | **0**/378 | 0 |
| comm_20_4 | 7743 | **0**/378 | 0 |
| comm_13_10 | 2496 | **0**/378 | 0 |
| comm_10_9 | 9644 | **0**/378 | 0 |
| comm_13_7 | 16798 | **0**/378 | 0 |

## (3) DIAGNOSIS — it is (ii) MIS-SCOPED compounded by (iii) GLOBAL-UNREACHABLE; NOT (i) too-small

**Two compounding causes, both numeric:**

**A. Applicability collapse (mis-scoped — (ii)).** **361/378 rules (95.5%) never fire on ANY benchmark
word.** The effective bank is ~17 rules. On the actual reduction targets (best_words) only **9/378** ever
fire and **82/119 words have exactly ZERO rules firing** (median 0/word). The bank was mined from the R2
short-window bias motifs + a held-out random-walk/mutation pool — a **different word-space** than the
comm_i_j benchmark words, so its LHS patterns mostly do not occur in them.

**B. Reachability wall (global — (iii)).** The one place the bank fires more is the **originals** (raw,
17/378, median 4/word) — i.e. the short-LHS rules target **local structure that beam ALREADY removes**.
On the beam-reduced best_words that local structure is gone (firing → ~0), and the **residual reduction
is global-scale**: the 6h campaign proved X-core geodesic **> 26** (BFS + meet-in-the-middle over 941k
elements), every window ≤360 reducer-stuck, and 7245 a robust attractor (200 ALNS kicks + 16 beam kicks
all snap back). **No local bounded-LHS (≤12) bank can reach it** — even the ~9 rules that DO fire net 0
reduction (campaign: 7245→7245 with the bank).

**Why NOT (i) too-small:** the problem is not rule COUNT — 95.5% of the current rules are dead weight, and
adding more short-LHS rules just adds more dead weight (they'd be mined from the same non-benchmark
word-space and still wouldn't occur in the best_words). Scaling the bank does not help.

### Verdict for Maria (item 4)
The 0 reductions are explained by **(ii) mis-scoping — 95.5% dead weight, wrong word-space (9/378 fire on
best_words, 82/119 words zero) — compounded by (iii) the fundamental wall: the residual reduction on the
beam-reduced targets is GLOBAL/full-word-scale and unreachable by ANY local bounded-LHS bank** (geodesic
>26, windows ≤360 stuck, 7245 robust attractor). Not (i): the bank is not too small; it is 95.5%
inapplicable, and a bigger local bank would not change the outcome. **The short-LHS local-rule paradigm is
redundant with beam on local structure and powerless on the global residual** — consistent with the
window-undecomposable finding. Companion: [[beat-beam-campaign-2026-07-21]], [[comm129-headroom-probe-2026-07-21]].
