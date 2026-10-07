---
title: "PatternBoost Generation — data"
domain: group-theory
project: challenge-gen
instance: B(2,5)
experiment_type: patternboost-generation
status: pending
author: asetlearning
tags: [agent/human, user/asetlearning, domain/group-theory, topic/b25, topic/patternboost, topic/trivial-words, project/challenge-gen, status/pending, data]
---

# PatternBoost Generation — data

**None of the data below is in git.** These are paths relative to the b25 repo root on the owner's machine. Recording sha256 hashes is a provenance TODO.

| Data | Path / source | Notes |
|---|---|---|
| Baseline targets: random certified trivial words | `data/pattern_boost_experiments/relator_sets/relators_sample_n1000_20260519_131825.json` (+ `.factorwords.json`, `.config.json`) | 1000 words from `experiment_local_search sample` (see [[patternboost-generation-constants]]). Same generator family as the initial pool, so solvable by construction |
| Baseline sweep output | `data/pattern_boost_experiments/pb_sweep/sweep_20260522_013909/` | `sweep_summary.json`, per-trial `run.jsonl` and `run.matches.jsonl`. Dashboard export: `/media/psf/writeups/pattern boost baseline experiment.html` |
| Baseline sweep config | `configs/pattern_boost_sweep_1.yaml` | **Missing from the repo.** Needed to fix the scorer and seed values |
| Real challenge words (later phases) | 150 HWW-derived words. In the vault repo: `data/b25_challenge_original_freelyreduced.json` (sha256 `0679778…cf3cde`; 32 are empty) | Trivial in B₀(2,5) ([[2026-09-30-b25-b0-challenge-triviality]]); open in free B(2,5) |
| 2.5-reduced challenges / relator sets | `data/pattern_boost_experiments/relator_sets/relators_shortlex_rules_2.5reduced*.json` | Used by `pattern_boost_2_5_reduced.yaml` and `pattern_boost_reduced_gens.yaml`. Used as relators these are **trusted, not verified**. `relators_shortlex_rules_2.5reduced.json` (68 relators, 132 with inverses) was the relator set of the Dehn-proxy run; its provenance (which KB run, which 2.5-reduction) should be recorded |
| Dehn-proxy run log (2026-07-23) | vault repo `shared/run_20260723_233147_complete_dehn_function_use_reduced_relations/` (`run.jsonl`, `tokenizer/`) | Full config on line 1. 2.5-reduced length per iteration in `pb_candidate_2.5_reduced_length_stats`; score = Dehn proxy. Original path `output/pattern_boost_reduced_gens/run_20260723_233147` |
| BPE tokenizers | `models/tokenizer/compression_bpe_sample_n1000_20260519_131825*.json`, plus the tokenizers trained on challenges (`bpe_tokenizer_challenge_*_20260317/18`) | The token statistics are in `/media/psf/writeups/B25 experiments RESULTS.md`: 1761 tokens (average length 2542) on the 2.5-reduced challenges; 1566 (average length 3723) on the originals |

Logs: per-trial `run.jsonl` (structured JSON) under the sweep directory. The code does not record SHAs or seeds beyond the config.

Registered datasets for this project are listed in [[project-challenge-gen]] § Problem instances. The first is [[ds-b25-trivial-2-5reduced-aut8-20261007]] (820 vetted candidate trivial words, no certificates). It is a candidate target set for later phases.

## Related material
- [[patternboost-generation-methodology]] · [[patternboost-generation-constants]] · [[patternboost-generation-results]]
- [[dep-b25-pyproject-agentic]]
- [[project-challenge-gen]]
