---
title: "Synthesis — beating beam-search B(2,5) reduction: KB ordering/rule levers + NN-guided detour search (focused, 2026-07-21)"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/knuth-bendix
  - topic/rewriting-systems
  - topic/reinforcement-learning
  - topic/b25
  - synthesis
  - project/b25
  - status/draft
papers_synthesized:
  - "[[tate-2011-equality-saturation]]"
  - "[[shypula-2021-superoptimize-real-world-programs]]"
key_concepts: []
date_range: 2009-01 to 2025-05
project: b25
---

# Synthesis — beating beam-search B(2,5) reduction

> **Focused dig, not a broad survey**, per Lead's ask. Builds on the two prior rounds already on record ([[_synthesis-b25-patternboost-tokenization]], [[Research/AI in Math/ML/_synthesis-b25-value-scoring-curriculum-auxchannel]]) — does not repeat DeepCubeA/Segler/CayleyPy in depth. Two questions: (1) does ordering/rule-biasing choice affect achievable reduction LENGTH, and why does a non-confluent overcomplete rule set (~7M rules) out-reduce a minimal one; (2) how do learned systems find detour-requiring reduction paths that beat a strong classical search, concretely.

## Q1 — KB ordering & rule biasing for shorter reductions

**Direct hit on "does ordering choice affect achievable reduction length": thin, essentially open.** No source found in either agent's pass discusses reduction-ORDERING choice as a lever for minimizing final word length specifically (as opposed to confluence/termination, which is what the classical literature — Dershowitz-Jouannaud, Sims — actually optimizes for). One concrete, tool-verified data point exists: the MAF manual (an automatic-groups tool, KBMAG-adjacent) reports that RPO-family ("recursive"/"rt_recursive") orderings "usually give the smallest minimal confluent rewriting system... of any of the supported word-orderings" — on one example group, shortlex produced 8225 equations vs. 94 under recursive ordering. This is a rule-COUNT effect, not a reduced-word-LENGTH effect, but it's a real, verified mechanism for why RPO-based cascades in the team's own experiments behave differently from shortlex ones (smaller confluent bases, likely different critical-pair generation dynamics). **Evidence strength: empirical, tool-documented, but answers an adjacent question, not the one asked.** Sims (1994) — the standard textbook reference most likely to address this directly — was not web-accessible and remains genuinely unread; flagged rather than guessed at.

**The real answer to "why does an overcomplete/non-confluent 7M-rule system reduce further than a minimal confluent one" — found, and it's a clean mechanism, not a curiosity.**

1. **ATP theory confirms the mechanism directly, current and rigorous.** Hajdu, Kovács, Voronkov, "Partial Redundancy in Saturation" (arXiv:2505.22213, 2025): standard redundancy-elimination in superposition calculus (the ATP analog of "keep only the confluent/minimal rule set") can be **too aggressive** — deleting clauses judged redundant by the standard criterion sometimes destroys the only path to a needed result. Their more permissive PaRC calculus, proven refutationally complete and implemented in Vampire, **solved 24 previously-unsolved TPTP benchmark problems** by keeping clauses a stricter system would have thrown away. This is a direct, theorem-plus-implementation-plus-benchmark validation of the team's own empirical finding: pruning to "just the confluent/necessary" rules is not free — it can foreclose reachability of a specific target that a looser, larger rule set would have found.

2. **Equality saturation / e-graphs give this a first-principles explanation, and a concrete engineering lever.** [[tate-2011-equality-saturation]] (Tate, Stepp, Tatlock, Lerner 2009/2011; modern implementation: `egg`, Willsey et al. PLDI 2021): instead of committing to ONE rewrite path (which requires confluence to guarantee you land on the best normal form regardless of rule-application order — the classical KB framing), an **e-graph** maintains a congruence over EVERY equivalent form discovered so far via union-find/hashcons; rewrites only ever ADD equalities, nothing is destructively replaced. You saturate (or run to a budget), then run a **separate extraction pass with an explicit cost function** (shortest length, for us) over everything the e-graph has proven equivalent. This structurally "obviates the need to worry about optimization ordering" — confluence stops being a requirement at all, because nothing is ever committed to a single path. **This reframes the team's 7M-rule observation from an empirical curiosity into an expected consequence**: a non-confluent, over-complete rule set loses nothing under this framing, because more rules can only ever add reachable equivalent forms, never remove options — which is exactly backwards from how the classical "minimal confluent system" framing treats extra rules (as redundant clutter to eliminate).

**Practical levers, ranked by directness:**
- **(Recommended first try) Build a small, budget-bounded e-graph-style saturation layer** over a windowed sub-word + a curated rule subset (not the full 7M at once — e-graph size explosion is `egg`'s own documented central engineering challenge, flagged honestly, not glossed over), extract-by-length, and compare against beam search on the identical sub-problem. This directly tests whether the "more rules, no confluence needed" mechanism generalizes to B(2,5), with a cheap, scoped pilot rather than a full production port.
- **Second lever**: treat RPO/wtlex-vs-shortlex choice as a rule-BASIS-SIZE lever (smaller confluent bases per the MAF finding), not a reduction-length lever directly — worth testing whether a smaller RPO-derived basis, injected alongside the existing shortlex rules (the team's own "Mixer" cross-ordering-sharing approach), changes cascade dynamics, but this is a weaker, more indirect bet than the e-graph lever.
- **Third, lowest-confidence lever**: rule-selection/prioritization heuristics from ATP given-clause algorithms (E-prover, DISCOUNT) — literature here addresses proof-search EFFICIENCY, not output-length quality, so this is the least directly transferable of the three.

## Q2 — NN-guided rewriting past local minima: what actually beat a classical baseline

**Confirmed, directly: dedicated neural-KB / RL-term-rewriting-rule-selection literature is empty** (zero arXiv hits across multiple query variants) — this specific niche remains genuinely unoccupied in the published literature, consistent with what Deep Round 1/2 already found for group-theory-specific ML.

**The concrete, decision-grade result — program superoptimization, not puzzles or chemistry.** [[shypula-2021-superoptimize-real-world-programs]] (Shypula et al. 2021, Best Paper ICLR'22 DL4Code workshop): superoptimization is STOKE-style stochastic search over program edits that **explicitly allows locally-worse intermediate programs** — the same "must get worse before better" structure as B(2,5) reduction, but for real x86-64 assembly rather than a puzzle or a chemistry reaction tree. Trained via **SILO (Self-Imitation Learning for Optimization)**, beating both a standard policy-gradient baseline and a compiler-pretrained baseline by **over 5×** (5.9% success rate vs. under ~1.2%) on 25,000+ real-world functions against GCC -O3. This is the single strongest quantified "neural approach beat a strong classical baseline by X% via architecture W trained via V" result found across all three rounds of this literature scan for a detour-requiring task.

**Why this is a materially different, and likely LOWER-RISK, recipe than the value-head path from Deep Round 2/3**: SILO's job is not to bootstrap a cost-to-go value function from scratch and use it to guide search (DeepCubeA's harder path, which Deep Round 2/3 flagged as carrying real bias-entrenchment risk per Validator's finding and Skalse et al.'s formal reward-hacking results). Instead, it **self-imitates the model's own best-found trajectories** from an existing detour-capable stochastic search (inherited from the earlier, smaller-scale [[Bunel et al. 2016, "Learning to Superoptimize Programs," arXiv:1611.01787]]) — i.e., the neural model learns to propose good edits by imitating successful search history, not by learning to SCORE states independently. Mapped onto B(2,5): **train a policy to imitate the team's own best-found beam-search + enabler-move reduction trajectories** (including the ones that needed a temporary length increase to unlock a later big reduction), rather than trying to bootstrap a value function that could inherit the reducer's known blind spots.

**Weaker/more distant analogs found, for completeness (not recommended as a first bet):**
- DragonLi (2024, arXiv:2411.15194): GNN guides split-decisions in word-EQUATION solving (Nielsen transformations) — moderate analog (strings, tree search, splits) but targets string-constraint satisfiability, not Burnside-relator length minimization.
- Equality-saturation-guided-by-MCTS for tensor-IR (Hartmann et al. 2024, arXiv:2410.05534): non-learned MCTS choosing which rewrite to apply inside an e-graph, up to 11% speedup — reinforces the e-graph mechanism from Q1 as a real, current, actively-developed search structure, but has no neural component to port directly.
- HyperTree Proof Search (Lample et al. 2022, arXiv:2205.11491) — AlphaZero-style transformer + tree search on Lean/Metamath tactics (56.5%→65.4%→82.6% via online training). Distant analog: rich tactic language, not pure length-minimizing term rewriting — already known from Deep Round 2, re-confirmed here as the best available AlphaZero-style precedent but not closer than SILO's more structurally on-point result.
- AlphaZero/MuZero applied directly to symbolic/algebraic rewriting (not games/puzzles/chemistry): **zero hits**, confirmed empty.

## Recommended first thing to try

**Two independent, complementary, low-risk-first experiments — not a single combined bet:**

1. **(Search-structure lever, no NN needed for a first cut)** Pilot a budget-bounded e-graph/equality-saturation layer on a windowed B(2,5) sub-word with a curated rule subset, extract-by-length, compare against beam search on the identical sub-problem. This tests the Q1 mechanism cheaply and, if it works, may deliver a better-than-beam-search reducer with NO neural network at all — a genuinely different lever from "add an NN," worth ruling in or out first since it's simpler to build and evaluate.
2. **(NN-guidance lever, lower-risk than a value head)** Train a self-imitation-style policy (SILO-inspired) on the team's own best-found beam-search + enabler-move trajectories, rather than bootstrapping a value function from scratch. This sidesteps the bias-entrenchment risk flagged in Deep Round 2/3 (no learned proxy scoring states independently — the model imitates successful search history, the search itself remains the ground truth) while still being a genuine, published, quantified beat-a-classical-baseline recipe.

Both are cheaper and lower-risk than the DeepCubeA-style bootstrapped value function explored in Deep Round 2/3, and neither requires resolving that path's open questions (backward-from-goal data generation for one-directional rules, ensemble-disagreement infrastructure) before yielding a testable result.

## What's settled / contested / open

**Settled**: overcomplete non-confluent rule sets reducing further than minimal confluent ones has a real, general, first-principles explanation (equality saturation's non-destructive-commit framing; ATP's partial-redundancy result) — this is not a B(2,5)-specific curiosity, it's an instance of a known phenomenon across rewriting/search fields.

**Contested/open**: whether e-graph-style saturation scales to B(2,5)'s actual rule-bank size and word lengths without heavy engineering investment (e-graph explosion is a real, documented risk, not resolved by this literature pass); whether SILO's self-imitation mechanics (not independently verified against primary text this session) actually transfer cleanly from assembly-superoptimization to group-word reduction; whether ordering choice (shortlex/wtlex/RPO) affects reduction LENGTH directly — this remains genuinely unanswered by the accessible literature, Sims (1994) is the most likely source and remains unread.

## Related material in vault

- Prior rounds: [[_synthesis-b25-patternboost-tokenization]] (Phase A, representation), [[Research/AI in Math/ML/_synthesis-b25-value-scoring-curriculum-auxchannel]] (Deep Round 2/3, value scoring)
- New papers this round: [[tate-2011-equality-saturation]], [[shypula-2021-superoptimize-real-world-programs]]
- Cited inline, no dedicated note (single-fact citations): Hajdu, Kovács, Voronkov, "Partial Redundancy in Saturation" (arXiv:2505.22213, 2025); MAF manual (maffsa.sourceforge.net, ordering/rule-count comparison); DragonLi (arXiv:2411.15194, 2024); Hartmann et al., MCTS-guided equality saturation for tensor IR (arXiv:2410.05534, 2024); Bunel et al., "Learning to Superoptimize Programs" (arXiv:1611.01787, 2016)
