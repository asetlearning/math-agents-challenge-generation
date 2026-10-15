---
title: t016-overlap-chaining-2026-10-14
hypothesis: "The 820 dataset relators have long cyclic overlaps (a piece y with a rotation of r_i ending in y and a rotation of r_j^±1 starting in y^-1) well beyond what random words of the same lengths show. Chaining factors along heavy overlaps gives certified L1 words with path-length D above 0.200. This D measures path length, not area."
status: inconclusive
author: asetlearning
date: 2026-10-14
todo: T-016
project: challenge-gen
instance: B(2,5)
experiment_type: structured-constructions
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, project/challenge-gen, status/inconclusive, experiment, methodology]
---

# T-016: overlap chaining of the dataset relators — pre-registration

Source: Math Expert proposal, idea 1 ([[2026-10-14-cancellation-constructions]]). Owner decisions of 2026-10-14 ([[project-challenge-gen]] § Cautions on D, todo T-016):
- chain words are reported as a separate **path-length D**, never mixed with area D;
- the T-006 token table may serve as a cheap candidate filter.

Local VM only: string matching plus the T-002 harness. No Mac time.

## Question
How long are the pieces that the 820 dataset relators ([[ds-b25-trivial-2-5reduced-aut8-20261014]]) share up to rotation and inversion? Do chains of factors glued along those pieces give certified L1 words with large N*/|w|?

## New terms (all defined here; added to [[challenge-gen-glossary]] with the results)
Words are over a, b, A = a⁻¹, B = b⁻¹; "relator" means one of the 1,640 table entries (820 dataset words and their inverses). Every relator is cyclically reduced.
- **Rotation, rotation prefix.** If a relator r = p q (as strings), then q p is a rotation of r and p is its rotation prefix. With conjugator c = p, the factor c⁻¹ r c freely reduces to q p. So every rotation is a legal factor, with the rotation prefix as its conjugator.
- **Overlap (piece) y of an ordered pair (u, v) of relators.** A nonempty word y such that some rotation of u ends in y and some rotation of v starts in y⁻¹. Equivalently, y is a common subword of the cyclic words of u and v⁻¹. For one occurrence, the product rot(u)·rot(v) cancels exactly 2|y| letters at the junction if y is maximal there. The overlap of the pair is the longest such y; |y| ≤ min(|u|, |v|). Since (u, v) and (v⁻¹, u⁻¹) give the same y, unordered pairs of cyclic words are enough.
- **Overlap ratio θ(u, v)** = |y| / min(|u|, |v|), with y the longest overlap.
- **Containment pair.** A pair whose longest overlap is the whole shorter relator (θ = 1), i.e. one relator contains the other or its inverse as a cyclic subword. These are the dataset's decomposable words: 9 words, 7 of them sharing a 42-letter block. They are reported separately and excluded from the falsifier.
- **Distinct classes.** A pair (u, v) where v is not u⁻¹ up to rotation. Such a pair would overlap fully and cancel freely, which loop erasure removes.
- **Overlap histogram.** The distribution of θ (and of |y|) over all pairs of distinct classes.
- **Overlap graph.** Directed graph on the 1,640 relators with an edge u → v, labelled by occurrence positions, for every maximal overlap occurrence with |y| ≥ ℓ_min. ℓ_min is fixed from the histogram before any chain is built: the smallest |y| at which the dataset count exceeds 10× the count of null model N1, but at least 6. Fallback, if no |y| satisfies this: the |y| at the top 1% of the dataset histogram, but at least 6.
- **Chain.** A factor word f₁ … f_k with f_t = c_t⁻¹ r_t c_t, where c_t is a rotation prefix and consecutive factors meet at an overlap occurrence. For a middle cell, the incoming piece and the outgoing piece must not overlap on the cyclic word of r_t, so rot(r_t) = y_{t−1}⁻¹ m_t y_t.
- **Exposure e_t** = |m_t|, the letters of cell t that stay on the boundary of w.
- **Heavy path.** A chain found by the walk below with large D_path.
- **D_path (path-length D).** For a chain word, D_path = N*_P/|w̄|. This is the same formula as D_P, but it carries a different name because the geometry differs.
  - A chain is a strip of cells glued in a line (a rewriting path x₁ → x₂ → … → x_{k+1}), not a disc.
  - |w̄| ≈ 2|y₀| + Σ e_t grows only with the exposures, so D_path → 1/(mean exposure) as k grows. It is unbounded when exposures are 0.
  - It is never reported in the same table or ranking as area D (owner).
  - Since chains use dataset relators only, D_dataset_P = D_P = D_path here.
- **Null models N0 and N1.** Each has 820 random words with the same multiset of lengths as the dataset, plus their inverses. Seed 16000001 (N0), 16000002 (N1). They get the same overlap computation.
  - **N0:** random cyclically reduced words.
  - **N1:** random cyclically reduced words with no 2.5-power, linear or cyclic (exact test `hardness/powerfree.py`). Generated letter by letter with backtracking.
  - N1 is the reference for H1b and ℓ_min. The dataset words are 2.5-reduced, and excluding powers shrinks the effective alphabet, so N1 has *more* chance overlaps than N0. N0 alone would understate the noise. This is needed because for words of 32–123 letters, chance alone produces long common pieces among about 1.3 million pairs: the expected maximum is roughly log₃(pairs·L²), about 20 letters, i.e. θ ≈ 0.3 for median-length (67-letter) words. So the H1 threshold of 0.20 alone cannot distinguish the dataset from noise.
- **Token filter.** Candidate pairs are pairs (u, v) such that u and v⁻¹ both contain, as cyclic subwords, the same T-006 token string of length ≥ ℓ_min. Tokens come from the BPE tokenizers trained on the challenge words ([[b25-challenge-token-analysis-results]]). **Recall** = the share of overlap-graph edges whose pair is a candidate. **Precision** = the share of candidates that are overlap-graph edges.

Existing terms used as defined: [[challenge-gen-glossary#headline D, D_P and D_dataset_P|F*_P, N*_P, D_P]], [[challenge-gen-glossary#rho_min16|ρ_min16]], [[challenge-gen-glossary#pre-check: no square and power-free|power-free shortcut (exact power test)]], [[challenge-gen-glossary#novel L1 and the guards G1 and G2|G2]], L0/L1/L2 ([[challenge-gen-success-metrics#Success levels]]).

## Hypotheses (falsifiable)
- **H1 falsifier (overlaps exist).** The max θ over distinct-class, non-containment pairs is ≥ 0.20. **If not, report and stop** (owner).
- **H1b (overlaps beat chance).** In the tail θ ≥ 0.3, the dataset has ≥ 10× as many distinct-class, non-containment pairs as the power-free null N1 (N0 reported alongside). **Falsified** otherwise. Then long overlaps are what random words of these lengths also have, and chaining is not a property of the dataset. Chains are still built (H2), but reported with this caveat.
- **H2 (chains beat the T-003 bar, path-length).** The walk produces at least one chain word that is certified L1 (ρ_min16 ≥ 0.5, certify mode) and novel (G2), with D_path > 0.200. **Falsified** if the maximum D_path over certified, novel L1 chains is ≤ 0.200.
  - 0.200 is the T-003 area-D bar, used here only as a numeric reference point, not as a comparison of like quantities. The best R-D area D of T-003 (0.083) is reported as a second marker.
  - Sizing: D_path → 1/(mean exposure), so D_path > 0.200 needs a mean exposure of at most about 5 letters, i.e. |y_in| + |y_out| ≥ L − 5 per middle cell. Chance-level overlaps (θ ≈ 0.3) cannot reach this; only long structured overlaps can.
  - Any chain with D_path ≥ 1 is reported as such but is **not** an L2 claim. L2 is read on the headline (area) D (owner decision 2026-10-14), never on D_path.
- **H3 (junctions keep words 2.5-reduced).** Prediction (Math Expert): a chain is a product of 2.5-reduced pieces, so it survives unless a junction creates a power. At least 80% of final chain words pass the exact power test (cyc(w̄) has no 2.5-power, linear or cyclic). Then ρ_min16 = |cyc(w̄)|/|w̄| with no reducer call: ρ is measured against |w̄|, and R₂.₅ includes the cyclic reduction. **Falsified** below 80%. Cyclic reduction itself is not a junction effect; it is handled by the walk gate (step 4).
- **H4 (token filter, owner observation). DEFERRED** (owner 2026-10-14): the tokenizer files are not on the VM. Design kept for a later run. Recall of the token filter on overlap-graph edges is ≥ 0.9. **Falsified** below 0.9. Precision and time saved are reported either way. Prior caveat: the tokens were trained on the 150 challenge words, not on the 820 dataset words, and most are longer than any dataset word (average token length 2,542 and 3,723). Only tokens of ≤ 123 letters can occur at all.
- **H5 (L0).** 100% of chain certificates pass the independent L0 check (re-expansion against the hash-pinned table, abelianization). **Falsified** by one failure.

Reported, not hypotheses:
- for the best chains, |w̄| against k, with the fitted slope (mean exposure) and intercept;
- the number of zero-exposure cells, i.e. chain stretches with bounded |w̄| (owner's watch item (c));
- N* vs N*_P per chain;
- every chain word with D_path ≥ 0.2: N*, N*_P, |w̄|, relator set (watch item in [[project-challenge-gen]] § Cautions on D).

## Method
1. **Overlaps (exact).**
   - Index every cyclic substring of length k₀ = 6 of each relator (doubled word, positions mod L).
   - Pairs sharing a k₀-mer are extended to their maximal common occurrences.
   - This is exact for |y| ≥ 6, which covers θ ≥ 0.2 for every pair (20% of the shortest word, 32, is 6.4). Shorter overlaps go into one bin "< 6".
   - Same code on the null models N0 and N1.
   - **Positive control:** the 7 decomposable words must show their known 42-letter block as containment pairs.
2. **Falsifier check** (H1, H1b). Stop here if H1 fails.
3. **Overlap graph** at ℓ_min (rule above), with and without containment edges.
4. **Walk (heavy paths).**
   - Deterministic beam search over chains, beam width 200, length k ≤ 60 (the T-003 factor cap).
   - State: (last relator, its incoming occurrence), so that the outgoing piece is chosen disjoint from it.
   - Walk score: k/|w̄| with incremental free reduction. The exact N*_P (`reduce_certificate`) is computed on finalists only, and the reported D_path always uses N*_P. Expected: N*_P = k for chains without repeated relators; any difference is reported.
   - Gate per step: |cyc(w̄)|/|w̄| ≥ 0.5 (exact, cheap). Strips that nearly close up lose letters to cyclic reduction and would otherwise fail L1 at evaluation.
   - Start set: every overlap-graph edge.
   - Relators may repeat. A step that would make the chain cancel freely beyond the planned piece is allowed, and the actual expansion is what counts.
   - Ties broken by seed 16000001.
   - Two runs: containment edges excluded (main) and included (reported separately, since a containment step trades two cells for a shorter trivial word).
5. **Finalists.**
   - Per run: the 200 best chains by D_path, plus the best chain per length k ∈ {2, 3, 5, 10, 20, 40, 60}.
   - Evaluation with the T-002 harness (`hardness/run_products eval`): L0 independent of the walk, F*, `reduce_certificate` (F*_P), exact power test, then certify-mode R₂.₅ and ρ_min16 where the test fails, and G2.
6. **Token filter** (H4, deferred). Uses the T-006 tokenizer vocabularies, both `bpe_tokenizer_challenge_*` files. Token strings of length ≥ ℓ_min are matched as cyclic subwords of u and v⁻¹ (Aho–Corasick or a set lookup), and the candidate set is compared with step 3. Timing for both routes.

Code: a new module `experiments/challenge_gen/t016/` on a b25 branch off main (`overlaps.py`, `chains.py`, `eval_chains.py`), with tests: the rotation-prefix factor identity, overlap exactness on planted pairs against a brute-force LCS, and the positive control. No changes to the workflow or harness.

## Cost
Local VM, an estimated 10–60 CPU-minutes in total. Overlaps: about 1.3 million pairs, k-mer seeded. Walk: 200 × 60 steps × candidates per step. Evaluation: about 1,600 words, mostly by the exact power test. No Mac time, no rjob.

## Anti-pattern check
- **No mixing of D kinds:** chain results are in their own table under D_path, and the reporting template has no column that combines them with T-002/T-003 area D.
- **Null model:** H1b separates "the dataset has structure" from "short words always overlap by chance".
- **D ≥ 1 is not L2:** stated in H2.
- **Novelty:** G2 on every L1 chain. A chain that reduces to one of its relators is not novel.

## Approval (owner, 2026-10-14)
- Approved as written, including H1b and the null models. VM only.
- **H4 deferred:** the tokenizer files (`bpe_tokenizer_challenge_*_20260317/18`) are not on the VM.
- **KB rule banks:** out of scope.
- **Validator:** reviews the D_path geometry claims ("a chain is a strip; |w̄| ≈ 2|y₀| + Σe_t; D_path → 1/mean exposure") together with the results, not before.
- **Placement:** new experiment type [[B25/Structured Constructions/_type|Structured Constructions]], also for T-018 and T-019 later.
- **Levels:** L2 and all D thresholds are read on the headline D ([[challenge-gen-success-metrics]]). D_path is not a headline D.
- **Added reporting for a possible PatternBoost follow-up:**
  - the conjugator (rotation-prefix) lengths each chain needs;
  - the token length of each chain in the PatternBoost factor stream: `[BOS] ([REL_i] ([CONJ_±k]+ | [CONJ_EMPTY]) [SEP])+ [EOS]` with one token per conjugator letter (unless BPE compresses it), against `n_positions` 512, and how many chains fit under `conj_len_max` 4.

## Deviations (2026-10-14, found while running)
1. **Loop rejection in the walk.** The first full walk cycled: from k = 6 on, |w̄| stayed at 20 letters while k grew. Every step returned to an earlier prefix word, a loop that loop erasure deletes. The best k = 60 chain had walk score 3.0 but N* = N*_P = 2 (D_path 0.10). The walk now rejects any step whose word equals an earlier prefix word of the chain, so the walk score k/|w̄| equals N*/|w̄|. Check: N* = N*_P = k on 720 chains (300 best plus best per k, both walks). The run with the original scoring is discarded.
2. **Dead ends kept out of the frontier.** A chain whose last cell has fewer than ℓ_min letters left for an outgoing piece cannot continue. Such chains are recorded as finalists but not kept in the beam. Without this the beam filled with 2-cell dead ends such as (ab)⁵ and stopped at k = 3.
3. **Finalists are the 200 best *distinct words*.** The 200 best chain entries share words and collapsed to 59, 41 and 36 distinct words in the three walks; a first evaluation on those is superseded. "200 best chains" is now read as the 200 best distinct words, plus the best per k, giving 203–204 finalists per walk.
5. **Extended novelty check for chains.** G2 checks only the relators a word uses (it was designed for T-002 random products). Chains use up to about 50 of them, and their reduced word can equal the class of another dataset relator. Such a word is reducer-equivalent to a single relator, a much cheaper certificate (owner caution (a)). Every L1 chain is therefore also checked against all 1,640 relator classes ("novel_all"). Proposed as the default for chain-type constructions.
4. **Exploratory walk E1 (not pre-registered).** Each step also requires the T-003 pool gate (screen-mode R₂.₅ nonempty and ≥ 0.5|w̄|), and 100 × beam candidates are rescored exactly per step instead of 8 × beam. Reason: the pre-registered walk produced no L1 word. E1 tests whether "no L1 chain exists" or "the walk did not look for L1". Reported separately below and labelled exploratory.

Code: b25 branch `21-t016-overlap-chaining` @ `75b426b` (local, not pushed), modules `overlaps.py`, `chains.py`, `eval_chains.py` and 5 tests. Built on main `11376b2`; the reducer (tcgraph `dd24bae` build) is identical to main's pin `aa0413e`, which differs only in a test file. Outputs: `~/Research/challenge-gen/runs/t016-20261014/` (local). Wall clock: overlaps 32 s for three sets; each walk 20–40 s; evaluation about 1 min.

## Results
**Status: inconclusive.** The pre-registered walk meets H2 only by the letter of G2: its 2 L1 words are both reducer-equivalent to an unused dataset relator. H3 is falsified. The exploratory walk E1 found certified L1 chain words that are novel under the extended check: 190 by the harness, **176 after Validator's corrections** (§ Validator review below). Every D below is a **path-length** D unless stated otherwise.

**Validator verdict (2026-10-14, [[2026-10-14-t016-overlap-chaining-review]]):**
- D_path is an **upper bound only, rejected as area**.
- All 50 words with D_path ≥ 1 compress to certificates of 4–8 cells (D_c ≤ 0.163).
- The chains are fans (rewriting paths of the tail), not ladders.
- The tables below are the pre-review numbers. The corrected counts are in § Validator review.

### Overlaps (steps 1–3)
Distinct-class pairs, one per class under swap and inversion: 672,400 per set. Overlap length |y| is in letters; θ = |y|/min(L).

| Set | Containment pairs | Median \|y\| | Max \|y\| | θ ≥ 0.2 | θ ≥ 0.3 | θ ≥ 0.4 | θ ≥ 0.5 | Max θ (non-containment) | Words power-free |
|---|---|---|---|---|---|---|---|---|---|
| Dataset | 9 | 11 | 92 | 305,616 | 174,885 | 73,259 | 12,330 | 0.976 (40 of 41) | 492 / 820 |
| N1 (power-free null) | 0 | 8 | 22 | 18,177 | 482 | 19 | 0 | 0.474 | 820 / 820 |
| N0 (random null) | 0 | 7 | 19 | 8,004 | 127 | 4 | 0 | 0.447 | 0 / 820 |

- **H1 holds.** Max θ = 0.976, far above 0.20.
- **H1b holds.** 174,885 dataset pairs with θ ≥ 0.3 against 482 for N1, a ratio of 363×; 1,377× against N0. The dataset relators share long pieces far beyond chance, consistent with their common Knuth–Bendix origin.
- **Positive control passed.** Exactly 9 containment pairs, matching the 9 decomposable words.
- **Side finding.** 328 of the 820 dataset words are not 2.5-power-free: they contain powers that the reducer rewrites without shortening. So the exact power test cannot certify most chain words; the reducer has to.
- **ℓ_min = 11** by the pre-registered 10× rule. The overlap graph at 11 covers about half of all pairs, so the walk finds junctions on the fly through an index of all cyclic 11-letter windows.

### Chains (steps 4–5)
200 best distinct words plus best per k per walk. "Novel": G2 / extended check against all 1,640 relator classes.

| Walk | Finalists | L0 | Certified L1 | Novel (G2 / all classes) | Max D_path, novel-all L1 | Novel-all L1 with D_path > 0.200 / ≥ 1 | Power-free | Fit of \|w̄\| against k (k ≥ 10) |
|---|---|---|---|---|---|---|---|---|
| Main (pre-registered) | 204 | 204 | **2** | 2 / **0** | — (G2-novel: 1.09) | 0 / 0 | 0 | 30.5 + 0.27 k |
| With containment steps | 203 | 203 | **0** | 0 / 0 | — | 0 / 0 | 0 | 20.8 + 0.05 k |
| **E1, screen-gated (exploratory)** | 203 | 203 | **197** | 196 / **190** | **1.43** | **189 / 50** | 0 | 35.1 + 0.15 k |

- **Main walk.** 202 of 204 finalists reduce to the empty word in screen mode: the high-D_path chains are short words that the reducer kills. The 2 L1 words (k = 60, |w̄| = 55, D_path 1.09, ρ_min16 0.58) are G2-novel, but R₂.₅(w) of each is the class of a dataset relator the chain does not use.
- **Containment walk.** All 203 reduce to the empty word.
- **E1.** 197 of 203 are certified L1, with ρ_min16 from 0.50 to 0.97. 190 are novel under the extended check: |w̄| from 34 to 64, k from 5 to 60, median D_path 0.97. The best is k = 60 cells on |w̄| = 42 letters, N* = N*_P = 60, D_path 1.43, ρ_min16 0.76, using 49 distinct relators. N* = N*_P on every chain in every walk: no Peiffer pairs.
- **Path-length signature (watch item (c)).** |w̄| grows by only 0.05–0.27 letters per cell, and a median of 23 of 60 cells have zero exposure. |w̄| is essentially bounded while N* grows: D_path measures the length of a rewriting path, not area.
- **Cheaper certificates (watch item (a)).** 7 of the 197 E1 L1 words, and both main-walk L1 words, are reducer-equivalent to a single dataset relator. For the other 190 no cheaper certificate is known, but none was searched for beyond this class check.
- **Level labels.** The harness labelled 52 E1 words (and both main-walk L1 words) "L2", because N*/|w̄| ≥ 1 on F*. By the owner's provenance rule of 2026-10-14 (below), chain words cap at **L1**. The output now shows `level` = L1, and the harness label is kept as `level_harness`. All tables in this note use the capped level.

Every certified chain word with D_path ≥ 0.2 (watch item) has N* = N*_P = k, so the table lists N*_P only. There are 194 such L1 words (189 novel-all). The 5 best, all k = 60 and all novel-all:

| \|w̄\| | N*_P | D_path | ρ_min16 | Distinct dataset relators |
|---|---|---|---|---|
| 42 | 60 | 1.429 | 0.76 | 49 |
| 43 | 60 | 1.395 | 0.74 | 51 |
| 50 | 60 | 1.200 | 0.64 | 48 |
| 51 | 60 | 1.176 | 0.63 | 51 |
| 53 | 60 | 1.132 | 0.60 | 53 |

All of them are listed in `walk_E1_screen/eval/summary.json` (`d_path_ge_0.2_words`), each with N*, N*_P, |w̄|, ρ_min16, novelty and its full relator list.

### Conjugators and PatternBoost stream length (owner item 7)
Conjugators are rotation prefixes, the shorter of R[:σ] and inv(R[σ:]), so their length is ≤ L/2 ≤ 61.

| Walk | Median conjugator length | Median / max longest conjugator per chain | Median token length | Chains ≤ 512 tokens | Chains with all conjugators ≤ 4 |
|---|---|---|---|---|---|
| Main | 15 | 23 / 27 | 970 | 4 / 204 | 0 |
| Containment | 15 | 27 / 27 | 1,026 | 3 / 203 | 0 |
| E1 | 14 | 28 / 29 | 956 | 3 / 203 | 1 |

A 60-cell chain needs about 950 stream tokens: one per conjugator letter plus [REL] and [SEP]. So `n_positions` 512 holds about 30 cells at this conjugator length, and `conj_len_max` 4 would allow almost none of these chains. A PatternBoost follow-up would need conjugators up to about 30 letters, and BPE or a rotation token (store σ instead of the letters) to fit the stream.

### Hypotheses
- **H1 holds** and **H1b holds**, by 363×.
- **H2 holds only by the letter of G2.** The main walk has 2 G2-novel certified L1 chains with D_path 1.09, but both are reducer-equivalent to an unused dataset relator; under the extended check, 0. **Exploratory E1:** 189 novel-all L1 chains with D_path > 0.200, 50 with D_path ≥ 1, max 1.43. This is path length, not area. Pending Validator.
- **H3 falsified:** 0% of finalists are power-free in any walk, against 80% predicted. This cannot be attributed to junctions alone: the dataset relators themselves are only 60% power-free.
- **H4 deferred.**
- **H5 holds:** L0 610/610.

### For Validator (with these results, owner decision 2026-10-14)
1. The D_path geometry: a chain is a strip of cells; |w̄| ≈ 2|y₀| + Σ e_t; D_path → 1/mean exposure. Data: |w̄| slope 0.05–0.27 letters per cell.
2. Do E1 words with N*_P ≥ |w̄| admit much cheaper certificates over the dataset relators? Probe: 7 of 197 L1 words reduce to the class of an unused dataset relator. Any area-type statement about them needs this answered.
3. All 610 L0 certificates are checked by the independent harness. By the T-003 rule, any harness-"L2" word gets an independent L0 re-check before any claim; Validator may re-check a sample of the 52.

Files for Validator (local VM, `~/Research/challenge-gen/runs/t016-20261014/`):
- `walk_E1_screen/eval/chains_results.jsonl`: per word, level, ρ_min16, N*, N*_P, D_path, cuts, exposures, conjugator lengths and relators.
- `walk_E1_screen/eval/samples/shard*/finalists.jsonl`: full certificates, i.e. relator indices, conjugators and word.
- `walk_E1_screen/eval/summary.json`.
- Overlaps: `overlaps/overlaps_summary.json`, plus `overlap_matrix_*.npy` and `words_*.json`.
- Dataset: `data/b25_trivial_2_5reduced_unique_aut8_20261014.txt` (sha-pinned in the harness).
- Code: b25 PR #12.

### Validator review and corrections (2026-10-14)
Source: [[2026-10-14-t016-overlap-chaining-review]] (+ [[2026-10-14-t016-overlap-chaining-review-triage]]). PR #12 was merged as b25 `ef86020` after the review.

1. **Geometry (validated as a description, with corrections).**
   - Σ e_t = |w̄| is a bookkeeping identity, not evidence of a geometry.
   - The words are literally rewriting paths of the tail: in the two best words the first 19 letters of P₁ survive in every prefix word, so w̄ = x₁·s_k.
   - **Fan, not ladder:** 189 of 190 words have cells with *negative* exposure (median 15 per word). "Strip" was approximate.
2. **D_path as area: rejected.** It is an upper bound only. The family has |w̄| ≤ 64, so its area is bounded by a constant, while D_path grows without bound along zero-exposure stretches.
3. **Cheaper certificates found.**
   - All 50 novel-all words with D_path ≥ 1 have certificates of **4–8 cells**, over the 1,640 dataset relators plus v⁵ with |v| ≤ 3, against N* = 48–60. Counts: 4 cells (8 words), 5 (12), 6 (22), 7 (5), 8 (3). So **D_c ≤ 0.163**, median 0.100, below the 0.200 bar.
   - The best word, **top-0** (|w̄| = 42, D_path 1.43), has a **5-cell certificate using dataset relators only**. The exhaustive ≤ 2-cell test brackets its area over the dataset relators at **3–5**.
   - Over the dataset relators, none of the top 76 words has a certificate of ≤ 2 cells (exhaustive for 20 ≤ |w̄| < 64).
4. **14 of the 190 novel-all words reduce to the empty word over {u⁵}, |u| ≤ 7,** by step-checked 2.5-rewriting paths of 10–21 cells. The cause is that the greedy reducer's move order reaches a dead end; it is not a missing rule.
   - IDs: E1_screen-top-2, -3, -30, -31, -41, -53, -59, -68, -87, -109, -144, -153, -154, -173.
   - **4 of the 7 harness "single relator class" hits also reduce to empty:** top-4, -6, -111, -134.
   - So E1 has **18 emptied L1 words**.
5. **L0 replicated** on all 52 words with harness D ≥ 1 (52/52).
6. **The all-classes check is correct but not sufficient** as a guard: it missed the 14. Validator proposes a stronger standard guard:
   - the non-increasing 2.5-closure contains neither ε nor a relator class;
   - there is no certificate with ≤ 2 cells over the table.
   - This is pending an owner decision, and the novelty threshold is not changed until then.

**Recount of E1 (run files updated 2026-10-14; originals kept as `*.orig`).** The 18 words are marked in `walk_E1_screen/eval/chains_results.jsonl`: `level` L0, `validator_empty_over_u5`, and `level_before_validator`. `summary.json` gets a `validator_correction` block, and the emptied words are removed from `d_path_ge_0.2_words`.

| E1 count | Harness | After Validator |
|---|---|---|
| Certified L1 | 197 | **179** |
| Novel-all L1 | 190 | **176** |
| Novel-all L1 with D_path > 0.200 | 189 | **175** |
| Novel-all L1 with D_path ≥ 1 | 50 | **44** |
| Max D_path, novel-all L1 | 1.43 | 1.43 (top-0, unaffected) |
| Best D_c of the D_path ≥ 1 words | — | ≤ 0.163 |

E1c and E1d are checked with Validator's closure script (`t016_more.py`, run unchanged by Experimenter 2026-10-14/15). Its enumerator self-test passed (0/300 mismatches). Re-run on the marked E1 file, it finds no further emptied word, which confirms Validator's 18.

**E1c recount** (run files marked the same way, originals kept as `*.orig`):
- 20 of 199 L1 words reduce to the empty word in their non-increasing closure: top-1, -2, -4, -5, -14, -16, -17, -36, -37, -41, -42, -53, -62, -84, -113, -153, -162, -165, -168, -186.
- 17 of them were novel-all, and 4 were harness relator-class hits.

| E1c count | Harness | After closure check |
|---|---|---|
| Certified L1 | 199 | **179** |
| Novel-all L1 | 194 | **177** |
| Novel-all L1 with D_path > 0.200 | 193 | **176** |
| Novel-all L1 with D_path ≥ 1 | 36 | **29** |
| Max D_path, novel-all L1 | 1.31 | 1.31 |

**Depth classes under the owner's area-like threshold (2026-10-14).** The threshold is N ≥ 16 and N_deep ≥ 2, besides T_deep ≥ 0.5 and T_depth ≥ 0.5; deep cells with N < 16 make a word "small enclosed". The wording is a placeholder while Math Expert's refinement is decided. Numbers are from Developer's T-023 stats (b25 `6f71817`, 1,684-entry table) on the compressed certificate; E1d was run by Experimenter with the same code and table.

| Walk | Finalists | N_deep > 0 | of which N_c ≥ 16 | N_deep ≥ 2 with N_c ≥ 16 | max maxdepth | Area-like (old T-023 label → new rule) |
|---|---|---|---|---|---|---|
| E1 | 203 | 10 | 0 | 0 | 1 | 1 → **0** (small enclosed) |
| E1c | 204 | 10 | 0 | 0 | 1 | 8 → **0** (small enclosed) |
| E1d | 204 | 46 | 7 | 0 | 1 | 20 → **0** (small enclosed or thick strip) |
| T-003 (7 runs, 2,256 words) | 2,256 | 2 (RD-C) | 0 | 0 | 1 | 0 → 0 |

No T-003 or T-016 word is area-like under the new rule, and none has maxdepth ≥ 2. The same holds under Math Expert's proposed refinement (a dual-connected deep core of ≥ 2 cells, or maxdepth ≥ 2), since no word has N_deep ≥ 2 with N ≥ 16 or maxdepth ≥ 2.

## Owner decisions on the results (2026-10-14)
1. **Provenance rule.** Chain-built words report D_path in its own column, never as headline D, and their level caps at L1 by construction. Implemented in `eval_chains.py` (`level` capped, `level_harness` kept) and recorded in [[challenge-gen-success-metrics]] and the glossary.
2. **Validator review**, requested by Lead: strip geometry, cheaper certificates, and an L0 re-check of a sample of the 52.
3. **The all-classes novelty check is standard for every construction**, next to G2 ([[challenge-gen-glossary#novel L1 and the guards G1 and G2]]).
4. **Code:** branch `21-t016-overlap-chaining` pushed; b25 **PR #12**, not merged (Lead merges after Validator).
5. **E1 confirmation:** pre-register E1 as written, then rerun it with a fresh seed and a fresh start set (addendum below).

## Addendum: E1 confirmation run E1c (pre-registered 2026-10-14, before running)
Pre-registers E1 as it was run, with **one change: the seed and the start set**.
- **Walk (unchanged from E1).** ℓ_min = 11, beam 200, k ≤ 60, loop rejection, dead ends kept out of the frontier, no containment steps, and 100 × beam candidates rescored exactly per step. Each step must pass both the gate |cyc(w̄)|/|w̄| ≥ 0.5 and the T-003 screen gate: screen-mode R₂.₅(w) nonempty and ≥ 0.5|w̄|.
- **Fresh seed:** 16000003, for tie-breaking and for drawing the start set.
- **Fresh start set.** All 116,836 (relator, rotation) start cells, minus the first cells of all 5,000 chains E1 kept (`walk_E1_screen/chains.jsonl`). From the rest, a uniform random 50% is drawn with seed 16000003.
- **Finalists and evaluation (unchanged).** The 200 best distinct words plus the best per k ∈ {2, 3, 5, 10, 20, 40, 60}, evaluated with the T-002 harness. Novelty is G2 plus the all-classes check, levels are capped at L1 (provenance rule), and D_path = N*_P/|w̄|.
- **Confirmation criteria (all three needed; otherwise E1 is not confirmed).** E1's values are in brackets.
  - (a) ≥ 75% of finalists are certified L1 [97%];
  - (b) ≥ 100 novel L1 words (G2 plus all-classes) with D_path > 0.200 [189];
  - (c) ≥ 1 novel L1 word with D_path ≥ 1 [50].
- **Reported:** the same table as E1, plus the |w̄|-against-k fit, conjugator and token lengths, and every D_path ≥ 0.2 word in `summary.json`.
- **Cost:** about 2 minutes on the VM.

### E1c results (2026-10-14)
Run from b25 `b9bfc18` (PR #12). Start cells: 116,836, minus 1 excluded, so 58,418 used.

| Walk | Finalists | L0 | Certified L1 | Novel (G2 / all classes) | Max D_path, novel-all L1 | Novel-all L1 with D_path > 0.200 / ≥ 1 | Power-free | Fit of \|w̄\| against k (k ≥ 10) |
|---|---|---|---|---|---|---|---|---|
| E1 (exploratory) | 203 | 203 | 197 (97%) | 196 / 190 | 1.43 | 189 / 50 | 0 | 35.1 + 0.15 k |
| **E1c (confirmation)** | 204 | 204 | **199 (98%)** | 198 / **194** | **1.31** | **193 / 36** | 0 | 33.1 + 0.26 k |

- **E1 confirmed:** (a) 98% ≥ 75%, (b) 193 ≥ 100, (c) 36 ≥ 1.
- **E1c details.** ρ_min16 0.50–0.97. Novel-all words have |w̄| from 34 to 64 and median D_path 0.95. The best is k = 55, |w̄| = 42, D_path 1.31, ρ 0.76, 47 distinct relators. N* = N*_P everywhere.
- **Conjugators and tokens (E1c).** Median conjugator length 14; median longest conjugator per chain 27 (max 33); median 949 stream tokens. 4 of 204 chains fit in 512 tokens, and 1 has all conjugators ≤ 4.
- **Labels.** 38 harness "L2" labels capped to L1.
- **Caveat on independence.** In each walk, all 5,000 kept chains descend from **one** start: the beam collapses onto a single lineage, with the same first two cells throughout. The excluded set was therefore a single cell, and E1c started from a different relator (250, against 267 in E1). The two lineages then converge on a shared region: the top lists share 356 words and 389 of about 450 relators. E1c replicates the result from a different start and seed, but it is not an independent sample of chain space. A diversity-preserving walk (one beam per start relator, or a per-lineage cap) would be the natural next test.

## Addendum: diverse-lineage walk E1d (owner-approved, pre-registered 2026-10-14, before running)
**Terms.** The *lineage* of a chain is its start relator: the table index of its first cell. The *lineage cap* m is the most states one lineage may hold in the beam at any step.
- **Walk:** as E1c (ℓ_min 11, beam 200, k ≤ 60, loop rejection, |cyc|/|w̄| gate, screen gate, 100 × beam candidates rescored per step, no containment steps), with these changes:
  - seed 16000004;
  - all 116,836 start cells;
  - **lineage cap m = 5**, so each step's beam holds at least 40 lineages;
  - the walk keeps the best 20,000 chains (instead of 5,000) so that finalist selection can be diverse.
- **Finalists:** the 200 best distinct words with **at most 10 per lineage**, plus the best per k ∈ {2, 3, 5, 10, 20, 40, 60}. Evaluation, novelty (G2 + all classes), the L1 cap and D_path as in E1c.
- **Criteria.** (a)–(c) as for E1c: ≥ 75% certified L1; ≥ 100 novel L1 with D_path > 0.200; ≥ 1 novel L1 with D_path ≥ 1. Plus **(d) diversity:** the novel L1 words with D_path > 0.200 come from ≥ 20 lineages, use ≥ 300 distinct relators, and no lineage supplies more than 10% of them. If (d) fails, the E1 result is a property of a few lineages; if (a)–(c) fail with (d) met, the high-D_path region is narrow.
- **Reported:** the E1c table, plus lineage count, relators used, the largest lineage share, and word overlap with E1 and E1c.

### E1d results (2026-10-14)
Run from branch 21 with the lineage options; the code is identical to `e0f5f7a` (PR #12). The walk took 298 s and kept 20,000 chains from 26 lineages.

| Walk | Finalists | Certified L1 | Novel (G2 / all classes) | Max D_path, novel-all L1 | Novel-all L1 with D_path > 0.200 / ≥ 1 | Lineages / distinct relators / largest lineage share (novel-all, D_path > 0.2) | Fit of \|w̄\| against k |
|---|---|---|---|---|---|---|---|
| E1 | 203 | 197 | 196 / 190 | 1.43 | 189 / 50 | 1 / — / 100% | 35.1 + 0.15 k |
| E1c | 204 | 199 | 198 / 194 | 1.31 | 193 / 36 | 1 / — / 100% | 33.1 + 0.26 k |
| **E1d (lineage cap 5)** | 204 | **201 (98.5%)** | 199 / **176** | **0.92** | **175 / 0** | **23 / 336 / 5.7%** | 40.2 + 0.42 k |

- **Criteria:** (a) met (98.5%); (b) met (175); **(c) not met** (0 words with D_path ≥ 1; max 0.92); (d) met (23 lineages, 336 relators, largest share 5.7%).
- **Verdict by the pre-registered reading:** "the high-D_path region is narrow". D_path ≥ 1 needs a beam concentrated on one lineage, which follows long zero-exposure stretches. Diverse chains still give certified, novel L1 words with D_path well above 0.2 (median 0.64), on longer words: |w̄| from 61 to 112, k from 33 to 60.
- **Overlap with earlier walks:** E1d shares no word with the kept lists of E1 or E1c. Lineage 250 (E1c's start) appears, but capped.
- **Best words:** k = 57, |w̄| = 62, D_path 0.92, ρ_min16 0.52, lineage 1070. Lineage 250 gives D_path 0.88 at k = 60, |w̄| = 68, ρ_min16 0.91.
- **Standard guard applied to the 175 E1d candidates** (owner decision 2026-10-14; novel-all L1 with D_path > 0.2):
  - **(i) Non-increasing 2.5-closure** (Validator's `t016_more.py`, unchanged): PENDING. The closures of these longer words (|w̄| 61–112) take more than 30 min in total, and the run is still going (output `walk_E1d/eval/guard_closure.out`).
  - **(ii) ≤ 2-cell certificate over the 1,640 dataset relators: 0 of 175 have one.**
    - Validator's shared-arc test (`t016_cheap.py`) finds none in 175/175 (`guard_cheap_le2.out`). It is exhaustive by itself only for |w̄| < 64 (3 words).
    - For |w̄| ≥ 64, two cells meeting at a vertex or joined by a stem (w = c X c⁻¹ Y cyclically) are tested by Experimenter's scratch check (`le2_vertex_stem.py`, positive control 300/300 planted words). Hits: 0 of 175 (`guard_le2_vertex_stem.out`).
    - The two tests together cover the 2-cell cases (arc, vertex, stem); Validator to confirm the case split.
    - Validator's heuristic depth-2 extension found a **3-cell** certificate for one candidate, top-192 (|w̄| 61, N* 33).
  - **(iii) N*_c** (T-023, 1,684-entry table): candidates' median N*_c is 13; D_c max 0.219, median 0.144.
- **Candidate benchmark set: ON HOLD** until the owner decides the guard question (Validator proposes a stronger standard guard; [[2026-10-14-t016-overlap-chaining-review]] claim 4). The text below predates the review. **Previous note (owner, 2026-10-14; no action yet).** The 175 certified, novel (G2 + all classes) E1d L1 words with D_path > 0.2 are diverse: 23 lineages, 336 relators. They are noted as a candidate benchmark set of path-like hard words, in `walk_E1d/eval/chains_results.jsonl` and `summary.json` (`d_path_ge_0.2_words`).
- **Path-length signature unchanged.** |w̄| grows by 0.42 letters per cell, and a median of 25 cells have zero exposure. Conjugators: median 15, max 31; median 977 tokens; 5 of 204 chains fit in 512 tokens.

## Addendum: triangle census (owner-approved, pre-registered 2026-10-14, before running)
Source: Math Expert, [[2026-10-14-area-vs-path-criterion]], triangle census section. Purpose: decide whether T-022 (a search with an area-type objective) has anything to start from.

**Terms.**
- **Dual graph** of a van Kampen diagram: one node per cell, one edge per maximal path shared by two cells. A chain's dual graph is a path, a tree with b₁ = 0, where **b₁** (cycle rank) = edges − nodes + 1.
- **Corner (C, p).** A cyclic relator word C (one of the 1,640) and a position p between two of its letters. From p it has two **rays** read outward from p: out(C, p) = C[p] C[p+1] …, and in(C, p) = C[p−1]⁻¹ C[p−2]⁻¹ …, the letters before p inverted and read backwards.
- **Triangle.** Three corners (C₁, p₁), (C₂, p₂), (C₃, p₃) whose rays agree pairwise on at least ℓ letters: out(C₁) with in(C₂), out(C₂) with in(C₃), and out(C₃) with in(C₁). Here ℓ = ℓ_min = 11 (the T-016 rule).
  - Geometrically, the three cells meet at one interior vertex, and each adjacent pair shares an edge of length ≥ ℓ, with labels x₁, x₂, x₃ read outward from the vertex. Then C₁ ⊇ x₁⁻¹x₂, C₂ ⊇ x₂⁻¹x₃ and C₃ ⊇ x₃⁻¹x₁.
  - This is the smallest configuration whose dual graph has a cycle (b₁ = 1).
  - Adjacent cells must be distinct classes (C_{i+1} ≠ C_i⁻¹, which would be a cancelling pair). Relators may otherwise repeat.
- **Corner graph.** Nodes are ℓ-letter words. Each corner is a directed edge from the first ℓ letters of in(C, p) to the first ℓ letters of out(C, p). Triangles are exactly the directed 3-cycles of this multigraph.
- **Counts.**
  - **T_raw:** directed 3-cycles divided by 3 (the rotation of (C₁, C₂, C₃)).
  - **T_class:** distinct unordered sets of relator classes {C₁, C₂, C₃} up to inversion, reported for all triples and for triples of three distinct classes.
  - The maximal edge lengths |x_i| are reported as a distribution.
- **Baselines.**
  - (i) The power-free null **N1** (seed 16000002, same code).
  - (ii) The **configuration model**: the dataset's corner graph with out-keys shuffled among corners (in-keys and out-key multiset fixed), so the pairwise overlap frequency is kept but corner alignment is random. 5 shuffles, seeds 16000011–15. This baseline isolates "three pieces meet at one vertex" from "the relators overlap a lot".

**Hypothesis TC (Math Expert's sphere conjecture, as a prediction).** Knuth–Bendix-derived relators form 3-cell *spheres* rather than triangles around a vertex, so the dataset's T_raw is at most the configuration-model mean. **Falsified** if the dataset T_raw exceeds the configuration-model mean by more than 3 standard deviations and by a factor ≥ 2.

**Decision rule for T-022 (recommendation to Lead).** T-022 is worth doing if the dataset has ≥ 100 distinct-class triangles (T_class with three distinct classes) **and** TC is falsified (triangles enriched beyond pair frequency). If triangles exist but are not enriched, report "possible but not favoured". If T_class = 0, T-022 has no seed over the 820, which points to idea 2 (|u| ≤ 7).

**Cost:** minutes on the VM. Code: `experiments/challenge_gen/t016/triangles.py` on branch 21 (added to PR #12).

### Triangle census results (2026-10-14)
Code `e0f5f7a` (PR #12). ℓ = 11, 116,836 corners per set, 5 s per set. Output: `~/Research/challenge-gen/runs/t016-20261014/triangles/triangles.json`, including 10 dataset examples with cells, positions and words.

| Set | T_raw | T_class | Three distinct classes | Relators in some triangle | Min shared edge per triangle (median / max) |
|---|---|---|---|---|---|
| **Dataset** | **9,136** | 4,383 | **4,379** | 759 of 820 | 12 / 36 |
| N1 (power-free null) | 2 | 1 | 1 | 3 | 11 / 11 |
| N0 (random null) | 0 | 0 | 0 | 0 | — |
| Configuration model (mean ± sd of 5) | **355,261 ± 12,097** | about 350,000 | about 350,000 | 820 | — |

- **Triangles exist and are not chance.** The dataset has 4,379 distinct-class triples around a vertex, against 1 in N1, and they involve 759 of the 820 relators. The most frequent relator class, index 240, appears in 1,950 triangle class-triples.
- **But they are strongly depleted relative to the dataset's own pairwise overlaps:** 9,136 against 355,261 ± 12,097 when corner alignment is randomised, 39× fewer and 28 sd below. Corners give the same long pieces, but those pieces rarely meet at a common vertex.
- **The sphere conjecture (TC) is not falsified;** the data supports it. KB-derived relators overlap in ways that close up as 3-cell spheres or rewriting paths, not as triangles around an interior vertex.
- **Baseline caveat.** The configuration model shuffles out-keys, which creates about 30,000 invalid corners (rays starting with inverse letters, i.e. not reduced). These are skipped. Before this fix the baseline mean was about 977,000; the conclusion holds either way.
- **Example triangle:** cells S[3], S[864] (inverse of dataset word 45) and S[141], at positions 12, 16 and 31. Their lengths are 38, 52 and 57, and each pair shares an edge of ≥ 11 letters.
- **T-022 decision by the pre-registered rule: "possible but not favoured".** There are 4,379 ≥ 100 distinct-class triangles, so a search over b₁ ≥ 1 configurations has seeds over the 820. But triangles are depleted 39× against pair frequency, so the dataset does not favour area-type gluing. A b₁ > 0 search would fight the relators' structure. Math Expert's idea 2 (|u| ≤ 7 standard relators) is the alternative the rule points to when triangles are not favoured.

## Related material
- [[2026-10-14-cancellation-constructions]] (idea 1)
- [[project-challenge-gen]] § Cautions on D
- [[challenge-gen-success-metrics]] · [[challenge-gen-glossary]]
- [[t002-dataset-relator-products-2026-10-14]] (harness and relator table)
- [[t003-gated-dehn-search-2026-10-14]] (area-D bar 0.200; best R-D area D 0.083)
- [[b25-challenge-token-analysis-results]] (T-006 tokens)
- [[ds-b25-trivial-2-5reduced-aut8-20261014]]

Verified by [[2026-10-14-t016-overlap-chaining-review]] and [[2026-10-14-t023-folded-diagram-review]]
