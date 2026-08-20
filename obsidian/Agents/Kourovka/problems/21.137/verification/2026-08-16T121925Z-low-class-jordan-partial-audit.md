---
title: "Verification — Kourovka 21.137 — low-class and Jordan reductions"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "The class-at-most-p Hall exclusion and the quotient-minimal Jordan/root-fibre reductions are valid necessary conditions for an active-scope counterexample."
claimant: Problem-21.137
target_statement: "For odd p, the actual p-power subgroup of every finite exponent-p^2 p-group is abelian whenever the power-value set is a subgroup."
target_object: "Finite odd-prime p-groups of exact exponent p^2 with closed actual p-power value set"
witness_object: "No witness; symbolic arguments in the target class and its exact-exponent quotients"
verification_method: line-by-line hand proof
tools_used: ["none; computation expressly excluded"]
scope_answered: ["class-at-most-p exclusion", "quotient-minimal structure", "order lower bound p^(p+5)"]
scope_not_answered: ["21.137/odd-prime-exponent-p2"]
active_assignment_answered: no
partial_result_certifiable: yes
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.137

## Verdict

**PASS as a `PARTIAL_RESULT`, subject to the two presentation corrections below.** The Hall argument really includes nilpotency class (p), the (p=3) case passes, exact exponent is preserved in every quotient where it is invoked, and the final hand-derived lower bound is (lvert G\rvert\ge p^{p+5}). No computation or catalogue statement is certified here.

## Hall-polynomial coordinate check

In the torsion-free free nilpotent group on (x,y), Hall collection is filtered by the multidegree counting occurrences of (x) and (y). Induction through the collection process shows that the coordinate of a basic commutator of multidegree ((r,s)) in ([x^m,y^n]) is an integer-valued polynomial (f_b(m,n)) of separate degrees at most (r,s): collection can create that coordinate only from products of lower coordinates whose multidegrees sum to ((r,s)). Hall coordinates are integral for every (m,n\in\mathbb Z), so finite differences give the integral binomial-basis expansion

\[
f_b(m,n)=\sum_{i=0}^{r}\sum_{j=0}^{s}a_{ij}\binom mi\binom nj,
\qquad a_{ij}\in\mathbb Z.
\]

Because ([x^0,y^n]=[x^m,y^0]=1), uniqueness of normal form removes all (i=0) and (j=0) terms. If the class is (c\le p), every mixed commutator has (r+s\le p), hence (1\le r,s\le p-1). Therefore every factor (\binom pi\binom pj) is divisible by (p^2), so every coordinate of ([x^p,y^p]) is a multiple of (p^2). Mapping to a group of exponent dividing (p^2) kills every collected factor.

This validates the coordinate-degree assertion rather than merely assuming an unnamed Hall formula. It also explains the exact boundary: class (p) is covered; at weight (p+1), multidegree ((p,1)) permits (\binom pp\binom p1=p), so this divisibility proof stops.

For (p=3), class at most 3 is included: the possible indices satisfy (i,j\in\{1,2\}), and both (\binom31) and (\binom32) equal 3. The displayed class-3 collection cross-check likewise has only exponents (p^2) and (p\binom p2), both divisible by 9. Thus the earlier conservative class-(<p) threshold can be sharpened to class-(\le p).

## Low-class order consequence

A counterexample must have class at least (p+1). A finite (p)-group of class (c\ge2) has (|G|\ge p^{c+1}): (G/\gamma_2(G)) has order at least (p^2), and the remaining (c-1) nontrivial lower-central factors each have order at least (p). Hence the low-class argument alone gives (|G|\ge p^{p+2}).

## Quotient-minimal reduction and exact exponent

For (N\lhd G), the quotient's actual value set is exactly (PN/N). Choosing a smallest quotient (H) with nonabelian power image (Q) preserves exponent exactly (p^2): a nontrivial (p)-th power survives, whereas a quotient of exponent at most (p) has trivial (p)-power set. Closure is preserved because (QN/N) is the image of the subgroup (P).

The same check applies to (H/C) and (H/D). Since nonabelian (Q) cannot lie in an order-(p) subgroup, its image is nontrivial, so those quotients retain exact exponent (p^2) whenever minimality is invoked.

Choose (C\le Q'\cap Z(H)) of order (p). If (Q/C) were nonabelian, (H/C) would be a smaller selected quotient; hence (Q'=C\cong C_p\le Z(H)), and (Q) has class exactly 2. A distinct order-(p) subgroup (D\le Z(H)) would leave derived image (CD/D\ne1), again contradicting minimality. Thus (C) is the unique order-(p) subgroup of (Z(H)), so (Z(H)) is cyclic of order (p) or (p^2), (Q\cap Z(H)=C), and every nontrivial normal subgroup contains (C). All these deductions pass.

## Jordan-chain reduction

The class-2 exponent-(p) group (Q) has the standard Baer/Lazard Lie algebra over (\mathbb F_p) because (p) is odd. Choose noncentral (a=x^p\in Q), let (A) be conjugation by (x), and (N=A-I). Then

\[
A^p=\operatorname{Inn}(a),\qquad N^p=A^p-I=\pm\operatorname{ad}(a)\ne0,
\]

where the sign depends only on the chosen commutator/adjoint convention and has no effect on rank or dimension. The image is the one-dimensional space (C=Q'). Choose (v) with (N^pv=c\ne0). Since conjugation by (x) fixes (a=x^p) and fixes (C\le Z(H)), (Na=Nc=0). Thus (v,Nv,\ldots,N^pv=c) are (p+1) independent vectors, and the kernel on their span is (\langle c\rangle). The additional fixed vector (a) is independent because it is noncentral. Therefore

\[
\dim Q\ge p+2,\qquad |Q|\ge p^{p+2}.
\]

Since (Q\ne H) (their exponents are (p) and (p^2)), the first index estimate gives (|H|\ge p^{p+3}).

## Root-fibre count and exponents

The fibre above (1) contains all (|Q|) elements of (Q). For each (a\in Q\setminus C), a root (x^p=a) commutes with (\langle a,C\rangle\cong C_p^2), producing at least (p^2) distinct roots. Each of the (p-1) nonidentity values in (C) has at least (p) roots by multiplication by (C). These disjoint fibres give

\[
|H|\ge |Q|+p^2(|Q|-p)+p(p-1)
=(p^2+1)|Q|-p^3+p^2-p.
\]

For nonabelian (Q), (|Q|\ge p^3), so the right side is strictly greater than (p^2|Q|). Since ([H:Q]) is a power of (p), ([H:Q]\ge p^3). Combining with (|Q|\ge p^{p+2}) yields

\[
|G|\ge |H|\ge p^{p+5}.
\]

At (p=3), this is (3^8=6561). The earlier theoretical intermediate exponents are also correct: (p^{p+2}) from class alone and (p^{p+3}) from the Jordan bound plus the first index factor.

## Required presentation corrections

1. Fix a commutator convention before writing (\operatorname{Inn}(a)=I+\operatorname{ad}(a)) and (N^pv=[a,v]); otherwise write the convention-independent (N^p=\pm\operatorname{ad}(a)). The sign does not affect the proof.
2. In the standalone Hall lemma, include the multidegree-preserving collection/finite-difference paragraph above. Calling the separate-degree assertion merely “standard” leaves the key class-(p) step implicit.

## What is NOT established

No argument here kills the first weight-(p+1) Hall layer or proves (Q) abelian in unrestricted class. The active odd-prime scope remains unanswered, and the excluded (p=2), exponent-8 clause is untouched.
