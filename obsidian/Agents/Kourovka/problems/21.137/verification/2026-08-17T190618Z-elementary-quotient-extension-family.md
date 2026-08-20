---
title: "Verification — Kourovka 21.137 — elementary-quotient extension family"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "For p=3, every finite extension of H_3(3) x C_3^3 by a finite elementary abelian 3-group has pairwise commuting actual cube values."
claimant: Problem-21.137-Counterexample
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the literal set {g^p:g in G} is a subgroup, then it is abelian."
excluded_scopes: ["21.137/two-group-exponent-8", "every p=2 example", "non-elementary or nonabelian quotients in the p=3 kernel layer", "other kernels and other odd primes"]
target_object: "Every finite same-p group at every odd prime, of exponent exactly p^2, whose literal p-th-power set is a subgroup"
witness_object: "No concrete witness; the checked object is the proper family of finite extensions 1 -> H_3(3) x C_3^3 -> G -> A -> 1 with A elementary abelian"
witness_equals_target: false
citation: "none; direct proof below"
verification_method: "independent line-by-line hand proof plus a bounded F_3 linear-algebra checker"
tools_used: ["Python 3.12.3", "GAP 4.12.1 (availability probe only)", "Poppler pdftotext 24.02.0"]
scope_answered: ["bounded p=3/H_3(3)xC_3^3/elementary-abelian-quotient family only"]
scope_not_answered: ["21.137/odd-prime-exponent-p2"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/proven]
---

# Verification — Kourovka 21.137

## The claim

Put \(K=H_3(3)\times C_3^3\).  The bounded claim is:

> If \(G\) is any finite extension
> \[
> 1\longrightarrow K\longrightarrow G\longrightarrow A\longrightarrow1
> \]
> with \(A\) elementary abelian, then every two actual cubes in \(G\)
> commute.

Such a group automatically has exponent dividing nine: \(g^3\in K\) and
\(K\) has exponent three, so \(g^9=1\).  Thus the theorem includes every
exact-exponent-nine member of this family.  If its literal cube set is a
subgroup, that subgroup is therefore abelian.  In particular the literal cube
set cannot equal the nonabelian kernel \(K\).

I reconstructed this theorem without assuming the submitted calculations.
The proof below checks the factor order, both action cases, zero labels, and
commutation of the actual cube elements rather than only their quotient labels.

## Scope, revision, and clause matrix

The canonical scope is `21.137/odd-prime-exponent-p2`, revision 2.  Page 184
of the rendered source PDF was visually checked.

| source clause | active? | result of this verification |
|---|---:|---|
| If actual \(p\)-th powers form a subgroup, must it be powerful? | no | not answered |
| For \(p\ne2\), exponent \(p^2\), if actual \(p\)-th powers form a subgroup, must it be abelian? | yes | only one proper \(p=3\) extension family is proved |
| For a 2-group of exponent 8, if actual squares form a subgroup, must it be abelian? | no | excluded; not used |

Consequently `active_assignment_answered: no`, even though the bounded theorem
itself passes.

## Constraint-and-conclusion matrix

| constraint_id | role | proof use / candidate value | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | only \(p=3\), kernel \(K\), elementary abelian quotient | fail for universal coverage |
| `21.137-odd-p-not-2` | admissibility | \(p=3\) | pass in bounded family |
| `21.137-odd-finite-p-group` | admissibility | finite kernel and finite elementary abelian quotient | pass in bounded family |
| `21.137-odd-exponent-p2` | admissibility | all family members have exponent dividing 9; target members have exact exponent 9 | pass for every target member of the family, not universal coverage |
| `21.137-odd-power-set-definition` | admissibility | the exact union of every coset cube image is used | pass |
| `21.137-odd-power-set-subgroup` | admissibility | not assumed; if the literal cube set is a subgroup, pairwise commutation makes it abelian | pass for the bounded implication |
| `21.137-odd-P-abelian` | target conclusion | every pair of actual cubes commutes | proved only in the bounded family |

The submitted partial has no matching claim-check JSON; the only current
21.137 claim-check belongs to a different graded-image result.  Since this is a
bounded `PARTIAL_RESULT`, not a scope-closing `CLAIM`, the omission does not
supply or invalidate mathematical evidence, but it prevents treating this note
as a scope-closure artifact.

## Target vs witness

There is no exhibited witness.  The source target quantifies over all odd primes,
all finite same-prime groups of exact exponent \(p^2\), and all possible literal
power subgroups.  The checked family fixes \(p=3\), fixes a normal subgroup
isomorphic to \(H_3(3)\times C_3^3\), and restricts the quotient to be elementary
abelian.  It is therefore a proper subfamily, not an object proved equal to the
source target.

The kernel \(K\) is also not identified with the source power set by notation.
The proof first computes the literal cube set.  Equality with \(K\) would be an
additional saturation condition; the theorem rules it out because all actual
cubes commute whereas \(K\) does not.

## Subclaims and what each method proves

| subclaim | method | a pass proves | a pass does not prove |
|---|---|---|---|
| section law, associativity, cube formula | direct collection | every extension and every root coset are represented with the correct factor order | existence of any counterexample |
| induced \(GL_2(3)\) action | hand proof plus exhaustive 48-matrix check | constancy and fixed-line conclusion in the nontrivial-action case | anything at another prime or kernel |
| trivial-action block equations | hand composition | correct signs in \(R^3=0\), \(R^2L=J_q\), and outer commutation | a classification of all extensions |
| \(J_3+J_1\) centralizer | complete hand normal form plus bounded checker | no centralizer parameter is omitted and labels are dependent | source-scope universality |
| final commutation | exact commutator formula in \(K\) | actual cubes, including arbitrary central coordinates and zero labels, commute | literal cube-set closure unless separately assumed |

## Proof

### 1. The kernel law and its signs

Work over \(k=\mathbb F_3\).  Let \(V=k^2\), let
\(Z=kc\oplus k^3\), and identify \(K\) with \(V\oplus Z\) under

\[
 (v,z)(w,t)=\bigl(v+w,z+t+2\det(v,w)c\bigr).                 \tag{1}
\]

The cocycle \(B(v,w)=2\det(v,w)c\) is bilinear, so

\[
B(v,w)+B(v+w,r)=B(w,r)+B(v,w+r),
\]

which proves associativity of (1).  The inverse of \((v,z)\) is
\((-v,-z)\).  With \([x,y]=x^{-1}y^{-1}xy\), direct collection gives

\[
 [(v,z),(w,t)]=(0,\det(v,w)c).                              \tag{2}
\]

For left conjugation \(c_a(x)=axa^{-1}\), the exact sign is

\[
 c_{(a,b)}(v,z)=(v,z+\det(a,v)c).                           \tag{3}
\]

Thus \(Z(K)=Z\), \(K'=kc\), and elements whose \(V\)-coordinates lie
on a common line commute regardless of their central coordinates.

### 2. Complete extension multiplication and associativity

Let \(s:A\to G\) be a normalized section and write every element uniquely as
\(x s(u)\), denoted \((x,u)\).  Define

\[
 \alpha_u(x)=s(u)x s(u)^{-1},
 \qquad f(u,v)=s(u)s(v)s(u+v)^{-1}.
\]

Then, with the kernel factors retained in their displayed order,

\[
(x,u)(y,v)=\bigl(x\alpha_u(y)f(u,v),u+v\bigr).              \tag{4}
\]

Comparing the action of \(s(u)s(v)\) on \(K\) gives

\[
\alpha_u\alpha_v=c_{f(u,v)}\alpha_{u+v}.                   \tag{5}
\]

Comparing \((s(u)s(v))s(w)\) with \(s(u)(s(v)s(w))\), without
commuting any kernel factors, gives

\[
 f(u,v)f(u+v,w)=\alpha_u(f(v,w))f(u,v+w).                   \tag{6}
\]

Conversely, normalized data satisfying (5) and (6) make (4) associative,
so this is the complete extension model rather than a pointwise action cover.

Since \(3u=0\), two applications of (4) give, exactly,

\[
C_u(x):=(x,u)^3
=x\alpha_u(x)f(u,u)\alpha_{2u}(x)f(2u,u).                  \tag{7}
\]

No factor in (7) was commuted.  Every element of \(G\) has one pair
\((x,u)\), hence the literal actual-cube set is

\[
 \mathcal C=\bigcup_{u\in A}C_u(K)
            =\{1\}\cup\bigcup_{u\ne0}C_u(K),              \tag{8}
\]

because \(C_0(x)=x^3=1\).  Formula (8) is the complete union over all
root cosets, not one norm image and not the subgroup generated by cube values.
If \(\mathcal C=K\), then literal closure and cross-coset coverage follow;
the proof below in fact needs no such saturation assumption.

### 3. Induced action and constancy of every coset image

Let \(M_u\) be the action induced by \(\alpha_u\) on
\(V=K/Z(K)\).  Inner automorphisms act trivially on \(V\), so (5) gives

\[
 M_uM_v=M_{u+v}.                                             \tag{9}
\]

Thus \(M:A\to GL_2(3)\) is a homomorphism, \(M_u^3=I\), and
\(M_{2u}=M_u^2\).  If \(q_u\in V\) is the \(V\)-coordinate of
\(s(u)^3=f(u,u)f(2u,u)\), projecting (7) to \(V\) gives

\[
 \overline{C_u(x)}=q_u+(I+M_u+M_u^2)\bar x.                 \tag{10}
\]

In characteristic three,

\[
 I+M_u+M_u^2=(M_u-I)^2.
\]

Also \((M_u-I)^3=M_u^3-I=0\).  A nilpotent endomorphism of a
two-dimensional space has square zero, so

\[
 I+M_u+M_u^2=0.                                              \tag{11}
\]

Therefore every actual cube rooted in the same quotient coset \(u\) has the
same \(V\)-label \(q_u\), including the possibility \(q_u=0\).

### 4. Nontrivial induced action

Let \(a\in A\), and conjugate a root \(g\in Ks(u)\) by any lift of
\(a\).  Since \(A\) is abelian, the conjugated root remains in
\(Ks(u)\).  Its cube is the conjugate of \(g^3\).  On \(V\), this sends
the label \(q_u\) to \(M_aq_u\).  Constancy from (10)--(11) says the new
cube still has label \(q_u\).  Hence

\[
 q_u\in V^{M(A)}\qquad\text{for every }u\in A.              \tag{12}
\]

The image \(M(A)\) is a 3-subgroup of \(GL_2(3)\).  As
\(|GL_2(3)|=48\), a nontrivial image has order three.  A nonidentity
order-three matrix in characteristic three is a single \(2\times2\)
unipotent Jordan block, so its fixed space is one-dimensional.  Thus, if
\(M(A)\ne1\), every label \(q_u\), zero labels included, lies on one
line in \(V\).  Equation (2) then shows that every two actual cubes commute.

### 5. Trivial induced action: the cube block equations

Assume now \(M(A)=1\).  If every \(q_u=0\), all cubes lie in
\(Z(K)\) and the result is immediate.  Otherwise choose \(u\) with
\(q=q_u\ne0\).

Every automorphism inducing the identity on \(V\) has the form

\[
 \alpha_u(v,z)=\bigl(v,(I+R)z+Lv\bigr),                     \tag{13}
\]

where \(R:Z\to Z\), \(L:V\to Z\), and \((I+R)c=c\).  Since
an automorphism preserves the center, it restricts linearly to \(Z\); equation
(2) forces it to fix \(c\), and comparison with (1) makes the central shear
\(L\) additive, hence \(k\)-linear.  Since
\(\alpha_u\) is conjugation by \(s(u)\),

\[
 \alpha_u^3=c_{s(u)^3}.                                     \tag{14}
\]

The sign in (14) is the sign fixed in (3).  Cubing (13) gives

\[
 \alpha_u^3(v,z)=
 \bigl(v,(I+R)^3z+(I+(I+R)+(I+R)^2)Lv\bigr).
\]

In characteristic three this becomes

\[
 \alpha_u^3(v,z)=\bigl(v,(I+R^3)z+R^2Lv\bigr).
\]

The \(V\)-coordinate of \(s(u)^3\) is \(q\), so (3) and (14) are
equivalent to

\[
 R^3=0,
 \qquad R^2L=J_q,
 \qquad J_q(t)=\det(q,t)c.                                  \tag{15}
\]

Because \(q\ne0\), \(J_q\ne0\), hence \(R^2\ne0\).  On the
four-dimensional space \(Z\), (15) forces the Jordan type \(J_3+J_1\).
For that Jordan type \(R^2\) has rank one, while (15) puts \(kc\) in its
image; hence the image of \(R^2\) is exactly \(kc\).  We may therefore choose a basis
\(e_1,e_2,c,d\) of \(Z\) with

\[
 Re_1=e_2,\qquad Re_2=c,\qquad Rc=Rd=0.                      \tag{16}
\]

### 6. Full centralizer and outer commutation

Take any other nonzero label \(q'=q_v\), and write its action as
\((I+R',L')\).  Its own cube equation is

\[
 R'^3=0,\qquad R'^2L'=J_{q'}.                                \tag{17}
\]

Equation (5) makes \(u\mapsto[\alpha_u]\) a homomorphism
\(A\to\operatorname{Out}(K)\).  Since \(A\) is abelian, for some
\(h\in V\) we may write

\[
 \alpha_u\alpha_v=c_h\alpha_v\alpha_u.
\]

Composition of the blocks in (13), with (3), gives the exact equations

\[
 RR'=R'R,
 \qquad RL'-R'L=J_h.                                        \tag{18}
\]

Changing the chosen \(h\) or reversing the displayed inner commutator only
changes the sign of \(J_h\); the reduction modulo \(kc\) used below is
unchanged.

Here is the full centralizer calculation.  Before imposing any conditions,
write

\[
R'e_1=a e_1+b e_2+\gamma c+\delta d.
\]

Commutation with (16) forces

\[
R'e_2=a e_2+b c,\qquad R'c=a c,
\qquad R'd=\varepsilon c+\zeta d.                            \tag{19}
\]

Because \(I+R'\) fixes \(c\), we have \(a=0\).  Because
\(R'^3=0\), its induced scalar \(\zeta\) on the remaining one-dimensional
quotient must be zero.  Thus every permitted \(R'\), with no parameter omitted,
has exactly the form

\[
\begin{aligned}
 R'e_1&=b e_2+\gamma c+\delta d,\\
 R'e_2&=b c,\\
 R'c&=0,\\
 R'd&=\varepsilon c.
\end{aligned}                                                 \tag{20}
\]

It follows that

\[
 R'^2e_1=(b^2+\delta\varepsilon)c,
 \qquad R'^2e_2=R'^2c=R'^2d=0.                              \tag{21}
\]

Let \(x(t)\) and \(x'(t)\) be the \(e_1\)-coefficients of \(L(t)\)
and \(L'(t)\).  Equations (15), (17), and (21) say

\[
 x(t)=\det(q,t),
 \qquad (b^2+\delta\varepsilon)x'(t)=\det(q',t).             \tag{22}
\]

Now reduce the second equation in (18) modulo \(kc\).  From (16) and
(20),

\[
 RL'(t)\equiv x'(t)e_2,
 \qquad R'L(t)\equiv b x(t)e_2+\delta x(t)d\pmod{kc}.
\]

Therefore

\[
 x'=b x,
 \qquad \delta x=0.                                         \tag{23}
\]

The nonzero vector \(q\) makes the functional \(x=\det(q,-)\) nonzero,
so \(\delta=0\).  The nonzero vector \(q'\) makes the second functional
in (22) nonzero, so \(b\ne0\).  Combining (22)--(23), and using
\(b^3=b\) in \(\mathbb F_3\), yields

\[
 \det(q',t)=b^2x'(t)=b^3x(t)=b\det(q,t)
 \qquad(t\in V).
\]

The alternating form on \(V\) is nondegenerate, hence

\[
q'=bq.                                                        \tag{24}
\]

Thus every pair of nonzero cube labels is dependent.  Every zero label is of
course on the same line \(kq\).  All actual cubes therefore have
\(V\)-coordinates on one line, and (2) proves that the actual elements commute,
whatever their central coordinates are.

The nontrivial and trivial induced-action cases exhaust (9), proving the bounded
theorem.

## Independent finite checks

The checker
`Agents/Kourovka/problems/21.137/verification/scratch/check_elementary_quotient_extension.py`
was written independently for this audit.  It exhausts \(GL_2(3)\), verifies
the kernel signs, computes the complete linear centralizer solution dimension,
filters all centralizer parameters by \(R'^3=0\), checks (21), and exhausts the
functional implications of (22)--(23).  It is supporting evidence; the universal
family conclusion rests on the hand proof above.

Verbatim command and output:

```text
$ python3 Agents/Kourovka/problems/21.137/verification/scratch/check_elementary_quotient_extension.py
GL2(3) size: 48
elements with A^3=I: 9 (nonidentity 8)
fixed-space dimensions for nonidentity A^3=I: [1]
I+A+A^2 vanishes for every A^3=I: True
E0 associative on all V-coordinate triples: True
inner conjugation has +det(a,v)c sign: True
commutator is det(v,w)c for all V-coordinate pairs: True
number of V-lines: 4; all full central fibres over one line commute: True
centralizer matrices fixing c: 243
dimension of full linear solution space [R,X]=0, Xc=0: 5
among them R'^3=0: 81
R'^3=0 forces exactly a=zeta=0: True
R'^2 formula in the claimed normal form: True
nonzero-functional outer-commutation cases checked: 48
cases violating proportional-label conclusion: 0
```

Tool probe, verbatim:

```text
$ which gap
/usr/bin/gap
$ which sage
[no output; not installed]
$ which python3
/usr/bin/python3
$ which magma
[no output; not installed]
$ gap -q -c 'Print(GAPInfo.Version,"\\n"); QUIT;'
4.12.1
$ python3 --version
Python 3.12.3
$ pdftotext -v
pdftotext version 24.02.0
Copyright 2005-2024 The Poppler Developers - http://poppler.freedesktop.org
```

## Verdict

`status/proven` for the bounded theorem only.

The normalized-section multiplication and cube formula have the correct order;
the literal union includes every quotient coset; the induced-action branch is
constant and conjugation-invariant; the trivial-action branch has the stated
positive inner-conjugation sign; the full \(J_3+J_1\) centralizer contains no
missing parameter after \(R'^3=0\); and the outer-commutation equation forces all
nonzero labels onto one line.  Zero labels are central, and equation (2) upgrades
the one-line statement to commutation of the actual cubes themselves.

`active_assignment_answered: no`.  This verdict must not be promoted to a proof
of the unrestricted odd-prime Kourovka clause.

## Why this verdict

Every implication in the submitted bounded proof has been independently derived
above, including the two places most vulnerable to a silent gap: the literal
all-coset cube union and the omitted-looking \(\zeta d\) centralizer term.  The
latter exists before nilpotence and is forced to zero, exactly as required.  The
bounded checker separately agrees on all finite linear-algebra claims.

## What is NOT established

- The active universal scope `21.137/odd-prime-exponent-p2` is not answered.
- No prime other than \(3\) is covered.
- No kernel other than \(H_3(3)\times C_3^3\) is covered.
- A nonabelian exponent-three quotient \(G/K\) is not covered.
- The theorem does not assert that the literal cube set is a subgroup; it proves
  that if it is one, it is abelian in this family.
- No concrete extension or counterexample is constructed.
- The separate \(p=2\), exponent-eight clause is wholly excluded.

## What would upgrade it

Upgrading to the active assignment would require a proof covering every odd prime
and every finite same-prime group of exact exponent \(p^2\), or an independently
reconstructible same-scope counterexample satisfying every literal power-set and
closure row.  Enlarging only the quotient or kernel at \(p=3\) would remain a
partial family result.
