---
title: "Kourovka program board"
author: operator
tags:
  - agent/lead
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - project/kourovka
  - status/draft
---

# Kourovka board

> Protocol v2 migration (2026-08-16): this table is a human-readable legacy
> scheduling view. Canonical target, constraint, revision, direction, and closure
> state now live in `Agents/Kourovka/scopes/<scope-key>.json`. Existing rows retain
> their historical wording and do not acquire new mathematical status from this
> migration. Before any row is resumed or rescoped, Lead must create its atomic
> scope record and pass `_meta/scripts/kourovka-state-check.py`. A notebook number
> cannot be retired while any human-approved scope remains unanswered.

> Historical gate: the original priority five were approved. Reconcile live
> processes and migrate the selected atomic scopes before any new resumption; old
> `running` labels alone are not evidence that an agent process is live.

## Protocol-v2 active scopes

| # | Problem | Scope | Rev | Direction | Agent | State | Elapsed | Last outcome | Strategy | Next action |
|---:|---|---|---:|---|---|---|---:|---|---|---|
| 1 | 12.15 | `12.15/normal-closure-fibres` | 1 | none | none | parked | 333m used / increment exhausted | PARKED after reviewed order-128 elimination; larger orders and unrestricted scope open | none | restart only with an order-independent least-counterexample parameter bound or universal conjugacy-invariant bridge |
| 2 | 21.137 | `21.137/odd-prime-exponent-p2` | 2 | proof | Problem-21.137-Proof | running | 962m cumulative / fresh 45m allocation | metabelian norm identities admit a formal nonzero amplitude; global cocycle/basepoint coherence active | METABELIAN-COCYCLE-BASEPOINT-COHERENCE | impose one associative extension cocycle and simultaneous power-basepoint map over all quotient elements, then eliminate or realize the amplitude |
| 3 | 20.21 | `20.21/two-index-twelve-kernels` | 1 | none | none | parked | 128m used / 52m unspent | PARKED: reviewed minimum-witness reductions preserved; no bounded model retains both marked kernels, their isomorphism, and ambient order-three compatibility; existence open | none | resume only with a complete marked-datum model or new functorial invariant |
| 4 | 19.30 | `19.30/vanishing-order-simple-recognition` | 1 | none | none | parked | 158m used / 22m preserved | three fixed recognition subcases and a restricted separator survive review; universal scope open | none | restart only with a complete family-level vanishing-order formula or a uniform defect-zero/chief-factor bridge |
| 5 | 20.50 | `20.50/four-involution-universal-group` | 1 | none | none | parked | 161m used / 19m unspent | PARKED: QORBIT-CLOSURE refuted only as a strategy; exact order and finiteness remain open | none | resume only with a finite INN-4T completeness model or other target-facing global invariant |
| 6 | 21.137 | `21.137/two-group-exponent-8` | 1 | none | none | parked | legacy evidence preserved | excluded from odd-prime blind run | none | remain parked |
| 7 | 21.90 | `21.90/diameter-three-distance-graphs` | 3 | none | none | parked | 259m used / 25m unspent | local-root positivity is isolated to the validated rank-17 array; full scope open | none | resume only with a new signature lemma, explicit construction input, or target-faithful source-family invariant |
| 8 | 20.49 | `20.49/two-generated-same-exponent` | 1 | none | none | parked | 74m used / 106m preserved | reviewed prime-cover/rank-profile partial survives; compatibility frontier does not close either branch | none | restart only with a validated chief/crown bridge retaining exponent-loss and explicit lift data |
| 9 | 21.52 | `21.52/involution-class-product-order-colouring` | 1 | proof | Problem-21.52-Proof | running | 349m27s used / fresh 45m extension | candidate PSL2 equality covers even q, split odd q, and q=7; odd nonsplit polar geometry active | PSL2-NONSPLIT-POLAR-BLOCK-RIGIDITY | recover the geometric polar-line blocks and projective-line completion intrinsically for q congruent to 3 mod 4, q>=11 |
| 10 | 21.53 | `21.53/two-minimal-prime-colours` | 2 | none | none | awaiting_lead | 159m used / 21m preserved | candidate theorem for the double-transposition class of every A_n, n>=7; fresh validation pending | none | independently reconstruct the overlay table and common-neighbour counts before reuse |
| 11 | 20.115 | `20.115/nonzero-character-order-divisibility` | 1 | proof | Problem-20.115-Proof | running | 8h02m07s used / fresh 45m allocation | candidate GL(2,q) theorem unreviewed; prime-degree PSL2 field extension active | PSL2-PRIME-FIELD-EXTENSION-CLIFFORD | derive invariant-character extensions, induced rows, and exact semilinear norm orders across the field-automorphism coset |

This table stays empty until a legacy item is atomized and reconciled. Add a row in
the same atomic update as its canonical scope and roster record. The tables below
are retained as historical backlog and prior-run evidence.

## Priority five — Lead recommendation

| Priority | Problem | Importance | Progress likelihood | Reason |
|---:|---|---|---|---|
| 1 | [[20.21-two-index-twelve-normal-subgroups|20.21]] | medium-high | very high | A single finite witness settles it; compatible extensions with two prescribed quotients of order 12 give a sharply bounded constructive search. |
| 2 | [[21.31-regular-subgroups-holomorph-solubility|21.31]] | very high | high | Important to Hopf–Galois theory and skew braces; existing work restricts minimal obstructions to composition factors isomorphic to PSL(2,7), providing a concrete next reduction. |
| 3 | [[20.55-same-character-table-derived-length-gap|20.55]] | high | high | Exact character-table equality makes a discovered pair certifiable, while Mattarei's adjacent derived-length constructions provide structure rather than a blind search. |
| 4 | [[21.89-partition-number-not-dividing-factorial|21.89]] | medium | very high | The question reduces completely to explicit arithmetic; computation can expose a valuation pattern and rigorously cover exceptions while theory handles the tail. |
| 5 | [[21.90-distance-regular-graph-distance-graphs|21.90]] | high | medium-high | Published feasibility work reduces the problem to four infinite families of intersection arrays, making parameter elimination or explicit construction a realistic substantial advance. |

First reserve: [[20.50-four-involution-exponent-four-presentation|20.50]]. It is important and exact, but universal-presentation enumeration has a materially higher chance of consuming a cycle without a certified bound.

| # | Problem | Slug | Agent | State | Cycle | Elapsed | Ext | Last outcome | Validator | Next action |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [[21.3-alternating-symmetric-soluble-double-cosets|21.3]] | alternating-symmetric-soluble-double-cosets | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 2 | [[21.4-five-subgroups-trivial-solvable-intersection|21.4]] | five-subgroups-trivial-solvable-intersection | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 3 | [[21.31-regular-subgroups-holomorph-solubility|21.31]] | regular-subgroups-holomorph-solubility | Problem-21.31 | retired-stale | 1 | 7m | 0 | arXiv:2607.22795 exact target match | replicated | human status decision; stop internal search |
| 4 | [[21.32-derived-subgroup-realizability-algorithm|21.32]] | derived-subgroup-realizability-algorithm | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 5 | [[21.35-word-values-p-nilpotence|21.35]] | word-values-p-nilpotence | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 6 | [[21.50-characteristic-subgroup-three-groups|21.50]] | characteristic-subgroup-three-groups | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 7 | [[21.51-normal-abelian-subgroups-p-groups|21.51]] | normal-abelian-subgroups-p-groups | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 8 | [[21.52-involution-coloured-graph-automorphisms|21.52]] | involution-coloured-graph-automorphisms | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 9 | [[21.53-involution-tuple-hypergraph-automorphisms|21.53]] | involution-tuple-hypergraph-automorphisms | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 10 | [[21.54-finite-soluble-groups-with-triality|21.54]] | finite-soluble-groups-with-triality | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 11 | [[21.55-maximum-p-length-linear-groups|21.55]] | maximum-p-length-linear-groups | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 12 | [[21.57-formation-maximal-intersection|21.57]] | formation-maximal-intersection | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 13 | [[21.59-character-degree-multisets-almost-simple|21.59]] | character-degree-multisets-almost-simple | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 14 | [[21.64-normal-closure-p-length|21.64]] | normal-closure-p-length | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 15 | [[21.68-semi-abelian-groups-monomial|21.68]] | semi-abelian-groups-monomial | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 16 | [[21.73-conjugacy-problem-class-transpositions|21.73]] | conjugacy-problem-class-transpositions | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 17 | [[21.74-class-transposition-dynamical-properties|21.74]] | class-transposition-dynamical-properties | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 18 | [[21.81-simple-group-generation-probability|21.81]] | simple-group-generation-probability | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 19 | [[21.87-coprime-index-generation-bound|21.87]] | coprime-index-generation-bound | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 20 | [[19.30-vanishing-element-order-recognition|19.30]] | vanishing-element-order-recognition | Problem-19.30 | running | 1 | 0h | 0 | replacement for solved 17.76 | pending | source/staleness gate; counterexample screen |
| 21 | [[21.90-distance-regular-graph-distance-graphs|21.90]] | distance-regular-graph-distance-graphs | Problem-21.90 | running | 1 | <1h | 0 | GRAPE 4.9.0 installed | pending | resume remaining active budget |
| 22 | [[21.91-brauer-degree-sum-bound|21.91]] | brauer-degree-sum-bound | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 23 | [[21.92-brauer-character-count-bound|21.92]] | brauer-character-count-bound | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 24 | [[21.94-recognizability-by-unlabelled-prime-graph|21.94]] | recognizability-by-unlabelled-prime-graph | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 25 | [[21.95-almost-simple-prime-graph-recognizability|21.95]] | almost-simple-prime-graph-recognizability | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 26 | [[21.100-coprime-action-nonvanishing-characters|21.100]] | coprime-action-nonvanishing-characters | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 27 | [[21.101-almost-simple-regular-map-automorphisms|21.101]] | almost-simple-regular-map-automorphisms | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 28 | [[21.108-character-codegree-prime-bound|21.108]] | character-codegree-prime-bound | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 29 | [[21.109-codegrees-and-derived-length|21.109]] | codegrees-and-derived-length | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 30 | [[21.114-weakly-ab-maximal-derived-length|21.114]] | weakly-ab-maximal-derived-length | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 31 | [[20.21-two-index-twelve-normal-subgroups|20.21]] | two-index-twelve-normal-subgroups | Problem-20.21 | running | 1 | 11m | 0 | no witness through order 132 | pending | slot 1: bounded search through 240 |
| 32 | [[20.25-odd-character-values-symmetric-groups|20.25]] | odd-character-values-symmetric-groups | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 33 | [[20.30-perfect-centreless-class-size-bound|20.30]] | perfect-centreless-class-size-bound | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 34 | [[20.31-isospectral-groups-s10-j2|20.31]] | isospectral-groups-s10-j2 | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 35 | [[20.37-exact-set-factorizations-finite-groups|20.37]] | exact-set-factorizations-finite-groups | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 36 | [[20.48-hughes-subgroup-fixed-point-free-automorphism|20.48]] | hughes-subgroup-fixed-point-free-automorphism | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 37 | [[20.49-two-generated-subgroup-same-exponent|20.49]] | two-generated-subgroup-same-exponent | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 38 | [[20.50-four-involution-exponent-four-presentation|20.50]] | four-involution-exponent-four-presentation | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 39 | [[20.51-odd-order-groups-given-class-number|20.51]] | odd-order-groups-given-class-number | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 40 | [[20.52-odd-order-groups-given-conjugacy-deficiency|20.52]] | odd-order-groups-given-conjugacy-deficiency | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 41 | [[19.25-euler-totient-simple-recognition|19.25]] | euler-totient-simple-recognition | Problem-19.25 | running | 1 | 0h | 0 | replacement for 16.4 | pending | source/staleness gate; finite recognition search |
| 42 | [[20.66-critical-graph-triple-factorization|20.66]] | critical-graph-triple-factorization | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 43 | [[20.67-brauer-block-character-degree-bound|20.67]] | brauer-block-character-degree-bound | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 44 | [[20.75-abelian-subgroup-generator-bound-p-groups|20.75]] | abelian-subgroup-generator-bound-p-groups | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 45 | [[20.76-abelian-subgroup-order-bound-p-groups|20.76]] | abelian-subgroup-order-bound-p-groups | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 46 | [[20.82-socle-quotient-of-spectrum-recognizable-groups|20.82]] | socle-quotient-of-spectrum-recognizable-groups | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 47 | [[20.84-class-three-fifth-dimension-subgroup|20.84]] | class-three-fifth-dimension-subgroup | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 48 | [[20.86-sylow-count-p-element-bound|20.86]] | sylow-count-p-element-bound | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 49 | [[20.115-nonzero-character-value-order-divisibility|20.115]] | nonzero-character-value-order-divisibility | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 50 | [[20.122-minimal-triple-intersections-and-fitting-subgroup|20.122]] | minimal-triple-intersections-and-fitting-subgroup | — | queued | — | 0h | 0 | draft-selected | pending | human/crew gate |
| 51 | [[12.15-normal-closure-conjugacy-derived-subgroup|12.15]] | normal-closure-conjugacy-derived-subgroup | Problem-12.15 | running | 4 | 156m | 3 | C8 and elementary-Q49 branches eliminated | partial | bounded C4xC2/[32,27] full-dual branch |
| 52 | [[21.137-power-set-subgroup-powerful|21.137]] | power-set-subgroup-powerful | Problem-21.137 | parked | 1 | 1m | 0 | legacy result did not close every source scope; target fidelity requires reconstruction | pending | atomize source constraints before resume; no whole-problem retirement |
