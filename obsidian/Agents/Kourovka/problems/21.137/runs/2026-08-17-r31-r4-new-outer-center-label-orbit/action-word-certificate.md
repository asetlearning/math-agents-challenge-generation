---
title: "R4 common-root tuple — exact action and 27-coset support certificate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: R4-NEW-OUTER-CENTER-LABEL-ORBIT
active_assignment_answered: no
evidence_status: hand_derivation_reproduced_by_leased_checker
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, topic/power-maps, project/kourovka, status/conjectured]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/manifest.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/checker-output.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r31-r4-new-outer-center-label-orbit/leased-output.md
---

# Exact target boundary

The source target concerns an odd prime `p>2`, a finite same-`p` group of exact
exponent `p^2`, and the literal actual set `{g^p:g in G}` being a subgroup;
it asks whether that subgroup must be abelian.  This certificate specializes
to `p=3`.  It is a pre-extension failure certificate, not an exponent-nine
group or a source-scope answer.  The `p=2`, exponent-eight sibling is excluded.

# Exact action words

Use the frozen coordinates and tuple in `manifest.md`.  Write

```text
a(v)=omega(e2,v),       b(v)=omega(f2,v),
X=(M,T,a t),            Y=(M,T^-1,b t),
Z=[X,Y].
```

Here `aM=a`, `bM=b`, and

```text
(I+T+T^2)t=(I+T^-1+T^-2)t=c.
```

The two cube words are therefore

```text
X^3=J_e2,               Y^3=J_f2,
omega(e2,f2)=1.
```

Thus the prescribed labels are nonzero and nonorthogonal.  Direct use of the
triple product and `[X,Y]=X^-1Y^-1XY` gives

```text
Z=(I,I,LZ),             LZ=(a+b)s-a c
  = 0002/0201/0000,
Z^3=1,
[X,Y]Z^-1=1,
[X,Z]=J_(e2+f2),
[Y,Z]=J_(-e2-f2).
```

Every defining word of
`H_3(3)=<x,y,z | x^3=y^3=z^3=1,[x,y]=z,[x,z]=[y,z]=1>`
is therefore inner (and the commutator-definition word is exact).  The frozen
tuple passes the complete action gate in `Out(K)`.

# Displayed invariant separating the exhausted transverse orbit

Let `M_z=[M_x,M_y]` be the symplectic matrix of the central quotient word.
Inner lift changes and center shears do not change `M_z`; simultaneous kernel
conjugacy conjugates it, so `rank(M_z-I)` is invariant.  A quotient
automorphism sends `z` to `z` or `z^-1`, which also preserves this rank.

```text
                         M_z                              rank(M_z-I)
new common-root tuple    I                                0
exhausted transverse     1020/0100/0010/0001=tau_e1      1
```

Hence this tuple is not in the exhausted transverse action/shear orbit.

# Factor-independent projected literal-cube supports

For the fixed word representative
`h(a,b,d)=X^a Y^b Z^d`, `0<=a,b,d<3`, write
`h^3=J_lambda`.  If a kernel element in that quotient coset has image `v` in
`V=K/Z(K)`, its actual cube projects to

`lambda+(I+M_h+M_h^2)v`.

This is the full coset support, not a generated-power subgroup.  Central
factor coordinates disappear in `V`, so it is factor-independent.  Here
`M_h=M^(a+b)` and
`I+M_h+M_h^2=0` for all `a,b`; consequently every support is the singleton
`F_h={lambda_h}`.

There is also a short hand derivation of every table entry.  Because both
functionals `a=omega(e2,-)` and `b=omega(f2,-)` are fixed by `M`, represent a
shear as a pair of center vectors multiplying `a,b`.  Composition then sends
the second pair through the current power of `T`.  In
`h=X^aY^bZ^d`, the `t`-coefficients of those two vectors are exactly `a,b`;
the derived `Z` shear has no `t`-component, so `d` does not enter.  If `a=b`,
the center action of `h` is trivial and its three-term norm is zero.  If
`a!=b`, that action is `T` or `T^-1`, whose three-term norm kills `c,s` and
sends `t` to `c`.  Hence the closed formula is

```text
lambda(a,b,d)=0                 if a=b,
lambda(a,b,d)=a e2+b f2         if a!=b.
```

| `h=(a,b,d)` | `lambda_h` | `W_h` | `F_h` |
|---|---|---|---|
| `000` | `0000` | `0` | `{0000}` |
| `001` | `0000` | `0` | `{0000}` |
| `002` | `0000` | `0` | `{0000}` |
| `010` | `0001` | `0` | `{0001}` |
| `011` | `0001` | `0` | `{0001}` |
| `012` | `0001` | `0` | `{0001}` |
| `020` | `0002` | `0` | `{0002}` |
| `021` | `0002` | `0` | `{0002}` |
| `022` | `0002` | `0` | `{0002}` |
| `100` | `0100` | `0` | `{0100}` |
| `101` | `0100` | `0` | `{0100}` |
| `102` | `0100` | `0` | `{0100}` |
| `110` | `0000` | `0` | `{0000}` |
| `111` | `0000` | `0` | `{0000}` |
| `112` | `0000` | `0` | `{0000}` |
| `120` | `0102` | `0` | `{0102}` |
| `121` | `0102` | `0` | `{0102}` |
| `122` | `0102` | `0` | `{0102}` |
| `200` | `0200` | `0` | `{0200}` |
| `201` | `0200` | `0` | `{0200}` |
| `202` | `0200` | `0` | `{0200}` |
| `210` | `0201` | `0` | `{0201}` |
| `211` | `0201` | `0` | `{0201}` |
| `212` | `0201` | `0` | `{0201}` |
| `220` | `0000` | `0` | `{0000}` |
| `221` | `0000` | `0` | `{0000}` |
| `222` | `0000` | `0` | `{0000}` |

Their exact union is

```text
Sigma={0000,0001,0002,0100,0102,0200,0201}
     ={0, +/-f2, +/-e2, +/-(e2-f2)}.
```

It has size seven and spans `<e2,f2>`, on which `omega` has rank two, but the
union itself is not a subspace.  The required explicit additive outsider is

```text
f2=0001 in Sigma,       e2=0100 in Sigma,
e2+f2=0101 not in Sigma.
```

If the literal cube set in a realizing extension were a subgroup, its image
in elementary abelian `V` would be an `F3`-subspace.  This hand-derived exact
outsider is therefore a factor-independent obstruction that no central factor
row can repair.

# Hard stop and limitation

The hand derivation meets the authorized kill criterion at the
projected-support gate, and the exact once-only leased checker reproduces every
action word, all 27 rows, the orbit invariant, and the additive outsider.  No
factor system, cohomology, finite group, group enumeration, exponent test, or
generated-power closure was opened.  This concerns only the one canonical
action representative frozen in `manifest.md`; it does not answer the
unrestricted odd-prime scope.
`active_assignment_answered: no`.
