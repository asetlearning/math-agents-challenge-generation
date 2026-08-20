---
title: "Verification — Kourovka 21.137 — rank-four kernel hand exclusion"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "For p=3, every finite extension of 3_+^(1+4) x C_3^2 by a finite elementary abelian 3-group has pairwise commuting actual cube values."
claimant: Problem-21.137-Counterexample
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the literal set {g^p:g in G} is a subgroup, then it is abelian."
excluded_scopes: ["21.137/two-group-exponent-8", "every p=2 example", "other kernels", "non-elementary or nonabelian quotients", "other odd primes"]
target_object: "Every finite same-p group at every odd prime, of exponent exactly p^2, whose literal p-th-power set is a subgroup"
witness_object: "No concrete witness; the checked object is the proper family of finite extensions 1 -> 3_+^(1+4) x C_3^2 -> G -> A -> 1 with A elementary abelian"
witness_equals_target: false
citation: "none; independent direct proof below"
verification_method: "line-by-line hand proof plus an independent exhaustive F_3 linear-algebra checker"
tools_used: ["Python 3.12.3", "GAP 4.12.1 (availability probe only)", "Poppler pdftotext 24.02.0"]
scope_answered: ["bounded p=3/3_+^(1+4)xC_3^2/elementary-abelian-quotient family only"]
scope_not_answered: ["21.137/odd-prime-exponent-p2"]
active_assignment_answered: no
outcome: PARTIAL_RESULT
review_active_minutes: 18
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/proven]
---

# Verification — Kourovka 21.137

## The claim

Put
\[
 K=3_+^{1+4}\times C_3^2.
\]
The submitted bounded theorem says that, for every finite extension
\[
 1\longrightarrow K\longrightarrow G\longrightarrow A\longrightarrow1
 \tag{E}
\]
with \(A\) elementary abelian, every two literal actual cubes in \(G\)
commute.

**Verdict: PASS for this bounded theorem.**  The reconstruction below checks the
BCH automorphism form, the exact section-cube and cube-inner equations, all
order-three symplectic types, the simultaneous action trichotomy, global label
invariance, both center branches, the shear-composition order, and the final
literal-set statement.  This remains a `PARTIAL_RESULT` with
`active_assignment_answered: no`.

## Scope, revision, and clause matrix

The locked record is `21.137/odd-prime-exponent-p2`, assignment revision 2.
I independently rendered and read source PDF page 184.

| source clause | active? | result here |
|---|---:|---|
| If the \(p\)-th powers form a subgroup, must it be powerful? | no | not answered |
| For \(p\ne2\), exponent \(p^2\), must a literal power subgroup be abelian? | yes | proved only for the proper family (E) at \(p=3\) |
| For a 2-group of exponent 8, must a literal square subgroup be abelian? | no | excluded and unused |

The active clause quantifies over every odd prime and every admissible finite
group.  Fixing one kernel and elementary quotients cannot answer it.

## Constraint-and-conclusion matrix

| constraint_id | role | proof use / candidate value | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | only \(p=3\), fixed kernel \(K\), elementary quotient | fail for universal coverage |
| `21.137-odd-p-not-2` | admissibility | \(p=3>2\) | pass in family |
| `21.137-odd-finite-p-group` | admissibility | finite extension of finite 3-groups | pass in family |
| `21.137-odd-exponent-p2` | admissibility | every member has exponent at most 9; every exact-exponent-nine member is covered | pass for target members of family only |
| `21.137-odd-power-set-definition` | admissibility | every element in every quotient coset is cubed | pass |
| `21.137-odd-power-set-subgroup` | admissibility | no closure is assumed; closure is used only in the final implication | pass for bounded implication |
| `21.137-odd-P-abelian` | target conclusion | all actual cube values commute | proved in bounded family only |

The routed artifact is a bounded `REPORT`/`PARTIAL_RESULT`, not a scope-closing
`CLAIM`, and supplies no claim-check JSON.  That does not affect the hand theorem,
but it also cannot satisfy the state gate for scope closure.

## Target versus checked object

The source target is the universal odd-prime implication.  The checked object is
the symbolic class (E), with no particular factor set or concrete witness.  The
checked class is a proper subclass of the source target, so
`witness_equals_target: false` and `active_assignment_answered: no` are mandatory.

The letter \(K\) here denotes the fixed normal kernel, not the source's literal
power set.  The proof computes all actual cubes first.  It neither assumes nor
silently substitutes equality of that set with \(K\).

## Subclaims and what the methods prove

| subclaim | method | a pass proves | a pass does not prove |
|---|---|---|---|
| BCH law and automorphism form | direct collection | no nonlinear shear term is omitted | existence/classification of factor sets |
| cube and cube-inner equations | exact composition | correct order and sign for every section lift | source-scope universality |
| \(\operatorname{Sp}_4(3)\) action types | hand proof plus exhaustive checker | \(N^2=0\) for every \(M^3=I\) | another prime or symplectic rank |
| simultaneous action and fixed labels | representation and conjugation proof | the \(R_0/F\) trichotomy and global invariance | literal cube-set closure |
| center branches | exact linear algebra | every square-zero and regular-center case | arbitrary larger centers |
| final commutator | kernel commutator law | arbitrary central cube coordinates are harmless | any group outside (E) |

## Proof

### 1. Kernel law, commutator, and every automorphism

Work over \(k=\mathbb F_3\).  Let \((V,\omega)\) be a nondegenerate
four-dimensional symplectic space and
\[
 Z=kc\oplus W,\qquad \dim W=2.
\]
The kernel is \(K=V\oplus Z\) with
\[
 (v,z)(w,t)=(v+w,z+t+2\omega(v,w)c).                       \tag{1}
\]
Bilinearity of \(2\omega\) proves associativity, and the inverse is
\((-v,-z)\).  With \([x,y]=x^{-1}y^{-1}xy\), direct collection gives
\[
 [(v,z),(w,t)]=(0,\omega(v,w)c).                            \tag{2}
\]
For left conjugation \(c_a(x)=axa^{-1}\), the exact sign is
\[
 c_{(q,r)}(v,z)=(v,z+\omega(q,v)c).                         \tag{3}
\]
Thus \(K'=kc\) and \(Z(K)=Z\).

Let \(\alpha\in\operatorname{Aut}(K)\).  It induces a linear map \(M\)
on \(V=K/Z\) and a linear map \(T\) on \(Z\).  Since \(K'=kc\) is
characteristic, write \(T(c)=\mu c\).  Preservation of (2) says
\[
 \omega(Mv,Mw)=\mu\omega(v,w).                             \tag{4}
\]
After choosing the displayed splitting \(V\to K\), write the remaining central
term as \(f(v)\).  Comparing \(\alpha((v,0)(w,0))\) with
\(\alpha(v,0)\alpha(w,0)\), and using (4), gives
\[
 f(v+w)=f(v)+f(w).
\]
Over \(\mathbb F_3\), \(f\) is linear.  Hence every automorphism has exactly
the form
\[
 \alpha(v,z)=(Mv,Tz+Lv),                                   \tag{5}
\]
with no omitted quadratic or nonlinear shear.

Choose a normalized section \(s:A\to G\), and let \(\alpha_u=c_{s(u)}\).
Since \(3u=0\),
\[
 \alpha_u^3=c_{s(u)^3}.                                    \tag{6}
\]
The right side is inner, so it fixes \(V\) and \(Z\).  Therefore
\(M_u^3=T_u^3=I\).  Its multiplier satisfies \(\mu_u^3=1\), but
\(k^*=C_2\), so \(\mu_u=1\).  Consequently
\[
 M_u\in\operatorname{Sp}(V,\omega),\qquad T_u(c)=c.        \tag{7}
\]
Writing \(M_u=I+N_u\), \(T_u=I+R_u\), characteristic three gives
\[
 N_u^3=0,\qquad R_u^3=0,\qquad R_uc=0.                      \tag{8}
\]

### 2. Exact section cube and cube-inner shear

Let \(q_u\in V\) be the \(V\)-coordinate of \(s(u)^3\).  For every
\(x\in K\), collection without commuting kernel factors gives
\[
 (x s(u))^3=x\,\alpha_u(x)\,\alpha_u^2(x)\,s(u)^3.         \tag{9}
\]
Projecting to \(V\),
\[
 \overline{(x s(u))^3}
 =q_u+(I+M_u+M_u^2)\bar x
 =q_u+N_u^2\bar x.                                         \tag{10}
\]

Now cube (5) as an actual composition.  Its central shear is
\[
 T_u^2L_u+T_uL_uM_u+L_uM_u^2
 =R_u^2L_u+R_uL_uN_u+L_uN_u^2.                             \tag{11}
\]
The cancellations in (11) use only characteristic three.  By (3), the inner
automorphism on the right side of (6) has shear
\[
 J_{q_u}(v)=\omega(q_u,v)c                                  \tag{12}
\]
with a positive sign.  Once \(N_u^2=0\) is proved below, (11) is therefore
exactly
\[
 R_u^2L_u+R_uL_uN_u=J_{q_u}.                               \tag{13}
\]
This is the submitted equation (8), with its composition order and sign intact.

### 3. Every order-three symplectic type has square-zero nilpotent part

Let \(M=I+N\in\operatorname{Sp}_4(3)\) and \(M^3=I\).  Then
\(N^3=0\).  A failure of \(N^2=0\) would have Jordan type \(J_3+J_1\).
Choose a chain
\[
 Nx=b,\qquad Nb=a,\qquad Na=0
\]
and a fixed vector \(y\) completing the basis.

Since \(Mb=b+a\) and \(My=y\), invariance of \(\omega(b,y)\) gives
\(\omega(a,y)=0\).  From \(Mx=x+b\) and \(Mb=b+a\), invariance of
\(\omega(b,x)\) gives
\[
 \omega(a,x)+\omega(a,b)=0.                                \tag{14}
\]
Also \(M^2x=x-b+a\) and \(M^2b=b-a\).  Invariance under \(M^2\)
gives \(\omega(a,x)=0\), and then (14) gives \(\omega(a,b)=0\).
Together with \(\omega(a,a)=0\), the nonzero vector \(a\) is orthogonal to
the whole basis, contradicting nondegeneracy.  Thus
\[
 N^2=0.                                                     \tag{15}
\]
The exhaustive possibilities are therefore
\(1^4\), \(2+1+1\), and \(2+2\): identity,
\(J_2+J_1+J_1\), and \(J_2+J_2\).  The independent checker below enumerates
all 51,840 matrices in \(\operatorname{Sp}_4(3)\): among the 801 matrices
with \(M^3=I\), their ranks \(\operatorname{rank}(M-I)\) are respectively
0, 1, and 2, and none violates (15).

### 4. Simultaneous normal form and global fixed labels

The section factor set changes \(\alpha_u\alpha_v\) from
\(\alpha_{u+v}\) only by an inner automorphism.  Inner automorphisms act
trivially on \(V\), so
\[
 M_{u+v}=M_uM_v.                                           \tag{16}
\]
Thus the \(M_u\) commute, and their products again have cube one.  Put
\(N=N_u\), \(N'=N_v\).  Using \(N^2=N'^2=0\) and \(NN'=N'N\),
\[
 (M_uM_v-I)^2=(N+N'+NN')^2=2NN'.                          \tag{17}
\]
The left side is zero by (15), and \(2\ne0\) in \(k\), hence
\[
 N_uN_v=0\qquad(u,v\in A).                                \tag{18}
\]

Because \(M_u^{-1}=I-N_u\) and \(M_u\) is symplectic, the symplectic
adjoint satisfies \(N_u^*=-N_u\).  Therefore
\[
 R_0:=\sum_u\operatorname{im}N_u
\]
is totally isotropic, and
\[
 F:=\bigcap_u\ker N_u=R_0^\perp.                          \tag{19}
\]
This proves the complete simultaneous trichotomy:

- if \(\dim R_0=0\), every \(N_u=0\);
- if \(\dim R_0=1\), write \(R_0=ka\).  Every
  \(N_u(v)=\lambda_u(v)a\), and \(N_u^*=-N_u\) forces
  \(\lambda_u\) to be a scalar multiple of \(\omega(a,-)\);
- if \(\dim R_0=2\), then \(R_0\) is Lagrangian.  Every \(N_u\) kills
  \(R_0\) by (18), and relative to \(V=R_0\oplus R_0^*\) has block form
  \(\left(\begin{smallmatrix}0&B_u\\0&0\end{smallmatrix}\right)\),
  with \(B_u\) symmetric by \(N_u^*=-N_u\).

By (10) and (15), every cube rooted in the whole coset \(Ks(u)\) has the
single projected label \(q_u\).  Conjugate any such root by \(s(v)\).
Because \(A\) is abelian, the conjugated root is still in \(Ks(u)\).  Cubing
commutes with conjugation, so its projected cube label is \(M_vq_u\); coset
constancy says that label is also \(q_u\).  Hence, globally and independently
of the factor set,
\[
 q_u\in F\qquad(u\in A).                                   \tag{20}
\]

If \(\dim R_0=2\), then \(F=R_0\) is Lagrangian, so all labels are already
pairwise orthogonal.  It remains only to treat \(\dim R_0\le1\).

### 5. The square-zero center branch has no hidden division

When \(\dim R_0=1\), fix \(R_0=ka\); when \(R_0=0\), set \(a=0\).
Let
\[
 E=kJ_a\subseteq\operatorname{Hom}(V,kc).
\]
The preceding normal form gives, for every functional \(\lambda\) and every
\(u\),
\[
 \lambda N_u\in E.                                        \tag{21}
\]

Fix a nonzero label \(q=q_u\) and abbreviate \(R=R_u\), \(N=N_u\),
\(L=L_u\).  If \(R^2=0\), equation (13) becomes
\[
 RLN=J_q.                                                   \tag{22}
\]
The nonzero right side makes \(R\ne0\).  A square-zero endomorphism of a
three-dimensional space has rank at most one, hence \(\operatorname{rank}R=1\).
Since (22) has image \(kc\), necessarily \(\operatorname{im}R=kc\).  Write
\(R(z)=\rho(z)c\).  Then
\[
 J_q=(\rho L)N\,c\in E                                    \tag{23}
\]
by (21), so \(q\in ka\).  No rank-one map was inverted and no scalar was
divided by.  Since every label lies in \(F=a^\perp\) by (20), such \(q\) is
orthogonal to every label.

### 6. The regular center branch, including \(b=0\)

The remaining case has \(R^2\ne0\).  Since \(R^3=0\) on the
three-dimensional center, \(R\) is one regular \(J_3\) block.  Because
\(Rc=0\), choose
\[
 Re_1=e_2,\qquad Re_2=c,\qquad Rc=0.                        \tag{24}
\]

Take any second label \(q'=q_v\) and write \(R',N',L'\) for its data.
Inner automorphisms fix the center, so the center actions \(T_u=I+R_u\) form
an honest representation of \(A\); in particular \(R'R=RR'\).
The centralizer of the regular nilpotent \(R\) in
\(\operatorname{End}(Z)\) is exactly \(k[I,R,R^2]\).  Since \(R'c=0\),
the identity coefficient is zero.  Thus, uniquely,
\[
 R'=bR+dR^2.                                                \tag{25}
\]
The checker independently enumerates all \(3^9\) endomorphisms and finds
exactly the same nine constrained matrices.

If \(b=0\), then \(R'=dR^2\) and \(R'^2=0\).  Its own equation (13) is
\[
 J_{q'}=dR^2L'N'.                                          \tag{26}
\]
The map \(R^2\) has image \(kc\); if \(x'\) is the \(e_1\)-coordinate
functional of \(L'\), (26) is \(J_{q'}=d(x'N')c\).  Equation (21) puts this
in \(E\), so \(q'\in ka\), including \(q'=0\) when \(d=0\).  Since
\(q\in a^\perp\), \(\omega(q,q')=0\).  This branch contains no division by
\(b\) and no omitted zero case.

Now suppose \(b\ne0\).  Decompose
\[
 L=e_1x+e_2y+cz,\qquad L'=e_1x'+e_2y'+cz'
\]
for functionals on \(V\).  Reading the \(e_2\)- and \(c\)-coordinates of
(13), first for \(R\) and then for \(R'=bR+dR^2\), gives exactly
\[
 xN=0,\qquad J_q=x+yN,                                     \tag{27}
\]
\[
 x'N'=0,\qquad J_{q'}=b^2x'+b y'N'.                        \tag{28}
\]
Here the term \(d x'N'\) vanishes only after the first equation in (28), and
the inference \(x'N'=0\) uses precisely the declared assumption \(b\ne0\).

For completeness, composition of automorphism triples is
\[
 (M,T,L)\circ(M',T',L')
   =(MM',TT',\,TL'+LM').                                   \tag{29}
\]
The two orders differ by an inner automorphism.  Their \(M\)- and \(T\)-parts
are equal, so the shear difference
\[
 D=RL'-R'L+LN'-L'N                                         \tag{30}
\]
has image in \(kc\).  Reversing the convention would replace \(D\) by
\(-D\), leaving the next zero coordinates unchanged.  The \(e_1\)- and
\(e_2\)-coordinates of (30) are
\[
 xN'-x'N=0,\qquad x'-bx+yN'-y'N=0.                         \tag{31}
\]
The parameter \(d\) occurs only in the discarded central coordinate; no term
has been suppressed from either displayed noncentral equation.

Reduce (27)--(31) modulo \(E\).  Equation (21) applies to every functional and
every \(N_u\), so
\[
 J_q\equiv x,\qquad J_{q'}\equiv b^2x',\qquad x'\equiv bx
 \pmod E.
\]
Since \(b^3=b\) in \(\mathbb F_3\),
\[
 J_{q'-bq}\in E,\qquad q'-bq\in ka.                         \tag{32}
\]
Both labels lie in \(F=a^\perp\), so (32) gives
\[
 \omega(q,q')=0.                                          \tag{33}
\]
When \(a=0\), equation (32) simply says that every nonzero label occurring
with a regular center action is a scalar multiple of \(q\).  Zero labels are
automatically orthogonal.  Together with the square-zero and Lagrangian branches,
(33) proves
\[
 \omega(q_u,q_v)=0\qquad(u,v\in A).                        \tag{34}
\]

### 7. Arbitrary central cube coordinates and the literal all-coset set

Every element of \(G\) has a unique form \(x s(u)\).  Formula (9), for every
\(x\in K\) and every \(u\in A\), is therefore the literal actual-cube set
\[
 \{g^3:g\in G\}
 =\bigcup_{u\in A}\{(x s(u))^3:x\in K\}.                  \tag{35}
\]
No generated-power subgroup replaces (35).  By (10), (15), and (34), the
\(V\)-coordinates of any two members of (35) are orthogonal.  Their central
coordinates may be arbitrary, but (2) shows those coordinates do not enter the
commutator.  Hence every two actual cubes commute.

Finally, \(K\) and \(A\) have exponent three.  Thus \(g^3\in K\) and
\(g^9=1\) for every \(g\in G\).  A member of (E) with a nontrivial cube has
exact exponent nine; the exponent-three members are irrelevant to the exact-
exponent-nine admissibility row but also satisfy the theorem.  If the literal
set (35) is a subgroup, pairwise commutation makes it abelian.

## Independent finite-field evidence

The checker
`Agents/Kourovka/problems/21.137/verification/scratch/check_rank4_linear.py`
was written independently for this audit.  It enumerates
\(\operatorname{Sp}_4(3)\) by all symplectic bases, not by the submitted proof,
and enumerates every \(3\times3\) matrix for the regular-center centralizer.
It is supporting evidence; the family theorem rests on the hand proof above.

Verbatim command and output:

```text
$ /usr/bin/time -f 'elapsed=%e sec maxrss=%M KB' python3 Agents/Kourovka/problems/21.137/verification/scratch/check_rank4_linear.py
Sp4(3) matrices from symplectic bases: 51840 (expected 51840)
M^3=I type counts by rank(M-I): {0: 1, 1: 80, 2: 720}
M^3=I with (M-I)^2 != 0: 0
End(F3^3) matrices commuting with regular R: 27
Centralizer equals F3[I,R,R^2]: True
Commuting R' with R'c=0 and (R')^3=0: 9
Constrained set equals {bR+dR^2}: True
elapsed=2.15 sec maxrss=21992 KB
```

Tool probe, verbatim:

```text
$ command -v gap
/usr/bin/gap
$ gap -q -c 'Print(GAPInfo.Version,"\\n"); QUIT;'
4.12.1
$ command -v sage
[no output; not installed]
$ command -v python3
/usr/bin/python3
$ python3 --version
Python 3.12.3
$ command -v magma
[no output; not installed]
$ command -v pdftotext
/usr/bin/pdftotext
$ pdftotext -v
pdftotext version 24.02.0
```

Source check, relevant verbatim output:

```text
$ source _meta/agents/Kourovka/paths.env
$ pdftotext -f 184 -l 184 -layout "$KOUROVKA_PDF" -
21.137. If the p-th powers in a finite p-group form a subgroup, must that subgroup
be powerful? That is, for p ̸= 2, if the p-th powers in a p-group of exponent p2 form a
subgroup, must that subgroup be abelian? For a 2-group of exponent 8, if the squares
form a subgroup, must that subgroup be abelian?
```

## Verdict

**PASS — `status/proven` for the bounded theorem only.**

Every algebraic step survives hostile reconstruction.  In particular, equation
(13) has the correct composition order and positive inner-conjugation sign; all
order-three symplectic actions in dimension four have square-zero nilpotent part;
the simultaneous \(R_0/F\) trichotomy is complete; constancy on a root coset plus
conjugation proves global label invariance; the square-zero center case uses only
rank and image, not an inverse; the regular-center centralizer is complete; the
\(b=0\) case is handled without division; and every term affecting the two
noncentral coordinates of the outer-commutation shear is present.  Orthogonality
then proves commutation of actual cube elements with arbitrary central coordinates.

The outcome is nevertheless only `PARTIAL_RESULT` and
`active_assignment_answered: no`.

## Why this verdict

The hand argument quantifies over every section and factor set because it uses only
identities forced in every complete extension (E).  It never assumes literal cube
closure, a multiplicative section, or saturation onto the kernel.  The independent
finite checker agrees with both finite linear-algebra classifications on which the
proof depends.

## What is NOT established

- The active universal scope `21.137/odd-prime-exponent-p2` is not answered.
- No odd prime other than \(3\) is covered.
- No kernel other than \(3_+^{1+4}\times C_3^2\) is covered.
- No non-elementary or nonabelian quotient is covered.
- The theorem does not assert that the literal cube set is a subgroup in an
  arbitrary family member; it proves that, if it is, it is abelian.
- No concrete extension or counterexample is constructed.
- The separate \(p=2\), exponent-eight clause is wholly excluded.

## What would upgrade it

Upgrading to the active assignment requires a proof for every odd prime and every
finite same-prime group of exact exponent \(p^2\), or an independently checked
same-scope counterexample satisfying every literal power-set and closure row.
Enlarging only this \(p=3\) extension family would remain partial progress.

## Review-time accounting

This was Validator review time, not problem-agent research time.  Active review
interval: 2026-08-17T19:31:52Z--2026-08-17T19:49:13Z.  Charge: 18 integer
review minutes.  No minutes were added to the problem-agent research ledger.
