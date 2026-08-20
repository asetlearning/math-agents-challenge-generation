---
title: "Working log — Kourovka 21.52 — alternating double-transposition reconstruction"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: proof
cycle: 9
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
---

# Working log — alternating double transpositions in \(A_n\)

## Active-time ledger

- `2026-08-18T04:48:41Z` — START cycle 9 proof lane; cumulative scope active minutes: 134. New-cycle allowance: at most 45 active minutes.

## Active target and source gate

Scope: `21.52/involution-class-product-order-colouring`, revision 1.

This clean family lane uses the canonical source transcription and the independently passed source-fidelity audit already recorded in the scope. The scope is discovery-blind, so `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`. The family target is only: for the single conjugacy class \(D_n\) of double transpositions in \(A_n\), prove the desired conclusion uniformly over an explicitly stated range \(n\ge 7\). Even success is an infinite-family `PARTIAL_RESULT`, not an answer for every finite nonabelian simple group.

### Seven-row scope checklist

| constraint id | role in this lane |
|---|---|
| `21.52-forall-L-D` | Not discharged universally: the lane deliberately proves only the admissible family \((A_n,D_n)\); this row therefore remains open for the notebook scope. |
| `21.52-L-finite-nonabelian-simple` | For every stated \(n\ge7\), \(A_n\) is finite nonabelian simple. |
| `21.52-D-single-involution-class` | \(D_n=\{(ab)(cd):a,b,c,d\text{ distinct}\}\) is the single \(A_n\)-conjugacy class of cycle type \(2^2 1^{n-4}\). |
| `21.52-Gamma-complete-on-D` | Every unordered pair of distinct members of \(D_n\) is used. |
| `21.52-edge-colour-exact-product-order` | The only edge datum is the exact integer \(|xy|\), not the conjugacy class of \(xy\). |
| `21.52-tau-preserves-all-edge-colours` | The input is an arbitrary permutation \(\tau\) of \(D_n\) preserving \(|xy|\) for every distinct pair. |
| `21.52-tau-induced-by-AutL` | Goal for the family: show \(\tau\) is conjugation by a point permutation, hence the restriction of an automorphism of \(A_n\); isolate the exceptional automorphism statement at \(n=6\). |

Explicit exclusions: Problem 21.53; unions of involution classes; product-conjugacy-class colouring; and any inference from this alternating-family theorem to all finite simple groups.

## Strategy portfolio

1. **Theoretical mode — selected (`ALTERNATING-DOUBLE-TRANSPOSITION-RECONSTRUCTION`).** Encode each vertex as a 2-edge matching on the natural point set. Derive the complete product-order table from the two coloured matchings' union graph. Use exact-colour two-point intersection data to recover the three matchings on each 4-support, then invoke/reprove the automorphism rigidity of the resulting Johnson 4-subset structure and recover points.
2. **Catalogue/small-case mode.** A bounded enumerator for \(7\le n\le N\) may test candidate intrinsic predicates and expose exceptional degrees. A collision only rejects that predicate; bounded success proves no uniform theorem.
3. **Structured-construction mode.** If direct fibre recovery fails, reconstruct the line graph of 2-subsets from maximal families of double transpositions sharing one transposition, then recover points from maximal intersecting line families.
4. **Certificate plan.** Give a hand-checkable union-component product-order table; exact polynomial two-point intersection signatures for every pair orbit; an intrinsic fibre predicate stated only in colour language; and a reconstruction proof whose only final external input is the explicitly qualified \(\operatorname{Aut}(A_n)\) theorem.

Theoretical mode is ranked first because the finite number of pair orbits makes its weakest gate—distinguishing same-support colour-2 pairs—cheap and exactly checkable.

## Exact combinatorial reduction

The matching-union analysis gives all product orders \(2,3,4,5,6\) and eight geometric rows. The only colour-2 rows are: same 4-support; one common edge with the remaining edges disjoint; and disjoint 4-supports. For these three types, exact joint-colour counts \((N_{33},N_{24})\) distinguish the same-support row for every \(n\ge7\). Full formulas and their hand partitions are in `findings.md`.

Consequently the three vertices on each 4-support are intrinsic blocks. The nine cross-fibre colours recover \(|S\cap T|\) by the four distinct multisets `2^9`, `6^9`, `2^1 3^4 4^4`, and `3^3 5^6` for support intersections 0, 1, 2, and 3.

## Bounded exploratory checks

Command observed:

`python3 Agents/Kourovka/problems/21.52/runs/2026-08-18-r9-alternating-double-transposition-reconstruction/pair_orbit_signatures.py`

The script exhaustively generated \(D_n\) for each \(7\le n\le12\), found respectively 7 pair types for \(n=7\) and 8 pair types for every \(8\le n\le12\), and printed the complete joint-colour signature of one representative of each type. The observed same-support \((N_{33},N_{24})\) sequence was `(12,6), (24,12), (40,20), (60,30), (84,42), (112,56)`, matching \((2(n-4)(n-5),(n-4)(n-5))\). The common-edge colour-2 sequence was `(12,2), (20,4), (28,8), (36,14), (44,22), (52,32)`, and the disjoint-support type appeared from \(n=8\) with `N33=32`. This was a bounded predicate-discovery check, not evidence for the uniform theorem; the formulas were then derived by hand.

Command observed:

`python3 Agents/Kourovka/problems/21.52/runs/2026-08-18-r9-alternating-double-transposition-reconstruction/n8_complement_lift.py`

Exact output:

```text
supports 70
nontrivial_pair_constraints 1820
search_nodes 1
complement_lift_exists False
```

This finite CSP check was only a prompt to find the certificate now written in `findings.md`: complementation maps a top triangle with identity colour-3 holonomy to a bottom triangle with transposition holonomy, so it cannot lift. The candidate proof does not rely on the search.

## Candidate family partial

The reconstruction closes the single double-transposition class in \(A_n\) uniformly for every \(n\ge7\): after the degree-8 complement obstruction, the induced support action is point-induced, and bottom-triangle holonomies force the fibrewise kernel to be trivial. The exact conclusion is conjugation by a unique element of \(S_n\). This leaves `21.52-forall-L-D` open and is therefore an infinite-family `PARTIAL_RESULT`, not a universal `CLAIM`.

Artifact hashes at stop:

- `pair_orbit_signatures.py`: `c31f928937b0d3886ff65168934a3afe6d5abe504803f19d1931ef0e7fc345e5`.
- `n8_complement_lift.py`: `d3df9544d366894ec698e01061111c6fafd1c76067048bd75fb5febcdce2d6a2`.
- `findings.md`: `357dfe1120a64f7bacb158ebec057130ad1e4f0ba9284b64b6d90ceb5a7f59d3`.

- `2026-08-18T04:58:08Z` — STOP after writing and hashing the candidate family theorem; 10 new active minutes charged, cumulative scope active minutes: 144. Outcome: `PARTIAL_RESULT`; state: `awaiting_lead` and fresh validation.
