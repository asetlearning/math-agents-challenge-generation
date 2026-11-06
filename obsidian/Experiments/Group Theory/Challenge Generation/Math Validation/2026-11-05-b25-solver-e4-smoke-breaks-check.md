---
type: validation
date: 2026-11-05
agent: Validator
status: both breaks CONFIRMED (L0-cert); pull-back reproduced cell for cell
---
# Validation: E4 smoke breaks C1|6|7 and C1|6|15
Triage: [[2026-11-05-b25-solver-e4-smoke-breaks-check-triage]]. Inputs: E4 smoke outputs (breaks.jsonl, attacks_shorter.jsonl, m2_inputs.jsonl, results.jsonl), E3 fix files (runs E3 and the E4 copy), rev-4 registry (data/, working tree, uncommitted). No word strings in this note. Convention: cell (c, x) = word x^-1 c x.

## 1. Replay (L0-cert): both CONFIRMED
| id | word | cells | max period | |g| | result |
|---|---|---|---|---|---|
| C1|6|7 | 257 | 44 | 25 | 383 | free product of cells . g^-1 g = rev-4 word |
| C1|6|15 | 263 | 52 | 29 | 0 | free product of cells = rev-4 word exactly |
All cores are literal reduced fifth powers, conjugators reduced. The rev-4 words equal the E3 start words.
C1|6|7 is an M2 hit directly on the registry word (loop round 1 = R, CL, KB, D with no change, 257 -> 257). Its break chain equals the attack line `T-blind|1|111` (out empty). Of the 10 attack lines, 7 have an empty output (6 T-blind, 1 v5) and 3 give a 249-letter word (shorter, not breaks); I replayed all 7 empty-output lines: each is a valid L0 certificate of the registry word (41-44 cells).

## 2. C1|6|15 pull-back through phi^-1, step by step: CONFIRMED
Route (E3 fix file, round 1): W (263 -> 242), R (242 -> 229, 13 trace cells, rotation of length 2), then CL, KB, D and a second R, CL, KB, D with no change (229 -> 229). The loop end word (229) is an automorphic image (automorphic_image true). M2 then kills the 229-letter word.
1. Chain of words: start_word = registry rev-4 word; W.in = start; W.out = R.in; R.out = loop end word of 229 letters.
2. W step: phi_inverse a->a, b->ab, conjugator and start empty. phi: a->a, b->Ab; I checked both compositions give the identity on the generators. The relation in = phi_inverse(cj) . phi_inverse(out) . phi_inverse(cj)^-1 holds exactly (cj empty). The map is an elementary Whitehead automorphism.
3. R step: in = (product of 13 trace cells) . rotation . out . rotation^-1 holds exactly in F_2; trace cores are literal fifth powers of period 1.
4. M2 certificate on the 229-letter word (attack line `T-blind|1|1390/ls4.0.0`, 39 cells, g non-empty, out empty): the product of its cells equals the 229-letter word.
5. Independent pull-back with my code: through R: the 13 trace cells plus the 39 M2 cells with conjugators multiplied by the inverse rotation (52 cells; product = the 242-letter R input, exact); through W: each core u^5 goes to phi_inverse(u)^5 written as p s^5 p^-1 with s cyclically reduced, conjugator p^-1 phi_inverse(x) phi_inverse(cj)^-1 (52 cells; product = rev-4 registry word, exact; all cores literal fifth powers).
6. The result is identical, cell for cell and in order, to the break chain in breaks.jsonl (52 cells, g empty).
Extra: the same pull-back applied to all 100 empty-output attack lines of C1|6|15 (T-blind and v5) gives 46-64 cells whose free product equals the registry word, cores literal fifth powers, in each of the 100 cases. So the pull-back is not special to the one chosen line.
Scope: this replays what the certificate asserts. The W choice, the R search and the M2 hit were not re-found.

## 3. Provenance (CONFIRMED from files and the earlier code review)
- Sources: the breaking sources (T-blind ids 111, 440, 1002 for C1|6|7; 1390/ls4.0.0, 1005, 214 for C1|6|15) are in m2_inputs.jsonl for the same target with identical word and cells; word = product of cells; cores are fifth powers of period <= 7 (v5: <= 5); conjugators of length <= 4; the 1390/ls4.0.0 descendant has a parent record `T-blind|1|1390` in m2_inputs, and C1|6|15 also breaks from raw words (1005, 214, ...), so no descendant is needed.
- T-blind pool: target-independent (see the E0 note: `blind_pool` takes no target or registry). E4 uses the same pool function with seed 1, pool 2000.
- Loop round 1 from E3 files: the E4 copy of the fix files has steps identical (byte for byte after canonical json) to the E3 files, for both ids; the E3 input held only the word (no recipe), as checked in my E3 note. E3 did not use rev-4 data except through start_word, which equals the rev-4 word.
- Not checked: that the E4 code used the pools as written; regeneration of the pool from seed 1.

## 4. M2 split (as before)
In each of the six lines a contiguous block of the chain, with n = number of source cells, is conjugate to a letter-map image of the source word u:
| id | source | n (periods) | block | letter map |
|---|---|---|---|---|
| C1|6|7 | 111 | 8 (5,6,6,7x5) | 36-43 | map 7, inverted |
| C1|6|7 | 440 | 7 | 35-41 | map 7, inverted |
| C1|6|7 | 1002 | 6 | 35-40 | map 4, inverted |
| C1|6|15 | 1390/ls4.0.0 | 5 (5,5,7,7,7) | 0-4 | map 2 |
| C1|6|15 | 1005 | 4 (5,7,7,7) | 0-3 | map 6 |
| C1|6|15 | 214 | 5 | 0-4 | map 2 |
The other cells (36, 35, 35 for C1|6|7; 34, 33, 34 for C1|6|15 before the 13 pulled-back trace cells) are the R-trace cells (periods up to 25 here, 19-29 after pull-back). So w = (conjugate of an image of u) . (R trace) in F_2, as in the E0 rerun note. Hit and rotations are not stored.
(Letter maps are indices into my enumeration of the 8 signed permutations; not the solver's numbering.)

## Remarks
- The v5 pool (relators of length <= 5 only) also breaks both targets (empty-output lines: C1|6|7: 1 v5 and 6 T-blind; C1|6|15: 86 v5 and 14 T-blind); the restriction to period <= 7 in the blind pool is not what makes the breaks possible.
- C1|6|15's break uses the registry word through the automorphic image; the automorphism is the same elementary W as in the E3 fix file.
- The registry data file in the working tree is revision 4 and modified (uncommitted); my replay used it.
Caveats: verified are L0 replay, pull-back and source integrity. Not verified: hit parameters, R search, pool regeneration, bench-contract run on the current head.
