---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/alternating-groups
  - project/kourovka
  - status/draft
---

# Problem 21.52 proof lane, cycle 14: even-matching centralizer moments

## 2026-08-18T06:36:11Z -- work start

Active-time ledger: start cumulative minute 216; this block may use at most 45
new active minutes.  Direction: proof.  Strategy:
`EVEN-MATCHING-CENTRALIZER-MOMENTS`.

## Source and scope gate

The source PDF resolved through `paths.env`.  Page 172 was inspected both via
`pdftotext -layout` and as a rendered PNG.  The displayed source asks: for a
finite nonabelian simple group `L`, a single conjugacy class `D` of involutions,
and the complete graph on `D` whose edge equivalence is exactly equality of
`|ab|`, is every colour-preserving permutation of `D` induced by an
automorphism of `L`?  The canonical typed conclusion is restriction from the
setwise stabilizer of `D` in `Aut(L)`.

`source_transcription_checked: yes`.  `active_scope_checked: yes`.
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`
as required by the scope's blind-run flag.  This fresh lane does not inspect or
use preceding solution-bearing run artifacts.

### Clause matrix

| source clause | active here? | use in this lane |
|---|---:|---|
| `L` finite nonabelian simple; `D` one involution class | yes | specialize to the family `L=A_n`, `D=D_{n,k}`; this can only yield an infinite-family partial |
| complete graph on `D` | yes | every unordered distinct pair of matchings is an edge |
| edge equivalence iff exact product orders agree | yes | only exact order colours and statistics definable from them may be used |
| every colour permutation induced by `Aut(L)` | yes | target family conclusion; universal all-simple-groups row remains open |
| Problem 21.53 | no | excluded |

### Seven-constraint checklist

1. `21.52-forall-L-D`: the notebook assertion is universal; an alternating-family
   theorem is explicitly only partial.
2. `21.52-L-finite-nonabelian-simple`: `A_n` is admissible only for `n>=5`.
3. `21.52-D-single-involution-class`: for even `k>=2` and `2k<=n`, cycle type
   `2^k1^(n-2k)` lies in `A_n`; its `S_n` class does not split in `A_n` because
   the cycle lengths are not distinct odd lengths, hence it is one `A_n` class.
4. `21.52-Gamma-complete-on-D`: retained exactly.
5. `21.52-edge-colour-exact-product-order`: retained exactly; no product-conjugacy
   refinement is allowed.
6. `21.52-tau-preserves-all-edge-colours`: all proposed statistics must be
   first-order/combinatorial counts in the exact-coloured graph.
7. `21.52-tau-induced-by-AutL`: after reconstructing the natural `n`-point
   action, point permutations induce conjugation on `D`; exceptional outer
   automorphisms and kernel/faithfulness still require an audit.

Explicit exclusions: no union of involution classes; no uncoloured-complete-graph
argument; no product-conjugacy colouring; no bounded sample presented as a
universal statement; no use of Problem 21.53.

## Strategy portfolio

1. **Theoretical / coefficient species (primary).** Derive the exact union-of-two-
   matchings product-order rule and the generating polynomial for type-`k`
   involutions centralizing a pair.  Seek several fixed-degree, colour-definable
   iterated common-neighbour moments whose factor contributions give a triangular
   system for the pair's internal component multiplicities.
2. **Structured reconstruction.** If the moments define pairs sharing a common
   `(k-1)`-matching core, reconstruct the natural points from the resulting
   matching-overlap graph and audit the `A_n` extension step.
3. **Catalogue/probe (discovery only).** A small bespoke enumerator may test
   formulas and locate collisions at small `(n,k)`; it cannot prove any stable
   range.  No heavy computation is planned.
4. **Certificate plan.** A useful partial will include hand-derived factor
   polynomials, the exact inversion matrix/determinant and parameter range, then
   a self-contained reconstruction lemma.  A failed inversion will be reported
   with an exact symbolic collision, not merely sampled equality.

Kill gate: if no fixed-degree invertible system can be justified, stop at the
strongest exact factorization/reduction or symbolic collision and recommend the
next representation; do not smuggle fixed samples into a uniform claim.

## 2026-08-18T06:53:33Z -- triangular classifier obtained

Active-time ledger: cumulative minute 233 (17 new active minutes in this block).

The exact commuting-pair orbit parameters are `(a,b,c)`: `a` common
transpositions, `b` one-sided transpositions of each generator, and `c`
alternating squares, with `a+b+2c=k` and common fixed-point count
`f=n-2k-2b`.  Direct orbit-species enumeration gives

`|D cap C(<x,y>)|=[t^k]F_a F_b^2 G_c M_f`,

with every factor derived in `findings.md`.

The successful fixed-degree statistic is not a radix evaluation.  For the
closed common commuting neighbourhood `K(x,y)`, take the vector
`T=(U,C)`, where `C=|K|` and `U` counts universal vertices of the induced
commuting graph on `K`.  When `n>=8k`, the common fixed set has at least `4k`
points; padding the standard wreath-product generators proves that the
universal vertices are exactly the type-`k` elements in the centre of the full
pair centralizer.  Its weight coefficient first forces `c=0` (with the explicit
`k=2` exception).  The recurrences

`F_b=(1+t)F_(b-1)+2(b-1)t^2F_(b-2)` and

`M_(f+2),j-M_f,j=(2f-2j+3)M_f,j-1`

then give a strict coefficientwise triangular chain at the *same* `n`:
`[t^k]P_1>...>[t^k]P_k`.  Consequently an intrinsic extremal condition on
`T` defines exactly the colour-2 pairs with `a=k-1,b=1,c=0`.  For `k=2`, the
target is the smaller of the two `U=3` types, with exact difference
`(2f-4)M_(f,1)>0`.

Colour-3 core pairs are then exactly the colour-3 pairs having a common
neighbour in that recovered colour-2 relation.  Their union is the graph on
`k`-matchings with adjacency `|X cap Y|=k-1`.  Largest-clique recovery followed
by the cross-star threshold `E>4` descends through every matching layer to
individual edges of `K_n`; 2-matching incidence recovers edge disjointness and
then the natural points from the line graph.  Thus a colour permutation is
conjugation by a natural point permutation.

This gives a candidate infinite-family `PARTIAL_RESULT` for every even `k>=2`
and `n>=8k`, documented in `findings.md`.  It leaves every other simple group,
other alternating involution classes/ranges, and the universal conclusion open.
No preceding unreviewed theorem was read or used.  The script in `scratch/` only
checked integer versions of the hand-derived formulas; no heavy computation or
lease was used.

### Self-check

- Exact scope/revision: `21.52/involution-class-product-order-colouring`, r1.
- All seven canonical rows are explicit in `findings.md`; six pass in the stated
  family and the universal conclusion row is deliberately marked partial.
- Representation stayed productive: pair-centralizer orbit species yielded a
  two-coordinate triangular classifier and a linear range.
- Fragile gates for independent review: universal vertices equal the centre;
  the `M_(f+2)` coefficient inequality; maximal-clique dichotomy; cross-star
  bound `E<=4` off the target overlap.
- Outcome: `PARTIAL_RESULT`, not a universal claim and not a solution of 21.52.

## 2026-08-18T06:53:33Z -- work stop

Charged active time in cycle 14: 17 minutes.  Cumulative problem ledger:
233 minutes.  Exact continuation recommendation: fresh Validator reconstruct
the four fragile gates above.  If they survive, retain `n>=8k` as a reviewed
alternating-family theorem; a later refinement could optimize the constant by
replacing the deliberately generous `f>=4k` coefficient bound.
