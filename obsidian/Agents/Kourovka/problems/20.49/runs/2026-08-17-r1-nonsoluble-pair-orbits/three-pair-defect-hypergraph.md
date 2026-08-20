---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/exponent
  - project/kourovka
  - status/conjectured
problem: "20.49"
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
direction: counterexample
strategy: THREE-PAIR-DEFECT-HYPERGRAPH
---

# Three-pair prime-power defects

Let `G` be a least-order counterexample, let

```text
exp(G) = product over p in pi of p^(a_p),
```

and, for a pair `(u,v)`, define

```text
Delta(u,v) = {p in pi : v_p(exp(<u,v>)) < a_p}.
```

Every `Delta(u,v)` is nonempty. Equivalently, the sets

```text
F_p = {{u,v} : p in Delta(u,v)}
```

cover all pairs of elements of `G`.

## Exact global consequences

1. If `t_p` is a `p`-element of order `p^(a_p)`, no pair incident to `t_p` belongs to `F_p`, because its generated subgroup already contains the full `p`-part.
2. If `p != q` and `t_p,t_q` have maximal `p`- and `q`-power orders, then
   `Delta(t_p,t_q)` is nonempty and is contained in `pi minus {p,q}`.
3. Therefore `|pi| >= 3`. If the exponent had only the primes `p,q`, the pair `(t_p,t_q)` would generate a subgroup of full exponent.

## Exact three-prime localization

If `pi={p,q,r}`, choose pure prime-power elements `x,y,z` of orders
`p^a,q^b,r^c`, respectively. The subgroup `<x,y,z>` has exponent `exp(G)`, so
the proper-subgroup criticality of a least counterexample forces `<x,y,z>=G`.
Since `d(G)=3`, this is an irredundant generating triple. Its defect sets are
forced and distinct:

```text
Delta(x,y) = {r},
Delta(y,z) = {p},
Delta(z,x) = {q}.
```

Thus distinct localization is valid in the exact special case where the ambient
exponent has three prime divisors and the triple is chosen prime-pure. It is not
a consequence for an arbitrary full-exponent generating triple.

## Non-invariance under changing the triple

The local data of an irredundant three-generator triple with all three pair
subgroups exponent-deficient is not invariant under Nielsen moves.

Use additive notation in

```text
A = C2^3 x C3 x C5 x C7 x C11.
```

Let `e1,e2,e3` be the standard basis of `C2^3` and define

```text
x = (e1;  1 mod 3, 1 mod 5, 0 mod 7, 0 mod 11),
y = (e2; -1 mod 3, 0 mod 5, 1 mod 7, 0 mod 11),
z = (e3;  0 mod 3, 0 mod 5, 0 mod 7, 1 mod 11).
```

Both `T=(x,y,z)` and the Nielsen-equivalent `T'=(x+y,y,z)` are irredundant
generating triples (their `C2^3` projections are bases), and every pair in either
triple is exponent-deficient. Yet

```text
T:  Delta(x,y)={11}, Delta(x,z)={7}, Delta(y,z)={5};
T': Delta(x+y,y)={11}, Delta(x+y,z)={3}, Delta(y,z)={5}.
```

The moving edge changes its localized defect from 7 to 3 while staying nonempty.
This group is soluble and has other full-exponent pairs, so it is not an in-scope
counterexample. It is an exact obstruction to treating the three colors attached
to one chosen triple as canonical without a new argument using the global
counterexample property.

## Abelian chief-factor exponent/action constraint

Let `N` be an abelian minimal normal subgroup of a least counterexample. Then
`N` is elementary abelian of order a power of one prime `p`. Write `p^a` for the
`p`-part of `exp(G)` and `p^b` for the `p`-part of `exp(G/N)`.

- Quotienting by `N` preserves every maximal `q`-power order for `q != p`, since
  a `q`-element intersects the `p`-group `N` trivially.
- Proper-quotient criticality therefore forces the exponent drop at `p`.
- Since `N` has exponent `p`, an element whose image has order at most `p^b`
  has `p`-power order at most `p^(b+1)`. Hence `a <= b+1`.
- The strict drop gives `b<a`, so necessarily `b=a-1`.

Thus an abelian minimal normal layer raises exactly one prime-power exponent by
exactly one `p`-step:

```text
v_p(exp(G/N)) = v_p(exp(G)) - 1.
```

Every `p`-element `g` of maximal order `p^a` satisfies
`1 != g^(p^(a-1)) in N`.

If the extension splits, `G=N semidirect Q`, then some `p`-element `u in Q` of
order `p^(a-1)` and some `n in N` must have nonzero norm

```text
n + n^u + ... + n^(u^(p^(a-1)-1)).
```

Indeed this norm is `(nu)^(p^(a-1))`; it is nonzero exactly when the lift has
order `p^a`. In particular the relevant `p`-action has a nonzero fixed vector in
the image of this norm. This is an exact action constraint, though it does not
assign the layer canonically to an edge of an arbitrary generating triple.

## Outcome

The hypergraph viewpoint yields a real three-prime reduction and an exact abelian
chief-factor norm condition. It does not force three distinct edge defects for an
arbitrary full-exponent triple; the displayed Nielsen move is the obstruction.

