---
title: "Planning chemical syntheses with deep neural networks and symbolic AI"
authors:
  - "Marwin H. S. Segler"
  - "Mike Preuss"
  - "Mark P. Waller"
year: 2018
venue: "Nature 555, 604–610 (2018); open precursor arXiv:1708.04202 ('Towards \"AlphaChem\": Chemical Synthesis Planning with Tree Search and Deep Neural Network Policies')"
url: "https://arxiv.org/abs/1708.04202"
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
  - "[[agostinelli-2019-deepcubea]]"
quality_notes: "IMPORTANT CORRECTION to the premise Experimenter surfaced this paper under: Segler et al.'s system does NOT use a learned value network. It uses classic AlphaGo-style Monte Carlo ROLLOUT evaluation (a fast policy network plays out to a terminal state; the resulting outcome IS the value estimate) — a materially weaker/different technique than DeepCubeA's bootstrapped value-iteration network. This is the single most important finding of this note — flagged prominently so it doesn't get miscited as 'two value-network precedents' when there is really only one (DeepCubeA)."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/monte-carlo-tree-search
  - topic/proof-search
  - paper
  - status/draft
---

# Planning chemical syntheses with deep neural networks and symbolic AI

## Abstract

**Nature 2018 paper — paywalled, abstract not independently re-verified against primary text this session.** The open precursor (arXiv:1708.04202, near-identical method, same lead author group) covers the same 3-network MCTS system; per subagent extraction: "target molecules are recursively transformed into increasingly simpler precursor compounds until a set of readily available starting materials is obtained" (this IS the "must get worse before better" — or rather "must consider many branching decompositions before finding the tractable one" — shape of problem, retrosynthesis being recursive backward search from a complex target toward simple, purchasable starting materials).

## TL;DR

**Correction to the framing this paper was proposed under**: there is no dedicated learned value network here. The system is a 3-network Monte Carlo Tree Search: (1) an expansion policy network proposing candidate retrosynthetic transforms (~300k known reaction-rule templates, ~90ms/call), (2) a much faster/coarser rollout policy (~17k templates, ~10ms/call) used to play out random rollouts to a terminal state, and (3) an in-scope binary feasibility filter. **Node values come from classic AlphaGo-style Monte Carlo rollout outcomes** (reward z=10 if solved, partial credit, −1 if unsolved after simulated rollout to depth cutoff), not from a trained value-regression network evaluating a state directly. Selection uses PUCT: `a_t = argmax_a [Q(s,a)/N(s,a) + c·P(s,a)·√N(parent)/(1+N(s,a))]`, c=3 (per subagent extraction from the open precursor). All three networks are trained **supervised** (negative log-likelihood / binary cross-entropy) on 12.4 million literature reactions — not via self-play or bootstrapped value iteration, unlike [[agostinelli-2019-deepcubea]].

## Problem

Retrosynthesis: given a target molecule, recursively decompose it into simpler precursors until reaching a set of commercially available starting materials — a search problem where the "right" first decomposition choice is often not locally obvious (a chemically valid but unproductive decomposition can look just as good locally as one that leads to a short synthesis route), structurally similar to needing to choose a non-greedy first move in a search tree.

## Approach

Three neural networks operating within a Monte Carlo Tree Search: an expansion policy (proposes candidate retrosynthetic transforms/rules to try at a node), a fast rollout policy (cheaper, used only to complete simulated rollouts to a terminal outcome for value estimation — the AlphaGo-style "simulation" step, not a learned static evaluator), and an in-scope filter (screens candidate precursors for chemical plausibility). All trained via supervised learning on a large literature reaction corpus (12.4M reactions), not self-play/reinforcement learning. Tree search combines expansion-policy-guided node selection (PUCT) with rollout-based value estimation.

## Key result

Per subagent's extraction from available (non-paywalled) sources: "solves almost twice as many molecules and is 30 times faster in comparison to the traditional search method based on extracted rules and hand-coded heuristics." A double-blind study (widely reported, not independently re-verified against primary text this session) found chemists could not reliably distinguish the system's proposed routes from literature-derived routes — the paper's own framing is that computer-generated routes reached rough parity with human/literature routes.

## Assumptions

A large, high-quality corpus of known reactions is available for supervised training of all three networks — this is a fundamentally different data regime from B(2,5), which has no analogous corpus of "known good rewrite-application decisions," only a deterministic reducer that can be RUN to generate outcomes, not a literature of expert-chosen moves to imitate directly.

## Limitations / scope

Because this is rollout-based (not a trained value-regression network), it does NOT directly answer R1's actual question ("how do you train a value-of-word/cost-to-go estimator") — it answers a related but distinct question ("how do you evaluate a search node when you don't have a trained value function: run a fast rollout policy to completion and use the outcome"). This is architecturally simpler than DeepCubeA's approach but requires many rollout simulations per node (expensive) rather than one forward pass through a value network (cheap) — a real cost tradeoff if the B25 team were choosing between these two paradigms. No admissibility framing appears in either paper (MCTS with PUCT does not target A*-style optimality guarantees the way weighted-A* does — a different theoretical framework entirely).

## Replication evidence

Not independently assessed. This system's approach (rollout-based MCTS evaluation via a fast auxiliary policy) is architecturally closer to AlphaGo (2016) than to AlphaGo Zero/DeepCubeA's self-play value-network lineage — worth noting as a genuinely distinct design point in the search-guidance design space, not a minor variant.

## Why this paper matters

The correction this note makes is itself the main value: Experimenter's proposal grouped DeepCubeA and Segler's retrosynthesis system together as "two value-network precedents," but they are architecturally different solutions to the same class of problem (non-greedy, sparse-terminal-reward tree search). DeepCubeA trains a value function via bootstrapped regression (directly portable in spirit to a B(2,5) cost-to-go head). Segler's system evaluates nodes via Monte Carlo rollout using a cheap auxiliary policy (a different, arguably simpler-to-implement-but-more-expensive-per-node alternative — B(2,5)'s deterministic reducer could itself serve as a "rollout policy" of sorts, since running it to a fixed point on a candidate word is exactly a rollout-to-terminal-outcome). Both are legitimate candidate designs, but they are NOT the same technique, and the choice between them (train a value regressor vs. use the existing deterministic reducer as a rollout evaluator inside MCTS/beam search) is itself an open design question this note surfaces rather than resolves.

## Open questions surfaced

Given B(2,5) already HAS a fast deterministic reducer (unlike DeepCubeA/DeepCube, which had no such shortcut and NEEDED a learned value function to avoid brute-force search), is Segler's rollout-evaluation paradigm — using the existing reducer itself as the "fast rollout policy" inside an MCTS/beam search, no learned value network required at all — actually a cheaper, more directly applicable design for B(2,5) than porting DeepCubeA's bootstrapped-value-iteration machinery? This is a genuinely open, high-leverage question this note surfaces for Experimenter/Developer: it may be that B(2,5)'s existing reducer already gives us "for free" what Segler's system had to learn a rollout policy to approximate.

## Related material in vault

- Related: [[agostinelli-2019-deepcubea]] (the actual value-network precedent; contrast this note's rollout-based alternative against it)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
