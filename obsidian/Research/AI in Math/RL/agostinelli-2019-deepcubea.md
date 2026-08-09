---
title: "Solving the Rubik's Cube with Deep Reinforcement Learning and Search (DeepCubeA); + McAleer et al. 2018 DeepCube (Autodidactic Iteration)"
authors:
  - "Forest Agostinelli"
  - "Stephen McAleer"
  - "Alexander Shmakov"
  - "Pierre Baldi"
year: 2019
venue: "Nature Machine Intelligence (2019); precursor McAleer, Agostinelli, Shmakov, Baldi, arXiv:1805.07470, NeurIPS 2018"
url: "https://arxiv.org/abs/1805.07470"
url_translated:
language: en
methodology_type: empirical
domain: ai
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
related:
  - "[[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]"
  - "[[chervov-2025-cayleypy-rl]]"
  - "[[futuhi-sturtevant-2026-admissible-heuristics]]"
quality_notes: "The primary source behind Experimenter's DeepCubeA proposal. DeepCubeA itself (Nature Machine Intelligence 2019) is paywalled — no arXiv preprint exists; a free PDF exists at cse.sc.edu/~foresta (Agostinelli's own site) and code at github.com/forestagostinelli/DeepCubeA, both used by the research subagent for this note. The 2018 NeurIPS precursor (DeepCube / Autodidactic Iteration, arXiv:1805.07470) is fully open and shares the core training procedure this note describes; the two systems differ in search-time combination (DeepCube: MCTS; DeepCubeA: weighted A*) and DeepCubeA drops DeepCube's policy head (value-only, DAVI vs. DeepCube's actor-critic ADI). Some figure/equation extraction from the DeepCubeA PDF was inconsistent across tool calls (compressed PDF stream parsing) — the GitHub README's plain-text description of the weighted-A* formula is the more reliable source and is what's reported below."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/reinforcement-learning
  - topic/monte-carlo-tree-search
  - topic/value-network
  - paper
  - status/draft
---

# Solving the Rubik's Cube with Deep Reinforcement Learning and Search (DeepCubeA) / DeepCube (Autodidactic Iteration)

## Abstract

**DeepCube (2018, arXiv:1805.07470, verified verbatim):** "A generally intelligent agent must be able to teach itself how to solve problems in complex domains with minimal human supervision. Recently, deep reinforcement learning algorithms combined with self-play have achieved superhuman proficiency in Go, Chess, and Shogi without human data or domain knowledge. In these environments, a reward is always received at the end of the game, however, for many combinatorial optimization environments, rewards are sparse and episodes are not guaranteed to terminate. We introduce Autodidactic Iteration: a novel reinforcement learning algorithm that is able to teach itself how to solve the Rubik's Cube with no human assistance. Our algorithm is able to solve 100% of randomly scrambled cubes while achieving a median solve length of 30 moves — less than or equal to solvers that employ human domain knowledge."

**DeepCubeA (2019, Nature Machine Intelligence)**: builds directly on the above, replacing MCTS with weighted A* search guided by a Deep Approximate Value Iteration (DAVI)-trained cost-to-go network; abstract not independently re-verified against primary text this session (paywalled), summary below per subagent's extraction from the free author-hosted PDF + GitHub README.

## TL;DR

Both systems solve a sparse-reward combinatorial puzzle (Rubik's Cube — no reward until fully solved, exactly the "must get worse before better" shape of problem the B25 team is asking about) by training a **cost-to-go value function via backward-from-goal self-play with bootstrapped one-step-lookahead targets**, then using that learned value to guide search (MCTS in DeepCube, weighted A* in DeepCubeA) rather than relying on a greedy local heuristic. **Neither system claims the learned heuristic is admissible** — both are explicitly "good enough, fast," not optimality-preserving.

## Problem

How to train an agent to solve a puzzle where the only reward signal is "solved / not solved" at the end (sparse, terminal-only reward, exactly analogous to "word reduced to identity" for B(2,5)) — and specifically how to guide search toward states that are far from a naive local optimum (a scrambled cube looks "no better" by any local metric until deep into a correct solve sequence) using a LEARNED value function rather than a hand-crafted or greedy heuristic.

## Approach

**Training (Approximate/Deep Value Iteration, both papers):** Generate training states by scrambling **backward from the solved goal state** (k random moves × l independent scramble sequences) — critically, this means the "distance to goal" for each generated state is roughly known by construction (its scramble depth), giving a natural curriculum from easy (near-goal) to hard (far-from-goal) built into the data generation itself, not needing a separate curriculum schedule. For each state x, the value-iteration target is a **one-step bootstrapped lookahead**: `target(x) = min_a (cost(a) + v(child_a))` over the state's possible next moves (children), using the CURRENT value network's own estimate of each child's value — this is exactly the "bootstrapping" the team asked about (value estimates trained on other value estimates). Loss is MSE regression on the value prediction (DeepCube's ADI additionally trains a policy head via cross-entropy, sharing the network backbone — an actor-critic setup; DeepCubeA's DAVI is value-only, letting the search itself supply the "policy").

**Stability mechanisms for the bootstrapping loop (directly answers the "pitfalls" ask):**
1. **Target network**, updated only when training loss drops below a threshold (`--loss_thresh`, e.g. 0.1 per the DeepCubeA GitHub README) — the network being trained is NOT the same network supplying the bootstrap targets; targets only refresh once training has genuinely improved, preventing a moving-target feedback loop from diverging.
2. **Curriculum built into data generation** (backward-from-goal scrambling means near-goal, easy-to-value-correctly states are always present in every training batch, not just early in training) — a structurally different curriculum mechanism than the length-window curriculum discussed under R3, but same underlying goal (anchor training on cases the model can get right, throughout training, not just early).
3. **Inverse-scramble-depth sample weighting**, `W(x) = 1/D(x)` (DeepCube specifically) — down-weights deeply-scrambled (hardest, least-reliable-target) states relative to near-goal states. DeepCube's own paper states directly: "We didn't see divergent behavior after this addition" — i.e. this weighting was added specifically because bootstrapping WAS unstable without it, a direct confirmation that the pitfall is real and this is the field's answer to it.

**Search-time combination:** DeepCubeA uses **weighted A***, `f(n) = λ·g(n) + h(n)` with λ ∈ [0,1] (learned value network supplies h). Per the GitHub README: "the weight on the path cost... increasing generally improves results" as λ→1 (closer to true A* / more optimal-seeking), while lower λ is more greedy-best-first (faster, less careful). DeepCube (2018) instead uses MCTS with the learned policy+value guiding node selection/expansion, more AlphaZero-shaped.

## Key result

DeepCube: "solve 100% of randomly scrambled cubes while achieving a median solve length of 30 moves — less than or equal to solvers that employ human domain knowledge," with NO human-provided heuristics or domain knowledge beyond the scrambling/move-set definition. DeepCubeA (per subagent's summary of the Nature MI paper, not independently re-verified against primary text): the weighted-A* + DAVI value combination scales to a much larger state space than the Cube (the paper's headline is that it generalizes the ADI/AVI+search template to the 15-puzzle, Sokoban, and other domains beyond just the Cube).

## Assumptions

A well-defined, invertible move set (children of a state are exactly and only reachable via legal moves) — this maps cleanly onto B(2,5): "moves" = rewrite-rule applications (including enabler moves), "children" of a word = all words reachable by one rule/enabler application. A single, unambiguous goal state (solved cube / identity element) — B(2,5)'s goal (reduce to empty/identity word) is directly analogous. Crucially: **backward-from-goal data generation is only cheap because the move set is invertible/symmetric** (any scramble sequence can be generated by applying moves starting FROM the solved state) — B(2,5) rewrite rules are largely one-directional (shortening), so "generating training data by working backward from the empty word via un-applying rules" is not obviously as cheap or well-defined as it is for a Rubik's Cube move group; this is a genuine adaptation question, not a free port.

## Limitations / scope

Both systems are for a FIXED, exactly-invertible combinatorial puzzle with a single, universally-reachable goal state and no notion of variable-length representation — the entire "state" is always a fixed-size cube configuration, never a variable-length string. This is a structurally different representation regime from B(2,5) words (variable length, growing/shrinking under moves) — the value-network TRAINING PROCEDURE (backward-from-goal + bootstrapped one-step lookahead + target network + curriculum-via-data-generation) is the transferable idea; the fixed-state-size architecture is not directly portable and would need adaptation for variable-length words. Neither paper claims or proves admissibility of the learned heuristic — see [[futuhi-sturtevant-2026-admissible-heuristics]] for the direct follow-up critique of exactly this gap.

## Replication evidence

DeepCubeA's own Nature MI paper (per subagent summary) reports generalizing the same ADI/DAVI+search template beyond the Cube to other puzzle domains (15-puzzle, Sokoban) — internal replication across domains within the same paper. [[chervov-2025-cayleypy-rl]] applies a related (diffusion-distance, not exactly DAVI) value-guided beam search to Cayley graphs of PERMUTATION groups, benchmarked against GAP — the closest published extension of this general paradigm toward actual group theory, though not group-word/free-presentation rewriting specifically.

## Why this paper matters

This is the most directly relevant, most rigorously documented answer available to R1: it is a real, published, reproducible (open-source code) demonstration that a LEARNED value/cost-to-go function, trained via bootstrapped backward-from-goal value iteration and combined with weighted A* or MCTS, solves EXACTLY the "must get worse before better, sparse terminal reward, greedy local heuristic fails" problem class the B25 team is asking about — for a combinatorial structure (Rubik's Cube group) that is a close cousin of a Burnside-group word problem (both are elements of a group acting on itself via a generating move set, with the goal being the identity element). The training-procedure template (bootstrapped one-step lookahead + target network + curriculum-via-backward-generation + inverse-distance sample weighting) is concrete and portable in spirit, though the fixed-size-state architecture requires real adaptation work to apply to variable-length B(2,5) words.

## Quotes

1. > "We introduce Autodidactic Iteration: a novel reinforcement learning algorithm that is able to teach itself how to solve the Rubik's Cube with no human assistance." — DeepCube Abstract
2. > "We didn't see divergent behavior after this addition" — DeepCube, on inverse-scramble-depth sample weighting stabilizing the bootstrapping loop (per subagent extraction)

## Open questions surfaced

Whether a value/cost-to-go head can be trained for B(2,5) words using an analogous backward-from-identity generation scheme, given that B(2,5)'s rewrite rules are mostly one-directional (length-decreasing) rather than freely invertible like Rubik's Cube moves — generating "scrambled" (long, far-from-identity) training words by applying rule RHS→LHS in reverse (i.e. deliberately un-reducing) is a plausible analog, but its cost/coverage properties relative to Rubik's-Cube-style backward scrambling are untested. This is THE concrete next question for Experimenter/Developer if a value-head approach is pursued.

## Related material in vault

- Related: [[chervov-2025-cayleypy-rl]] (closest group-theory extension of value-guided search, permutation groups not free presentations)
- Related: [[futuhi-sturtevant-2026-admissible-heuristics]] (direct critique of the admissibility gap this paper leaves open)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
