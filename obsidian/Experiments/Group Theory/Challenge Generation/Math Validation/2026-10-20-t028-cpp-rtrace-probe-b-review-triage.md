---
type: triage
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: code review of the C++ R trace (reduction2_5) and the B-probe sampler (probe_b/), tcgraph worktree tcgraph-t028, branch feat/t028-pilot-cpp from 63564c3 (uncommitted)"
---
# T-028 C++ R trace + probe_b: triage

These are two Lead requests (2026-10-20). Both are covered in one review note: [[2026-10-20-t028-cpp-rtrace-probe-b-review]].

**R trace asks:**
1. The traced reducer returns the same word as the untraced one on every input. The word sets are the 351 pool words, the T-024 originals, the T-027 chain words and synthetic words.
2. Each cell is a literal u⁵ with a conjugator (rotation included), and the composition reproduces the output.
3. The untraced path is unchanged in behaviour and speed. To check speed, I time a pin-63564c3 build against the branch.
4. The code follows tcgraph's style and reuses existing code.

**probe_b asks:**
- The probe implements pre-registration §B, r6 and r7.
- "Closed" and "2.5-reduced" are decided correctly.
- It is deterministic in (seed, index).
- It reuses existing code.
- Its output JSON gives what the drop/pause rule needs.

**Method:**
- Read the code.
- Build my own copies (out of tree, in my scratchpad) of the branch and of the 63564c3 pin.
- Write two independent drivers:
  - an equivalence, free-group identity and timing driver;
  - a brute-force window-exponent and cell-product checker for samplePatch.
- Run the gtests.
- Everything runs under capjob at 2 GB / 2 CPUs, one job at a time.

**Spotted on reading (to confirm):**
- The pre-registered beam width is **64** (§B). The code default and the Developer's measurement use **50**, the per-setting denominator.
- The JSON has no seed, no instance index and no code version, and it caps the examples at 3.
- probe_b duplicates `word.h` helpers on `std::vector<int>`, and `insertAt` takes `std::vector<int>` in a public API.
- The R trace changes existing functions (approval rule) and uses output-pointer parameters.
- `PowerCell` sits next to `ExponentCell`, and the two use opposite composition orders.
- The top-level CMakeLists adds `probe_b`.

## Re-check after the Developer's fixes (triage, 2026-10-20 evening)

Lead request: re-check only the touched parts. Results go into a new section of [[2026-10-20-t028-cpp-rtrace-probe-b-review]].

**Asks and method:**
1. **R trace after the refactor** (internal helpers return structs; library `cellsProduct`): rerun my 27,328-word equivalence and identity driver, and the untraced timing against the 63564c3 pin build.
2. **probe_b:** read the new JSON fields (seed, revision, indices, all closed patches); run the app twice and diff; rerun `pbcheck` and the unit tests; check beam 64 and distinct mutation positions.
3. **kbcert:** the golden test with the environment set; R3 at cap 10⁶ against the registry certificate, with my independent Python L0 check.
4. **New `PowerCellCertifier`:** read it for soundness (every certified cell L0 over R7, checked against the table; "uncertified" reported, never silently dropped); run it on the long R-trace cells from my substitution set, and L0-check its output independently.
5. Judge whether keeping `ExponentCell` and `PowerCell` separate is acceptable.

All builds and runs under capjob (2 GB / 2 CPUs), one job at a time.
