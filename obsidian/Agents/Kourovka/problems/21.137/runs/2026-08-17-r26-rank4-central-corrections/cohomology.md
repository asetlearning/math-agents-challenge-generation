---
title: "RANK4-NONSPLIT-H3 — complete central-correction system"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
outcome: CHECKPOINT
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-cohomology, project/kourovka, status/conjectured]
---

# Exact active source scope

Odd `p>2`; finite same-`p` group; exponent exactly `p^2`; literal actual set `P={g^p:g in G}`, never its generated subgroup; the literal set itself is a subgroup; ask whether it is abelian. The separate `p=2`, exponent-eight sibling is excluded.

# Result of the pre-enumeration gate

> **CONTROL QUARANTINE (2026-08-17T21:16:56Z).** The 2,028-variable,
> 59,049-equation elimination is a solver/enumeration job under common compute
> rules even though its wall time was 58.01 seconds. It ran without a prior
> lease. Therefore every numerical rank, dimension, feasibility, affine-image,
> and gauge-equivalence conclusion below is provisional and is not evidence.
> The independently written formulas and checker remain candidate mathematics
> only. Promotion requires the one hash-pinned leased rerun in
> `scratch/full_group_manifest.md` and later independent review.

Provisionally, the frozen `p=3`, `K=3_+^(1+4) x C3^2`, quotient-`H_3(3)` automorphism lift reconstructs and its complete central factor obstruction appears soluble. The quarantined elimination suggests an affine system of dimension eight on the 18 central relator coordinates. No one of the `3^18` central rows was enumerated. None of these computed conclusions is presently evidence.

This is not yet a group/witness claim. A simple feasible presentation row is exposed, but exact coordinate construction and every target-facing cube gate remain to be run under a new frozen heavy-compute lease.

## Conventions and independent lift reconstruction

Use BCH coordinates on

`K=V x Z`, `V=<e1,e2,f1,f2>`, `Z=<c,s,t>`,

with

`(v,z)(w,u)=(v+w,z+u+2 omega(v,w)c)` over `F3`.

Then `[v,w]=omega(v,w)c` for `[a,b]=a^-1 b^-1 a b`. A frozen triple acts by

`alpha(v,z)=(M v,T z+L v)`

and triples compose as

`(M,T,L)(M',T',L')=(MM',TT',T L'+L M')`.

The independent checker re-enters the displayed `A,B,C`, `TX,TY,TZ`, and `LX,LY,LZ`, and checks all matrix relations directly. It obtains the six inner labels, in the relator order

`X^3,Y^3,Z^3,[X,Y]Z^-1,[X,Z],[Y,Z]`,

as

```
(0,0,0,1), (0,1,0,0), 0,
(2,0,2,1), (0,2,0,2), (0,1,0,1).
```

Thus `qX=f2`, `qY=e2`, and `omega(qX,qY)=2 != 0`, exactly as prescribed. The old factor diagnostic is not used.

## Complete factor equation

Write quotient elements canonically as `q=(a,b,c)=x^a y^b z^c`; then

`(a,b,c)(d,e,f)=(a+d,b+e,c+f-bd)`.

Let `alpha_q=alphaX^a alphaY^b alphaZ^c`. Every one of the 729 defects

`alpha_q alpha_r alpha_(qr)^-1`

is checked to be inner. Let its unique noncentral label be `v(q,r) in V`, and write a possible factor as

`f(q,r)=(v(q,r),u(q,r))`, `u(q,r) in Z`,

normalized by `u(1,r)=u(q,1)=0`. Associativity is equivalent, component by component in `Z`, to

```
u(q,r)+u(qr,s)-T_q u(r,s)-u(q,rs)
 = L_q v(r,s)
   + 2 omega(M_q v(r,s),v(q,rs)) c
   - 2 omega(v(q,r),v(qr,s)) c.                 (E)
```

This is the complete nonabelian-factor obstruction because its `V` part is already forced by and checked against the inner-action defects. There are 2,028 normalized scalar `u` variables and 59,049 scalar instances of `(E)`. Exact streaming elimination over `F3` gives

```
rank = 1951,
augmented rank = 1951,
solution affine dimension = 77.
```

The `V` part was not inferred from innerness alone. The checker separately
recomputes all 729 pair defects and then checks, for every
`(q,r,s) in Q^3`,

`v(q,r)+v(qr,s)=M_q v(r,s)+v(q,rs)`.

All 19,683 vector identities, equivalently 78,732 scalar `F3` identities,
vanish exactly. Thus this strictly contains the requested 729-coordinate
certification.

## Complete eliminated system on the 18 relator coordinates

Write each central correction in `(c,s,t)` order and flatten

```
r=(r0,...,r17)
 =(x3_c,x3_s,x3_t,
   y3_c,y3_s,y3_t,
   z3_c,z3_s,z3_t,
   xy_c,xy_s,xy_t,
   xz_c,xz_s,xz_t,
   yz_c,yz_s,yz_t).
```

Here `xy` denotes `[X,Y]Z^-1`. Eliminating the normalized `u(q,r)` from `(E)` and the six exact relator evaluations gives exactly the following ten independent affine equations:

```
r1 = 0
r2 = 0
r4 = 0
r5 = 0
r6 + 2 r11 + 2 r13 = 0
r7 = 0
r8 = 0
r11 + 2 r13 + 2 r16 = 0
r14 = 2
r17 = 2.                                      (R)
```

The image therefore has affine dimension `18-10=8`. In particular the zero-central row is impossible for an exact, section-independent reason: every feasible row has

`xz_t=yz_t=2`.

A simplest feasible row sets every other coordinate to zero:

```
r14=r17=2; all other ri=0.                     (R0)
```

In ordered kernel words, `(R0)` is

```
X^3 = f2,
Y^3 = e2,
Z^3 = 1,
[X,Y] Z^-1 = e1^2 f1^2 f2 c,
[X,Z] = e2^2 f2^2 c t^2,
[Y,Z] = e2 f2 c t^2.
```

The `c` factors already present in the last three displayed representatives are precisely the ordered-word conversion of BCH central coordinate zero; only the two displayed `t^2` factors are new.

## Exact section gauge

For an arbitrary normalized central section change `s'(q)=h(q)s(q)`, the factor coordinates transform by

`u'(q,r)=u(q,r)+h(q)+T_q h(r)-h(qr)`.

On the 18 relator coordinates it suffices to record the generator values

`a=h(x)`, `b=h(y)`, `d=h(z)` in `(c,s,t)` order. The gauge increment is `G(a,b,d)`, where the rows of `G` are in the above order and its columns are

`(a_c,a_s,a_t,b_c,b_s,b_t,d_c,d_s,d_t)`:

```
002000000
000000000
000000000
000001000
000000000
000000000
000000000
000000000
000000000
020020200
002001020
000000002
002000021
000000001
000000000
000002012
000000001
000000000
```

This matrix has rank five. Direct substitution shows that every column preserves `(R)`, including the forced constants `r14=r17=2`. Thus the feasible eight-dimensional affine family has a three-dimensional quotient by central generator-lift gauge.

### Completeness modulo normalized section gauge

The equivalence between the full cochain system and the assigned 18
coordinates is dimension-certified, not assumed from the presentation. The
normalized central 1-cochain space has dimension `3*(27-1)=78`. Exact
elimination of

`(delta h)(q,r)=h(q)+T_q h(r)-h(qr)`

gives coboundary rank 74 and 1-cocycle dimension four. The homogeneous
solution space of `(E)` has dimension 77, so its quotient by all normalized
section gauges has dimension `77-74=3`.

On relator coordinates, `(R)` has dimension eight and the displayed
generator-gauge matrix has rank five, so its quotient also has dimension
`8-5=3`. More sharply, the kernel of the full-cochain-to-exact-relator map has
dimension `77-8=69`. Central section changes whose induced relator increment
is zero have dimension

`(78-5)-4=69`,

and lie in that kernel by the displayed section formula. Equality of
dimensions proves equality of these two kernels. Consequently:

- every row satisfying `(R)` is realized by a full normalized factor system;
- two full factor systems give the same exact 18-coordinate row precisely up
  to a normalized central section change with zero relator increment;
- after allowing generator-lift gauge, the induced map from the full cochain
  quotient to `(R)/G` is a bijection of three-dimensional affine spaces.

This is the required equivalence modulo normalized section gauge.

## Reproduction and limits

Exact command actually run:

```text
$ /usr/bin/time -f 'elapsed=%e sec maxrss=%M KB' timeout 60s python3 -u Agents/Kourovka/problems/21.137/runs/2026-08-17-r26-rank4-central-corrections/scratch/central_cohomology.py
frozen triple reconstruction: PASS
six inner labels: [(0, 0, 0, 1), (0, 1, 0, 0), (0, 0, 0, 0), (2, 0, 2, 1), (0, 2, 0, 2), (0, 1, 0, 1)]
nonorthogonal cube labels omega(qX,qY): 2
all 729 canonical-section action defects are inner: PASS
V-coordinate defect/associativity checks: 729 19683 78732
normalized central 2-cochain variables: 2028
associativity scalar equations generated: 59049
rank before stop/full rank: 1951
inconsistent: None
solution affine dimension: 77
combined rank after 18 relator definitions: 1969
relator-image affine dimension: 8
complete affine constraints on r=(x3,y3,z3,xyzinv,xz,yz), each in (c,s,t):
  1*r1 = 0
  1*r2 = 0
  1*r4 = 0
  1*r5 = 0
  1*r6+2*r11+2*r13 = 0
  1*r7 = 0
  1*r8 = 0
  1*r11+2*r13+2*r16 = 0
  1*r14 = 2
  1*r17 = 2
elapsed=58.01 sec maxrss=13952 KB
```

The V-identity and gauge-rank supplements were also run independently after
the displayed main calculation:

```text
pair action defects certified: 729
V associativity triples certified: 19683
V scalar identities certified: 78732
normalized C1 dimension 78
central coboundary rank 74
central 1-cocycle dimension 4
relator generator-gauge rank 5
gauge fixing exact relator row dimension 69
homogeneous cochain solution dim 77; relator-map rank 8; kernel 69
H2 dim 3 relator quotient dim 3
```

Script: `scratch/central_cohomology.py`.

What this establishes: exact feasibility and the complete section-gauged central-correction family for this one frozen lift.

What this does not establish: no exact extension group has yet been materialized from `(R0)`; order, kernel embedding, quotient, exponent, the 59,049 literal cubes, literal-set closure, and noncommutativity have not yet been checked. The universal odd-prime scope remains unanswered.
