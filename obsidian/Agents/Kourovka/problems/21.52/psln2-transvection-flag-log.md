---
title: "21.52 proof lane log — PSL_n(2) transvection flags"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
strategy_id: LIN2-TRANSVECTION-FLAG
direction: proof
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/projective-geometry
  - project/kourovka
  - status/draft
---

# Active-time ledger

- 2026-08-17T16:50:42Z — work started, cumulative active time `0 min`.

## 2026-08-17T16:53:02Z — source and scope gate (cumulative active time: 2 min)

- Read the source statement on rendered PDF page 172 and compared it visually with
  the canonical scope transcription.
- `source_transcription_checked: yes`.
- `active_scope_checked: yes`.
- Corrected transcription: Let `L` be a finite nonabelian simple group and `D` a
  conjugacy class of involutions. On the complete graph with vertex set `D`, set
  `(a,b)~(c,d)` exactly when `|ab|=|cd|`. A coloured-graph automorphism is a
  permutation `tau in S_D` with `(a,b)~(a^tau,b^tau)` for every edge. The question
  is whether this permutation group is induced by `Aut(L)` (typed in the canonical
  scope via restriction from the setwise stabilizer of `D`).
- The active universal statement quantifies over every finite nonabelian simple
  pair `(L,D)`. This lane is deliberately restricted to
  `L=PSL_n(2)=GL_n(2)`, `n>=3`, and the single rank-one transvection class `D`.
  Therefore even a complete family argument can only be a `PARTIAL_RESULT`; the
  universal constraint `21.52-forall-L-D` remains uncovered.
- Discovery-blind restriction honored: no open-web or historical solution search.
  `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.

## Strategy portfolio

1. `LIN2-TRANSVECTION-FLAG` (selected): hand-derive the product-order table,
   classify maximal colour-2 cliques, and reconstruct point--hyperplane incidence.
2. Catalogue/small-case mode: excluded for this increment by Lead's no-computation
   instruction; in any case it could not prove the infinite family.
3. Structured mode: view transvections as square-zero rank-one tensors and turn
   order 2 into mutual flag incidence.
4. Theoretical mode: recover the incidence graph from intrinsic minimum maximal
   colour-2 cliques, then apply the fundamental theorem only with its dimension
   and field hypotheses explicit.
5. Certificate plan: a line-by-line hand proof with all rank-one products and both
   type-preserving and type-swapping realizations written explicitly for Validator.

## 2026-08-17T16:56:48Z — gates G0 and G1 (cumulative active time: 6 min)

- `G0` passes for the proposed family: over `F_2`, incident flags parametrize
  injectively one conjugacy class of involutions, `GL_n(2)=PSL_n(2)`, and the
  classical simplicity exception list excludes no `n>=3`.
- `G1` passes by hand. For distinct flags and cross-scalars
  `(a,b)=(f(v),g(u))`, the exact orders are `2,3,4` for `(0,0)`, `(1,1)`, and
  the two asymmetric cases, respectively. In an asymmetric case, writing the
  product as `I+N` gives `N^2` equal to a nonzero rank-one tensor and `N^3=0`,
  so the order is exactly four.
- No computation was used. The full derivation is being written in
  `Agents/Kourovka/problems/21.52/psln2-transvection-flag-reconstruction.md`.

## Ledger correction

The 16:50:42Z entry marked the start of the source check, not the start of charged
work. Reading the mandatory protocol and the assigned decision began at the Lead
activation time `2026-08-17T16:47:30Z`; cumulative times below use that start.

## 2026-08-17T16:58:01Z — gate G2 (cumulative active time: 10 min)

- Every colour-2 clique `C` lies in `K_U`, where `U` is the span of its point
  coordinates; maximality gives equality. Conversely, a vertex adjacent to every
  member of `K_U` must itself lie in `K_U`, using the intersection of all
  hyperplanes through `U`.
- The size formula is `(2^r-1)(2^(n-r)-1)`. For every interior dimension the
  excess over the endpoint size is
  `2(2^(r-1)-1)(2^(n-r-1)-1)>0`. For `n=3` there are no interior dimensions.
- Thus `G2` passes; no offending clique or size tie exists.

## 2026-08-17T17:03:32Z — first red-team pass (cumulative active time: 16 min)

- Equal vertices occur only in the `(0,0)` scalar case and would give product
  order `1`; the edge table explicitly assumes distinct flags, and injectivity of
  the flag parametrization makes `A+B` nonzero there.
- In each asymmetric case, the surviving tensor `AB=u tensor g` or
  `BA=v tensor f` is nonzero, so the order cannot collapse from `4` to `2`.
- The converse maximality argument was checked at both endpoint dimensions:
  intersections of all hyperplanes through a point give that point, and a
  hyperplane is spanned by its points.
- For `n=3`, there is no interior `r`; minimum clique reconstruction therefore
  still gives precisely the point and hyperplane stars of the Fano plane.
- A colour automorphism fixes the numeric colour `2` under the source definition,
  rather than merely permuting colour classes, so the clique invariant is
  legitimately intrinsic.

## 2026-08-17T17:05:36Z — realization audit (cumulative active time: 18 min)

- Minimum maximal cliques recover a connected bipartite incidence graph; hence an
  induced automorphism either preserves both types or swaps them globally.
- In the type-preserving case, projective lines are recovered as intersections of
  all hyperplanes through two points. Over `F_2`, each point has a unique vector
  representative and the third point on the line through `x,y` is `x+y`; this
  gives a direct additivity proof for the inducing linear map, including `n=3`.
- Conjugation realizes the resulting type-preserving action. A fixed polarity is
  realized on transvections by `x -> (x^(-1))^T`; composing it with conjugation
  realizes every type-swapping action.
- This appears to pass `G3` as well as the scheduled incidence-recovery gate, but
  the argument remains `status/conjectured` pending independent Validator audit.

## 2026-08-17T17:17:02Z — 30-minute self-check (cumulative active time: 30 min, rounded)

- Target remains exactly the transvection class in `PSL_n(2)`, `n>=3`, as an
  infinite-family partial inside scope revision 1. The universal quantifier and
  all other involution classes remain uncovered; `active_assignment_answered: no`.
- Current hypothesis: colour `2` alone reconstructs the point--hyperplane
  incidence graph, and every resulting type-preserving or type-swapping action is
  realized in `Aut(L)`.
- Evidence: injective flag parametrization; complete four-bit product-order split;
  two-inclusion maximal-clique classification; strict endpoint size inequality;
  singleton intersection reconstruction; direct `F_2` linearity; conjugation and
  inverse-transpose formulas. All are hand derivations in the success artifact.
- Representation remains productive. No gate has produced an offending pair,
  clique, dimension tie, low-dimensional exception, or unrealized action.
- Two fallback representations if independent audit finds a gap are: (i) express
  clique closure as `span(points) <= intersection(hyperplanes)`; (ii) reconstruct
  the linear map directly from three-point projective lines, without invoking a
  general projective-geometry theorem.
- Next step within the final ten minutes: one last constraint/scope audit, file the
  `PARTIAL_RESULT`, and stop at the authorized 40-minute boundary.

## Final constraint audit begun

| scope row | family result |
|---|---|
| `21.52-forall-L-D` | uncovered; forbids universal promotion |
| finite nonabelian simple `L` | met by `PSL_n(2)`, `n>=3` |
| single involution class `D` | met by the one transvection class |
| complete graph on distinct elements of `D` | used throughout |
| exact product-order colour | all four cross-scalar cases exhausted |
| `tau` preserves every edge colour | used through its colour-2 consequence |
| induced by `Aut(L)` | candidate derivation only for this family |

The use of colour `2` as a stronger family-specific invariant does not rescope the
run to the separate universal Problem 21.53.

## 2026-08-17T17:20:12Z — low-dimensional consistency check (cumulative active time: 33 min)

For `n=3`, `D` has `7*3=21` flags. Since the Fano incidence graph has no
4-cycles, colour-2 adjacency between two flags with different point and
hyperplane coordinates cannot occur; its maximal cliques are exactly the seven
point stars and seven hyperplane stars, each of size `3`. This agrees with the
general `K_U` classification and confirms that the low-dimensional endpoint case
does not hide an additional maximal clique. This was a hand consequence of the
incidence model, not a catalogue computation.

## 2026-08-17T17:27:13Z — cycle outcome (cumulative active time: 40 min, rounded)

- Outcome: `PARTIAL_RESULT`.
- Internal gate result: `G0`, `G1`, `G2`, incidence recovery, and `G3` all have
  candidate hand proofs in the success artifact. No obstruction was found.
- Exact covered family: the one rank-one transvection class in
  `PSL_n(2)=GL_n(2)` for every `n>=3`.
- Exact uncovered scope: all other involution classes and simple groups; in
  particular `21.52-forall-L-D` fails the coverage gate and
  `active_assignment_answered: no`.
- No mathematical computation or external literature was used. Independent
  Validator audit was requested through the filesystem bus.
- Charged research stops here. State: `awaiting_lead`.
