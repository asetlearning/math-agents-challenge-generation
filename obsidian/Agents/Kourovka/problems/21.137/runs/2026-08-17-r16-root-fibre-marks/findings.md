---
title: "Kourovka 21.137 — complete feasible root-fibre mark vector"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: ROOT-FIBRE-MARKS
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/burnside-marks
  - project/kourovka
  - status/conjectured
---

# ROOT-FIBRE-MARKS failure certificate

## Active target

Scope: `21.137/odd-prime-exponent-p2`  
Assignment revision: `2`

For every odd prime `p` and finite `p`-group `G` of exponent exactly `p^2`, if
the complete actual value set `P={x^p:x in G}` is a subgroup, prove that `P` is
abelian.

This note does **not** answer that target. It gives the requested method kill: a
prime-uniform nonnegative integral formal mark vector satisfying every frozen
fixed-point, restriction, orbit, Burnside/Möbius, elementary power-count, and
surjectivity row while its label group is nonabelian.

## 1. Complete frozen mark rows

For an actual power map put

```
X_a = {x in G : x^p=a},
K_a = C_G(a),
m_H(a) = |X_a intersect C_G(H)| = |X_a^H|.
```

It is enough to index `H` over every subgroup, not just conjugacy-class
representatives; the conjugacy row then records all redundancy.

### F1. Support and root centrality

Every root commutes with its power. Hence

```
m_H(a)=0                         if H is not <= K_a,
m_H(a)=m_<H,a>(a)                if H <= K_a.
```

### F2. Conjugacy

For all `g in G`,

```
m_{H^g}(a^g)=m_H(a).
```

### F3. Centralizer partition and surjectivity

Restriction of the map to `C_G(H)` partitions that centralizer, so

```
sum_{a in C_P(H)} m_H(a)=|C_G(H)|.
```

The complete actual-value hypothesis is exactly

```
m_1(a)>0 for every a in P.
```

### F4. Burnside marks

For each `a`, `X_a` is a finite `K_a`-set. If `n_{a,L}` is the number of
transitive summands isomorphic to `K_a/L`, then, for every `H <= K_a`,

```
m_H(a) = sum_[L] n_{a,L} |(K_a/L)^H|,
n_{a,L} in Z_{>=0}.
```

Equivalently, if

```
e_{a,H}=sum_{J>=H} mu(H,J)m_J(a)
```

counts points with exact stabilizer `H`, then

```
e_{a,H} >= 0,
e_{a,H} = 0 mod |N_{K_a}(H):H|.
```

For a full `G`-orbit of labels, the same formula is applied to the induced
`G`-set.

### F5. Elementary rows retaining the power origin

Because `P` is a subgroup consisting entirely of `p`-th powers and `G` has
exponent `p^2`, `P` has exponent `p` and `P <= X_1`. Consequently

```
m_H(1) >= |C_P(H)|.
```

For `a!=1`, the free operation `x -> x a` on actual roots gives

```
m_H(a) = 0 mod p.
```

For every integer `r` prime to `p`, the bijection `x -> x^r` gives

```
m_H(a)=m_H(a^r).
```

The construction below satisfies these additional numerical rows as well.

## 2. A prime-uniform nonabelian label group

Fix any odd prime `p`. Let

```
P = H_p = {(u,v,w):u,v,w in F_p}
```

with multiplication

```
(u,v,w)(u',v',w')=(u+u', v+v', w+w'+u v').
```

Then `P` has exponent `p`, is nonabelian, and

```
P'=Z(P)=C={<c^j>:j in F_p},   |C|=p,
```

where `c=(0,0,1)`. Thus the label group has exactly the class-two,
central-order-`p` commutator shape retained by the minimum-counterexample
reduction.

Let `T=<t>` be cyclic of order `p^2`, form the central product identifying
`t^p` with `c`, and adjoin a central elementary abelian group `B=C_p^s`, where
`s>=1`:

```
Gamma = ((T x P)/<(t^p,c^-1)>) x B.
```

The embedded copy of `P` is normal, `Gamma` is a finite `p`-group of exact
exponent `p^2`, and `Gamma/P` is elementary abelian. Every element has a unique
normal form

```
x=t^i b u,   0<=i<p, b in B, u in P.
```

Conjugation depends only on the `P`-coordinate `u`.

## 3. The formal equivariant map

Define `f:Gamma -> P` by

```
f(t^i b u) = 1       if i=0,
               u       if i!=0 and u!=1,
               c^i     if i!=0 and u=1.
```

This is a well-defined surjection. It is conjugation-equivariant: conjugation
changes only `u` to `u^v`, preserves whether `u=1`, and fixes `c`. It also has
the root-centrality shadow

```
[x,f(x)]=1
```

for every `x`.

Moreover, in `Gamma`,

```
(t^i b u)^p=c^i.
```

Thus `f^-1(1)` is exactly the true set of elements with `p`-th power `1`, and it
contains the embedded `P`. The map is deliberately **not** the power map on the
mixed elements with `i!=0` and `u!=1`; this is the precise information forgotten
by the mark relaxation.

## 4. Closed formula for every mark

For an arbitrary subgroup `H <= Gamma`, write

```
Q_H=C_P(H),   q_H=|Q_H|.
```

Here conjugation by `H` is understood through its `P`-coordinate. The complete
mark vector of `f` is

```
(M1)  m_H(1) = p^s q_H.

(M2)  m_H(a) = p^(s+1)
      for every 1!=a in Z(P).

(M3)  m_H(a) = (p-1)p^s
      for a notin Z(P) with a in Q_H.

(M4)  m_H(a) = 0
      for a notin Q_H.
```

Indeed:

- the identity fibre has `i=0`, arbitrary `b`, and `u in Q_H`;
- for central `a=c^r!=1`, the points with `i!=0,u=a` contribute
  `(p-1)p^s`, and the points with `i=r,u=1` contribute another `p^s`;
- a noncentral label `a` has precisely the points with `i!=0,u=a`, and
  these are fixed by `H` exactly when `a in Q_H`.

These formulas cover every subgroup `H`, so there is no unfilled mark row.

## 5. Row-by-row feasibility

### Support, conjugacy, and centralizer restriction

For a noncentral label, `(M3)-(M4)` is nonzero exactly when `H<=C_Gamma(a)`.
Central labels are fixed by every subgroup. Conjugation preserves `q_H`,
centrality, and the membership condition `a in Q_H`. Also, whenever
`H<=C_Gamma(a)`, adjoining `a` does not alter whether a listed point is fixed,
so `m_H(a)=m_<H,a>(a)`.

### Partition

Since `Z(P)` has `p` elements and `Q_H` contains `Z(P)`, summing over the fixed
labels gives

```
sum_{a in Q_H} m_H(a)
 = p^s q_H +(p-1)p^(s+1)+(q_H-p)(p-1)p^s
 = p^(s+1)q_H
 = |C_Gamma(H)|.
```

### Burnside and Möbius rows

No abstract integrality assertion is needed; the fibres have explicit orbit
decompositions.

- `X_1` is `p^s` copies of the conjugation `Gamma`-set `P`.
- If `1!=a in Z(P)`, `X_a` consists of `p^(s+1)` central points, hence that many
  trivial `Gamma`-orbits.
- If `a` is noncentral, `X_a` consists of `(p-1)p^s` points fixed by
  `K_a=C_Gamma(a)`. The union over the conjugacy class `aC` is
  `(p-1)p^s` copies of `Gamma/K_a`.

For completeness, the only exact stabilizers in `X_1` are `Gamma` and the
`p+1` index-`p` subgroups lifted from the maximal abelian centralizers in `H_p`.
Their exact-point counts are respectively

```
p^(s+1),
p^s(p^2-p)=p^(s+1)(p-1).
```

Each index-`p` centralizer is normal, and its exact-point count is divisible by
the required normalizer quotient `p`. All other Möbius exact-stabilizer counts
are zero. The central nonidentity fibres have exact stabilizer `Gamma`; each
noncentral conjugacy-class union has exact stabilizer `K_a` and total exact count
`p(p-1)p^s`, divisible by `|N_Gamma(K_a):K_a|=p`.

### Surjectivity and elementary power congruences

At `H=1`, all four displayed positive values occur, so every label has a formal
root. The identity count contains all of `P`. For every nonidentity label the
count is divisible by `p` because `s>=1`. Counts are constant on `a -> a^r` for
`(r,p)=1`: all nontrivial central labels have the same count, as do all
noncentral labels.

Thus every frozen integral row is satisfied for every odd prime.

## 6. Exact method failure

The nonabelian multiplication of `P` affects its centralizer lattice and label
orbits, and the vector above already respects both. What the vector does not
record is the cross-fibre equation tying a particular mixed element to its actual
power. In the formal model,

```
f(t^i b u)=u,          but          (t^i b u)^p=c^i
```

when `i!=0` and `u!=1`. Fixed-point marks, restriction, and Burnside congruences
cannot distinguish those two labels once the fibres have the same permitted
stabilizer data.

Therefore `ROOT-FIBRE-MARKS`, with precisely the rows assigned, cannot yield an
integral contradiction from `P'!=1`. A future proof would have to add a genuinely
multiplicative root-action/carry relation (for example the individual relation
`conj(x)^p=Inn(x^p)`) that is not a mark of the conjugation `G`-set.

## Constraint-and-conclusion matrix

This is a method certificate, not a candidate for the active scope.

| constraint_id | role | treatment | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | construction and formulas are uniform for all odd `p` | method row only |
| `21.137-odd-p-not-2` | admissibility | assumes odd `p` | pass for formal test |
| `21.137-odd-finite-p-group` | admissibility | `Gamma` is a finite same-`p` group | pass for ambient test |
| `21.137-odd-exponent-p2` | admissibility | `t` has order `p^2`; all elements have order dividing `p^2` | pass for ambient test |
| `21.137-odd-power-set-definition` | admissibility | `f` is not the actual power map on mixed elements | **fail** |
| `21.137-odd-power-set-subgroup` | admissibility | formal image is subgroup `P`, but not the actual value set | **fail for target** |
| `21.137-odd-P-abelian` | target conclusion | formal label group `P=H_p` is nonabelian | shows only coarseness |

`active_assignment_answered: no`.

## Outcome

`STRATEGY_EXHAUSTED` for `ROOT-FIBRE-MARKS` only. The explicit feasible integral
relaxation meets the Lead-specified early kill. The unrestricted odd-prime target
remains open, and the solver awaits Lead rather than self-parking.

