---
title: "Verification — Kourovka 21.137 — common-flag center bound"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "In the quotient-minimal counterexample model, dim_Fp Z(Q) >= p; hence Q cannot be extraspecial."
claimant: Problem-21.137
verification_method: computation-free line-by-line hand proof
tools_used: ["none"]
scope_answered: ["center-dimension bound in quotient-minimal counterexample"]
scope_not_answered: ["21.137/odd-prime-exponent-p2"]
active_assignment_answered: no
partial_result_certifiable: yes
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Verdict

**PASS as a structural PARTIAL_RESULT.** The common-flag indexing, the identity \(N^p=D_a\), and the use of simultaneous root-surjectivity are correct. The result proves

\[
\dim_{\mathbf F_p}Z(Q)\ge p,
\]

so it strictly subsumes the separate extraspecial-\(Q\) exclusion. It does not prove \(Q\) abelian.

# Common flag

Let \(L\) be the class-2 exponent-\(p\) Lie algebra of \(Q\), and let \(S\) be the image of \(H\) in \(\operatorname{Aut}(L)\). Because \(H\) is a finite \(p\)-group, \(S\) is a finite \(p\)-group. Every finite \(p\)-group representation over \(\mathbf F_p\) has a nonzero fixed vector; applying this successively to quotients gives a complete common invariant flag

\[
0=F_0<F_1<\cdots<F_m=L,\qquad \dim F_i=i,
\]

for which

\[
(A-I)F_i\le F_{i-1}\qquad(A\in S).
\]

The term \(F_p\) exists. Independently, choose noncentral \(a\in Q\) and a root \(x\); then \(N^p=D_a\ne0\) already forces \(\dim L\ge p+1\). It also exists by the previously audited stronger bound \(m\ge p+2\).

# Root-action identity and center bound

For arbitrary \(a\in Q\), actual-value surjectivity supplies \(x\in H\) with \(x^p=a\). Let \(A\) be conjugation by \(x\) on \(L\) and \(N=A-I\). In characteristic \(p\),

\[
N^p=(A-I)^p=A^p-I.
\]

The map \(A^p\) is conjugation by \(x^p=a\). Since \(L\) has class \(2\), this inner automorphism is \(I+D_a\), where, with the fixed convention,

\[
D_a(v)=[v,a]_L.
\]

Thus \(N^p=D_a\) (or the same identity with a global harmless sign under the opposite convention). For \(v\in F_p\), repeated flag lowering gives

\[
N^pv\in F_0=0.
\]

This root action is available for every \(a\in Q\), so

\[
[v,a]_L=0\qquad(v\in F_p,\ a\in Q).
\]

Therefore \(F_p\le Z(L)=Z(Q)\), and its dimension is \(p\). Since nonabelian class-2 \(Q\) has \(\dim Q/Z(Q)\ge2\), one also recovers \(\dim Q\ge p+2\).

# Separate extraspecial argument

The preceding proof already rules out \(Z(Q)=Q'\cong C_p\). The longer argument at 12:41:54Z is also sound: in extraspecial coordinates \(L=V\oplus C\), every induced automorphism fixing \(C\) has form \((A,\lambda)\); a common flag for the \(p\)-group image on \(V\) makes

\[
(A,\lambda)^p=(I,\lambda(A-I)^{p-1})
\]

annihilate the same nonzero flag term. Nondegeneracy identifies inner automorphisms with \(V\), placing all these \(p\)-th powers in one proper annihilator. Root-surjectivity would realize every inner automorphism, a contradiction.

For complete standalone wording, if \(\dim V<p-1\), replace the displayed \(V_{p-1}\) by \(V_{\min(p-1,\dim V)}\); in the present model \(\dim V\ge p\), so the logged \(V_{p-1}\) is defined and no correction is needed.

