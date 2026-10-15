---
title: "Challenge generation — difficulty metrics and success criteria (B(2,5))"
domain: group-theory
project: challenge-gen
instance: B(2,5)
status: draft
author: asetlearning
date: 2026-10-05
tags: [agent/human, user/asetlearning, domain/group-theory, topic/b25, topic/burnside, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, project/challenge-gen, status/draft, decision]
---

# Challenge generation: difficulty metrics and success criteria (B(2,5))

> **Owner's definitions**, set 2026-10-05 by Alex Myasnikov (asetlearning). They replace "similarity to the challenge words" as the main objective. Thresholds and design choices were confirmed by the owner. The implementation notes are proposals until code exists.

## Goal

Generate words in the free Burnside group **B(2,5)** that are **provably trivial**, by construction or with a certificate, and that are **not easy to decide**: a solver should not be able to tell quickly that they are trivial.

## Notation

- **Certificate.** F = (k₁,c₁) … (k_m,c_m) is a factor word, i.e. a list of (relator index, conjugator) pairs. Its expansion is w = ∏ cᵢ⁻¹ R_{kᵢ} cᵢ, freely reduced.
- **Reduced word.** w̄ is the freely reduced expansion of F, and n = |w̄|.
- **2.5 reduction.** R₂.₅(w) = `greedyReduceCyclicExhaustive(greedyReduce(w̄))`, in tcgraph `reduction2_5`. From Python it is `greedy_reduce_cyclic_exhaustive2_5(greedy_reduce2_5(w))`, via `tcgraph_ext` / `algorithms/word_problem.py`.

## Level 0: valid challenge (required for everything below)

1. **Certified.** Re-expanding F gives exactly w̄. Every relator used is trivial in free B(2,5):
   - the standard relators v⁵, |v| ≤ L, qualify automatically;
   - relators from a file or from BPE must carry their own certificate of triviality in **free** B(2,5). Triviality in B₀(2,5) is not enough.
2. **Sanity check.** The abelianization is trivial: exponent sums ≡ 0 mod 5. This is a cheap bug detector, not a proof.
3. **Recorded with the challenge:** the minimised certificate F* (see Metric 2) and the generation provenance (code SHAs, config, seeds).

## Metric 1: resistance to 2.5 reduction (heuristic difficulty)

**Definition.** ρ(w) = |R₂.₅(w)| / |w̄|.

**Why this threshold works.** The owner reports, from experiments, that **every randomly generated factor word reduces to the identity under 2.5 reduction**, i.e. ρ = 0. Generic certified words therefore fail this metric, and resisting 2.5 reduction is a meaningful difficulty threshold even though the reducer is heuristic. The baseline should re-measure ρ on random factor words in every new setting, to confirm the threshold still separates them.

**Pass.** R₂.₅(w) ≠ 1 **and** ρ(w) ≥ **0.5**. The value of ρ is reported for every final candidate, so the threshold can be revised later.

**Cost.**

| Step | Cost |
|---|---|
| `greedyReduce` (`findSquares`) | O(n²) |
| `greedyReduceCyclic`, all shifts | ≈ O(n³) |
| `greedyReduceCyclicExhaustive` | repeats `greedyReduceCyclic` |

Guidance for using it sparingly:
- **Two modes.**
  - *Screen* mode passes `fractions = {0, 0.5}` (as the `length_range` scorer does) and is used inside the loop on the pool or top-k.
  - *Certify* mode uses all cyclic shifts and runs only on final candidates. ρ is reported in certify mode.
- **Never run it per local-search neighbour.** Run it on the pool or top-k after each iteration, and cache results by word hash (`WordHash`).
- **Cheap pre-checks.** First test whether w̄ contains any subword power with exponent ≥ 2.5 (maximal-power detection). If none exists, `greedyReduce` cannot rewrite anything. This needs verifying against the code before relying on it.
- Lengths are measured on freely reduced words. Also record the cyclically reduced length.

## Metric 2: Dehn-function proxy (theoretical difficulty)

**Background.** Owner's motivation: Myasnikov–Ushakov ([[myasnikov-ushakov-2011-random-van-kampen]]; the full text was not accessible, so this comes from the abstract and later restatements) show that a **random van Kampen diagram over a fixed finitely presented group is hyperbolic**, even when the group is not. The filling function they introduce is **depth** δ(w): for hyperbolic groups δ(w) = O(log |w|), and a relator-closure solver runs in Õ(|w|·L(R)^{δ(w)}). Random relator-insertion words, which are exactly our baseline factor words, are therefore generic and easy. Hard challenges must have atypically large fillings. The paper's results concern **depth, not area**, and assume a finite presentation, which B(2,5) is not. Using area (D below) is the owner's choice of proxy, and depth is a candidate companion metric (see Open questions).

**Definition.** D(w) = |F*| / |w̄|, where F* is the **minimised** certificate. This is the tcgraph `DehnFunctionScorer` (`pb_scoring.cpp:340`, `#factors / |expanded freely reduced word|`), applied to F* rather than to the raw F.

**Why the certificate must be minimised.** |F| is an upper bound on the area of w̄ (the minimal number of relators in a van Kampen diagram), not the area itself. A raw F can be inflated without changing w̄. The standard set contains both v⁵ and v⁻⁵, so a pair c⁻¹v⁵c · c⁻¹v⁻⁵c cancels freely while adding 2 to |F|. Unminimised scores reward padding. The minimisation:
- **Loop erasure.** Track the freely reduced prefix words P_j = expand(f₁…f_j). If P_i = P_j for some i < j, the block f_{i+1}…f_j freely cancels; delete it and repeat. A hash of the free-reduction stack makes this roughly linear in the total expanded length. This removes adjacent inverse pairs and every longer freely cancelling block.
- **What it does not remove.** Blocks that cancel only modulo relators stay. So D(w) on F* is still an **upper bound** on area/n. True area lower bounds are out of reach in general, and this caveat must accompany any claim.

**Gate.** D is counted toward success only for words that **pass Metric 1**.

**Targets.**
- **Good challenge:** D(w) ≥ 1 on F*, i.e. at least as many factors as letters.
- **Great success:** quadratic growth, |F*| ≍ c·n². This is a property of a **family** across lengths n, not of a single word. Fit the exponent α in |F*| ∝ n^α over Metric-1-passing words at several n; α ≈ 2 is the target. A single word only has a ratio.

## Owner decision 2026-10-14: representative convention for ρ (T-001)

Source: the T-001 baselines ([[hardness-baselines-results]]). The heuristic reducer is rotation-invariant but **not invariant under letter relabelling or inversion**: for 2 of the 820 words of [[ds-b25-trivial-2-5reduced-aut8-20261007]], 13 of 16 and 15 of 16 images (8 letter automorphisms × inversion) reduce to the empty word, while the stored strings were fixed points of the parent form. Validator: the words are trivial in free B(2,5) (proven).

**Decision.** Any hardness claim uses ρ_min16 = min over the 16 images of |R₂.₅(image)| / |w̄|. Screening may use the generated word only; all 16 images are computed on finalists. The definitions above are unchanged; this fixes which representative a reported ρ refers to. Implementation: `--min16` in `experiments/challenge_gen/hardness/run_baselines.py` (b25 branch `12-hardness-harness`), record fields `min16_lens`, `min16_len`, `rho_min16`; the level classification uses ρ_min16 when the flag is set.

## Owner decision 2026-10-14: headline D for mixed relator sets (T-003, T-020)

Source: T-003 stage 1 ([[t003-gated-dehn-search-2026-10-14#Results]]) and the Peiffer check ([[2026-10-14-t020-peiffer-loophole]]).
- On a relator set that mixes standard v⁵ and dataset relators (R-M), D can be raised by padding. Standard factors that the reducer removes add cells but leave no trace in R₂.₅(w): R-M best D 0.13, but best D on dataset factors only 0.039.
- Loop erasure also leaves Peiffer pairs (two factors M⁻¹f_i M f_j = 1 that cancel only together).

**Definitions** (all on the freely reduced word w̄, n = |w̄|):
- **F*_P, N*_P.** The certificate after alternating loop erasure and Peiffer-pair deletion until the factor count stops changing (`reduce_certificate` in b25 `experiments/challenge_gen/hardness/minimise.py`). N*_P = |F*_P| ≤ N* = |F*|.
- **D_P** = N*_P / n. Like D, it is an **upper bound** for area/n, never the area: the count depends on the deletion order, and larger cancelling tuples are not searched.
- **D_dataset_P** = (number of dataset-relator factors in F*_P) / n. Standard factors are not counted.

**Decision.** For any relator set containing both standard and dataset relators, the **headline D** is D_dataset_P. Full D and D_P are always reported next to it. (Consequence, not part of the decision: for a pure dataset relator set (R-D), D_dataset_P = D_P.) **Levels (owner decision 2026-10-14, closing the open question).** L2 and every D threshold (for example the T-003 bar 0.200) are read on the headline D: D_dataset_P on mixed relator sets, D_P on pure sets. Full D is always reported alongside. A path-length D (D_path, T-016 overlap chains) is never a headline D and never counts toward L2.

**Provenance rule (owner decision 2026-10-14, after T-016).** Words built as chains (rewriting-path constructions: a strip of cells with nearly bounded |w̄|) report D_path in its own column, never as headline D. Their level label **caps at L1 by construction**, even when N*_P/|w̄| ≥ 1, because for pure-dataset words D_P and D_path coincide numerically but D_path measures path length, not area.

## Owner decision 2026-10-14: headline D_c for all constructions (T-023)
Source: Developer's T-023 results (b25 PR #13), as relayed by Lead. Loop erasure and Peiffer deletion leave further cheaper certificates:
- about 25% of T-003 R-M finalists have adjacent inverse cells;
- T-016 chains compress hard once blocks are replaced by single relators (best E1c word: N* 55 → N*_c 7).

**Definition.** D_c = N*_c/|w̄|. N*_c is the factor count after, in order:
1. loop erasure;
2. Peiffer-pair deletion (to the fixpoint, as for F*_P);
3. inverse-cell reduction (adjacent inverse cells, i.e. cancelling pairs in the folded diagram, deleted);
4. relator-closure compression: every contiguous block of factors whose expansion is cyclically a table entry is replaced by one factor. The table is all 1,630 R7 entries (b25_full, v^{5k} with |v| ≤ 7, and inverses, multiples included).

Like D, it is an upper bound for area/|w̄|, never the area.

**Decision.** D_c is the **headline certificate measure for all constructions**, and all D thresholds (L2: ≥ 1; bars such as 0.200) are read on it. D, D_P, D_area, b₁ and N_int are reported alongside. Earlier headline measures (D_P, D_dataset_P) are kept as columns. The T-003 and T-016 headline tables are updated once Developer's numbers are final.

**Mixed relator sets (owner decision 2026-10-14).** On sets that mix dataset and standard relators, the headline is **D_dataset_c** = (dataset-relator factors of the compressed certificate F_c)/|w̄|, with the full D_c alongside. On pure sets the headline is D_c.

## Owner decision 2026-10-14: vertex depth as the area-vs-path classification
Source: Math Expert's vertex-depth criterion ([[2026-10-14-vertex-depth-criterion]]), which replaces the edge-based N_int and b₁ of [[2026-10-14-area-vs-path-criterion]]. Those counted tiny triangles in chains as interior. All statistics are computed on the compressed, reduced certificate F_c (headline) and on the raw certificate (diagnostic).
- **Deep cell:** no vertex of the cell lies on the boundary ∂Δ (one touching point counts as touching).
- **Peeling and depth:** remove all cells touching ∂Δ, recompute the boundary, and repeat; depth(cell) is the removal round, counting from 0. **maxdepth** is the largest depth, and **N_deep** counts the cells of depth ≥ 1.
- **Normalised against the ideal square with the same N** (N ≥ 9): T_deep = N_deep/(√N − 2)² and T_depth = maxdepth/((√N − 1)/2).
- **Classification:**
  - **path-like** iff N_deep = 0;
  - **area-like** iff T_deep ≥ 0.5 and T_depth ≥ 0.5;
  - **thick strip** otherwise.
  - Hub degree and cut width are diagnostics. The 0.5 cutoffs are conjectured (Math Expert).
- **V_int** = number of interior vertices, the shaping term of the T-018 objective J = (N_deep + 0.25·V_int)/|w̄|.
- **Depth success criterion (T-018):** the first L1-certified, novel B(2,5) word with maxdepth ≥ 2 and T_deep ≥ 0.5. D and D_c are tracked but not expected to reach 1. Math Expert's sizing conjecture: a square-like disc has |w̄| ≈ 4√N·e, so D ≥ 1 needs N ≳ 16e², about 1,300 cells for |v| ≤ 7.

**D_area (owner decision 2026-10-14).** When T-023 provides it, D_area = N_int/|w̄| (interior cells of the folded diagram, Math Expert's [[2026-10-14-area-vs-path-criterion]]) is reported alongside D and D_path, not as headline.

**Novelty (owner decision 2026-10-14, after T-016).** For every construction, "novel" means G2 **and** the all-classes check: R₂.₅(w) is not the canonical class of any of the 1,640 relators, used or not ([[challenge-gen-glossary#novel L1 and the guards G1 and G2]]).

**Standard guard (owner decision 2026-10-14, from Validator's T-016 review).** For EVERY construction, a word counts as L1 and novel only if it also passes:
1. **Non-increasing 2.5-closure:** the closure contains neither the empty word nor any relator class. This catches the greedy reducer's move-order dead ends: 14 of 190 T-016 E1 words, and 20 of 199 E1c L1 words, reduce to empty this way.
2. **Exhaustive ≤ 2-cell certificate test** over the relator table: no certificate with at most 2 cells.
3. **N*_c reported next to D.**

It is reported as "no cheaper certificate found by these tests", never as an area statement. To be revisited if a method places standard cells genuinely inside the diagram (T-018), so that they are no longer padding.

## Owner decision 2026-10-15: final area-like rule, wrapped-relator guard, depth-sum J
Source: Math Expert's follow-ups ([[2026-10-14-depth-followups]]), after T-023 showed 10 E1c chain words with one deep cell each on the compressed certificate (9 of them the same 60-letter dataset relator, #212). These are rings of 6–9 cells around one relator, so the word is conjugate to that relator rather than thick. The three proposals are accepted as below. They are `#status/conjectured`, and Validator reviews them in parallel with the T-018 start, not before it.
1. **Area-like rule (final; replaces "N_deep ≥ 2" of the 10-14 rule).**
   - **area-like** iff N ≥ 16, T_deep ≥ 0.5, T_depth ≥ 0.5, and either the deep cells contain a **dual-connected core of ≥ 2 cells** (deep cells sharing an edge path, connected in the dual graph restricted to deep cells) or **maxdepth ≥ 2**;
   - **small enclosed** iff N_deep ≥ 1 and N < 16;
   - **thick strip** iff N_deep ≥ 1, N ≥ 16, and the diagram is not area-like (owner, 2026-10-15: thick strip kept for large non-area-like diagrams);
   - **path-like** iff N_deep = 0.
   - Why: two wrapped relators joined by a chain have N_deep = 2 yet stay path-like at the larger scale.
2. **Wrapped-relator guard (novelty).** If the compressed, reduced diagram has N_deep = 1 and every other cell touches both ∂Δ and the deep cell, the word is reported as **"wrapped relator"** and is **not novel**, in the same way as a word that is reducer-equivalent to a relator. This applies to every construction.
3. **Objective J (T-018 and later depth searches):** J = (Σ_cells depth(c) + 0.25·V_int)/|w̄|. This replaces (N_deep + 0.25·V_int)/|w̄|. The depth-sum term is 0 for a chain, 1 for a wrapped relator and 10 for a 5×5 grid (whose full J numerator is 14, since V_int = 16), so a second ring is worth more than extra first-ring cells.
4. **maxdepth-vs-N logging (falsifier).** Every depth search logs maxdepth at every N it reaches, per lineage, and reports a log N against √N fit across seeds. If the curve looks logarithmic, the presentation behaves hyperbolically at these scales: D stays bounded and the area route is closed for those relators. Report that as a finding.

The success criterion (maxdepth ≥ 2 and T_deep ≥ 0.5 on an L1-certified, novel word) is unchanged. Not adopted for now: novelty by centre relator, ring-diagram templates, and a T-016 ring-growth follow-up around #212.

## Success levels

| Level | Criterion | Meaning |
|---|---|---|
| L0 Valid | Certificate re-expands to w̄; standard (or certified) relators; abelianization passes | Provably trivial in free B(2,5) |
| L1 Hard (heuristic) | L0, R₂.₅(w) ≠ 1, ρ ≥ 0.5 (certify mode) | Defeats the reducer that kills all random factor words |
| L2 Hard + high filling | L1 and D(w) ≥ 1 on F* | Non-generic filling, an upper-bound proxy |
| L3 Great | A family of L1 words with \|F*\| growing ≈ quadratically in n (fitted α ≈ 2) | Quadratic area as a function of reduced length (proxy) |

**Reporting** for every run: counts and rates at each level, the distribution of ρ and of D (on F*), n, |F| versus |F*|, and the generation cost. The baseline is random factor words from the same sampler; the owner's finding predicts ρ = 0 for all of them.

## Secondary (optional)

Similarity to the 150 real challenge words (edit/Hellinger scorers) is kept as an optional shaping term or diagnostic. It is no longer an objective. The real challenge words are known trivial only in B₀(2,5) ([[2026-09-30-b25-b0-challenge-triviality]]), so they cannot be L0 instances.

## Open questions

- **Evidence so far (2026-07-23 run, [[patternboost-generation-results]]):** maximising raw D alone gave 0/~300k L1 words and a best D of 0.344. It shrank the words instead of growing the factor count. The objective needs a Metric-1 term or a length floor.

- Does PatternBoost with an objective of the form "ρ (screen mode) × D(F*)" escape the generic regime, or does it find shortcuts? Remaining loopholes include cancellation modulo relators and long conjugators that inflate n.
- Is there a cheap **lower** bound on area for B(2,5) words that could replace the upper-bound proxy?
- **Depth versus area.** Compute a depth statistic from the certificate's diagram, i.e. how deeply nested the factors are relative to the boundary. A certificate with many factors can still describe a shallow "fan" diagram that relator-closure solvers finish in a few rounds. Test which of D and depth better predicts solver failure.
- Interaction with length: D ≥ 1 is easier for short w̄. Should successes be reported by length band?

## Related material
- [[project-challenge-gen]] · [[Challenge Generation/_progress]]
- [[B25/PatternBoost Generation/_type|PatternBoost Generation]]: the current generator
- [[myasnikov-ushakov-2011-random-van-kampen]]: theory anchor for Metric 2
- [[dehn-function]] · [[kapovich-2003-generic-case-complexity]] (generic instances are easy) · [[_synthesis-hard-instance-generation]]
- [[dep-tcgraph-agentic]]: 2.5 reduction and `DehnFunctionScorer`
