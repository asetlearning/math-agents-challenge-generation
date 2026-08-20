---
title: "Verification — Kourovka 21.137 — identity-coset affine refinement"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "The identity-coset correction strengthens the necessary counterexample-order bound to |G| >= p^(2p+3)."
claimant: Problem-21.137
verification_method: computation-free line-by-line hand proof
tools_used: ["none"]
scope_answered: ["necessary order bound |G| >= p^(2p+3)"]
scope_not_answered: ["21.137/odd-prime-exponent-p2"]
active_assignment_answered: no
partial_result_certifiable: yes
supersedes_numerical_conclusion: 2026-08-16T122615Z-affine-covering-partial-audit.md
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Verdict

**PASS as a sharpened PARTIAL_RESULT.** The strict inequality and the discrete power-of-\(p\) jump are both valid. The new \(p^{2p+3}\) bound supersedes the numerical conclusion of the earlier affine audit, while leaving that earlier, weaker inequality true.

# Line-by-line audit

Retain the checked quotient-minimal notation

\[
|Q|=p^m,\qquad C=Q'\cong C_p,\qquad
k=\left\lfloor\frac{m-1}{p}\right\rfloor,\qquad
M=p^{k+1},\qquad r=[H:Q].
\]

1. The affine rank calculation bounds the actual \(p\)-power image of every nonidentity coset of \(Q\) by \(M\). This includes the possible \(p\) lifts over one projected value and is therefore a valid upper bound even when collisions occur.
2. The identity coset \(Q\) contributes exactly \(\{1\}\), because \(Q\) has exponent \(p\). Since every element of \(Q\) is an actual \(p\)-th power in \(H\), the exact union bound is

   \[
   p^m\le 1+(r-1)M.
   \]

   No disjointness of the nonidentity images is assumed.
3. If \(r\le p^{m-1-k}\), then

   \[
   1+(r-1)M
   \le 1+\bigl(p^{m-1-k}-1\bigr)p^{k+1}
   =p^m-p^{k+1}+1<p^m,
   \]

   a contradiction. Thus the old lower endpoint is not merely an unattained equality case: every smaller \(p\)-power is excluded too.
4. The index \(r\) is a power of \(p\). Therefore the next permissible value gives

   \[
   [H:Q]=r\ge p^{m-k}
   =p^{m-\lfloor(m-1)/p\rfloor}.
   \]
5. Multiplying by \(|Q|=p^m\) yields

   \[
   |H|\ge p^{\,2m-\lfloor(m-1)/p\rfloor}.
   \]

   For integral \(m\), this exponent increases by \(1\) or \(2\) when \(m\) increases by one. The previously audited Jordan-chain reduction gives \(m\ge p+2\), so its minimum occurs at \(m=p+2\):

   \[
   2(p+2)-\left\lfloor\frac{p+1}{p}\right\rfloor=2p+3.
   \]

   Since \(H\) is a quotient of the original counterexample,

   \[
   \boxed{|G|\ge |H|\ge p^{2p+3}}.
   \]

The proof is uniform for odd \(p\), including \(p=3\), and continues to use the actual power-value set. It does not prove \(Q\) abelian or answer the active assignment.

