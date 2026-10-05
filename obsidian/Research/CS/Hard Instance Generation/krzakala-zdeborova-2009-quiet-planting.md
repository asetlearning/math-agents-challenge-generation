---
title: "Hiding Quiet Solutions in Random Constraint Satisfaction Problems"
authors: Florent Krzakala, Lenka Zdeborová
year: 2009
venue: "Physical Review Letters 102, 238701 (2009)"
url: "https://arxiv.org/abs/0901.2130"
language: en
domain: cs
status: draft
methodology_type: theoretical
citation_count: 119
citation_count_date: 2026-10-05
key_concepts:
  - "[[Concepts/quiet-planting]]"
  - "[[Concepts/certified-instance-generation]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[achlioptas-jia-moore-2004-hiding-assignments]]"
cited_by:
  - "[[2606.15979]]"
quality_notes: "Four-page PRL letter; results come from the cavity method (non-rigorous statistical physics), checked numerically on single graphs with N = 10^5. Asymptotic equivalence of planted and random ensembles is rigorously proven only up to c_q < c_c (Achlioptas–Coja-Oghlan 2008, cited as [22]). Citation count from Semantic Scholar."
author: asetlearning
tags:
  - agent/research
  - user/asetlearning
  - domain/cs
  - topic/hard-instance-generation
  - topic/planted-solutions
  - topic/average-case-hardness
  - paper
  - status/draft
  - project/challenge-gen
project: challenge-gen
---

# Hiding Quiet Solutions in Random Constraint Satisfaction Problems

## Abstract

We study constraint satisfaction problems on the so-called planted random ensemble. We show that for a certain class of problems, e.g. graph coloring, many of the properties of the usual random ensemble are quantitatively identical in the planted random ensemble. We study the structural phase transitions, and the easy/hard/easy pattern in the average computational complexity. We also discuss the finite temperature phase diagram, finding a close connection with the liquid/glass/solid phenomenology.

## TL;DR

For CSPs whose belief-propagation fixed point on the purely random ensemble is uniform (graph q-coloring is the canonical case), the *natural* planting (colour vertices at random, then add only edges between different colours) is **quiet**: below a computable density the planted ensemble is indistinguishable from the random one, apart from the planted state itself. The letter locates the hard window for planted q-coloring: from the usual easy/hard transition up to $c_l = (q-1)^2$, where the planted solution becomes a spontaneous attractor for BP. It also says when this does not work. Random k-SAT has a non-uniform BP fixed point, so the method does not apply there.

## Problem

"A major point in evaluating the performance of new algorithms for hard CSPs is to be able to generate difficult instances that are guaranteed to be satisfiable." (intro). Planting is the standard method, but "planting a solution changes the properties of the ensemble", and the planted solution is often easier to find than a random one, which has been proven for high constraint density (refs [10–12]). The question is: for which CSPs, and at which densities, can a solution be hidden without changing the ensemble, and where is the planted ensemble algorithmically hard?

## Approach

- **Planting protocol (q-coloring).** "One assigns a random color with equal probability to each of the N vertices, and then constructs the graph by randomly throwing links between vertices of different colors." The degree distribution stays Poisson with mean c, so planted graphs are locally tree-like like Erdős–Rényi graphs (§ "Hiding without changing").
- **Cavity / BP analysis.** BP equation (1) and entropy (2). The planted ensemble needs q colour-dependent distributions $P_s(\psi)$, eq. (3). Key observation: eq. (3) "is nothing else but the 1RSB equation for the coloring of purely random graphs at m = 1". So the planted ensemble's properties can be read off the known random-ensemble results (Zdeborová–Krzakala 2007, ref [14]).
- **Linear stability of the liquid (uniform) fixed point** $\psi_s = 1/q$. It is stable against perturbations towards the planted configuration for $c < c_l = (q-1)^2$.
- **Numerics.** BP on single graphs initialised randomly vs. in the planted configuration. Whitening to count frozen variables. Walk-COL, BP decimation, BP reinforcement and simulated annealing, run on planted and random 5-coloring instances with N = 10⁵ (Fig. 2).
- **Finite temperature.** Liquid/glass/solid phase diagram, with the planted state acting as a crystal (Fig. 3, eq. (4)).

## Key result

1. **Quiet planting (equivalence of ensembles).** For $c < c_l$, "the properties of the planted ensemble are exactly the same as the properties of the purely random ensemble, up to the existence of the planted state". For $c < c_c$ (the condensation transition), "the purely random and planted ensembles of random graphs are asymptotically equivalent". This is rigorously proven (ref [22]) only up to $c_q < c_c$, with "$c_q$ = 3.83(q=3), $c_q$ = 7.81(q=4) and $c_q \to c_c$ as q → ∞" (footnote [27]).
2. **Phase structure of the planted ensemble** (Fig. 1, 5-coloring). For $c_d < c < c_c$ the planted cluster is one of exponentially many equilibrium clusters. Above $c_c$ "the planted state dominates the total number of solution". Above $c_s$ (the random colourability threshold) all clusters disappear except the planted one. "The values of $c_d$, $c_c$ and $c_s$ given q are identical to those in the purely random ensemble, and are listed in [14]." The numeric values are not printed in the letter's text.
3. **Easy/hard/easy pattern.** Below $c_s$ the easy/hard behaviour is the same in both ensembles: "No difference is visible" for Walk-COL (Fig. 2 inset). The second hard→easy transition sits exactly at the liquid spinodal: "the hard/easy transition coincides with a local instability of the liquid phase at $c_l = (q-1)^2$" (Conclusion). For $c > c_l$, BP converges spontaneously to the planted fixed point and BP decimation solves in linear time. For $c_s < c < c_l$, BP decimation, BP reinforcement, Walk-COL and simulated annealing were "not able to find solutions in polynomial time".
4. **Concrete numbers (5-coloring, N = 10⁵, Fig. 2):** "For c > $c_l$ = 16 BP converges spontaneously to the planted fixed point. For c < 14.04 [17] there are no frozen variables in the planted cluster."
5. **q = 3 is degenerate:** "since $c_d = c_l$ for q = 3, the planted 3-coloring is algorithmically easy for all degrees."
6. **Finite temperature.** The liquid becomes unstable towards the planted (solid) state at the spinodal $T_2 = -1/\log\frac{c-(q-1)^2}{q-1+c}$ (eq. 4), which starts at $c_l$ at T = 0. Slow enough annealing above $c_l$ finds the planted state (Fig. 3 inset, N = 5·10⁵, c = 20).
7. **Scope of the method.** Quiet planting needs "the uniformity of the BP fixed point in the purely random ensemble". It applies to problems without disordered interactions on random regular graphs, to hypergraph bicoloring and to balanced locked problems. "The random satisfiability problem, however, is a canonical example where the fixed point of the BP equation is not uniform and where our results do not apply." (Conclusion)

## Assumptions

- Sparse random ensembles in the thermodynamic limit N → ∞, with Poisson degree distribution and locally tree-like graphs.
- The cavity method with "absence of long range correlations" (replica-symmetric / 1RSB ansatz). The results are physics-level, not theorems, except the part covered by ref [22].
- The CSP has a uniform BP fixed point on the random ensemble, e.g. through colour-permutation symmetry.
- Hardness is judged against specific algorithm families: message passing, local search, annealing.

## Limitations / scope

- Does not cover random k-SAT, which the authors flag explicitly. Quiet planting for k-SAT came later: see [[2606.15979]] for a statistical-query treatment and [[achlioptas-jia-moore-2004-hiding-assignments]] for the earlier heuristic symmetrisation.
- The hardness claims are empirical for the window $c_s < c < c_l$: no algorithm tried succeeded, but there is no lower bound.
- The letter does not address detectability by global/spectral methods beyond BP. Indistinguishability is in the sense of "properties of the ensemble" (phase diagram, entropy), not a formal statistical test.

## Replication evidence

Partial. The equivalence below $c_q$ is rigorously proven by Achlioptas–Coja-Oghlan (2008, ref [22]). The extended companion paper, Zdeborová & Krzakala, "Quiet planting in the locked constraint satisfaction problems" (SIAM J. Discrete Math. 25, 750–770 (2011); arXiv:0902.4185, https://arxiv.org/abs/0902.4185), carries the analysis over to locked CSPs. Its abstract states: "Our main result is the location of the hard region in the planted ensemble. In a part of that hard region instances have with high probability a single satisfying assignment." The k-SAT extension in [[2606.15979]] cites this letter as the theory line for single planted solutions (§7).

## Why this paper matters

This is the reference point for "quiet" planting. It shows that planting does not have to make instances easy. When the planted ensemble is statistically identical to the random one, the planted solution is invisible to any algorithm that only "sees" ensemble properties. The letter also gives a clean physical reason for where hardness ends: once $c > c_l$, the uniform fixed point becomes unstable and the planted state acts as a spontaneous attractor. It also pins down the operating window. Hard planted instances live at densities where a purely random instance would be **unsatisfiable** ($c_s < c < c_l$). So the planted instance is guaranteed solvable while random instances at the same density are not, and the solver cannot tell which case it faces.

The negative result is equally useful. The method depends on a uniform BP fixed point, and k-SAT does not have one. That opened the line of work that [[achlioptas-jia-moore-2004-hiding-assignments]] (symmetrisation, earlier) and [[2606.15979]] (SQ-quiet multi-solution planting) address from different directions.

**Relevance to challenge-gen:** The challenge-gen analogue of the KZ window is a range of word lengths and generation parameters where (a) a naive random word in the generators is almost never trivial in B(2,5), yet (b) the planted trivial word's local statistics match random words: letter and subword frequencies, the distribution of short-prefix images in finite quotients such as B₀(2,5), and the distribution of free reduction. If the planted words are distinguishable on such cheap statistics, a learner can exploit the planting rather than solve the word problem. The KZ test to copy is: does a reference solver (or a local "BP-like" heuristic such as greedy relator cancellation) converge towards the planted structure spontaneously? If it does, the challenge is past its own "$c_l$" and is easy.

## Quotes

1. > "the properties of the planted ensemble are exactly the same as the properties of the purely random ensemble, up to the existence of the planted state" — § "Hiding without changing"
2. > "the hard/easy transition coincides with a local instability of the liquid phase at $c_l = (q-1)^2$" — Conclusion

## Open questions surfaced

- How to plant quietly when the random ensemble's BP fixed point is not uniform. The canonical case is random k-SAT, raised by the authors in the Conclusion and partly answered by [[2606.15979]] under the statistical-query model.
- Rigorous proof of the hard window $c_s < c < c_l$ for any algorithm class (here only empirical).
- Is there a group-theoretic analogue of the "uniform fixed point" condition, i.e. a symmetry of the relator set under which planted trivial words look locally like random words? Open for challenge-gen.

## Related material

- [[hard-instance-generation-overview]]: parent directory map
- [[_moc-hard-instance-generation]]: MOC, sections "Why random instances are easy" and "Planting a solution without making it easy to find"
- [[_synthesis-hard-instance-generation]]: cross-domain synthesis for challenge-gen
- [[project-challenge-gen]]: project this note serves
- Cites: [[achlioptas-jia-moore-2004-hiding-assignments]], ref [8], the JAIR 24, 623 (2005) version
- Cited by (in this vault): [[2606.15979]], which places KZ in the theory line for single planted solutions (§7)
- [[kapovich-2003-generic-case-complexity]]: the group-theory counterpart on why generic instances are easy
- [[elder-2015-random-trivial-words]]: sampling trivial words, the object a quiet planting for challenge-gen would have to imitate
- Companion (no vault note): Zdeborová & Krzakala, "Quiet planting in the locked constraint satisfaction problems", SIAM J. Discrete Math. (2011), arXiv:0902.4185
- [[sato-2019-hisampler]]: learned hard-instance sampling with no planted answer, the complementary approach
