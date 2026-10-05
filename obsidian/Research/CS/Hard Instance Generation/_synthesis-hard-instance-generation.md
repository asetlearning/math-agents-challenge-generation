---
title: "Generating hard instances with a known solution — synthesis for challenge-gen"
author: asetlearning
language: en
domain: cs
status: draft
tags:
  - agent/research
  - user/asetlearning
  - domain/cs
  - topic/hard-instance-generation
  - topic/planted-solutions
  - topic/average-case-hardness
  - topic/trivial-words
  - topic/andrews-curtis
  - topic/proof-certificates
  - topic/curriculum-learning
  - synthesis
  - project/challenge-gen
  - status/draft
papers_synthesized:
  - "[[kapovich-2003-generic-case-complexity]]"
  - "[[elder-2015-random-trivial-words]]"
  - "[[2607.26241]]"
  - "[[coulon-2018-trivial-elements-criterion]]"
  - "[[miasnikov-1999-ac-genetic]]"
  - "[[shehper-2024-ac-hardness]]"
  - "[[carreras-2026-ac-certificates]]"
  - "[[achlioptas-jia-moore-2004-hiding-assignments]]"
  - "[[krzakala-zdeborova-2009-quiet-planting]]"
  - "[[2606.15979]]"
  - "[[sato-2019-hisampler]]"
  - "[[dennis-2020-paired]]"
key_concepts:
  - "[[Concepts/certified-instance-generation]]"
  - "[[Concepts/quiet-planting]]"
  - "[[Concepts/andrews-curtis-moves]]"
date_range: 1999-01 to 2026-07
project: challenge-gen
---

# Generating hard instances with a known solution — synthesis for challenge-gen

> **Synthesis note.** This summarizes 12 paper readings into a cross-domain view. Per-paper detail is in the linked notes. It was written for [[project-challenge-gen]] (literature scan of 2026-10-05). The reading path is [[_moc-hard-instance-generation]].

## The question

How can we generate problem instances that (a) have a solution, with a **certificate produced by the generation process itself**, and (b) are **hard** in the way rare open-problem instances are hard, not easy in the way generic random instances are? The target is phase 1 of challenge-gen: hard trivial words in B(2,5).

## Sources reviewed

*Why random is easy*
1. [[kapovich-2003-generic-case-complexity]]: the word problem is generically "No", in linear time, even in groups where it is undecidable. In an infinite group the trivial words have density 0 (Thm 6.3). The authors explicitly leave the witness version (producing a product of conjugates of relators) open.

*Certified generators in group theory*

2. [[elder-2015-random-trivial-words]]: a Metropolis chain on trivial words whose moves are conjugation and relator insertion. Each trajectory is a certificate (Lemma 2.3). The stationary law depends only on length (Cor. 2.13), so the samples are **generic**.
3. [[2607.26241]] (WPNet): trivial training words made by "tangling" with at most 150 insertions. The generator is certified, but hardness is **not controlled**: the Dehn function is cited as motivation and never measured.
4. [[miasnikov-1999-ac-genetic]]: random AC walks from ⟨x,y;x,y⟩. Difficulty grows steeply with walk length: 10/20/30 moves need 20/300/2208 GA generations. Random moves applied to a hard AK seed "always converged to the original presentation". Composition G(H) transports certificates.
5. [[shehper-2024-ac-hardness]]: about 1.8M AC-equivalent presentations from reverse walks on 1190 Miller–Schupp seeds (App. D). An unsupervised transformer still separates GS-solved from GS-unsolved seeds after "thousands of AC-moves". It gives an operational hardness definition (needs a larger search budget N) and a topological one (persistent homology of the length filtration).
6. [[carreras-2026-ac-certificates]]: certificate-first methodology. JSON move ledgers are replayed by a small stdlib verifier in under 1 s, with hash-pinned artifacts. It introduces an exact bottleneck score (minimax total length along a path) as a hardness measure.
7. [[coulon-2018-trivial-elements-criterion]]: w is trivial in B(r,n) iff a finite sequence of power-removing moves empties it. This holds **only for large odd n**, so it has no theorem behind it for B(2,5). Its value here is that it shows what a natural certificate looks like.

*Planted solutions in random CSP/SAT*

8. [[achlioptas-jia-moore-2004-hiding-assignments]]: planting one assignment biases the clause distribution, and solvers (zChaff, Unit Clause, SP) find it easily. Planting A together with its complement Ā ("2-hidden") symmetrises the bias. The resulting formulas are about as hard as unplanted ones for WalkSAT and zChaff.
9. [[krzakala-zdeborova-2009-quiet-planting]]: **quiet planting**. For q-colouring below c_l = (q−1)², the planted ensemble is indistinguishable from the random one, apart from the existence of the planted solution. The window c_s < c < c_l is hard and guaranteed satisfiable. The method does not apply to random k-SAT.
10. [[2606.15979]]: up to 2^t − 1 solutions can be planted in k-SAT using codes. The result is SQ-indistinguishable from uniform up to about n^{r/2} clauses. The authors' own caveat: these instances are solvable by Gaussian elimination.

*Learned or adversarial generators*

11. [[sato-2019-hisampler]]: REINFORCE learns a distribution of graphs that are hard for a fixed solver, with replay of the top-K hardest instances. On DSATUR it finds instances orders of magnitude harder than Erdős–Rényi. Hardness is solver-relative, and the instances have no known answer or certificate.
12. [[dennis-2020-paired]]: the adversary maximises regret (antagonist return minus protagonist return). The antagonist's success serves as an empirical witness of solvability, and the scheme produces a curriculum of "the easiest task outside the protagonist's skill range".

## Convergence

- **Generic random instances are easy, and hard ones are rare.** In group theory this is proven in the form "the No-answers are fast and generic" [[kapovich-2003-generic-case-complexity]]. In CSPs it is shown empirically for naive planting [[achlioptas-jia-moore-2004-hiding-assignments]]. Every certified group-theoretic generator in the set produces generic instances unless something extra is added [[elder-2015-random-trivial-words]], [[2607.26241]], [[miasnikov-1999-ac-genetic]].
- **Certificates come cheaply from the forward process.** Walking from a known solution yields a replayable proof at no extra cost: relator insertions/conjugations [[elder-2015-random-trivial-words]], AC moves [[miasnikov-1999-ac-genetic]], [[shehper-2024-ac-hardness]], planted assignments [[krzakala-zdeborova-2009-quiet-planting]]. Certificate checking should be a small, independent verifier [[carreras-2026-ac-certificates]].
- **Naive planting leaks.** A planted structure biases the instance statistics, and solvers exploit that bias: a single hidden assignment [[achlioptas-jia-moore-2004-hiding-assignments]], or random moves applied to a seed, which greedy search undoes [[miasnikov-1999-ac-genetic]]. Hiding the structure needs symmetrisation or quietness [[achlioptas-jia-moore-2004-hiding-assignments]], [[krzakala-zdeborova-2009-quiet-planting]].
- **Hardness is relative to a solver.** Every empirical hardness measure in the set is defined against a specific solver or budget: a solver's runtime [[sato-2019-hisampler]], search budget N [[shehper-2024-ac-hardness]], branchings for zChaff/WalkSAT [[achlioptas-jia-moore-2004-hiding-assignments]], regret [[dennis-2020-paired]]. The only solver-independent measures are structural: the bottleneck score [[carreras-2026-ac-certificates]] and persistent-homology barcodes [[shehper-2024-ac-hardness]].

## Disagreement

- **Is statistical indistinguishability enough?** KZ treat quietness as the key to hard planted instances in their window [[krzakala-zdeborova-2009-quiet-planting]]. But [[2606.15979]] is SQ-quiet and still falls to Gaussian elimination. So quiet means "not detectable by statistics", not "hard". Algebraic structure, such as XOR/linear planting or group relators, can give the solution away to a non-statistical solver.
- **Does scrambling preserve seed hardness?** [[miasnikov-1999-ac-genetic]] finds that random AC moves applied to a hard seed are undone by the GA. [[shehper-2024-ac-hardness]] finds that a hardness signal survives thousands of moves as a learned *feature*. These are compatible: the second shows the signal stays detectable, the first that the scrambled instance does not become harder than the seed. Neither shows that scrambling creates new hardness.

## What's settled

- Certified generation by forward moves from a known solution is sound and cheap [[elder-2015-random-trivial-words]], [[miasnikov-1999-ac-genetic]], [[shehper-2024-ac-hardness]].
- Uniform-like sampling of trivial words, or of instances with a known answer, gives generic and easy instances [[kapovich-2003-generic-case-complexity]], [[elder-2015-random-trivial-words]].
- A single naively planted solution makes SAT instances markedly easier, and symmetric or quiet planting fixes that for specific ensembles and solvers [[achlioptas-jia-moore-2004-hiding-assignments]], [[krzakala-zdeborova-2009-quiet-planting]].
- Machine-checkable move ledgers make AC claims cheap to verify independently [[carreras-2026-ac-certificates]].

## What's contested

- Whether *any* general-purpose quiet planting exists for algebraic problems (k-SAT, word problems) that resists every polynomial-time method. [[2606.15979]] shows SQ-quietness can coexist with easy solvability.
- Whether learned hardness features, like Shehper's transformer clusters, reflect actual intrinsic difficulty or quirks of the reference solver [[shehper-2024-ac-hardness]].

## What's open

1. **The witness version of the generic-case question for trivial words.** Is producing a product-of-conjugates certificate generically hard, even though the "No" side is generically easy? This is left open explicitly by [[kapovich-2003-generic-case-complexity]] (§4). This is the theoretical heart of challenge-gen.
2. **Quiet planting for trivial words.** Is there a generator of certified trivial words in B(2,5), or in a quotient, whose output is statistically close to a target "hard" distribution, such as the 119/150 HWW challenge words? It would need to be close in length, commutator depth, and subword statistics. No paper in the set attempts this.
3. **A hardness measure for B(2,5) trivial words.** Candidates suggested by the literature:
   - solver-relative: the [[matveeva-2026-ai-problem-solving]] reducer portfolio, the reduction ratio of beam search, kbmag behaviour;
   - certificate-relative: length of the generation trace, an upper bound on area (only an upper bound, per [[elder-2015-random-trivial-words]]);
   - structural: the bottleneck, i.e. maximum intermediate length along any reduction, the analogue of [[carreras-2026-ac-certificates]].
4. **Adversarial generation with certificate-preserving actions.** Combine the RL + replay-of-hardest loop of [[sato-2019-hisampler]] or the regret objective of [[dennis-2020-paired]] with an action space restricted to certified moves (relator insertion, conjugation; Elder's chain). Hardness should be rewarded against a *portfolio* of solvers, not a single one. The reference solver must never see the certificate, or regret collapses.
5. **Free group vs B₀(2,5).** For B(2,5), triviality in B₀(2,5) is necessary but not sufficient. Certified generation through insertion of u⁵ and conjugation proves triviality in the free B(2,5) directly. Independent checks via GAP (B₀) or kbmag only confirm the quotient.

## Methodology notes

- Evaluate a generator across **several solver families and ensembles**: planted, unplanted, and naive-planted, as in [[achlioptas-jia-moore-2004-hiding-assignments]] (3 ensembles × 4 solvers). A generator tuned against one solver overfits to that solver [[sato-2019-hisampler]].
- Report hardness of the *distribution*, not just the hardest instance found. HiSampler's headline numbers are the hardest single instance [[sato-2019-hisampler]].
- Some sources are weak:
  - [[carreras-2026-ac-certificates]]: single author, AI-assisted, not peer-reviewed, but its claims are backed by replayable ledgers;
  - [[2607.26241]]: single author, with internal inconsistencies noted in its quality_notes;
  - several citation counts are missing because of API rate limits.

## Recommendation

For phase 1 of challenge-gen:
1. Build a **baseline certified generator** for B(2,5) trivial words: Elder-style insertion of conjugates of u⁵, plus free reduction, emitting a trace/certificate. Verify it with an independent small checker, following Carreras's certificate-first pattern. Cross-check in B₀(2,5) via GAP, reusing [[2026-09-30-b25-b0-challenge-triviality]].
2. **Define hardness metrics first.** Compute them on (a) baseline generator output and (b) the human challenge words. The gap between (a) and (b) is the target for the generator to close.
3. Then try **hardness-seeking generation**: an adversarial/RL generator over certified actions (HiSampler/PAIRED style), rewarded against a solver portfolio, with diversity constraints.

Route open question 1 (witness generic-case hardness) to a math expert/Validator. Route questions 2–4 to an Experimenter once the code repo is registered in the profile.

## Related vault material

- Papers: see `papers_synthesized`
- Concepts: [[Concepts/certified-instance-generation]], [[Concepts/quiet-planting]], [[Concepts/andrews-curtis-moves]]
- MOC and overview: [[_moc-hard-instance-generation]], [[hard-instance-generation-overview]]
- Prior syntheses: [[_synthesis-rl-for-math]], [[_synthesis-b25-beat-beam-search]]
- Project and experiments: [[project-challenge-gen]], [[Challenge Generation/_progress]], [[2026-09-30-b25-b0-challenge-triviality]], [[matveeva-2026-ai-problem-solving]]
