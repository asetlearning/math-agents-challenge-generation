---
title: "Cyclic-Seam Sweep — seam-reduction discovery rate across 119 words (2026-07-22)"
date: 2026-07-22
domain: group-theory
project: b25
instance: b25-beat-beam
experiment_type: cascade
author: maumayma
status: pending
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/beat-beam, project/b25, status/pending, results]
---

# Cyclic-Seam Sweep — discovery rate at scale

Full cyclic sweep (Lead GO, Validator-PROVEN mechanism): per word, rotate the beam-best form through
bounded offsets, RUST braid_reduce each (--no-beam --rules-file mega_le16), keep the min. Measures the
**seam-reduction DISCOVERY RATE** across all 119 benchmark words — the ceiling of the cheap CLASSICAL fix
and the metric that decides whether a v2 net is needed. GAP-gated. No commit.
`runs/b25/beatbeam_20260721/{cyclic_sweep.py, cyclic_sweep_beats.json, seam_decomp.json}`.

## Headline — TWO distinct findings, cleanly separated

| finding | words | chars | mechanism | GAP |
|---|--:|--:|---|---|
| **GENUINE SEAM reduction** | **77/119 (65%)** | **283** | rotate @period-72 + re-reduce beats the no-rotation fixpoint | all = target ✓ |
| stale-best (separate axis) | 37/119 | ~540 | no-rotation reducer beats the STALE stored best_word | all = target ✓ |

**Framing (Validator's, adopted):** this is **verified existence of sub-beam seam-reductions at scale**,
NOT "the method beats beam." The seam number is the load-bearing result.

## Genuine cyclic-seam reductions: 77 words, 283 chars

- **77/119 words (65%)** have a reduction that rotation@72 exposes **beyond** the no-rotation reducer
  fixpoint (pure seam = L₀ − L₇₂ > 0 for all 77). Total **283 chars**. Per-word Δ **1–12**.
- **Uniform winning rotation = 72 = the period.** The quasi-periodic words break periodicity at the
  wrap-around; rotating by exactly one period brings that seam defect into a linearly-reducible position
  the greedy beam (which scans linearly, blind to the cyclic wrap) cannot reach.
- **All GAP-verified** = target in B0(2,5) (is_identity + equal(result, original)). Element-preserving
  (rotation of a =e word = conjugate = e). Witnessed path = single rotation @72 + re-reduce.
- Includes the two **Validator-PROVEN** beats: comm_13_10 (Δ2), comm_11_7 (Δ3).
- Examples: comm_19_3 11275→11263 (seam Δ12), comm_23_2 11830→11818 (Δ12), comm_10_9 9644→9634 (Δ10).

## Stale-best (distinct, housekeeping): 37 words, ~540 chars
The no-rotation RUST reducer (braid+bank) beats the **stored** benchmark-0001 best_word on 37 words
(~540 chars) — the stored bests are stale (predate this reducer). **Matches the earlier diagnostic's
37/540 exactly.** This is NOT the seam mechanism; it just means the benchmark best_words should be
refreshed. (15 words are pure stale @rot0; 22 of the 77 seam words also carry a stale component.)

## Decision implication (the point of the measurement)
- **Ceiling of the cheap classical fix = 283 chars over 77 words (Δ1–12 each).** Small and shallow — a
  single period-rotation captures it. A **cyclic-aware reducer** (reduce, then test period-rotation, keep
  min) captures ALL of it cheaply and completely; no NN needed to learn "try a rotation @period."
- **The seam residual is SHALLOW** — no deep multi-step cascade appeared (max seam Δ = 12; the deep
  relator-insertion cascades never won). So after cyclic-awareness, the remaining headroom on these words
  is ~0 by classical means, and beating beam *meaningfully* still needs the global align-then-collapse
  (established out-of-reach: X-core geodesic > 26, robust attractor).
- **v2-net recommendation (mine, matching Lead/Validator):** a policy net trained to "try a rotation"
  is wasteful — adopt the cyclic-aware reducer instead. Build the net ONLY if a target beyond the seam +
  cheap-reformulation set is identified; the seam sweep shows that residual is currently empty/shallow on
  the benchmark family. **Gate the net on a real deep-residual target, not on these Δ1–12 seam wins.**

## Iterated cyclic-aware reduce — does it COMPOUND? (Validator-flagged, decisive)
Loop { reduce→fixpoint; try period-multiple rotations 72,144,… (+ non-period controls 36,100,150,250);
keep any shorter; repeat } on the 77 seam words. RUST reducer, GAP-gated.

| metric | value |
|---|--:|
| single-rotation total Δ | 283 |
| **ITERATED total Δ** | **351** (+68, +24%) |
| words that COMPOUND (>1 rotation) | **8/77** |
| rotation hits: period-aligned / control | **101 / 0** |
| all GAP = target | ✓ |

**VERDICT: PLATEAUS (shallow).** 69/77 words are fully captured by a SINGLE period-72 rotation; only
**8/77** compound — and they compound via **repeated @72 rotations** (e.g. comm_16_2: 10×@72 → Δ21;
comm_14_3: 5×@72 → Δ16), each exposing the seam defect at the *next* period boundary. **Only period-72
rotations EVER help (0 control hits)** — the mechanism is purely period-seam alignment, mechanical and
deterministic, with NO random/deep structure.

**Decision (confirms shelve-the-net):** the classical cyclic-aware reducer = `loop { reduce; rotate@72;
keep min } until plateau` captures the FULL ceiling (351 chars over 77 words). It is a deterministic
classical loop, not a learnable deep target — a net would only relearn "keep rotating by the period."
The cyclic lever is SHALLOW; meaningful beat-beam still requires the out-of-reach global move. → adopt the
classical cyclic-aware reducer (351-char ceiling), refresh the 37 stale bests, no v2 net.

Confirmed seam-beats (single + iterated) batched to Validator for #status. Companion: [[cascade-prototype-prereg-2026-07-22]].
