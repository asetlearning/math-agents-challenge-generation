---
title: Dynamic Rule Generation — data
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: dynamic-rulegen
status: pending
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/rule-generation, project/b25, status/pending, data]
---

# Dynamic Rule Generation — data

Inputs consumed by the pipeline (repo is source of truth; vault links only).

## Dynamic-state corpus sources

| Source | Repo path | Contents |
|---|---|---|
| Current bests | `experiments/b25_reduce_core/runs/b25-reduce-core-benchmark-0001/data/best_words/*.txt` | 119 recorded best words |
| Period-72 seam traces | `runs/b25/patternboost_loop_v1/maxpower_v2_20260724/cert_comm_*.json` (`seam_rotations`) | 92 rotated-intermediate trajectories |
| le80-no-rotation fixpoints | regenerated via `braid_reduce --no-beam` on `extract_le80.rules` | greedy fixpoints |

## Rule banks

| Bank | Repo path | Size |
|---|---|---|
| le80 (incumbent) | `runs/b25/beatbeam_20260721/maxpower_coverage_20260724/extract_le80.rules` | 9,394,214 rules (851 MB) |
| mega_le16 | `runs/b25/beatbeam_20260721/mega_le16_bank.rules` | 5,578 rules |

## R2 Δ=0 candidate population (~330)

- `runs/b25/patternboost_R2_rulegen/admission_tooling/cand_rules.tsv`
- `runs/b25/patternboost_R2_rulegen/extraction_20260701/{cand_rules.tsv, admit_results.tsv, fire_annotation.tsv}`

## Generation pipeline (script)

- `experiments/burnside/b25/dynamic_rulegen/` (to be created; git SHA recorded per candidate file for Validator).

## Related material

- [[_type]] — experiment-type root
- [[dynamic-overlap-rulegen-2026-07-28]] — methodology / pre-registration
- [[results]] — outcomes table
