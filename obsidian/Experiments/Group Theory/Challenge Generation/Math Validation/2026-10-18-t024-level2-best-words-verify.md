---
type: validation-verdict
date: 2026-10-18
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-024: independent verification of the 12 best level-2 onion finals (pilot rjob 20261018-000601-9e5902)"
verdict: "Addendum 2026-10-19: all 11 confirmed level-2 words and the ds519 level-3 word are L1 (rho_min16 = 1) and novel. 11 of 12 CONFIRMED (L0, 2.5-reduced, S2 depth 3-4 and flip-(d) depth both above the components'); ds 707 CONFIRMED under S2 only (flip-(d) depth 2 = components' 2). No cheaper certificate found by our reducers; minimality not established."
---
# T-024: verification of the best level-2 onion words

Triage: [[2026-10-18-t024-level2-best-words-verify-triage]]. This was a Lead task (2026-10-18; the owner approved the T-024 next steps; the replay driver and rjob were approved by Lead).

Terms used below:
- **L0**: the certificate re-expands to the word.
- **2.5-reduced**: no power with exponent above 2.5. Exact 2.5-powers ("exact halves") are allowed.
- **S2**: strict depth: the peel depth of the diagram, with cells whose root has length 1 absorbed into the exterior.
- **flip (d)**: the S2-flip control under rule (d). A cell whose exposed run is at least 2.5|v|, measured against the boundary and already absorbed cells only, is absorbed before the peel.
- **Bouquet control**: the word's depth must exceed its components' maximum depth. The components are the level-1 parent and the tiles.
- **Targets**: the pilot finals that are L1 (ρ_min16 = 1), pass the bouquet control, and have S2 depth 3–4. That is 9 B finals and 8 A finals, which are 12 distinct words.

## Method

1. **Independent replay (rjob 20261018-095405-e53f79, Mac, 9 CPUs, 62 min wall).**
   - Build: the pilot's exact build, b25 `90bc1cb` + tcgraph `4390614` (rjob reused the pilot's cached build).
   - A scratch driver (Validator scratch, not product code) ran the pilot's own `run_seed` for each target seed and captured the level-2 certificates. It dumped the raw assembled certificate, the compressed (pipeline) certificate, the parent's certificate and the tile certificates.
   - **All 12 reproduced finals equal the stored words.** The measures equal the stored rows. The only difference is the format of the `gates` windows field (tuples vs lists) on 4 B words.
2. **Cheaper certificates, in the same job** (`certificate_reduction.cpp` is identical in `4390614` and main `ca2ceb9`). Four reductions per word:
   - `full_reduce` (loop erasure + Peiffer + inverseCellReduce, iterated) on the pipeline certificate;
   - `closure_fixpoint` with inverse cells on the pipeline certificate;
   - the same two on the raw assembled certificate.
   - All 48 reductions finished, and every result re-expands to the word.
3. **Local checks** with tcgraph main `ca2ceb9` (b25 `ae6a79c` bindings, rule (d); ctest 20/20) under capjob:
   - L0 with two expanders: the C++ `RelatorMap.expand` and the Python `certificate.expand` over the core table.
   - The gate with two detectors: `power_gates` B and my own detector (`cyc_has_power_gt`, threshold > 2.5).
   - S2 and flip (d) in C++ and with the Python references `strict_depth.analyse` and `strict_depth_flip.analyse_flip(rule='d')`.
   - The bouquet control, recomputed on the dumped parent and tile certificates.

## Results per word

N = number of cells in the pipeline certificate. comp = the components' maximum depth, under S2 and under flip (d). Exact halves = the number of exact 2.5-powers.

| ds | final | \|w\| | N | L0 | 2.5-reduced (2 detectors) | exact halves | S2 | flip (d) | comp S2 / flip (d) | cheaper cert found | **Verdict** |
|---|---|---|---|---|---|---|---|---|---|---|
| 94 | A | 216 | 445 | ✓ | ✓ | 0 | 3 | 3 | 2 / 2 | no | **CONFIRMED** depth 3 |
| 125 | A, B | 163 | 298 | ✓ | ✓ | 0 | 3 | 3 | 2 / 2 | no | **CONFIRMED** depth 3 |
| 145 | A | 361 | 468 | ✓ | ✓ | 0 | 3 | 3 | 2 / 2 | no | **CONFIRMED** depth 3 |
| 160 | B | 261 | 379 | ✓ | ✓ | 1 | **4** | **4** | 2 / 2 | no | **CONFIRMED** depth 4 (S2 and flip) |
| 368 | A | 211 | 336 | ✓ | ✓ | 0 | 3 | 3 | 2 / 1 | no | **CONFIRMED** depth 3 |
| 512 | B | 378 | 545 | ✓ | ✓ | 1 | 3 | 3 | 1 / 1 | no | **CONFIRMED** depth 3 |
| 547 | A, B | 699 | 878 | ✓ | ✓ | 0 | 3 | 3 | 2 / 2 | no | **CONFIRMED** depth 3 |
| 566 | B | 320 | 515 | ✓ | ✓ | 2 | 3 | 3 | 1 / 1 | no | **CONFIRMED** depth 3 |
| 665 | A, B | 405 | 618 | ✓ | ✓ | 0 | **4** | 3 | 2 / 2 | no | **CONFIRMED** S2 4; flip (d) 3 |
| 707 | A, B | 259 | 460 | ✓ | ✓ | 0 | 3 | **2** | 2 / 2 | no | **S2 only**: flip (d) 2 = components' 2, so it fails the bouquet control under flip |
| 764 | A, B | 635 | 954 | ✓ | ✓ | 0 | 3 | 3 | 2 / 1 | no | **CONFIRMED** depth 3 |
| 781 | B | 529 | 767 | ✓ | ✓ | 1 | 3 | 2 | 1 / 1 | no | **CONFIRMED** S2 3; flip (d) 2, still above its components' 1 |

### L0
On all 12 words, all of these certificates re-expand correctly, with both expanders:
- the pipeline certificate and the raw certificate (to the word);
- the parent certificate (to w₁);
- every tile certificate.

### Target gate
- All 12 words are 2.5-reduced, by both detectors.
- The 8 A words have no exact half; they are strictly power-free.
- The 4 B-only words (160, 512, 566, 781) have 1–2 exact 2.5-powers each, all of period 2, plus one of period 6 in 566.

### Depth
- C++ and Python agree on S2 and flip (d) for all 12 words.
- **S2** reproduces the pilot: depth 3 on 10 words and depth 4 on 2 (160, 665). S2 passes the bouquet control on all 12.
- **flip (d):**
  - 9 words keep their S2 depth.
  - 665 drops 4 → 3, and 781 drops 3 → 2; both still pass the bouquet control.
  - 707 drops 3 → 2, which equals its components' maximum.
  - Only ds 160 is depth 4 under flip (d).
- **Pilot rule (c) vs rule (d):** the pilot's stored "flip" column was rule (c), the old over-conservative exposure, so it understated depth (e.g. 160: 3 under (c), 4 under (d)).
- **Tile depths:** they equal the pilot's `tile_depth` on every word. The tile maximum is S2 1. The components' maximum always comes from the parent.

### Cheaper certificates
- None of the four reductions shrinks the pipeline certificate of any word. Each pipeline certificate is a fixed point of `full_reduce` and of `closure_fixpoint` with inverse cells.
- On the raw certificate, the reductions reach at best the pipeline's N. Two `full_reduce` runs end above it: 125 at 390 vs 298, and 547 at 884 vs 878.
- So the depth survives every cheaper certificate our reducers can find: there is none.

## Verdict

- **11 of 12 CONFIRMED.** On each one, L0 holds, the word is 2.5-reduced, and its S2 depth (3 or 4) and its flip-(d) depth are both above its components' maximum, on a certificate no reducer of ours can shorten.
- **ds 707:** S2 depth 3 is confirmed, but under flip (d) its depth is 2, equal to its components', so it does not count under the flip control.
- **Depth 4:** confirmed under S2 for 160 and 665, and under flip (d) for **160 only**.
- **Pilot falsifier:** the level-1 maximum is 4 (seed 594), so nothing here exceeds it. That conclusion stands.

## Scope and limits

- Depths are for **our certificates after our reductions**. Our reducers are local: loop erasure, Peiffer pairs, inverse cells, and relator closure. They do not establish minimality, and a genuinely smaller van Kampen diagram with lower depth is not excluded.
  - My earlier non-contiguous subset merge (area7, |S| ≤ 4) found cheaper certificates where the pipeline did not. But it costs O(N⁴) in Python, so it is infeasible at N = 300–950 without new code. Possible follow-up, on request.
- I did not re-check L1 (ρ_min16). It is taken from the pilot.
- I did not re-check novelty or area-likeness.
- The bouquet control uses the components' certificates as compressed by the pipeline.

Files (Validator scratch, not committed): `scratch/t024verify/`.
- `replay_verify.py`, `job.toml`, `targets.json`;
- `check_local.py` → `check_local.jsonl`;
- rjob outputs in `runs/20261018-095405-e53f79/`.

## Addendum 2026-10-19: independent L1 and novelty re-check

This was a Lead task (2026-10-19, after the owner closed T-024 in vault `e5019b5`). Triage: [[2026-10-19-t024-l1-novelty-recheck-triage]].

**Scope:** 12 words. These are the 11 level-2 words confirmed above (all except ds 707) plus the level-3 word ds519_L3_c2_B from [[2026-10-18-t024-level3-first-word-verify]]. Lead's message counted 11 words ("10 level-2 words"), but the table above confirms 11 level-2 words, so the total is 12.

**Inputs:**
- The level-2 words come from my replay dumps (each dump checked equal to the stored final).
- The level-3 word comes from the timing job's certs (sha256 matching `index.json`).

**Run:** tcgraph main `188f8ae` (b25 `ae6a79c` bindings; ctest 20/20), one local capjob (2 GB, 1 CPU), about 5 min wall. Script and outputs are in Validator scratch, not committed: `scratch/t024verify/check_l1_novelty.py`, giving `check_l1_novelty.json` and `.out`.

### (1) L1

- **Definition.** ρ_min16 = min over the 16 images of |R_2.5(image)| / |w|.
  - The 16 images are the 8 letter automorphisms of F(a,b) (a, b swapped and/or inverted), each with and without inversion of the word.
  - R_2.5 is the tcgraph 2.5-reducer in certify mode: `greedy_reduce2_5`, then `greedy_reduce_cyclic_exhaustive2_5` over all shifts. No timeout was used.
- **Independent images.** I generated the images with my own code. For every word, the set equals the project's `images16`.
- **Result.** Every one of the 16 images of every word is a fixed point of R_2.5: |R_2.5| = |w| in all 192 reductions. So **ρ_min16 = 1.0 for all 12 words.** This equals the run's stored values (status `ok`).
- **Thresholds.** The words are L1 under both the project definition (ρ_min16 ≥ 0.5, the one Lead's task uses) and the stricter T-024 selection rule (ρ_min16 = 1).
- **Scope.** This is a statement about the heuristic reducer only. It does not say the words are hard in B(2,5).

### (2) Novelty

A word is novel if it is not conjugate in F(a,b) to any of the following, and not conjugate to the inverse of any of them. Conjugate in F means its cyclic reduction is a rotation of theirs.
- **Dataset:** the 820 dataset words.
- **R7:** all 1,630 relators of the kbmag file `b25_full` (815 relators plus their inverses).
  - My own parse of the file equals `table_from_kbmag`.
  - The classes of the core table are a subset of these.
- **HWW:** the 118 challenges of Havas, Wall and Wamsley (1974), as the registered 2.5-reduced file. As an extra, also the 118 non-empty words of the original freely reduced file.
- **Each other:** the other 11 words.

**Result: all 12 words are novel, and the reason is simple: no candidate has the same length as any reference word.**
- The length of the cyclic reduction is invariant under conjugation, inversion and the letter automorphisms.
- The 12 words are cyclically reduced, with lengths 163, 211, 216, 261, 320, 361, 378, 405, 529, 635, 699 and 1,548. All of these are different.
- The reference sets have cyclic lengths outside that range: the dataset 32–123, R7 5–35, HWW (2.5-reduced) 2,494–27,321, and the original HWW 2,498–41,886.
- So no reference word can be conjugate to any of the 12, and no two of the 12 are conjugate to each other.
- Even under the coarser equivalence that also allows the 16 images (automorphisms and inversion), there is no match.
- The pilot's own novelty flag (conjugacy against the core table and the dataset up to automorphisms) was `True` for all 12. It never checked HWW; this re-check adds HWW.

### Per-word verdict

| word | \|w\| | ρ_min16 (mine / run) | L1 (≥ 0.5 / = 1) | novel (conj. / up to 16 images) | **Verdict** |
|---|---|---|---|---|---|
| ds94 L2 | 216 | 1.0 / 1.0 | ✓ / ✓ | ✓ / ✓ | **CONFIRMED** |
| ds125 L2 | 163 | 1.0 / 1.0 | ✓ / ✓ | ✓ / ✓ | **CONFIRMED** |
| ds145 L2 | 361 | 1.0 / 1.0 | ✓ / ✓ | ✓ / ✓ | **CONFIRMED** |
| ds160 L2 | 261 | 1.0 / 1.0 | ✓ / ✓ | ✓ / ✓ | **CONFIRMED** |
| ds368 L2 | 211 | 1.0 / 1.0 | ✓ / ✓ | ✓ / ✓ | **CONFIRMED** |
| ds512 L2 | 378 | 1.0 / 1.0 | ✓ / ✓ | ✓ / ✓ | **CONFIRMED** |
| ds547 L2 | 699 | 1.0 / 1.0 | ✓ / ✓ | ✓ / ✓ | **CONFIRMED** |
| ds566 L2 | 320 | 1.0 / 1.0 | ✓ / ✓ | ✓ / ✓ | **CONFIRMED** |
| ds665 L2 | 405 | 1.0 / 1.0 | ✓ / ✓ | ✓ / ✓ | **CONFIRMED** |
| ds764 L2 | 635 | 1.0 / 1.0 | ✓ / ✓ | ✓ / ✓ | **CONFIRMED** |
| ds781 L2 | 529 | 1.0 / 1.0 | ✓ / ✓ | ✓ / ✓ | **CONFIRMED** |
| ds519 L3 c2 B | 1,548 | 1.0 / 1.0 | ✓ / ✓ | ✓ / ✓ | **CONFIRMED** |

**Scope:** novelty here means only "not conjugate in the free group" to the listed words. It does not exclude words that are equal in B(2,5) to a reference word, or words that contain reference words as subwords. The onion words are built from dataset tiles, so they do contain such subwords.

