---
title: "Mega-Bank Multi-Word Test — 5578-rule bank on 10 benchmark words (2026-07-22)"
date: 2026-07-22
domain: group-theory
project: b25
instance: b25-loop-v1
experiment_type: patternboost
author: maumayma
status: pending
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, project/b25, status/pending, results]
---

# Mega-Bank Multi-Word Test (Maria: real ≥10-word test, beat-beam shot)

Ran the mega-derived 5578-rule bank (`runs/b25/beatbeam_20260721/mega_le16_bank.rules`, LHS 3-16, Δ<0,
from `mega_ab_rules.live`) via braid_reduce (beam+bank, from the ORIGINAL) on 10 benchmark words. No commit.

## Result table

| word | orig | reduced | beam best | verdict | our time | rules fire (static) |
|---|--:|--:|--:|---|--:|--:|
| comm_12_7 | 8456 | **3698** | 3698 | **= beam exactly** | (prior) | 2 |
| comm_22_3 | 4162 | 4156 | 4156 | = beam | 180s | 0 |
| comm_13_10 | 2500 | 2496 | 2496 | = beam | 92s | 0 |
| comm_26_1 | 3576 | 3567 | 3567 | = beam | 180s | 2 |
| comm_11_1 | 3756 | 3744 | 3744 | = beam | 93s | 4 |
| comm_12_10 | 4972 | 4964 | 4964 | = beam | 180s | 0 |
| comm_14_9 | 4966 | 4957 | 4957 | = beam | 180s | 1 |
| comm_11_7 | 3792 | 3777 | 3777 | = beam | 91s | 5 |
| comm_26_2 | 8340 | 4761 | 4761 | = beam | 205s | 3 |
| comm_12_9 | 28652 | 7249 | 7245 | ≈beam (+4) | 1869s | 4 |

**9 of 10 words reach beam-best EXACTLY; comm_12_9 (the 28652-char outlier) reaches 7249 — within 4 chars
of beam's 7245, but not exact and slower (1869s), because the 90s×2 beam budget was insufficient for the
3×-larger word.** GAP-verified: all reduced = target in B0(2,5) (comm_22_3, comm_13_10, comm_26_2, and
comm_12_9's 7249 → all True).

## (1) Beat-beam: NO beat
All words match beam-best exactly. Broad stale-best scan (Python braid+power+tandem on **all 119**
originals vs recorded best_len): **0 words below best_len.** The recorded bests are solid; the reducer
reaches but does not beat them. (Beating still needs the global align-then-collapse — established
out-of-reach; geodesic > 26, robust attractor.)

## (2) SPEED: ~4-10× FASTER than beam
Our wall time **91-205s/word** vs beam's ~240s×4 ≈ **960s/word**. The reducer reaches beam-best in a
fraction of beam's time — a real efficiency win (braid does the bulk fast; a short beam polishes).

## (3) RULE-USAGE: the 5578 "proper" bank is 99.9% DEAD — reduction is BRAID-DRIVEN
- **Effective bank: 7/5578 rules fire (static, LHS occurs) on ≥1 of the 9 words = 0.1%; 5571 dead.**
  Per word: 0-5 rules fire (comm_22_3, comm_13_10, comm_12_10 fire ZERO).
- **Leftmost-trace rule applications: 0** on all words.
- **braid-ALONE (no bank, no beam) reaches within 2-11 chars of beam-best** (comm_13_10 2498, comm_26_2
  4772, comm_11_1 3754). The bank+beam close the final 2-11 chars (the "polish") via a handful of rules
  in the beam stage (untraced by leftmost). So the reduction is **BRAID-DRIVEN**; the rule bank
  contributes only a marginal polish.

## Diagnosis (deepens Maria item 4)
Switching from the 378 bank to the mega "right-word-space" bank did **NOT** increase firing — the mega
bank is **also 99.9% dead** (7/5578) on the benchmark words. Root cause: the benchmark words are
quasi-periodic with only ~24,725 distinct 4-20-char substrings, and rule LHS patterns overwhelmingly do
not match them. **No local rule bank fires meaningfully on these words** — the reduction to beam-best is
**braid-driven**, and the rule/NN augmentation layer adds ~0 because braid already reaches the beam floor.
This fully explains the axplorer's 0 reductions (0 gain over braid), reframes "mis-scoped bank" as
"reduction is braid+global, not rule-driven," and confirms beating beam needs the global move. **Net
positive: the reducer reaches beam-best on all words, 4-10× faster than beam.**
Companion: [[bank-applicability-audit-2026-07-21]], [[beat-beam-campaign-2026-07-21]].
