---
type: validation
date: 2026-10-29
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 mixer R1: six new break certificates"
---
# Mixer R1: six new breaks

Triage: [[2026-10-29-t028-mixer-r1-six-breaks-check-triage]]. Method as in [[2026-10-28-t028-mixer-c3r2-2-2-1-check]]; own code (string replay, `wordreduce`), no algo-mixer code, no mixer re-run. Numbers only; words private.

## Verdict: all six CONFIRMED
Each word is a product of conjugates of literal fifth powers in the free group, hence trivial in B(2,5) (L0 certificate), and each equals the public registry word.

| id | letters | cells | cell periods > 7 (max) | path steps (fwd/inv/braid) | rules (kbmag rec, slx) | braid periods | W to word link |
|--|--|--|--|--|--|--|--|
| C1\|6\|9 | 225 | 21 | 5 (18) | 14 (5/4/5) | 6 (6, 6) | 12, 18 | rev-4 chain |
| C3\|4\|19 | 270 | 708 | 9 (23) | 617 (304/303/10) | 26 (25, 26) | 1, 9, 10, 12, 16, 17, 23 | rev-4 chain |
| C1\|6\|0 | 286 | 4195 | 5 (24) | 2901 (1436/1459/6) | 42 (42, 42) | 5, 12, 15, 24 | none: D step |
| C1\|8\|0 | 308 | 83 | 4 (29) | 35 (18/13/4) | 15 (15, 15) | 15, 21, 29 | rev-4 chain |
| C1\|8\|7 | 322 | 74 | 10 (27) | 52 (24/18/10) | 11 (11, 11) | 13, 14, 20, 22, 27 | rev-4 chain |
| C1\|16\|22 | 786 | 440 | 13 (80) | 423 (224/186/13) | 10 (10, 10) | 8, 38, 42, 68, 80 | rev-4 chain |

Checks, identical for all six:
1. **W rebuilds from the public construction.** From `data/b25_challenge_candidates.json` revision 2 (`construction`: t word, sign, x/y per round with round 1 applied first, conjugator, free then cyclic reduction) I rebuilt the original W; it equals the registry `W` (414, 746, 360, 440, 456, 960 letters, matching `W_length`).
2. **Certificate word = registry word.** The certificate's W equals, letter for letter, the registry word, the rev-4 word and the `.word` file. Freely and cyclically reduced; `g` and `end` empty.
3. **Product of cells.** The product of the conjugated cells `c^-1 core c` free-reduces to the certificate word; every core is a literal fifth power; cell counts match the replay JSON.
4. **Link from construction W to the registry word.** Five of the six carry a rev-4 certificate chain W = P g^-1 word g in fifth-power cells; it replays as a free-group identity. C1|6|0 has none: its W-to-word path includes a D step (equality in G_k, uncertified). Its break of the registry word is still a full L0 certificate; only the construction-W link is not.
5. **Path replay** (path files in `r1/outputs/mixer/paths/`): each starts at the registry word, every fwd/inv step reproduces exactly (pattern at position, replacement, free reduction), and ends at the empty word. Every gen_braid step has word_k * word_{k+1}^-1 cyclically equal to a literal fifth power.
6. **Rules.** All distinct rules are freely reduced and reduce to IdWord under kbmag slx; rec fails on one rule of C3|4|19 (25 of 26) but slx covers it. These are G_7 equalities, modulo kbmag.

## Period > 7 flags
Cells and braid steps with a period above 7 appear in all six (counts in the table). Those steps are fifth powers of words longer than 7, so they are valid in B(2,5) but are not G_7 relators: the paths prove B(2,5)-triviality, not G_7-triviality. The rule steps need no flag: all pass kbmag, so they are G_7 equalities. C3|4|19 has a braid step of period 1 (a fifth power of a single letter). C1|16|22 has braid steps up to period 80 (the word has 786 letters).

## Not checked
The beam search and its budgets; the report's counts of the 28 shortened and 21 killed words (not examined); step-by-step kbmag on whole path steps for the long paths (only rules and braid structure).
