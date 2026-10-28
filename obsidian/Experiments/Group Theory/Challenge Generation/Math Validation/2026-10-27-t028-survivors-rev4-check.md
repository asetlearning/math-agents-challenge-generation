---
type: validation
date: 2026-10-27
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 survivors rev 4 (220 words) independent check"
---
# Survivors rev 4 check

Triage: [[2026-10-27-t028-survivors-rev4-check-triage]]. File sha256 c0e22bb0... (matches the request). Ids and numbers only; words stay private. Scope: my own replay and diff code; D steps, the T3u gate and held-out ladders were not re-run.

## Results
1. **15 changed records.** 15 = 12 (fix12) + 3 (fix215); no other word differs from rev 3.
   - Each stored word equals the final word in the matching `fix_<id>.json` (fix215 file for the 3 fix215 words, fix12 file otherwise); the fix215 start word equals the rev-4 word for the 10 fix12 fixpoints, so fix215 ran on them at their new length. `length` equals the word length.
   - `history` keeps the rev-3 word and length as its last entry; the rev-3 history is kept in front where it existed; the rev-3 `reproduction.steps` are a prefix of the rev-4 steps (new steps appended, continuity holds, each ends at the stored word).
   - No old escalation or ladder label survives: all 15 carry "escalation NOT re-run on this word" and the held-out label for the new word (kbmag ho_slx/ho_rec and D<->R rml 7 up to 10^9 not broken); the `escalation` verdict reads "not re-run". The 2 broken ones carry only the BROKEN and certification labels.
2. **fix215 changes.**
   - C3|4|1 492 to 418 (R, 1 step) and C3r2|2,3|22 568 to 565 (R, 1 step): R cells are literal fifth powers and replay as free-group identities. Both certificates replay: chain W = P g^-1 word g holds against the rev-3 W, and the L0 product over the per-word table equals the new word (28 and 42 = max period, cell counts 1046 and 1121 match). Both words trivial in the 5^34 quotient (necessary only).
   - C1|6|0 288 to 286: the only new step is a D step (rml 7, 10^8 cosets), an equality in G_k and not certifiable; it is correctly listed under `not_certified` and the certificate is removed (it had one in rev 3). Trivial in B0.
3. **Counts.** Status: 215 not a candidate, 5 broken (C1|24|29, C3r2|2,3|1, |3, |9, |19). T3u 215. Certificate chains: 204 (= rev 3's 205 minus C1|6|0). That 204 includes 4 broken words (|1, |3, |9, |19); among the 215 live words 200 are certified and 15 are not. All 15 changed words are trivial in B0, as are the 3 rev-3 emptied ones. Structural check over all 220: freely and cyclically reduced, exponent sums multiples of 5, `length` correct.
   - The 12 fix12 and 3 fix215 records replay as in [[2026-10-27-t028-fix12-check]]: every adopted R step and every length-changing KB step (images 0 and 1, rotations 0, 3, 6, 43) replays with equality proven by wordreduce in both systems; the 3 adopted D steps (C1|6|0, C3r2|3,3|23 and nothing else new) are listed.
4. **202 unchanged records.** All 205 non-changed records equal rev 3 except the `fixpoint` block (which the 202 live ones and the 3 rev-3 emptied ones all carry; the emptied ones say "not run: already broken"). Top-level `description`, `code`, `inputs_sha256`, `change_log` differ as declared.

## Not checked
The T3u gate and held-out D ladders (10^8 / 10^9) for the 15 words, fix215's 212 no-change verdicts (not re-run), and the D steps.
