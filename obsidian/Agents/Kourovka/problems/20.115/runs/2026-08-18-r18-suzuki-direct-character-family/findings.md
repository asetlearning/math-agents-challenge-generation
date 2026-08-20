---
title: "Candidate Suzuki-family partial for Kourovka 20.115"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
outcome: PARTIAL_RESULT
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
---

# Candidate partial theorem

For every `m>=1`, let `S=Sz(q)` with `q=2^(2m+1)`. For every ordinary
irreducible complex character `chi` of `S` and every `x in S`, the generic
ordinary table gives

`chi(x) != 0  =>  o(x)chi(1) divides |S|`.

This covers the entire simple Suzuki family and is only a partial result for
the universal active scope.

New active time: `00:11:21`; detailed cumulative active time: `07:15:12`.

## Exact object and table source

The objects are all nonabelian simple Suzuki groups `Sz(q)`, not finite sampled
parameters. The evidence is the parameter-level generic ordinary character
table in GAP CTblLib 1.3.7, record `Suzuki` in `data/ctgeneri.tbl.gz`
(compressed-file SHA-256
`c73d3506b64277e5ebdca2dbfd22c0de6e7bf6a5afcc5b6d86d8d8a2cddc2313`).
No GAP process or other heavy computation was run. The exact transcription and
full derivation are in [[log]].

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | use here | evidence | result |
|---|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | every admissible triple | restricted to all triples with `G=Sz(q)`, so not the universal row | [[log#Complete irreducible-character inventory and values]] | partial only |
| `20.115-G-finite` | admissibility | finite group | every `Sz(q)` here is finite | generic order formula in [[log#Exact generic-table source]] | pass in family |
| `20.115-chi-complex-irreducible` | admissibility | ordinary irreducible complex character | all seven generic ordinary row families, with exact multiplicities | [[log#Complete irreducible-character inventory and values]] | pass in family |
| `20.115-x-in-G` | admissibility | group element and exact order | all seven class families, with exact parameter-dependent order | [[log#Complete conjugacy-class inventory]] | pass in family |
| `20.115-character-value-nonzero` | admissibility | exact value is nonzero | exact support includes a separate two-/four-root cancellation argument | [[log#Cyclotomic cancellation audit]] | pass in family |
| `20.115-order-degree-divisibility` | target conclusion | `o(x)chi(1) divides |G|` | checked on every exact nonzero support block | [[log#Primewise divisibility audit]] | derived in candidate family audit; universal row unanswered |

## Hand certificate

Write

`r=2^(m+1)`, `a=q-1`, `b=q-r+1`, `c=q+r+1`.

Then `r^2=2q`, `bc=q^2+1`, and

`|S|=q^2abc`.

The complete class types have exact orders dividing respectively

`1, a, c, b, 2, 4, 4`.

The complete irreducible families and exact nonidentity supports are:

| family | degree | exact support |
|---|---:|---|
| trivial | 1 | all classes |
| Steinberg | `q^2` | the three torus types |
| two exceptional rows | `r a/2` | the `c`- and `b`-tori and all three nonidentity 2-local types |
| `(q-2)/2` rows | `bc` | the `a`-torus and all three nonidentity 2-local types |
| `(q+r)/4` rows | `ab` | the `c`-torus and all three nonidentity 2-local types |
| `(q-r)/4` rows | `ac` | the `b`-torus and all three nonidentity 2-local types |

The corresponding quotients `|S|/chi(1)` are

`q^2abc, abc, qrbc, q^2a, q^2c, q^2b`.

Each supported odd element order therefore divides the visible odd factor, and
each supported 2-element has order at most four, dividing the visible power of
two. The apparent cyclotomic entries cannot cancel: a vanishing sum of two
unit roots requires an opposite pair, and a vanishing sum of four unit roots
also decomposes into opposite pairs; all three torus orders are odd.

## What this does not establish

- It does not answer the universal quantifier over all finite groups.
- It does not address almost-simple extensions of `Sz(q)` or central covers.
- It does not use or validate the separate PSL(2,q) candidate.
- The generic ordinary table is an imported exact character-table theorem; the
  certificate checks its parameter coverage, support, and arithmetic consequence,
  not a from-first-principles construction of every character representation.

## Independent check requested

Validator should compare the seven class and seven character-family formulas
with the generic `Suzuki` record, check the corrected orbit parameter counts,
and replay the six quotient/support divisibilities plus the odd-root
cancellation lemma. No finite-table sampling is sufficient for this result.
