---
title: "Kourovka 21.52 — rank-two all-colour intersection refinement log"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: proof
strategy: RANK2-ALL-COLOUR-INTERSECTION-REFINEMENT
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/coherent-configurations
  - project/kourovka
  - status/draft
---

# Active-time ledger

- 2026-08-18T00:54:00Z — work start at official cumulative active minute 82. Read in full, in the order directed: common protocol; problem-agent protocol; canonical scope revision 1; `psln2-rank2-nilpotent-incidence.md`; `psln2-rank2-decorated-fibre-collision.md`. Problem-21.52 inbox then contained no file, so no Lead `DECISION` authorizing the new strategy was available. Entered `awaiting_lead`; no mathematics or computation begun. Cumulative active time remains 82 minutes pending authorization.

# Assignment fidelity

- Exact universal target retained: every finite nonabelian simple `L`, every *single* conjugacy class `D` of involutions, complete graph on `D` coloured exactly by the product order `|ab|`, and every permutation preserving every exact order-colour must be the restriction of an automorphism of `L` stabilizing `D` setwise.
- Assigned partial lane only: rank-two square-zero class `I+N` in `PSL_n(2)=GL_n(2)`, `n>=4`.
- Excluded: all-involution unions, product-conjugacy-class colours, the underlying uncoloured graph, Problem 21.53, and fixed-family evidence presented as a universal proof.
- Mandatory prior obstruction retained: the common-colour-2 monochromatic-`K_6` predicate has a genuine same-fibre/cross-fibre collision in `PSL_4(2)`.
- `active_assignment_answered: no` unless the exact universal target is actually reached.

# Awaiting Lead decision

The next permitted strategy is the proposed full two-point array

\[
 S_{ij}(P,Q)=\#\{T:\ |(I+P)(I+T)|=i,\ |(I+Q)(I+T)|=j\}
\]

for colour-2 pairs `(P,Q)`, over all exact product-order colours in the rank-two class, with an exact `n=4` gate before any uniform extrapolation. A Lead decision/compute protocol is required before this materially stronger strategy starts.

- 2026-08-18T00:56:00Z — Lead decision received and read: authorized `RANK2-ALL-COLOUR-INTERSECTION-REFINEMENT` at cumulative minute 82 for at most 45 active minutes; route-minute-12 gate is a complete fibre-separating `PSL_4(2)` signature or an explicit full-array collision. Computation requires a frozen design and Lead lease. Source page 172 was also freshly rendered and visually compared: the canonical target and exclusions above agree with the typeset statement; the configured corpus contains only issue 20, so no issue-21 corpus flags exist locally. The canonical record has an independent passed source audit. Because `blind_run.enabled: true`, external staleness searching is deferred to Lead/human and no open-web search was performed. `source_transcription_checked: yes`; `active_scope_checked: yes`. Charged work resumes from official cumulative minute 82.

# Frozen `n=4` computation design (lease pending)

Object: all `4 x 4` binary matrices `T` with `T^2=0` and rank `2`; these are exactly the 210 vertices of the single Jordan class `2^2` in `GL_4(2)=PSL_4(2)`.

Algorithm, in a purpose-built deterministic Python script to be frozen before execution:

1. Enumerate integers `0..65535` as binary matrices; retain exactly the matrices satisfying square-zero and rank two. Assert vertex count `210` and uniqueness.
2. For every unordered vertex pair, calculate the exact order of `(I+P)(I+Q)` by repeated binary-matrix multiplication, with a hard mathematical bound checked by the order of `GL_4(2)`, `20160`; record the observed exact colour set and full symmetric colour matrix.
3. Enumerate every colour-2 pair and classify it independently as `same_fibre` iff `(im P,ker P)=(im Q,ker Q)`, using exact row/column-space bitmasks.
4. For each colour-2 pair `(P,Q)`, count all vertices `T` (including endpoints; their diagonal relation has product order `1`) into the complete ordered array `S_ij(P,Q)`. Record signatures as sorted triples `(i,j,count)` including zero cells implicitly through the common observed colour set. Also output the endpoint-excluded variant as a consistency check; the separation decision is invariant once the convention is fixed.
5. Compare the set of signatures attained by same-fibre pairs with that attained by cross-fibre pairs. If their intersection is nonempty, output the lexicographically first explicit pair of each type with the identical complete array and the four 16-bit matrices, plus flags and colour-2 checks. If disjoint, output every signature type with multiplicity and a complete separation certificate.
6. Internal assertions: symmetry `S_ij(P,Q)=S_ji(Q,P)`; each array totals 210 (or 208 endpoint-excluded); all pair-order entries divide 20160; every retained vertex is square-zero rank two; exactly 35 bare fibres each of size 6; every same-fibre pair has colour 2.

What a pass establishes, pending independent audit: exact fixed-`n=4` separation or collision for the first two-point coherent-configuration refinement. What it cannot establish: any statement for `n>4`, any fibre definability after higher coherent refinement, the rank-two family theorem, or the universal Kourovka target.

Expected resources: under 10 seconds CPU and under 100 MB RAM; request a 60-second timeout and a 5-minute lease. Although this is below the heavy-job threshold, the Lead decision requires a lease for every nontrivial computation, so execution is paused pending explicit approval.

- 2026-08-18T00:57:52Z — frozen exact script at `scratch/psl4_rank2_full_intersection.py`, 302 lines, SHA-256 `2dd9c1805d7bc52f6b998d280c67171bc5ee04f4ea0edc5452da502e6f35fecc`. Sent exact lease request to Lead. Work stop at cumulative active minute 87; lease wait is uncharged.

# Hand reduction for the `n=4` gate

While the lease is pending, one exact orbit count explains what the enumerator must see. Under the standard isomorphism `GL_4(2) = PSL_4(2) ~= A_8`, the 210 rank-two square-zero involutions correspond to the 210 double transpositions. For `a=(12)(34)`, the 17 distinct commuting double transpositions split by support pattern into:

- 2 on the same four-point support, namely `(13)(24)` and `(14)(23)`;
- 12 sharing exactly one transposition with `a`: choose one of the two transpositions of `a`, then one of the six transpositions on the four complementary points;
- 3 on the disjoint four-point complement.

Thus colour 2 has `210*17/2=1785` edges, in simultaneous-conjugacy orbit sizes `210`, `1260`, and `315` (the script does not assume this classification). Independently, in each six-decoration fibre the 15 unordered pairs split according to the relative element of `GL_2(2) ~= S_3`: 6 pairs with relative order 3 and 9 with relative order 2. Across 35 fibres these give `210` and `315` edges. Hence the same-fibre colour-2 pairs exhaust precisely the support-4 and support-8 counts, while the 1260 support-6 pairs are cross-fibre. The full array therefore only needs to compare three pair-orbit signatures in `n=4`; the previous collision is between the support-4 same-fibre orbit and support-6 cross-fibre orbit. This is a hand consistency prediction, not substituted for the frozen complete enumeration.

- 2026-08-18T01:01:00Z — hand orbit reduction completed; work stop at cumulative active minute 90. Lease wait remains uncharged. The route-minute-12 gate is due by cumulative minute 94.

## Route-minute-12 gate: outcome A at cumulative minute 92

- One leased invocation completed with exit code 0 in 0.749556311 seconds. Frozen script SHA-256: `2dd9c1805d7bc52f6b998d280c67171bc5ee04f4ea0edc5452da502e6f35fecc`. Certificate SHA-256: `27ad591f2366b45dd65d00fc7eb91e8d032d5262a01875c6683f11abff9c0e7f`.
- Exact model: all 210 rank-two square-zero `4 x 4` binary matrices, hence the single `2^2` involution class in `GL_4(2)=PSL_4(2)`. Observed edge colours are exactly `2,3,4,5,6`.
- Exact coverage: all `1785` colour-2 unordered pairs; `525` same-fibre and `1260` cross-fibre. Same-fibre pairs have exactly two complete-array signatures, of multiplicities `210` and `315`; cross-fibre pairs have exactly one, of multiplicity `1260`; the signature sets are disjoint.
- A much smaller separating cell emerges from the complete arrays:

  \[
  S_{2,3}(P,Q)=\#\{T:\ |(I+P)(I+T)|=2,\ |(I+Q)(I+T)|=3\}
  \]

  is `0` for every same-decoration-fibre colour-2 pair and `4` for every cross-fibre colour-2 pair. The transposed cell `S_{3,2}` has the same values, so the predicate is independent of endpoint order. Endpoint inclusion/exclusion does not affect these cells.
- The prior common-colour-2 collision is visible but resolved: one same-fibre signature and the cross signature both have `S_22=4`, yet `S_23` is respectively `0` and `4`.
- Internal checks passed: 210 vertices; 35 flags of six vertices; every same-fibre pair has colour 2; exact arrays sum to 210 (208 endpoint-excluded); colour-2 edge count and the hand orbit counts agree; endpoint-included and endpoint-excluded gate outcomes agree.
- Gate status: **(A), fixed `n=4` only**. This does not establish the formula for `n>4`, graph-theoretic fibre recovery throughout the infinite family, a rank-two family theorem, or the universal target.

Ledger correction: the preceding `2026-08-18T01:01:00Z` hand-reduction stop was entered as a rounded prospective wall time rather than observed from `kv_now`; it is not an exact timestamp and must not be used for wall-time auditing. The computation-release time `2026-08-18T01:00:33Z` and this checkpoint time `2026-08-18T01:01:25Z` were observed. Cumulative active-minute accounting is unchanged: gate delivered at minute 92, within the minute-94 requirement.

- 2026-08-18T01:01:25Z — route-minute-12 checkpoint filed at cumulative active minute 92. Continue only with a symbolic uniform-`n` test of `S_23`; do not reconstruct or assume the quotient unless uniform extension is established.

## Uniform-`n` hand test and strategy disposition

- Put `V=A direct-sum Z direct-sum B`, with `dim A=dim B=2`, and put `P` in the single block `B -> A`.  Direct multiplication shows every `T` commuting with `P` has block form `[[X,C,Y],[0,H,W],[0,0,X]]`.
- For any two square-zero maps `Q,T`, the corresponding involutions have product order 3 (when distinct) exactly when `Q+T+QTQ+TQT=0`.
- If `Q` is in the same decoration fibre as `P`, it occupies only the `B -> A` block with an invertible matrix `R`.  The preceding equation and the centralizer block form force `T=Q`.  Hence `S_23=0` for all same-fibre pairs for every `n>=4`.
- For every `n>=6`, choose a rank-two surjection `U:Z -> A` and let cross-fibre `Q` occupy only that block.  It has the same image as `P` but a different kernel and commutes with `P`.  The same order-3 equation again forces `T=Q`; hence this explicit cross-fibre pair also has `S_23=0`.
- Therefore the exact `n=4` separator does not extend uniformly.  The required condition for quotient reconstruction fails, so no quotient is assumed.  A stronger full-array analysis in `n>=6` would be a new experiment; it is not licensed by the present fixed-cell formula.

- 2026-08-18T01:07:21Z — uniform obstruction derived and outcome drafting begun at cumulative active minute 98.

## Outcome and handoff

- Wrote `psln2-rank2-all-colour-intersection-refinement.md` with all three exact `n=4` arrays, the finite certificate record, the uniform block obstruction, the full scope matrix, and explicit limitations.
- Outcome: `PARTIAL_RESULT`.  Fixed `n=4` fibres are separated by the complete arrays (indeed by `S_23`), but the extracted formula has explicit cross-fibre zeroes for every `n>=6`, so quotient reconstruction is forbidden.  Stronger full-array separation for larger `n` remains open.
- `witness_equals_target: false`; `active_assignment_answered: no`.
- 2026-08-18T01:09:41Z — work stop and `awaiting_lead` at official cumulative active minute 104.  This route used 22 of its authorized 45 active minutes (82 through 104); no further computation or replacement refinement was started.

- 2026-08-18T01:09:42Z — brief work restart to audit certification language and the final handoff files.
- 2026-08-18T01:11:30Z — final work stop and `awaiting_lead` at official cumulative active minute 106.  Total route charge: 24 of the authorized 45 active minutes (82 through 106).  The minute-104 stop above was superseded only by this two-minute wording/file audit; no mathematical strategy or computation resumed.
