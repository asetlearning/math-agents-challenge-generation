---
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
direction: counterexample
run: 2026-08-17-r3-psl211-two-colour-separation
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/coloured-graphs
  - project/kourovka
  - status/draft
---

# PSL(2,11) two-colour separation log

## 2026-08-17T20:30:35Z — active work start

Cumulative active time starts at minute 34. This bounded lane has at most 45 new
active minutes and tests exactly `L = PSL(2,11)` with one complete involution
class. No catalogue expansion is permitted.

## Staleness and source gate

- Rendered Notebook No. 21 PDF p. 172 was inspected visually, including inherited
  Problem 21.52. Source transcription checked: yes.
- Active source statement: `L` is the finite nonabelian simple group inherited
  from 21.52; `D` is one conjugacy class of involutions; the complete graph on
  `D` is coloured by the exact product order `|ab|`. For every positive integer
  `t`, `Aut_t(Gamma)` preserves all `t`-edges, vacuously when none occur.
  `Aut(Gamma)` is the intersection over all colours. Problem 21.53 asks whether
  `Aut(Gamma)=Aut_2(Gamma) intersect Aut_p(Gamma)`, where `2,p` are the two
  smallest distinct prime divisors of the group order.
- Scope revision 2 matches those clauses and retains the inherited nonabelian
  simple restriction. Active scope checked: yes.
- Discovery-blind gate applies (`blind_run.enabled: true`, `open_web: false`):
  `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
  The current source prints the problem unstarred; no solution-bearing search was
  performed in this run.
- The independently replicated PSL(2,8) result is treated only as the bounded
  partial stated in the incoming Validator verdict. No universal inference is
  imported.

## Constraint checklist for the fixed probe

| constraint_id | fixed-probe check |
|---|---|
| 21.53-forall-L-D | A strict failure for this admissible pair would refute the universal assertion; equality would remain bounded only. |
| 21.53-L-finite-nonabelian-simple | Must establish this for `PSL(2,11)`. |
| 21.53-D-single-involution-class | Must enumerate all involution classes and select exactly one whole class. |
| 21.53-Gamma-product-order-colouring | Must save every unordered-pair product order. |
| 21.53-Aut-t-definition | Apply for every positive `t`, including vacuous labels. |
| 21.53-two-minimal-primes | Must factor the exact group order and derive `p`. |
| 21.53-full-colour-group-definition | Full group preserves every occurring colour. |
| 21.53-two-colours-determine-all | A counterexample requires an explicit permutation preserving all 2- and p-edges and changing a displayed other-colour edge. |

## Strategy portfolio

1. **Assigned finite probe (highest information per minute).** Construct the
   quotient `SL(2,11)/{+I,-I}` directly, enumerate its complete involution class,
   and freeze the full product-order matrix. At most three occurring colours ends
   by the exact complement/vacuity argument.
2. **Exact automorphism comparison (conditional).** If at least four colours
   occur, freeze all inputs and request a Lead lease for one bounded GAP/GRAPE or
   nauty-compatible computation of `Aut_2 intersect Aut_3` versus the full colour
   group. No such computation starts without the lease.
3. **Structural/theoretical route.** Inspect whether the 2- and 3-relations recover
   the remaining relation classes through common-neighbour/intersection counts.
   This is secondary to the assigned exact separator probe and is not a licence to
   change targets.
4. **Certificate plan.** Save canonical matrix representatives, all 1,485
   unordered-pair colours, hashes, deterministic scripts, and exact software
   versions. Any strict inequality must additionally save one explicit vertex
   permutation, exhaustively check every 2- and 3-edge, and display one changed
   other-colour edge. Equality is reported only for this pair.

## 2026-08-17T20:35:55Z — complete matrix and four-colour gate

Active interval `20:30:35Z--20:35:55Z`: 6 minutes charged; cumulative active
minute 40. Command actually run:

```bash
timeout 30s python3 Agents/Kourovka/problems/21.53/runs/2026-08-17-r3-psl211-two-colour-separation/scratch/build_psl211_matrix.py
```

Observed terminal tag: `PSL211_MATRIX_BUILD_OK`. Python 3.12.3 completed in 1.6
wall-clock seconds. Exact outputs and hashes are frozen in `scratch/` and
`scratch/frozen-manifest.md` (manifest SHA-256
`f4e5eb04dc4fe560d25aa34c5258b3169fc21039cd4d1aac8096aaa8f844b87b`).

### Group and class gates

The model is `SL(2,11)/{+I,-I}`. Direct enumeration gives
`|SL(2,11)|=11(11^2-1)=1320` and 660 central pairs. This is `PSL(2,11)` by
definition. The two displayed matrices

`u=(1,1,0,1)` and `s=(0,1,10,0)`

generate all 660 quotient elements and do not commute. For a direct finite
simplicity check independent of merely naming the group, the script enumerated
all eight conjugacy classes. Their `(element order, class size)` pairs are

`(1,1), (2,55), (3,110), (5,132), (5,132), (6,110), (11,60), (11,60)`.

For every one of the seven nonidentity classes, the subgroup generated by the
whole class has order 660. Any nontrivial normal subgroup contains one such class,
so no proper nontrivial normal subgroup exists. Thus the exact finite group is
nonabelian and simple.

There are exactly 55 elements of quotient order 2. They form the single class of
size 55 above; its directly enumerated centralizer has order 12, consistent with
`660/12=55`. Thus `D` is exactly one complete involution class, not a union, and
there is no second involution class to test in this fixed group.

Finally, `660=2^2*3*5*11`, so the second-smallest distinct prime is exactly
`p=3`.

### Complete product-order colouring

The files `vertices.tsv`, `unordered_edges.tsv`, and
`product_order_matrix.csv` give, respectively, all 55 canonical involution
representatives, every one of the 1,485 unordered pairs with `|ab|`, and the
complete symmetric matrix (diagonal `|aa|=1`). Exactly four off-diagonal colours
occur:

| product order | vertex valency | unordered edges |
|---:|---:|---:|
| 2 | 6 | 165 |
| 3 | 12 | 330 |
| 5 | 24 | 660 |
| 6 | 12 | 330 |

The valencies sum to 54 and the edge counts sum to 1,485. For every positive
integer `t` outside `{2,3,5,6}`, there is no `t`-edge and therefore
`Aut_t(Gamma)=S_55` vacuously. In particular, neither required colour is
vacuous here.

Because four colours occur, the direct complement/vacuity tautology does not
decide this pair. Inputs are frozen. No graph-automorphism command has been run;
the next action requires the requested Lead lease.

## 2026-08-17T20:41:30Z — one leased automorphism comparison; fixed equality

Lead granted compute slot 2 through
`2026-08-17T21:37:09Z` for exactly one invocation. Before execution, SHA-256 was
recomputed for every frozen artifact; all eight values agreed with the frozen
manifest, including approved checker hash
`34a946f10ef13758c1309dd2ff63004fdcedc921c586ba2c7caf8ce38ff5ab4b`.

The exact command was run once and no other automorphism computation was run:

```bash
timeout 120s gap -q Agents/Kourovka/problems/21.53/runs/2026-08-17-r3-psl211-two-colour-separation/scratch/compare_aut_groups.g
```

Exact observed standard output:

```text
PSL211_AUT_COMPARISON_OK
GAP_VERSION=4.12.1
GRAPE_VERSION=4.9.0
VERTICES=55
COLOURS=[ 2, 3, 5, 6 ]
AUT2_ORDER=1320
AUT3_ORDER=1320
AUT5_ORDER=1320
AUT6_ORDER=1320
TWO_COLOUR_ORDER=1320
FULL_COLOUR_ORDER=1320
FULL_SUBGROUP_TWO=true
EQUALITY=true
```

Exit code was exactly 0; tool-observed wall time was 2.206156983 seconds. The
process used slot 2, one GAP invocation, and GAP's single CPU process under the
approved 512 MiB envelope; no timeout fired. Peak RSS and exact CPU seconds were
not independently instrumented because the authorized command had to be invoked
verbatim, so no unobserved numerical resource figure is asserted.

The script constructs each of the four simple relation graphs from the frozen
matrix and computes `Aut_2`, `Aut_3`, `Aut_5`, and `Aut_6`. It then sets
`two=Aut_2 intersect Aut_3` and
`full=two intersect Aut_5 intersect Aut_6`, checks `full <= two`, and exhaustively
checks every generator of `two` on all colour-2 and colour-3 edges and every
generator of `full` on all four colours. Since containment holds and both finite
groups have order 1320, they are equal for this exact pair. The strict branch did
not fire, so no separator exists in the computed group difference and the
explicit-separator certificate is inapplicable.

Slot 2 was released by REPORT at `2026-08-17T20:41:30Z`, immediately after the
successful invocation.

Active interval for hash verification, the one run, inspection, release, and
recording: 2 minutes charged; cumulative active minute 42. Of the 45 new active
minutes authorized from cumulative minute 34, 37 are returned unused. Outcome:
`PARTIAL_RESULT` for exactly `(PSL(2,11),D)`. The universal revision-2 scope remains
open, and no further target, class, or catalogue entry is started here.

