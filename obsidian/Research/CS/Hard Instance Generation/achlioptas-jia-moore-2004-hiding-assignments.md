---
title: "Hiding Satisfying Assignments: Two are Better than One"
authors: Dimitris Achlioptas, Haixia Jia, Cristopher Moore
year: 2004
venue: "AAAI 2004 (preliminary version); Journal of Artificial Intelligence Research 24:623–639 (2005)"
url: "https://arxiv.org/abs/cs/0503046"
language: en
domain: cs
status: draft
methodology_type: theoretical
citation_count: 62
citation_count_date: 2026-10-05
key_concepts:
  - "[[Concepts/quiet-planting]]"
  - "[[Concepts/certified-instance-generation]]"
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[krzakala-zdeborova-2009-quiet-planting]]"
  - "[[2606.15979]]"
quality_notes: "Mixed theory and experiment. A first-moment calculation and a differential-equation analysis of Unit Clause are rigorous; hardness for zChaff, Satz, WalkSAT and SP is empirical (25–100 trials per point). arXiv cs/0503046 (submitted 2005-03-20; 'Preliminary version appeared in AAAI 2004'). Semantic Scholar's count (62) is attached to the AAAI 2004 record. Not to be confused with arXiv cs/0503044 (Jia–Moore–Strain, 'Generating Hard Satisfiable Formulas by Hiding Solutions Deceptively', AAAI 2005)."
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

# Hiding Satisfying Assignments: Two are Better than One

## Abstract

The evaluation of incomplete satisfiability solvers depends critically on the availability of hard satisfiable instances. A plausible source of such instances consists of random k-SAT formulas whose clauses are chosen uniformly from among all clauses satisfying some randomly chosen truth assignment A. Unfortunately, instances generated in this manner tend to be relatively easy and can be solved efficiently by practical heuristics. Roughly speaking, as the formula's density increases, for a number of different algorithms, A acts as a stronger and stronger attractor. Motivated by recent results on the geometry of the space of satisfying truth assignments of random k-SAT and NAE-k-SAT formulas, we introduce a simple twist on this basic model, which appears to dramatically increase its hardness. Namely, in addition to forbidding the clauses violated by the hidden assignment A, we also forbid the clauses violated by its complement, so that both A and Ā are satisfying. It appears that under this "symmetrization" the effects of the two attractors largely cancel out, making it much harder for algorithms to find any truth assignment. We give theoretical and experimental evidence supporting this assertion.

## TL;DR

Naive "1-hidden" planted 3-SAT is easy because the hidden assignment pulls solvers towards it, and the pull grows with density. Hiding a **complementary pair** A, Ā ("2-hidden") symmetrises the clause distribution so the two pulls cancel. The paper backs this with a first-moment calculation, an exact Unit-Clause analysis and experiments with four solvers. 2-hidden formulas come out about as hard as unplanted random 3-SAT of the same size and density. It is the classic demonstration that a planted solution can be hidden by a symmetry instead of by sophistication.

## Problem

Incomplete solvers (local search) cannot be benchmarked on random formulas without knowing satisfiability, and filtering with a complete solver "greatly limits the size and difficulty of problem instances that can be considered". The natural generator rejects clauses violated by a hidden A, but it "is highly biased towards formulas with many assignments clustered around A". On those formulas WalkSAT does much better than on filtered random satisfiable formulas (§1). Can a simple, analysable generator produce satisfiable formulas as hard as random ones?

## Approach

- **Generator.** Pick A at random, draw rn random 3-clauses, and reject any clause violated by A *or* by its complement Ā. With A = all-ones this means forbidding all-negative and all-positive clauses, which makes the clause distribution symmetric under global negation. The motivation is NAE-k-SAT, whose solutions form a uniform "mist" rather than clumps (refs [4, 6]) (§1).
- **§2 First moment.** Expected number of solutions as a function of overlap α with the hidden assignment: $f_{k,r}(\alpha)$ for 1-hidden and $g_{k,r}(\alpha)$ for 2-hidden.
- **§3 Unit Clause heuristic** via Wormald's differential-equation method and a two-type branching process for unit-clause propagation.
- **§4 Experiments.** 0-, 1- and 2-hidden formulas with n ≥ 1000, run on zChaff and Satz (complete), WalkSAT (local search) and Survey Propagation.

## Key result

1. **Solution geometry (§2.1).** For 1-hidden formulas, $f_{k,r}(\alpha) = \frac{1}{\alpha^\alpha(1-\alpha)^{1-\alpha}}\left(1-\frac{1-\alpha^k}{2^k-1}\right)^r$ is always maximised at some α > 1/2. "The set of solutions is dominated by truth assignments that can 'feel' the hidden assignments", and this gets worse as r increases.
2. **2-hidden is symmetric (§2.2).** $g_{k,r}(\alpha) = \frac{1}{\alpha^\alpha(1-\alpha)^{1-\alpha}}\left(1-\frac{1-\alpha^k-(1-\alpha)^k}{2^k-2}\right)^r$ is symmetric about α = 1/2. There is a sequence $\epsilon_k \to 0$ such that $g_{k,r}$ has a unique global maximum at α = 1/2 for all $r \le 2^k \ln 2 - \frac{\ln 2}{2} - 1 - \epsilon_k$ (eq. 5). Compare the unsatisfiability bound for random k-SAT, $r \ge 2^k \ln 2 - \frac{\ln 2}{2} - \frac12$ (eq. 6). Table 1 (eq. 5 vs eq. 6): k = 3: 7/2 vs 4.67; k = 4: 35/4 vs 10.23; k = 5: 20.38 vs 21.33; k = 7: 87.23 vs 87.88; k = 10: 708.40 vs 708.94; k = 20: 726816.15 vs 726816.66. "the hidden assignments are 'not felt.'"
3. **Unit Clause (§3).** With symmetric initial clause distributions, the UC differential equations reduce exactly to those for 0-hidden (random) 3-SAT. "UC fails on these formulas at exactly the same density for which it fails on random 3-SAT instances", i.e. it succeeds with constant probability iff r < 8/3. For 1-hidden formulas UC succeeds "up to r < 2.679". The authors conjecture that all myopic DPLL algorithms behave on 2-hidden formulas as on 0-hidden ones.
4. **zChaff (§4.1, Fig. 2).** On 20 < r < 60 with n = 1000–3000, 2-hidden formulas are "almost as difficult as 0-hidden ones", while 1-hidden formulas need "a number of branchings between 2 and 5 orders of magnitude smaller". Each point is the median of 25 trials.
5. **Satz (§4.1).** All three types are within a multiplicative constant. This is because Satz tries branches in a fixed order (false first), which ignores the hidden attractor.
6. **Survey Propagation (§4.2, Fig. 3).** With n = 10⁴, "SP solves 2-hidden formulas at densities somewhat above the threshold, up to r ≈ 4.8, while it solves the 1-hidden formulas at still higher densities, up to r ≈ 5.6."
7. **WalkSAT (§4.3, Fig. 4).** With n = 10⁴ and 10⁸ flips, below the threshold 2-hidden and 0-hidden running times "coincide to within the resolution of the figure", and both are hardest at r ≈ 4.2. 1-hidden formulas peak around r = 5.2 and are much easier. A biased start with 75% agreement with one hidden assignment ("exponentially unlikely") makes 2-hidden formulas about as easy as 1-hidden. At r = 4.25, with n from 100 to 2000, the figure annotates log-log slopes "2.8", "2.7", "1.3" and "1.3". The caption pairs 2-hidden (random start) with 0-hidden, and biased-start 2-hidden with 1-hidden. The slope-to-curve mapping is read off the figure, not stated in the text. The median running time "for all three is polynomial" (Fig. 4 right).
8. **Recommendation (§5).** "random 2-hidden instances could make excellent satisfiable benchmarks, especially just around the satisfiability threshold, say at r = 4.25".

## Assumptions

- Random 3-SAT (k-SAT for §2) with m = rn independent clauses and n → ∞ for the analytical parts.
- The first-moment bound describes where E[X] concentrates, not the typical number of solutions. A second-moment analysis is not done.
- The UC analysis assumes Wormald's theorem applies, with the branching process subcritical throughout.
- The solvers tested are the 2004 state of the art (zChaff, Satz, WalkSAT, SP). Hardness is measured as median branches or flips.

## Limitations / scope

- The hardness claims are empirical. There is no proof that DPLL takes exponential time on 2-hidden formulas; the authors list this as open (§5, item 1).
- The construction is detectable *in principle*: no clause is all-positive or all-negative relative to A. [[2606.15979]] (§1, §3) notes that naive planting is vulnerable to statistical-query algorithms, and the 2-hidden distribution is not shown to be SQ-indistinguishable from uniform. The paper only plants two solutions, and they are complementary. Arbitrary multi-solution geometry is addressed in [[2606.15979]] (Prop. 2 there shows why one sign-pattern distribution cannot plant a second solution at Hamming distance k).
- SP still solves 2-hidden formulas above the satisfiability threshold (up to r ≈ 4.8). Beating SP "requires somewhat higher densities" (§5).

## Replication evidence

Partial. The follow-up by Jia, Moore & Strain, "Generating Hard Satisfiable Formulas by Hiding Solutions Deceptively" (AAAI 2005; arXiv cs/0503044; no vault note), develops the hidden-solution line further. [[krzakala-zdeborova-2009-quiet-planting]] cites this paper (ref [8]) among the planting protocols whose hardness was "still very poor[ly]" understood. It then gives the statistical-physics account of when planting is quiet, but explicitly not for k-SAT. [[2606.15979]] cites it (§7) as the theoretical treatment for "up to two solutions".

## Why this paper matters

This is the canonical example that *how* a solution is planted matters more than *whether* it is planted. 1-hidden formulas leak the planted assignment through a first-order statistic: literal polarity is biased towards A, so the overlap gradient points at A. 2-hidden formulas remove that first-order leak by symmetry, at no cost in simplicity. The paper is also a model of how to argue hardness for a generator: it compares three ensembles (0-, 1- and 2-hidden) on four solvers from different families, and adds analytical results (the first-moment landscape and exact Unit Clause behaviour) that explain *why* the solvers behave as they do.

**Relevance to challenge-gen:** Two lessons carry over directly. First, the evaluation design: every challenge generator should be benchmarked against at least three baselines. These are (i) random words, which are generically non-trivial and correspond to "0-hidden", (ii) naively planted trivial words, e.g. random products of conjugates of relators, the "1-hidden" analogue, and (iii) the candidate generator, each on more than one solver family (e.g. kbmag rewriting, a B₀(2,5) word-problem oracle, a learned reducer). Second, the symmetrisation idea: a naive trivial word built as a product of conjugated relators leaks its construction through statistics such as relator-shaped subwords or a biased letter balance. The analogue of hiding A and Ā is to cancel these first-order signals, for example by mixing constructions whose biases point in opposite directions, so that cheap statistics stay flat.

## Quotes

1. > "under this 'symmetrization' the effects of the two attractors largely cancel out" — Abstract
2. > "UC fails on these formulas at exactly the same density for which it fails on random 3-SAT instances" — §3

## Open questions surfaced

From §5:
1. "Proving that the expected running time of natural Davis-Putnam algorithms on 2-hidden formulas is exponential in n for r above some critical density."
2. "Explaining the different threshold behaviors of SP on 1-hidden and 2-hidden formulas."
3. "Understanding how long WalkSAT takes at the midpoint between the two hidden assignments, before it becomes sufficiently unbalanced to converge to one of them."
4. "Studying random 2-hidden formulas in the dense case where there are ω(n) clauses."

Added for the vault: is the 2-hidden distribution SQ-distinguishable from uniform 3-SAT at the densities tested? Answering this would connect the empirical line here to the formal line in [[2606.15979]].

## Related material

- [[hard-instance-generation-overview]]: parent directory map
- [[_moc-hard-instance-generation]]: MOC, section "Planting a solution without making it easy to find"
- [[_synthesis-hard-instance-generation]]: cross-domain synthesis for challenge-gen
- [[project-challenge-gen]]: project this note serves
- Cited by (in this vault): [[krzakala-zdeborova-2009-quiet-planting]] (ref [8]) and [[2606.15979]] (§7, "up to two solutions")
- [[marques-silva-sakallah-1999-grasp]]: the CDCL lineage behind zChaff, one of the four solvers these instances were tested against
- [[gomes-selman-2001-portfolios]]: heavy-tailed runtimes on hard satisfiable instances, relevant to how the median-of-25 hardness numbers should be read
- Related (no vault note): Jia, Moore & Strain, "Generating Hard Satisfiable Formulas by Hiding Solutions Deceptively", AAAI 2005, arXiv cs/0503044
- [[kapovich-2003-generic-case-complexity]]: the group-theory counterpart; typical instances are easy, so hard instances with a known answer must be constructed
