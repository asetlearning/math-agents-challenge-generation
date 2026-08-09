---
title: Dynamic Rule Generation on B(2,5)
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: dynamic-rulegen
status: pending
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/rule-generation, topic/knuth-bendix, topic/proof-search, project/b25, status/pending, experiment-type]
---

# Dynamic Rule Generation — B(2,5)

## What this experiment type is

A rule-**source** program, not another reducer. Static overlap-scored rule banks are **saturated at 17
firing rules at ANY bank size** on B(2,5) identity-certificate words — more length-decreasing rules of the
same kind are inert. This experiment type generates *new certified spellings* (`L = R` equalities in
B₀(2,5)) whose substrings overlap the reducer's **active** structure in the **rotated / conjugated /
fixed-point states** the original word never exposes — i.e. **dynamic** overlap, scored against the states
the seam actually visits, not the raw benchmark strings.

Two rule classes the monotone reducer cannot reach on its own are admitted here, in **bounded sequence
search only** (never in the monotone reducer):
- **Same-length (Δ=0) phase-shifters:** `W_fixed → W_same → W_shorter` — an alignment a descent-only reducer
  can't step to.
- **Small length-increasing (Δ>0) enablers:** `W_fixed → W_larger → W_much_shorter` — the "expand first"
  barrier crossing.

Every generated `L = R` is **GAP-admitted in B₀(2,5) by Validator BEFORE use** (finite-pc oracle +
alphabet gate); the pipeline never trusts its own PASS.

**Scope guard:** these are =e identity-certificate words (HWW pcps commutator relators, trivial in B₀ by
construction). "Reduction" = shortening an identity-proof. NOT a free-B(2,5) claim (Kourovka 11.48 OPEN).

## Parameter variants live in `results/results.md`

One folder, one results table; each generation/scoring configuration is one row.

## Related material

- [[dynamic-overlap-rulegen-2026-07-28]] — first pre-registration (H3, load-bearing)
- [[2026-07-28-b25-attack-design-arms-and-rulegen]] — Lead attack design this implements
- [[project_b25_beatbeam_cyclic_seam]] — the seam mechanism this generates rules for
- [[PatternBoost/_type]] — sibling experiment type (transformer-guided rule proposal)
