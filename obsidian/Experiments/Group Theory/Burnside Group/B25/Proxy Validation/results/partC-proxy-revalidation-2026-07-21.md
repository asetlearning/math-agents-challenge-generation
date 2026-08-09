---
title: "Part C r-re-validation — Proxy Pass Results (378-bank, absolute-residual, 2026-07-21)"
date: 2026-07-21
domain: group-theory
project: b25
instance: b25-loop-v1
experiment_type: proxy-validation
author: maumayma
status: pending
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/proxy-validation, project/b25, status/pending, results]
---

# Part C r-re-validation — Proxy Pass Results

Rules-injected re-validation of the reducer proxy on the **verified 378-rule bank** + absolute-residual
objective, run at Maria's floor GO (passed explicitly through Lead). Corpus + method:
[[partC-stratified-corpus-2026-07-19]]. Bank: [[r2-rulegen-bank-2026-07-19]]. No commit.

## GATE VERDICT: **PASS**

within-stratum Spearman ρ ≥ 0.90 on EASY **and** HELD-OUT (both required):

| stratum | n | Spearman ρ | p | 95% CI | gate |
|---|--:|--:|--:|---|---|
| **easy / generic** | 45 | **0.966** | ~0 | [0.938, 0.981] | **PASS** |
| **held-out (transfer)** | 45 | **0.987** | ~0 | [0.977, 0.993] | **PASS** |
| hard / blind (=e) | 60 | **undefined** | — | — | reported, NOT gated |
| pooled (descriptive only) | 150 | 0.952 | ~0 | [0.935, 0.965] | — |

- **Both non-blind strata clear 0.90 decisively**; the held-out transfer check (0.987) is even stronger
  than easy (0.966) → the cheap `--no-beam` proxy tracks the best-effort reference on unseen material.
- **Pooled ρ (0.952) is DESCRIPTIVE only** — =e is collinear with stratum, so a pooled value is
  Simpson-inflatable (Lead/Validator-flagged); the gate reads within-stratum.

## Definitions

- **X (proxy)** = `braid_reduce --no-beam --rules-file <378-bank> --num-passes 1` residual length (the
  cheap scoring proxy the loop uses).
- **Y (reference)** = `braid_reduce --rules-file <378-bank> --beam-secs 5 --num-passes 3` residual length
  (best-effort). No geodesic/distance GAP step (=e labels + best-effort-reducer reference, per Validator).
- Corpus: 150 words, GAP-labeled (`=e in B0(2,5)` via EpimorphismPGroup, order 5³⁴). Strata: 60 hard
  (all =e, 5 diverse grammars) / 45 easy / 45 held-out. 119 benchmark words excluded.

## Hard-stratum result (reported, not gated) — a notable subfinding

**Y = 0 for all 60 hard words** (best-effort beam+bank reduces every diverse blind-class =e construction
to identity), so Y has **zero variance** → Spearman ρ is **undefined** (not merely low). The cheap proxy
X reaches 0 on only **53%** of hard words (X range 0–105) → the `--no-beam` proxy under-reduces the blind
class where best-effort succeeds. Two reads:
1. **Scope (the gate's purpose):** the proxy is **valid on the non-blind class** (easy+held-out); the
   blind class is deferred to v2, exactly as pre-registered.
2. **Subfinding worth surfacing:** unlike the *greedy* reducer (P4: ~77% flat on this class), the **378-bank
   + beam is NOT blind on these constructions — it fully reduces them to identity.** The blindness is a
   property of the CHEAP proxy (X), not of the best-effort reducer (Y), on this corpus. That strengthens
   the v1a thesis (search/beam + bank escapes the blind class) and is a data point for the v2 value-head
   /rollout-budget question.

## Process discipline

- Ran at explicit Lead trigger (Maria floor GO → Lead → me). num_workers=2, pgrep-coordinated to keep
  COMBINED braid_reduce ≤4 (peaked at 3 with Developer's v1a), yielded to v1a. Explicit-PID-only. 276 s,
  0 failed calls. Files: `runs/b25/proxy_partC_20260719/{proxy_sweep.py,proxy_results.jsonl,compute_rho.py,gate_verdict.json}`.
- Absolute-residual objective (not the disproven ratio); this validates the proxy the v1a scorer uses.

## Bottom line
The `--no-beam` 378-bank proxy is a **valid rank-proxy for best-effort reduction on the non-blind class**
(ρ 0.97 easy / 0.99 held-out, gate PASS). Blind class deferred to v2. Feeds Lead → Maria.
