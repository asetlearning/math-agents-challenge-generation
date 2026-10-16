---
title: "Standard guard (b25 PR #14) — math review"
status: replicated
domain: group-theory
project: challenge-gen
claim: "guard.py: (i) the non-increasing 2.5-closure test and (ii) the exhaustive <= 2-cell certificate test are correct, exhaustive and fail-closed; the novelty hook does not change guard_passed"
claimant: Developer (owner decision 2026-10-14, from [[2026-10-14-t016-overlap-chaining-review]])
verification_method: "proof sketches for soundness and exhaustiveness; independent naive closure on 611 finalists; planted <=2-cell fuzz (|w| up to 231); table-closure and hook tests"
tools_used: ["python3 3.12.3 (scratch/guard_check.py, guard_fuzz.py, guard_r7.py)", "b25 branch 22-guard-closure-le2 @ c3c89df (object under test)"]
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, topic/proof-certificates, project/challenge-gen, status/replicated, proof]
---

# Review — standard guard, b25 PR #14 @ c3c89df
Context: [[challenge-gen-success-metrics]] § Standard guard; triage-free review (verification of a pre-existing artifact, within the T-016 review scope [[2026-10-14-t016-overlap-chaining-review]]). Scripts in `Agents/asetlearning/Validator/scratch/`.

**Terms.** A *cyclic word* is a word up to rotation, freely and cyclically reduced. A *table* is a list of relators; its *cores* are their cyclic reductions. A *cell* is one conjugate c⁻¹R_kc; a *k-cell certificate* is a product of k cells that freely reduces to w. The *non-increasing closure* of w is the set of cyclic words reachable by 2.5-moves that do not lengthen the word.

**What a pass means.** "No cheaper certificate was found by these two tests." Never an area statement, and nothing about w being non-trivial.

## Verdict
| Item | Status |
|---|---|
| (a) closure matches my T-016 closure | **replicated**: 0 disagreements with my independent closure on 611 finalists |
| (b) ≤ 2-cell test exhaustive for all \|w\| (arc, vertex, stem, nested) | **proved** under two stated preconditions (§2); fuzz: 5,997 of 5,997 planted words found |
| (c) novelty hook does not change guard_passed | **true in effect, not by construction** (§3) |
| Merge at c3c89df | **GO** (math), with three non-blocking recommendations |

## 1. Non-increasing 2.5-closure (check a)
**Soundness of one move.** A subword s of length LL with period m and LL ≥ 2.5m is a prefix of v^∞ (v = its first m letters). If LL < 5m, let t be the continuation of v^∞ from LL to 5m. Then s·t = v⁵ freely, so s = t⁻¹ in B(2,5), and the code's `new` is t⁻¹. If LL ≥ 5m, s = v⁵·(prefix of length LL−5m), and the code deletes v⁵. The new length is |5m−LL| ≤ LL, so no move lengthens the word.

**Completeness of the search.** LL ≤ n and LL ≥ 2.5m force m ≤ n/2, which is the range of `m`. `ext[s] + m` is the longest period-m subword starting at s, so every LL from ⌈2.5m⌉ to that maximum is tried, from every rotation s < n. Hits are `empty` or a canonical rotation in the 16-image set (8 letter automorphisms × inversion) of a table core. Hitting `cap` returns False (fail-closed).

**Independent check.** My own closure (naive subword scan, no run-length array; own 8-automorphism and inversion class set from the same table) compared with `closure_report` on all 611 T-016 finalists (E1c 204, E1_screen 203, E1d 204), run table (1,640 dataset entries + v⁵, |v| ≤ 3): **0 disagreements** in the hit/no-hit decision and in the reason.

| Run | no hit | relator-class hit |
|---|---|---|
| E1c | 178 | 26 |
| E1_screen | 178 | 25 |
| E1d | 135 | 69 |

On R7 (`b25_full`, 1,630 entries) the guard reproduces Developer's counts exactly: E1c passes 180/204 (24 hits), E1_screen 181/203 (22 hits), none with a ≤ 2-cell certificate. The table-dependent counts differ from the run-table ones because the tables differ, not because the code differs.

**On "words that empty".** All hits reported here are `relator` and none `empty`: a word that reduces to ε first passes through a v⁵ state, which is a table class, so the hit is recorded earlier under that name. This is consistent with my T-016 closure; the 14 E1 and 20 E1c emptied words are among the hits, but I did not re-derive the 14/20 split.

**Premise caveat.** A hit means "w reaches a relator class by non-lengthening moves", i.e. w has a short certificate *if that relator is trivial in free B(2,5)*. The dataset relators are known trivial only in B₀(2,5) ([[2026-09-30-b25-b0-challenge-triviality]]) and automorphic images are used. The guard is conservative in the safe direction (it rejects more words), but a hit is not by itself a triviality statement.

## 2. Exhaustive ≤ 2-cell test (check b)
**Claim.** If w has a certificate with at most two cells over a table that is closed under inversion and whose entries are cyclically reduced, `le2_cell_certificate` finds one. Every returned certificate is re-expanded and compared with w (assert), so positives are sound.

**Proof sketch.** Let w̄ be the cyclic reduction, w = p·w̄·p⁻¹. A two-cell certificate is a van Kampen diagram with two cells; folding it, and removing a reducible pair if there is one (then w̄ has a ≤ 1-cell diagram), leaves one of these.
- **0 or 1 cell.** Empty core, or w̄ a rotation of a core (`_factor`).
- **Two cells sharing one arc π** (they cannot share two disjoint arcs: that would enclose a hole needing a third cell; sharing the whole boundary of the smaller cell is the nested case with β empty). The boundary is αβ with |α|+|β| = n, A = απ, B = βπ⁻¹ cyclically. One piece, say α, has |α| ≥ n/2. Then W = αβ and R = απ are rotations with a common prefix of length ≥ |α| ≥ ⌈n/2⌉ = `amin`, and R⁻¹W freely reduces to π⁻¹β, a conjugate of B. The prefix bucket of length min(10, amin) contains R. If |β| is the long piece, swap the roles of A and B; the table contains inverses so both orientations are in the bucket.
- **Two cells meeting at a vertex or joined by a stem s.** The boundary is A·(sBs⁻¹) cyclically, after folding any cancellation between A and s into a shorter stem. B is a rotation of a core, hence cyclically reduced, so the greedy peeling of matched end pairs removes exactly s, and what remains is B. Rotations W cover every attachment point; the prefix lengths are the core lengths of the table.

**Preconditions (both met by the callers, neither enforced).**
1. The table must be closed under inversion. Test (C): a table of the 820 dataset words without their inverses finds 0 of 800 planted "inverse + forward" pairs; adding the inverses finds 300 of 300. `table_from_kbmag` appends inverses by default and `build_table` includes them, so every current caller is fine.
2. Entries must have non-empty cyclic cores (entries with an empty core are skipped by `relator_classes`).

**Fuzz (independent of Developer's self-test).** 6,000 requested words of four kinds, drawn from the run table. Kinds: real overlaps (rotations that cancel ≥ 6 letters, giving shared arcs), two conjugated cells at a vertex, a stem of length 1–12, and one relator inserted into another's pocket. Every generated word (5,997; 3 arc draws found no overlap) was found. |w| ranges up to 231, and 99 % have |w| ≥ 64, which is the range the earlier script `t016_cheap.py` did not cover. Developer's R7 self-test reports 2,700 of 2,700.

## 3. Novelty hook (check c)
- `standard_guard` ANDs every extra check into `passed`, and `diagram_stats.guard_fields` passes `NOVELTY_CHECKS` and stores `guard_passed = g["passed"]`. So the hook **can** change `guard_passed` in principle.
- In effect it does not: `novelty_check` fires iff the cyclically reduced w is a rotation of a table relator or its inverse, and then `le2_cell_certificate` already returns a one-cell certificate on the same table. Test (D): `passed` with and without the hook is identical on 1,500 of 1,500 words (half of them conjugates of relators).
- It can differ only for a table not closed under inversion, because `relator_class_set` always includes inverses while the guard index does not.
- The row does not record the hook's own result, so a failed novelty check is not distinguishable from a ≤ 2-cell hit.

## Recommendations (non-blocking)
1. `RelatorIndex` should add the inverses itself (or assert closure), since exhaustiveness silently fails otherwise.
2. Record the hook result in its own field (e.g. `guard_novelty_ok`), so `guard_passed` can be decomposed.
3. State in `guard.py`'s docstring that a closure hit uses automorphic images and relators known trivial only in B₀(2,5), and is a screen, not a triviality claim.

## Verdict
**GO** for merge at c3c89df on the math. `#status/replicated` for the closure (independent agreement, plus the earlier brute-force completeness check of the move enumerator); the ≤ 2-cell exhaustiveness is a proof sketch under the two preconditions, supported by the fuzz. Nothing here is an area statement.

## Addendum — PR #16 (guard follow-ups) @ 2f8bd90 (2026-10-15)
Diff c3c89df..2f8bd90 (guard.py, diagram_stats.py, tests; 16 lines of code). All three recommendations are implemented as asked.
- **Rec 1.** `RelatorIndex` appends the inverse of every relator the table lacks, after the given entries; `n_given` records the original count. This removes precondition 1 of §2. Re-run of my test (C): the dataset-only table (no inverses) now finds **800 of 800** planted inverse+forward pairs (before: 0 of 800). Duplicate input entries would add a duplicate inverse, which is harmless.
- **Rec 2.** `guard_novelty_ok` is the hook's own result (`extra["not_conjugate_to_relator"]`; `None` when no hook is run), so a failed novelty check is now distinguishable from a ≤ 2-cell hit.
- **Rec 3.** The docstring now says hits are screens, not triviality claims, and names the B₀(2,5) caveat.
- **Side effect.** `guard_table_size` is the closed index size; `guard_table_sha256` hashes the table as given. Rows from before and after PR #16 therefore differ in `guard_table_size` for the same table. This is a record-keeping point only.
- **Regression checks (code extracted at 2f8bd90).** Closure vs my independent closure on 611 finalists: 0 disagreements, same counts as before. Planted ≤ 2-cell fuzz: 5,997 of 5,997 found. Hook effect on `guard_passed`: 0 of 1,500 differ. I did not run Developer's test suite (pytest is not installed here).

**Verdict: GO** for merge at 2f8bd90 on the math. Precondition 2 of §2 (non-empty cyclic cores) is still not enforced, but is met by every current caller.
