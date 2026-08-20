---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/alternating-groups
  - topic/coloured-graphs
  - project/kourovka
  - status/draft
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
cycle: 15
strategy: SIX-MATCHING-BOUNDARY-EXACT
---

# Cycle 15 log — six-matching boundary exact

## 2026-08-18T07:00:00Z — work start

Cumulative active minute at start: 233. This cycle may use at most 45 new active
minutes. The lane is restricted to the single class of involutions of cycle type
`2^6 1^(n-12)` in `A_n`, for every `n>=12`. Previous unreviewed even-matching
claims are not premises.

## Source and staleness gate

Rendered source page 172 was inspected directly from the PDF resolved by
`_meta/agents/Kourovka/paths.env`; `pdftotext` was used only for navigation.
Corrected transcription: let `L` be finite nonabelian simple and `D` a single
conjugacy class of involutions. The complete graph on `D` has edge equivalence
`(a,b)~(c,d)` iff `|ab|=|cd|`. A colour automorphism is a permutation `tau` of
`D` preserving that equivalence on every edge. The question asks whether each
such permutation is induced on `D` by an automorphism of `L` stabilizing `D`.

`source_transcription_checked: yes`. The rendered formulas, quantifiers, and the
separate statement of Problem 21.53 agree with all seven canonical constraints.
The active family specialization has `L=A_n`, `n>=12` (hence finite nonabelian
simple), and `D` the single `A_n`-class `2^6 1^(n-12)`; this `S_n` class does not
split in `A_n` because its cycle lengths are not distinct odd lengths.

Clause matrix:

| source clause | active specialization | in this lane |
|---|---|---|
| finite nonabelian simple `L`; one involution class `D` | `A_n`, `n>=12`; type `2^6 1^(n-12)` | yes |
| complete graph on `D` | vertices are six-edge matchings of `[n]` | yes |
| exact edge colour iff equal product order | preserve the integer `|xy|`, not a product conjugacy class | yes |
| every colour permutation induced by `Aut(L)` | prove the full colour group is the natural `S_n` image | yes |
| Problem 21.53/two selected colours | different source problem | excluded |

Admissibility checklist: `21.52-forall-L-D` is used only for the stated family
partial; `21.52-L-finite-nonabelian-simple`, `21.52-D-single-involution-class`,
`21.52-Gamma-complete-on-D`, `21.52-edge-colour-exact-product-order`, and
`21.52-tau-preserves-all-edge-colours` retain their literal meanings; the target
row `21.52-tau-induced-by-AutL` becomes induction by the natural `S_n` action.
No constraint mismatch was found. `active_scope_checked: yes`.

The scope record marks this as a discovery-blind run (`open_web:false`,
`solution_bearing_history_allowed:false`). Accordingly no web or historical
solution-bearing notes were inspected:
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
The source is the current 21st issue (2026); no issue-21 JSONL corpus row exists,
so the legacy corpus flags are unavailable rather than silently inferred.

## Strategy portfolio

1. **Exact centralizer generating functions (first).** Classify every commuting
   pair by `a+b+2c=6`; count six-transposition common colour-2 neighbours from the
   centralizer of the generated `C_2` or `C_2^2` action. This gives intrinsic
   polynomial signatures and an exact collision/failure list.
2. **Fixed-degree certificate probe.** At the smallest feasible degrees, enumerate
   only pair types and symbolic neighbour counts (not the full enormous graph) to
   test whether five-edge-core adjacency can be isolated. A sub-60-second bespoke
   script is sufficient; no heavy compute is planned.
3. **Theoretical reconstruction.** If core adjacency is colour-definable, identify
   maximal core cliques/layers and reconstruct the underlying edge set and then
   the `n` points. Audit `n=12`, where distinct perfect matchings cannot share five
   edges, separately through four-edge flips.
4. **Certificate plan.** Preserve explicit generating functions, expanded
   polynomials/collision tables, and a hand reconstruction statement. A family
   claim would require exact treatment of every small degree and action
   containment, not group-order equality.

Kill criterion for the first strategy: if common-colour-2 counts collide on the
five-core type at some degree, record that as failure of this statistic and move
only to a named iterated-neighbour statistic; do not call it a graph
counterexample.

## 2026-08-18T10:08:17Z — hard stop and 45-minute checkpoint

Cumulative active minute: 278 (the full authorized `233--278` increment is
charged). The safety clock was already past the roster stop when next polled, so
no further research is authorized. This late poll is a protocol incident; the
mathematical outputs below were all bounded and no heavy job was run. The first
symbolic script invocation failed immediately because `sympy` was absent; it was
replaced by a degree-12 exact `fractions.Fraction` implementation, not by installing
or recreating a general CAS. The first `n=14` brute run exposed and corrected two
bad expected constants (`945945`, not `135135`, vertices; target centralizer count
`287`, not `92`) before the passing rerun. No failed constant is used below.

New facts:

- Every commuting pair has a unique orbit type `(a,b,c)` with
  `a+b+2c=6`. Exact centralizer generating functions give its entire number of
  common colour-2 neighbours. The five-common/disjoint-extra type `(5,1,0)` is
  isolated for every `n>=14`; a complete independent `n=14` enumeration of all
  `945945` vertices gives common-neighbour values `157,63,61,285,67,37` for the
  six feasible types, with `285` unique to `(5,1,0)`.
- Every order-3 pair has a unique `S_3`-orbit type `(a,p,q)` with
  `a+p+3q=6`. Its common-colour-2 count isolates the five-common/intersecting-extra
  type `(5,1,0)` for every `n>=15`. At `n=13,14`, where that statistic collides,
  complete exact pair arrays isolate it by `(N_22,N_33)=(0,241)` and `(0,1312)`.
- Consequently the ordinary graph `J_6(n)` joining six-matchings with five common
  edges is definable from the exact product-order colouring for every `n>=13`.
  At `n=12` it is empty, but the four-common flip relation is definable: the three
  commuting types have centralizer counts `75,39,63`, so the flip type `(4,0,1)`
  is unique.
- A self-contained descent through matching layers shows
  `Aut(J_6(n))=S_n` for every `n>=15`: recover core stars, recover the disjoint
  exchange graph by star intersections, use the `>4` common-neighbour test to add
  intersecting exchanges, and iterate to two-matchings; their core stars recover
  the disjointness graph on edges and hence the points.

What is ruled out: failure of the first moment on the target commuting type; it
has no feasible integer collision. The order-3 first moment does collide exactly
at `n=13,14`, but the full exact arrays resolve those two degrees. These are
statistic collisions, not source counterexamples.

Bottleneck: action rigidity after `J_6` recovery at `n=13,14`, and after flip
recovery at `n=12`. The stable descent uses
`binom(n-2s-1,2)>4`; its first step fails only in these nearby degrees. No
counterexample was found, but equality of group orders was neither computed nor
assumed.

Two qualitatively different continuations:

1. **Small-degree residue reconstruction (recommended):** prove directly that the
   panel geometry of `J_6(13)` (three-point five-core lines), the star/top geometry
   of `J_6(14)` (clique sizes `6` and `7`), and the flip-triangle geometry at
   `n=12` reconstruct the edge-disjointness graph `KG(n,2)`.
2. **Frozen sparse-graph certificate:** encode only these definable sparse
   relations, compute their full automorphism groups with a leased canonical graph
   tool, and require explicit containment/action identification. This is a finite
   certificate route, not extrapolation.

Recommended next experiment (one hour): carry out the hand residue descent for
`n=13,14`, with the kill criterion that any ambiguous residue class surviving two
iterated incidence counts triggers a frozen leased automorphism computation. Audit
`n=12` separately; do not infer it from `n=13`.

Current candidate passes the object, class, complete-graph, exact-colour, and
colour-preservation constraints only for the stated `A_n` family. The universal
`forall L,D` row and full target-conclusion row remain open, and even the family
conclusion remains open at `n=12,13,14`. There is no source-scope claim.
