---
title: "Verification — Kourovka 21.137 — cyclic isotropic cover bound"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "If dim_Fp Q/Z(Q)=2d in the quotient-minimal model, then [H:Q] >= p^(d+1)."
claimant: Problem-21.137
verification_method: computation-free line-by-line hand proof
tools_used: ["none"]
scope_answered: ["cyclic isotropic cover index bound"]
scope_not_answered: ["21.137/odd-prime-exponent-p2"]
active_assignment_answered: no
partial_result_certifiable: yes
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Verdict

**PASS as a structural PARTIAL_RESULT.** The cover, nonzero-point count, conversion from cyclic subgroups to \(|H/Q|\), and discrete power-of-\(p\) step are correct. The result is generally weaker than the affine rank bound and does not force \(Q\) abelian.

# Audit

Put

\[
U=Q/Z(Q),\qquad \dim_{\mathbf F_p}U=2d.
\]

The commutator form on \(U\) is nondegenerate alternating. For each order-\(p\) cyclic subgroup \(K\le R=H/Q\), the audited cyclic-coset lemma puts all projected \(p\)-power values whose root cosets lie in \(K\) inside one totally isotropic linear subspace \(W_K\le U\). Thus \(|W_K|\le p^d\).

These subspaces cover \(U\). Indeed every element of \(Q\) is an actual \(p\)-th power in \(H\). A root in the identity coset \(Q\) has power \(1\), because \(Q\) has exponent \(p\); hence every nonzero vector of \(U\) is supplied by a nonidentity root coset and belongs to the piece indexed by its cyclic subgroup. Zero belongs to every \(W_K\).

If \(t\) is the number of order-\(p\) cyclic subgroups of \(R\), counting nonzero vectors gives

\[
p^{2d}-1\le\sum_K(|W_K|-1)\le t(p^d-1).
\]

Therefore

\[
t\ge\frac{p^{2d}-1}{p^d-1}=p^d+1.
\]

The quotient \(R\) has exponent \(p\), since every \(x^p\) lies in \(Q\). Its nonidentity elements consequently partition into its order-\(p\) cyclic subgroups, even if \(R\) is nonabelian. Hence

\[
t=\frac{|R|-1}{p-1},
\]

and

\[
|R|\ge(p-1)(p^d+1)+1>p^d.
\]

As \(|R|\) is a power of \(p\), the strict inequality yields the discrete jump

\[
\boxed{[H:Q]=|R|\ge p^{d+1}}.
\]

The logged symplectic-spread example is also correct: the \(p^d+1\) one-dimensional \(\mathbf F_{p^d}\)-subspaces of \(\mathbf F_{p^d}^2\), viewed over \(\mathbf F_p\) with the trace alternating form, are totally isotropic, meet pairwise only in zero, and cover the space. It shows that isotropy and cardinality alone cannot improve this covering step or prove global vanishing of the commutator form.

