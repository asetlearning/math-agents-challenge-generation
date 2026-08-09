---
title: "B25 reduction methods — what we have & combined results"
date: 2026-07-23
domain: group-theory
project: b25
instance: b25-beat-beam
experiment_type: synthesis
author: maumayma
status: living
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/beat-beam, project/b25, status/living, synthesis]
---

# B25 reduction methods — what we have & combined results

**Goal:** shorten identity-certificate words in B₀(2,5). Each benchmark word `= e`; "beat beam" = a shorter word still `= e`. Every positive is GAP-verified in B₀ (order 5³⁴) before it counts.

**Bottom line:** deep reductions (e.g. `comm_12_9` 28652→7245) are **global** and out of reach for every local method. The only genuinely new wins are the shallow **cyclic-seam** slivers. Everything else ties beam or is pending.

## Methods (that actually produce reductions)

- **braid_reduce** — deterministic greedy rewriter + rule bank (Rust). The trusted reducer used inside every other method; on its own it's the honest greedy baseline.
- **Beam search** — linear left-to-right beam over rewrite rules. The incumbent: sets the target `best_len` per word. Blind to the cyclic wrap-around seam.
- **Cyclic-seam @72** — rotate a `=e` word by its period (72) so a reducible block straddling the linearization seam moves into the interior, then re-reduce. Classical, deterministic. → [[cyclic-seam-sweep-2026-07-22]] · viz `ui/cyclic_seam.html`
- **axplorer v2 macro-search (grow-then-shrink)** — MDP over words; net-free MCTS/PUCT over element-preserving macro cells incl. length-increasing relator insertion (`c·U⁵·Inv(c)`); run on the 42 plateau words.

## All levers

Every method above decomposes into these element-preserving moves (all keep the word `= e` in B₀). Coarse arms (bottom rows) are compositions of the atomic ones — a bandit can pull them at either granularity. Each arm is GAP-checkable in isolation.

| arm                     | kind          | what it does                                                                 |        length effect |        trusted?         |
| ----------------------- | ------------- | ---------------------------------------------------------------------------- | -------------------: | :---------------------: |
| **free-cancel**         | atomic        | delete adjacent inverse pair `xX`/`Xx` (also `mM`,…)                         |                   −2 |  ✅ free-group identity  |
| **power-5 collapse**    | atomic        | `U⁵ → e` for any generator/short word `U`                                    |             −5·\|U\| |   ✅ defining relation   |
| **rule shortening**     | atomic        | apply one bank rule `L→R` with \|R\|<\|L\| (e.g. `AAA→aa`, `ababaBB→BABAbb`) |       −(\|L\|−\|R\|) | ✅ GAP `L=B0 R` per rule |
| **relator insertion**   | atomic (grow) | insert `c·U⁵·Inv(c)` (length-increasing, sets up a later collapse)           |                   +k |   ✅ inserts identity    |
| **cyclic rotation @72** | atomic        | rotate whole `=e` word by one period → conjugate of `e` = `e`                | 0 (enables later −Δ) | ✅ conjugation-invariant |
| braid_reduce            | composite     | greedy fixpoint of {free-cancel, power-5, rule shortening} over the bank     |                   ≤0 |    ✅ honest baseline    |
| Beam                    | composite     | linear beam over the bank rules; sets `best_len`                             |                   ≤0 |       — incumbent       |
| Cyclic-seam loop        | composite     | `{ braid_reduce; rotate@72; keep min }` until plateau                        |                   ≤0 |        ✅ proven         |
| axplorer v2             | composite     | MCTS/PUCT over {relator insertion (grow) → braid_reduce (shrink)}            |               ≤0 net |   ⏳ ablation-pending    |

**Arm design note:** the atomic shrink arms (free-cancel, power-5, rule shortening) are exactly what `braid_reduce` greedily saturates — a bandit over just those re-derives the greedy baseline. The *interesting* arms are the ones the greedy reducer **can't** reach on its own: **relator insertion** (must go up before coming down) and **cyclic rotation @72** (must leave the linear frame). Reward should be net `−Δlen` after a full re-reduction, gated by the 3-check sanity gate below.

## Combined results

| method | scope | beats beam? | net new reduction | note |
|---|---|:--:|--:|---|
| braid_reduce alone | per word | no | 0 | greedy baseline; blind on compressed segments |
| Beam (incumbent) | 119 words | — | — | sets the target; comm_12_9 → 7245 (robust attractor) |
| **Cyclic-seam @72** | 77 / 119 words | **yes** | **351 chars** | ✅ Validator-proven; shallow (avg 3.7, max 12); a classical `{reduce; rotate@72; keep min}` loop captures all |
| axplorer v2 (grow-then-shrink) | 42 plateau words | 1 candidate | pending | comm_12_3 15036→15019 (−17), pending ablations; elsewhere ties/above beam |

## Why it's hard (the wall)

- Deep reductions are **global** — reducible structure spread across the whole word (macros separated by single chars, needing global alignment). 7245 is a **proven robust attractor**; no local move set reaches under it.
- **X-core geodesic > 26** (GAP BFS radius 14 + meet-in-middle) — proven lower bound; the collapse can't be short-cut locally.
- So local methods either tie beam (re-deriving it via a better rule bank) or find only the marginal cyclic-seam wins. Meaningful beat-beam needs the out-of-reach **global align-then-collapse**.

## Discipline

Every candidate passes a 3-check sanity gate: (1) same group element as target (GAP in B₀, not blind abelianization), (2) non-degeneracy floor (≥100 chars — no empty collapses), (3) reached by a witnessed path of valid moves. Positives independently re-verified by Validator.

---
_Provenance: `runs/b25/patternboost_loop_v1/` (v2 stageB), `runs/b25/beatbeam_20260721/` (cyclic-seam). Related: [[cyclic-seam-sweep-2026-07-22]]._
