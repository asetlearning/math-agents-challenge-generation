---
title: "T-016 overlap chaining review — triage"
status: conjectured
domain: group-theory
project: challenge-gen
claim: "Chains are rewriting paths, not area; cheaper certificates; L0 of the D_path ≥ 1 words; all-classes novelty guard"
claimant: Experimenter (via Lead)
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, topic/proof-certificates, project/challenge-gen, status/conjectured, triage]
---

# Triage — T-016 review
Written at the start of the work, finalised after the checks (each took seconds to minutes). Source: [[t016-overlap-chaining-2026-10-14]] § Results; b25 `21-t016-overlap-chaining` @ 75b426b; run `~/Research/challenge-gen/runs/t016-20261014/walk_E1_screen/`. Scope extended by Lead to T-023 (PR #13), which gets its own note.

- **Premise/model:** all statements are about free B(2,5) = F/⟨⟨u⁵⟩⟩ and about identities in the free group F(a,b). The dataset relators are trivial in free B(2,5) by the dataset's kbprog proof ([[ds-b25-trivial-2-5reduced-aut8-20261014]]); I take that as given, not re-proved (same conditional as T-001).
- **Sub-claims:** 1 geometry (strip, |w̄| bookkeeping, D_path vs area); 2 cheaper certificates; 3 L0 of the D_path ≥ 1 words; 4 novelty-all guard, correctness and sufficiency.
- **Tools:** python3 3.12.3, own scripts only (`scratch/t016_*.py`, `t001_search.py`, `t001_trace.py`); the dataset file (sha256 e0eeb777…); harness outputs read as data.
- **Methods:** 1: bookkeeping check + finite-family argument; 2: exhaustive area ≤ 2 test over the 1,640 relators (with a positive control), heuristic depth-2 for 3 cells, step-checked rewriting over {u⁵} and its full non-increasing closure; 3: independent re-expansion; 4: code reading + the closure as an independent re-check.
- **Limits:** no lower bound on area over any relator set; 3-cell search over the dataset relators is heuristic.
