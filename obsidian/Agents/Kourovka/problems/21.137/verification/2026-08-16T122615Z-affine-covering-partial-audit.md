---
title: "Verification — Kourovka 21.137 — affine coset-image covering bound"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "The affine coset-image argument forces every active-scope counterexample to have order at least p^(2p+2)."
claimant: Problem-21.137
target_object: "A quotient-minimal odd-prime exponent-p^2 counterexample with closed actual power set"
verification_method: line-by-line hand proof
tools_used: ["none; computation expressly excluded"]
scope_answered: ["necessary order bound |G| >= p^(2p+2)"]
scope_not_answered: ["21.137/odd-prime-exponent-p2"]
active_assignment_answered: no
partial_result_certifiable: yes
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.137

## Verdict

**PASS as a `PARTIAL_RESULT`.** Every formula, rank estimate, covering count, and exponent in the 2026-08-16T12:23 affine argument is correct. The argument uses the actual-value-set hypothesis and remains within the odd-prime, exact-exponent-(p^2) scope.

## 1. Power values from a fixed coset

Let (Q) have order (p^m), let (C=Q'\cong C_p), and put (V=Q/C\cong\mathbb F_p^{m-1}). For a fixed coset (xQ), write (a=x^p\in Q), let (A) be conjugation by (x) on (V), and set (N=A-I).

Since (A^p) is conjugation by (x^p=a\in Q), and every inner automorphism induced by (Q) is trivial on (Q/Q'=Q/C),

\[
A^p=I,\qquad N^p=(A-I)^p=A^p-I=0.
\]

For (q\in Q), direct collection gives

\[
(xq)^p=x^p q^{x^{p-1}}q^{x^{p-2}}\cdots q^xq.
\]

After projection to the additive elementary-abelian group (V), this becomes

\[
\overline{(xq)^p}=\bar a+(I+A+\cdots+A^{p-1})\bar q.
\]

Over (\mathbb F_p), the polynomial identity

\[
1+T+\cdots+T^{p-1}=(T-I)^{p-1}
\]

holds because every coefficient of ((T-1)^{p-1}) is 1 modulo (p). Substitution (T=A) therefore gives the exact projected image

\[
\bar a+\operatorname{im}N^{p-1}.
\]

## 2. Rank bound

The relation (N^p=0) makes every Jordan block of (N) have size at most (p). Applying (N^{p-1}) kills every block of size below (p) and has rank 1 on every size-(p) block. Hence

\[
\operatorname{rank}N^{p-1}
=\#\{\text{size-}p\text{ blocks}\}
\le\left\lfloor\frac{m-1}{p}\right\rfloor.
\]

Thus one coset gives at most (p^{\lfloor(m-1)/p\rfloor}) values modulo (C). Each projected value has at most (|C|=p) lifts in (Q), so one coset contributes at most

\[
p^{\lfloor(m-1)/p\rfloor+1}
\]

actual power values. This is an upper bound; possible collisions only strengthen it.

## 3. Coverage and index

The domain (H) is partitioned by its ([H:Q]) cosets, and the image of the (p)-power map is exactly the actual power set (Q), of size (p^m). The union bound therefore yields

\[
[H:Q]p^{\lfloor(m-1)/p\rfloor+1}\ge p^m.
\]

Consequently

\[
[H:Q]\ge p^{m-1-\lfloor(m-1)/p\rfloor}.
\]

No disjointness of the affine images is assumed; overlap cannot invalidate this necessary inequality.

## 4. Final exponent

Multiplying by (|Q|=p^m) gives

\[
|H|\ge p^{,2m-1-\lfloor(m-1)/p\rfloor}.
\]

For integral (m), the exponent

\[
e(m)=2m-1-\left\lfloor\frac{m-1}{p}\right\rfloor
\]

is strictly increasing: (e(m+1)-e(m)) is 1 when (p\mid m) and 2 otherwise. The previously checked Jordan argument gives (m\ge p+2), so the minimum is attained at (m=p+2), where

\[
e(p+2)=2(p+2)-1-\left\lfloor\frac{p+1}{p}\right\rfloor=2p+2.
\]

Because (H) is a quotient of the original counterexample (G),

\[
\boxed{|G|\ge |H|\ge p^{2p+2}}.
\]

For (p=3), this is (3^8), agreeing with the earlier hand bound. For (p\ge5), (2p+2>p+5), so it strictly improves the root-fibre exponent.

## What is NOT established

The affine pieces may overlap or collectively cover (V); the count gives only the minimum number of root cosets required. It does not prove (Q) abelian, does not answer the active assignment, and says nothing about the excluded (p=2), exponent-8 clause.
