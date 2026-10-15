---
title: "T-016 overlap chaining — review of results"
status: validated
domain: group-theory
project: challenge-gen
claim: "E1 chain words: D_path is path length, not area; cheaper certificates; L0 of the D_path ≥ 1 words; all-classes novelty guard"
claimant: Experimenter (via Lead)
verification_method: "bookkeeping + finite-family argument; exhaustive area ≤ 2 test over the 1,640 dataset relators; step-checked 2.5-rewriting over {u⁵} with full non-increasing closure; independent re-expansion"
tools_used: ["python3 3.12.3 (own scripts scratch/t016_*.py, t001_search.py, t001_trace.py)", "producer: b25 21-t016-overlap-chaining @ 75b426b, tcgraph dd24bae reducer (read as data only)"]
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, topic/proof-certificates, topic/dehn-function, project/challenge-gen, status/validated, proof]
---

# Review — T-016 overlap chaining (E1)
Triage: [[2026-10-14-t016-overlap-chaining-review-triage]]. Source: [[t016-overlap-chaining-2026-10-14]] § Results. Group: free B(2,5). Words and certificates from `runs/t016-20261014/walk_E1_screen/eval/`.

**Terms.**
- P_t is the prefix word after t cells.
- e_t, the *exposure* of cell t, is the change |P_t| − |P_{t−1}| (the harness definition).
- The *non-increasing closure* of w is the set of cyclic words reachable from w by 2.5-moves that do not lengthen the word, shortening or length-neutral. A 2.5-move replaces v^p by v^{p−5}, with p ≥ 2.5. Each move is one cell u⁵ and is sound in free B(2,5) (lemma in [[2026-10-14-t001-l0-soundness-and-words-13-14]]).
- "Area over R" is the minimal number of cells from R.

## Claim 1 — strip geometry: VALIDATED (description), with corrections
- **Σ e_t = |w̄| on 190/190 words, but this is a tautology:** exposure is defined as the change in prefix length. "|w̄| ≈ 2|y₀| + Σ e_t" is the same identity relabelled, not evidence of a geometry.
- **Rewriting path, literally.** In the two best words, the first 19 letters of P₁ survive in every P_t, while |P_t| stays at 34–62 (median 59). So w̄ = x₁·s_k: each cell rewrites the tail s_{t−1} → s_t. This is the content of "w ≈ x₁ x_{k+1}⁻¹".
- **Correction: a fan, not a ladder.** 189/190 words have cells with *negative* exposure (median 15 per word), i.e. a cell cancels past the previous cell's exposed letters. "Strip" is approximate; "rewriting path of the tail with bounded |w̄|" is accurate. The median of 23/60 zero-exposure cells is confirmed.
- **D_path as area: no.**
  - (a) N*/|w̄| bounds area/|w̄| from above for any certificate, and no better.
  - (b) The family has |w̄| ≤ 64. Only finitely many words have length ≤ 64, and each member of the family has a finite certificate (its chain), so area is bounded by a constant on the family, while D_path → ∞ as k grows with exposure 0. Growth of D_path along a chain therefore cannot reflect growth of area. This is the finite-words argument of [[2026-10-14-t020-peiffer-loophole]] claim 3, applied locally.
  - (c) Concretely, see claim 2: 14 of the words have ≤ 21 cells against N* = 60.

## Claim 2 — cheaper certificates: FOUND for all 50 D_path ≥ 1 words (4–8 cells), and for 14/190 over {u⁵} alone
- **Relator-closure compression (my own implementation, cross-checking T-023's N*_c): every one of the 50 novel-all words with D_path ≥ 1 has a certificate of 4–8 cells** over R = the 1,640 dataset relators plus all v⁵ with |v| ≤ 3, against N* = 48–60. The counts: 4 cells (8 words), 5 (12), 6 (22), 7 (5), 8 (3). D_c = N*_c/|w| is at most 0.163, median 0.100. 26 of the 50 use at least one v⁵ cell.
  - Method: contiguous blocks of the chain whose free product is conjugate *in the free group* to a relator of R are replaced by that one factor (dynamic programming over all blocks, iterated). Every result re-expands to w exactly.
  - The best word, top-0 (|w| = 42, D_path 1.43), has a **5-cell certificate using dataset relators only**.
  - With my exhaustive ≤ 2-cell test this brackets its area over the dataset relators at 3–5.
  - T-023's E1c top-0 (55 → 7, all dataset cells) is replicated exactly.
- **Over {u⁵}: 14 of the 190 novel-all certified L1 words reduce to the empty word in 10–21 step-checked cells, all with |u| ≤ 7.** Every step was re-verified by `check_step` (string identity sub + complement = v⁵). 6 of the 14 have D_path ≥ 1.
  - In 11 of the 14 traces every move strictly shortens the word, so even a strictly shortening path exists that the harness's greedy reducer did not take.
  - **Order dependence, not a rule gap (tested):** on top-2 the tcgraph reducer returns, in all 16 images, a 32-letter word with no legal 2.5-move at all (my enumerator finds 0). My path reaches a *different* 32-letter word at step 5, which the reducer itself reduces to ε in all 16 images. The greedy reducer is correct per move but takes a dead-end order. This also supports, without proving, the T-001 neutral-move explanation.
  - IDs (cells / N*): top-2 (10/60), top-3 (11/60), top-30 (15/60), top-31 (11/50), top-41 (14/60), top-53 (13/60), top-68 (14/60), top-59 (14/60), top-87 (11/48), top-109 (15/60), top-144 (14/60), top-154 (15/60), top-153 (21/60), top-173 (17/60). All carry the `T016-E1_screen-` prefix.
  - Example, top-2 (|w| = 50, ρ_min16 0.64, harness D_path 1.20): (baa)^{13/3} → AA, (AA)³ → a⁴, (aaB)³ → bAAbAA, a³ → A², A³ → a², (bAAbaa)^{19/6} → AABaaBAABaa, A⁵ → ε, a³ → A², (AAB)⁴ → baa, a⁵ → ε. Lengths 50, 39, 37, 34, 33, 32, 24, 17, 16, 5, 0.
  - Also: 4 of the 7 words the harness classed as "a single relator class" reduce to the empty word too, so they are not even one relator.
- **The other 176 (including the best, top-0, |w| = 42, D_path 1.43) are stronger than the harness says.** Their full non-increasing closure has ≤ 228 states (cap 20,000, never reached) and contains neither ε nor any of the 1,640 relator classes (up to rotation, inversion and the 8 automorphisms). So no sequence of non-lengthening 2.5-moves certifies them. The move enumerator was checked complete against brute force (0/300 mismatches). This is a statement about 2.5-rewriting, not about area: certificates that pass through longer words are not excluded.
- **Over the 1,640 dataset relators: no certificate with ≤ 2 cells for any of the top 76 words by D_path** (this includes all 50 with D_path ≥ 1). The test is exhaustive for 20 ≤ |w| < 64. Two cells meeting only at a vertex or joined by a stem would need |w| ≥ 32 + 32, so the cells share one arc, one boundary piece of ≥ ⌈|w|/2⌉ letters lies on one cell, and it is found through a 10-letter prefix index (hence |w| ≥ 20). Positive control: 2,639/2,639 planted 2-cell words with 20 ≤ |w| < 64 detected. The remaining 114 words were not run: the compression above makes them moot. A depth-2 extension (heuristic, not exhaustive) found no 3-cell certificate either. So the area over the dataset relators of the D_path ≥ 1 words is ≥ 3 and otherwise unknown.
- Do not read the {u⁵} cell counts as area over the dataset relators: D depends on R ([[project-challenge-gen]] § Cautions on D).
- Lead also reports Developer's T-023 compression of the best E1c word, 55 → 7 cells. It is reviewed in the T-023 note.

## Claim 3 — L0 on the D_path ≥ 1 words: REPLICATED (all 52, not a sample)
Own code: the table was rebuilt from the dataset file (sha256 e0eeb777…, lines 1–820, inverses 821–1640). Each factor c⁻¹ r c was expanded and free-reduced. The result equals the stored word, |w| matches, and abelianization ≡ 0 mod 5 on **52/52**. I did not reproduce the table hash `fd1a6fed…`; word equality on all 52 makes that check redundant. Triviality in free B(2,5) is conditional on the dataset's kbprog proof of its relators.

## Claim 4 — all-classes novelty check: CORRECT for its definition, NOT SUFFICIENT as a standard guard
- **Implementation:** canon(R₂.₅(w)) is compared with the canon of all 1,640 relators, under rotation, inversion and the 8 letter automorphisms (`canon` over 16 images). Matching up to automorphism is conservative, which is fine for novelty.
  - It fails open: a reducer status ≠ ok counts as novel. This never happened here (0 null fields over 197 L1 words). Make it fail closed.
  - It compares R₂.₅(w) with the raw relator, not with R₂.₅(relator). That is correct only while every dataset word is a reducer fixed point (true for the 2026-10-14 dataset per T-001).
- **Re-check by an independent route:** the non-increasing closure of all 197 L1 words reproduces all 7 harness hits and adds 14, exactly the 14 emptied words above. So the guard missed 14 because the greedy reducer is order-dependent.
- **Not sufficient:** it detects only "one relator plus reducer cells" along the greedy path. It misses (i) relator classes reachable by another move order (14 here), (ii) multi-cell certificates over the table.
- **Recommended standard guard for chain-type and other constructed words:** (1) the non-increasing closure contains neither ε nor a relator class (≤ 228 states here, under 1 s per word); (2) no certificate with ≤ 2 cells over the relator table (about 1–18 s per word, exhaustive for |w| < 64). Both as cheap screens, reported as "no cheaper certificate found by these tests", never as an area statement.

## Verdict
| Claim | Status |
|---|---|
| 1 rewriting-path description | validated (bookkeeping is a tautology; fan, not ladder) |
| 1 D_path says anything about area | rejected (upper bound only; bounded-|w| family) |
| 2 "no cheaper certificate" | disproven: all 50 D_path ≥ 1 words have 4–8-cell certificates (D_c ≤ 0.163); 14/190 empty over {u⁵} in 10–21 cells; no ≤ 2-cell certificate over the dataset relators for the top 76 |
| 3 L0, 52 D_path ≥ 1 words | replicated, 52/52 |
| 4 all-classes check | correct; insufficient as a guard (missed 14) |

Under the compressed certificates none of the 50 D_path ≥ 1 words has D_c above 0.163 (T-003 area-D bar 0.200); T-023 reports best D_c 0.172 over all E1c finalists (see the T-023 note). Recount without the 14 emptied words: novel-all certified L1 190 → **176**; D_path > 0.200: 189 → **175**; D_path ≥ 1: 50 → **44**. The best word, top-0 (D_path 1.43), is unaffected.
