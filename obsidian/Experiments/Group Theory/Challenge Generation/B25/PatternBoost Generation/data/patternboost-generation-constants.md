---
title: "PatternBoost Generation — constants"
domain: group-theory
project: challenge-gen
instance: B(2,5)
experiment_type: patternboost-generation
status: pending
author: asetlearning
tags: [agent/human, user/asetlearning, domain/group-theory, topic/b25, topic/patternboost, topic/trivial-words, project/challenge-gen, status/pending, data]
---

# PatternBoost Generation — constants

Values come from `b25:configs/pattern_boost.yaml` (main @ 7d32335b), which is the `base_config` of the sweeps. **Caveat:** the baseline sweep's own config, `configs/pattern_boost_sweep_1.yaml`, is **not in the repo**, so any value it overrode is unknown. In particular, its scorer is unknown; the base default is hybrid = 1.0·edit + 0.5·abelianized_product_length(q = 5).

| Group | Parameter | Value |
|---|---|---|
| Group | Alphabet | {a, A, b, B} = {1, −1, 2, −2}, exponent 5 |
| Relators | `max_relator_len` | 5 (standard v⁵, \|v\| ≤ 5) |
| Relators | `num_generators` | 2 |
| Model | GPT-2 | `n_layer` 6, `n_head` 8, `n_embd` 256, `n_positions` 512 |
| Training | | `batch_size` 16, `lr` 5e-4, `weight_decay` 0.01, `grad_clip` 1.0; `epochs` 10 (fixed in the sweep) |
| Initial sampling | | `n_initial` 50000; factors 3–10; `conj_len_max` 4; `min_expanded_len` 5 |
| Generation | | `n_samples` = 1.1·pool (derived); `temperature` 1.0; `top_k` 50; `top_p` 0.95; `max_length` 512 |
| Local search | Fixed | `num_insert_samples` 5; `num_conj_samples` 5; `conj_max_len` 4; factors 1–10; `conj_move_strategy` deterministic |
| Local search | Swept | `beam_width`, `max_steps` |
| Workflow | | `num_iterations` 20 (base); `top_k` = `max_pool_size` (derived); `parallel_workers` 12; `seed` 12345 (base) |
| Workflow | Sweep seed | 42 in `pattern_boost_sweep.yaml`. The seed actually used by sweep_1 is unknown |
| Baseline challenges | Generator | `configs/generate_sample.yaml`: 1000 samples, `seed` 42, `max_relator_len` 5, factors 3–10, `conj_len_max` 4, `min_expanded_len` 10 |

## Related material
- [[patternboost-generation-methodology]] · [[patternboost-generation-data]] · [[patternboost-generation-results]]
- [[dep-b25-pyproject-agentic]]
- [[project-challenge-gen]]
