---
title: "Partial result — rank-four symplectic kernel exclusion"
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
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
outcome: PARTIAL_RESULT
active_assignment_answered: no
strategy: RANK4-SYMPLECTIC-SATURATION
strategy_status: exhausted
---

# Rank-four symplectic kernel exclusion

## Active target

Scope: `21.137/odd-prime-exponent-p2`, assignment revision 2.

Target statement: Let \(p\) be an odd prime and \(G\) a finite \(p\)-group of
exponent exactly \(p^2\). If the literal set
\(\{g^p:g\in G\}\) is a subgroup, then it is abelian.

## The bounded claim

Put
\[
 P=3_+^{1+4}\times C_3^2.
\]
For every finite extension
\[
 1\longrightarrow P\longrightarrow G\longrightarrow A\longrightarrow1
\]
with \(A\) elementary abelian, every two actual cubes in \(G\) commute.

In particular this covers the frozen quotient \(A=C_3^5\). No normalized factor
set on that carrier can have literal cube image equal to the nonabelian kernel
\(P\), and no member of the family whose literal cube set is a subgroup can be a
counterexample to the active assertion.

This is a candidate bounded theorem submitted for independent reconstruction. It
does not answer the universal odd-prime scope.

## Constraint-and-conclusion matrix

| constraint_id | role | bounded-family use | evidence | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | Only \(p=3\), the fixed kernel, and elementary-abelian quotients are covered. | Claim statement | fail for universal coverage |
| `21.137-odd-p-not-2` | admissibility | \(p=3>2\). | Claim statement | pass in bounded family |
| `21.137-odd-finite-p-group` | admissibility | Kernel and quotient are finite 3-groups; the frozen member has order \(3^{12}\). | Extension statement | pass |
| `21.137-odd-exponent-p2` | admissibility | Every family member has exponent dividing nine; the argument covers every exact-exponent-nine member. A nontrivial cube forces exact exponent nine. | Section 7 | pass for target members of the family |
| `21.137-odd-power-set-definition` | admissibility | Every coset cube image is used; no generated-power substitution occurs. | Sections 2 and 7 | pass |
| `21.137-odd-power-set-subgroup` | admissibility | Closure is not assumed in the proof; if the literal set is a subgroup, pairwise commutation makes it abelian. | Section 7 | pass for the bounded implication |
| `21.137-odd-P-abelian` | target conclusion | All actual cubes commute, hence any literal cube subgroup is abelian. | Sections 4–8 | established only in the bounded family |

## 1. Kernel coordinates

Let \(k=\mathbb F_3\), let \((V,\omega)\) be a four-dimensional symplectic
space, and put
\[
 Z=kc\oplus W,\qquad \dim W=2.
\]
In BCH coordinates the fixed kernel is \(P=V\oplus Z\), with multiplication
\[
 (v,z)(w,t)=(v+w,z+t+2\omega(v,w)c).                       \tag{1}
\]
Thus
\[
 [(v,z),(w,t)]=(0,\omega(v,w)c),                            \tag{2}
\]
\(P'=kc\), and \(Z(P)=Z\). In particular commutation in \(P\) depends only on
the symplectic pairing of the two \(V\)-labels.

Every automorphism obtained by conjugating \(P\) with a lift from the elementary
quotient can be written
\[
 \alpha(v,z)=(Mv,Tz+Lv),                                   \tag{3}
\]
where \(L:V\to Z\) is linear. Its cube is inner, hence it acts trivially on
\(P'=kc\) after cubing. The multiplier on \(kc\) lies in \(k^*=C_2\) and has
cube one, so it is already one. Consequently
\[
 M\in\operatorname{Sp}(V,\omega),\qquad Tc=c.              \tag{4}
\]

## 2. Exact section and cube identities

Choose a normalized section \(s:A\to G\), let \(\alpha_u\) be conjugation by
\(s(u)\), and let \(q_u\in V\) be the \(V\)-coordinate of \(s(u)^3\).
The factor set is retained implicitly: it determines \(s(u)^3\), hence \(q_u\),
and no restriction on it is imposed below.

Because \(3u=0\),
\[
 \alpha_u^3=\operatorname{Inn}(s(u)^3).                    \tag{5}
\]
Write
\[
 M_u=I+N_u,\qquad T_u=I+R_u.
\]
Equation (5) gives
\[
 M_u^3=I,\qquad R_u^3=0.                                   \tag{6}
\]
For an arbitrary root \(x s(u)\), projection of the exact collected cube to
\(V=P/Z(P)\) is
\[
 \overline{(x s(u))^3}=q_u+(I+M_u+M_u^2)\bar x
                       =q_u+N_u^2\bar x.                  \tag{7}
\]

Cubing (3) and comparing its central shear with the inner automorphism in (5)
gives the exact equation
\[
 R_u^2L_u+R_uL_uN_u=J_{q_u},
 \qquad J_q(v)=\omega(q,v)c.                               \tag{8}
\]
Indeed
\[
 T_u^2L_u+T_uL_uM_u+L_uM_u^2
 =R_u^2L_u+R_uL_uN_u
\]
in characteristic three once \(N_u^2=0\), which is established next.

## 3. Compatible order-three symplectic actions

Let \(M=I+N\in\operatorname{Sp}_4(3)\) with \(M^3=I\). Then \(N^3=0\).
In fact
\[
 N^2=0.                                                     \tag{9}
\]
If not, the Jordan type would be \(J_3+J_1\). Choose
\(x,b=Nx,a=N^2x\) and a complementary fixed vector \(y\). Symplectic
invariance under \(M\) and \(M^2\) gives
\[
 \omega(a,x)=\omega(a,b)=\omega(a,y)=0.
\]
Also \(\omega(a,a)=0\), so \(a\) would be orthogonal to all of \(V\), a
contradiction. Thus the individual possibilities are exactly identity,
\(J_2+J_1+J_1\), and \(J_2+J_2\).

Inner automorphisms of \(P\) act trivially on \(V\). Therefore
\(u\mapsto M_u\) is an honest representation of \(A\): the \(M_u\) commute and
\(M_{u+v}=M_uM_v\). From (9),
\[
 0=(M_uM_v-I)^2=2N_uN_v,
\]
so
\[
 N_uN_v=0\quad\hbox{for every }u,v.                        \tag{10}
\]
Also \(N_u^*=-N_u\), because \(M_u^{-1}=I-N_u\). Hence
\[
 R_0:=\sum_u\operatorname{im}N_u
\]
is totally isotropic, and the common fixed space is
\[
 F:=\bigcap_u\ker N_u=R_0^\perp.                           \tag{11}
\]
This gives the complete simultaneous normal-form trichotomy:

- \(\dim R_0=0\): the induced action is trivial;
- \(\dim R_0=1\): after choosing \(R_0=ka\), every
  \(N_u\) is a scalar multiple of \(v\mapsto\omega(a,v)a\);
- \(\dim R_0=2\): \(R_0\) is Lagrangian, and in a decomposition
  \(V=R_0\oplus R_0^*\), every \(N_u\) has block form
  \(\left(\begin{smallmatrix}0&B_u\\0&0\end{smallmatrix}\right)\) with
  \(B_u\) symmetric. The \(B_u\) form a linear subspace of
  \(\operatorname{Sym}_2(k)\).

## 4. All coset labels are globally fixed

Equation (9) reduces (7) to the single label \(q_u\) on every root in the coset
\(Ps(u)\). Conjugating such a root by any lift of \(v\in A\) leaves its quotient
coset equal to \(u\), because \(A\) is abelian. Its cube label is transformed to
\(M_vq_u\), but constancy on the coset says it is still \(q_u\). Thus
\[
 q_u\in F\qquad(u\in A).                                   \tag{12}
\]

If \(\dim R_0=2\), equations (11)–(12) put every label in the Lagrangian
\(F=R_0\), so all labels are already pairwise orthogonal. It remains to treat
\(\dim R_0\le1\).

## 5. The short-center cases

If \(\dim R_0=1\), fix \(R_0=ka\); if \(R_0=0\), use the convention
\(a=0\). Put
\[
 E=kJ_a\subseteq\operatorname{Hom}(V,kc).
\]
For every linear functional \(\lambda\) and every \(u\),
\[
 \lambda N_u\in E.                                        \tag{13}
\]

Consider a nonzero label \(q=q_u\), with center nilpotent \(R=R_u\).
If \(R^2=0\), equation (8) becomes \(RLN=J_q\). Its nonzero right side forces
\(R\) to have rank one and image \(kc\); then (13) gives \(J_q\in E\), hence
\[
 q\in ka.                                                  \tag{14}
\]
Such a label is orthogonal to every label in \(F=a^\perp\).

The only remaining possibility is \(R^2\ne0\). Since \(Z\) has dimension
three, \(R\) is one length-three Jordan block. Because \(Rc=0\), normalize
\[
 Re_1=e_2,\qquad Re_2=c,qquad Rc=0.                        \tag{15}
\]

## 6. A length-three center chain forces orthogonality

Take any other label \(q'=q_v\), and put \(R'=R_v\), \(N'=N_v\),
\(L'=L_v\). Outer commutation of \(\alpha_u\) and \(\alpha_v\) differs only
by an inner automorphism. Since inner automorphisms fix the center, \(R'\)
commutes with \(R\). The full centralizer of the regular nilpotent (15), together
with \(R'c=0\), gives
\[
 R'=bR+dR^2                                                  \tag{16}
\]
for unique \(b,d\in k\).

If \(b=0\), equation (8) for the primed action is
\[
 J_{q'}=dR^2L'N'.
\]
By (13), \(J_{q'}\in E\), so \(q'\in ka\) and \(q'\) is orthogonal to \(q\).

Suppose \(b\ne0\). Let \(x,y\) be the \(e_1,e_2\)-coordinate functionals of
\(L\), and let \(x',y'\) be those of \(L'\). Comparing the \(e_2\)- and
\(c\)-coordinates in (8) gives
\[
 xN=0,qquad J_q=x+yN,                                      \tag{17}
\]
and
\[
 x'N'=0,qquad J_{q'}=b^2x'+b y'N'.                        \tag{18}
\]

The difference between the central shears of
\(\alpha_u\alpha_v\) and \(\alpha_v\alpha_u\) is
\[
 RL'-R'L+LN'-L'N.
\]
It has image in \(kc\), because the outer commutator is inner. Comparing its
\(e_1,e_2\)-coordinates yields
\[
 xN'-x'N=0,qquad x'-bx+yN'-y'N=0.                         \tag{19}
\]
Modulo \(E\), equations (13) and (17)–(19) therefore give
\[
 J_q\equiv x,qquad J_{q'}\equiv b^2x',qquad x'\equiv bx,
\]
so, using \(b^3=b\) in \(k\),
\[
 J_{q'-bq}\in E,qquad q'-bq\in ka.                       \tag{20}
\]
Both \(q\) and \(q'\) lie in \(F=a^\perp\) by (12), and hence
\[
 \omega(q,q')=\omega(q,bq+ta)=0.                           \tag{21}
\]
This also contains the trivial-action case by setting \(a=0\): all nonzero
labels arising alongside a length-three center chain are scalar multiples.

Equations (14) and (21), together with the Lagrangian case in Section 4, prove
\[
 \omega(q_u,q_v)=0\qquad(u,v\in A).                        \tag{22}
\]

## 7. Literal cube-set conclusion

Every element of \(G\) lies in exactly one root coset \(Ps(u)\). Equations
(7), (9), and (22) describe the \(V\)-label of its actual cube, and (2) shows
that arbitrary central coordinates do not change the commutator. Therefore any
two actual cubes commute.

This conclusion uses the literal all-coset cube set. It does not replace that set
by the subgroup generated by cubes, and it does not assume a local affine cover
extends to a group.

Since \(G/P\) and \(P\) have exponent three, every family member has exponent
dividing nine. If it has any nontrivial cube, then it contains an element of order
nine and its exponent is exactly nine. Thus every exact-exponent-nine member is
covered. If its literal cube set is a subgroup, pairwise commutation makes that
subgroup abelian. In particular the literal cube set cannot equal the nonabelian
kernel \(P\).

## What was computed in

No finite computation was run. The checked object is the full symbolic family of
extensions of the fixed kernel \(3_+^{1+4}\times C_3^2\) by an elementary
abelian 3-group, with arbitrary normalized factor set. The proof uses necessary
identities satisfied by every such complete extension and therefore does not need
to enumerate factor systems.

## What this does not establish

- It does not answer the active universal scope.
- It does not cover another odd prime.
- It does not cover another possible power subgroup, including larger symplectic
  rank or center.
- It does not cover a non-elementary or nonabelian quotient over this kernel.
- It does not assert literal cube-set closure for an arbitrary family member; it
  shows that closure, if present, can only yield an abelian subgroup.
- It does not classify normalized factor sets or construct a finite witness.

## How this could be wrong

1. The reduction (3) uses the class-two exponent-three BCH model; an omitted
   nonlinear automorphism term would invalidate the center-shear equations.
2. The assertion that conjugation actions fix \(c\) uses both
   \(\alpha_u^3\) inner and \(\mathbb F_3^*\) having no nontrivial element of
   order three; this must be checked before calling \(M_u\) symplectic.
3. A sign or composition-order error in (8) or (19) could alter the relation among
   \(x,x',y,y'\), although the argument only uses their classes modulo \(E\).
4. The passage from conjugation invariance to (12) requires the projected cube map
   to be constant on a whole quotient coset; this depends critically on the
   four-dimensional symplectic fact \(N_u^2=0\).
5. Independent reconstruction should verify that the centralizer (16) contains
   every center action and that the \(b=0\) branch has not silently divided by
   \(b\).

## Independent certificate plan

A validator can reconstruct the result without trusting constants or software:

1. build the BCH law (1) and rederive (3), (7), and (8);
2. check the three symplectic action types and the simultaneous trichotomy in
   Section 3;
3. repeat the three-dimensional regular-nilpotent centralizer calculation (16);
4. compare the two noncentral coordinates in (17)–(19);
5. conclude (22) and use (2) on arbitrary actual cube elements.

No computation output is offered as evidence.
