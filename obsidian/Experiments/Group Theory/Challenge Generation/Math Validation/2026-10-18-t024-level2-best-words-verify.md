---
type: validation-verdict
date: 2026-10-18
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-024: independent verification of the 12 best level-2 onion finals (pilot rjob 20261018-000601-9e5902)"
verdict: "11 of 12 CONFIRMED (L0, 2.5-reduced, S2 depth 3-4 and flip-(d) depth both above the components'); ds 707 CONFIRMED under S2 only (flip-(d) depth 2 = components' 2). No cheaper certificate found by our reducers; minimality not established."
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
