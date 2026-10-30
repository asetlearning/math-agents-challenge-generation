---
type: validation
date: 2026-10-30
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "Review of challenge-gen-candidate-workflow.md against bench 7d435cf"
---
# Workflow note review (verdict)

Triage: [[2026-10-30-t027-workflow-note-review-triage]]. Read-only: I read `bench/` (README, verify.py, budgets.json, test_candidate.py, accept.py, top_run.py, jobs.py, ladder_run.py), the t028 `gates.py`, `heldout.py`, `kb.py`, `fix12.py`, `certify_survivors.replay_chain`, and the registry note [[ds-b25-challenge-candidates]] and [[challenge-gen-success-metrics]]. Nothing was built or run. The Acceptance result is pending and not reviewed.

**Verdict: sound in structure; 7 corrections before commit (3 of them are overstatements).**

## What matches the code
- Step order: fix loop, T3u gate, held-out, top rung, reducer ladder, recorded rerun, certification (README stages 1 to 5, `classify`, `stage_ladder_input`, `stage_after_ladder`).
- Loop parameters: 12 tie-break orders, D 10^8 cosets with relators up to length 7 (budgets.json `fix`), KB rec/slx on 16 images, CL periods up to 7.
- Ladder table: M1-gen b25_gen 1024/300 s, M2-all merged six 1024/300 s, M3-allwide merged six 4096/900 s, max one pass each, at most 3 levels; a proved word leaves, survivors move up at their shortest end; recorded rerun only for proved words. "Merged six" is b25_gen + rec + slx (the file `r2`) + rpo + rpo_rtl + shortlex.
- Contract for `bench solver` and its budget (time, memory, threads); counts 8 / 207 / 38 for `bench accept`.
- `verify_break`: solver certificate, else closure-search certificate, else kbmag, else `unverified`. `verify_shortening` forms the loop `word . (c out c^-1)^-1`, as written.
- `replay_chain` is a definition-level replay: it rejects any core that is not a literal fifth power and compares free reductions. So `verified-cert` is a proof in free B(2,5).

## Corrections
1. **`verified-kb` is a proof only modulo kbmag, with no replayable object.** A reduction to IdWord is an equality in G_7 (derived by Knuth-Bendix from the G_7 relators); G_7 maps onto B(2,5), so the word is trivial in B(2,5). That is sound, but: (a) it rests on kbmag's correctness and on the systems being exactly the G_7 ones; (b) `verify.py` takes the systems from the environment (`KBMAG_SYSTEMS_DIR`) and records only the system name, not a hash, so a wrong directory would verify wrongly; (c) it is not a certificate. Write "proof modulo kbmag (G_7 equality)", record the sha256 of the system files in the verification result, and say that a registry removal needs `verified-cert` (see 2).
2. **Section 4 and the table disagree.** §4 says a broken candidate moves to `tested` "with its certificate", but §2 lets a `verified-kb` break count as verified. Either require `verified-cert` for a registry removal (my recommendation: the registry rule is certificates wherever practical, and kb breaks can be upgraded by the closure search), or say that a kb-only break is recorded with `certified: false`.
3. **Shortening check, incomplete description.** The conjugator is the one the solver gives; if it gives none, the code tries 21 (none, one letter, two letters). A cyclic output that differs by a longer conjugator is `unverified`: sound, incomplete. Say so. Also list the strongest outcome: the loop reduces to the empty word by free reduction alone (`verified-cert`, method "free reduction"). The check proves word = c out c^-1 in B(2,5); it gives out = 1 only because the candidate word is trivial, which is the case for registry words.
4. **Plain-English box overstates.** "Every step that removes or shortens a word must be backed by a proof that can be checked independently" is false for D steps (15 candidates) and for `shortest_known` (38 words, `certified: false`). Say: a removal needs a replaying certificate; a shortening is recorded with whether it is certified.
5. **Step 4 (held-out).** The held-out kbmag solvers are the two other rewriting systems `ho_slx` and `ho_rec` (other orderings) on all rotations of the word, not "kbmag on the other images". The deep rung is D<->R alternation (rml 7) on the ladder 2^24, 10^8 and 10^9 cosets (`top_run` runs the 10^9 rung for every word that passed), not plain "D at 10^9". The same wording slip is in the bench README.
6. **Step 3 (gate).** State that D1 in the gate is D(20M, rml 5) on the identity image only (`chain.D_BOUND`, `gates.py`), not the loop's D; and that S2-chain is evaluated after the gate (on the identity image, only when S1-each holds) and is reported with T3u but is not part of the gate's test. A word that fails the gate is `broken-gate` in `classify`; the note's "a word that breaks is recorded under tested" should say that gate failures are labelled, not discarded.
7. **Step 5 and §3.** (a) "A word the reducer shortens goes through R once more": the code runs the whole fixpoint loop again on the shortened end (`fix2`, `skip_unchanged`); a word the loop leaves unchanged gets no gate, held-out or certificate, a changed one does. (b) "`bench accept` ... replays every certificate of the revision": it replays only the `tested` records with a `certificate_chain` and a `registry_word` (the 8 reducer breaks); it does not replay the 200 W-to-word chains nor the revision-1 R7 certificates. Say "the 8 certificates of the broken words".

## Not reviewed
Pending Acceptance sample; the process claims (who replays what) beyond the code; `finish.py` record assembly beyond `classify`; the unit tests.
