---
title: tcgraph_agentic (C++ group-theory core)
kind: our-repo
upstream: https://github.com/asetlearning/tcgraph_agentic (private)
license: see repo LICENSE
ownership: we-own
obtain: "git clone https://github.com/asetlearning/tcgraph_agentic.git — or as the `cpp/tcgraph` submodule of [[dep-b25-pyproject-agentic]] (see Known pitfalls: the submodule URL currently points elsewhere)"
build: "cmake -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build -j  # out-of-source only; Debug adds ASan + -Wall -Werror"
test: "cd build && ctest   # 2026-10-05: 8/9 pass; test_pb_local_search does not compile on main (see Known pitfalls)"
versions_in_use:
  - "main @ a0d5e92 (2026-10-05: CLAUDE.md merged; code unchanged since 26f4f5a9, 2026-07-24)"
  - "c09327705a (2026-06-18) — the commit pinned as submodule in b25_pyproject_agentic main (13 commits behind main)"
local_patches: []
capabilities:
  - "group theory: Todd–Coxeter coset enumeration for 2-generator presentations (TCGraph<2>); decides finite index / finite order only when enumeration closes within coset_bound"
  - "group theory: semi-decision of triviality in B(2,5) (attemptToDecideIfTrivial_in_B_2_5) — `true` is sound; `false` only means non-trivial in the cover ⟨a,b | v⁵, |v| ≤ k⟩, NOT in B(2,5); nullopt = unknown"
  - "group theory: sound word shortening via geodesics in a partial Cayley graph built from Burnside relators or a supplied relator file (attemptToReduceUsingRelations[Greedy])"
  - "group theory: 2.5-power greedy reduction (reduction2_5::greedyReduce*, greedyReduceCyclicExhaustive) — every rewrite is a valid B(2,5) identity; heuristic, not a normal form, may not reach the empty word"
  - "group theory: Havas–Wall–Wamsley (1974) nilpotent generators and relations of B₀(2,5), expanded to words in a,b"
  - "challenge generation: pattern_boost primitives — RelatorMap/Factor/FactoredWord (products of conjugates of relators = triviality certificate), samplers, scorers, beam local search, BPE WordCompressor"
heavy_processes: [experiments.b25_cayley_graph_approximation, experiments.b25_reduce_challenges_given_relators, experiments.b25_greedy_reduce_tcgraph_challenges, pb.local_search, "2.5-power reduction of long words (greedyReduce*, greedyReduceCyclicExhaustive — findSquares is O(n²)), wherever called, incl. scorers with reduce2_5 / reduce_before_scoring"]
mcp: none
local_checkouts:
  asetlearning: ~/Research/challenge-gen/tcgraph_agentic   # also ~/Research/challenge-gen/b25_pyproject_agentic/cpp/tcgraph (submodule)
docs: "repo README.md, pattern_boost/README.md, CODE_GUIDELINES.md, CLAUDE.md (agent context; merged to main via PR #1, a0d5e92, 2026-10-05)"
used_by: ["[[project-challenge-gen]]"]
tags: [meta, type/reference]
---

# tcgraph_agentic

## What it is
This is our C++20 group-theory core for B(2,5) work. Generators are encoded as integers: a=1, A=−1, b=2, B=−2. Its main parts:
- **`Word`**: free and cyclic reduction, powers, periods, hashing, abelianization counts.
- **`TCGraph<n>`**: a Todd–Coxeter coset table with geodesic BFS and word tracking. When the tracked word gets a shorter geodesic, it throws `ShorterLengthFound`.
- **Word-problem drivers** for B(2,5) and arbitrary presentations.
- **`reduction2_5`**: maximal-power detection, plus greedy rewriting of base^p with 2.5 ≤ p < 5 to (base^(5−p))⁻¹.
- **The B₀(2,5) relations** from Havas–Wall–Wamsley.
- **`pattern_boost/`**, the C++ engine of the challenge generator. It has `RelatorMap` (`expandFactor` computes c⁻¹·R·c), `FactoredWord`, samplers, scorers (Hellinger, Hamming, Edit, WordProductLength, AbelianizedProductLength, LengthRange, HighPowerCount, DehnFunction, Hybrid), `LocalSearcher`, and `BPETokenizer`/`WordCompressor`.
- `mixer_agents/` is a stub JSON-lines agent SDK. It is not used by challenge-gen.

## How we use it
- **From Python, the preferred route.** Most essential procedures have Python bindings, so scripts get efficient C++ execution. The bindings are not in this repo; they live in [[dep-b25-pyproject-agentic]] (`cpp/bindings.cpp`, `cpp/bindings_pattern_boost.cpp`). They build the module `tcgraph_ext` and its submodule `tcgraph_ext.pattern_boost`. The binding surface:
  - `Word`;
  - `attempt_to_decide_if_trivial`, which releases the GIL;
  - `attempt_to_reduce_using_relations` and `..._greedy`;
  - `greedy_reduce2_5`, `greedy_reduce_cyclic2_5` and `greedy_reduce_cyclic_exhaustive2_5`;
  - the `ShorterLengthFound` exception;
  - `pattern_boost`: RelatorMap, sample generation, all scorers, LocalSearcher, WordCompressor.

  New experiment code should call these rather than re-implement them in Python. New heavy primitives should be added here in C++, exposed through b25's bindings, and the submodule pin bumped.
- **CLI binaries**, for standalone runs: `pb.generate_samples`, `pb.score_samples` and `pb.local_search`. The last two hard-code the Hellinger scorer. There are also `experiments.*` for TC-based reduction.

## Protected surfaces
- **Triviality invariant of `pattern_boost`.** A `FactoredWord` is a product of conjugates of relators, so its expansion is trivial **only if every relator in the `RelatorMap` is trivial in B(2,5)**.
  - `buildStandardRelators(L)` gives w⁵ for |w| ≤ L, which is safe.
  - Relators loaded from a file or built from BPE tokens are trusted without a check.
  - Local-search moves (relator swap, conjugator mutation, factor insertion and deletion) preserve the product-of-conjugates form.

  Any change to the moves or to `expandFactor` must keep this invariant.
- **The `FactoredWord` JSON format** (`{word, relator_indices, relator_names, conjugators, version}`) and the 1-based relator indexing.
- **The `tcgraph_ext` binding API** that b25 scripts depend on. Changing a C++ signature requires a matching binding change and a pin bump in b25.

## Known pitfalls
- **main does not build all targets.** `pattern_boost/tests/test_pb_local_search.cpp` still calls `LocalSearcher::scoreWord`, which commit 26f4f5a9 removed. Verified on 2026-10-05 (GCC 13.3, CMake 3.28, Release, VM): `cmake --build` fails only on that target (`test_pb_local_search.cpp:234: 'class pattern_boost::LocalSearcher' has no member named 'scoreWord'`). All other targets build, and `ctest` passes 8/9; test 8 is "Not Run". To build just the libraries and other targets, use `cmake --build build --target <name>`.
- **The b25 submodule points elsewhere.** b25's `.gitmodules` sends `cpp/tcgraph` to `git@github.com:gt-computations/tcgraph.git`, not to this repo. Its pin `c09327705a` predates the Hybrid, Dehn, LengthRange, Abelianized and HighPower scorers that b25's bindings use. Local workaround, which changes only local config: `git config submodule.cpp/tcgraph.url https://github.com/asetlearning/tcgraph_agentic.git`, then check out the wanted commit. This is documented, not fixed (decision of 2026-10-05).
- **The word-problem semi-decision's `false` is not a non-triviality proof** (see capabilities). The Python docstring in b25 overstates it.
- **Which group the computation is in.** The B₀(2,5) HWW relations live in the *restricted* group. `pattern_boost/README.md` mislabels B(2,5) as "restricted" and calls the challenge words "known to be trivial". They are known trivial only in B₀(2,5); see [[B25/_progress]].
- **Hybrid scorer limitations.** `HybridScorer` ignores each sub-scorer's `reduce2_5` and `penalize_trivial`. `DehnFunctionScorer` throws inside Hybrid, since it is `scoreSample` only.
- **Local search has no visited set,** and every neighbour is expanded twice. Cost is O(beam × neighbours × steps × score).
- **Toolchain.** `std::format` needs GCC 13+ or Clang 17+. spdlog and CLI11 are fetched at configure time, so network access is needed.
- **Agent docs.** `CLAUDE.md` is on main since 2026-10-05 (PR #1, a0d5e92). Keep it in sync with code changes.

## Related material
- [[projects-and-dependencies-convention]]
- [[project-challenge-gen]]
- [[dep-b25-pyproject-agentic]]: consumer, which holds the Python bindings
- [[dep-gap]], [[dep-kbmag]]: independent validation paths
