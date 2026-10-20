---
type: validation-verdict
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-017 close-out note (t017-recertification-and-minimality-2026-10-19): numbers, pooled table, deviations, scope and status, checked against the Validator's verify notes and the raw outputs"
verdict: "Numbers CONFIRMED with corrections. The pooled table reproduces independently from the raw records of all 8 jobs: every pooled N, S2, flip, baseline value, class, component count and capped flag. Errors: (1) the S2 definition (root length 1, not conjugator length 1); (2) the R7 definition (cores v^{5k}, |v| ≤ 7, from b25_full, not 'all primitive 5th powers'); (3) §3's tile-check statement (both levels were checked against the pilot tile table, and the tile words are not 'free reductions of own expansions'). Also incomplete 'set by' lists for ds160, ds512, ds566 and ds781, plus minor items. Status: 'validated' overstates a universally quantified H17 that fails on ds547. Recommend scoping the hypothesis/verdict line, or a mixed status."
---
# T-017 close-out note: check

This was a Lead request (2026-10-20): check the close-out note
`B25/Hardness Evaluation/methodology/t017-recertification-and-minimality-2026-10-19.md` against my verify notes. I made no edits to it.

**Method.** I recomputed the pooled table from the raw records of all 8 jobs (k=4 R7 both objectives, k=5, k=6), with my own script (`pool.py`, session scratchpad):
- pooled S2 / flip = the minimum over runs of the `min_*` measures;
- pooled N = the minimum over runs of start and final N;
- baseline = the max over components of each one's pooled min.

These are the note's own definitions. The underlying certificates were verified in [[2026-10-19-t017-m1-results-verify]], [[2026-10-20-t017-step3-k5-verify]] and [[2026-10-20-t017-step3-s6-verify]].

## Pooled table (§2): reproduced

| check | result |
|---|---|
| stored (N, S2, flip), pooled N and its run, pooled S2 and flip | 12/12 |
| baseline values S2 / flip | 12/12 |
| H17 flip and H17 S2 classes | 12/12 (flip: 1 fails, 6 drop, 5 unchanged; S2: 3 fails, 4 drop, 5 unchanged) |
| component counts (9, 8, 13, 10, 12, 13, 46, 20, 14, 15, 24, 19) | 12/12 |
| capped flags (k6 words; ds547 parent at k6; ds764 k5 df; ds519 k4 df (3,600 s) and k5 df; ds160 and ds368 none) | 12/12 |
| "first reached" = k4 af wherever the note gives one; ds665 S2 = k4 af only | correct |

**"Set by" columns: incomplete.** The note's rule is "up to three components that attain the maximum". These rows list fewer than the rule allows, or mix up the two measures:

| word | note | attained by (S2 / flip) |
|---|---|---|
| ds160 | parent; S2 also tiles 02, 03 | S2: parent, tiles 02, 03, 08. **Flip: parent, tiles 03, 08** (the note implies the parent alone) |
| ds512 | parent | S2: parent, **tiles 05, 08, 10**; flip: parent only |
| ds566 | parent | S2: parent, **tiles 03, 05, 09**; flip: parent only |
| ds781 | parent, tiles 00, 01, 05 | S2: parent, tiles 00, 01, 05, 09, 14. Flip: parent, tiles 01, 05. **Tile 00 sets only S2** |

ds94, ds125, ds145, ds368, ds519, ds547, ds665 and ds764 are correct (ds94: tile 04 also attains it; ds764 flip: tiles 20, 21 also attain it, so the lists are truncated at three).

**Two minor points.**
- The column header says "later runs are listed when they attain it too", but no row lists them. In fact k4 df, k5 and k6 attain every pooled depth except ds665's S2. Either drop that sentence or list the runs.
- Pooled N follows the stated rule (start or final). A smaller valid certificate exists for ds665: a measured candidate at k=6 with **465** cells (S2 3, flip 3), which is L0-verified. A footnote would cover it.

## §1, §3–§6

**Correct:**
- the headline and the S2 tallies;
- the per-word bounds;
- the ds160 retirement against baseline 1;
- the five k=5 component drops;
- the k=6 statements (0 events, 286–792 hits, 0.86–1.55 M sets);
- any-u5 = R7 (0/860 extended entries);
- the CPU figures (60.245 = 8.2598 + 27.9852 + 24.0000);
- the pool sizes (11,386 / 23,228 / 38,729, as recorded; I did not check their composition);
- the input sha256 values;
- the ds519 caps (k=4 df 1 CPU-h, k=5 df 3 CPU-h);
- ds764 at a fixpoint at k=4.

**Errors:**
1. **S2 definition (§1).** "cells of conjugator length 1 absorbed" is wrong. S2 absorbs cells of **root length 1** (|v| = 1, a⁵-type cells) that touch the exterior, repeated before every layer ([[challenge-gen-success-metrics]], `strict_depth.py`).
2. **R7 definition (§1).** "5th powers of cyclically reduced primitive words of length ≤ 7" is not the table. The table is the cyclic cores of b25_full's relators v^{5k}, |v| ≤ 7, with inverses (glossary). It holds exponents up to 35 for |v| = 1 (v¹⁰ … v³⁵, 104 entries), plus v¹⁰ / v¹⁵ for |v| = 2, 3. ~~It does not contain every primitive v of length ≤ 7 (only 312 entries have |v| = 7).~~ **Corrected 2026-10-20:** that last sentence was wrong. b25_full covers all 510 primitive, cyclically reduced classes with |v| ≤ 7, up to rotation and with inverses. 312 is exactly the number of |v| = 7 classes. The definitional point stands: R7 is the core table, and it also holds higher exponents.
3. **Tile check (§3, last bullet).** "Level-2 words only were verified against tile inputs …; the tile words are the free reductions of the tiles' own expansions" is wrong on both counts.
   - [[2026-10-19-t017-m1-tile-inputs-check]] checked level 2 (146/146) **and** level 3 (45/45 tiles, plus the parent).
   - It checked the tile words against the pilot's **tile table** (dataset word or its inverse, rotated by the stored offset). The "free reduction of own expansion" staging was the tautological check that the note replaced.
   - The staged level-3 words are the stored replay words.

**Imprecise (minor):**
4. **§4 M2'.** For the 5 words with exact halves, the closure result is at periods ≤ 7. My extra check also found no shortening of any period in those closures. As written, the note drops the qualifier.
5. **§5.1.** The run mode is vertex_pairs. Its Step 0 justification is that line 49 needs a vertex-connected triple, and that vertex_pairs reproduces my subset-merge areas on all 7 lines ([[2026-10-19-t017-m1-code-review]]). The quoted "adjacent + pairs reaches every target" was the earlier adjacent_pairs mode.
6. **§5.6 vs §3.** §5.6 gives ds764 and ds519 the same exclusion reason: "capped; a k=6 run without more budget says nothing". But ds764 is at baseline + 2 (flip 3 vs 1), so the one-sided rule excludes it anyway. ds519 is eligible and was excluded on budget, as §3 says. Make §5.6 match.
7. **§7.** `542992216c3e84e8` is the run's internal table hash, listed under "Input hashes (sha256)". The file's sha256 is `61bfebc15bd928feb4d0cd07e6ba6209348f34ed7a6d6ab5c39528085d870a23`.
8. **§7 verification line.** The Validator has now reproduced the full pooled table (this note), not only the k=5 pooled classes. The header "Every number was verified by the Validator" also covers process figures I did not check: the 30 CPU-h decision, the wall times, the pool composition.

## Status

- The pre-registration (plan v2) has three bands:
  - ≥ 6/12 fail: negative;
  - **1–5/12 fail: record the failing words as unconfirmed, run Step 3, stop**;
  - 0/12 fail: the positive branch.
- The result is in the middle band: 1/12 on flip, 3/12 on S2.
- The frontmatter states H17 universally ("for each of the 12 … stays above"). As written, H17 is false for ds547, so `#status/validated` ("scored against gates, passed") overstates it.
- **Fair options:**
  - keep `validated`, but scope the hypothesis/verdict line to what passed: "H17 holds for 11/12 words (flip; 9/12 S2) under M1 at |S| ≤ 5; ds547 fails and is unconfirmed; the pre-registered 1–5/12 band";
  - or use a mixed label.
- The final-verdict text already says this. The frontmatter and the status tag do not.
