---
title: "Kourovka 21.137 — order-3^10 pair classification and map-manifest obstruction"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
direction: counterexample
strategy: O310-EQUIVARIANT-LABEL
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
active_minutes_charged: 8
scope_cumulative_active_minutes: 449
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r17-o310-equivariant-label/log.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T122251Z-min9-action-family-empty.md
---

# Order-`3^10` structural gate

## Exact active target

The active scope remains: `p>2`, finite same-prime group of exact exponent `p^2`, complete actual `p`th-power value set itself a subgroup, and the question whether that subgroup is abelian. This gate fixes `p=3` and seeks a nonabelian actual cube subgroup in an exponent-`9` group. It constructs no group, so every finite-group admissibility row remains unpassed and `active_assignment_answered: no`.

## Candidate complete pair classification

Conditional only on the reviewed quotient-minimal rows named by Lead, a hypothetical least `p=3` counterexample of order `3^10` has

`P ~= H_3(3) x C3^2`, `|P|=3^5`, and `|R=G/P|=3^5` with `exp(R)=3`.

Indeed, for `|P|=3^m` the reviewed inequalities give `m>=5` and

`log_3|G/P| >= m-floor((m-1)/3)`.

Total logarithmic order `10` forces `m=5`. The reviewed class-two, exponent-three, `P'=C3`, and centre-dimension-at-least-three rows then identify `P` as displayed.

There are exactly four candidate quotient types. Each is represented by an alternating map `beta:Lambda^2(V)->W`, with `dim(V)+dim(W)=5`:

| quotient | `dim V` | `dim W` | nonzero basic values of `beta` |
|---|---:|---:|---|
| `C3^5` | 5 | 0 | none |
| `H_3(3) x C3^2` | 4 | 1 | `beta(e1,e2)=z1` |
| extraspecial exponent-three `3_+^(1+4)` | 4 | 1 | `beta(e1,e2)=beta(e3,e4)=z1` |
| `K32` | 3 | 2 | `beta(e1,e2)=z1`, `beta(e1,e3)=z2` |

Here `K32` denotes the unique class-two exponent-three group associated to a surjection `Lambda^2(F3^3)->F3^2`.

Completeness: `Phi(R)=R'`. Generator rank five is abelian. Rank four gives a central derived line and the rank-two/rank-four alternatives for an alternating form on a four-space. Rank at most two is too small because every two-generated exponent-three group has order at most `27`. At rank three, `|R'|=3^2`. If `gamma_3(R)` were nontrivial, a nonzero symbol `[[x,y],z]` would make the three pair symbols `[x,y],[x,z],[y,z]` independent modulo `gamma_3` by bracketing a relation with `z,y,x`; repeated-variable triple brackets vanish inside two-generated exponent-three subgroups. This would require at least four dimensions in `R'`, a contradiction. Thus `R` is class two, and `GL_3(3)`-transitivity on lines of `Lambda^2(F3^3)` gives the single surjective form.

The exact coordinate law

`(v,z)(v',z')=(v+v',z+z'+(1/2)beta(v,v'))`

gives all `243` elements, products, commutators, and conjugacy relations for every row.

## Map-complete manifest schema

Let `S` be the reviewed Sylow `3`-subgroup of `Out(P)`, of order `3^8`. Every outer action is conjugate to one with image in `S`. For a row `(V,W,beta)`, every homomorphism `rho:R->S` and only such a homomorphism is specified by images `a_i` of a basis of `V` and central images `c_j` of a basis of `W`, subject to

- every `a_i,c_j` has cube one;
- every `c_j` commutes with every entry;
- `[a_i,a_j]=product_k c_k^(beta(e_i,e_j)_k)`.

A valid later row would have to retain the full `243`-element map, not only `U=rho(R)`: exact kernel and `k=243/|U|`; fibrewise quotient commutator/conjugacy multiplicities; the nine inner-action lifts over every `rho(r)^(-1)` (each with `27` actual lifts); the label and central-supply table; and every conjugacy-equivariance equation.

## Why the structural gate stops

The four pair types are short. The homomorphism rows are not. The raw exact cover has up to `|S|^5=3^40` tuples. A short complete list needs a new orbit theorem or categorical enumeration under simultaneous `Out(P)` conjugacy and `Aut(R)` precomposition. Neither exists in the reviewed inputs.

The earlier image-subgroup census is not a substitute: it records an abstract image and kernel size, while this strategy was chosen precisely to retain map-specific quotient-element and relation correlations. Replacing all epimorphisms onto one `U` by one row would be an unproved conflation.

Thus the mandated precomputation hard kill fires. `O310-EQUIVARIANT-LABEL` is exhausted at the structural-manifest gate, but the order-`3^10` pair classification is a bounded candidate partial result suitable for Validator reconstruction. No factor system, cocycle, extension, descendant, GAP run, web/history route, or excluded prime/clause was opened.
