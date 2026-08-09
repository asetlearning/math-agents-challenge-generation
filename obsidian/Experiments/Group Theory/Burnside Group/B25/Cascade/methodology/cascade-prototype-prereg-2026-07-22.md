---
title: "Overlap-Scored Cascade Expand-Then-Collapse — Prototype Pre-Registration (2026-07-22)"
date: 2026-07-22
domain: group-theory
project: b25
instance: b25-beat-beam
experiment_type: cascade
author: maumayma
status: pending
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/beat-beam, project/b25, status/pending, experiment]
---

# Cascade Expand-Then-Collapse Prototype — Pre-Registration

**GO/NO-GO for the v2 learned rewrite-path policy net** (Lead-routed, Maria-green-lit). Classical
(no NN) overlap-scored targeted expand-then-collapse. Pre-registered BEFORE any run. No commit.

## Hypothesis (falsifiable) — REFRAMED per Experimenter diagnostic addendum (2026-07-22)
Overlap-scored **MULTI-STEP CASCADING** expand-then-collapse — expansions whose RHS **RE-EXPOSES FURTHER
reducible sites** (chains ≥2 reductions), OR length-neutral conjugation/cyclic reformulation exposing
**multiple** motifs at once — produces **≥1 sub-beam GAP-verified word**, where BOTH **RANDOM ALNS**
(216 attempts: 200 kicks + 16 perturbations, all snapped back) AND **SINGLE-motif injection**
(settled-insufficient: comm_26_1/comm_11_1/comm_14_9 already contain firing motifs; beam fired them, saved
only 9–12 chars, NO cascade; effective bank = 17 non-composing Δ-1 nibbles) already yielded **ZERO**.

**Do NOT re-prove single-motif injection fails — settled.** The untested lever is expansions SELECTED (by
overlap-score) FOR their **downstream re-exposure** — a chained 2+-step cascade — and element-preserving
by construction (a local motif-creation changes the local element, so it MUST be a global =e move that
reshapes, balanced by the rest of the word). Entry points: the Hamming-1 near-miss sites the diagnostic
found (e.g. comm_22_3 pos 887 `babABABBAB`) — but CHASE the cascade after firing, not the single +1 nibble.

## Kill criteria (pre-registered NULL)
**≥50 overlap-scored cascade attempts per word, across ≥4 words, yielding 0 sub-beam GAP-verified words
= NULL** = the cascade does not beat beam on B(2,5) = **recommend AGAINST building the v2 net**.
A NULL is high-value: it confirms the robust-attractor wall is fundamental to expand-then-collapse.

## Mechanism (B(2,5)-adapted overlap-scoring, ported from B(4,3) v10d idea)
- **Reducer** = braid_reduce logic (braid + power + tandem). Established: rule-applications ≈0, reduction
  is **BRAID/POWER-driven**. So the sites that chain are **braid/power sites** (partial 5th powers,
  alternating runs, power runs), NOT bank-rule LHS.
- **Reducible-site score** of a word = count/size of braid-eligible alternating runs (len≥6 after a move),
  power runs reducible (g^k, k giving shorter via 5th-power/inverse), partial 5th powers extendable.
- **Expansion moves — element-preserving BY CONSTRUCTION (=e in B0(2,5)):**
  1. **conjugated relator insertion** `c·u⁵·c⁻¹` (=e) at a chosen position;
  2. **cyclic reformulation** `w1·w2 → w2·w1` (=e for identity words; conjugate);
  3. **conjugation** `w → c·w·c⁻¹` (=e for identity words).
- **Overlap-scoring**: score each candidate expansion by the **NET new braid/power-reducible content its
  RHS creates** (Δ reducible-site score), i.e. how much it CHAINS into further reduction after re-reduce.
  Pick top-scored, apply, re-reduce, iterate (cascade). Track global best; keep any net-shorter form.

## Targets (STEP 2, cheap→hard)
comm_22_3 (4156), comm_13_10 (2496) — weak words that contain firing motifs but did NOT cascade; + 2 more
weak words (comm_12_10 4964, comm_11_7 3777); then **comm_12_9 (7245)** — the robust attractor (hardest).

## Gate (STEP 3)
Any sub-beam candidate MUST (a) pass the sanity gate: element-preservation via **GAP-in-B0** (o.equal to
target) AND floor AND a valid witnessed reduction path (element-preserving by construction); AND (b)
GAP-verify = target. A sub-beam GAP-verified word is a genuine **BEAT** — flagged LOUD immediately.

## Baselines
- RANDOM ALNS (prior): 0 sub-beam over 200+16 kicks (the negative this targets to beat).
- Plain reducer: reaches beam-best exactly, 0 beats (established).

## Seeds
Deterministic per-word RNG (seed = word-hash + attempt index) for reproducibility; ≥50 attempts/word.

## RESULTS (2026-07-22) — VERDICT: POSITIVE (v2 justified), mechanism = cyclic reformulation

| word | beam best | cascade | verdict | mechanism |
|---|--:|--:|---|---|
| comm_22_3 | 4156 | 4156 | = beam | (rotation didn't expose a seam site) |
| **comm_13_10** | 2496 | **2494** | **BEAT Δ2** | cyclic rotation @2053 + re-reduce |
| comm_12_10 | 4964 | 4964 | = beam | — |
| **comm_11_7** | 3777 | **3774** | **BEAT Δ3** | cyclic rotation @1774 + re-reduce |
| comm_12_9 | 7245 | 28569 | no test | Python reducer too weak on the 28652-char word (Rust reaches 7249) |

**Two GENUINE sub-beam GAP-verified beats.** Not stale-best: the standard reducer reaches beam-best
EXACTLY (2496, 3777); the beat REQUIRED the element-preserving move. Witnessed paths exported
(`cascade_BEAT_{comm_13_10,comm_11_7}.trace`): original → reduce→fixpoint(=beam-best) → **cyclic rotation**
→ reduce→fixpoint(=beat). Every path state GAP-verified = target in B0(2,5); start = original word.

**Mechanism finding (changes the v2 calculus):** the winning move is a **CYCLIC REFORMULATION** (rotate
the word, length-neutral, element-preserving = conjugate = e), which exposes a seam-reducible site beam's
LINEAR greedy pass cannot see. It is **classically cheap** (no NN needed). So this argues for a
**cyclic-aware reducer first** (sweep rotations + re-reduce, all 119 words), then gate the v2 net on the
DEEP relator-insertion cascades that remain out of reach after cyclic + cheap reformulations are exhausted.

**Honest calibration:** beats are small (Δ2, Δ3); the winning move is a SINGLE cyclic reformulation +
cascading re-reduction, NOT the hypothesized deep multi-step relator-insertion chain (those did not win).
But it is genuine, sound, witnessed, and beam-inaccessible — the load-bearing existence result: a targeted
element-preserving reformulation beats beam's linear floor where random ALNS (216) + single-motif = 0.
Kill criteria NOT triggered (≥1 beat found). Pending: Validator's official verdict on the 2 beats; then
(human-directed) the classical cyclic sweep across all 119 words, on Lead's explicit GO.

## Anti-pattern check
- Not tuning on scoring targets: overlap-score uses the reducer's OWN site-structure, not the beam answer.
- Soundness by construction: all moves are =e; every sub-beam candidate GAP-gated before any claim.
- Honest NULL: pre-registered kill criteria; a NULL is reported as the primary decision-grade result.
- No over-claim: the parallel "37 stale-best / motif-injection" note is kept DISTINCT and not merged here.
