---
title: "Learning to Sample Hard Instances for Graph Algorithms"
authors: Ryoma Sato, Makoto Yamada, Hisashi Kashima
year: 2019
venue: "ACML 2019 (PMLR 101:1–16); arXiv:1902.09700 (v2, 3 Oct 2019)"
url: https://arxiv.org/abs/1902.09700
url_translated:
language: en
domain: cs
status: draft
methodology_type: empirical
citation_count: 1
citation_count_date: 2026-10-05
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "Citation count is uncertain. The Semantic Scholar arXiv record (indexed under the v1 title 'Learning to Find Hard Instances of Graph Problems') shows 1 citation on 2026-10-05. The ACML proceedings version is probably indexed separately and could not be queried (API rate-limited), so the true count is likely higher. Code: github.com/joisino/HiSampler. Results are the mean over 5 seeds of the single hardest instance found per run (§5.2), not the mean hardness of the learned distribution."
author: asetlearning
project: challenge-gen
tags:
  - agent/research
  - user/asetlearning
  - domain/cs
  - topic/hard-instance-generation
  - topic/reinforcement-learning
  - topic/average-case-hardness
  - project/challenge-gen
  - paper
  - status/draft
---

# Learning to Sample Hard Instances for Graph Algorithms

## Abstract

"Hard instances, which require a long time for a specific algorithm to solve, help (1) analyze the algorithm for accelerating it and (2) build a good benchmark for evaluating the performance of algorithms. There exist several efforts for automatic generation of hard instances. For example, evolutionary algorithms have been utilized to generate hard instances. However, they generate only finite number of hard instances. The merit of such methods is limited because it is difficult to extract meaningful patterns from small number of instances. We seek for a probabilistic generator of hard instances. Once the generative distribution of hard instances is obtained, we can sample a variety of hard instances to build a benchmark, and we can extract meaningful patterns of hard instances from sampled instances. The existing methods for modeling the hard instance distribution rely on parameters or rules that are found by domain experts; however, they are specific to the problem. Hence, it is challenging to model the distribution for general cases. In this paper, we focus on graph problems. We propose HiSampler, the hard instance sampler, to model the hard instance distribution of graph algorithms. HiSampler makes it possible to obtain the distribution of hard instances without hand-engineered features. To the best of our knowledge, this is the first method to learn the distribution of hard instances using machine learning. Through experiments, we demonstrate that our proposed method can generate instances that are a few to several orders of magnitude harder than the random-based approach in many settings. In particular, our method outperforms rule-based algorithms in the 3-coloring problem."

## TL;DR

HiSampler trains a small MLP that maps Gaussian noise to edge probabilities of an $n$-vertex graph. Its reward is the measured cost (recursive calls, SAT decisions, or seconds) of a *specific* solver on the sampled graph, and it is trained with REINFORCE plus a top-K replay pool. At fixed $n$ and budget $B = 10000$, it finds instances orders of magnitude harder than Erdős–Rényi, a genetic algorithm, and hand-designed generators. The best case is DSATUR 3-colouring: 610,024,238.8 recursive calls versus 407.0 for the best Erdős–Rényi. The hardness is solver-relative, and instances come with no known answer or certificate.

## Problem

Generic random graphs are easy: "worst time complexity is often far worse than average time complexity" (§1). Evolutionary search finds individual hard instances, not a distribution. Rule-based generators need problem-specific expertise. The goal is a problem-agnostic, sample-efficient *distribution* $\mathcal D_L$ maximising $\mathbb E_{A \sim \mathcal D_L}[\text{hardness}(A, L)]$ for a given algorithm $L$ (§2.1).

## Approach

- **Model** (§2.2): a fully connected net $N_\theta$ with $z \sim \mathcal N(0, I_{d_0})$ as input, outputting $P \in [0,1]^{n(n-1)/2}$; then $A \sim \text{Bernoulli}(P)$. Edges are conditionally independent given $P$ but correlated through $z$.
- **Training** (§2.2): immediate RL with REINFORCE, with reward $r = \text{hardness}(A, L)$ obtained by running the solver.
- **HiSampler-PER**: keeps a pool of the top-K hardest instances seen and trains on a uniform sample from it. This addresses the observation that "hard instances are sparse in the instance space" (§2.2).
- **Key assumptions** (§2.1): *Assumption 1 (Small instance)*: fix $n$, "because we can generate arbitrarily hard instances just by increasing the number of vertices". *Assumption 2 (Sample efficiency)*: a budget of $B$ hardness evaluations.
- **Initialisation** (§5.2): pick the hardest Erdős–Rényi density $p^*$ by a cheap scan, and set the output bias to $b = -\log(1/p^* - 1)$. The authors say this is "the most important step".
- **Extensions** (§3): hardness can be any measurable score, such as approximation ratio $L(A)/OPT(A)$ or the delay of enumeration algorithms.
- **Setup** (§5): three layers ($d_0=10, d_1=100, d_2=500$); Adam with lr 0.0001; $K = 10$; CPU only.

## Key result

**Table 3** (§5.2), hardest instance found, mean of 5 runs, $B = 10000$:

| Problem / algorithm | n | p* | HiSampler-vanilla | HiSampler-PER | Genetic | ER p=p* | best rule-based |
|---|---|---|---|---|---|---|---|
| 3-col / DSATUR (calls) | 50 | 0.1 | 261331027.8 | 610024238.8 | 2464.8 | 407.0 | 240867.8 (Vlasie 1995) |
| 3-col / MiniSat (decisions) | 200 | 0.025 | 1120.4 | 2674.2 | 660.8 | 693.6 | 875.4 (Mizuno–Nishihara 2008) |
| Vertex cover / B&B (calls) | 50 | 0.1 | 8145.2 | 21376.4 | 8127.6 | 3259.2 | N/A |
| Clique / BK (calls) | 32 | 0.9 | 65460.4 | 110591.0 | 25019.6 | 6380.8 | N/A |
| Clique / MCS (10⁻² s) | 150 | 0.9 | 573.4 | 1877.0 | 1117.4 | 276.2 | N/A |
| Clique / FMC (10⁻⁶ s) | 32 | 0.9 | 6119052.0 | 5682186.0 | 2588840.0 | 58655.6 | N/A |
| Isomorphism / Nauty (10⁻⁶ s) | 50 | 0.9 | 604.0 | 786.0 | 57.6 | 10.2 | 230.0 (R(B(Gn,σ)) 2017) |

**Diversity** (§5.4): for DSATUR, the hardest instance found has hardness 1637666819. Of 1000 samples with edge-Jaccard < 0.7 to it, the mean hardness is 3943028.974 (mean Jaccard 0.646), and the hardest has 819309215 (Jaccard 0.694).

**Knowledge extraction** (§5.3, Fig. 3): a sampled 3-colouring instance on which "DSATUR takes more than one billion recursive calls" is *uncolourable* because of a 4-clique. The clique is attached to the rest of the graph by a degree-2 path, which DSATUR colours last. The resulting preprocessing fix is to delete vertices of degree ≤ 2. gSpan frequent-subgraph mining over 1000 samples recovers the 4-clique and the clique-plus-path motif (support ≥ 959, §5.6).

**Approximation ratio** (§5.5): for greedy vertex cover at $n = 50$, "None of the uniformly random graph models found an instance A that satisfies L(A)/OPT(A) = 2. However, all five HiSampler models succeeded".

## Assumptions

- Hardness is defined *for a specific algorithm* (footnote 1, §1), and measured by actually running it (calls, decisions or wall time).
- Instances are small, fixed-size, simple undirected graphs represented by adjacency matrices. Isomorphism is ignored (§6).
- Good initialisation needs a pre-scan for the hard edge density $p^*$ (§5.2).
- Each reward requires a full solver run. That is why the budget is $B = 10000$ and why runs are stopped "when it takes more than a day".

## Limitations / scope

- Reported numbers are the **hardest single instance** per run, not the distribution's mean (§5.2). Diversity is checked only for DSATUR (§5.4).
- Hardness may not transfer across solvers. The paper trains one sampler per algorithm and does not test cross-solver transfer.
- No ground truth is attached: instances may be satisfiable or not, and the answer is whatever the solver eventually returns. No planted solution, no certificate.
- Graph symmetry is not modelled (§6). The output layer is $O(n^2)$, and experiments use $n \le 200$.
- Researcher's note: the wall-time rewards (MCS, FMC, Nauty) are noisy, and the FMC column is the one case where vanilla beats PER.

## Replication evidence

No independent replication found in the vault. Code is public (github.com/joisino/HiSampler). The paper is an early instance of the learned/adversarial instance-generation line that [[dennis-2020-paired]] continues in RL environment design.

## Why this paper matters

HiSampler states the generative version of the hard-instance problem: learn a *distribution* concentrated on instances that a given solver finds hard, using only black-box hardness feedback. It shows that RL with a top-K replay pool finds that rare region far more efficiently than random or genetic baselines. It also shows that hard instances are interpretable: the 4-clique-behind-a-bottleneck motif is exactly the kind of structure frequent-pattern mining recovers.

The method is solver-relative by design. The paper defines a hard instance as one that takes a long time "for a specific algorithm" (footnote 1). That is a strength for stress-testing a given solver and a weakness for building benchmarks meant to outlast it.

**Relevance to challenge-gen:** HiSampler is the template for the "learned adversarial generator" half of challenge-gen. It shows that black-box RL with solver cost as reward, plus replay of the top-K hardest instances, beats random sampling by orders of magnitude at fixed size (Assumption 1 matches the project's "hard at fixed length" requirement). But its instances carry no known answer. The showcase DSATUR instance is uncolourable, and its short proof of that (the 4-clique) is exactly what the solver missed. Challenge-gen would have to keep certificates by restricting the generator's action space to certified moves, e.g. relator insertions and conjugations as in [[elder-2015-random-trivial-words]]. It would also have to guard against overfitting to one solver by rewarding hardness across a portfolio.

## Quotes

1. > "hard instances are sparse in the instance space" — §2.2
2. > "we can generate arbitrarily hard instances just by increasing the number of vertices" — §2.1

## Open questions surfaced

- Do HiSampler instances stay hard for solvers other than the training target? No cross-solver evaluation is reported.
- Can the same REINFORCE/PER loop drive a generator whose actions are *certified* moves (relator insertion, conjugation, AC-moves), so every sample keeps its proof? This is the challenge-gen adaptation.
- What is the hardness distribution of the learned sampler, as opposed to the hardest sample? Only §5.4 gives a mean (3943028.974 for DSATUR).
- Can sequence-valued instances (words, presentations) be handled with an autoregressive policy instead of a Bernoulli adjacency output?

## Related material

- Parent overview: [[hard-instance-generation-overview]]
- MOC: [[_moc-hard-instance-generation]] (listed under "Learned and adversarial instance generators")
- [[dennis-2020-paired]]: adversarial environment design, the RL-curriculum relative of learned hard-instance sampling.
- [[krzakala-zdeborova-2009-quiet-planting]], [[achlioptas-jia-moore-2004-hiding-assignments]], [[2606.15979]]: the complementary approach. Planting gives a *known* answer and studies whether it stays hidden, whereas HiSampler maximises hardness with no known answer.
- [[kapovich-2003-generic-case-complexity]]: the group-theory statement of why uniform random instances are easy, the premise HiSampler shares for graphs.
- [[elder-2015-random-trivial-words]]: a certified-move sampler that could serve as the action space for a HiSampler-style trivial-word generator.
- [[_synthesis-hard-instance-generation]], [[project-challenge-gen]]
- [[_moc-algorithm-cooperation]]: SAT/CDCL solvers (MiniSat appears among HiSampler's targets).

## Related material in vault

- Extends: —
- Contradicts: —
- Replicates: —
- Concepts introduced/used: —
- Cites: — (cites Cheeseman et al. 1991, Achlioptas et al. 2000 (Latin squares), van Hemert 2006, Smith-Miles et al. 2010; none in vault)
- Cited by (in this vault): —
