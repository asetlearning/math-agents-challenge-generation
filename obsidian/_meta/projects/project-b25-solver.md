---
title: Project profile — b25-solver
project: b25-solver
owner: asetlearning
repos:
  - "[[dep-b25-pyproject-agentic]] — main experimental repo (Python/uv): PatternBoost loop (algorithms/pattern_boost, experiments/pattern_boost), challenge-gen bench (experiments/challenge_gen/bench); new code on branches, merge with owner approval"
  - "[[dep-tcgraph-agentic]] — C++ core (submodule cpp/tcgraph of b25): Word, 2.5-reduction, pattern_boost engine (sampler, scorers, local search); exposed via tcgraph_ext"
dependencies:
  - "[[dep-tcgraph-agentic]] — may-modify (on branches; bump the b25 submodule pin when bindings change)"
  - "[[dep-remote-jobs]] — infrastructure; every remote run goes through rjob"
  - "[[dep-kbmag]] — read-only; held-out solver and verifier (verified-kb)"
  - "[[dep-gap]] — read-only; oracle"
build: "as [[project-challenge-gen]]"
test: "uv run pytest tests/ -v (b25); cd build && ctest (tcgraph). Any scorer or generator change: certificate re-expansion and trivial-abelianization check on a regression sample"
smoke: "PatternBoost smoke config on a local sample (as [[project-challenge-gen]]); E0 smoke: seed pool for one short benchmark word, 1k words"
lint: "C++: clang-format -style=file; Python: none configured"
languages: [Python 3.12, C++20]
run_pattern: "remote: rjob submit <job.toml> → rjob wait → rjob fetch. CPU experiments on cpuserver; model training on the GPU server (owner adds it). Local VM: code, tests, smoke only"
runs_dir: "runs/b25-solver/<experiment-id>/ in the local challenge-gen workspace, outside git (fetched rjob outputs + provenance.json)"
provenance_fields: [rjob job id + host, b25 git SHA, tcgraph SHA in cpp/tcgraph, uv.lock hash, config YAML as run, registry revision + sha256 of the target words, track (T-in / T-out / T-blind) and the excluded recipe ids, seed-pool source + hash, seeds, torch/transformers versions if a model ran, device, wall-clock]
heavy_processes: [pattern_boost_main, pb.local_search, "2.5-reduction of long words", "scorers over rotations × 16 images", kbprog]
protected_interfaces:
  - "FactoredWord JSON — the triviality certificate (shared with [[project-challenge-gen]])"
  - "bench solver contract (verdict, output word, certificate) — every solver result is verified through it"
  - "candidate registry data/b25_challenge_candidates.json — changed only with owner approval, per [[challenge-gen-candidate-workflow]]"
hot_paths:
  - "Policy (owner): heavy algorithms in tcgraph (C++) with Python bindings; one library, no duplicated code; develop in our repos only"
  - "Scorers (owner 2026-11-04): new scorers are welcome and may be combined with existing ones, but each is a class in the existing tcgraph scorer structure (WordScorer family, usable in HybridScorer and LocalSearcher), bound to Python, with no unnecessary changes to existing code. Efficiency is a high priority: the long-term targets are very long words, so state the per-call complexity and measure on words of 2,000-5,000 letters"
  - "LocalSearcher::search and the scorers (edit distance O(|w|·|c|); group distance over rotations and images)"
vault_docs:
  experiments: Experiments/Group Theory/B25 Solver/
  progress: Experiments/Group Theory/B25 Solver/_progress.md
  todo: Agents/<handle>/Lead/todo/todo-b25-solver.md   # private, gitignored — [[project-todo-convention]]
  datasets: Datasets/Group Theory/B25/
tags: [meta, convention, project/b25-solver]
---

# Project profile — b25-solver

## Goal

Build a **solver for trivial words in B(2,5) that adapts to the word it is given**, instead of acting the same way on every word as Knuth-Bendix, normal-closure enumeration and coset enumeration do. The hypothesis: moves (relators, rules) chosen from a distribution learned for the word shorten it more often than moves chosen without looking at it. Started 2026-11-04 by the owner.

- **First target:** the benchmark words of [[ds-b25-challenge-candidates]] (registry revision 3: 207 words, length 138–1313). They are certified trivial and survive every solver we have; [[project-challenge-gen]] generated them for this purpose. The HWW challenges come only after something works on the benchmark.
- **Success:** one verified break of a benchmark word (rare-event rule). A verified shortening counts as progress.
- **Verification:** every result goes through the `bench solver` contract ([[challenge-gen-candidate-workflow]] § 2): only `verified-cert` or `verified-kb` counts; unverified claims are counted separately and never acted on. Registry changes need the owner's approval.

## Approach

Two framings (owner note, 2026-11-04):
- **A, reduce w directly**, with a learned order of moves. Length is the signal; on hard words almost no single move shortens, so the signal is thin.
- **B, drive trivial words u towards w**, minimising a distance d(w, u). With d = |red(w·u⁻¹)| (free reduction), d < |w| is already a certified shortening of w. String distances (Hamming, edit) are not invariant under rotation or the automorphisms; combinations go through the hybrid scorer.

Stage 1 takes B with PatternBoost (factor words, transformer, local search; the existing b25 code). Group invariants of B(2,5) cannot tell w from u (both are trivial), so mathematical similarity measures are taken in the free group or in finite approximations.

## Information tracks

The target's own recipe and certificate are never shown to the solver (a recipe is a proof).

| Track | The solver may learn from |
|---|---|
| **T-in** (same arm) | words of the target's construction arm, other seeds |
| **T-out** (other arms) | words of the other construction arms only |
| **T-blind** (no recipes) | relators, certified short trivial words, solver outputs; no challenge-gen recipes |

The gap between T-in and T-out measures transfer; T-blind is the track that could carry over to the HWW challenges.

## Experiment naming

Experiments carry a code plus a meaning suffix (owner 2026-11-04), e.g. `E0-rebuild-seed-pool`; never the bare code.

## Roles

Developer develops and tests code; Experimenter-B25 runs experiments (experiments that need a GPU wait for the GPU server); Researcher and Math Expert review similarity measures and invariants; Validator replays certificates; Lead plans, reviews and commits.

## Related material
- [[project-challenge-gen]] — source of the benchmark, the generator and the bench
- [[challenge-gen-candidate-workflow]]
- [[ds-b25-challenge-candidates]]
- [[projects-and-dependencies-convention]]
