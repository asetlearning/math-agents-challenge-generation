---
title: "b25-solver stage 1 — E0-rebuild-seed-pool and I1-invariant-review (plan)"
domain: group-theory
project: b25-solver
instance: B(2,5)
experiment_type: patternboost-solver
status: draft
author: asetlearning
date: 2026-11-04
tags: [agent/lead, user/asetlearning, domain/group-theory, topic/b25, topic/burnside, topic/trivial-words, topic/patternboost, topic/word-problem, project/b25-solver, status/draft, experiment, methodology]
---

# Stage 1 plan: E0-rebuild-seed-pool and I1-invariant-review

> [!info] Plain English
> We want a solver that learns from the word it is trying to prove trivial. Stage 1 uses PatternBoost the other way round: it builds words that are trivial by construction (each comes with its proof) and steers them towards the target word. If one of them equals the target, or cancels a long piece of it, the target is proved trivial or shortened, with a certificate. Earlier PatternBoost runs never even produced words that look like our targets: every word they made collapsed under 2.5-reduction. So stage 1 first checks that a better starting pool reaches the target's regime (E0-rebuild-seed-pool), and in parallel reviews which mathematical similarity measures make sense (I1-invariant-review). No model is trained in stage 1.

Project: [[project-b25-solver]]. Decisions: owner, 2026-11-04.

## Terms
- **Benchmark word, arm, recipe:** a registry candidate of [[ds-b25-challenge-candidates]] (revision 3). Its recipe (construction arm C1, C3 or C3r2, parameters, seed, factors) is a proof of triviality.
- **Factor word / certificate:** a product of conjugated relators; it expands to a trivial word and is its proof ([[challenge-gen-candidate-workflow]] § 3).
- **Pool:** the set of factor words PatternBoost scores, searches from, and (later) trains on.
- **R₂.₅:** greedy, then cyclic exhaustive, 2.5-reduction.
- **Group distance d(w, u):** the length after inserting u⁻¹ into the cyclic word w at the best position and cancelling on both sides (a suffix of u before the position, a prefix of u after it), minimised over positions and the 16 images of w (8 letter automorphisms × inversion). It is the cyclically reduced length of a conjugate of w·u⁻¹; for trivial u, d(w, u) < |w| means w is shortened, with a certificate. The scorer value is the cancelled fraction, cancel / min(|u|, |w|).
- **Tracks:** T-in (learn from same-arm words, other seeds), T-out (other arms only), T-blind (no challenge-gen recipes). The target's own recipe is never used.

## Targets

The 6 shortest benchmark words:

| id | length | arm |
|---|---|---|
| C1\|6\|1 | 138 | C1 |
| C1\|6\|16 | 156 | C1 |
| C3\|4\|22 | 192 | C3 |
| C3\|4\|17 | 220 | C3 (shortest known 215, uncertified) |
| C3\|4\|15 | 222 | C3 |
| C1\|6\|29 | 249 | C1 |

## Development (Developer; heavy parts in tcgraph, Python bindings)

1. **Seed-pool sources for PatternBoost**, one per track:
   - T-in: the challenge-gen construction for the target's arm, fresh seeds;
   - T-out: the construction for the other two arms;
   - T-blind: plain products of conjugates of v⁵ relators (|v| ≤ 7).
   The target's own recipe is excluded in every track, and its id is recorded in provenance. Reuse the challenge-gen generator code; do not copy it.
2. **Group-distance scorer:** d(w, u) over rotations and the 16 images, as a hybrid-score term next to the existing scorers.
3. **E0 measurement:** build the pool, measure, run the existing local search (small budget) on the best of the pool with the new scorer, measure again. Measured per pool: the distribution of |R₂.₅(u)|, the best hybrid score and the best d(w, u) against each target. Do the same for the old v⁵ pool (|v| ≤ 5) as the baseline.
4. **Certificate adapter:** factor word → `bench solver` certificate, so that any break or shortening is verified by the bench.

Tests: certificate re-expansion and trivial abelianization on a regression sample, plus unit tests for the new scorer (invariance under rotation and the images).

## E0-rebuild-seed-pool (Experimenter-B25, cpuserver, CPU only)

- For each target and each track: build a pool (size set in the run plan), score it, run the existing local search with small budgets, and measure as in Development item 3.
- **Pass, per target:** (i) at least 10% of the pool survives 2.5-reduction at length ≥ |w|/2, against 0% for the old v⁵ pool; and (ii) the best hybrid score beats the best of the old v⁵ pool.
- **E0 passes if this holds for at least 1 of the 6 targets in each track.**
- Any u with d(w, u) < |w| goes straight to verification through `bench solver`; it is a shortening of a benchmark word.
- Rare-event rule: stop at the first decisive result; later steps are "not run".
- The run plan, with measured costs, goes to Lead before submit.

## I1-invariant-review (Researcher, then Math Expert)

Group invariants of B(2,5) and its quotients take the same value on w and u, since both are trivial. A useful similarity must therefore be measured in the free group F₂ or in finite approximations. Candidates to review:
- (a) images in the free nilpotent quotients F₂/γ_c; the Magnus expansion and Fox derivatives over ℤ₅;
- (b) images in the approximation groups B_k (relators of length ≤ k);
- (c) free-group distances: d(w, u), common subwords, BPE token profiles.

The Researcher reviews the literature. The Math Expert proposes candidates, with soundness and cost. The Developer implements accepted ones as hybrid-score terms after E0.

## Budget and stop

- Stage 1 is capped at about $30 of cpuserver time; reassess after.
- No model training in stage 1. Experiments that need a GPU wait for the GPU server.
- If E0 fails in every track, the next step is a new pool construction, not a model.

## Settled details (Lead, 2026-11-04, in the Developer plan review)
- T-blind uses only plain products of conjugates of v⁵ relators (|v| ≤ 7): no t-words, no certified-word datasets, no substitution step (those are the generator's inputs and mechanism). A variant with the substitution step can be added later.

## Related material
- [[project-b25-solver]]
- [[challenge-gen-candidate-workflow]]
- [[ds-b25-challenge-candidates]]
- [[patternboost-generation-methodology]] — the generation-side PatternBoost and its earlier results
- [[patternboost-generation-results]]
