---
title: "Frozen manifest — rank-four H3 shear-orbit projected-support gate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: RANK4-H3-SHEAR-ORBIT-SUPPORT
direction: counterexample
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, topic/power-maps, project/kourovka, status/draft]
---

# Evidence boundary

This increment uses only the frozen matrices and conventions displayed in the
rank-four lift manifest.  It does not import the submitted `6,561`, `27`, `135`,
or `729` family outputs; it opens no central factor system, central relator row,
or finite extension group.

All arithmetic is over `F3`.  Column coordinates on
`V=<e1,e2,f1,f2>` use

`omega(v,w)=v_e1 w_f1+v_e2 w_f2-v_f1 w_e1-v_f2 w_e2`.

The exact frozen inputs are

```text
A = 1100/0100/0010/0021     B = 1001/0110/0010/0001
C = 1020/0100/0010/0001

TX = 120/011/001            TY = 110/011/001
TZ = 101/010/001

qX = f2 = 0001              qY = e2 = 0100.
```

The checker first verifies all order-three, commutator, symplectic, fixed-label,
and `omega(qX,qY)=2` identities directly.

# Independently reconstructed 56-row system

For triples `(M,T,L)` use only

`(M,T,L)o(M',T',L')=(MM',TT',T L'+L M')`

and `[u,v]=u^-1 v^-1 u v`.  The 36 variables are the row-major entries of
`LX,LY,LZ`.  The checker evaluates the following exact residuals at zero and at
each of the 36 coordinate vectors, thereby reconstructing rather than copying
the affine matrix:

1. all 12 coordinates of `alphaX^3-(I,I,J_qX)`;
2. all 12 coordinates of `alphaY^3-(I,I,J_qY)`;
3. the eight `s,t` coordinates of `alphaZ^3`;
4. the eight `s,t` coordinates of `[alphaX,alphaY]alphaZ^-1`;
5. the eight `s,t` coordinates of `[alphaX,alphaZ]`;
6. the eight `s,t` coordinates of `[alphaY,alphaZ]`.

Here `J_q` has `c` row
`(-q_f1,-q_f2,q_e1,q_e2)`.  The frozen gate requires exactly 56 equations,
36 variables, coefficient and augmented rank 17, and affine dimension 19.  A
mismatch terminates the route without editing any input.

# Complete equivalence transformations

An independent quotient-generator lift change changes one generator shear by
an arbitrary inner row `J_u`.  Since

`I+A+A^2=I+B+B^2=0`,

all four inner directions preserve each of the exact labels `qX,qY`; the `Z`
label is not frozen.  Thus twelve displayed coordinate translations (the four
`c`-row entries in each of `LX,LY,LZ`) are admissible.

For a simultaneous kernel automorphism `beta=(D,U,R)`, direct use of the triple
law gives

`L_i -> U^-1 (L_i D + T_i R - R M_i)`.

The continuous shear part `D=I,U=I` therefore contributes the twelve explicit
translations

`Delta L_i=T_i R-R M_i`, for the twelve matrix units of `R in Mat(3,4)`.

For completeness, the finite stabilizer is derived without a group catalogue.
Commuting with `A,B`, fixing `f2,e2`, and preserving `omega` successively forces

`D_a(e1)=e1, D_a(e2)=e2, D_a(f1)=f1+a e1, D_a(f2)=f2`, `a in F3`.

Commuting with `TX,TY`, fixing `c`, and then commuting with `TZ` forces

`U_d(c)=c, U_d(s)=s, U_d(t)=t+d c`, `d in F3`.

Hence the complete discrete stabilizer has exactly nine pairs `(D_a,U_d)`.  Its
action with `R=0` is `L_i -> U_d^-1 L_i D_a`.  The checker verifies the listed
centralizer identities, embeds every translation in the 19-dimensional
homogeneous solution space, and checks the nine induced affine quotient maps
form `C3 x C3`.  Genuine orbit count is computed by Burnside and, only if at
most 729, replayed explicitly; the orbit-size sum is the original `3^19` shear
space.

# Factor-independent support observable

Use the fixed section word

`h=(a,b,d) -> alphaX^a alphaY^b alphaZ^d`, `0<=a,b,d<3`.

For all 27 words the checker requires `alpha_h^3=(I,I,J_lambda)` exactly.  Put

`W_h=im(I+M_h+M_h^2)` and `F_h=lambda+W_h`.

The signature is represented canonically by applying a row basis of the
annihilator of `W_h` to `lambda`, i.e. as a point of the direct product
`product_h V/W_h`.  The checker row-reduces its affine image and kernel.  It
verifies exact invariance under every translation gauge and equivariance
`Sigma(beta^-1 L beta)=D_a^-1 Sigma(L)` under the finite stabilizer.  Therefore
subspace shape and symplectic rank are genuine necessary-gate invariants.

If the signature-image dimension exceeds eight, or the exact genuine-orbit
count exceeds 729, the script emits the mandated hard-kill certificate and does
not enumerate representatives.  Otherwise every genuine representative gets
all 27 `(lambda,W_h,F_h)` rows, the complete union `Sigma`, subspace status, and
the rank of `omega` on its linear span.

# Frozen checker and bounded command

Checker:
`Agents/Kourovka/problems/21.137/runs/2026-08-17-r27-rank4-shear-orbit-support/scratch/check_shear_orbits.py`

Exact requested command:

```text
timeout 45s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r27-rank4-shear-orbit-support/scratch/check_shear_orbits.py --full
```

Expected resources: one CPU, less than 128 MB RAM, less than 45 seconds wall
time.  Requested lease duration: five minutes.  No solver package, group
enumerator, factor system, or network access is used.

`checker_sha256`: `8b33f11c261c78aad8f8d5e54d52b9aa7c7fb3a449301c283a49d26d57f4f969`

# Interpretation limit

A passing projected support is not a group or counterexample and authorizes no
cohomology by itself.  An all-orbit failure excludes only this frozen
automorphism-lift family.  In all cases `active_assignment_answered: no`.
