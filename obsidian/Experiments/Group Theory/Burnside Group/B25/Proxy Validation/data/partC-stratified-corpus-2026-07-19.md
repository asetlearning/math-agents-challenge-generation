---
title: "Part C r-re-validation — Stratified Corpus (built + GAP-labeled, 2026-07-19)"
date: 2026-07-19
domain: group-theory
project: b25
instance: b25-loop-v1
experiment_type: proxy-validation
author: maumayma
status: pending
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/proxy-validation, project/b25, status/pending, data]
---

# Part C r-re-validation — Stratified Corpus (PREP; proxy sweep HELD)

Bank-independent, reusable corpus for the rules-injected r-re-validation of the reducer proxy on the
378-rule bank + absolute-residual objective. **Built now per Lead; the proxy-vs-reference correlation
pass (braid_reduce `--no-beam --rules-file <378-bank>` sweep) is HELD until Maria's floor GO** — if she
opts to adjust generation the bank changes and only the proxy pass, not this corpus, would need redoing.
Dir: `runs/b25/proxy_partC_20260719/`. Generator `build_corpus.py`, labeler `label_corpus.g`. No commit.

## Composition (n=150, ≥30% hard ✓)

| stratum | n | construction | GAP =e in B0(2,5) |
|---|--:|---|---|
| **hard** ([G,G]/(aba)⁵-type, blind) | **60 (40%)** | 5 DIVERSE grammars, 12 each | **all 60 = e ✓** |
| easy / generic | 45 | 23 random walks + 22 seed mutations | all 45 ≠ e |
| real held-out | 45 | sampled from 12k held-out pool (20260701) | all 45 ≠ e |

**119 benchmark words excluded** from all strata (verified). Lengths 16–1018, mean 231.

### Hard-stratum diversity (not one id-aug grammar)
- **A** `c·u⁵·c⁻¹` conjugated-relator products (varied period-≥3 `u`, varied conjugator) — 12, all =e.
- **B** direct multi-letter 5th powers `w⁵` (1–3 concatenated) — 12, all =e.
- **C** commutator 5th powers `([x,y])⁵` and products (blind [G,G] structure) — 12, all =e.
- **D** random normal-closure (k random `u⁵` inserted at random positions w/ random conjugation) — 12, all =e.
- **E** mixed concatenations of A/B/C pieces — 12, all =e.

Each grammar independently GAP-verified: all 12 words `=e`. Confirms the hard stratum is genuine
identity-class blind material from **structurally diverse** sources, so a proxy validated here is not
overfit to one construction.

## GAP labeling (finite-pc-group eval)

`EpimorphismPGroup(G,5,12)` → B0(2,5), **order 5³⁴ confirmed**; `IsOne(Image(phi, word))` per word (25 s
for all 150). Labels merged into `corpus_labeled.json` (`is_identity_B0` per word). Method matches
Validator's registered B0-object checklist.

## Forward flag for the proxy-pass design (Validator/Lead)
The `=e` boolean is **stratum-aligned** (hard=True, easy+held-out=False), so a proxy-vs-`=e` correlation
would be confounded with stratum. If the registered protocol needs a **graded within-stratum reference**
(true geodesic / coset distance to identity in B0, e.g. on the hard =e words where the reducer is flat),
that is an **additional GAP step** (distance computation) to add before the sweep — flagging now so it
can be decided at proxy-pass GO. The `=e` labels are delivered as specified either way.

## Status
- Corpus + `=e` labels: **DONE** (this note).
- Proxy-vs-reference correlation pass (braid_reduce sweep on 378-bank): **HELD for Maria floor GO.**
- Related: [[r2-rulegen-bank-2026-07-19]] (the bank), [[axplorer-representation-grounding-2026-07-17]]
  §P4 (the blind-class blindness this validates against).
