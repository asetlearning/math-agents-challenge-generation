---
title: "Problem 21.52 cycle 12 — four-transposition small degrees"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
cycle: 12
strategy: FOUR-TRANSPOSITION-SMALL-DEGREES-EXACT
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

# Exact small-degree audit for the four-transposition class

## Active-time ledger

- `2026-08-18T05:46:12Z`: work start at cumulative active minute 182; cycle allowance is at most 45 new active minutes.
- `2026-08-18T06:09:23Z`: work stop after 24 new active minutes, cumulative active minute 206; outcome `PARTIAL_RESULT`; state `awaiting_lead` while independent validation is pending.

## Source and scope gate — 2026-08-18T05:51:43Z

Read the configured source PDF, page 172, both as `pdftotext -layout` and as a rendered page image. The source says:

> Let \(L\) be a finite non-abelian simple group, and let \(D\) be a conjugacy class of involutions in \(L\). On the complete graph with vertex set \(D\), colour \(\{a,b\}\) exactly by \(|ab|\). Is every colour-preserving permutation induced by an automorphism of \(L\)?

The displayed superscripts \(a^\tau,b^\tau\), the quantifier "every edge", and the exact equality \(|ab|=|cd|\) agree with the canonical revision-1 scope. `source_transcription_checked: yes`; `active_scope_checked: yes`. The adjacent Problem 21.53 is visibly a different question and is excluded.

This is a discovery-blind continuation (`blind_run.enabled: true`, `open_web: false`), so `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`. The canonical synthesis records the source problem as unstarred. The advertised corpus JSONL for issue 21 is absent; no corpus flag is invented.

### Seven-constraint reconciliation

| constraint_id | role | application in this bounded family | gate |
|---|---|---|---|
| `21.52-forall-L-D` | admissibility | The universal quantifier is not discharged; this cycle treats only six pairs \((A_n,D_n)\), \(8\le n\le13\). | partial only |
| `21.52-L-finite-nonabelian-simple` | admissibility | \(A_n\) is finite nonabelian simple for every \(n\ge5\). | pass |
| `21.52-D-single-involution-class` | admissibility | \(D_n\) is to be checked as the single \(A_n\)-class of cycle type \(2^4 1^{n-8}\); every element has order 2. | pending explicit audit |
| `21.52-Gamma-complete-on-D` | admissibility | Every unordered pair of distinct four-matchings is an edge. | pass by construction |
| `21.52-edge-colour-exact-product-order` | admissibility | Pair colours will be computed from the exact permutation product order, with all occurring orders listed. | pending exact audit |
| `21.52-tau-preserves-all-edge-colours` | admissibility | The target group is the full simultaneous automorphism group of all exact-order binary relations. | pending exact audit |
| `21.52-tau-induced-by-AutL` | target conclusion | For each \(n\), compare this group as a permutation group on \(D_n\) with the restriction image of the setwise stabilizer in \(\operatorname{Aut}(A_n)\). | pending |

Explicit exclusions: no claim about Problem 21.53; no union of involution classes; no colouring by the conjugacy class of \(ab\); no inference from this bounded family to all finite simple groups.

## Strategy portfolio

1. **Small exact orbit mode (first).** Classify the \(S_n\)-orbits on ordered pairs of four-matchings via their alternating union components and calculate exact product orders independently. For \(n=8\), feed the complete 105-vertex colour structure to `dreadnaut`; for larger degrees use orbit-level intersection signatures rather than a complete dense matrix.
2. **Structured reconstruction mode.** Seek a colour-definable relation equal to "the two four-matchings share three transpositions" (or the best small-degree substitute). Reconstruct the underlying transposition set and then the natural \(n\)-point set from maximal cliques/stars.
3. **Theoretical mode.** Prove \(\operatorname{Aut}` of the reconstructed matching-incidence graph is \(S_n\), auditing the exceptional shapes at \(n=8,9\). Separately use the standard \(\operatorname{Aut}(A_n)=S_n\) theorem for \(n\ge7\), and explicitly identify the outer coset at \(n=8\).
4. **Certificate plan.** Save canonical pair-orbit representatives, exact order palettes, defining intersection signatures, and `dreadnaut` output. Equality will be the two containments \(S_n\le\operatorname{Aut}_{\rm col}(D_n)\le S_n\) on the same labelled action, not an order comparison.

Ranking: derive the orbit table and test reconstructing signatures first; if the relation is not colour-definable in some degree, use the exact 105-vertex computation at \(n=8\) and a degree-specific incidence reconstruction for \(n=9,\dots,13\). Kill criterion: if no colour-invariant relation with a hand-auditable reconstruction emerges by +25 minutes, freeze a bounded exact computation plan and request a Lead lease rather than launching heavy work.

## Exact orbit and colour audit — 2026-08-18T06:00:59Z

Created the independent purpose-built enumerator `scratch/orbit_audit.py`. For each \(n=8,\ldots,13\), it generated all \(105\binom n8\) four-matchings, fixed the matching `((0,1),(2,3),(4,5),(6,7))`, and exhausted all other vertices. A pair key records common edges plus the alternating coloured-union path/cycle multiset. The program independently computed the literal permutation-product order and the theoretical component formula, asserting equality on every vertex. Orbit multiplicities were asserted to sum to \(|D_n|-1\).

Observed bounded batch output:

```text
n=8  vertices=105    palette=[2,3,4]                              pair_orbits=4  signature_collisions=0
n=9  vertices=945    palette=[2,3,4,5,6,7,9,10]                  pair_orbits=11 signature_collisions=0
n=10 vertices=4725   palette=[2,3,4,5,6,7,8,9,10,12,15,21]      pair_orbits=30 signature_collisions=0
n=11 vertices=17325  palette=[2,3,4,5,6,7,8,9,10,12,14,15,20,21] pair_orbits=43 signature_collisions=0
n=12 vertices=51975  palette=[2,3,4,5,6,7,8,9,10,12,14,15,20,21,30] pair_orbits=57 signature_collisions=0
n=13 vertices=135135 palette=[2,3,4,5,6,7,8,9,10,12,14,15,20,21,30] pair_orbits=62 signature_collisions=0
orbit-batch elapsed=24.63 rss_kb=82048
```

For a pair \((x,y)\), the complete intrinsic array \(N_{r,s}(x,y)=|\{z:|xz|=r,|yz|=s\}|\) separates every stabilizer pair orbit in all six degrees. At \(n=8\), exact order 3 is precisely common-edge count 1. At \(n=9\), the common-three relation is one uniquely signed order-3 orbit. At \(n=10,\ldots,13\), common-three is the union of two uniquely signed orbits, of orders 2 and 3. Hence an exact-colour automorphism preserves the relation \(R_8:\ |M\cap N|=1\), respectively \(R_n:\ |M\cap N|=3\) for \(n\ge9\).

## Exact full relation automorphism groups — 2026-08-18T06:03:00Z

`scratch/matching_relation_dre.py` regenerated complete sparse dreadnaut inputs. Internal assertions checked every vertex degree and the handshake edge count. All jobs were expected and observed below 60 seconds and 1 GB, so no heavy-compute lease was required. Nauty/dreadnaut 2.8.8 gave:

```text
n=8  v=105    degree=32 edges=1680    full relation group=40320=8!
n=9  v=945    degree=8  edges=3780    full relation group=362880=9!
n=10 v=4725   degree=20 edges=47250   full relation group=3628800=10!
n=11 v=17325  degree=36 edges=311850  full relation group=39916800=11!
n=12 v=51975  degree=56 edges=1455300 full relation group=479001600=12!
n=13 v=135135 degree=80 edges=5405400 full relation group=6227020800=13!
dreadnaut-batch elapsed=6.46 rss_kb=101760
```

Every dreadnaut stderr file is empty. Outputs include generators, not only orders. The natural \(S_n\) action on the same labelled matching set is visibly relation-preserving and faithful; `scratch/certify_boundary.py` regenerated all adjacent-point-transposition actions as bijections. Thus the natural \(S_n\) is an identified subgroup of the full relation group of the displayed full order, so equality is an action-level containment conclusion rather than an order-only guess.

## `A_8` outer audit — 2026-08-18T06:04:23Z

GAP 4.12.1 independently returned `Size(Aut(A8))=40320`, inner group size 20160, outer quotient size 2, and the two involution-class sizes 210 (double transpositions) and 105 (four transpositions). Since natural conjugation by \(S_8\) injects into \(\operatorname{Aut}(A_8)\) with the full order 40320, the unique outer coset is precisely represented by odd point permutations; it preserves the four-transposition class. Exact script/output: `scratch/a8_outer_audit.g`, `scratch/a8_outer_audit.out`.

## Short self-check and outcome — 2026-08-18T06:07:00Z

- **Target:** exactly \((A_n,D_n)\) for the one class \(2^4 1^{n-8}\), \(8\le n\le13\), revision 1. No prior \(n\ge14\) array or theorem was read or used.
- **New facts:** complete order palettes and pair relations; intrinsic two-point signatures defining a rigid relation; exact full relation groups; explicit Aut\((A_8)\) outer audit.
- **Containments:** natural \(S_n\le\operatorname{Aut}_{\rm col}(D_n)\le\operatorname{Aut}(R_n)=S_n\), on the same labelled action; the Aut\((A_n)\) restriction image is that same natural \(S_n\).
- **Small-degree failure:** share-three is empty at \(n=8\); at \(n=9\) its core stars have size only 3. The substitute exact computations cover both rather than invoking a false uniform largest-clique premise.
- **Seven constraints:** six family-local gates pass in the submitted argument; `21.52-forall-L-D` remains undistributed outside these six pairs, so the outcome is only `PARTIAL_RESULT` and `active_assignment_answered: no`.
- **Bottleneck:** independent reconstruction by Validator, especially the orbit-key completeness and the largest \(n=13\) sparse input.
- **Recommendation:** validate \(n=8,9\) first and spot-check \(n=13\); only after separate validation may MathExpert consider splicing this boundary with an independently reviewed \(n\ge14\) result.

The aggregate checker printed `PASS degrees=8..13 all exact gates`; its certificate is `scratch/boundary-certificate.json`. Detailed argument and limitations are in `findings.md`.
