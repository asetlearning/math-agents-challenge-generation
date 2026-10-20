---
type: validation-verdict
date: 2026-10-19
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-017 Steps 1-2: independent check of the certificates behind the M1 headline results (ds547 fails, ds160 4 -> 3, drop words, baselines) and of the summary's min/max logic"
verdict: "CONFIRMED. Every min_s2 / min_flip_d certificate in the 6 jobs (1,720, both objectives, r7 and any_u5) re-expands exactly to its staged input word and has the recorded N, S2 and flip (d) under tcgraph main. The target words and their components were also cross-checked with the Python references. ds547: word min flip 2 (775 cells), baseline 2 from the parent (269 cells), so it fails. ds160: flip 3 (318 cells), above baseline 2. The results table (24 rows) is reproduced exactly from the min_* states, with baseline = max over components of each one's min."
---
# T-017 M1 results: certificate check (Steps 1-2)

This was a Lead request (2026-10-19). It checks the results note `Agents/asetlearning/Experimenter-B25/2026-10-19-t017-m1-results.md` against the raw outputs of the 6 rjob jobs: `20261019-200113-ea4941`, `-200115-670fa5`, `-200116-795704`, `-200118-08644a`, `-201804-6f7e1d` and `-201806-92215a`. I fetched the outputs myself (25 MB).

**Terms.**
- N = number of cells.
- S2 = strict depth.
- flip (d) = the S2-flip depth under rule (d).
- L0 = the certificate's expansion over the R7 core table equals the word exactly.
- The **min state** of a run is the certificate the record names in `min_s2` or `min_flip_d`. It is the start, an accepted state, the final, or a rejected candidate that was measured.
- **Baseline** = the maximum over a word's components (the parent and the tiles) of each component's minimum.

## Method (own code, local capjob, 2 GB / 1 CPU, 44 s)

- **Words.** The staged inputs `words11`, `l3word`, `parents`, `tiles` and `l3components` (`data/inputs/t017/`). Their sha256 equal the jobs' `inputs.sha256`. The tile and parent words were checked against the pilot's tile table in [[2026-10-19-t017-m1-tile-inputs-check]].
- **Certificate of each min state:**
  - `same_as: final`: the record's `cells` (I also asserted `final` = the min measure);
  - `same_as: start`: the input cells (asserted `initial` = the min measure);
  - otherwise: the stored `cells` of the min state (14 cases, 8 of them from rejected candidates).
- **L0** with two expanders: the C++ `RelatorMap.expand` and the Python `certificate.expand` over `core_table_r7.json`. Both must equal the input word exactly.
- **Measure.**
  - Every certificate: tcgraph main `ca2ceb9` (b25 `ae6a79c` bindings, rule (d)). This build is independent of the surgery branch, the same one used in [[2026-10-18-t024-level2-best-words-verify]].
  - Cross-check on 576 of the 1,720 min-state entries (N ≤ 775): the Python references `strict_depth.analyse` and `strict_depth_flip.analyse_flip(rule='d')`. They cover the 5 target words (ds547, ds160, ds94, ds512, ds665) and all their components, both objectives, both tables.
- **Summary.** Recomputed from the records:
  - the word min is the minimum over the two objectives of the `min_*` measure;
  - the baseline is the maximum over components of that same per-component min;
  - the H17 classes follow the results note's definitions.
  - The result was compared field by field with the note's 24 table rows.

## Results

| check | result |
|---|---|
| the 12 staged words = the words verified in [[2026-10-18-t024-level2-best-words-verify]] (replay `w2`) and the stored `ds519_L3_c2_B` | **12/12**, letter for letter |
| records' `initial` (N, S2, flip) of the 11 level-2 words = the 2026-10-18 table | 11/11 |
| records present (215 inputs = 12 words + 203 components, × 2 objectives × 2 tables) | 860/860, none missing, no duplicate |
| min-state certificates: L0 (both expanders) | **1,720/1,720** |
| recorded (N, S2, flip (d)) = my C++ main measure | **1,720/1,720** |
| Python reference = C++ main (S2 and flip (d)) | 576/576 |
| any_u5 record = r7 record (initial, final, cells, both min states) | all; no extended entry used (0/860, table size 1630) |
| results table rows reproduced (start, mins per objective, comps, baseline, H17 flip, H17 S2, mixed) | **24/24** |

### (1) ds547 (H17 fails)

| certificate | N | L0 | S2 | flip (d) | run |
|---|---|---|---|---|---|
| word, min state (area_first and depth_first, state 49 = final) | 775 | ✓ | 2 | 2 | fixpoint, not capped |
| **parent** (area_first state 24 = final) | 269 | ✓ | 2 | 2 | fixpoint, not capped |
| parent (depth_first state 23 = final) | 277 | ✓ | 2 | 2 | fixpoint, not capped |
| the other 19 components (tiles) | 11–56 | ✓ | ≤ 1 | ≤ 1 | all fixpoints, none capped |

- The baseline is 2 under both measures, and the parent alone sets it. Word min 2 ≤ baseline 2, so ds547 **fails** under flip and under S2.
- All four values are measured on certificates that I re-expanded myself.

### (2) ds160: flip 4 → 3

- Word: area_first state 35 (= final), N 318, L0 ✓, S2 3, flip (d) 3. depth_first: state 34, N 322, 3 / 3. Both runs are fixpoints and not capped.
- Baseline 2 (the parent: 115 cells, 2 / 2).
- So the drop to 3 is real under M1. 3 > 2 puts it in "drops but stays above", and the depth-4 claim is retired.

### (3) Drop words (ds94, ds512, ds665)

| word | word min (N, S2 / flip) | baseline S2 / flip | baseline set by |
|---|---|---|---|
| ds94 | 391, 2 / 2 | 1 / 1 | parent (127 cells) and tiles 00, 02, 04, all 1 / 1 |
| ds512 | 466, 2 / 2 | 1 / 1 | flip: the parent alone (206 cells); S2: the parent and tiles 05, 08, 10 |
| ds665 | 475 (area_first), 2 / 2 | 2 / 1 | S2: the parent (175 cells, 2 / 1); flip: the parent and tiles 04, 05, 06 |

- Every one of these certificates passes L0, and the two depth implementations agree on it.
- ds665 depth_first ends at S2 3 (493 cells), and area_first reaches 2. The word min takes the better objective, as defined.

### (4) Summary logic: CONFIRMED

- Minima come from the `min_*` states, not from the finals, and the baseline is the max over components of each component's min. My recomputation reproduces every table cell.
- **This choice matters.** With the area_first finals alone, the flip baseline of ds94 and ds125 would be 2 instead of 1, because the area-first acceptance raised a tile's depth: ds94 tile00_k43 goes 1 → 2 at 56 → 55 cells. Both words would then "fail". Taking the min, which includes the start, avoids that.
- After taking the minimum over the two objectives, the finals give the same 12 classes. So none of the headline classes depends on the convention.

**Baselines vs the pre-M1 component maxima.** The pre-M1 values are the "comp" column of [[2026-10-18-t024-level2-best-words-verify]].
- Every new baseline is ≤ the old one, as it must be.
- **Only 3 of the 11 level-2 words have a lower baseline:**
  - ds94: S2 and flip, 2 → 1;
  - ds125: flip, 2 → 1;
  - ds665: flip, 2 → 1.
- The other 8 are unchanged: ds512, ds566 and ds781 were already 1 / 1, and ds368 and ds764 already had flip 1.
- So "baselines mostly fell from 2 to 1" is not right. Most baselines that are 1 were already 1 before M1.

## Scope and notes

- **Scope.** All results are upper bounds under M1 at |S| ≤ 4 (vertex_pairs), as the results note says. I did not re-run the surgery and did not check the pool (11,386 classes, hash `388b80e8…`). A certificate missed by M1 could lower any word or baseline further.
- **Capped run.** The ds519 L3 depth_first runs (both tables) are the only records that are capped and not a fixpoint, as the note says. ds519's min comes from area_first (3 / 3, state 104), which is a fixpoint.
- **Tie-break (cosmetic).** When several states tie on the target measure, the min state is not always the best on the other measure. For example:
  - `ds764_L2_tile14_k112` depth_first `min_flip_d` is a rejected candidate with (flip 0, S2 1), although the start has (0, 0);
  - `ds547_L2_tile04_k332` and `ds512_L2_tile05_k265` behave the same way.
  - The minimum values are unaffected.
- **Scratch.** `check_m1res.py` and its JSON are in my session scratchpad, not committed.
