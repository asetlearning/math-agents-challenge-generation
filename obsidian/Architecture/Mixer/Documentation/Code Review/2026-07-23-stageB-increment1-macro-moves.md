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

# Code Review — v2 Stage B Increment 1: macro-keyed move engine

Branch `feat/patternboost-b25-loop-v1`. Files: `experiments/burnside/b25_patternboost/macro_moves.py`
(ADD, 340L), `tests/test_macro_moves.py` (ADD, 187L). Spec [[v2-rewrite-path-policy-spec-2026-07-22]]
§3b/§4/§9; plan [[stageB-increment1-macro-moves-2026-07-23]]. Scope [B0(2,5); free-B(2,5) OPEN].

## VERDICT: MERGE (code quality) — math gated on Validator; commit gated on Maria

**Patch summary.** The deterministic §3b substrate: `global_features(W)` (abelianization, run-length
histogram, X-core motif map + reversed inverses, maximal exact-power spans = macro-period, seams) +
three macro-cell proposers (exact-U⁵ collapse, relator-insertion `c·U⁵·Inv(c)` at seams,
relator-complement delete). Net-free, search-free — the substrate a later learned policy ranks.

**Data-model verdict: SOUND.** The load-bearing design choice — *no new soundness surface; every
`MacroCell` is ONE already-Validator-signed §2a primitive, only positioned/keyed by global structure*
— is exactly right and keeps the risk surface to positioning/spelling. `MacroCell` with stale-span
guards (`apply` raises if the anchored span drifted) + `cell_preserves_b0` GAP backstop is clean.
Element preserved by construction: `U⁵=e` (collapse/insert), delete-verified-relator (complement).

**Tests verdict: PASS — I ran them.** 21 new (0.53s) incl. the load-bearing **negative** gate-3 tests
(near-miss + too-few-repeats NOT collapsed — collapsing a non-power would change the element),
gate-2 `Inv('ab')=='BA'`, macro-keying (insertions at seams only), stale-cell guards, and **3
GAP-backed element-preservation tests that RAN** (`b0.equal(W, cell.apply(W))` per kind). Full suite
**192 passed, 3.09s, no regression**.

**Doctrine:** no violations. Boring-in-the-good-way, surgical (new module), no bogus-shit.
**Userspace:** none (pure new experiment module; no mixer protocol / pyo3 / KBMAG). **Scope leakage:** none.

**Advisory (NON-blocking, no fix required to merge):**
1. `exact_power_spans` is O(n²) worst-case (max_period × n scan). Fine now; on 28k-char words called
   *per MCTS node* in Stage B self-play it may bite — consider a suffix-structure / bounded-period
   fast path before scaling.
2. `propose_relator_complement` trusts the caller's `atlas` = verified relators (documented contract,
   backstopped by `cell_preserves_b0` + the per-output Validator gate). Keep the contract explicit at
   every call site.

**Math gate:** routed to Validator (element-preservation of each cell kind; the =e claim for
`c·U⁵·Inv(c)` any c,U; atlas-trust fencing). MERGE on the math layer requires its #status.

**Commit gate:** NOT committed. Per Maria's standing constraint (no commit until the PatternBoost code
is "working as intended"), this is a substrate increment, not the working discovery system — the commit
decision is Maria's, and the commit ritual (explicit y/n) applies. Next increment proceeds on-branch,
uncommitted.
