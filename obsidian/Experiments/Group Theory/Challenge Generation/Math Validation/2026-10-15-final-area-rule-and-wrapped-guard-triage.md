---
title: "Final area-like rule and wrapped-relator guard — triage"
status: conjectured
domain: group-theory
project: challenge-gen
claim: "Owner rule 2026-10-15: area-like iff N>=16, T_deep>=0.5, T_depth>=0.5 and (dual-connected deep core >=2 or maxdepth>=2); wrapped-relator guard; no chain word has a connected deep core of size 2"
claimant: Math Expert (accepted by owner)
verification_method: "combinatorial proof sketches; synthetic planar-map classifier; re-run of own depth peeling on T-023 certificates"
tools_used: ["python3 (scratch/rule_*.py)"]
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, topic/van-kampen, project/challenge-gen, status/conjectured, proof]
---

# Triage — final area-like rule, wrapped-relator guard, size-2 core conjecture
Request from Lead 2026-10-15. Source: [[challenge-gen-success-metrics]] § Owner decision 2026-10-15, [[2026-10-14-depth-followups]], [[t018-t021-diagram-search-2026-10-14]] rev. 4. Earlier work: [[2026-10-14-t023-folded-diagram-review]]. Parallel review, not a T-018 gate; deadline is before any T-018 claim.

## Scope check
Verification of definitions and a stated conjecture, not an experiment. No new constructions are searched for. Synthetic planar maps are used only as test inputs for the rule.

## Sub-claims
1. **Rule gameability.** Which diagrams satisfy the rule as written, and does the dual-connected-core clause do what it is meant to?
2. **Guard soundness.** Does "N_deep = 1 and every other cell touches ∂Δ and the deep cell" imply that w is conjugate to the deep relator? In which group? What does it miss?
3. **Conjecture.** No chain-derived word, compressed or not, has a connected deep core of size 2.
4. **Premise/model.** Everything here is about the shape of one certificate (an upper bound on area). None of it is a statement about the free group B(2,5) or its Dehn function.

## Tools (probed)
- python3 3.12.3 (used in the earlier T-023 review).
- Own depth-peeling code `scratch/t023_depth.py` and compression `scratch/t023_compress.py`, independent of PR #13.
- GAP is not needed: nothing here is a group-equality claim.

## Methods inventory
| Sub-claim | Method | Proves |
|---|---|---|
| 1 | hand classification of grid, ladder, onion and wrapped-pair families by a standalone implementation of the rule | counterexamples to "area-like means quadratic area" (sufficient to refute); not a proof of safety |
| 2 | topological argument (annulus cut) plus check on the T-023 compressed certificates with N_deep = 1 | soundness in the right group; completeness is only a negative statement |
| 3 | Euler identity b1 = V_int − s from the T-023 review, plus counts on existing certificates | proof for tree-like dual graphs; empirical for compressed ones |

## Hard limits
- Whether a given abstract planar map is realisable with the dataset and v⁵ relators is not decided here. Realisability is an experiment.
- Only existing T-023 outputs are used.

## Recommendation
Full verification path for 1–3, with the limits above. Verdict note: [[2026-10-15-final-area-rule-and-wrapped-guard]].
