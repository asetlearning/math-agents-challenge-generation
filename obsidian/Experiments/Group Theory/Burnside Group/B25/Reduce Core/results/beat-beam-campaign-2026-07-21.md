---
title: "Beat-Beam Campaign — comm_12_9 vs 7245 (honest negative + characterization, 2026-07-21)"
date: 2026-07-21
domain: group-theory
project: b25
instance: comm_12_9
experiment_type: reduce-core
author: maumayma
status: pending
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, project/b25, status/inconclusive, results]
---

# Beat-Beam Campaign — comm_12_9 (target: below beam-best 7245)

**STATUS: CONCLUDED (Lead stand-down 2026-07-21).** 6-hour autonomous campaign (Lead-directed).
**Result: no sub-7245 reduction found by any feasible method** — a definitive, exhaustive negative with a
mathematical lower bound (X-core geodesic > 26) and pre-registered kill criteria met across every method.
`runs/b25/beatbeam_20260721/`. No commit (Lead/Maria gate).

Companion deliverables: [[comm129-headroom-probe-2026-07-21]] (window-granularity probe), B0 oracle
handoff `runs/b25/gap_oracle/` (Developer-confirmed, powers v1b accept-gate). The working axplorer + the
consolidated 6h deliverable live in Lead's scope.

## Every method stalls at 7245 (robustness verified many ways)

| lever | method | result |
|---|---|---|
| ordering/bias | wtlex 318k biased bank + beam on 7245 | Δ=0 (no reduction) |
| ordering/bias | fresh-path: 10624 after_power + wtlex bank + beam | crawled to 10560 (bank ≪ 7M beam) |
| lifted/compressed | comm_13_10 lifted bank (1.95M m/M rules) on 563-form | 563→544 lifted, m-count 96 fixed → real **7264** |
| macro m⁵=e | m/M free+power reduction (mM=e, m⁵=e, Aa/bB) | 563→563, 3325→3325 (no change) |
| macro collapse | GAP-scan 322 lifted substrings (≥2 macro) for =e | **0 collapsible** |
| lifted KB | augmented bank LHS≤34 + explicit m⁵/M⁵/mM relators + beam | m-count stuck 96 |
| tandem | U^k scan (raw + lifted), k≥5 | none (max k=2) |
| ALNS (Python) | 200 diverse-restart kicks, destroy +20..60, randomized re-reduce, SA | **zero sub-7245** |
| ALNS (beam) | 16 large perturbations (+20..60) + braid_reduce beam+318k-bank | **all 16 → exactly 7245** |

Every reduction system — raw bank+beam, lifted bank, m/M free+power, macro collapse — leaves 7245 (or
its 563-char lifted equivalent) unchanged. All GAP-verified = comm_12_9.

## The X-core is a DEEP element (the key structural result)

The beat-beam leverage was: X-core (35 chars) recurs 88× disjoint in comm_12_9 + shared across 5 words,
so a shorter X′ (Δ chars) → beat comm_12_9 by 88·Δ and all 5 words. **Does a shorter X′=X exist?**

- **GAP BFS from identity in B0(2,5):** X-core NOT found within radius 14 (ball 1.55M) → geodesic > 14.
- **Meet-in-the-middle (2×13):** scanned 940,941 ball elements for M = u·v with |u|,|v|≤13 → **none.
  X-core geodesic > 26** (definitive lower bound).
- Reducer stuck at 35. So X-core geodesic ∈ (26, 35] — a **deep element with no short form**. Forms of
  length 27–34 are unreachable by BFS and reducer-stuck; even if one existed the max win is Δ≤8 and it is
  unfindable by any feasible method. **The "substitute a shorter X" path is effectively closed.**

## Why 7245 is robust (characterization)

The macro relations that COULD cut comm_12_9 exist and are GAP-verified: **m⁵ = X⁻¹b⁵X = e**, **mM = e**
(M = m⁻¹). But in the lifted form the 96 macros are **tissue-separated** (m→M tissue = single `a`/`A`;
projection is a clean `(mM)⁴⁸` but never adjacent), so mM=e / m⁵=e **cannot fire without global
alignment** — commuting m past the a/b tissue to bring macros adjacent. That alignment is a genuine
**global align-then-collapse** move that no local reducer, bounded-LHS rule bank (≤34), or free+power
reduction performs. This matches Developer's pilot finding independently: comm-word reductions are
**holistic / window-undecomposable** (0% at every window ≤4096).

## ALNS (the proven nearest-domain method, Shehper 2024) — also exhausted
Full-word diverse-restart ALNS was the one untried proven method. Both variants tried: (a) Python, 200
diverse-restart kicks with large perturbation (+20..60, past the §7 cap) and randomized re-reduction +
SA acceptance → zero sub-7245; (b) beam, 16 large perturbations re-reduced by braid_reduce beam+318k-bank
→ **all 16 snapped back to exactly 7245**. 7245 is an **extremely robust attractor**: every perturbation,
diverse or beam re-reduced, returns to 7245. Kill criterion (200 kicks / K≤60 / zero sub-7245) MET.

## Honest bottom line
**7245 is robust to every feasible move in the 6h budget** (raw, ordering, lifted, macro, m/M free+power,
BFS-to-26, and diverse-restart ALNS). No shorter X-core (proven geodesic >26), no sub-7245 reduction. Beating a 7M-rule beam here
requires a genuinely hard **global alignment-then-collapse** beyond bounded search / this budget — not a
cheap ordering/bank/macro trick. The deliverable is the **working axplorer + this precise characterization
of where the win must come from** (global cross-copy/macro alignment), not a beat-beam number this session.
