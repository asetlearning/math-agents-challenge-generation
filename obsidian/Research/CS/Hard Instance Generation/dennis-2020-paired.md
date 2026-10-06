---
title: "Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design"
authors: Michael Dennis, Natasha Jaques, Eugene Vinitsky, Alexandre Bayen, Stuart Russell, Andrew Critch, Sergey Levine
year: 2020
venue: "NeurIPS 2020 (34th Conference on Neural Information Processing Systems)"
url: "https://arxiv.org/abs/2012.02096"
language: en
domain: ai
status: draft
methodology_type: empirical
citation_count: 362
citation_count_date: 2026-10-05
key_concepts:
  - "[[Concepts/certified-instance-generation]]"
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "Introduced the UED framing and the PAIRED algorithm. Semantic Scholar count 362. Experiments use five seeds per method on MiniGrid-based navigation (ref [9], gym-minigrid) plus one MuJoCo hopper study. Theorems 1–2 are game-theoretic characterisations of the equilibrium; there is no convergence guarantee ('multi-agent learning may not always converge', §4). Code: google-research/social_rl."
author: asetlearning
tags:
  - agent/research
  - user/asetlearning
  - domain/ai
  - topic/curriculum-learning
  - topic/reinforcement-learning
  - topic/hard-instance-generation
  - paper
  - status/draft
  - project/challenge-gen
project: challenge-gen
---

# Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design

## Abstract

A wide range of reinforcement learning (RL) problems — including robustness, transfer learning, unsupervised RL, and emergent complexity — require specifying a distribution of tasks or environments in which a policy will be trained. However, creating a useful distribution of environments is error prone, and takes a significant amount of developer time and effort. We propose Unsupervised Environment Design (UED) as an alternative paradigm, where developers provide environments with unknown parameters, and these parameters are used to automatically produce a distribution over valid, solvable environments. Existing approaches to automatically generating environments suffer from common failure modes: domain randomization cannot generate structure or adapt the difficulty of the environment to the agent's learning progress, and minimax adversarial training leads to worst-case environments that are often unsolvable. To generate structured, solvable environments for our protagonist agent, we introduce a second, antagonist agent that is allied with the environment-generating adversary. The adversary is motivated to generate environments which maximize regret, defined as the difference between the protagonist and antagonist agent's return. We call our technique Protagonist Antagonist Induced Regret Environment Design (PAIRED). Our experiments demonstrate that PAIRED produces a natural curriculum of increasingly complex environments, and PAIRED agents achieve higher zero-shot transfer performance when tested in highly novel environments.

## TL;DR

PAIRED trains a learned instance generator (the "adversary") to maximise **regret**: the antagonist's return minus the protagonist's return. Uniform random generation (domain randomization) gives no structure. Pure minimax generation produces unsolvable instances. Regret rewards instances that *some* agent can solve but the learner cannot, so solvability is enforced by an empirical witness and difficulty tracks the learner's frontier. On maze navigation this yields an emergent curriculum and much better zero-shot transfer to human-designed mazes.

## Problem

Designing training-task distributions by hand is error-prone. The two automatic alternatives fail in opposite directions. Uniform sampling "will often fail to generate interesting structures". A minimax adversary "is incentivized to make the environments completely unsolvable, generating mazes with unreachable goals" (§1). The paper formalises **Unsupervised Environment Design (UED)**: given an underspecified environment (a UPOMDP with free parameters Θ) and a policy, produce a distribution over fully specified environments that supports the policy's continued learning (§3).

## Approach

- **UED formalism (§3).** An environment policy Λ : Π → Δ(Θ^T). Domain randomization corresponds to Laplace's "insufficient reason", minimax adversarial training to Wald's "maximin", and PAIRED to Savage's "minimax regret" (Table 2, §2).
- **Regret estimate (§4, eq. 1).** $\mathrm{REGRET}^{\vec\theta}(\pi^P, \pi^A) = U^{\vec\theta}(\pi^A) - U^{\vec\theta}(\pi^P)$. In practice they use $\max_{\tau^A} U(\tau^A) - \mathbb{E}_{\tau^P}[U(\tau^P)]$ over several trajectories per environment to reduce noise.
- **Algorithm 1.** Three RL agents. The adversary generates θ. The protagonist is trained on −REGRET. The antagonist and the adversary are trained on +REGRET. All use PPO. Navigation policies are RNNs because the environments are partially observable.
- **Environments (§5).** A 2D grid navigation task where the adversary places the agent (t = 0), the goal (t = 1) and then obstacles one per step. Plus a MuJoCo hopper where the adversary applies joint torques.
- **Baselines.** Domain randomization (DR), minimax (antagonist removed), and population-based minimax ("our closest approximation of POET").

## Key result

1. **Theorem 1 (§3).** If rewards split into SUCCESS and FAILURE classes, separated by more than their internal ranges, and some policy succeeds on every θ where success is possible, then "minimax regret will choose a policy which has that property". DR and minimax lack this property (Appendix).
2. **Theorem 2 (§4).** At a Nash equilibrium where antagonist and adversary jointly best-respond, "the protagonist learns the minimax regret policy": $\pi^P \in \arg\min_{\pi^P}\{\arg\max_{\pi^A,\vec\theta}\{\mathrm{REGRET}^{\vec\theta}(\pi^P,\pi^A)\}\}$.
3. **Easiest-unsolved-task incentive (§4).** If the reward has an efficiency bonus, "the adversary gets the most regret for proposing the easiest task which is outside the protagonist's skill range", i.e. the "zone of proximal development".
4. **Emergent complexity (§5.1, Fig. 2, five seeds, 95% CI).** "PAIRED is the only method that continues to increase the passable path length to create more challenging mazes … producing agents that solve more complex mazes than the other techniques". DR and minimax (including PBT) stay flat on solved path length.
5. **Zero-shot transfer (§5.1, Fig. 3, 10 trials × 5 seeds).** "In the Labyrinth (Maze) environment, PAIRED agents are able to solve the task in 40% (18%) of trials. In contrast, minimax agents solve 10% (0.0%) of trials, and DR agents solve 0.0%."
6. **Continuous control (§5.2, Fig. 4).** After the minimax adversary's torque cap is lifted (it is ramped from 0.1 to 1.0 over 300 iterations), "the agent's reward is driven to zero". "PAIRED is able to automatically adjust the difficulty of the adversary to ensure the task remains solvable."

## Assumptions

- A parameterised generator space Θ (the UPOMDP) that the adversary can act on step by step.
- The antagonist is a good-enough proxy for the optimal policy. The regret estimate is only as good as the antagonist.
- Rewards admit a success/failure separation for Theorem 1 to bite.
- Small-scale environments: 2D grids and a single MuJoCo task.

## Limitations / scope

- No convergence guarantee for the three-player training; Theorem 2 is an equilibrium characterisation only.
- "Solvable" is an empirical claim, witnessed by the antagonist's success, not a proof. If the antagonist and protagonist are both weak, regret is ≈ 0 and the signal vanishes. Appendix E.1 explores regret approximations that break the coordination assumption.
- Only 5 seeds, and only gridworld and hopper domains. No discrete-math or proof-search domains.
- No notion of *verifiable* solutions. A navigation episode is checked by the simulator, which is cheap here but not in general.

## Replication evidence

Partial: the code is public (google-research/social_rl). This vault does not track the later UED literature that builds on PAIRED (e.g. regret-based level replay methods). No independent replication has been checked here.

## Why this paper matters

PAIRED is the reference point for learned, adversarial instance generators that stay *solvable*. Its central move is to replace "hard for the learner", which degenerates into unsolvable instances, with "hard for the learner *but solved by someone*". The regret objective then produces a curriculum that keeps moving with the learner's frontier. It sits with [[agarwal-2021-polynomial-simplification-curriculum]] (curricula for math RL) and [[sato-2019-hisampler]] (learned hard-instance samplers) as the ML side of hard-instance generation, complementing the planted-ensemble side ([[krzakala-zdeborova-2009-quiet-planting]]).

**Relevance to challenge-gen:** PAIRED's antagonist is an empirical solvability witness. In challenge-gen, solvability is instead guaranteed by construction through a certificate, so the regret idea maps onto a *hardness* metric: generate trivial words or AC presentations on which a reference solver (the "antagonist", e.g. kbmag or a strong search baseline) succeeds and the learner fails. That targets the learner's frontier rather than generic or unsolvable instances. One caveat is essential: the antagonist must be a fair solver. If it is handed the generation trace or certificate, it trivially wins and regret collapses to plain minimax over the learner. A second caveat: regret selects the *easiest* task the learner fails, which is a curriculum signal, not a benchmark of hard instances.

## Quotes

1. > "minimax adversarial training leads to worst-case environments that are often unsolvable" — Abstract
2. > "the adversary gets the most regret for proposing the easiest task which is outside the protagonist's skill range" — §4

## Open questions surfaced

- How to estimate regret when no strong antagonist exists, i.e. when the reference solver is itself the bottleneck, as in open math search problems.
- Whether regret-driven generation transfers to discrete combinatorial domains with exact verifiers, such as SAT, trivial words or AC moves. This is not tested in the paper.
- Convergence and stability of the three-player game (§4).

## Related material

- [[hard-instance-generation-overview]]: parent directory map
- [[_moc-hard-instance-generation]]: MOC, section "Learned and adversarial instance generators"
- [[_synthesis-hard-instance-generation]]: cross-domain synthesis for challenge-gen
- [[project-challenge-gen]]: project this note serves
- [[sato-2019-hisampler]]: sibling learned hard-instance sampler for graph algorithms
- [[agarwal-2021-polynomial-simplification-curriculum]]: curriculum design for RL on a symbolic math task
- [[_synthesis-rl-for-math]]: RL for math, where PAIRED-style task generation would feed training
- [[shehper-2024-ac-hardness]]: RL on Andrews–Curtis with a hardness measure; the domain where a regret-driven generator would most directly apply in challenge-gen's later phase
