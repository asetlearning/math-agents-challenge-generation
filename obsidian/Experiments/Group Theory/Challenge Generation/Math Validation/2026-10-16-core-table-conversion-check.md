---
title: "Cyclic-core conversion of the R7 table for diagram statistics — check"
status: replicated
domain: group-theory
project: challenge-gen
claim: "kbcert.core_table / to_core_cert preserve expansion, N and relator classes; diagram_stats' Euler identity holds over the core table and fails over the raw b25_full table only because of non-reduced cells"
claimant: Experimenter (branch t018-diagram-search @ 10611db)
verification_method: "short proof; random-certificate fuzz; Euler counts on the line 1 and 2 seed certificates over raw, freely reduced and core tables; count of self-shared edges"
tools_used: ["t018 venv python (scratch/seed/core_check.py, core_check2.py), run under capjob 2G/1 CPU"]
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, topic/van-kampen, project/challenge-gen, status/replicated, proof]
---

# Check — cyclic-core conversion (Lead request 2026-10-16, before the T-018 smoke run)
Related: [[2026-10-14-t023-folded-diagram-review]] (where the Euler identity b1 = V_int − spheres was derived), [[t018-t021-diagram-search-2026-10-14]] § Step-0 seed findings.

**Terms.** A *cell* (k, c) is c⁻¹ R_k c. The *cyclic core* of an entry is its cyclic reduction. *b1* is the cycle rank of the dual graph (one dual edge per shared edge class). *V_int* is the number of interior vertices of degree ≥ 3. A *self-shared edge* is an edge class whose two sides lie on the same cell.

## Verdict
| Item | Status |
|---|---|
| (1) conversion preserves expansion, N, classes | **proved** and **replicated** |
| (2) Euler identity: holds over the core table; raw-table failure is caused by non-reduced cells | **replicated**: b1 − V_int equals the number of self-shared edges, exactly, on both lines |
| (3) my T-023 validation unaffected | **yes**: its table had no non-reduced entry |
| T-018 smoke run on the core table | **GO** (math) |

## (1) Conversion
`cyclic_reduce` strips matching end pairs of the freely reduced word f, so f = q · core · q⁻¹ with q = f[: (|f| − |core|)/2]. Then c⁻¹ R_k c = c⁻¹ q core q⁻¹ c = (q⁻¹c)⁻¹ core (q⁻¹c) freely, which is exactly `to_core_cert`. The index list is unchanged (same N), and the core is in the same cyclic class (the classes are defined on cores anyway). Checks:
- every one of the 1,630 entries satisfies fr(R) = q·core·q⁻¹ with a non-empty, cyclically reduced core; the class changes for 0 entries;
- 20,000 random certificates (1–8 cells, random conjugators up to 12 letters): 0 mismatches in expansion, N or indices;
- the line 1 and line 2 seed certificates (N = 28 and 47) expand to their words over both tables.

Core table sha prefix de1eb091796e reproduced. Note: the 1,080 entries that are not cyclically reduced are all also not freely reduced (they are written with literal backtracks), not only "some".

## (2) Euler identity
Same certificates, three tables (folded, uncompressed):

| line | table | b1 | V_int | self-shared edges | spheres |
|---|---|---|---|---|---|
| 1 | raw | 58 | 32 | 26 | 1 |
| 1 | freely reduced (stem q kept) | 17 | 15 | 2 | 1 |
| 1 | cyclic cores | 12 | 12 | 0 | 1 |
| 2 | raw | 75 | 44 | 31 | 0 |
| 2 | freely reduced | 23 | 20 | 3 | 0 |
| 2 | cyclic cores | 13 | 13 | 0 | 0 |

In every row b1 − V_int is exactly the number of self-shared edges. Reason: a self-shared edge class is a dual self-loop, so it adds 1 to b1. It is folded backtracking inside one cell (a spur, or the stem q·q⁻¹), so it creates no degree-≥3 interior vertex. The T-023 derivation assumed cells bounded by cyclically reduced relators, which have no self-shared edges. So the raw-table failure is an artefact of the cell words, not an error in the identity or the folding. Over the core table the identity holds; line 1 even has a sphere and still b1 = V_int (the assertion is only enforced when the diagram is sphere-free). I checked the uncompressed certificates; the Experimenter's quoted numbers are for F*_P (b1 52 vs V_int 22), which I did not recompute.

**Side effect to know about.** Over the core table more reducible pairs are visible (line 1: 7 → 12, line 2: 14 → 20), because mirror cells are recognised once their stems are removed. So every statistic that depends on reducible pairs or compression (F*_R, N*_c, depth, guard ≤2-cell) must be computed over the core table, and pre-conversion numbers from the raw table are not comparable.

## (3) My T-023 validation
It used `products.build_table` on the dataset (the 1,684-entry T-002 table): 0 entries not freely reduced and 0 not cyclically reduced. Its Euler checks and depth statistics are unaffected. The PR #14/#16 guard work uses cores through `relator_classes` and `RelatorIndex`, not diagrams, so it is unaffected too.

**Recommendation (non-blocking).** Make `diagram.fold` (or `annotate`) reject or convert any non-cyclically-reduced table entry, so a raw table cannot silently produce wrong b1/V_int/depth again.

## Addendum — b25 PR #17 @ b6742e0 (fold over cyclic cores), 2026-10-16
`diagram.core_factor` uses the same identity as §1 (c⁻¹ a q a⁻¹ c = (a⁻¹c)⁻¹ q (a⁻¹c)) and `fold` applies it to every cell, so depth, J, enclosed_relator, diagram_stats and annotate inherit it. A freely trivial relator gives q = [] (not reachable with R7).

**End-to-end check (capjob 2G/1 CPU, code extracted at b6742e0).** `annotate` over the raw R7 table (1,630 entries) versus the core table, lines 1 and 2:
- **Before PR #17** (t018 worktree code): raw fails with `Euler check failed: b1=52 V_int=22` on line 1 (the Experimenter's numbers) and b1=32 V_int=18 on line 2.
- **At b6742e0:** all 48 scalar fields are identical between raw and core, including diag_cert_size, N*_c, D_c, b1, V_int, N_deep, maxdepth, depth class, J, depth_sum, deep_core, enclosed_relator and the reducible-pair counts. The only differences are the table sha and `core_converted_c` (raw 2 and 3 cells, core 0).
  - Line 1: 16 cells, N*_c 4, path-like.
  - Line 2: 23 cells, N_deep 6, maxdepth 1, thick strip, J 0.2422.

**Verdict: GO** for merge at b6742e0 (math).

**Tooling note.** The t018 venv has the project installed in editable mode, so `sys.path.insert` does not override it: a check of another branch silently imports the t018 worktree code. I ran with `python -S` and an explicit path, and printed the module file to confirm which code was tested.
