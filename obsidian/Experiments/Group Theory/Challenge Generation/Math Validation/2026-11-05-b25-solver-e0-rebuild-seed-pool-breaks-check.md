---
type: validation
date: 2026-11-05
agent: Validator
status: L0-cert CONFIRMED for all 16 lines; route CONFIRMED structurally (hit rotations not recorded)
---
# Validation: E0 rerun breaks C3|4|15, C3|4|22, C1|6|1 repeats

Triage: [[2026-11-05-b25-solver-e0-rebuild-seed-pool-breaks-check-triage]]. Input: the rerun job outputs (shortenings.jsonl, m2_inputs.jsonl, results.jsonl, summary.json, e0.log), registry rev 3. No word strings in this note (ids and numbers only).
Model check: all checks are free reductions in F_2 with my own code (no tcgraph, no finite quotient). Convention: a cell (c, x) is the word x^-1 c x; L0-cert = free-reduced product of such cells, every c a literal fifth power, equals the target word (g^-1 out g is trivial because out is empty).

## 1. Replay (L0-cert): 16 of 16 CONFIRMED
For every line of shortenings.jsonl: out_word empty; every core is a literal reduced fifth power; conjugators freely reduced; red(product of cells . g^-1 out g) equals the rev-3 registry word of the target; g^-1 g cancels.
| target | lines | cells | max period | |g| |
|---|---|---|---|---|
| C3|4|22 | 1 (raw 16311) | 41 | 16 | 187 |
| C3|4|15 | 5 (raw 13314, 16311, 2963; ls5 16581, 3281) | 29, 28, 26, 20, 18 | 22, 20, 20, 20, 20 | 272, 227, 262, 154, 193 |
| C1|6|1 | 10 (9 ls1, 1 raw 285) | 9-12 (ls1), 24 (raw) | 18-20 | 70-166 |
Cells above period 7 are allowed in an L0 certificate (it only needs literal fifth powers). Scope: the certificate proves triviality in B(2,5) of the registry word. It does not say anything about how the solver found it.

## 2. Provenance: no recipe use (CONFIRMED from config, events and code)
- T-blind pool: `blind_pool(n, max_relator_len, seed, ...)` takes no target, no registry and no data file; it samples products of 3-8 conjugates (conjugator length <= 4) of fifth powers of all words of length <= 7 (PatternBoost sampler, `build_standard_relators(7)`). The six pool_measured events for T-blind carry the same pool hash (one pool shared by all targets); v5 likewise has one hash.
- The 16 sources are in m2_inputs.jsonl for the same target with identical word and cells; every source word equals the product of its cells; all source cores are literal fifth powers of period <= 7; all source conjugators have length <= 4 (the sampler's bound). So no source cell has a target-derived shape.
- `T-blind|1|16311` appears in the m2 lists of both C3|4|15 and C3|4|22 with the same word; this is expected from a shared pool and is itself evidence that the pool is not target-specific.
- The recipe exclusion (excluded_recipe_hits) applies to T-in/T-out only; for T-blind there is nothing to exclude, by construction.
- Descendants now have their own ids (`<parent>/lsN`, with a `parent` field in the pool record): my earlier request is met. Sources of the ls lines sit in m2_inputs under those ids.
- Not checked: that the build ran the code at f693f81 (I read the worktree); the re-generation of the pool from seed 1 (needs the compiled sampler).

## 3. M2 route for the 5 raw-source lines (CONFIRMED structurally)
Not stored: the hit (letter automorphism k, rotations of w and u) and the R trace. So I derived the route from the certificate and the source cells:
- For each raw line the 16 letter maps x {inverted or not} were tried; in every case exactly one contiguous block of n cells of the chain (n = number of source cells: 7, 8, 8, 8, 6) has a free product that is conjugate (cyclic reductions equal up to rotation) to the image of the source word u under one letter map; the periods of the block's cores equal the periods of the source cores (as multisets). The other cells are the R-trace cells pulled back (17, 33, 21, 20, 20 cells; periods 1-22).
  | line | letter map (k) | block | trace cells |
  |---|---|---|---|
  | C1|6|1 raw 285 | identity | 0-6 | 17 |
  | C3|4|22 raw 16311 | a->A, b->B, inverted | 33-40 | 33 |
  | C3|4|15 raw 13314 | a->b, b->A | 0-7 | 21 |
  | C3|4|15 raw 16311 | a->b, b->A | 0-7 | 20 |
  | C3|4|15 raw 2963 | a->b, b->a, inverted | 20-25 | 20 |
- Consequence: w = (conjugate of an image of u) . (product of the trace cells) in F_2, exactly the structure w = P1 . P2 of `certificate.py`, so the certificate follows from u (a product of its source cells) plus an R trace whose cells are literal fifth powers. This replays what the certificate asserts; it does not replay the scorer's hit choice or the R search (compiled `tcgraph_ext` not available here).
- The same u gives C3|4|22 (k: a->A, b->B, inverted) and C3|4|15 (k: a->b, b->A) with different automorphisms: the pool word is not tied to one target.

## 4. Why R on w.u^-1 can succeed where R on w failed (comment, partly measured)
Measured: under the identification above, q = cyclic reduction of ru^-1 z' has cyclic length equal to that of psi(P2) (conjugation invariant): 351, 455, 453, 487, 399 letters for the five lines, against |w| = 138, 192, 222, 222, 222. So the M2 word is 2 to 2.5 times LONGER than w in all five cases. Shortness of the input is not what makes R succeed.
Reading (hypothesis, not tested): the greedy R2.5 (cyclic exhaustive 2.5-reduction) is a descent; the registry words are chosen so that R on each of the 16 images of w stalls (S1-each R True). A hit multiplies by u^-1 (conjugated), an uphill move in length that a greedy descent never makes, and u is a product of short-period cells (<= 7) so that the product w.u^-1 cancels into a word whose fifth-power blocks R does see; the trace then uses periods up to 22 although u only has periods <= 7. The sampled u is thus acting like a "move out of the local minimum" for R, and the structure to look at is the cell split P1 + P2 above: 6-8 u-cells and 17-33 trace cells.
Evidence against a simple "u is close to w" story: the group-distance score only picks the pair; the two words are far (cyclic lengths 251-303 for u against 138-222 for w).
Open for the Experimenter: R on the same x for the other T-blind words with the same lcf (the 30 per target are in m2_inputs) to see how often it fails; no test was run by me.

## 5. C1|6|1 repeats
10 lines, all verified-cert on replay. 9 are ls1 descendants whose sources are small (2-3 period-6/7 cells, |u| = 64 or 98 or 96): six distinct cyclic classes up to inversion, four of them a single class of length 64. One is raw (285, 7 cells). So C1|6|1 now has a raw T-blind break, no descendant needed.
Differences from my 2026-11-05 smoke note: its certificate had |g| = 72, here the sibling lines have 70-166; same shape, different run (tcgraph ba72168); not an inconsistency.

## Caveats
- Verified only: L0 certificate replay (16), source-record integrity, structural split. Not verified: hit parameters, R search, pool regeneration, bench-contract run on the current head (needs compiled `tcgraph_ext`).
- cyclic-length numbers in section 4 assume the chain block is the hit's u-part (conjugacy established, exact conjugator ambiguity is only up to the centralizer of u).
