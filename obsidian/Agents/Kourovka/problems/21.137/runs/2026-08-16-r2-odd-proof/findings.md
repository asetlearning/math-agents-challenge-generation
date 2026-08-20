---
title: "Partial result for 21.137: low-class exclusion and affine lower bound"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/power-maps
  - project/kourovka
  - status/conjectured
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
outcome: PARTIAL_RESULT
active_assignment_answered: no
strategy_status: exhausted
ended_utc: 2026-08-16T12:55:52Z
active_minutes_used: 64
---

# Partial result: low-class exclusion and structure of a minimal counterexample

## Active target

Scope: `21.137/odd-prime-exponent-p2`

Assignment revision: 2

Target statement: Let \(p\) be an odd prime and \(G\) a finite \(p\)-group of exponent exactly \(p^2\). If the set \(P=\{g^p:g\in G\}\) of \(p\)-th powers is a subgroup of \(G\), then \(P\) is abelian.

## Partial-result statement

The active target remains unanswered. The following narrower assertions are submitted for independent checking.

Review state: Validator and Lead accepted items 1–6 as structural partial results. The active assignment remains unanswered.

1. If \(G\) has exponent dividing \(p^2\) and nilpotency class at most \(p\), then all \(p\)-th powers commute; the value-set closure hypothesis is not needed in this class-bounded family.
2. If a counterexample to the active target exists, it has a quotient \(H\) whose actual power subgroup \(Q\) satisfies
   \[
   \exp Q=p,\qquad Q'=C\cong C_p\le Z(H),
   \]
   where \(C\) is the unique order-\(p\) subgroup of \(Z(H)\).
3. Writing \(|Q|=p^m\), one has \(m\ge p+2\) and
   \[
   [H:Q]\ge p^{m-\lfloor(m-1)/p\rfloor}.
   \]
   Consequently every counterexample must satisfy
   \[
   |G|\ge p^{2p+3}.
   \]
4. In the quotient-minimal model, any two \(p\)-th powers whose roots lie in the same coset of \(Q\) commute.
5. A common-flag argument gives the further structural restriction
   \[
   \dim_{\mathbb F_p}Z(Q)\ge p,
   \]
   which in particular excludes an extraspecial minimal power subgroup.
6. Power values whose root cosets lie in one cyclic subgroup of \(H/Q\) commute. In particular, if \(u=x^p\), \(uv=z^p\), and \(zQ\in\langle xQ\rangle\), then \([u,v]=1\).

These are reductions and exclusions only. They do not prove \(P\) abelian in arbitrary nilpotency class.

## Fixed conventions

Throughout,
\[
[u,v]=u^{-1}v^{-1}uv,
\qquad u^v=v^{-1}uv,
\]
and higher commutators are left-normed. On a class-2 exponent-\(p\) group, the associated Lie bracket uses the logarithm of this group commutator. For right conjugation by \(a\), define
\[
D_a(v)=[v,a]_{L};
\]
then conjugation by \(a\) on the class-2 Lie algebra is \(I+D_a\).

## 1. Elementary consequences of actual-value closure

Assume the active hypotheses. Since the actual value set \(P\) is a subgroup containing every \(p\)-th power,
\[
P=G^p.
\]
For \(u=g^p\in P\),
\[
u^p=g^{p^2}=1.
\]
Exact exponent of \(G\) supplies a nontrivial \(p\)-th power, so \(P\) has exponent exactly \(p\).

If \(N\unlhd G\), the actual value set in the quotient is exactly
\[
\{(gN)^p:g\in G\}=PN/N,
\]
which is a subgroup. The quotient has exponent \(p\) precisely when \(P\le N\); otherwise it retains exact exponent \(p^2\). This is the quotient-inheritance fact used below.

## 2. Hall multidegree proof for class at most \(p\)

Let \(G\) have exponent dividing \(p^2\) and class \(c\le p\); no value-set hypothesis is needed. Fix \(x,y\in G\).

Work in the torsion-free free nilpotent group \(F_{2,c}\) on \(X,Y\), with an ordered Hall basis. If a basic commutator \(b\) contains \(r\ge1\) copies of \(X\) and \(s\ge1\) copies of \(Y\), its exponent in the collected form of \([X^m,Y^n]\) is an integer-valued Hall polynomial \(f_b(m,n)\) of separate degrees at most \(r\) and \(s\).

For completeness, the multidegree part of the collection theorem says that collection at the coordinate of multidegree \((r,s)\) uses at most \(r\) choices among the \(X\)-copies and at most \(s\) choices among the \(Y\)-copies. Equivalently, its \((r+1)\)-st finite difference in \(m\) and its \((s+1)\)-st finite difference in \(n\) vanish. Every integer-valued polynomial with those separate degree bounds has a unique integral binomial-basis expansion. Since the whole commutator is the identity when either exponent is zero, uniqueness of Hall coordinates removes the terms with binomial index zero. Thus
\[
f_b(m,n)=
\sum_{i=1}^{r}\sum_{j=1}^{s}
a_{ij}\binom mi\binom nj,
\qquad a_{ij}\in\mathbb Z.
\]

Here \(r+s\le c\le p\). Because \(r,s\ge1\), both are at most \(p-1\). For \(1\le i,j\le p-1\), both \(\binom pi\) and \(\binom pj\) are divisible by \(p\). Hence every \(f_b(p,p)\) is divisible by \(p^2\). Mapping \(F_{2,c}\) to \(\langle x,y\rangle\), every factor in the collected form of \([x^p,y^p]\) is raised to a multiple of \(p^2\), so every factor is trivial. Therefore
\[
[x^p,y^p]=1.
\]

At \(p=3\), the allowed positive multidegrees have total at most 3: \((1,1),(2,1),(1,2)\). The same binomial-basis calculation gives a factor 9 in every coordinate, so the endpoint \(c=p=3\) is included; no division by 3 occurs.

## 3. Quotient-minimal structure

If a counterexample exists, choose a quotient \(H\) of smallest order whose actual power set \(Q\) remains a nonabelian subgroup. Then \(Q=H^p\) and \(\exp Q=p\).

The nontrivial subgroup \(Q'\) is normal in the finite \(p\)-group \(H\), so choose \(C\le Q'\cap Z(H)\) of order \(p\). Since the nonabelian \(Q\) is not contained in \(C\), the quotient \(H/C\) retains exact exponent \(p^2\), and its actual power subgroup is \(Q/C\). Quotient minimality makes \(Q/C\) abelian. Thus
\[
Q'=C\cong C_p\le Z(H).
\]

If \(D\le Z(H)\) also has order \(p\) and \(D\ne C\), then \(H/D\) retains exact exponent \(p^2\), while
\[
(QD/D)'=CD/D\ne1.
\]
That would be a smaller counterexample. Hence \(C\) is the unique order-\(p\) subgroup of \(Z(H)\). It follows that \(Z(H)\) is cyclic of order \(p\) or \(p^2\), that \(Q\cap Z(H)=C\), and that every nontrivial normal subgroup of \(H\) contains \(C\).

## 4. One noncentral root forces \(m\ge p+2\)

Choose \(a\in Q\setminus Z(Q)\), and choose \(x\in H\) with \(x^p=a\). Because \(p\) is odd, the class-2 exponent-\(p\) group \(Q\) has its standard BCH Lie algebra \(L\) over \(\mathbb F_p\), with \(\dim L=m=\log_p|Q|\).

Let \(A\) be right conjugation by \(x\) on \(L\), and let \(N=A-I\). Then
\[
A^p=I+D_a,
\qquad N^p=(A-I)^p=D_a\ne0.
\]
The image of \(D_a\) is the one-dimensional derived algebra \(C\). Choose \(v\) with \(N^pv=c\ne0\). Conjugation by \(x\) fixes both \(a=x^p\) and \(C\le Z(H)\), so \(Na=Nc=0\). Hence
\[
v,Nv,\ldots,N^pv=c
\]
is a Jordan chain of length \(p+1\). The fixed noncentral vector \(a\) is independent of this chain: the kernel within the chain is spanned by the central endpoint \(c\). Therefore
\[
m\ge p+2.
\]

## 5. Simultaneous roots give the affine covering bound

Fix a coset \(xQ\), put \(a=x^p\), and let \(A\) act on
\[
V=Q/C\cong\mathbb F_p^{m-1}.
\]
Since \(A^p\) is conjugation by \(a\), it is the identity on the abelian group \(Q/C\); thus \(N^p=0\) on \(V\).

For \(q\in Q\), direct multiplication gives
\[
(xq)^p=x^p q^{x^{p-1}}q^{x^{p-2}}\cdots q^xq.
\]
In additive notation modulo \(C\),
\[
\overline{(xq)^p}
=\bar a+(I+A+\cdots+A^{p-1})\bar q
=\bar a+N^{p-1}\bar q,
\]
using \(1+T+\cdots+T^{p-1}=(T-I)^{p-1}\) over \(\mathbb F_p\).

All Jordan blocks of \(N\) have size at most \(p\), so
\[
\operatorname{rank}N^{p-1}
\le\left\lfloor\frac{m-1}{p}\right\rfloor.
\]
One coset contributes at most \(p^{\lfloor(m-1)/p\rfloor}\) projected values and therefore at most \(p^{\lfloor(m-1)/p\rfloor+1}\) actual values, because \(|C|=p\). The identity coset \(Q\), however, contributes only the value \(1\), since \(\exp Q=p\). Put \(k=\lfloor(m-1)/p\rfloor\), \(M=p^{k+1}\), and \(r=[H:Q]\). Covering all of \(Q\) gives the sharper inequality
\[
p^m\le1+(r-1)M.
\]
The weaker bound \(r\ge p^{m-1-k}\) cannot be an equality, because it would make the right side \(p^m-M+1<p^m\). Since \(r\) is a power of \(p\),
\[
r\ge p^{m-k}=p^{m-\lfloor(m-1)/p\rfloor}.
\]
Combining this with \(m\ge p+2\), and noting that
\[
2m-\left\lfloor\frac{m-1}{p}\right\rfloor
\]
is increasing in integral \(m\), yields
\[
|G|\ge|H|\ge p^{2p+3}.
\]

## 6. Same-coset commutativity

On the full Lie algebra, \(N^p=D_a\). Since \(A\) fixes \(a\) and fixes \(C\) pointwise,
\[
N^{p+1}=0.
\]
On \(U=Q/Z(Q)\), the commutator form is nondegenerate alternating and is preserved by \(A\). The adjoint of \(N=A-I\) is
\[
N^*=A^{-1}-I=-A^{-1}N.
\]
Thus \((\operatorname{im}N^i)^\perp=\ker N^i\). For \(i=p-1\), the relation \(N^{p+1}=0\) and \(2p-2\ge p+1\) show
\[
\operatorname{im}N^{p-1}\le\ker N^{p-1},
\]
so this image is totally isotropic. Also
\[
D_aN^{p-1}=N^{2p-1}=0.
\]
The affine image \(\bar a+\operatorname{im}N^{p-1}\) is therefore a commuting subset modulo the central subgroup, and changes by \(C\) do not affect commutators. Any two power values with roots in the same coset \(xQ\) commute.

## 7. Common root-action flag and the center

Let \(S\) be the finite \(p\)-subgroup of \(\operatorname{Aut}(L)\) induced by \(H\). Over \(\mathbb F_p\), it admits a complete common invariant flag
\[
0=F_0<F_1<\cdots<F_m=L,
\qquad (A-I)F_i\le F_{i-1}\quad(A\in S).
\]
For every \(a\in Q\), choose \(x^p=a\) and let \(N=A_x-I\). Then \(N^p=D_a\). If \(v\in F_p\), flag lowering gives
\[
D_a(v)=N^pv=0
\]
for every \(a\in Q\). Hence \(F_p\le Z(Q)\), and
\[
\dim_{\mathbb F_p}Z(Q)\ge p.
\]
Since \(Q/Z(Q)\) is a nonzero symplectic space, it has dimension at least 2, recovering \(m\ge p+2\). In particular \(Z(Q)\ne Q'=C\), so a quotient-minimal counterexample cannot have an extraspecial power subgroup.

## 8. Cyclic root cosets and a cross-pairing criterion

Let \(xQ\ne Q\), put \(a=x^p\), and let \(A=I+N\) act on the relevant quotient. For \(1\le j\le p-1\),
\[
(x^j)^p=a^j,
\qquad
A^j-I=N\bigl(jI+\tbinom j2N+\cdots\bigr).
\]
The parenthesized factor is invertible and commutes with \(N\), so
\[
\operatorname{im}(A^j-I)^{p-1}
=\operatorname{im}N^{p-1}.
\]
All power values rooted over the cyclic subgroup \(\langle xQ\rangle\) therefore project into the isotropic span of \(a\) and \(\operatorname{im}N^{p-1}\); central changes do not affect commutators. They commute pairwise.

Consequently, if \(u=x^p\) and \(uv=z^p\) with \(zQ\in\langle xQ\rangle\), then \(u\) commutes with \(uv\), and class 2 gives
\[
[u,v]=[u,uv]=1.
\]
The symmetric statement holds relative to a root coset for \(v\). Closure alone does not force this cyclic incidence.

## 9. Why compatible roots do not close the gap

For compatible roots \(a=x^p\), \(b=y^p\), and \(ab=z^p\), write their Lie logarithms in \(Q\) as \(u,v,u+v+\tfrac12[u,v]\). The induced root actions satisfy
\[
(A_z-I)^p
=D_{u+v+\frac12[u,v]}
=D_u+D_v
=(A_x-I)^p+(A_y-I)^p.
\]
The cross-pairing \([u,v]\in C\) disappears because central elements induce the zero inner derivation. Equivalently, in Hall form \(z=xyt\) with an unconstrained coset for \(t\), and its independent coordinates can absorb the first extreme-multidegree obstruction. The compatible-root comparison therefore reaches the stated cyclic-incidence criterion but does not prove that incidence from closure. This is the kill point for the affine/Hall/action proof representation.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | use in this partial result | evidence | result |
|---|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | all qualifying \(p,G\) | The reductions and necessary bounds are uniform in every odd prime and every qualifying group. | Sections 1–8 | pass for partial scope |
| `21.137-odd-p-not-2` | admissibility | \(p>2\) prime | Oddness is used in the class-2 BCH/Lie structure; \(p=3\) is audited separately in Hall collection. | Sections 2 and 4 | pass |
| `21.137-odd-finite-p-group` | admissibility | finite \(p\)-group | Finiteness supplies quotient-minimality and central order-\(p\) subgroups. | Section 3 | pass |
| `21.137-odd-exponent-p2` | admissibility | exact exponent \(p^2\) | Gives \(\exp P=p\) and controls which quotients retain exact exponent. | Sections 1 and 3 | pass |
| `21.137-odd-power-set-definition` | admissibility | actual values, not only generated subgroup | Used for root-surjectivity and the coset covering of all \(Q\). | Sections 1, 4, and 5 | pass |
| `21.137-odd-power-set-subgroup` | admissibility | actual value set is a subgroup | Gives \(P=G^p\), exponent \(p\), and quotient inheritance. | Section 1 | pass |
| `21.137-odd-P-abelian` | target conclusion | \(P\) abelian | Established only for class at most \(p\); arbitrary high class remains open. | Section 2 and “What this does not establish” | **not proved** |

## Procedural computation note

The run log preserves exploratory GAP outputs from two bounded SmallGroups screens. Lead later corrected that every GAP/enumeration command requires a lease. Those runs were unleased and are procedurally provisional; no computational coverage claim is part of this partial-result proof.

## What this does not establish

- It does not prove the active target for groups of class greater than \(p\).
- It does not show that a counterexample of order \(p^{2p+3}\), or of any order, exists.
- A sufficiently large family of commuting affine power images can cover a nonabelian class-2 group; the covering bound alone gives no contradiction.
- The automorphism-quotient reformulation has an abelian power subgroup and therefore does not recursively produce a smaller counterexample.
- The common-flag center bound does not rule out \(\dim Z(Q)\ge p\); the sharp-center case remains structurally possible at the level of one root action.

## How this could be wrong

1. The Hall proof would fail if the stated separate multidegree bounds for collected coordinates were not applied in a torsion-free free nilpotent group before specialization.
2. A sign mismatch between group conjugation and the Lie adjoint could change \(D_a\) to \(-D_a\); the Jordan and rank conclusions survive, but the fixed convention must be kept throughout.
3. The affine count would be overstated if values from one coset had more than \(p\) lifts over one element of \(Q/C\); they cannot, because \(|C|=p\), but this is a key counting row.
4. Same-coset commutativity uses the nondegenerate form only after quotienting by all of \(Z(Q)\); applying the adjoint argument directly to the degenerate form on \(Q/C\) would be invalid.
5. The common-flag argument requires one flag invariant under the entire p-subgroup of root actions, not a separately chosen flag for each root.

## Evidence and review state

The UTC working log, exact source audit, complete derivations, messages, scripts, and real outputs are in `Agents/Kourovka/problems/21.137/runs/2026-08-16-r2-odd-proof/`. Validator and Lead accepted the class-\(\le p\) theorem, quotient-minimal reduction, \(p^{2p+3}\) affine bound, same- and cyclic-root-coset commutativity, cross-pairing incidence statement, and common-flag center bound as structural partial results. Status remains `status/conjectured`; `active_assignment_answered: no`.

## Final cycle disposition

Outcome: `PARTIAL_RESULT` after 64 active minutes (including final packaging). Lead ordered the affine/Hall/action proof representation stopped after its compatible-root comparison met the stated kill criterion. No new proof or counterexample strategy was begun in this clean proof context. The uncovered case is the full class-greater-than-\(p\) scope subject to all original odd-prime, finite, exact-exponent, and actual-value-set hypotheses.
