---
author: maumayma
date: 2026-07-23
tags:
  - agent/lead
  - user/maumayma
  - domain/group-theory
  - project/b25
  - status/merge
  - review
---

# Code Review — v2 Stage B Increment 2: MCTS/PUCT macro search

Branch `feat/patternboost-b25-loop-v1`. Files: ADD `macro_search.py` (283L), ADD
`tests/test_macro_search.py` (14); EDIT `macro_moves.py` (`verify_atlas` + `max_period` plumbing),
EDIT `tests/test_macro_moves.py` (+5 atlas tests). Spec [[v2-rewrite-path-policy-spec-2026-07-22]]
§4/§5/§7; plan [[stageB-increment2-macro-search-2026-07-23]]. Scope [B0(2,5); free-B(2,5) OPEN].

## VERDICT: MERGE (code quality) — math gated on Validator; commit gated on Maria

**Patch summary.** Net-free MCTS/PUCT grow-then-shrink search over the increment-1 macro cells
(node value = real reducer residual, no learned net yet). §4 temp-expansion budget (grow ≤
path_best + max_expansion, ≤ max_insert_apps insertions/path, prune-no-progress). Witnessed
`word_path` + `move_names` certificate; `validate_result` routes the endpoint through the shipped
`sanity_gate` (provenance="reducer"). This is the discovery *machine*; whether it *finds* a
beyond-rotation reduction (K1/K3) is the empirical Stage B question, not what this increment shows.
Also folds in the inc-1 hardening: rec-i `verify_atlas` fail-fast at ingestion, rec-ii per-cell
`cell_preserves_b0` on relator_complement cells only, and a `max_period=256` cap on the O(n²) span
scan (covers the K4 U=71 scale).

**Data-model verdict: SOUND.** Every edge is a §2a-signed cell (no new surface); budget correctly
enforced; certificate reconstructed root→best. `verify_atlas` verified (fail-fast `is_identity` per
relator). Clean, modelled on `rollout_search.py`.

**Tests verdict: PASS — I ran them.** 40 (macro_search 14 + macro_moves 26) incl. a constructed
grow-then-shrink WIN and GAP-backed every-path-step B0-preservation (ran, not skipped) + atlas
fail-fast. Full suite **211 passed, 2.95s, no regression**.

**Doctrine:** no violations; surgical; no bogus-shit. **Userspace:** none. **Scope leakage:** none.

**Review note (non-blocking for merge; FIX before any RECORDED reduction).** `result.word_path`
starts at `root_residual` (the reduced original), NOT the original word — the initial reducer step
`original → root_residual` is not in the witnessed certificate. Validator's per-output beat-beam gate
requires start=original char-for-char (per the 2-beat verdict), so the caller must prepend `original`
(+ the reduce step) for a complete certificate. `validate_result` itself is sound via the
`best_word =_{B0} original` check; this is certificate completeness for recording. Routed to Validator
for a ruling; Developer to align with it.

**Advisory (inherited):** `exact_power_spans` O(n²) now capped by `max_period=256`; revisit if
self-play needs larger periods.

**Math gate:** routed to Validator (sanity_gate wiring on =e targets + the word_path-completeness
ruling + no-new-surface confirm).

**Commit gate:** NOT committed — Maria's standing "working as intended" constraint. This is the search
machine, not yet a working discovery (= a Validator-gated beyond-rotation reduction). Next on-branch,
uncommitted: wire the certificate fix + run on real words to test K1/K3.
