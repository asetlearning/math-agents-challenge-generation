---
type: validation-verdict
date: 2026-10-19
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-017 M1 inputs: the 146 level-2 tile certificates and the 11 level-2 parents staged by Experimenter-B25, checked against the pilot's tile table and the replay dumps"
verdict: "CONFIRMED (level 2 and level 3). All 146 level-2 tile words equal the pilot's tile-table entry (dataset word or its inverse, rotated by the stored offset, identity automorphism), and their cells equal the dump cells and expand to that word. All 11 parents equal w1 of the dumps, with cells equal to F1 and L0 exact. The tile results can count. Level 3 (ds519_L3_c2_B): 45/45 tiles and the parent confirmed the same way, and the staged l3components.jsonl equals the replay components."
---
# T-017 M1 inputs: tile words and parents

This was a Lead request (2026-10-19). Experimenter-B25 staged the M1 inputs, per its plan `Agents/asetlearning/Experimenter-B25/2026-10-19-t017-m1-run-plan.md`.
- The tiles' `word` was set to the free reduction of the tile's own cell expansion, because the dumps do not store tile words. So the Experimenter's L0 check was tautological.
- This note checks the words against the tile table the pilot actually used.

**Inputs checked.** The staged copies, snapshot by sha256:
- `tiles.jsonl` `fcac15d7…b5d3` (146 records);
- `parents.jsonl` `e3d7a6ac…8937` (11 records).

`words.jsonl` was not part of this check: Lead's 12 words were already L0-verified in [[2026-10-19-t017-m1-code-review]].

**References.**
- My level-2 replay dumps (rjob `20261018-095405-e53f79`, [[2026-10-18-t024-level2-best-words-verify]]): fields `w1`, `F1_cells` and `tiles[] = {tile, offset, cells}`.
- The pilot's tile table, rebuilt in plain Python from its definition (`t024_m1_tiling.load_data` / `t024_onion_cpp.init`):
  - the sources are the dataset lines with a stored certificate in `certs_gt53.jsonl` + `seeds_power_free_len_le53.jsonl`, in sorted order: 453 sources, 906 entries;
  - entry t is the source `t // 2`, inverted iff t is odd (the order of `TileTable`);
  - the tile word is that word rotated left by `offset` (`rotatedCertificate`, identity automorphism).
- The dataset file is the 820-word file. Its sha256 `e0eeb777…dda1` equals the replay job's `dataset.txt`.
- Expansion is over `core_table_r7.json` (1-based cells).

## Results (own Python, no tcgraph; local capjob)

| check | result |
|---|---|
| a tile record exists for every dump tile (name `ds{N}_L2_tile{j}_k{tile}`), no extra records | 146/146, 0 unmatched |
| tile word = table entry (source, orientation, offset) | **146/146** |
| tile cells = dump cells | 146/146 |
| tile cells expand exactly to the table word | 146/146 |
| independent lookup: the word is an exact rotation of exactly one dataset word or its inverse, and that is the expected (line, orientation, offset) | 146/146, no ambiguous match |
| parent word = dump `w1` | **11/11** |
| parent cells = dump `F1_cells`, expanding exactly to w1 | 11/11 |

Shape of the inputs:
- 146 tiles use 141 distinct (line, orientation, offset) keys from 75 dataset words; 81 tiles are inverted.
- The parents have 132–338 cells.

**Scope.** The check covers the 11 level-2 words; ds707 is excluded, as in the plan. The level-3 tiles and parent come from the seed-519 replay and need the same check when they are staged. The rebuilt table depends on the two certificate files in the b25 tree (`b25-surgery`). Its sources match the pilot's definition, and the independent rotation lookup confirms every tile without using that table.

Scratch: `check_tiles.py` and its JSON are in my session scratchpad, not committed.

## Level 3: ds519_L3_c2_B components (2026-10-19)

This was a Lead request; the Experimenter asked for the same check.

**Inputs.**
- Seed-519 replay (Experimenter; b25 `t017-replay-l3` `6dcd95e`): `runs/t017/replay188/tiles_ds519_L3_c2_B.json.gz`, sha256 `53559859…7af5`, equal to Lead's. It has the parent plus 45 tiles, with the stored tile words.
- Staged: `l3components.jsonl`, sha256 `c7e966d7…00fbb3` (46 records). The tile words there are the stored words, not expansions.
- References:
  - the stored level-2 parent `ds519_L2_c2` (pilot-3 certificates; sha256 `95a6f093…`, the same in all 4 copies);
  - the stored level-3 word `ds519_L3_c2_B`;
  - the same rebuilt tile table as above.

| check | result |
|---|---|
| replay word = stored level-3 word | yes |
| parent word = `ds519_L2_c2` word (558 letters) | **yes** |
| parent cells = the stored compressed level-2 certificate (546 cells), L0 exact | yes |
| tile word = table entry (source, orientation, offset) | **45/45** |
| tile cells expand exactly to that word | 45/45 |
| independent rotation lookup is unique and equals the expected (line, orientation, offset) | 45/45 |
| the record's own fields (`ds` 0-based, `orient`, `tile_len`) agree with the table | 45/45 |
| staged record (word and cells) equals a replay component | 46/46 |

Shape: 44 distinct (tile, offset) keys (the key (9, 34) is used twice), from 32 dataset words; 21 tiles are inverted.

**Verdict:** CONFIRMED. The level-3 tile and parent results can count. The level-3 components' baselines (S2 and flip (d) per component) come from the M1 component runs on this file.

Scratch: `check_l3_tiles.py` and its JSON are in my session scratchpad, not committed.
