---
title: "PatternBoost Generation on B(2,5) — methodology"
domain: group-theory
project: challenge-gen
instance: B(2,5)
experiment_type: patternboost-generation
status: pending
author: asetlearning
source: "/media/psf/writeups/B25Pattern_Boost_implementation.md (+ B25Pattern_Boost_notes.md, TODOLOG.md) — Alex Myasnikov"
tags: [agent/human, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/trivial-words, topic/hard-instance-generation, topic/tokenization, project/challenge-gen, status/pending, methodology]
---

# PatternBoost Generation on B(2,5) — methodology

> This condenses Alex Myasnikov's design writeup (`/media/psf/writeups/B25Pattern_Boost_implementation.md`, May–July 2026) and maps it onto the code in [[dep-b25-pyproject-agentic]] and [[dep-tcgraph-agentic]]. The project motivation is in [[project-challenge-gen]].

## What this experiment type is

PatternBoost ([[charton-2024-patternboost]]) alternates two phases. In the first, a cheap **local search** improves many candidates. In the second, a **transformer** trained on the best candidates proposes new ones. Here a candidate is not a raw word in a and b. It is a **factor word**:

$$w = \prod_{i=1}^{N} c_i^{-1}\, R_{k_i}\, c_i, \qquad R_k \in R^*\ \text{(relators, e.g. } v^5\text{)},\ c_i \in \langle a,b\rangle,$$

so w is trivial in B(2,5) **by construction**. The list of (k_i, c_i) pairs is the proof. The model only ever emits factor structure, local search only edits factor structure, and the scorer compares the expanded word with target words. The writeup frames this as "the proof of the property is in the process itself".

## Why we ran this

Random products of conjugates are certified trivial, but they are *generic*: the 2.5-power heuristic reduces them easily. The hypothesis is that a score that pulls candidates toward known hard words (the challenge words) will drive PatternBoost to produce certified trivial words that **share structure with the hard ones**. The phase-1 question is narrower: can the loop *steer* toward a given target at all?

## The PatternBoost loop (formal)

At iteration i, with model M_i:
1. **Generate.** Sample S = {M_i^{(k)}(p)}, k = 1..N, at temperature > 0.
2. **Local search.** S* = {𝓛(c) | c ∈ S}, where 𝓛 : S → 𝒮 must land in the search space, i.e. return a trivial word. A model output is either decoded *algorithmically* into a guaranteed-trivial instance, or rejected. Checking triviality after the fact would defeat the purpose.
3. **Select.** D̂ = the top-scoring outputs by R(c). Then D_i = τ(D̂), where τ maps them back into the model's input format.
4. **Fine-tune.** M_{i+1} = tune(M_i, D_i). Repeat until the score passes a threshold θ, or until the iteration budget is spent.

**Code mapping** (`b25:algorithms/pattern_boost/workflow.py:run_pattern_boost`):
- **Initial sample:** the C++ `generate_words`, giving random factor words. These are scored, and the top `max_pool_size` are kept.
- **Model:** GPT-2 (`model.py`), trained on the pool and then sampled.
- **Decoding:** `tokenizer.try_decode`. Malformed outputs are dropped.
- **Local search and selection:** C++ `LocalSearcher.search` runs in parallel, then the outputs are scored, and the top `top_k` are merged into the pool. A match stops the loop.

## Representation: factor-word token stream

- **Tokens:** one `[REL_i]` per relator; one `[CONJ_±k]` per generator, used for the conjugator letters; specials `[BOS] [EOS] [SEP] [CONJ_EMPTY] [PAD]`. The stream is `[BOS] ([REL_i] ([CONJ_±k]+ | [CONJ_EMPTY]) [SEP])+ [EOS]`. Optionally, HuggingFace BPE is trained over this stream (`tokenizer.use_bpe`).
- **The design also has an alternative:** BPE tokens learned from the challenge words become relators τ⁵, with separate conjugation tokens. The code implements this as **generator compression** (`WordCompressor`). Each BPE token becomes a new generator g; g⁵ and g⁻⁵ are relators; and the scorer decodes back to a and b.
- **Representation is non-unique.** For example, `aaabb = g₁g₁g₁g₂g₂ = g₁g₃g₄` when g₃ = aa and g₄ = bb. Because of this, scoring and stopping act on expanded words in {a, b}.

## Relator sets

| Source | Config | Soundness |
|---|---|---|
| **Standard** (default) | `max_relator_len` L | All cyclically reduced v⁵ with \|v\| ≤ L: 4, 16 and 44 relators for L = 1, 2, 3. Trivial in free B(2,5) |
| **Hybrid / compressed** | BPE generators | g⁵ only, for non-standard tokens |
| **From file** | `relators.relators_file` | E.g. 2.5-reduced shortlex KB rules. **Trusted, not verified.** The certificate is then only as good as the file |

## Scoring

The writeup's design is challenge similarity, R(w, c) = −D(f(w), f(c)) over token-frequency vectors, with R₁ = max over challenges and R₂ = mean over challenges. It considers several distances:
- frequency-based: cosine, JS, **Hellinger** (good for sparse histograms), weighted Jaccard;
- structural: **Levenshtein**, n-gram similarity.

The implemented scorers, all in C++ and selected with `scoring.type`:

| Type | Notes |
|---|---|
| `hellinger` | Bigram histograms |
| `hamming` | |
| `edit` | Levenshtein |
| `word_product_length` | \|reduce(w c⁻¹)\| |
| `abelianized_product_length` | |
| `length_range` | Optionally on the 2.5-reduced length |
| `high_power_count` | Penalises powers ≥ 2.5 |
| `dehn_function` | \|factors\| / \|freely reduced w\| |
| `hybrid` | Weighted sum of the above |

Options: `reduce2_5` and `penalize_trivial`, which scores 0 if the word 2.5-reduces to empty.

Any scorer that runs 2.5-reduction is a **heavy** process on long words.

## Local search

Moves preserve triviality:
- **The design** lists three moves: insert a relator r at position i; insert a cyclic permutation of r; apply a rewrite rule lhs → rhs with lhs·rhs⁻¹ = 1.
- **The implementation** works on factor words: relator swap (exhaustive); conjugator mutation (`deterministic`, i.e. all edit-distance-1 neighbours, or `random`); factor insertion (sampled); factor deletion (exhaustive).

The frontier is beam search with width N: N = 1 is greedy, and N = ∞ is enumeration. Parameters are `beam_width`, `max_steps`, `num_insert_samples`, `num_conj_samples`, `conj_max_len`, `min_factors` and `max_factors`.

## Sanity check: abelianization

Every trivial word must have exponent sums ≡ 0 (mod 5) in a and b. This is necessary, not sufficient. It is checked on every expansion (`_is_trivial_abelianization`) to catch bugs, since an accidental bug is unlikely to preserve it.

## How we ran it (baseline)

1. Generate random target challenges from the same sampler: `experiment_local_search sample configs/generate_sample.yaml`, giving `relators_sample_n*.json` plus `.factorwords.json`.
2. Sweep: `pattern_boost_main sweep <sweep.yaml>`. Each trial targets one challenge (`sample_size: 1`, non-overlapping windows), and there are 50 trials per combo. Swept parameters: `epochs` = 10; `beam_width` ∈ {1, 5, 10}; `max_steps` ∈ {1, 5, 10}; `max_pool_size` ∈ {100, 1000, 5000}.
3. Inspect results with the marimo dashboard (`sweep_dashboard.py`).

The baseline sweep used sweep root `data/pattern_boost_experiments/pb_sweep/sweep_20260522_013909` and config `configs/pattern_boost_sweep_1.yaml`. That config is **not in the repo**, and the sweep data lives outside git. See [[patternboost-generation-data]].

## How it was validated

- **Certificates.** Every candidate is a product of conjugates of standard relators by construction, so triviality in free B(2,5) follows from the expansion. With file or compressed relators this holds only if those relators are themselves certified.
- **Bug detection.** The abelianization check runs on every expansion.
- **Not yet done:** no independent re-expansion of stored FactoredWords, and no GAP B₀(2,5) or kbmag cross-check of generated words. Proposed: re-expand them, run the [[2026-09-30-b25-b0-challenge-triviality]] pipeline as a necessary condition, and use [[dep-kbmag]] as an independent check. Status: **Validation of generated words: none yet.**
- **The sweep validates the steering mechanism, not hardness.** A target counts as found only on exact cyclic-rotation equality of the expanded, *unreduced* strings.

## What "success" means

- **Baseline:** a trial succeeds if any candidate's expanded word equals the target random challenge up to cyclic rotation, within the iteration budget. This is recorded in `run.matches.jsonl`.
- **Project-level success** is defined in [[challenge-gen-success-metrics]] (2026-10-05): L1 means 2.5-reduction resistance ρ ≥ 0.5; L2 adds the Dehn proxy D ≥ 1 on a minimised certificate; L3 is quadratic growth. Under these metrics the baseline random targets are expected to score ρ = 0.

## Related material
- [[PatternBoost Generation/_type|experiment type]] · [[patternboost-generation-results]] · [[patternboost-generation-data]]
- [[project-challenge-gen]] · [[Challenge Generation/_progress]]
- [[charton-2024-patternboost]]: the method
- [[_synthesis-hard-instance-generation]]: certified generators tend to produce generic instances, which matches what was observed here
- [[elder-2015-random-trivial-words]]: the same idea of the trajectory serving as the certificate
- [[miasnikov-1999-ac-genetic]]: an earlier warning that randomly scrambled instances are easily undone
