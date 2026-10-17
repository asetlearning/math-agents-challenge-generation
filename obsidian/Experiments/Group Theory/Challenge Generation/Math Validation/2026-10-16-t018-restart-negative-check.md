---
type: validation-verdict
date: 2026-10-16
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-018 C++ restart: 'no state has strict maxdepth >= 2 (S2)', 'H2 falsified'"
verdict: "CONFIRMED (H2 falsified) with one correction (certificate dependence)"
---
# T-018 restart negative: independent check

Triage: [[2026-10-16-t018-restart-negative-and-tcgraph-pr5-pr6-triage]]. Data: b25 `t018-diagram-search` @ 03da2f7, `experiments/challenge_gen/t018/data/cpp_restart/` (inputs.sha256: b25_full b1d511fe…). Scripts and outputs: `Agents/asetlearning/Validator/scratch/restart/` (`s2_all.py/.out`, `probe.py`, `probe.out`, `probe_broad.out`, `ring.py/.out`, cheaper certificates `cert_*.json`). Every run used capjob (2G, 1 cpu), one at a time, with `python -S` and an explicit fold module path (printed).

**Terms.**
- **S2 (strict depth):** cells of root length 1 (|v| = 1, i.e. a⁵-type cells) touching the exterior by a vertex are absorbed into it. This is repeated before every layer. All other cells are peeled by vertex contact.
- **Strict maxdepth:** the largest S2 layer index of a cell of root length ≥ 2.
- **T_deep:** N_deep / (√N − 2)², over the full N.
- **N*_c:** the compressed-certificate cell count, an upper bound on area.

## Verdict

| claim | verdict |
|---|---|
| On the arms' stored certificates, no state of the four arms (374 states) has strict maxdepth ≥ 2 | **CONFIRMED**, on all 374 states (not a sample) |
| H2 falsified (no novel finalist with strict maxdepth ≥ 2 **and** T_deep ≥ 0.5, from ≥ 1 growth step) | **CONFIRMED**, and robust to cheaper certificates (see 2) |
| "No state has strict maxdepth ≥ 2" read as a property of the **words** | **REFUTED for the line-48 lineage**: cheaper certificates of L48 steps 0, 4, 5 and 6 have strict maxdepth 2 |

## 1. Recompute on all 374 states

- **Method:**
  - my own kbmag parse (1,630 entries; every core is u^(5k));
  - my own raw → core conversion (fr(R) = q·core·q⁻¹, conjugator → fr(q⁻¹c));
  - the Python reference fold (main 714caa9; identical to the 03da2f7 `diagram.py`);
  - my own standard and S2 peeling, independent of `strict_depth.py` and of the C++.
- **L0 (the certificate expands to w):** holds for 374 / 374 states, both on the raw table and after conversion.
- **Field-by-field agreement with `strict_rescore.json`** (standard maxdepth, S2 maxdepth, S2 N_deep, S2 depth sum, N_≥2) and with the states' `strict_maxdepth`: **0 mismatches in 374**. The histograms are identical to the note's:

| arm | standard maxdepth 0/1/2/3 | S2 maxdepth 0/1 |
|---|---|---|
| B0 beam | 6/60/23/0 | 50/39 |
| B0 greedy | 6/47/26/0 | 42/37 |
| B0+N beam | 6/63/42/0 | 52/59 |
| B0+N greedy | 6/48/38/3 | 42/53 |

- No |v| = 1 cell is left unabsorbed in any state.
- Max D_c,≥2 is 0.648 at L34 B0+N greedy step 14, as reported.

## 2. Certificate dependence (my subset merge |S| ≤ 4 + 714caa9 closure_fixpoint, then S2 again)

**Probed:**
- L34 B0+N greedy steps 12–16 (the max D_c,≥2 states);
- L48 steps 0, 4, 5 and 6;
- the seeds L13 and L22 (the highest S2 T_deep);
- best candidates #4 (L47 step 3) and #5 (L20 step 1);
- **every other distinct word (41) with standard maxdepth ≥ 2** outside L48.

| states | cheaper certificate | S2 maxdepth |
|---|---|---|
| L34 steps 12–16 | N 62–70 → 50–58 (−12 each) | 1 → 1 (N_deep 11 → 7) |
| **L48 steps 0, 4, 5, 6** | N 56/64/66/68 → 55/63/65/67 (one merge) | **1 → 2** (N_deep 3–5 → 9; T_deep 0.31 / 0.26 / 0.25 / 0.24; T_depth 0.56–0.62) |
| 41 other words | 33 of 41 get cheaper (largest drop 16 cells) | 0 / 1 unchanged; **none reaches 2** |
| L13 seed (dataset) | 41 → 38 | 1; T_deep 0.519 (the only T_deep ≥ 0.5 anywhere, at maxdepth 1) |
| #4 L47 step 3 | **46 → 30** | 1 |

**Readings.**
- **H2 stands.** No probed certificate has strict maxdepth ≥ 2 outside L48. The L48 lineage is registered as inherited depth and is excluded from H2. Its depth-2 certificates have T_deep ≤ 0.31, under the 0.5 bar. No state anywhere combines maxdepth 2 with T_deep ≥ 0.5.
- **Correction to the note's wording.** "No state of any arm has strict maxdepth ≥ 2" is true of the arms' stored certificates only.
  - The L48 seed's restart certificate (56 cells) has S2 maxdepth 1. My 55-cell certificate of the same word has 2. The note's best-candidates caveat (ii) already quotes the 2.
  - The same holds at steps 4–6. So the restart histograms understate the strict depth available for the L48 words.
  - Suggested wording: "no stored certificate has strict maxdepth ≥ 2; cheaper certificates of the L48 (inherited) lineage reach 2".
- **Compression can raise strict depth.** Removing one cell turned depth 1 into 2 in all four L48 cases. So the strict-depth statistics are not monotone in certificate quality, and a shallow result on a non-minimal certificate is not automatically the conservative one.
- **The N*_c values are loose.**
  - L34 steps 12–16 are 12 cells too high, so D_c,≥2 at step 14 is 29/54 = 0.537 on my certificate, not 0.648.
  - Best candidate #4 goes 46 → 30.
  - These are upper bounds anyway, but best-candidate #3's D_c,≥2 "0.648 (best)" falls to 0.537 on a cheaper certificate.

**Scope.**
- Verified: the 374 stored certificates, and cheaper certificates of the 54 probed words (13 targeted + 41 broad).
- Not verified: minimal area, or certificates outside my merge neighbourhood. All 374 states were recomputed; certificate dependence was probed on the words that have standard depth ≥ 2.
