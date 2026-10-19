---
type: validation-verdict
date: 2026-10-18
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-024: checks (a)-(d) on the first level-3 onion word (timing rjob 20261018-130149-66017e; ds 519, chain 2, gate B)"
verdict: "CONFIRMED: L0, 2.5-reduced, S2 3 and flip (d) 3 above the components' 2 (parent flip depth 2 confirmed); no cheaper certificate found by our reducers"
---
# T-024: verification of the first level-3 word

This was a Lead task (2026-10-18). The method is the same as for level 2, [[2026-10-18-t024-level2-best-words-verify]], where the terms (L0, 2.5-reduced, S2, flip (d), bouquet control) are defined.

**Input:** `certs/` of the timing job, with sha256 equal to `index.json`:
- the level-3 final `ds519_L3_c2_B` (1,548 letters; 1,871 cells assembled, 1,863 compressed);
- its level-2 parent `ds519_L2_c2` (558 letters, 546 cells compressed).

**Tools:** tcgraph main `ca2ceb9` (b25 `ae6a79c` bindings), the Python references, and my own power detector. Run locally as one capjob (2 GB, 1 CPU), 5.8 h.

| Check | Result |
|---|---|
| (a) L0 | The compressed and assembled certificates expand to the word, and the parent's two expand to its word. Two expanders (C++ and Python) agree. ✓ |
| (b) gate | 2.5-reduced by `power_gates` B and by my independent detector ✓. Not strictly power-free: 2 exact 2.5-powers of period 2, at positions 969 and 1336. |
| (c) S2 / flip (d) | Final: S2 **3**, flip (d) **3** (rule c: 3). Python = C++. |
| parent | S2 2, flip (d) **2**, Python = C++: **the parent flip depth of 2 is confirmed.** |
| bouquet | The components' maximum is 2 (the stored `comp_max`; the parent's depth 2 is re-confirmed here). The tile certificates are not in the dump, so the tile part of `comp_max` was taken from the run (at level 2 the tiles were always S2 1). 3 > 2 under both S2 and flip (d) ✓ |
| (d) cheaper certificate | `full_reduce` and `closure_fixpoint` with inverse cells: the compressed certificate stays at 1,863 under both (31 min each), and the assembled one reaches 1,863 (2.1 h and 2.6 h). All results satisfy L0. **None is cheaper**, so the depth survives. |

**VERDICT: CONFIRMED** for our certificates after our local reducers.
- The word has depth 3 under S2 and under flip (d), one above its level-2 parent's 2 (and above the components' maximum 2).
- It does not exceed the pilot's level-1 maximum of 4.
- Minimality is not established (subset-merge search deferred to T-017).
- L1, novelty and area-likeness were not re-checked; they are taken from the run.

Files (Validator scratch, not committed): `scratch/t024verify/check_l3.py`, with outputs `check_l3.json` and `check_l3.out`.
