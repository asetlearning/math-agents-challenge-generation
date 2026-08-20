---
title: "Q81 noninner central carrier — exact action-word certificate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
strategy: Q81-NONINNER-CENTRAL-CARRIER
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - project/kourovka
  - status/conjectured
active_assignment_answered: no
---

# Exact scope

The active question is only the following odd-prime clause: for an odd prime
`p>2` and a finite same-`p` group `G` of exponent exactly `p^2`, if the literal
actual set `P={g^p:g in G}` (not merely the subgroup it generates) is itself a
subgroup, must `P` be abelian?  The `p=2`, exponent-eight sibling is excluded.

This certificate concerns only the single frozen `p=3` proposed carrier

```text
K = 3_+^(1+4) x C3^2,
Q81 = <x,y,z,w | x^3=y^3=z^3=w^3=1,
                     [x,y]=z, z and w central>.
```

It is an action-gate failure, not a group, projected-support pass, factor
system, or counterexample to the active question.

# Coordinate and composition conventions

Work over `F3`.  Put

```text
V = <e1,e2,f1,f2>,       Z(K) = <c,s,t>,
omega(e_i,f_j)=delta_ij, omega(f_j,e_i)=-delta_ij.
```

One concrete model of `K` is `V x Z(K)` with multiplication

```text
(v,z)(v',z')=(v+v', z+z'+(1/2)omega(v,v')c).
```

Thus `[K,K]=<c>`.  An automorphism triple acts by

```text
(M,T,L):(v,z) |-> (Mv,Tz+Lv).
```

Automorphisms are composed as functions, with the rightmost map applied first.
Equivalently, their block matrices and products are

```text
A(M,T,L) = [ M  0 ] ,
             [ L  T ]

(M1,T1,L1)(M2,T2,L2)
  = (M1 M2, T1 T2, L1 M2 + T1 L2),

(M,T,L)^(-1)
  = (M^(-1),T^(-1),-T^(-1)L M^(-1)).
```

Use the group commutator `[A,B]=A^(-1)B^(-1)AB`.  Changing to the other
standard commutator notation replaces the derived commutator by an
inverse/conjugate and cannot turn a noncentral outer element into a central
one.

Because `[K,K]=<c>` and `omega` is nondegenerate, the inner automorphisms of
`K` are exactly the triples `(I,I,rho)` with `rho:V-><c>` linear.  Therefore a
pure shear with a nonzero `s` or `t` component is non-inner.  This is the only
inner/outer test used below.

# Frozen input

Set

```text
a(v)=omega(e1,v),       b(v)=omega(f1,v),
M_X=tau_e1,             M_Y=tau_e2,
tau_u(v)=v+omega(v,u)u,

T(c)=c,                 T(s)=s+c,        T(t)=t+s,

A=alpha_X=(M_X,T,a t),
B=alpha_Y=(M_Y,T,b t),
W=alpha_W=(I,I,a s),
C=alpha_Z=[A,B].
```

The useful identities, all obtained directly from the displayed basis, are

```text
a M_X=a,  a M_Y=a,  b M_Y=b,  b M_X=b+a,
T^3=I,
T^(-1)(s)=s-c,
T^(-1)(t)=t-s+c,
(I+T+T^2)(t)=c.
```

The symplectic transvections `M_X,M_Y` commute because
`omega(e1,e2)=0`.

# Cube words and labels

For a triple `(M,T,L)` whose `M` and `T` have order three,

```text
(M,T,L)^3=(I,I,T^2 L+T L M+L M^2).
```

Here the relevant functionals are invariant under their corresponding `M`, so

```text
A^3=(I,I,a c),
B^3=(I,I,b c),
W^3=I.
```

Thus the `x^3` and `y^3` words are inner, with nonzero inner labels represented
by `e1` and `f1` up to a common harmless sign.  Their symplectic pairing is
`omega(e1,f1)=1`, so the prescribed nonzero/nonorthogonal cube-label gate
passes.  The outer orders of `A` and `B` are exactly three because their
transvection parts are nontrivial.  The non-inner shear `W` also has outer
order three.

# Derived z-action

Direct substitution in the product and inverse laws gives

```text
L_C = T^(-1)(L_B-L_A)+T^(-2)(L_A M_Y-L_B M_X).
```

Using `L_A=a t`, `L_B=b t`, and `T^(-2)=T`, this is

```text
C=(I,I,L_C),
L_C(v) = (b-a)c + (a+b)s - a t.                 (1)
```

Consequently `C^3=I`, and `[A,B]C^(-1)=I` holds exactly by the definition of
`C`.  The `z` outer class is nontrivial and has order three.

# Fatal centrality word

For any pure shear `N(L)=(I,I,L)`, the same multiplication law yields

```text
[A,N(L)] = (I,I,L-T^(-1)L M_X).
```

Applying this to (1) gives the exact word

```text
[A,C] = (I,I, a s + (b-a)c).                    (2)
```

In particular, on `v=f1` one has `a(f1)=1`, `b(f1)=0`, and hence

```text
[A,C](f1,0)=(f1,s-c).
```

The nonzero `s` component makes (2) non-inner.  Thus

```text
[bar(alpha_X),bar(alpha_Z)] != 1 in Out(K),
```

contrary to the defining `Q81` relation that `z` is central.

For completeness, the remaining central-carrier words obtained from the same
formula are

```text
[B,C]=(I,I,-a s+(b-a)c),
[A,W]=(I,I,a c),
[B,W]=(I,I,a c),
[C,W]=I.
```

The second `z`-centrality word is also non-inner, while all three commutators
with `W` are inner (indeed the last is trivial).  The first failed required
word is already (2).

# Consequence and hard stop

An extension of `K` by `Q81` necessarily induces a homomorphism
`Q81 -> Out(K)`.  The frozen images above do not define such a homomorphism,
because the image of the central generator `z=[x,y]` fails to commute with the
image of `x` (and also with that of `y`).  Multiplying a lift by an inner
automorphism or choosing a central factor system cannot repair a relation that
already fails in `Out(K)`.

Therefore the authorized candidate is killed at the action gate.  In
particular:

- no 81-coset projected-support union was formed;
- no factor equations were opened;
- no crossed product or group was constructed;
- no literal cube set was computed;
- no script, solver, enumeration, or heavy command was run, so no Lead compute
  lease was required.

This exhausts only `Q81-NONINNER-CENTRAL-CARRIER` with the single frozen datum.
It does not answer or park `21.137/odd-prime-exponent-p2`.
