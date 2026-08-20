---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/conjectured
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: MCO-CENTRAL-COMMUTATOR
outcome: PARTIAL_RESULT
---

# Partial result: minimal central extension and root-fibre norm

## Active target

Scope: `21.137/odd-prime-exponent-p2`

Assignment revision: `2`

Target statement: Let `p` be an odd prime and `G` a finite `p`-group of exponent exactly `p^2`. If the set `P={g^p:g in G}` of actual `p`th powers is a subgroup of `G`, then `P` is abelian.

## Outcome

`PARTIAL_RESULT`, pending independent review. The minimum-counterexample reduction in the Lead decision passes all three hard gates. It reduces a hypothetical counterexample to a central extension with an exact cocycle/root-fibre obstruction, but does not close the target.

## Candidate reduction

If a counterexample exists, choose one of minimum order. Then:

1. `P` is characteristic, has exponent `p`, and is nonabelian.
2. There is `N<=P' intersect Z(G)` with `|N|=p`.
3. The actual `p`th-power set of `G/N` is exactly `P/N`, not merely its generated subgroup.
4. `exp(G/N)=p^2`: otherwise `P<=N`, whence `P=N` is abelian.
5. Minimality makes `P/N` abelian, so `P'=N<=Z(G)`.
6. Every nontrivial normal subgroup of `G` contains `N`. Thus `N` is the unique minimal normal subgroup of `G`.
7. The center is cyclic, necessarily of order `p` or `p^2`; in the latter case its generator is a central `p`th root of `N`.

The full line-by-line argument is in `Agents/Kourovka/problems/21.137/runs/2026-08-16-r6-minimal-central-obstruction/log.md`.

## Exact root-fibre/cocycle formulation

Let `Q=G/N`, `A=P/N`, and choose a normalized section `s:Q->G` with factor set

`f(u,v)=s(u)s(v)s(uv)^{-1} in N`.

Then

`f(u,v)f(uv,w)=f(v,w)f(u,vw)`.

For `R_a={u in Q:u^p=a}` define

`lambda_a(u)=s(u)^p s(a)^{-1}=product_{i=1}^{p-1} f(u^i,u)`.

Actual-value-set closure is equivalent to `lambda_a(R_a)=N` for every `a in A`. This condition is invariant under changing the section. Meanwhile

`beta(a,b)=f(a,b)f(b,a)^{-1}`

is the section-independent commutator pairing of `P`; `P` is abelian exactly when `beta` is identically `1`. In a hypothetical minimum counterexample, `beta` is nontrivial with image `N`.

The precise obstruction is that the onto `lambda_a` conditions inspect cyclic restrictions of `f`, while `beta` is its alternating rank-two restriction. Closure provides existence, but no canonical composition of selected roots in `R_a` and `R_b` into a selected root in `R_{ab}`. Thus the cyclic norms cannot presently be polarized into an identity forcing `beta=1`.

The cyclic-center dichotomy makes the obstruction concrete. If `|Z(G)|=p^2`, write `Z(G)=<z>` with `z^p` generating `N`; then `(gz^k)^p=g^p(z^p)^k`, so one root over a quotient value automatically yields every central lift. Root-fibre surjectivity is therefore automatic in that branch and is blind to `beta`. The remaining branch has `Z(G)=N` and no central root of `N`; it was not resolved here.

There is also a canonical stabilizer test. For `a in A`, a lift `t in P`, and the inverse image `S_a` of the stabilizer of `a` in `Q`, the map `chi_a(g)=t^{-1}t^g` is a well-defined homomorphism `S_a->N`. Its restriction to `P` is the commutator row `beta(a,-)` up to orientation. If `a` is outside `rad(beta)`, conjugates of one power value already fill all of `P_a`; hence closure adds no constraint precisely in every direction on which `beta` is detected. This explains why the observable does not force `[P,P]=1`.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | use in the reduction | evidence | result |
|---|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every admissible `p,G` | argue from an arbitrary counterexample and choose minimum order | run log, minimal-central-obstruction audit | used |
| `21.137-odd-p-not-2` | admissibility | `p` odd | retained throughout; oddness is also relevant to the separation between cyclic power data and alternating commutator data | source gate and cocycle section of run log | used |
| `21.137-odd-finite-p-group` | admissibility | finite `p`-group | supplies a minimum-order counterexample and `P' intersect Z(G) != 1` | run log, minimal-central-obstruction audit | used |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | gives `exp(P)<=p` and proves quotient exponent remains exact | run log, gates 2 and preliminary paragraph | used |
| `21.137-odd-power-set-definition` | admissibility | actual values, not their span | gives `exp(P)<=p`, exact quotient value set, and onto root-fibre maps | run log, gates 1 and root-fibre observable | used |
| `21.137-odd-power-set-subgroup` | admissibility | actual value set is a subgroup | gives characteristic subgroup `P`, quotient closure, and multiplication of values | run log, gates 1 and root-fibre observable | used |
| `21.137-odd-P-abelian` | target_conclusion | `P` abelian | equivalent after reduction to `beta=1`; no argument forcing this has been obtained | cocycle skew criterion and obstruction | unresolved |

## What this does not establish

It does not prove `P` abelian, construct a counterexample, or show that the root-fibre surjectivity conditions are inconsistent with nonzero `beta`. It does not address the general powerfulness clause, any `p=2` group, or the exponent-8 clause.

## How this could be wrong

- The quotient exponent argument could conceal an exponent-divisibility case; the check is that a quotient of an exponent-`p^2` `p`-group has exponent only `1`, `p`, or `p^2`, and either lower case forces `P<=N`.
- The equality of the quotient's actual value set with `P/N` could be confused with equality of generated subgroups; the displayed elementwise equality in the log is meant to prevent that error.
- The cyclic-norm formula or its section-change law could have an ordering error; centrality of `N` is essential at both points and should be reconstructed independently.
- Fibrewise surjectivity is equivalent to closure only after fixing `A=P/N` as the quotient's actual power set and `P=pi^{-1}(A)`; both equalities must be retained.
