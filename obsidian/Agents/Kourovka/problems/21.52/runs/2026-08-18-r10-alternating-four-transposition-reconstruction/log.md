---
title: "Problem 21.52 cycle 10 — four-transposition reconstruction log"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/alternating-groups
  - project/kourovka
  - status/draft
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: proof
run: 2026-08-18-r10-alternating-four-transposition-reconstruction
---

# Active-time ledger

- 2026-08-18T05:04:11Z — research start at cumulative active minute 144; allocation ends at minute 180.

## 2026-08-18T05:04:11Z — source, scope, and staleness gate

The configured source PDF is readable. I rendered PDF page 172 and visually checked
the complete statement of 21.52 against the canonical revision-1 scope. The source
asks whether, for a finite nonabelian simple group `L` and one conjugacy class `D`
of involutions, every permutation of `D` preserving the exact equality classes of
all product orders `|ab|` is induced by `Aut(L)`. The seven canonical rows agree
with the rendered typography. Problem 21.53 is a separate clause and is excluded.

`source_transcription_checked: yes`
`active_scope_checked: yes`

The No. 21 source prints 21.52 unstarred and gives no editor or later comment in
the statement. There is no No. 21 JSONL corpus record in this vault. The canonical
scope has `blind_run.enabled: true` and `blind_run.open_web: false`, so the external
literature check is deferred: `external_staleness_check:
deferred_to_lead_or_human_for_discovery_blind_run`.

### Clause matrix

| source clause | active here? | treatment |
|---|---:|---|
| finite nonabelian simple `L`, one involution class `D` | yes | specialize only to `L=A_n`, `D=2^4 1^(n-8)`, explicitly a partial family |
| complete graph on `D` | yes | every unordered pair of distinct four-matchings is retained |
| edge equivalence iff exact product orders agree | yes | no product-conjugacy-class refinement is used |
| every colour permutation comes from `Aut(L)` | yes | target only for the stated alternating-family range |
| Problem 21.53 two-selected-colour question | no | excluded |

### Seven-row admissibility checklist

| constraint_id | use in this lane |
|---|---|
| `21.52-forall-L-D` | this lane is a stated subfamily partial, never the universal assertion |
| `21.52-L-finite-nonabelian-simple` | prove `A_n` finite nonabelian simple for every degree actually claimed |
| `21.52-D-single-involution-class` | prove the `2^4 1^(n-8)` `S_n` class does not split in `A_n` |
| `21.52-Gamma-complete-on-D` | work with all pairs of distinct four-edge matchings |
| `21.52-edge-colour-exact-product-order` | derive the order as an lcm over every alternating component |
| `21.52-tau-preserves-all-edge-colours` | use only relations intrinsically definable from those exact colours |
| `21.52-tau-induced-by-AutL` | if reconstruction succeeds, identify the faithful restriction of the setwise stabilizer in `Aut(A_n)` |

## Strategy portfolio

1. **Theoretical / alternating-component classification (first):** classify every
   red-blue path, doubled edge, and even cycle in the union of two four-matchings;
   derive a closed lcm formula and enumerate all feasible component signatures.
2. **Structured reconstruction:** seek a colour-definable equivalence or incidence
   relation recovering supports, underlying transposition edges, or point stars;
   then invoke the automorphism theorem for the recovered subset/incidence geometry.
3. **Bounded catalogue probe:** for `n=8,9` only, compute exact two-point colour
   intersection signatures to expose order collisions and test candidate intrinsic
   predicates. A negative test rules out only that predicate, not reconstruction.
4. **Certificate plan:** Validator can check the component lemma by tracing one
   alternating component and the finite signature list by its two edge-count sums.
   Any uniform reconstruction must be a hand characterization; small-degree claims
   need a complete exact colour-group comparison, not counts alone.

## 2026-08-18T05:08:00Z — component classification

Writing red and blue for the two matchings gives only doubled common edges,
alternating even cycles, and alternating paths.  On a path with `l` edges the
product is one cycle of length `l+1`; on an alternating cycle with `2k` edges it
is two `k`-cycles.  The resulting red/blue edge-count equations are sufficient
as well as necessary.  The 38-line deterministic script
`component_signatures.py` enumerated 68 ordered signatures (54 modulo global
red/blue interchange) and exact order set
`[2,3,4,5,6,7,8,9,10,12,14,15,20,21,30]`.

Command:

`python3 Agents/Kourovka/problems/21.52/runs/2026-08-18-r10-alternating-four-transposition-reconstruction/component_signatures.py`

The full hand formula and feasibility equations are in `findings.md`; the script
is a check, not the proof.

## 2026-08-18T05:10:00Z — first two-point refinement probe

For every ordered pair signature, I computed the intrinsic array
`N_{r,s}(a,b)=#{c:|ac|=r,|bc|=s}` by enumerating all four-matchings `c`.  An initial
run showed impossible entries with one order equal to 1.  Inspection found that
the closing edge of a realized alternating cycle was stored as `(high,low)`, so
tuple comparison failed to exclude `c=b`.  I normalized both endpoints of every
edge in `realize`; all pre-correction array counts are invalid and are not used.

Corrected commands and exact summaries:

```
for n in 8 9 10 11 12; do
  /usr/bin/time -f 'elapsed=%e rss=%M' python3 \
    Agents/Kourovka/problems/21.52/runs/2026-08-18-r10-alternating-four-transposition-reconstruction/pair_array_probe.py "$n"
done
```

Output summaries:

```
n 8  vertices 105    types 4  array_classes 4  collisions 0
n 9  vertices 945    types 11 array_classes 11 collisions 0
n 10 vertices 4725   types 30 array_classes 30 collisions 0
n 11 vertices 17325  types 43 array_classes 43 collisions 0
n 12 vertices 51975  types 57 array_classes 57 collisions 0
```

Corrected `n=13` command:

`/usr/bin/time -f 'elapsed=%e rss=%M' python3 Agents/Kourovka/problems/21.52/runs/2026-08-18-r10-alternating-four-transposition-reconstruction/pair_array_probe.py 13`

Output:

```
n 13 vertices 135135 types 62 colours [2,3,4,5,6,7,8,9,10,12,14,15,20,21,30]
array_classes 62 collisions 0
elapsed=43.38 rss=35072
```

At `n=8`, `N_22` alone takes the four distinct values `5,11,3,7` on
`C4,C2C2,EC3,EEC2`.  At `n=9`, the three-coordinate table recorded in
`findings.md` separates all eleven signatures.  Thus the computation is not just
a raw automorphism count: it identifies the exact colour-intrinsic relation that
is needed for reconstruction, namely whether the pair has a common transposition.

## 2026-08-18T05:18:00Z — uniform reconstruction reduction

If common-transposition incidence is intrinsic, the graph whose adjacency means
sharing an edge recovers the transposition stars `F_e` as its maximum cliques by
the matching-EKR equality case.  Empty intersection of two recovered stars is
then exactly adjacency of their underlying edges in `K_n`; the line graph of
`K_n` recovers the `n` points and forces the original permutation to be the
natural `S_n` action.  This bypasses the complement symmetry of the support-only
Johnson scheme at `n=16`.

The remaining uniform check is finite: for a signature on `V<=16` union points,
every array coordinate is
`sum_q A_q binom(n-V,q)`, degree at most eight.  At most 4,116,315 labelled local
cases determine all coefficients for one signature.  A future frozen symbolic
checker can certify cross-`e=0/e>0` noncollision for all integer `n>=14`.

## 2026-08-18T05:22:00Z — rejected shortcut

Because colour 7 uniquely means signature `E P6`, I tested whether colour-7
triangles keep one common transposition.  They do not.  With a fixed vertex,
mixed-label colour-7 triangles already number 1,536 at `n=9` and 3,456 at `n=10`;
explicit examples are printed by `r7_triangle_probe.py`.  Thus simple triangle
components do not recover edge-stars.  This kills only that shortcut and leaves
the exact polynomial-refinement route live.

## 2026-08-18T05:24:00Z — stop and outcome

Stop at cumulative active minute 164 (20 new active minutes; allocation was
144--180).  Outcome: `PARTIAL_RESULT`.  The complete component/order theorem,
the reconstruction lemma, exact first-implementation coverage `8<=n<=13`, and
the degree-at-most-eight uniform reduction are in `findings.md`.  The active
universal scope is not answered.  Recommended continuation: freeze a symbolic
coefficient generator and exact polynomial root/sign certificate for `n>=14`,
then route both the matching-EKR equality case and the coefficient certificate
to independent Validator reconstruction.
