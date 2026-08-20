---
title: "Problem 20.115 partial result: cyclic central products and generalized Fitting trichotomy"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
outcome: PARTIAL_RESULT
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
---

# Cyclic central products and generalized Fitting trichotomy

## Outcome

`PARTIAL_RESULT`. After rederiving the unreviewed primitive/faithful/quasiprimitive prerequisites, I obtain:

1. the target property is closed under central products whose central intersection is cyclic;
2. if \(G\) is a least-order counterexample and \(F^*(G)=G\), then \(G\) is quasisimple;
3. in the branch \(F(G)=Z(G)\) with one component \(L\), \(G/Z(G)\) is almost simple with socle \(L/Z(L)\), and the original pair yields an exact projective-character counterexample on that quotient;
4. the remaining branches require either an unprovided classification of noncentral normal \(p\)-subgroups of primitive linear groups or new projective/coset-value information.

The universal ordinary-character target remains unanswered.

## Rederived least-counterexample configuration

Choose \(G\) of least order with a witness \(\chi\in\operatorname{Irr}(G)\), \(x\in G\), \(\chi(x)\ne0\), and \(o(x)\chi(1)\nmid|G|\).

- The induced-value coset formula makes \(\chi\) primitive: a nonzero induced value has a nonzero summand in the proper inducing subgroup, where minimality supplies the target.
- Deflation through \(K=\ker\chi\), together with \(o(x)/o(xK)\mid|K|\), makes \(\chi\) faithful.
- Clifford correspondence gives \(\chi_N=e_N\theta\) for every \(N\trianglelefteq G\), with \(\theta\) faithful and \(G\)-invariant. The multiplicity is a projective degree and satisfies \(e_N\mid[G:N]\) by lifting to a finite central extension and applying Itô's theorem.
- Hence \(x\) lies in no proper normal subgroup: otherwise minimality in \(N\) and \(e_N\mid[G:N]\) give the forbidden divisibility. Thus \(\langle x^G\rangle=G\).
- Every abelian normal subgroup is cyclic central.

The run log contains each derivation; none is imported as a reviewed fact.

## Cyclic central-product closure

Let

\[
G=AB,\qquad[A,B]=1,\qquad C=A\cap B\le Z(G),
\]

where \(C\) is cyclic, and suppose the target holds in \(A\) and \(B\). Pulling \(\chi\in\operatorname{Irr}(G)\) back to \(A\times B\) gives \(\alpha\otimes\beta\), so \(\chi(1)=\alpha(1)\beta(1)\). Write \(x=ab\), with \(\chi(x)\ne0\).

Fix a prime \(p\), write \(|C|_p=p^k\), and let \(C_p\) be the Sylow \(p\)-subgroup. All central shifts satisfy

\[
\alpha(ac)\ne0,\qquad\beta(c^{-1}b)\ne0\qquad(c\in C_p).
\]

Put

\[
u_A=v_p(|A|/\alpha(1)),\quad
u_B=v_p(|B|/\beta(1)),
\]

\[
R_A=\max_{c\in C_p}v_p(o(ac)),\quad
R_B=\max_{c\in C_p}v_p(o(c^{-1}b)).
\]

The target in the factors gives \(R_A\le u_A\), \(R_B\le u_B\). Each maximum is at least \(k\): otherwise every element of a coset of the cyclic group \(C_p\) would have exponent at most \(p^{k-1}\), forcing all quotients of coset elements, hence \(C_p\), to have that smaller exponent. If \(q=v_p(o(ab))\), commutativity gives \(q\le\max(R_A,R_B)\). Therefore

\[
u_A+u_B\ge R_A+R_B\ge q+k.
\]

Since \(|G|=|A||B|/|C|\),

\[
v_p(|G|/\chi(1))=u_A+u_B-k\ge q.
\]

This holds for every \(p\), yielding the target in \(G\). Thus a least-order counterexample cannot be a central product of two proper commuting normal subgroups, because its central intersections are cyclic.

## Generalized Fitting consequences

Let \(F=F(G)\), \(E=E(G)\), and \(F^*=FE\). Standard generalized-Fitting facts give \([F,E]=1\), \(F\cap E=Z(E)\), and \(C_G(F^*)\le F^*\).

The rederived abelian-normal property implies

\[
Z(F)=Z(F^*)=Z(G),
\]

which is cyclic. If \(F\) is abelian, then \(F=Z(G)\). If \(F=Z(G)\), the layer cannot be trivial, because otherwise self-centralization would give \(G=C_G(Z(G))\le Z(G)\).

If \(F^*=G\), cyclic central-product closure forces \(E=G\) (the alternative \(F=G\) is nilpotent). Components are normal inside \(E\); two or more components would again split \(G\) as a forbidden cyclic central product. Hence \(G\) has one component and is quasisimple.

If \(F=Z(G)\) and \(E=L\) is one component, then \(C_G(L)=Z(G)\). If an element acts trivially on \(L/Z(L)\), its commutator map from the perfect group \(L\) into \(Z(L)\) is trivial, so it already centralizes \(L\). Conjugation therefore embeds

\[
G/Z(G)\le\operatorname{Aut}(L/Z(L))
\]

with \(L/Z(L)\) contained as the inner automorphism group. Thus \(G/Z(G)\) is almost simple with socle \(L/Z(L)\).

The exact surviving alternatives for a least-order counterexample are therefore:

- \(G\) is quasisimple; or
- \(F^*(G)<G\) and \(F(G)>Z(G)\), leaving a noncentral normal \(p\)-subgroup branch; or
- \(F^*(G)<G\), \(F(G)=Z(G)\), and \(E(G)\) has at least two components; or
- \(F^*(G)<G\), \(F(G)=Z(G)\), \(E(G)=L\), and \(G/Z(G)\) is almost simple.

## Exact obstruction outside proper normals

For \(N=F^*(G)<G\), normal generation gives \(x\notin N\). Character-triple theory factors a representation affording \(\chi\) as reciprocal projective representations over \(N\) and \(G/N\). Nonzero \(\chi(x)\) gives nonzero projective traces, but it does not imply \(\theta(x^m)\ne0\) for \(m=o(xN)\): nonzero matrix trace need not survive taking an \(m\)-th power. Nor does \(e_N\mid[G:N]\) imply \(m e_N\mid[G:N]\). This is exactly where homogeneity stops.

More sharply, let \(M=N\langle x\rangle\). The cyclic quotient \(M/N\) makes \(\theta\) extend to \(\widetilde\theta\in\operatorname{Irr}(M)\), and the character-triple restriction shows \(\chi(x)\ne0\Rightarrow\widetilde\theta(x)\ne0\). If \(M<G\), minimality yields

\[
o(x)\theta(1)\mid|M|.
\]

Lifting this to \(\chi(1)=e_N\theta(1)\) requires exactly \(e_N\mid[G:M]\), equivalently \(m e_N\mid[G:N]\). That is the missing projective order-degree assertion. If \(M=G\), then \(e_N=1\), but no smaller-group induction is available.

In the one-component branch set \(H=G/Z(G)\). The central order lift is controlled: if \(m=o_H(xZ(G))\), \(n=o_G(x)\), then \(r=n/m\mid|Z(G)|\). The representation of \(G\) gives an irreducible projective character \(\widehat\chi\) of \(H\), nonzero at \(xZ(G)\), and

\[
m\widehat\chi(1)\mid|H|
\quad\Longrightarrow\quad
n\chi(1)\mid|G|.
\]

Therefore the original bad pair yields a projective bad pair on the almost-simple quotient. It need not yield an ordinary irreducible character of that quotient. Passing further requires covering-group/factor-set and ultimately family information not supplied here.

## Constraint audit

All deductions retain finite \(G\), ordinary irreducible complex \(\chi\), exact \(x\), and exact nonvanishing. The central-product lemma establishes the requested conclusion on its stated class. The generalized-Fitting trichotomy is a reduction only: `20.115-forall-G-chi-x` and the universal conclusion remain partial. No Brauer character, reducible character, solvable-only universalization, weaker fourth-power bound, or bounded screen is substituted.

## Evidence and limitations

The complete primewise central-product proof, generalized-Fitting theorem inputs, component tensor calculation, projective character-triple audit, and explicit kill points are in `Agents/Kourovka/problems/20.115/runs/2026-08-18-r11-fstar-quasiprimitive-outside-normals/log.md`. The status remains `status/conjectured` pending independent review.
