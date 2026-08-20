---
title: "Verification — Kourovka 21.137 — class-p-plus-one Hall lemma"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "For every odd prime p, every group G of exponent dividing p^2 and nilpotency class at most p+1 has commuting p-th powers."
claimant: Problem-21.137
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the actual p-th-power value set P is a subgroup, then P is abelian."
excluded_scopes: ["the general powerfulness clause", "21.137/two-group-exponent-8", "odd-prime groups of exponent other than exactly p^2"]
target_object: "Every finite odd-prime p-group of exact exponent p^2 whose actual p-th-power value set is a subgroup."
witness_object: "The strict additional family of arbitrary groups of exponent dividing p^2 and class at most p+1."
witness_equals_target: false
citation: none
verification_method: "Independent hand proof using truncated Magnus expansions, integral finite differences, elementary class-two collection, and an explicit semidirect quotient."
tools_used: ["GAP 4.12.1 (availability probe only)", "Python 3.12.3 (availability probe only)"]
scope_answered: ["the additional family inside 21.137/odd-prime-exponent-p2 with nilpotency class at most p+1"]
scope_not_answered: ["21.137/odd-prime-exponent-p2 without a class bound", "the general powerfulness clause", "21.137/two-group-exponent-8"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/hall-collection, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.137

## The claim

The submitted partial theorem is correct: if \(p\) is odd, \(\exp(G)\mid p^2\), and \(\operatorname{cl}(G)\le p+1\), then

\[
[x^p,y^p]=1\qquad(x,y\in G).
\]

This is a gap-free hand proof of a strict additional-class family. It does **not** answer the unrestricted active assignment.

Throughout,
\[
[u,v]=u^{-1}v^{-1}uv,\qquad u^v=v^{-1}uv=u[u,v],
\]
and iterated commutators are left-normed.

## Scope, revision, and clause matrix

The rendered source page states three questions. The canonical revision-2 scope selects only the odd-prime exponent-\(p^2\) abelianity clause, and its transcription is faithful.

| source clause | active? | result of this verification |
|---|---:|---|
| If a power-value subgroup in a finite \(p\)-group exists, must it be powerful? | no | not addressed |
| If \(p\ne2\), \(\exp G=p^2\), and the actual \(p\)-th-power values form a subgroup, must it be abelian? | **yes** | proved only with the extra hypothesis \(\operatorname{cl}(G)\le p+1\) |
| If \(G\) is a 2-group of exponent 8 and its squares form a subgroup, must it be abelian? | no | not addressed |

active_assignment_answered: no.

## Constraint-and-conclusion matrix

| constraint_id | role | source requirement | independently checked proof use | result |
|---|---|---|---|---|
| 21.137-odd-forall-p-G | admissibility | every qualifying \(p,G\) | proof has the additional restriction \(\operatorname{cl}(G)\le p+1\) | **fail for unrestricted scope; pass for stated partial family** |
| 21.137-odd-p-not-2 | admissibility | \(p>2\) prime | \(p\mid\binom pi\) for \(0<i<p\), and oddness gives \(p\mid\binom p2\) | pass |
| 21.137-odd-finite-p-group | admissibility | finite \(p\)-group for the same \(p\) | the hand proof applies to arbitrary groups under the stronger-inclusive exponent and class assumptions, hence to source groups in the partial family | pass for partial family |
| 21.137-odd-exponent-p2 | admissibility | exact exponent \(p^2\) | the proof assumes \(\exp G\mid p^2\), which includes exact exponent \(p^2\) | pass |
| 21.137-odd-power-set-definition | admissibility | \(P=\{g^p:g\in G\}\), the actual value set | the conclusion is pairwise commutation of those actual values; \(K=\langle P\rangle\) is only auxiliary | pass |
| 21.137-odd-power-set-subgroup | admissibility | the actual value set \(P\) is a subgroup | unnecessary for pairwise commutation; under the source hypothesis \(P=K\) | pass |
| 21.137-odd-P-abelian | conclusion | \(P\) abelian | established for \(\operatorname{cl}(G)\le p+1\), not above that class | pass for partial family; **unproved unrestricted** |

## Target versus witness

There is no finite computational witness. The source target is an unrestricted class of finite \(p\)-groups, while the proof object is the strict subclass cut out by \(\operatorname{cl}(G)\le p+1\). Thus witness_equals_target is false as classes of objects. The proof nevertheless applies to every source-admissible object lying in that subclass.

## Subclaims and what each method proves

1. A truncated Magnus/Newton argument proves the integral Hall-coordinate formula with the required **separate** degree bounds. It proves the needed divisibilities, but nothing above class \(p+1\).
2. An elementary quotient by \(Z(G)\), followed by class-two collection, proves \(K'\le Z(G)\) and \(\exp K\mid p\) for all products without assuming either conclusion.
3. A Hall-basis count and an explicit semidirect quotient prove uniqueness and coefficient \(+1\) of the multidegree-\((p,1)\) coordinate. This proves membership of that extreme commutator in \(K\), but not class-\(p+2\) isolation.
4. An exhaustive split by weight and multidegree proves that every factor in the final collection dies. It leaves all higher-class groups open.
5. A direct conjugation calculation audits the \(p=3\), class-\(5\) obstruction formula. That calculation diagnoses failure of this method; it neither proves nor disproves the class-\(p+2\) theorem.

## Evidence: independent hand reconstruction

### 1. Separate-degree integral Hall coordinates

Let
\[
N_c=F(X,Y)/\gamma_{c+1}F(X,Y)
\]
be the torsion-free free two-generator nilpotent group of class \(c\), and choose a Hall–Lyndon basis ordered by weight. For a mixed basic commutator \(b\) of multidegree \((r,s)\), write \(f_b(m,n)\) for its exponent in the Hall normal form of \([X^m,Y^n]\).

Here is a direct justification of the assertion that was only stated in the submitted proof. Use the Magnus expansion, truncated above total degree \(c\),
\[
X\longmapsto1+\xi,\qquad Y\longmapsto1+\eta.
\]
For every integer \(m\), the coefficient of \(\xi^i\) in \((1+\xi)^{\pm m}\) is \(\binom{\pm m}{i}\), a polynomial of degree \(i\) in \(m\); the analogous statement holds for \(\eta,n\). Consequently, in the expansion of
\[
[X^m,Y^n]=X^{-m}Y^{-n}X^mY^n,
\]
the coefficient of every associative word containing \(R\) copies of \(\xi\) and \(S\) copies of \(\eta\) is an integer-valued polynomial having degree at most \(R\) in \(m\) and at most \(S\) in \(n\).

The leading Magnus forms of the Hall–Lyndon commutators are unitriangular, with unit diagonal, in their corresponding Hall words. Compare the Magnus expansion with the collected Hall normal form, successively by weight and Hall order. At multidegree \((r,s)\), the new coordinate \(f_b\) occurs with coefficient \(1\). Every contribution built from earlier coordinates is a product whose constituent multidegrees add to \((r,s)\); by induction its separate degrees add to at most \(r,s\). No division is introduced because the comparison is unitriangular. Therefore \(f_b(m,n)\) is an integer-valued polynomial with
\[
\deg_m f_b\le r,\qquad \deg_n f_b\le s.
\]

The two-variable Newton expansion gives
\[
f_b(m,n)=\sum_{i=0}^{r}\sum_{j=0}^{s}
  \Delta_m^i\Delta_n^j f_b(0,0)\binom mi\binom nj.
\]
Every coefficient is an integer because \(f_b\) is integer-valued. Moreover \([X^0,Y^n]=[X^m,Y^0]=1\), and uniqueness of Hall coordinates in \(N_c\) gives \(f_b(0,n)=f_b(m,0)=0\). Hence all zero-index coefficients vanish:
\[
f_b(m,n)=\sum_{i=1}^{r}\sum_{j=1}^{s}
 a_{b,i,j}\binom mi\binom nj,
\qquad a_{b,i,j}\in\mathbb Z. \tag{1}
\]

This proves, rather than assumes, the separate-degree integral Hall assertion.

Take \(c=p+1\). If \(r+s\le p\), then \(1\le r,s\le p-1\). Each summand in \(f_b(p,p)\) contains two binomial factors divisible by \(p\), so \(p^2\mid f_b(p,p)\). After specialization to a group of exponent dividing \(p^2\), all factors of weight at most \(p\) vanish. Thus
\[
[x^p,y^p]\in\gamma_{p+1}(G). \tag{2}
\]

At weight \(p+1\), the same \(p^2\)-divisibility holds unless \((r,s)=(p,1)\) or \((1,p)\). In either exceptional case (1) still supplies one factor \(\binom p1=p\), so the coordinate is divisible by \(p\).

### 2. Why \(K'\le Z(G)\) and why every element of \(K\) has order dividing \(p\)

Put
\[
S=\{g^p:g\in G\},\qquad K=\langle S\rangle.
\]
The identities
\[
(g^p)^{-1}=(g^{-1})^p,\qquad (g^p)^h=(g^h)^p
\]
show that \(S\) is inverse-closed and conjugacy-invariant, so \(K\unlhd G\).

For \(s=x^p,t=y^p\in S\), (2) and the class bound give
\[
[s,t]\in\gamma_{p+1}(G)\le Z(G). \tag{3}
\]
The images of the generating set \(S\) therefore commute in \(K/(K\cap Z(G))\). That quotient is abelian, so
\[
K'\le K\cap Z(G)\le Z(G). \tag{4}
\]
This fills the normal-generation step: centrality of the commutators of the generating set really does imply centrality of the full derived subgroup.

Every \(s\in S\) satisfies \(s^p=1\). By (3),
\[
[s,t]^p=[s^p,t]=1.
\]
Since \(K'\) is centrally generated by these pair commutators, \(\exp K'\mid p\).

Now let \(k\in K\). Because \(S^{-1}=S\), write \(k=s_1\cdots s_n\) with \(s_i\in S\). Induct on \(n\). If \(a=s_1\cdots s_{n-1}\), the induction hypothesis gives \(a^p=1\), while \([s_n,a]\in K'\) has order dividing \(p\). As \(K'\) is central, the exact class-two product formula is
\[
(a s_n)^p=a^p s_n^p [s_n,a]^{\binom p2}=1,
\]
because \(p\mid\binom p2\) for odd \(p\). Hence
\[
\exp K\mid p. \tag{5}
\]
This is an induction on word length, not an assumption about arbitrary products. It is completed before any extreme commutator is shown to lie in \(K\), so there is no circularity.

### 3. Uniqueness and unit coefficient of multidegree \((p,1)\)

Let \(H=G/K\). Normality of \(K\) was established independently above, and
\[
(gK)^p=g^pK=K,
\]
so \(\exp H\mid p\). In \(H\), collect
\[
1=[\bar y,\bar x^p]. \tag{6}
\]

For a Hall factor in (6) having \(X\)-degree \(r<p\), formula (1), evaluated at the \(X\)-parameter \(p\), makes its exponent divisible by \(p\). It dies individually because \(H\) has exponent dividing \(p\). If \(r=p\), the class bound \(r+s\le p+1\) forces \(s=1\); no \(r>p\) factor can occur.

There is exactly one standard Hall basic commutator with \(p\) copies of \(X\) and one copy of \(Y\):
\[
c_p=[Y,{}_{p}X].
\]
Indeed, the only basic commutator containing no \(Y\) is \(X\) itself. Recursing through the Hall definition forces any basic commutator containing exactly one \(Y\) to be \(c_k=[c_{k-1},X]\). Equivalently, the multigraded Witt count is
\[
\frac1{p+1}\binom{p+1}{p,1}=1.
\]

It remains to check that the coordinate in (6) is a **unit**, not an unspecified Hall-polynomial constant. This can be done without assuming that quotienting by two-\(Y\) commutators preserves a coordinate. Let \(A\) be the free abelian group with basis \(e_0,\ldots,e_p\), and let \(X\) act by the integral unitriangular automorphism
\[
e_i^X=e_i e_{i+1}\quad(0\le i<p),\qquad e_p^X=e_p.
\]
Set \(Q=A\rtimes\langle X\rangle\) and \(Y=e_0\). Then \(Q\) is a two-generator nilpotent group of class \(p+1\), every commutator containing at least two copies of \(Y\) is trivial, and
\[
c_i=[Y,{}_{i}X]=e_i.
\]
The \(e_i\) are independent. Induction using \(u^X=u[u,X]\) and Pascal's identity gives
\[
[Y,X^m]=\prod_{i=1}^{p} e_i^{\binom mi}. \tag{7}
\]
Because \(Q\) is a quotient of the free nilpotent group and kills every factor with at least two \(Y\)'s while sending the one-\(Y\) Hall factors \(c_i\) to independent basis elements \(e_i\), (7) reads off the original \(c_p\)-coordinate:
\[
f_{c_p}(m,1)=\binom mp.
\]
At \(m=p\) it is \(\binom pp=1\) (or \(-1\) if the opposite Hall orientation is chosen). Thus every other factor in (6) has already died individually and the sole remaining factor gives
\[
[y,{}_{p}x]\in K. \tag{8}
\]
Swapping \(x,y\) gives the corresponding result for the unique multidegree-\((1,p)\) commutator.

### 4. Exhaustion of all factors in the final collection

Collect \([x^p,y^p]\) in the free nilpotent group of class \(p+1\) and specialize to \(G\). Every basic factor is mixed and has weight at most \(p+1\).

- At weight at most \(p\), both multidegree entries are \(<p\), so its coordinate is divisible by \(p^2\) and the factor dies under \(\exp G\mid p^2\).
- At weight \(p+1\), every non-extreme multidegree again has both entries \(<p\), so the same argument kills it.
- The only remaining multidegrees are \((p,1)\) and \((1,p)\). Their coordinates are divisible by \(p\), their unique underlying basic commutators lie in \(K\) by (8) and its swapped form, and those factors die by \(\exp K\mid p\).
- There is no factor of weight greater than \(p+1\) because of the class bound.

This is exhaustive. Since the Hall expression is already an ordered product and each displayed factor is the identity after specialization, no new weight-\(p+1\) correction can be created by deleting them. Therefore
\[
[x^p,y^p]=1.
\]

### 5. Separate audit of the \(p=3\), class-\(p+2\) obstruction

This calculation is not used above. Suppose only that the class is at most \(5\), and put
\[
c_1=[y,x],\quad c_2=[c_1,x],\quad c_3=[c_2,x],\quad d=[c_2,c_1].
\]
The element \(d\) has weight \(5\) and is central. Directly from \(u^x=u[u,x]\),
\[
y^x=yc_1,\qquad y^{x^2}=yc_1^2c_2,
\]
and
\[
y^{x^3}=y c_1(c_1c_2)^2(c_2c_3).
\]
Using \(c_2c_1=c_1c_2[c_2,c_1]=c_1c_2d\), and noting that every further commutator required to move \(c_3\) has weight above \(5\), this collects exactly to
\[
y^{x^3}=y c_1^3c_2^3c_3d.
\]
Hence, with the stated convention and definition of \(d\), the sign is positive:
\[
[y,x^3]=c_1^3c_2^3c_3d. \tag{9}
\]
In an exponent-\(3\) quotient, \(x^3=1\) and \(c_1^3=c_2^3=1\), so (9) gives only \(c_3d=1\). It does not isolate \(c_3\). Here \(c_3\) has multidegree \((3,1)\) and \(d\) has multidegree \((3,2)\). Thus the claimed contamination formula is correct, but it does not show that either factor is nontrivial and does not refute a class-\(p+2\) statement.

For general odd \(p\), the multidegree-\((p,2)\) free-Lie rank is
\[
\frac1{p+2}\binom{p+2}{p,2}=\frac{p+1}{2},
\]
because \(\gcd(p,2)=1\). Formula (1) permits an \(X\)-index-\(p\), \(Y\)-index-\(1\) term, so Hall divisibility alone cannot remove this layer.

## Tool and command record

No mathematical computation and no web or literature search were performed. The proof above was reconstructed by hand from only the assigned source image, canonical scope, submitted findings, and submitted log.

Availability probe, verbatim:

    $ for tool in gap sage python3 magma; do command -v "$tool" || true; done
    /usr/bin/gap
    /usr/bin/python3
    $ python3 --version
    Python 3.12.3
    $ gap -q -c 'Print(GAPInfo.Version,"\n"); QUIT;'
    4.12.1

## Verdict

**Mathematical result:** the submitted class-at-most-\(p+1\) partial lemma survives hostile line-by-line reconstruction. The proof is gap-free after supplying the Magnus/Newton derivation and the explicit semidirect-quotient argument above. The separate \(p=3\) obstruction formula is also correct under the stated convention.

**Current certification tag:** status/conjectured. The common protocol permits status/proven only after the human has seen the checked proof. I therefore do not alter the claimant's tag in this clean validation pass. This administrative hold does not indicate a mathematical gap.

**Active scope:** active_assignment_answered: no. The unrestricted odd-prime exponent-\(p^2\) question remains open.

## Why this verdict

Each vulnerable dependency was reconstructed independently: integral separate-degree bounds; passage from generator commutators to \(K'\le Z(G)\); exponent \(p\) for arbitrary products in \(K\); uniqueness and unit coefficient of the extreme coordinate; and an exhaustive terminal collection. None uses closure of the actual power-value set, none assumes \(\exp K\mid p\) before proving it, and no quotient-coordinate uniqueness is smuggled into the argument.

## What is NOT established

- No group of class greater than \(p+1\) is covered.
- The unrestricted active assignment is not answered.
- The class-\(p+2\) statement is neither proved nor refuted; only this isolation method is shown to fail there.
- The general powerfulness clause and the separate exponent-8 two-group clause are untouched.
- No literature or staleness conclusion is made in this discovery-blind validation.

## What would upgrade it

After the human has seen this checked proof, Validator may change the **partial lemma's** certification tag to status/proven. That upgrade would certify only the additional class-at-most-\(p+1\) theorem and would not close or retire 21.137/odd-prime-exponent-p2.
