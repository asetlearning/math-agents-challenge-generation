---
type: validation
date: 2026-11-06
agent: Validator
status: 61 of 61 CONFIRMED (L0-cert)
---
# Validation: E4-blind-insertion-R breaks, 60 + 1 mixer
Triage: [[2026-11-06-b25-solver-e4-blind-insertion-breaks-check-triage]]. Follows [[2026-11-05-b25-solver-e4-smoke-breaks-check]]. Inputs: E4 breaks.jsonl (60), attacks_shorter.jsonl (8263 lines), m2_inputs.jsonl (194815 rows), E4-mixer mixer_breaks.jsonl (3 rows, 1 certified), registry-rev4-draft (200 candidates; its words equal the vault data/ rev-4 file for all 200 ids). No word strings in this note. Cell (c, x) = word x^-1 c x.

## 1. Replay: 61 of 61 CONFIRMED
For each break: the target id is in the 200 rev-4 candidates; every core is a literal reduced fifth power; conjugators are freely reduced; red(product of cells . g^-1 g) equals the registry word (for 60 of 60 the product of the cells alone already equals it; g is empty in 39 of the 60, non-empty but cancelling in 21).
| group | rows | cells | max core period |
|---|---|---|---|
| M2 T-blind | 51 | 25-192 | 16-72 |
| M2 v5 | 4 | 64-157 | 21-53 |
| loop after M2 (R_emptied) | 5 | 57-78 | 22-36 |
| algo-mixer C3|6|21 | 1 | 707 | 39 (|g| 1054) |
Ids: 60 distinct ids in breaks.jsonl; the mixer id C3|6|21 is not among them. The earlier smoke breaks C1|6|7 and C1|6|15 are again in the list (new certificates: 36 and 52 cells; the C1|6|15 chain is identical to the smoke one).

## 2. Open candidates, no duplicates
All 61 ids are in the 200 candidates of rev 4 and none is among the 7 ids moved to tested in rev 4 (C1|16|3, C1|6|1, C3|4|13, C3|4|15, C3|4|17, C3|4|22, C3|4|28) nor among the 27 tested ids. No id occurs twice. So the 61 are new breaks of open candidates.

## 3. Source integrity and provenance (bulk)
All 8263 attack lines (4934 T-blind, 3329 v5): the source record is present in m2_inputs.jsonl for the same target with identical word and cells; the source word equals the product of its cells; every source core is a literal fifth power; periods are <= 7 for T-blind and <= 5 for v5; conjugator lengths are <= 4. Zero exceptions. Every M2 break id has an attack line with empty output. The 5 loop-after-M2 ids have only non-empty-output M2 lines (shorter words), the rest of the route being the loop (R, W) steps that end empty: for those the check is the end-to-end L0 replay (exact product), not a per-step replay of the loop steps.
Pool: T-blind and v5 pools are target-independent (see the E0 rerun note); the E4 loop round 1 inputs were checked in the smoke note. Not re-checked here: regeneration of the pools from the seed; the per-step replay of W/R steps of the 5 loop-after-M2 rows and of the multi-round M2 chains (step lists up to 14 steps, e.g. W, R, CL, KB, D, R, CL, KB, D, M2, R, CL, KB, M2); these are covered only through the final chain.

## 4. Algo-mixer C3|6|21
Certified row: steps R, CL, KB, D, M2, R, CL, KB, M2, R, CL, KB, MIX (13). The flattened chain (707 cells, 727-letter registry word) replays: literal fifth-power cores (max period 39), conjugators reduced, product equals the registry word; g (1054 letters) cancels. So the break is an L0 certificate irrespective of how the MIX step was found. The two other rows (id C3r2|2,2|8, twice) are uncertified (reason: replay of step 18 failed); they are not breaks and are not in the 60.
Not checked: the mixer path itself (reducer run, rule set), whether the rules used anything target-specific; for L0 this does not matter, for the provenance claim of the mixer stage it does.

## Caveats
Verified: L0 replay of 61 certificates, id status, source integrity of the pool words. Not verified: hits, R/W/KB steps one by one for the long chains, pool regeneration, the mixer run, the bench contract on the current head (Lead reports verify_break passes).

## Addendum: C3r2|2,2|8 (bridge fix) and the rev-5 draft
### A. C3r2|2,2|8: CONFIRMED (L0-cert)
Source: E4-mixer-fixed/mixer_breaks.jsonl (certified row). The registry word has 463 letters (rev 4). The chain has 2523 cells, max core period 28, all cores literal reduced fifth powers, conjugators reduced; g has 657 letters and cancels; the free product of the cells equals the rev-4 word (with and without g). The C3|6|21 row in the same file is identical to the earlier certified one. Not checked: the bridge fix or the mixer path (irrelevant for L0).
### B. rev-5 draft (registry-rev5-draft, revision 5)
- Moved set: the 62 ids that left the candidates (rev 4 vault file, 200 -> 138) equal exactly my 61 confirmed ids plus C3r2|2,2|8; the new tested ids (27 -> 89, 62 new, no duplicate ids) are the same 62; the 27 old tested records are unchanged.
- Remaining 138 candidates: all are rev-4 candidates; the records are byte-identical (canonical json) to rev 4, words included.
- Replay of the 62 new tested records: registry_word equals the rev-4 candidate word, registry_word_length is correct, word is empty, levels L0-cert / none, all cores literal reduced fifth powers, conjugators reduced, red(product of the certificate chain . g^-1 g) equals the registry word: 62 of 62.
Not checked: the build script itself, diff_summary beyond the moved list, the other registry fields (W, labels, notes).
