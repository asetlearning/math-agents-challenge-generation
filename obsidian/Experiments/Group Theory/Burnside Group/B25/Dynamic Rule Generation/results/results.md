---
title: Dynamic Rule Generation — results
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: dynamic-rulegen
status: rejected
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/rule-generation, project/b25, status/rejected, results]
---

# Dynamic Rule Generation — results

One row per generation/scoring configuration. Pre-registered under [[dynamic-overlap-rulegen-2026-07-28]] (H3).

**VERDICT: H3 KILL** (pre-registered kill condition met, 2026-07-30). No admitted rule of any bucket fires
on any dynamic state to produce a gate-passing sub-current reduction on any of the 119 words. **Not a
self-close — routed to Lead/Maria per exhaustive-negative discipline.**

| Run ID | Date | Parameters | Outcome | Validated by | Notes |
|---|---|---|---|---|---|
| gate-leg1-bank37 | 2026-07-30 | 37 Δ<0 seam-window rules → monotone bank; re-reduce all 119 current bests (braid_reduce) | **0 fires** | own gate + braid_reduce | rules were extracted FROM the seam reductions already in the bests |
| gate-leg2-v2 | 2026-07-30 | 94 Δ=0 oriented moves + 5 Δ=+1 enablers; app_cap 2 / exp_cap 8; T2/T3/T4; mega44 bank | **0 fires / 281,809 applications / 0 window-shrinks**; 5/5 enablers T2-rejected | own gate + braid_reduce; detector validity-guarded | H3 KILL |
| slice-c-trace | 2026-07-30 | rule-fire census + critical-pair extraction over 206 seam/base traces | **0 critical pairs** (19/206 states fire rules, 157 apps, 0 overlapping) | braid_reduce --trace-file | seam is braid-move driven, not rule-driven |

## Version history

- **pre-reg (2026-07-28):** H3 registered; 4 sub-slices.
- **generation (2026-07-30):** (a) corpus 92 words/412 states/92 faithful; (b) 37 Δ<0 window rules;
  (c) 0 critical pairs; (d) 254 Δ=0 → 47 score>0. Validator admitted 84 + 14 wtlex Gate-B.
- **H3 hinge (2026-07-30): KILL.** 0 fires across all buckets/words/depths; detector validity-guarded.

## Main findings

1. **H3 KILL.** Δ<0 window (37), Δ<0 wtlex workhorse motifs (7), Δ=0 phase-shifters (94 oriented),
   Δ=+1 enablers (5) — none produces a sub-current reduction on any of the 119 words.
2. **Root cause (mechanistic):** the cyclic-seam gain is **braid-move / free-cancellation driven, not
   rule-fire driven** (trace census: only 9% of states fire rules, 0 overlapping); current bests are
   braid_reduce-fixpoints; the effective 17-rule core is saturated and already in mega_le16
   (`bank_refresh = 0`). Generated rewrite rules can't help a mechanism that doesn't use rewrite rules.
3. **All 5 Δ=+1 enablers revert** (T2): each `R` braid-reduces straight back to ≤ `L` — no-op cycles, the
   v1a trap.

## Open questions / redirect (for Lead/Maria — NOT self-closed)

- The KILL points away from rewrite-rule generation toward **braid-move / rotation-period search** (arm #1)
  and the deep **HWW/tissue** sources (#4/#5, needs Researcher+Validator, stage 3 — not greenlit).

## Related material

- [[_type]] — experiment-type root
- [[dynamic-overlap-rulegen-2026-07-28]] — pre-registration / methodology
- [[data]] — inputs (corpus, banks, R2 population)
