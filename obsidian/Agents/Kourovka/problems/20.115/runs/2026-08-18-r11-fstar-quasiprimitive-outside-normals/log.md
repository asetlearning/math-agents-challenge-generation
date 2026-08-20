---
title: "Problem 20.115 proof refinement: generalized Fitting structure"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
strategy: FSTAR-QUASIPRIMITIVE-OUTSIDE-NORMALS
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
---

# Generalized Fitting structure outside proper normal subgroups

## Active-time ledger

- Work start: `2026-08-18T04:31:37Z`; inherited detailed cumulative active time: `01:53:36`.
- Increment cap: 45 active minutes. Safety stop: `2026-08-18T05:31:37Z`.

## Scope and independence gate

The unchanged target is the exact universal implication for every finite \(G\), ordinary \(\chi\in\operatorname{Irr}(G)\), and \(x\in G\):

\[
\chi(x)\ne0\Longrightarrow o_G(x)\chi(1)\mid |G|.
\]

All six canonical constraints remain. The prior `PARTIAL_RESULT` is unreviewed and is not taken as a premise; every prerequisite used below will be rederived. No unreviewed `SU_3(8)` scan is read or used.

## Strategy portfolio

1. **Generalized-Fitting route (selected).** Re-derive faithful quasiprimitivity, then analyze \(F(G)\), the layer \(E(G)\), and \(F^*(G)=F(G)E(G)\). Seek a primewise factorization of \(o(x)\chi(1)\) or a reduction to one component modulo the center.
2. **Component tensor route (selected second).** Use homogeneous restriction to each component and commuting-component tensor structure; test whether multiple components force an imprimitive/tensor-induced reduction or yield independent order-degree factors.
3. **Central almost-simple quotient route.** If \(F^*(G)\) has one component, test whether \(C_G(F^*(G))\le F^*(G)\) and the outer action reduce \(G/Z(G)\) to almost simple, with every center/order lift accounted for.
4. **Catalogue mode (rejected).** Bounded tables cannot justify a universal Fitting reduction.

Certificate plan: every structural step states the exact standard theorem used and separately audits element-order lift through centers and kernels. Kill immediately if the step needs an unstated classification theorem, if the central order lift does not multiply, or if homogeneous restriction supplies no usable degree divisor.

## Re-derivation of prerequisites used in this refinement

Assume the target fails and choose \(G\) of least order admitting a pair

\[
\chi\in\operatorname{Irr}(G),\qquad x\in G,\qquad
\chi(x)\ne0,\qquad o(x)\chi(1)\nmid|G|.
\]

Then the target holds, with all its quantifiers, in every finite group of order below \(|G|\).
The source's known solvable case excludes solvable \(G\); it is used only as this base-case exclusion, not as a universal argument.

### Primitive

If \(\chi=\operatorname{Ind}_H^G\psi\) with \(H<G\), the exact formula

\[
\chi(x)=\sum_{\substack{gH\in G/H\\g^{-1}xg\in H}}
\psi(g^{-1}xg)
\]

has a nonzero summand. The inducing genuine character is automatically irreducible: otherwise its nonnegative irreducible decomposition induces to a decomposition of \(\chi\). For \(y=g^{-1}xg\) with \(\psi(y)\ne0\), minimality gives \(o(y)\psi(1)\mid|H|\), and multiplication by \([G:H]\) contradicts the chosen failure. Thus \(\chi\) is primitive. Cancellation cannot affect the existence of a nonzero summand.

### Faithful

Let \(K=\ker\chi\), \(n=o_G(x)\), and \(m=o_{G/K}(xK)\). The deflated character is nonzero at \(xK\). Moreover \(m\mid n\), \(x^m\in K\), and \(o(x^m)=n/m\mid|K|\). If \(K\ne1\), minimality in \(G/K\) gives \(m\chi(1)\mid|G/K|\), and multiplication yields \(n\chi(1)\mid|G|\), impossible. Hence \(\chi\) is faithful.

### Quasiprimitive and normally generated

For \(N\trianglelefteq G\) and \(\theta\in\operatorname{Irr}(N)\) below \(\chi\), let \(I=I_G(\theta)\). Clifford correspondence gives an irreducible character of \(I\) inducing to \(\chi\); primitivity forces \(I=G\). Hence

\[
\chi_N=e_N\theta
\]

with \(\theta\) \(G\)-invariant. The multiplicity \(e_N\) is the degree of an irreducible projective representation of \(G/N\). Lift its finite-order factor set to a finite central extension with cyclic kernel \(C\). Itô's theorem for the abelian normal subgroup \(C\) gives

\[
e_N\mid[G:N].
\]

Faithfulness of \(\chi\) makes \(\theta\) faithful. If \(x\in N<G\), then \(\theta(x)\ne0\), minimality gives \(o(x)\theta(1)\mid|N|\), and multiplying by \(e_N\mid[G:N]\) contradicts the chosen failure. Therefore

\[
\langle x^G\rangle=G.
\]

Finally, if \(A\trianglelefteq G\) is abelian, \(\chi_A=e_A\lambda\) with \(\lambda\) faithful, linear, and \(G\)-invariant. Hence \(A\) is cyclic and invariance plus faithfulness makes \(A\le Z(G)\). In particular all abelian normal subgroups are cyclic central. These are rederived candidate consequences, not imported review verdicts.

## Generalized Fitting analysis

Write

\[
F=F(G),\qquad E=E(G),\qquad F^*=F^*(G)=FE.
\]

The standard generalized-Fitting facts used here are:

- \(F\) and \(E\) are characteristic in \(G\);
- \(E\) is the central product of the components, distinct components commute, and each component is quasisimple;
- \([F,E]=1\), \(F\cap E=Z(E)\);
- \(C_G(F^*)\le F^*\).

No classification of simple groups is used in these facts.

Because \(Z(F)\) is characteristic in \(F\), it is abelian normal in \(G\), hence \(Z(F)\le Z(G)\). Conversely \(Z(G)\) is nilpotent normal, so \(Z(G)\le F\), and therefore \(Z(G)\le Z(F)\). Thus

\[
Z(F)=Z(G),
\]

and this group is cyclic. The same argument gives \(Z(E)\le Z(G)\). Since \(Z(F^*)\) is characteristic in \(F^*\), it too is abelian normal in \(G\), while \(Z(G)\le F^*\); hence

\[
Z(F^*)=Z(G).
\]

If \(F\) is abelian, the earlier abelian-normal argument gives \(F\le Z(G)\), so \(F=Z(G)\). Therefore the Fitting alternatives are exact:

1. \(F=Z(G)\); or
2. \(F\) contains a noncentral normal \(p\)-subgroup. Its center, and every abelian characteristic subgroup of it, is cyclic central.

Advancing from alternative 2 to the usual “symplectic-type” description requires the classification theorem for finite \(p\)-groups whose characteristic abelian subgroups are cyclic. That theorem and its hypotheses were not supplied here, so this branch meets the stated classification kill criterion; I do not import the description.

If \(F=Z(G)\) and \(E=1\), then \(F^*=Z(G)\). Since \(Z(G)\) is central,

\[
G=C_G(Z(G))=C_G(F^*)\le F^*=Z(G),
\]

making \(G\) abelian, contrary to the nonsolvable least-counterexample configuration. Hence under \(F=Z(G)\), the layer \(E\) is nontrivial.

### Component restriction

Since \(E\trianglelefteq G\), quasiprimitivity gives

\[
\chi_E=e_E\theta,\qquad
\theta\in\operatorname{Irr}(E)\text{ faithful and \(G\)-invariant},\qquad
e_E\mid[G:E].
\]

Let \(L_1,\dots,L_t\) be the components. An irreducible representation of their central product pulls back to a tensor product

\[
\theta_1\otimes\cdots\otimes\theta_t
\]

on \(L_1\times\cdots\times L_t\), with compatible scalar characters on the central kernel. Consequently

\[
\theta(1)=\prod_{i=1}^t\theta_i(1).
\]

The \(G\)-invariance of \(\theta\) sends \(\theta_i\) to the corresponding conjugate character when \(G\) permutes components. This is only tensor homogeneity; it supplies no value formula for an element outside \(E\).

For each component, Itô's theorem applied to \(Z(L_i)\trianglelefteq L_i\) gives

\[
\theta_i(1)\mid|L_i:Z(L_i)|.
\]

Since \(E/Z(E)\cong\prod_i L_i/Z(L_i)\),

\[
\theta(1)\mid|E:Z(E)|.
\]

Together with \(e_E\mid[G:E]\), this recovers the degree divisor

\[
\chi(1)\mid\frac{|G|}{|Z(E)|}.
\]

This is genuine primewise degree control, but it contains no factor from \(o(x)\). When \(E<G\), normal generation gives \(x\notin E\), so \(\chi(x)\ne0\) does not imply nonvanishing of any \(\theta(y)\) for \(y\in E\).

### Exact one-component reduction

Assume the structurally clean branch

\[
F(G)=Z(G)\quad\text{and}\quad E(G)=L
\]

for one component \(L\). Then \(F^*=Z(G)L\). If \(g\in C_G(L)\), it also centralizes \(Z(G)\), hence centralizes \(F^*\), so \(g\in F^*\). Inside \(Z(G)L\), the centralizer of \(L\) is \(Z(G)Z(L)=Z(G)\). Therefore

\[
C_G(L)=Z(G).
\]

Conjugation embeds \(G/Z(G)\) into \(\operatorname{Aut}(L)\). It also acts faithfully on \(S=L/Z(L)\): if \(g\) acts trivially on \(S\), then \(l\mapsto[l,g]\) is a homomorphism from the perfect group \(L\) to \(Z(L)\), hence is trivial, so \(g\in C_G(L)=Z(G)\). The image on \(S\) contains the inner automorphism group

\[
L/Z(L)\cong LZ(G)/Z(G),
\]

which is nonabelian simple. Hence

\[
G/Z(G)\le\operatorname{Aut}(S)
\quad\text{is almost simple with socle }S=L/Z(L).
\]

This is an exact central almost-simple reduction in the one-component, central-Fitting branch. It uses only the self-centralizing property of \(F^*\), not a CFSG classification list.

If \(E\) has at least two components, the same argument gives \(C_G(E)=Z(G)\) and embeds \(G/Z(G)\) into the automorphism group of the central product \(E\), whose quotient \(E/Z(E)\) is a direct product of at least two nonabelian simple groups. Excluding this product-type branch would require additional tensor/permutation analysis; primitivity alone does not exclude it (tensor-product primitive representations exist).

## Cyclic central-product closure — primewise calculation

The center-loss problem can be controlled when the **whole group** is a central product. Let

\[
G=AB,\qquad [A,B]=1,\qquad C=A\cap B\le Z(G),
\]

assume \(C\) is cyclic, and assume the target property holds in both \(A\) and \(B\). Let \(\chi\in\operatorname{Irr}(G)\). Pullback along \(A\times B\to G\) gives

\[
\widetilde\chi=\alpha\otimes\beta
\]

for \(\alpha\in\operatorname{Irr}(A)\), \(\beta\in\operatorname{Irr}(B)\), with compatible central characters; in particular \(\chi(1)=\alpha(1)\beta(1)\).

Write \(x=ab\). If \(\chi(x)\ne0\), then \(\alpha(a)\ne0\) and \(\beta(b)\ne0\). Fix a prime \(p\), let \(C_p\) be the cyclic Sylow \(p\)-subgroup of \(C\), and write \(|C_p|=p^k\). For every \(c\in C_p\), central scalar action gives

\[
\alpha(ac)\ne0,\qquad \beta(c^{-1}b)\ne0.
\]

Set

\[
u_A=v_p\!\left(\frac{|A|}{\alpha(1)}\right),\qquad
u_B=v_p\!\left(\frac{|B|}{\beta(1)}\right),
\]

and

\[
R_A=\max_{c\in C_p}v_p(o(ac)),\qquad
R_B=\max_{c\in C_p}v_p(o(c^{-1}b)).
\]

The target in the two factors, applied for every central shift, gives

\[
R_A\le u_A,\qquad R_B\le u_B.
\]

Both \(R_A\) and \(R_B\) are at least \(k\). For example, in the abelian \(p\)-group generated by the \(p\)-part of \(a\) and \(C_p\), if every member of the coset \(a_pC_p\) had exponent at most \(p^{k-1}\), then the quotient of any two coset members would too, contradicting that \(C_p\) contains an element of order \(p^k\).

Let \(q=v_p(o(ab))\). For every \(c\in C_p\), the commuting elements \(ac\) and \(c^{-1}b\) have product \(ab\), so

\[
q\le
\max\!\bigl(v_p(o(ac)),v_p(o(c^{-1}b))\bigr)
\le\max(R_A,R_B).
\]

Since \(\min(R_A,R_B)\ge k\),

\[
u_A+u_B\ge R_A+R_B\ge q+k.
\]

Finally,

\[
v_p\!\left(\frac{|G|}{\chi(1)}\right)
=u_A+u_B-k
\ge q,
\]

because \(|G|=|A||B|/|C|\). This holds for every prime \(p\), so

\[
o(x)\chi(1)\mid|G|.
\]

Therefore the target property is closed under cyclic central products. In the least-counterexample configuration every abelian normal subgroup, hence every central intersection \(A\cap B\), is cyclic. Consequently \(G\) cannot be a central product of two proper commuting normal subgroups.

### Consequence when \(F^*(G)=G\)

If \(G=F^*=FE\), the cyclic central-product closure excludes the case in which both \(F\) and \(E\) are proper. The alternative \(F=G\) would make \(G\) nilpotent and hence solvable. Thus \(E=G\).

Now \(G=E\) is the central product of its components. Inside \(E\), each component is normal: it is normalized by itself and centralized by all other components. If there were at least two components, one component and the product of the rest would be proper commuting normal subgroups with cyclic central intersection, again contradicting central-product closure. Hence

\[
F^*(G)=G\quad\Longrightarrow\quad
G\text{ is quasisimple}.
\]

This is an unconditional exact reduction for the \(F^*=G\) branch and uses no classification list.

## Order and value audit outside \(F^*(G)\)

Put \(N=F^*(G)\). If \(N<G\), normal generation forces \(x\notin N\). Let

\[
m=o_{G/N}(xN),\qquad n=o_G(x),\qquad y=x^m\in N.
\]

Then \(m\mid n\) and \(o_N(y)=n/m\). Thus the element-order lift itself is exact. The obstruction is the character value.

The invariant constituent \(\theta\) admits the standard character-triple realization: a projective representation \(P\) of \(G\), restricting to a representation affording \(\theta\) on \(N\), and an irreducible projective representation \(T\) of \(G/N\) with reciprocal factor set, such that a representation affording \(\chi\) is \(P\otimes T\). Hence

\[
\chi(x)=\operatorname{tr}P(x)\,\operatorname{tr}T(xN).
\]

Nonvanishing gives both projective traces nonzero. But it does **not** give

\[
\theta(x^m)=\operatorname{tr}P(x^m)
=c\,\operatorname{tr}\!\bigl(P(x)^m\bigr)\ne0.
\]

Here \(c\ne0\) is the relevant cocycle scalar. Even for \(D=\operatorname{diag}(1,i)\), \(\operatorname{tr}D=1+i\ne0\) while \(\operatorname{tr}(D^2)=0\). Thus nonzero trace does not force a nonzero trace of its \(m\)-th power, and minimality in \(N\) cannot be invoked at \(y=x^m\) from the source hypothesis at \(x\).

Even if that nonvanishing were available, the quotient factor would require the projective analogue

\[
m\,e_N\mid|G/N|
\]

from \(\operatorname{tr}T(xN)\ne0\). The active theorem concerns ordinary irreducible characters, not projective characters, so this statement cannot be assumed. Homogeneity and the degree divisor \(e_N\mid[G:N]\) separately do not imply the product \(m e_N\mid[G:N]\). This fires the assigned “homogeneity with no order-degree product” kill criterion for the \(F^*<G\) branch.

There is one sharper ordinary-character reformulation. Put

\[
M=N\langle x\rangle,\qquad |M:N|=m.
\]

Because \(M/N\) is cyclic and \(\theta\) is invariant, \(\theta\) extends to an ordinary \(\widetilde\theta\in\operatorname{Irr}(M)\). Restricting the character-triple factorization to the cyclic quotient writes

\[
\chi_M=\widetilde\theta\sum_{\lambda\in\operatorname{Irr}(M/N)}
a_\lambda\lambda,\qquad
\sum_\lambda a_\lambda=e_N.
\]

Thus \(\chi(x)\ne0\) forces \(\widetilde\theta(x)\ne0\). If \(M<G\), minimality supplies the genuine ordinary-character divisibility

\[
o(x)\theta(1)\mid|M|=|N|m.
\]

To lift this to \(\chi(1)=e_N\theta(1)\), one needs

\[
e_N\mid[G:M].
\]

But this is equivalent to \(m e_N\mid[G:N]\), precisely the missing projective quotient implication above. If \(M=G\), the cyclic quotient makes \(e_N=1\), but there is no smaller group on which to invoke minimality. Hence the cyclic-overgroup refinement identifies the exact missing primewise divisor but does not remove it.

### Central quotient audit in the one-component branch

In the exact branch \(F=Z(G)\), \(E=L\), set \(H=G/Z(G)\), which is almost simple. A faithful representation affording \(\chi\) induces an irreducible projective character \(\widehat\chi\) of \(H\), of degree \(\chi(1)\); choosing a section changes its values only by nonzero scalars, so

\[
\widehat\chi(xZ(G))\ne0.
\]

Let \(m=o_H(xZ(G))\), \(n=o_G(x)\), and \(r=n/m\). Then \(x^m\in Z(G)\), \(o(x^m)=r\), and \(r\mid|Z(G)|\). Consequently,

\[
m\chi(1)\mid|H|\quad\Longrightarrow\quad
n\chi(1)=r\,m\chi(1)\mid |Z(G)|\,|H|=|G|.
\]

Thus an ordinary counterexample in this branch yields an exact **projective** counterexample on the almost-simple quotient:

\[
\widehat\chi(xZ(G))\ne0,\qquad
o_H(xZ(G))\widehat\chi(1)\nmid|H|.
\]

The center/order lift is controlled here; the unresolved step is that \(\widehat\chi\) need not be an ordinary character of \(H\). Converting this projective statement to ordinary almost-simple character theory requires a theorem about covering groups and factor sets (and, for a universal conclusion, Schur multipliers/family classification) not supplied in this lane. I stop rather than import such a classification.

## Early checkpoint — 2026-08-18T04:44:38Z

- Active increment: `00:13:01`; cumulative detailed active time: `02:06:37`.
- Target/revision: exact universal ordinary-character scope, revision 1.
- New facts: primewise cyclic central-product closure; \(F^*=G\) forces a quasisimple least counterexample; the branch \(F=Z(G)\), \(E=L\) gives an exact almost-simple quotient; the cyclic overgroup \(F^*\langle x\rangle\) isolates the missing divisor \(e_{F^*}\mid[G:F^*\langle x\rangle]\).
- Ruled out: uncontrolled cyclic central intersections when the whole group is a central product; multiple components in the \(F^*=G\) branch.
- Bottleneck: for \(F^*<G\), nonzero \(\chi(x)\) gives projective nonvanishing outside \(F^*\), but not nonvanishing at \(x^{o(xF^*)}\) inside \(F^*\), and only \(e\mid[G:F^*]\), not the needed order-degree product. In the almost-simple quotient the character is projective, not ordinary.
- Alternatives: (1) a supplied classification theorem for noncentral Fitting \(p\)-subgroups and component permutation/tensor types; (2) a theorem establishing the projective analogue on almost-simple groups/covering groups.
- Recommendation: route the cyclic central-product lemma and Fitting trichotomy to Validator; any continuation needs MathExpert/Lead to supply one of those theorems or a genuinely new coset-value mechanism.
- Kill criteria: both the homogeneity-without-order-degree-product criterion and the unprovided-classification criterion have fired. Continuing to 30 minutes would repeat the same projective obstruction.
- Constraint status: the central-product class satisfies every ordinary-character row and the desired conclusion. The Fitting statement is only a reduction; `active_assignment_answered: no`.

## Outcome and work stop — 2026-08-18T04:45:27Z

- Outcome: `PARTIAL_RESULT`.
- Increment charged: `00:13:50`.
- Detailed cumulative active time: `02:07:26`.
- Unused increment time returned: `00:31:10`.
- Universal target: unanswered; `active_assignment_answered: no`.
- No heavy computation was used.
- State: `awaiting_lead` after the required Report.

### Ledger correction — 2026-08-18T04:46:02Z

The Report write followed the preliminary stop line. Final work stop: `2026-08-18T04:46:02Z`; increment: `00:14:25`; detailed cumulative active time: `02:08:01`; unused increment returned: `00:30:35`. This supersedes only the preliminary time totals; the outcome is unchanged.
