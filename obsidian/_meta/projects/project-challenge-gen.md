---
title: Project profile — challenge-gen
project: challenge-gen
owner: asetlearning
repos:
  - "[[dep-b25-pyproject-agentic]] — main experimental repo (Python/uv): PatternBoost generator, configs, sweeps, dashboards; all new experimental code on branches, merge to main only with owner approval"
  - "[[dep-tcgraph-agentic]] — C++ core (submodule cpp/tcgraph of b25): Word, TC graph, 2.5-reduction, pattern_boost engine; exposed to Python via tcgraph_ext"
dependencies:
  - "[[dep-tcgraph-agentic]] — may-modify (on branches; bump the b25 submodule pin to the right tcgraph_agentic commit when bindings change)"
  - "[[dep-gap]] — read-only; oracle and validator (word problem in finite / polycyclic quotients, e.g. B₀(2,5) via ANUPQ)"
  - "[[dep-kbmag]] — read-only; validator (Knuth-Bendix / rewriting), run as the GAP package or standalone kbprog — an independent path from GAP's word problem"
build: "b25: git submodule init && git config submodule.cpp/tcgraph.url https://github.com/asetlearning/tcgraph_agentic.git && git submodule update && uv sync  (C++ rebuild: uv sync --reinstall-package b25-pyproject). tcgraph standalone: cmake -B build && cmake --build build"
test: "uv run pytest tests/ -v (b25); cd build && ctest (tcgraph). Plus, for any generator change: certificate check on a regression sample (see Test matrix)"
smoke: "uv run python -m experiments.pattern_boost.pattern_boost_main run configs/pattern_boost_smoke.yaml — NOTE: its challenges path is hard-coded to /media/psf/b25_pyproject/...; point it at a local sample first"
lint: "C++: clang-format -style=file (tcgraph CODE_GUIDELINES.md); Python: none configured"
languages: [Python 3.12, C++20, GAP]
run_pattern: "timeout <cap> uv run python -m experiments.pattern_boost.pattern_boost_main run|sweep configs/<x>.yaml   (baseline challenges: experiments.pattern_boost.experiment_local_search sample configs/generate_sample.yaml)"
runs_dir: "b25 repo: output/run_<ts>/ and <output_dir>/sweep_<ts>/combo_NNNN_<slug>/trial_NNNN/ (run.jsonl, run.matches.jsonl, tokenizer/, iter_NNNN/); sweep_summary.json at sweep root. Existing sweeps: data/pattern_boost_experiments/pb_sweep/ (outside git)"
provenance_fields: [b25 git SHA, tcgraph_agentic SHA actually checked out in cpp/tcgraph, uv.lock hash, config YAML (as run), relator source + hash, challenge file + hash, sweep/run seeds, torch/transformers versions, GAP version + kbmag build if validation ran, certificate (FactoredWord JSON) format version, host (CPU/GPU/RAM), wall-clock — NOTE: the code currently logs only the config]
heavy_processes: [pattern_boost_main, pb.local_search, "2.5-power reduction of long words (tcgraph greedyReduce*; also inside scorers with reduce2_5)", attempt_to_decide_if_trivial, gap, kbprog]
protected_interfaces:
  - "FactoredWord JSON {word, relator_indices, relator_names, conjugators, version} — the triviality certificate"
  - "relator JSON schema {\"R1\": {version, word, details?}}"
  - "tokenizer stream format [BOS] ([REL_i] ([CONJ_±k]+ | [CONJ_EMPTY]) [SEP])+ [EOS] — trained checkpoints depend on it"
  - "sweep_summary.json + run.matches.jsonl layout — dashboard and vault results tables read them"
  - "tcgraph_ext binding API — b25 scripts depend on it"
hot_paths:
  - "LocalSearcher::search — O(beam × ~250+ neighbours × steps × score cost); no visited set; neighbours expanded twice"
  - "scorers with reduce2_5 / length_range reduce_before_scoring — greedyReduceCyclicExhaustive, findSquares O(n²)"
  - "edit-distance scorer — O(|w|·|c|) per challenge"
vault_docs:
  components: TBD
  code_reviews: TBD
  math_validation: Architecture/Mixer/Documentation/Math Validation/   # shared location until the project has its own
  experiments: Experiments/Group Theory/Challenge Generation/
  progress: Experiments/Group Theory/Challenge Generation/_progress.md
tags: [meta, convention, project/challenge-gen]
---

# Project profile — challenge-gen

## Goal

**Challenge generation.** Build ways to generate *hard* problem instances that come with a proof that they have a solution. The instances serve as benchmarks and training sets for new search algorithms, including ML, LLM and RL approaches. Phase 1 is **hard trivial words ("challenges") in B(2,5)**. If that works, the project extends to other problems, e.g. searching for counterexamples to Andrews–Curtis. The standing state is in [[Challenge Generation/_progress|the progress note]].

## Difficulty metrics and success criteria (owner, 2026-10-05)

Full definitions are in [[challenge-gen-success-metrics]]. In short, generate words **provably trivial in free B(2,5)** (certificate or construction) that are **hard to decide**:
- **Metric 1, 2.5-reduction resistance.** ρ = |R₂.₅(w)| / |w̄|, where R₂.₅ is greedy then cyclic-exhaustive 2.5 reduction. Pass: R₂.₅(w) ≠ 1 and ρ ≥ 0.5. Every random factor word reduces to 1 (owner's experiments), so this separates hard from generic. The reduction costs O(n²) to O(n³), so screen with shifts {0, 0.5} on the pool and certify with all shifts on finalists. Never run it per neighbour.
- **Metric 2, Dehn proxy.** D = |F*| / |w̄| on the **minimised** certificate F*: freely cancelling factor blocks are removed by loop erasure. It is an upper bound on area, and it counts only for words passing Metric 1. Good: D ≥ 1. Great: a family with |F*| ≈ c·n², i.e. quadratic area.
- **Success levels:** L0 valid (certified), L1 hard (Metric 1), L2 L1 + D ≥ 1, L3 quadratic family.
- **Similarity** to the 150 challenge words is now secondary and optional.

## Idea & motivation

Many hard open problems in mathematics reduce to search problems. Often the task is to find a connection between two vertices in a search space, or a path in a large (possibly infinite) group. For open problems it is usually not known whether such a path exists: the instances in question are potential counterexamples. So if we want to develop new algorithms, in particular with machine learning (LLMs, RL, …), how do we test their performance, and where do training sets come from?

The counterexamples themselves are one option. But there are usually few of them, and any real progress on them is almost equivalent to solving the problem. That leaves very little signal for evaluation and training.

Random samples are another option, generated by some procedure or picked as random vertices of the search-space graph. Here a solution is known to exist, so algorithm performance can be measured. Random instances are a good baseline. However, most random generation procedures produce *generic* (uniformly distributed) instances. In many settings, solving a random instance is known to be much easier than solving the special "hard" instances we care about, and those are very rare.

We need a way to sample instances that share properties with the hard ones. This is not trivial. A "hard" instance is one where checking the required property is as hard as solving the problem on that instance. So the generation process must be organised so that **the proof of the property is part of the process itself**: it can be attached to the instance, or the process reversed, as evidence.

## Problem instances

| Phase | Problem | Instance property | Status |
|---|---|---|---|
| 1 | B(2,5): free Burnside group, 2 generators, exponent 5 | word is trivial in B(2,5), and hard to reduce | active |
| later (candidate) | Andrews–Curtis conjecture ([[andrews-curtis-conjecture]]) | balanced presentation is AC-trivial, and hard to trivialise | not started |
| later (candidate) | other search-reducible open problems | TBD | not started |

For B(2,5), triviality in the restricted quotient B₀(2,5) is **necessary but not sufficient** for triviality in the free B(2,5) (see [[B25/_progress]]). A certificate must prove triviality in the group the experiment claims.

## Components under test

See *Current implementation* below. Record the component actually used in each experiment: the scorer type, the relator source, and the local-search strategy.

## Current implementation — PatternBoost generator (B(2,5))

Design and results: [[B25/PatternBoost Generation/_type|PatternBoost Generation]] (methodology, data, results). The loop follows [[charton-2024-patternboost]]:

```
initial sample (C++ generator: random products of conjugates of relators)
   → score → keep top max_pool_size                         ┐
   → train GPT-2 on factor-word token streams  (model.py)    │ repeat
   → sample n_samples streams → decode to FactoredWords      │ num_iterations
   → C++ beam local search per candidate (LocalSearcher)     │ (stop on match)
   → score → merge top_k into pool                           ┘
```

| Component | Where |
|---|---|
| Loop | `b25:algorithms/pattern_boost/workflow.py:run_pattern_boost` |
| Model | `model.py` (GPT-2) |
| Token stream | `tokenizer.py` |
| Scorers | `common.py:make_scorer` → C++ `pb_scoring` |
| Relator sets | `relators.py` + C++ `pb_relator_map` |
| Local search | C++ `pb_local_search`. Moves: relator swap, conjugator mutation (deterministic edit-distance-1 or random), factor insertion, factor deletion |
| Sweeps and dashboard | `sweep.py`, `experiments/dashboards/sweep_dashboard.py` |

## Certificate model

The certificate is the **factor word**: w = ∏ cᵢ⁻¹ R[idxᵢ] cᵢ. It is checked by re-expanding it and comparing with w, which is cheap and needs no word-problem solver. It is sound **only if every relator in the RelatorMap is trivial in the group claimed**:
- **Standard relators** v⁵ (|v| ≤ L) are trivial in free B(2,5). This is safe.
- **File relators** (`relators.relators_file`, e.g. 2.5-reduced shortlex KB rules) and **BPE-token relators** (g⁵ for compressed generators g) are trusted without verification. They need their own provenance, and they must be certified trivial in free B(2,5), not just in B₀(2,5), before the "certified in free B(2,5)" claim holds.
- The abelianization check (exponent sums ≡ 0 mod 5) is a cheap necessary condition, used to catch bugs.

The model never emits letters directly, so malformed generations decode to `None` and are dropped. Every candidate in the pool is a product of conjugates by construction.

## Known issues (as of 2026-10-05; documented, not fixed)
- **Submodule.** b25's `.gitmodules` points `cpp/tcgraph` at `gt-computations/tcgraph`, not `asetlearning/tcgraph_agentic`. The pin `c09327705a` is 13 commits behind tcgraph_agentic main and predates the scorers b25 binds. Use the local URL override and check out the right commit; see [[dep-b25-pyproject-agentic]].
- **tcgraph_agentic main** fails to build `test_pb_local_search`, which uses the removed `scoreWord`; see [[dep-tcgraph-agentic]].
- **No provenance or seeds** are logged: no SHAs or data hashes, and model init and training are unseeded. Data files are not in git.
- **Pool merge** keeps the newest entries, not the best. Sweep-level logs land in trial logs.
- **Which group.** "Match" means exact cyclic equality with a target and says nothing about hardness. The challenge words are known trivial only in B₀(2,5).

## Core requirement — certificates

Every generated instance ships with a **certificate**, e.g. a generation trace or an explicit derivation from relators, from which the property can be checked mechanically and cheaply. Validator checks certificates. Where possible, it also cross-checks the property through a path independent of the generator, such as GAP's word problem in a finite quotient or kbmag rewriting, and records which path it used.

## Test matrix

| Change kind | Required |
|---|---|
| New or changed generator | certificate check on a regression sample (all certificates verify) + independent property check on a subsample (GAP/B₀ or kbmag) |
| New or changed certificate format | Validator review of the format's soundness + re-verification of existing benchmark sets |
| New hardness metric | documented definition + baseline values on random (generic) instances and on the 150 human challenge words |

## Protected interfaces — why each one exists

- **Challenge + certificate format.** Benchmarks, training pipelines and validators all consume it. Once defined, changes need a version bump and Lead approval.
- **`runs/challenge-gen/` layout.** Results tables and the progress note link into it.

## Experiment template fields

In [[experiment]], also fill:
- **Target property**: what each generated instance is claimed to satisfy (e.g. "trivial in free B(2,5)").
- **Group computed in**: free B(2,5), restricted B₀(2,5), or a named finite quotient. Mandatory for Burnside instances.
- **Generation procedure**: the algorithm and parameters, plus the seed.
- **Certificate type**: what is attached and how it is checked.
- **Hardness metric(s)**: how "hard" is measured, e.g. performance of reference solvers or length/structure statistics, and the baseline it is compared with.

## Related material
- [[myasnikov-ushakov-2011-random-van-kampen]]: theory anchor for the metrics: random diagrams are hyperbolic and shallow
- [[projects-and-dependencies-convention]]
- [[Challenge Generation/_progress]]: progress note
- [[project-b25]]: sibling project on B(2,5) itself
- [[B25/_progress]]
- [[dep-b25-pyproject-agentic]], [[dep-tcgraph-agentic]]: code
- [[dep-gap]], [[dep-kbmag]]
- [[B25/PatternBoost Generation/_type|PatternBoost Generation]]: first experiment type
- [[challenge-gen-success-metrics]]: difficulty metrics and success levels
- [[andrews-curtis-conjecture]]
- [[_synthesis-hard-instance-generation]]: literature scan of 2026-10-05 (12 papers)
- [[_moc-hard-instance-generation]]: reading path
- [[Concepts/certified-instance-generation]]: concept hub for the core requirement
