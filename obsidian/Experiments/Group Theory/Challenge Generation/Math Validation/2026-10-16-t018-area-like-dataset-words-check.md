---
title: "T-018: the 7 area-like power-free dataset words — independent check"
status: replicated
domain: group-theory
project: challenge-gen
claim: "Dataset lines 36, 17, 47, 13, 21, 49, 48 are cyclically power-free, have R7 certificates with N*_c 33-56, maxdepth 2, and are area-like (Experimenter, seeds_power_free_len_le53.jsonl @ 4ceb3d7)"
claimant: Experimenter
verification_method: "independent L0 (own kbmag parse, own core table, own expansion); reproduction with main 714caa9; own non-contiguous subset-merge compression (|S| <= 4) alternated with closure_fixpoint; depth by 714caa9 diagram code and by own vertex peeling"
tools_used: ["t018 venv python -S on extracted main 714caa9", "scratch/area7/area7.py", "capjob 2G / 1 CPU (one job)"]
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, topic/van-kampen, topic/proof-certificates, project/challenge-gen, status/replicated, proof]
---

# Check — 7 area-like power-free dataset words (Lead request 2026-10-16)
Source: [[t018-t021-diagram-search-2026-10-14]] § Finding: power-free dataset words with R7 certificates. Scripts and best certificates: `Agents/asetlearning/Validator/scratch/area7/` (`best_line<L>.json`, `runall.out`).

**Terms.** *R7* = the 815 relators of `b25_full` (sha b1d511fe…) and their inverses. A *certificate* is a list of cells (k, c) whose product of c⁻¹R_k c freely reduces to w; its length N is an **upper bound** on the area of w. *N\*_c* is the length after the Developer's compression; *D_c* = N\*_c/|w|. *L0* = the certificate expands exactly to the word. *maxdepth* is the vertex-peeling depth on the folded diagram of one certificate.

## Verdict
| Item | Status |
|---|---|
| (1) L0 for all 7 over R7 | **replicated**: own parse (1,630 entries; core sha de1eb091796e), own expansion; each word is a rotation/inverse of its dataset line |
| Triviality | every R7 core is u^(5k), so these certificates prove w = 1 in the **free** Burnside group B(2,5), not only in B₀(2,5) |
| Experimenter's statistics | **reproduced exactly** on main 714caa9 (all 13 fields, all 7 words) |
| (2) cheaper certificates | found for **5 of 7**; best N below |
| (3) area-like label | survives for **6 of 7**; **line 47 drops to thick strip** (maxdepth 1) on a cheaper certificate |

| line | \|w\| | N_raw | N\*_c (Exp.) | best N (mine) | D_c best | N_deep | maxdepth | class (best) |
|---|---|---|---|---|---|---|---|---|
| 36 | 51 | 99 | 33 | 33 | 0.65 | 14 | 2 | area-like |
| 17 | 46 | 98 | 34 | **28** | 0.61 | 8 | 2 | area-like |
| 47 | 52 | 144 | 40 | **24** | 0.46 | 9 | **1** | **thick strip** |
| 13 | 42 | 113 | 41 | **38** | 0.90 | 25 | 2 | area-like |
| 21 | 47 | 108 | 42 | 42 | 0.89 | 18 | 2 | area-like |
| 49 | 52 | 144 | 49 | **45** | 0.87 | 16 | 2 | area-like |
| 48 | 52 | 98 | 56 | **55** | 1.06 | 29 | **3** | area-like |

Own vertex peeling agrees with the 714caa9 depth on every best certificate (N_deep, maxdepth).

## Method for (2)
The Developer's compression merges only *contiguous* blocks of the product. Mine merges any subset S (|S| ≤ 4) of cells, anywhere in the product: if the ordered product of S is conjugate to a table relator (or trivial), move the members of S together (each element they pass gets conjugated, so it stays a cell) and replace them by one cell (or none). Every step is checked by re-expansion. Merges alternate with both `closure_fixpoint` variants, keeping the smallest. Merges found: 3-cell merges dominate (line 47: three successive 3→1 merges, 40 → 24). The search is not exhaustive (subsets ≤ 4, greedy order, one starting certificate), so **best N is still only an upper bound**, and the true area may be smaller for all 7.

## Reading
- That the 7 words are trivial in B(2,5) with explicit certificates, and power-free, is solid.
- "Area-like" is a property of a certificate, not of the word: 1 of 7 loses it under a cheap local improvement, and D_c dropped by up to 40 % (line 47). The other six keep maxdepth ≥ 2 on the best certificate I found; line 48 even reaches maxdepth 3 and D_c 1.06.
- So a statement may say "certificates with maxdepth 2 exist for 6 words (lines 36, 17, 13, 21, 49, 48)", but not that their area is quadratic or that their diagrams are area-like; and line 47 should not be listed as area-like.

## Part 2 — the novel T-018 smoke finalists (H4 rule; Lead request 2026-10-16)
Source: Experimenter smoke run, branch t018-diagram-search @ 281e8d2, `data/smoke15/finalists.jsonl` (sha prefix d2e90fa5). **The certificates are not committed.** I took them from the Experimenter's local run output `smoke15/states.jsonl` (copied to `scratch/area7/smoke15_states.jsonl`, sha prefix 489d43ed), matching each finalist by lineage, step and exact word. States are over the raw R7 table; I converted them to cyclic cores myself (conjugator q⁻¹c). Script `scratch/area7/area_smoke.py`, output `smoke.out` (capjob 2G, one job).

| finalist | \|w\| | N (state = N\*_c) | best N (mine) | D_c best | N_deep | maxdepth | class (best) |
|---|---|---|---|---|---|---|---|
| L51 step 9 | 51 | 37 | 37 | 0.73 | 12 | 2 | area-like |
| L51 step 10 | 53 | 39 | 39 | 0.74 | 12 | 2 | area-like |
| L48 step 4 | 55 | 64 | **63** | **1.15** | 36 | **3** | area-like |
| L48 step 5 | 57 | 66 | **65** | **1.14** | 38 | **3** | area-like |

For all four:
- L0 holds over the raw R7 table and over the core table.
- My checks confirm cyclically power-free (own naive test) and novel (no rotation of the word or its inverse equals a dataset word).
- The Experimenter's statistics reproduce exactly on 714caa9.
- My own peeling agrees with the depth code.

**Verdicts.**
- **L51 steps 9 and 10 (the H2 candidate): replicated, with an upper-bound caveat.** No cheaper certificate was found (subset merges ≤ 4, both closure variants), so maxdepth 2 and the area-like label survive this search. That is not a proof that every certificate of these words has depth ≥ 2: the area and the depth of a minimal diagram are unknown. For H2 this supports "a certificate with maxdepth 2 exists for a novel, power-free, L0-certified word grown from a non-area-like seed". It does not support "the word has quadratic area".
- **L48 steps 4 and 5 (H4, D_c ≥ 1): D_c ≥ 1 is not established as a property of the words.** A cheaper certificate exists (one 2-cell merge each), and D_c stays above 1 (1.15, 1.14) on it. But my search is shallow, and the Experimenter's observation is a strong warning that these certificates are not minimal: the greedy adds about 2 cells per step while the boundary stays nearly constant. As an upper bound D_c is real; as evidence of area ≥ |w| it is nothing. Maxdepth 3 on the improved certificate is likewise a property of that certificate.
- **Provenance gap:** the finalists' certificates should be committed (or registered) with the smoke data; right now the claims rest on an uncommitted `/tmp` file.

## Part 3 — strict depth (|v| = 1 cells as trivial), Lead request 2026-10-16
Definition checked: [[2026-10-16-junction-repair-rule]] §7 R3. Script `scratch/area7/strict.py`, output `strict.out`. I used my best certificates, the 714caa9 fold and my own peeling (capjob, one job). A cell's root length is the minimal period of its core (so a¹⁰ counts as |v| = 1).

**Well-posedness: proved.** The absorbed set is the least fixed point of the monotone map A ↦ {|v| = 1 cells touching ∂Δ ∪ vertices(A)}. Each pass adds at least one cell or stops, so it terminates in at most N passes, and every fair order reaches the same least fixed point. Checked: 20 random orders per certificate give identical sets. After absorption the usual peeling is deterministic. **But "touching" must be fixed.** With vertex contact (consistent with vertex peeling) and with edge contact the results differ: for line 51, strict maxdepth is 0 versus 1.

| certificate | N | N_≥2 | D_c | D_c,≥2 | maxdepth | strict maxdepth (vertex / edge) | strict N_deep (vertex) | strict T_deep | strict deep roots |
|---|---|---|---|---|---|---|---|---|---|
| **L51 step 9 (H2)** | 37 | 23 | 0.73 | 0.45 | 2 | **0 / 1** | 0 | 0 | — |
| **L51 step 10** | 39 | 24 | 0.74 | 0.45 | 2 | **0 / 1** | 0 | 0 | — |
| L48 step 4 | 63 | 27 | 1.15 | **0.49** | 3 | 2 / 2 | 9 | 0.88 | 2:2, 3:3, 4:2, 5:2 |
| L48 step 5 | 65 | 28 | 1.14 | **0.49** | 3 | 2 / 2 | 9 | 0.83 | 2:2, 3:3, 4:2, 5:2 |
| line 48 (seed) | 55 | 23 | 1.06 | 0.44 | 3 | 2 / 3 | 9 | 1.15 | 2:2, 3:3, 4:2, 5:2 |
| line 13 | 38 | 19 | 0.90 | 0.45 | 2 | 1 / 1 | 9 | 1.62 | 4:5, 6:3, 7:1 |
| line 36 | 33 | 20 | 0.65 | 0.39 | 2 | 1 / 1 | 6 | 0.98 | 2:1, 3:2, 4:2, 5:1 |
| line 21 | 42 | 21 | 0.89 | 0.45 | 2 | 1 / 1 | 5 | 0.75 | 2:1, 3:1, 4:2, 5:1 |
| line 17 | 28 | 12 | 0.61 | 0.26 | 2 | 1 / 1 | 2 | 0.93 | 2:1, 5:1 |
| line 49 | 45 | 20 | 0.87 | 0.39 | 2 | 1 / 1 | 4 | 0.66 | 2:1, 3:2, 4:1 |
| line 47 | 24 | 12 | 0.46 | 0.23 | 1 | 1 / 1 | 2 | 0.93 | 2:2 |

Strict T_deep and T_depth use N_≥2 in the normalisation. That is my choice and should be fixed in the definition; with N_≥2 ≈ 12–28 the (√N − 2)² denominator is small, so T_deep is inflated and is not comparable with the old T_deep. The full root mix (all deep cells, not only strict) is in `strict.out`; |v| = 1 cells are 36–62 % of every certificate and 44–79 % of the deep cells.

**Verdicts.**
- **H2 candidate (line 51, steps 9 and 10): fails strict depth.** Strict maxdepth is 0 (vertex contact) or 1 (edge contact). All 14 (15) |v| = 1 cells touch the exterior and are absorbed, and then no |v| ≥ 2 cell is deep. Its maxdepth 2 was entirely an a⁵-shield effect, on my certificates (the same as the Experimenter's for these two; no cheaper one was found).
- **Area-like seeds:** only **line 48** keeps strict maxdepth ≥ 2 (2 with vertex contact, 3 with edge contact). Lines 13, 36, 21, 17, 49 and 47 drop to strict maxdepth 1.
- **L48 finalists:** strict maxdepth 2, with the same 9 strict-deep cells and the same root mix as the seed line 48 certificate. So their strict depth is inherited from the seed, not created by the growth.
- **D_c,≥2 is ≈ 0.23–0.49 everywhere.** The D_c ≥ 1 of the L48 family comes from |v| = 1 cells (36 of 63 cells in step 4).
- All of this is per certificate: another (cheaper) certificate could move N and depth in either direction.

### Part 3b — recomputed with the adopted S2 definition (owner decision 2026-10-16)
S2: root-length-1 cells are absorbed (vertex contact, least fixed point) before *every* layer; T over the full N. `strict_s2.out`.
- **Maxdepth and N_deep: identical** to Part 3 for all 11 certificates. No root-1 cell is ever left to receive a depth.
- **But with the full-N normaliser, line 48 is not strictly area-like.** Its strict T_deep is 0.307 (below 0.5), with T_depth 0.623 and maxdepth 2. L48 steps 4/5: T_deep 0.255 / 0.245.
- No certificate here passes all of maxdepth ≥ 2, T_deep ≥ 0.5 and T_depth ≥ 0.5 under S2 (line 13 has T_deep 0.52 but maxdepth 1).
- So the corrected record should read **"no word is strictly area-like"**, not "only line 48". Line 48 is the only one with strict maxdepth ≥ 2. Under the N_≥2 variant (Part 3) line 48 would pass T_deep (1.15); the label therefore depends on the normaliser choice.
