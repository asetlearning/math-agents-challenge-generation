---
type: validation-verdict
date: 2026-10-17
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "tcgraph PR #5 (T-018 C++ port, 2c264fd) and PR #6 (consolidation, f2cb8a1): math-layer equivalence with the Python reference"
verdict: "PR #5 GO; PR #6 GO (one stale-comment nit, coverage gaps recommended as follow-up tests)"
---
# tcgraph PR #5 / #6: math-layer review

Triage: [[2026-10-16-t018-restart-negative-and-tcgraph-pr5-pr6-triage]]. The request was Lead's (owner-approved, 2026-10-16): does the C++ preserve the Python reference semantics (certificates, folding, depth and strict depth, guard, expansion)? It also asked for the coverage gaps in the equivalence tests and, for #6, the expandFactor change and the hash and relator-builder equivalences.

**VERDICT: PR #5 GO. PR #6 GO.** Scope: the math layer only, against b25 `t018-diagram-search` @ 03da2f7 (the Python reference). Build, packaging and search-loop performance were not reviewed.

## What was checked

Both builds came from clean archives: b25 03da2f7 plus tcgraph 2c264fd (PR #5) or f2cb8a1 (PR #6), each in its own scratch tree. Python ran with `python -S` and explicit paths, and the module paths printed at start confirm that the scratch tree and the scratch `.so` were the ones loaded.

1. **Code reading (side by side with the Python):**
   - `coreFactor` vs `core_factor`, raw→core conjugator conversion (q⁻¹c): identical.
   - `diagram_fold.cpp` vs `diagram.py` fold: lollipop concatenation, stem pairs, leftmost free-cancellation matching, union-find on edges and vertices. It matches line by line.
   - `strict_depth.cpp` vs `t018/scripts/strict_depth.py`: S2 absorption of |v| = 1 cells (cells whose root has length 1) before every layer, the empty-layer break (unreached cells get no depth), and the N < 9 handling of T_deep / T_depth. They match.
   - Depth profile: matches.
2. **ctest:** 15/15 pass on both PRs.
3. **Own equivalence fuzz** (`Agents/asetlearning/Validator/scratch/restart/fuzz_eq.py`; outputs `fuzz_pr5.out`, `fuzz_pr6.out`). The comparison is whole-dict equality of Python vs C++ results, and when one side raises, the other must raise too.

| Section | Inputs | PR #5 | PR #6 |
|---|---|---|---|
| A: strict depth + diagram_stats | 2,244 certificates from the 374 restart states (full, random sub-certificates, planted a⁵/b⁵ cells, perturbed and empty conjugators) | 2,244 / 2,244 equal | same |
| B: same | 3,000 random small-table certificates (commutator, a⁵, b⁵, (ab)⁵, a non-freely-reduced relator; grids, a⁵/b⁵ shields); S2 maxdepth spread 0: 4,504, 1: 646, 2: 93, 3: 1 | 5,244 strict depth equal; diagram_stats 5,224 equal + 20 raise on both sides; 0 fails | same |
| C: `expand_factor` | 1,630 raw R7 entries × (empty, random conjugator) vs `free_reduce(Python expand_factor)` | 2,180 equal, **1,080 differ** (the old unreduced return for an empty conjugator, as expected) | **3,260 / 3,260 equal** |
| C: `expand` | 3,000 random | 3,000 equal | 3,000 equal |
| D: guard | all 138 distinct restart and finalist words: full `standard_guard` dict, `closure_report`, `le2_cell_certificate` | 138 / 138 on all | same |

## PR #6 specifics

- **expandFactor always free-reduces.** This is the one behaviour change, and it is correct. Every b25 Python caller already free-reduces the result, and the binding `expand_factor` is not called from b25 Python, so no caller changes. Section C confirms PR #6 equals `free_reduce(expand_factor)` everywhere.
- **RollingHash:** same constants and formulas as the code it replaces (read). findSquares and loopErase return the same values; `squareBases` keeps insertion order.
- **buildStandardRelators** (moved to the core): `(w^5).cyclicallyReduce()` replaces `.reduce()`. For a cyclically reduced w the two are equal, and the builder only gets cyclically reduced bases. The guard now uses `rm.words()`, and section D shows the same guard output.
- `Word::random(seed)` is additive.

## Findings

- **Nit (PR #6):** `certificates/tests/test_certificate_reduction.cpp` lines 114 and 131 still say expandFactor returns relators unreduced for an empty conjugator. That is stale after #6.
- **Coverage gaps** in the PRs' own tests (not blocking; my fuzz covers them this time, and I recommend adding them as tests):
  1. strict_depth is tested only on run states (smoke15, full_r7_mac). There is no random or small-table test, so no test reaches S2 maxdepth ≥ 2 or the unreached-cell branch. Section B reaches both.
  2. The guard test compares only `passed` / `extra`, on 40 run words per file. It does not compare `closure` or `le2`.
  3. The cpp_restart words, whose guard was computed in C++ only, are not in any test.
  4. No test covers `expand_factor` with an empty conjugator against a reduced reference. That is exactly the case #6 changes.

## Not checked

- The b25 pytest suites (`hardness/tests/test_cpp_*.py`, the t018 tests) were not re-run against my builds. The fuzz above is a superset for the math layer but not for the binding signatures.
- Search-loop code (`search/`) beyond the functions it calls from the math layer.
- Performance.
