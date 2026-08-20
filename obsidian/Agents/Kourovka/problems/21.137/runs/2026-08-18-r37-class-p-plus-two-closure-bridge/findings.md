---
title: "Kourovka 21.137 r37 — last-layer p-power reduction"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
outcome: PARTIAL_RESULT
active_assignment_answered: no
active_minutes_used: 16
official_cumulative_minutes: 781
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/hall-collection, project/kourovka, status/conjectured]
---

# Last-layer reduction at class `p+2`

## Active target

Scope: `21.137/odd-prime-exponent-p2`, revision 2. The assigned bounded target
asks whether every source-admissible group of class at most `p+2` has abelian
literal power subgroup. The unrestricted source target remains strictly broader.

## Partial claim

Let `p` be odd, let `G` have exponent dividing `p^2` and class at most `p+2`,
and suppose the literal set `P={g^p:g in G}` is a subgroup. Then

`[P,P] <= gamma_{p+2}(G)^p <= Z(G) intersect P`.

Here `gamma_{p+2}(G)^p` is the literal set of `p`th powers of the central
abelian group `gamma_{p+2}(G)`, hence is itself a subgroup.

Consequently `P` is abelian if the last lower-central term has exponent at most
`p`. In general, literal closure alone is invariant under the central root shifts
that realize this residual defect, so this argument does not prove it trivial.

There is also a stronger exceptional-prime conclusion: for `p=3`, the full
assigned class-five family has abelian `P`. More generally, the conclusion holds
at any odd `p` under the additional condition `cl(G/P)<=p`.

## Constraint-and-conclusion matrix

| constraint_id | role | proof use / candidate result | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | last-layer reduction is uniform; abelianity is obtained only at `p=3` or under `cl(G/P)<=p` | pass for partial families; fail for full scope |
| `21.137-odd-p-not-2` | admissibility | uses `p+2<2p` and standard odd-prime binomial divisibility; `p=3` is checked separately | pass |
| `21.137-odd-finite-p-group` | admissibility | applies to every finite source group in the bounded family (the hand argument itself does not need finiteness) | pass |
| `21.137-odd-exponent-p2` | admissibility | proved under the inclusive stronger-form hypothesis `exp(G)|p^2`, hence includes exact exponent `p^2` | pass |
| `21.137-odd-power-set-definition` | admissibility | every `u in P` is an actual power and therefore `u^p=1`; no generated-power substitution | pass |
| `21.137-odd-power-set-subgroup` | admissibility | gives `PC/C` as the literal subgroup in the quotient and supplies an actual root `z^p=x^p y^p` | pass |
| `21.137-odd-P-abelian` | target conclusion | proved for `p=3`, class at most five, and conditionally when `cl(G/P)<=p`; otherwise reduced to the last-layer defect | partial only |

## Proof

Use `[u,v]=u^-1 v^-1 u v` and put `C=gamma_{p+2}(G)`. Then `C<=Z(G)`.
The quotient `G/C` has exponent dividing `p^2`, class at most `p+1`, and literal
power set `PC/C`, a subgroup. The independently reviewed class-`p+1` theorem
therefore gives `[P,P]<=C`.

For completeness, collect `[X^p,Y^p]` in the free nilpotent group of class
`p+2`. The reviewed Magnus/Newton argument says that the exponent of a mixed
basic commutator `b` of multidegree `(r,s)` has the integral form

`f_b(p,p)=sum a_(b,i,j) binom(p,i)binom(p,j)`, with `1<=i<=r`, `1<=j<=s`.

Coordinates through weight `p` are divisible by `p^2`. At weight `p+1`, all
but the unique extreme multidegrees `(p,1)` and `(1,p)` are also `p^2`-divisible.
Every coordinate at weights `p+1` and `p+2` is divisible by `p`: a nonzero
summand has `i,j<=p`, while `i=j=p` would force `2p<=r+s<=p+2`, impossible for
odd `p`. After specialization to `G`, exponent `p^2` kills all twice-divisible
factors. Weight-`p+2` factors are central and their remaining exponents are
multiples of `p`, so they lie in `C^p`.

It remains to handle either extreme weight-`p+1` basic commutator `e`. In `G/C`,
the extreme-coordinate sublemma inside the reviewed theorem gives
`eC in <(G/C)^p>`. Since the literal image `PC/C` is a subgroup, this generated
subgroup equals `PC/C`. Thus `e=uc` for some `u in P`, `c in C`. Actual-value
membership and `exp(G)|p^2` give `u^p=1`; centrality gives `e^p=c^p in C^p`.
Every surviving Hall factor is therefore in `C^p`, proving the inclusion.

## Why literal closure does not finish this collection

For `A=x^p`, `B=y^p`, set `D=[A,B]` and choose `c in C` with `c^p=D`.
Literal closure gives some `z`—chosen only for this pair—with `z^p=AB`. Since
`AB=BA D`,

`(z^A)^p=BA=(z c^-1)^p`.

These are merely two roots in the same fibre; the hypotheses do not identify
them. In fact `(g c^k)^p=g^p D^k`, so central order-`p^2` elements automatically
saturate the literal image along their `p`th powers. Thus the remaining defect
is not lost by replacing the literal set with `G^p`; it persists even after the
literal closure equation is used exactly. A further theorem would need genuine
root-fibre rigidity forcing `C^p cap [P,P]=1`.

## `p=3` audit

For class five, weights `<=3` die by divisibility by `9`; the weight-four
`(2,2)` coordinate also dies, and the extreme `(3,1),(1,3)` coordinates are
multiples of `3`. All weight-five coordinates—multidegrees `(4,1),(3,2)`,
`(2,3),(1,4)`—are multiples of `3`, including every basic commutator in the
two-dimensional `(3,2)` and `(2,3)` homogeneous components. The independently reviewed class-five
contamination term belongs to `C=gamma_5(G)` and is absorbed into the central
lift `c`; cubing still lands in `C^3`. Hence no exceptional coefficient escapes
the reduction at `p=3`.

The exceptional prime in fact closes. Put `H=G/P`, which has exponent three.
For `a,b in H`, write `u=b`, `v=b^a`, `w=b^(a^2)`. The identities
`(ab)^3=1` and `(a b^-1)^3=1` give `wvu=1` and `uvw=1`. Thus
`w=u^-1v^-1=v^-1u^-1`, so `u` and `v` commute. Hence
`[b,a]=u^-1v` centralizes `b`; after swapping variables, every two-generator
subgroup has class at most two and `H` is 2-Engel. The standard elementary
2-Engel lemma (`gamma_4(H)=1`) now gives `gamma_4(G)<=P`.

Every Hall factor that survived the divisibility audit has weight four or five,
so its underlying basic commutator lies in `P`. Since every element of literal
`P` is a cube in a group of exponent dividing nine, `exp(P)<=3`; all surviving
cubes are trivial. Therefore `[x^3,y^3]=1` for all `x,y`.

The same argument gives a prime-uniform conditional theorem: if additionally
`cl(G/P)<=p`, then `gamma_{p+1}(G)<=P`, every weight-`p+1` or
weight-`p+2` survivor has base in `P`, and `P` is abelian.

## What this does not establish

- For odd primes above three, it does not prove `gamma_{p+2}(G)^p=1` under the source hypotheses.
- It does not prove the assigned class-at-most-`p+2` theorem or the unrestricted
  source target uniformly over all odd primes; it proves the `p=3`, class-five subfamily only.
- It supplies no counterexample and makes no existence claim for a group with a
  nonzero surviving defect.
- It says nothing about `p=2`, exponent-eight groups, or the broader powerfulness
  question.

## Review dependency

The only imported mathematical result is the canonical Validator artifact
`Agents/Kourovka/problems/21.137/verification/2026-08-16T144312Z-class-p-plus-one-hall-lemma.md`,
including its extreme-coordinate sublemma. The new weight-`p+2` divisibility,
lift to `C^p`, central-root shift, and separate `p=3` audit require independent
Validator reconstruction. The `p=3` upgrade additionally uses the standard
2-Engel class-three lemma; its two-generator Engel reduction is written out,
but Validator should reconstruct the Hall--Witt step rather than accept the
named lemma on authority.
