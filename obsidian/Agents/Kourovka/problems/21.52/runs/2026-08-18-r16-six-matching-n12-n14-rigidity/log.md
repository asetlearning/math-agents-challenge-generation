---
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
cycle: 16
strategy: SIX-MATCHING-N12-N14-RIGIDITY
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/alternating-groups, project/kourovka, status/draft]
---

# Cycle 16 log — six-transposition class in degrees 12--14

## 2026-08-18T10:12:00Z — active work start

- Ledger at start: cumulative active minute 278; this increment authorizes at most 45 active minutes.
- Exact assignment: only the conjugacy class of permutations of type `2^6 1^(n-12)` in `A_n`, for `n=12,13,14`.
- Discovery isolation: the cycle-15 theorem and pair statistics are not premises and its run files were not opened. The canonical record has `blind_run.enabled: true`, so open-web staleness checking is deferred.

## Staleness and source-fidelity gate

The configured source PDF exists and was read at rendered page 172, both as layout text and as a 160-dpi rendered page. Corrected transcription:

> **21.52.** Let \(L\) be a finite non-abelian simple group, and let \(D\) be a conjugacy class of involutions in \(L\). Consider the complete graph \(\Gamma\) with vertex set \(D\). Define an equivalence relation \(\sim\) (graph coloring) on the set of edges as follows: \((a,b)\sim(c,d)\) if and only if \(|ab|=|cd|\). An automorphism of the coloured graph \(\Gamma\) is a permutation \(\tau\in S_D\) such that \((a,b)\sim(a^\tau,b^\tau)\) for every edge \((a,b)\). Is it true that the automorphism group of \(\Gamma\) is a subgroup of \(\operatorname{Aut}(L)\)?

The adjacent Problem 21.53 is a separate two-selected-colour question and is excluded here. The rendered statement has no editor or later comment. The locally configured corpus directory ends at issue 20 and therefore has no issue-21 JSONL row from which to read the three extraction flags; this absence is recorded rather than silently inventing them. The canonical scope record itself reports no answer and `scope_answered:false`.

- `source_transcription_checked: yes`
- `active_scope_checked: yes`
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

### Clause matrix

| source clause | exact interpretation | active here? | literature status in this blind run |
|---|---|---:|---|
| finite non-abelian simple \(L\), one involution conjugacy class \(D\) | for this family, \(L=A_n\) and \(D\) is the single `2^6 1^(n-12)` class | yes, only \(n=12,13,14\) as a family partial | external check deferred |
| complete graph on \(D\) | every unordered pair of distinct class elements is an edge | yes | definitional |
| equal colour iff \(|ab|=|cd|\) | exact element order, not product conjugacy class | yes | definitional |
| colour automorphism \(\tau\) | \(|ab|=|a^\tau b^\tau|\) for every distinct pair | yes | definitional |
| ask \(\operatorname{Aut}_{col}(\Gamma)\leq\operatorname{Aut}(L)\) | typed as restriction of the setwise stabilizer of \(D\) in \(\operatorname{Aut}(L)\) | yes | universal question remains open in canonical record |

### Seven-constraint checklist

| constraint id | role in this bounded family |
|---|---|
| `21.52-forall-L-D` | the notebook quantifier is universal; this run can establish only the stated alternating-family partial, never the universal conclusion |
| `21.52-L-finite-nonabelian-simple` | \(A_n\) is finite nonabelian simple for \(n=12,13,14\) |
| `21.52-D-single-involution-class` | permutations of cycle type `2^6 1^(n-12)` are involutions and form one \(A_n\)-class because the symmetric cycle type has even repeated parts, hence does not split in \(A_n\) |
| `21.52-Gamma-complete-on-D` | all distinct pairs of six-matchings are considered |
| `21.52-edge-colour-exact-product-order` | every relation used must be recovered from the exact product-order colouring |
| `21.52-tau-preserves-all-edge-colours` | arbitrary permutations of \(D\) preserving every exact order colour are the objects bounded |
| `21.52-tau-induced-by-AutL` | target for each fixed degree is equality with the natural \(S_n\) restriction; for \(n\ge 7\), \(n\ne 6\), \(\operatorname{Aut}(A_n)\cong S_n\) |

Explicit exclusions: no Problem 21.53; no union of involution classes; no uncoloured-complete-graph automorphisms; no product-conjugacy-class refinement; no claim that three bounded degrees settle the universal scope.

## Strategy portfolio

Ranked by expected information per active minute:

1. **Theoretical incidence mode.** Regard each class element as a six-edge matching. Derive product order from alternating union components. Recover the five-common-edge exchange graph for \(n=13,14\), respectively the four-common-edge flip graph for \(n=12\), from an independently computed exact two-point colour signature; classify the relation graph's maximal star/top cliques and reconstruct the ground points.
2. **Exact small-orbit mode.** Enumerate only orbit representatives of ordered matching pairs under the natural \(S_n\), and for each compute the complete two-point colour-intersection array. This is a bounded certificate for colour-definability of the desired sparse relation, not by itself a full automorphism-group certificate.
3. **Sparse relation automorphism mode.** If the hand reconstruction stalls, use a frozen sparse-graph automorphism calculation. Equality must include explicit natural \(S_n\) generators/containment and faithfulness, not merely group order. Any expected run beyond 60 seconds will be frozen and leased first.
4. **Separating-permutation mode.** If a relation graph has extra automorphisms, test each candidate on the complete exact-order matrix and return an explicit first violated/preserved condition; only an extra full-colour automorphism could be a counterexample.

Certificate plan: exact matching encoding; complete orbit/signature table; a written star/top reconstruction or full sparse-graph generators; explicit natural adjacent-transposition action on matchings; and a labelled containment/equality check.

## 2026-08-18T10:17:04Z--10:44:30Z — exact work

### Independent pair-orbit and colour-signature enumeration

Commands actually run:

```bash
/usr/bin/time -f 'ELAPSED=%e MAXRSS_KB=%M EXIT=%x' timeout 60s python3 .../scratch/matching_orbits.py
python3 .../scratch/pair_colour_signatures.py 12 --compact
python3 .../scratch/pair_colour_signatures.py 13 --compact
python3 .../scratch/pair_colour_signatures.py 14 --compact
```

The pair inventory completed in 23.00 seconds and enumerated `10395/135135/945945` vertices with `10/29/74` coarse union-component signatures for `n=12/13/14`. The `n=14` key can merge orientations of unequal odd paths, so it is not a full orbit claim outside the needed colours; colours 2 and 3 contain only the orientation-balanced path types described in `findings.md`, making the candidate lists there complete. Compact intrinsic separators:

- `n=12`, order-2 orbits with common-edge counts `0,2,4`: `N_22=61,37,73`; the desired four-edge flip is uniquely `73`.
- `n=13`, order-3 orbits with common-edge counts `0,2,3,5`: `N_23=33,15,21,0`; desired five-edge adjacency is uniquely `0`.
- `n=14`, all order-2 ambiguous orbits: `N_24=258,122,176,260,290,530`; all order-3 ambiguous orbits: `72,24,39,201,25,125`. The two five-common-edge types are uniquely `(order,N_24)=(2,530)` and `(3,125)`. The final compact run took 46.53 seconds and 17,792 KiB.

### Relation automorphisms

1. `n=12`: the full GRAPE/nauty flip-graph run exited zero in 7.60 seconds, 142,720 KiB. It constructed the faithful labelled natural `S_12`, checked it is a subgroup of the full graph group, and obtained exact permutation-group equality of order `479001600` on 10,395 vertices (degree 30, 155,925 edges).
2. `n=13`: `scratch/n13_local_distance_certificate.py` completed in 13.00 seconds, 91,612 KiB. The local graph is `6 K_2`; distance colouring from the pointwise-fixed closed neighborhood followed by equitable refinement has colour counts `7701 -> 107463 -> 135135`, so the kernel is trivial. Thus the vertex stabilizer is at most `2^6 6! = 46080` and the full group at most `13!`; faithful natural `S_13` containment gives equality.
3. Perfect-matching `F_14`: `scratch/n14_flip_kernel_refinement.py` completed in 12.29 seconds, 151,488 KiB. Local direction-pair common-neighbor counts are `1` within a direction, `2` for disjoint directions, `3` for intersecting directions. On direction triangles, triple-common-neighbor counts are `1` for even orientation parity and `3` for odd. Hence the local image has size at most `2^6 7!`. Pointwise closed-neighborhood refinement has 1,303 singleton and 66,916 two-element stable cells; individualizing one point of a two-cell makes the partition discrete, bounding the kernel by 2. Therefore `Aut(F_14)=S_14` by faithful natural containment and the `14!` upper bound.
4. `n=14`: maximal cliques in the five-edge graph are core-stars of size 6 and perfect-matching tops of size 7. Each star meets exactly three tops in two vertices each, reconstructing `F_14`. The induced top action is faithful because every pair inside a top is its intersection with a unique star. Therefore `Aut(X_14)` embeds in `Aut(F_14)=S_14`; natural containment gives equality.

### Failed heavy invocation (non-evidence)

Two honest 60-second probes of the large GRAPE jobs timed out. A frozen manifest and hashes were sent to Lead. Lead leased slot 1 for the single frozen runner. It was invoked exactly once; the first redundant `n=13` job timed out (`exit 124`, `ELAPSED=172.58`, `MAXRSS_KB=302592`) with empty stdout, and fail-fast prevented the `n=14` job from launching. Slot 1 was immediately released by bus report. No result from this failed run is used.

## 2026-08-18T10:44:30Z — research stop and packaging

- New active research time charged: 33 minutes, cumulative scope ledger `278 -> 311`.
- Research stopped below the 45-minute cap; packaging began after the stop.
- Outcome: `PARTIAL_RESULT`, a candidate equality for exactly the six-transposition classes in `A_12,A_13,A_14`. The universal Problem 21.52 scope remains open.
- Full argument and reproducibility details: `findings.md` in this run directory.
