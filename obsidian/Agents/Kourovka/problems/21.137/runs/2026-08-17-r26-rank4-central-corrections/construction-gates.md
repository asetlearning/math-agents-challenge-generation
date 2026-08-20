---
title: "RANK4-NONSPLIT-H3 — conditional exact construction gates"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

# Control status

The unleased elimination is quarantined. In particular `(R0)` is only a
provisional row until the hash-pinned leased rerun validates it. This note is a
hand derivation of what each later machine gate would imply; it reports no
computed group or target witness.

# Exact active source scope

Odd `p>2`; finite same-`p` group; exponent exactly `p^2`; literal actual set
`{g^p:g in G}`, never generated subgroup; literal set itself a subgroup; ask
whether it is abelian; `p=2`/exponent-eight sibling excluded.

# Conditional crossed-product construction

The kernel coordinate law is

`(v,z)(w,u)=(v+w,z+u+2 omega(v,w)c)`

on `F3^4 x F3^3`. Alternation of `omega` gives inverse `(-v,-z)`, and a direct
four-factor calculation gives

`[(v,z),(w,u)]=(0,omega(v,w)c)`.

Thus its 2,187 coordinate tuples form exactly
`3_+^(1+4) x C3^2`: all elements have order three, the derived group is
`<c>`, and the center is `<c,s,t>`.

The quotient law

`(a,b,c)(d,e,f)=(a+d,b+e,c+f-bd)`

on `F3^3` has 27 distinct normal forms `x^a y^b z^c`, exponent three,
`[x,y]=z`, and central `z`; hence it is `H_3(3)`.

Suppose a leased run supplies a normalized factor
`f(q,r)=(v(q,r),u(q,r))` satisfying both

```
alpha_q alpha_r = Inn_(f(q,r)) alpha_(qr),
f(q,r) f(qr,s) = alpha_q(f(r,s)) f(q,rs).
```

Then on the literal Cartesian set `K x Q`, define

`(k,q)(l,r)=(k alpha_q(l) f(q,r),qr)`.

The second displayed identity is exactly the associativity calculation for
this multiplication; normalization gives the identity. Solving

`k alpha_q(l) f(q,q^-1)=1`

gives the explicit inverse used by the frozen checker. Therefore this is an
exact finite group, not merely a class-bounded quotient or an fp
presentation diagnostic.

The coordinate injection `k -> (k,1)` embeds all of `K`, because normalized
factors make its multiplication unchanged. Projection `(k,q)->q` is a
surjective homomorphism with exactly that kernel. Consequently the order is
`|K||Q|=3^7*3^3=3^10=59049`, and the ten coordinates are unique collected
polycyclic normal forms. Evaluating the six lift words in this group then
checks, rather than assumes, the proposed power-commutator presentation row.

# Exact target-facing gates

For `p=3`, the source exponent row is exactly exponent nine. Inspecting every
one of the 59,049 coordinate tuples and checking `g^9=1` proves the upper
bound; exhibiting one tuple with `g^3 != 1` proves the exponent is exactly
nine.

The checker forms

`S={g^3:g in G}`

by inserting the cube of every one of those 59,049 tuples into a set. This is
the literal image. It then constructs the subgroup `H=<S>` only as a
comparator and tests the exact set equality `S=H`. Because `S` is already
fully materialized, equality is equivalent to literal-set subgroup closure;
no generated-power substitution occurs.

If `S=H`, incremental subgroup generators are themselves members of `S`.
Pairwise commutation of those generators is equivalent to `H` being abelian;
one noncommuting generator pair is therefore an explicit pair of
noncommuting actual cubes. This last check is logically separate from both
exponent and closure.

# Constraint-and-conclusion gate prepared in advance

| constraint_id | role | required leased evidence before any claim |
|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | a single explicit `p=3` witness is sufficient to violate the universal assertion |
| `21.137-odd-p-not-2` | admissibility | frozen prime is `3` |
| `21.137-odd-finite-p-group` | admissibility | exact `K x Q` coordinate group of order `3^10` |
| `21.137-odd-exponent-p2` | admissibility | all 59,049 ninth powers trivial plus an order-nine witness |
| `21.137-odd-power-set-definition` | admissibility | set of all 59,049 literal cubes, deduplicated only after evaluation |
| `21.137-odd-power-set-subgroup` | admissibility | exact equality of that literal set with its subgroup closure |
| `21.137-odd-P-abelian` | target conclusion | explicit noncommuting pair from the literal cube set |

Unless every leased row passes, `active_assignment_answered: no` and the
object is not a counterexample.
