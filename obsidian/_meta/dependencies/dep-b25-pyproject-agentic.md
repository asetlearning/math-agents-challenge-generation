---
title: b25_pyproject_agentic (PatternBoost challenge generator, Python)
kind: our-repo
upstream: https://github.com/asetlearning/b25_pyproject_agentic (private)
license: unspecified
ownership: we-own
obtain: "git clone https://github.com/asetlearning/b25_pyproject_agentic.git; then git submodule init && git config submodule.cpp/tcgraph.url https://github.com/asetlearning/tcgraph_agentic.git && git submodule update (local URL override — see Known pitfalls)"
build: "uv sync   # Python 3.12, scikit-build-core + pybind11 build the tcgraph_ext extension; force C++ rebuild: uv sync --reinstall-package b25-pyproject"
test: "uv run pytest tests/ -v"
versions_in_use:
  - "main @ 7e50fea (2026-10-05: CLAUDE.md merged; code unchanged since 7d32335b, 2026-07-24); submodule cpp/tcgraph still pinned at c09327705a, so remote jobs override it to tcgraph main"
local_patches: []
capabilities:
  - "challenge generation: PatternBoost loop (GPT-2 over factor-word token streams + C++ beam local search + scoring + top-k selection) producing words trivial in B(2,5) by construction (products of conjugates of relators)"
  - "challenge generation: random certified trivial words (sample generator over standard w⁵ relators) — used as baseline challenges"
  - "challenge generation: scorers toward target words (hellinger, hamming, edit, word_product_length, abelianized_product_length) and target-free (length_range, high_power_count, dehn_function, hybrid)"
  - "experimentation: parameter sweeps with per-trial challenge windows and a marimo dashboard (success rate, iterations/time to first match, Pareto frontier)"
  - "group theory (via tcgraph_ext bindings to [[dep-tcgraph-agentic]]): 2.5-power reduction, TC-based semi-decision of triviality, relation-based shortening — C++ speed from Python"
heavy_processes: [pattern_boost_main (model training + parallel local search), "2.5-power reduction of long words via tcgraph_ext", attempt_to_decide_if_trivial]
mcp: none
local_checkouts:
  asetlearning: ~/Research/challenge-gen/b25_pyproject_agentic
docs: "repo README.md, CLAUDE.md (agent context; merged to main via PR #1, 7e50fea, 2026-10-05), experiments/pattern_boost/README.md, experiments/dashboards/README.md"
used_by: ["[[project-challenge-gen]]"]
tags: [meta, type/reference]
---

# b25_pyproject_agentic

## What it is
This is the main experimental repo for [[project-challenge-gen]]. It holds the Python implementation of the PatternBoost challenge generator, the configs, the sweep machinery and the dashboards. Through the `cpp/tcgraph` submodule and the `tcgraph_ext` pybind11 module, it uses the C++ core in [[dep-tcgraph-agentic]] for everything heavy: expansion, sampling, scoring, local search and 2.5-reduction.

## How we use it
- **Run**:
  - `uv run python -m experiments.pattern_boost.pattern_boost_main run configs/<x>.yaml` for a single run, written to `output/run_<ts>/`.
  - `... sweep configs/pattern_boost_sweep*.yaml` for a sweep, written to `<output_dir>/sweep_<ts>/` with `sweep_summary.json` and `combo_NNNN_<slug>/trial_NNNN/{run.jsonl, run.matches.jsonl, tokenizer/, iter_NNNN/}`.
- **Baseline challenges**: `uv run python -m experiments.pattern_boost.experiment_local_search sample configs/generate_sample.yaml` writes `relators_sample_n{N}_{ts}.json` plus `.factorwords.json` (the certificates).
- **Dashboard**: `uv run marimo run experiments/dashboards/sweep_dashboard.py`.
- **Code map**:

  | What | Where |
  |---|---|
  | Loop | `algorithms/pattern_boost/workflow.py:run_pattern_boost` |
  | Model | `model.py` (GPT-2 build/train/sample) |
  | Tokenizer | `tokenizer.py` (`[BOS] ([REL_i] ([CONJ_±k]+ \| [CONJ_EMPTY]) [SEP])+ [EOS]`, optional HF BPE) |
  | Scorer factory | `common.py:make_scorer` |
  | Relator sets | `relators.py` (standard / hybrid with BPE generators) |
  | Sweep | `sweep.py` |
  | Bindings | `cpp/bindings*.cpp` |
- **Python access to tcgraph**: prefer calling `tcgraph_ext` (see [[dep-tcgraph-agentic]] § How we use it) over reimplementing algorithms in Python.

## Protected surfaces
- The FactoredWord JSON format and the relator JSON schema (`{"R1": {"version", "word", "details?"}}`).
- The tokenizer stream format, since trained checkpoints depend on it.
- The `sweep_summary.json` and `run.matches.jsonl` layout, which the dashboard and the vault results tables read.
- The configs are YAML mirroring dataclasses, and unknown keys raise an error. Add new keys to the dataclasses.

## Known pitfalls
- **Submodule URL and stale pin.** `.gitmodules` points at `git@github.com:gt-computations/tcgraph.git`, which this account's token cannot reach. The source of truth is `asetlearning/tcgraph_agentic`. The pin `c09327705a` predates scorers the bindings use (Hybrid, Dehn, LengthRange, Abelianized, HighPower), so a fresh build at the pin is **expected to fail**. This is not yet verified, because `uv sync` was not run on 2026-10-05. It is documented only; fixing it awaits approval. To build, override the URL locally and check out tcgraph_agentic `main` inside `cpp/tcgraph`. Note that `main` itself breaks only the `test_pb_local_search` target, which b25 excludes via `EXCLUDE_FROM_ALL`.
- **Triviality depends on the relator set.** `relators.relators_file` words are trusted as trivial and are not verified. The README's claim that "names are preserved" is wrong; they are renamed `R1..Rn` after passing through a `set`. Combining `relators_file` with `use_compression` is unsupported. The abelianization filter (`_is_trivial_abelianization`) is a necessary condition only.
- **What "match" means.** The expanded candidate, **unreduced**, must equal the challenge string up to cyclic rotation (`workflow.py:379–382`). There is no reduction, inverse equivalence or score threshold.
- **Missing provenance.** Runs log the config only: no git SHA, submodule SHA, data hashes or package versions. Model initialisation and training shuffles are unseeded, so runs are not bit-reproducible.
- **Data is not in the repo.** Challenge files, relator sets and tokenizers live outside it. `configs/pattern_boost_smoke.yaml` hard-codes `/media/psf/b25_pyproject/...`.
- **Known code issues, not fixed:**
  - `_merge_pool` keeps the newest entries, not the best.
  - Sweep-level log events land in the previous trial's `run.jsonl`; treat `sweep_summary.json` as the reliable aggregate.
  - `experiment_local_search.py:82` unpacks `SearchResult` as a tuple, which will likely raise a TypeError.
  - `wheel.packages` lists a non-existent `ml`.
  - The READMEs omit the `run|sweep` subcommands.
- **Branch policy** (owner instruction, 2026-10-05): all new experimental code goes on a separate branch, and nothing merges to `main` without the owner's approval.

## Related material
- [[projects-and-dependencies-convention]]
- [[project-challenge-gen]]
- [[dep-tcgraph-agentic]]: the C++ core, as a submodule
- [[charton-2024-patternboost]]: the method
