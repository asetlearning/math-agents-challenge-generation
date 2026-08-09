---
title: "CayleyPy RL: Pathfinding and Reinforcement Learning on Cayley Graphs"
authors:
  - "A. Chervov"
  - "M. Obozov"
  - "A. Soibelman"
  - "et al. (33 authors total)"
year: 2025
venue: "arXiv:2502.18663 (math.CO / cs.LG); v-latest May 2026"
url: "https://arxiv.org/abs/2502.18663"
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
  - "[[gukov-2020-learning-to-unknot]]"
  - "[[petschack-2025-symmetric-group]]"
quality_notes: "The single closest group-theory analog found across all three literature rounds (Phase A, Deep Round 2, Deep Round 3) to 'learn a distance-to-identity heuristic for group elements and use it to guide search.' Directly benchmarked against GAP. Deep Round 3 (2026-07-17) read the methods (§1.1, §2.2, Prop. 2.1) at implementation depth and reached a transfer verdict: the data-generation mechanism transfers cleanly to B(2,5)/B₀(2,5) via the free generators {a,b,A,B} (already invertible by presentation), and the finiteness requirement is satisfied by our actual gated scope (B₀(2,5), order 5^34, not free B(2,5)) — but the distance LABEL does not transfer as-is and should be replaced with our own braid_reduce-based scoring. See § Methods at implementation depth."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/cayley-graphs
  - topic/reinforcement-learning
  - topic/value-network
  - paper
  - status/draft
---

# CayleyPy RL: Pathfinding and Reinforcement Learning on Cayley Graphs

## Abstract

Per subagent extraction (not independently re-verified verbatim by Researcher against primary ar5iv text in this pass): the authors present approaches combining reinforcement learning with a "more direct diffusion distance approach" for pathfinding on massive graphs, particularly Cayley graphs. They benchmark neural network architectures, random walk generators, and beam search methods against the computer algebra system GAP. A key application examines the symmetric group's Cayley graph, providing evidence supporting a conjecture about its diameter and identifying longest elements with desired decompositions.

## TL;DR

Trains a **learned distance heuristic** (via a diffusion-distance-style approach, distinct from DeepCubeA's bootstrapped value iteration) for elements of a group's Cayley graph — i.e., exactly "how far is this group element from the identity, under this generating set" — and uses it to guide **beam search** toward the identity, benchmarked directly against GAP (the standard computer-algebra ground truth) on graphs up to ~10^70 nodes (permutation groups, including Rubik's-cube-type generating sets). This is architecturally the closest published work to "learn a cost-to-go/distance-to-identity function for a group word and use it to guide reduction search" — the exact shape of technique R1 asked about, but for permutation groups, not free/Burnside presentations.

## Problem

How to find short paths (word-length-minimizing routes) from an arbitrary element of a massive group (Cayley graph up to ~10^70 nodes — far too large for brute-force BFS) back to the identity, using a learned distance heuristic to guide beam search, validated against exact ground truth (GAP) on tractable cases.

## Approach

Combines a learned neural distance/value estimator (diffusion-distance framing — likely related to graph diffusion/heat-kernel distance approximations, though the exact training procedure was not extracted at implementation depth by the research subagent in this pass) with **beam search** (not A* or MCTS) to find short generator-sequences back to the identity. Compares multiple neural architectures and random-walk-based training data generators. Validates against GAP's exact computations where GAP remains tractable, and extrapolates to graphs far beyond GAP's reach for the paper's headline results (diameter conjecture evidence, longest-element identification).

## Key result

Per subagent extraction: provides "evidence supporting a conjecture about [the symmetric group's Cayley graph] diameter and identif[ies] longest elements with desired decompositions" — i.e. the learned-heuristic-guided beam search produces genuinely new mathematical evidence (longer/harder cases than GAP can directly verify), validated by cross-checking against GAP wherever GAP remains tractable. This is itself a PatternBoost-adjacent result: a learned heuristic extending computational reach beyond what exact methods (GAP) can directly compute, exactly the role a B(2,5) value head is being considered for.

## Assumptions

The group is a **permutation group** with a Cayley graph defined by a fixed, invertible generating set (transpositions, cyclic shifts, Rubik's-cube-type moves) — every generator has a well-defined inverse generator in the same generating set, making "distance to identity" a well-posed, symmetric graph-distance question. Beam search (not A*) is the search algorithm — no admissibility framing is invoked (beam search doesn't have A*'s optimality-guarantee machinery to begin with, so this sidesteps rather than resolves the admissibility question [[futuhi-sturtevant-2026-admissible-heuristics]] raises for A*-based systems).

## Limitations / scope

**This is the critical scope gap to flag plainly**: B(2,5) is a free/Burnside PRESENTATION problem, not a permutation group with a fixed invertible generating set in the CayleyPy sense. B(2,5) word "moves" (rewrite-rule applications) are mostly one-directional (length-decreasing), and the object being searched over (variable-length strings) is a different structure from a permutation group's fixed-size Cayley graph nodes. The diffusion-distance training methodology was not extracted at implementation depth in this pass (abstract/summary level only) — a closer read of the full paper is needed before treating this as a ready-made recipe rather than a promising analog.

## Replication evidence

Cross-validated against GAP within the paper's own methodology (exact ground truth wherever tractable) — this is itself a strong internal replication/verification practice, directly relevant to this vault's own discipline of preferring GAP-verified claims (see project memory on B(2,5) reduction verification standards).

## Why this paper matters

This is the strongest existing precedent for "yes, learning a distance-to-identity heuristic for group elements and using it to guide search toward the identity is a real, working, GAP-validated technique" — directly on-point for the conceptual shape of what a B(2,5) value head would need to do. It is NOT a ready-made recipe (permutation groups vs. free presentations is a genuine structural gap, and the training procedure needs a closer read), but it substantially de-risks the general approach: this is not speculative territory, it has been done successfully for a structurally adjacent class of group-theoretic search problems, with the same "validate against exact computation, extend beyond it" methodology this vault already values.

## Open questions surfaced

1. ~~Does CayleyPy's diffusion-distance training methodology require the generating-set invertibility that permutation groups have~~ — **ANSWERED, Deep Round 3 (2026-07-17), full methods read.** See § Methods at implementation depth (below) for the transfer verdict.
2. Would beam search (CayleyPy's choice) or weighted A* (DeepCubeA's choice) be the better search-time pairing for a learned B(2,5) value function, given B(2,5) doesn't have (and may not need) an admissibility guarantee either way? Still open.
3. ~~Should Experimenter/Math-expert read this paper's full methods section before Developer scopes any value-head implementation work~~ — done this round; see below.

## Methods at implementation depth (Deep Round 3, 2026-07-17, ar5iv full text §1.1, §2.2, Prop. 2.1)

**Training-pair generation (§2.2):** **Forward** random walks starting AT the identity/target `e` (not backward from a solved goal the way DeepCubeA scrambles) — "Generate N random walk trajectories starting from the selected node e. Each random walk trajectory consists of up to K_max steps... If a random walk visits node s for the first time at step k, we store the pair (s,k) in our training set." Because the generating set is symmetric (see next point), a forward walk from identity is the functional equivalent of DeepCubeA's backward-from-goal scrambling — either direction generates "states with a known upper bound on true distance from the goal."

**Distance label (§2.2):** The label is **the first-visit step number during the random walk**, treated as an approximate "diffusion distance" — explicitly NOT a BFS-verified exact geodesic in general (BFS/GAP verification is used only as a small-scale sanity check, not as the training label at scale). This is an important, honest limitation of their own method: the label is an *upper bound* on true distance (a walk of length k reaches a state that MIGHT be reachable in fewer than k steps via a different path), not ground truth — the network is trained to approximate this upper-bound statistic, not the true geodesic distance.

**Invertibility requirement (§1.1):** Confirmed explicit: "We choose a set of generators a₁^±1,…,a_k^±1 ∈ S_n" — the generating set is symmetric BY CONSTRUCTION (every generator's inverse is also a generator). This is what makes "walk forward from identity, treat walk-length as a distance proxy" a coherent procedure at all: without symmetric generators, a random walk from identity might not be able to reach some states, or might reach them by paths of very different character than the "true" shortest path back.

**Finiteness (§1, Prop. 2.1):** The paper explicitly targets **finite** Cayley graphs (their empirical scale: up to ~10^70 nodes, still finite), and their theoretical convergence result (Proposition 2.1, a Bellman-equation fixed-point argument) is stated "for any finite connected graph G."

### The transfer verdict

**Neither pure (a) "doesn't transfer" nor pure (b) "direct template" — the correct answer is a THIRD option: the mechanism transfers cleanly to B(2,5)/B₀(2,5), but not via the rewrite rule bank.**

1. **The invertibility requirement is about the group's GENERATING SET, not the rewrite RULE BANK.** B(2,5)'s rule bank (31 junction rules, mostly length-decreasing) is the wrong thing to compare against CayleyPy's `a_i^{±1}` — the right comparison is B(2,5)'s actual generators, `{a, b, A, B}`, where `A = a⁻¹` and `B = b⁻¹` **are already inverse pairs by definition of the presentation itself**. A CayleyPy-style forward random walk in `{a,b,A,B}` starting from the empty word is directly available, requires no new infrastructure, and is in fact **already exactly how part of the existing corpus is built** — the "rand_walk" category in the B25 Experimenter's 12k held-out pool ([[axplorer-representation-grounding-2026-07-17]], Task 4b) is precisely a non-backtracking random walk over this alphabet. **This is directly transferable, right now, with existing tooling.**
2. **The finiteness requirement is satisfied by our actual gated scope, not by the free group.** Per the verdict doc, this whole gate's scope is explicitly `B₀(2,5)` (the restricted, FINITE Burnside quotient, order 5^34) — free B(2,5)'s infiniteness status is OPEN (Kourovka 11.48) and explicitly out of scope. 5^34 ≈ 5.8×10^23 is within the same order-of-magnitude regime CayleyPy already operates in (their headline results reach ~10^70). **The finiteness objection does not bind for our actual current target.**
3. **What does NOT transfer directly: the distance LABEL itself.** CayleyPy's label (raw random-walk step count at first visit) is a good proxy for THEM because their downstream task — find a short sequence of the SAME generators back to identity — is literally what that label measures. Our downstream task's real cost metric is different: "how hard is this word to reduce via the rule bank," which is not the same quantity as raw free-generator word length (free reduction and Burnside relations can make the true reduction-cost far below the raw generator-count). **Directly porting CayleyPy's label would train a value head to predict the wrong thing.** The corrected recipe: generate candidate words via CayleyPy-style random walks in `{a,b,A,B}` (their data-generation mechanism, which transfers), but label each with `len(reduce(word))` from the actual `braid_reduce` reducer — our own fast oracle — instead of raw walk-length. This is arguably a STRONGER label than CayleyPy's own (we have a better proxy for true distance than they do, precisely because we have a fast approximate reducer and they don't have an equivalent for large permutation groups beyond BFS/GAP, which doesn't scale).

**Bottom line for Developer/Math-expert**: CayleyPy is a real, working template for the DATA-GENERATION half of a B(2,5) value head (forward random walks over the invertible free generators, from identity outward) — already partially built via the existing `rand_walk` corpus category — but NOT for the LABEL half, where the existing `braid_reduce`-based scoring (already in place per the verdict's C9 fix) is the better signal to regress against, not CayleyPy's walk-length proxy. This substantially de-risks the value-head proposal: the hardest-seeming part (generating well-distributed training data for a group with mostly one-directional rewrite rules) turns out to have a ready answer once the generating-set/rule-bank distinction is made explicit.

## Related material in vault

- Related: [[agostinelli-2019-deepcubea]] (bootstrapped value iteration + weighted A*, the other main value-guided-search precedent)
- Related: [[gukov-2020-learning-to-unknot]], [[petschack-2025-symmetric-group]] (other group-theory + transformer/RL precedents from Phase A, none of which target distance-to-identity specifically)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
