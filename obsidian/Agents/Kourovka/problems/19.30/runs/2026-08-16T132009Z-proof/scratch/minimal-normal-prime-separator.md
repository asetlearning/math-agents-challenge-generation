---
title: "Minimal-normal prime separator for vanishing-element orders"
author: operator
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
---

# Minimal-normal prime separator

Write

\[
  V_o(X)=\{|x|:x\in X\text{ and }\chi(x)=0
  \text{ for some }\chi\in\operatorname{Irr}(X)\}.
\]

The results below are a sufficient reduction, not a proof of the universal
Kourovka scope.

## Lemma 1 — what a normal subgroup of prime order actually gives

Let \(N\triangleleft X\) and \(|N|=p\), where \(p\) is prime. Then every
\(1\ne x\in N\) is nonvanishing in \(X\):

\[
  \chi(x)\ne0\qquad\text{for every }\chi\in\operatorname{Irr}(X).
\]

Consequently, if every element of order \(p\) in \(X\) lies in \(N\), then
\(p\notin V_o(X)\). In particular this conclusion holds when
\(|X|_p=p\) and \(N\) is normal, because then \(N\) is the unique Sylow
\(p\)-subgroup.

### Proof

Fix \(1\ne x\in N\). Since \(|N|=p\), \(x\) generates \(N\). Choose a
primitive \(p\)-th root \(\zeta\), and label
\(\operatorname{Irr}(N)=\{\lambda_0,\ldots,\lambda_{p-1}\}\) so that
\(\lambda_j(x)=\zeta^j\).

For \(\chi\in\operatorname{Irr}(X)\), Clifford's restriction theorem gives

\[
  \chi_N=e\sum_{j\in A}\lambda_j,
\]

where \(e\) is a positive integer and \(A\) is one nonempty \(X\)-orbit on
\(\operatorname{Irr}(N)\). The trivial character is fixed by every automorphism
of \(N\), so either \(A=\{0\}\) or
\(A\subseteq\{1,\ldots,p-1\}\).

If \(A=\{0\}\), then \(\chi(x)=e\ne0\). Otherwise suppose for contradiction
that \(\chi(x)=0\). Then

\[
  f(\zeta)=0,\qquad f(T)=\sum_{j\in A}T^j\in\mathbb Z[T].
\]

The minimal polynomial of \(\zeta\) over \(\mathbb Q\) is
\(\Phi_p(T)=1+T+\cdots+T^{p-1}\), so \(\Phi_p\mid f\) in
\(\mathbb Q[T]\). But \(f\ne0\), \(\deg f\le p-1\), and the constant
coefficient of \(f\) is zero. If \(\deg f<p-1\), divisibility is impossible.
If \(\deg f=p-1\), comparison of leading coefficients forces
\(f=\Phi_p\), contradicting the constant coefficients. Hence
\(\chi(x)\ne0\).

The final assertion follows because membership in \(V_o(X)\) at the integer
\(p\) requires at least one vanishing element of order \(p\). ∎

### The coverage hypothesis cannot be dropped

A characteristic subgroup of order \(p\) need not contain all elements of order
\(p\). For example, let \(X=C_2\times S_3\) and
\(N=Z(X)=C_2\times1\). Then \(N\) is characteristic of order two, but if
\(t\) is a transposition, \((1,t)\) has order two and is vanishing. Indeed the
degree-two irreducible character of \(S_3\) is the natural permutation character
minus the trivial character, so its value on \(t\) is \(1-1=0\); its external
tensor product with the trivial character of \(C_2\) is irreducible and vanishes
at \((1,t)\). Thus \(2\in V_o(X)\).

So Clifford theory alone controls the elements in \(N\); absence of the integer
\(p\) from the full invariant needs the additional coverage condition.

## Lemma 2 — the full order of a normal Sylow subgroup is absent

Let \(P\triangleleft X\) be a Sylow \(p\)-subgroup and write
\(|P|=p^a\). Then

\[
  p^a\notin V_o(X).
\]

### Proof

Because \(P\) is normal, it is the unique Sylow \(p\)-subgroup, so every
\(p\)-element of \(X\) lies in \(P\). If \(P\) is noncyclic, \(X\) has no
element of order \(p^a\): any such element would generate all of \(P\).

Suppose that \(P\) is cyclic, and let \(x\) generate it. For
\(\chi\in\operatorname{Irr}(X)\), Clifford restriction gives

\[
  \chi_P=e\sum_{\lambda\in\mathcal O}\lambda
\]

for a positive integer \(e\) and one \(X\)-orbit \(\mathcal O\) on
\(\operatorname{Irr}(P)\). Conjugation by \(P\) is trivial because \(P\) is
abelian, so \(|\mathcal O|\) divides \(|X:P|\) and is therefore prime to
\(p\).

Let \(\zeta\) be a primitive \(p^a\)-th root. Since evaluation at the generator
\(x\) identifies the distinct characters of \(P\) with the distinct powers of
\(\zeta\), there is a polynomial

\[
  f(T)=\sum_{j\in A}T^j\in\mathbb Z[T],\qquad
  |A|=|\mathcal O|,\qquad 0\le j<p^a,
\]

such that \(\chi(x)=e f(\zeta)\). If \(f(\zeta)=0\), then the cyclotomic
polynomial

\[
  \Phi_{p^a}(T)=1+T^{p^{a-1}}+\cdots+T^{(p-1)p^{a-1}}
\]

divides \(f\) in \(\mathbb Q[T]\). Gauss's lemma makes the quotient integral,
so evaluation at \(T=1\) gives \(p\mid f(1)=|\mathcal O|\), contrary to the
orbit-size observation. Thus no generator of \(P\), and hence no element of
order \(p^a\), is vanishing. ∎

For \(a=1\), this recovers the prime-absence consequence of Lemma 1. The benefit
of the full-order formulation is that it does not require the prime to occur only
once in \(|X|\).

## Lemma 3 — a minimal-normal criterion forcing a normal Sylow subgroup

Let \(m\) be a positive integer and let \(p\mid m\) be prime. Assume:

1. **(CS-p)** Whenever \(A\) is a nonabelian finite characteristically simple
   group such that \(|A|\mid m\) and \(|A|<m\), one has
   \(p\nmid|A|\).
2. **(Aut-p)** Whenever \(A\) is a finite characteristically simple
   \(p'\)-group with \(|A|\mid m\), one has
   \(p\nmid|\operatorname{Aut}(A)|\).

Then every nonsimple group \(X\) of order \(m\) has a normal Sylow
\(p\)-subgroup.

### Proof

We prove the slightly stronger induction statement: for every divisor \(d\mid m\)
with \(p\mid d\) and \(d<m\), every group of order \(d\) has a normal Sylow
\(p\)-subgroup; the same is true at \(d=m\) for nonsimple groups.

Let \(X\) be a least-order counterexample to that statement, and let
\(N\ne1\) be a minimal normal subgroup of \(X\). A characteristic subgroup of
\(N\) is normal in \(X\), so minimality makes \(N\) characteristically simple.

First suppose \(p\mid|N|\). If \(N\) is abelian, it is elementary abelian of
order \(r^b\) for a prime \(r\), and here \(r=p\). If
\(p\nmid|X/N|\), then \(N\) is already a normal Sylow \(p\)-subgroup. If
\(p\mid|X/N|\), induction gives a normal Sylow \(p\)-subgroup
\(\overline P\) of \(X/N\); its full preimage is a normal \(p\)-subgroup
whose order is the full \(p\)-part of \(|X|\), hence is a normal Sylow
subgroup of \(X\). Both alternatives contradict the choice of \(X\). If
\(N\) is nonabelian, then \(|N|<m\): at the top order,
\(X\) is assumed nonsimple and hence \(N<X\); at a proper divisor,
\(|N|\le |X|<m\), including the case \(N=X\). This contradicts
**(CS-p)**.

It remains that \(p\nmid|N|\). The quotient \(X/N\) has smaller order, its
order divides \(m\), and its order is divisible by \(p\). By induction it has a
normal Sylow subgroup \(\overline P\). Let \(M\) be the full
preimage of \(\overline P\) in \(X\). Then \(M\triangleleft X\),
\(N\triangleleft M\), and \(M/N=\overline P\) is a \(p\)-group.

Choose a Sylow \(p\)-subgroup \(P\) of \(M\). Since \(N\) is a normal
\(p'\)-subgroup and \(M/N\) is a \(p\)-group, the product formula gives
\(M=NP\). Conjugation induces a homomorphism

\[
  P\longrightarrow\operatorname{Aut}(N).
\]

Condition **(Aut-p)** says that the target has order prime to \(p\), so this
homomorphism is trivial. Hence \(P\) centralizes \(N\). Since \(M=NP\), this
makes \(P\triangleleft M\). It is therefore the unique Sylow \(p\)-subgroup of
\(M\), hence characteristic in \(M\). Finally \(M\triangleleft X\) gives
\(P\triangleleft X\), contradicting the choice of \(X\). ∎

No Schur--Zassenhaus complement theorem is needed: an arbitrary Sylow subgroup
\(P\le M\) already satisfies \(M=NP\) by the order calculation.

## Theorem 4 — prime-power separator recognition criterion

Let \(S\) be a finite simple group of order \(m\). Suppose there is a prime
\(p\mid m\), and put \(p^a=m_p\). Assume all of the following:

1. **(Target-vanishing)** There are \(s\in S\) of order \(p^a\) and
   \(\theta\in\operatorname{Irr}(S)\) such that \(\theta(s)=0\).
2. Conditions **(CS-p)** and **(Aut-p)** of Lemma 3 hold for \((m,p)\).
3. **(Simple-order uniqueness)** Every finite simple group of order \(m\) is
   isomorphic to \(S\).

Then every finite group \(G\) of order \(m\) with
\(V_o(G)=V_o(S)\) is isomorphic to \(S\).

### Proof

Suppose first that \(G\) is nonsimple. Lemma 3 supplies a normal Sylow
subgroup \(P\) of order \(p^a\). Lemma 2 then gives
\(p^a\notin V_o(G)\). On the other hand **(Target-vanishing)** gives
\(p^a\in V_o(S)\), contradicting
\(V_o(G)=V_o(S)\). Thus \(G\) is simple. By **(Simple-order uniqueness)**,
\(G\cong S\). ∎

When \(a=1\), Theorem 4 is exactly the prime-order separator requested by the
active strategy: Lemma 1 supplies the Clifford step, and Lemma 3 supplies the
normal Sylow subgroup.

### Separate character-theoretic input on the simple side

The abstract theorem deliberately assumes **(Target-vanishing)** directly. A
standard sufficient package is: \(S\) contains an element of order \(m_p\), and
there is a \(p\)-defect-zero irreducible character \(\theta\), meaning
\(\theta(1)_p=|S|_p\), together with the defect-zero vanishing theorem that such a
character vanishes on every nonidentity \(p\)-singular element. The element-order
and defect-zero inputs are separate dependencies; the normal-prime Clifford
argument says nothing about vanishing inside \(S\).

## Conditional Suzuki specialization

This subsection records exactly what the permitted MathExpert seed supports, while
keeping every ungrounded standard input explicit.

Let \(n\ge3\) be odd, \(q=2^n\),
\(S=\operatorname{Sz}(q)\), and

\[
  m=|S|=q^2(q^2+1)(q-1).
\]

Assume there is a prime \(p\) such that:

1. **(P1)** \(\operatorname{ord}_p(2)=4n\);
2. **(P2)** for every odd prime \(r\ne p\) dividing \(m\),
   \(\operatorname{ord}_p(r)>v_r(m)\).

Also assume the following named external inputs:

0. **(E0)** for odd \(a\ge3\), \(\operatorname{Sz}(2^a)\) is finite simple
   of order \(2^{2a}(2^{2a}+1)(2^a-1)\);
1. **(E1)** every nonabelian finite simple group of order prime to three is a
   Suzuki group \(\operatorname{Sz}(2^a)\) for odd \(a\ge3\);
2. **(E2)** \(\operatorname{Out}(\operatorname{Sz}(2^a))\cong C_a\);
3. **(E3)** \(\operatorname{Sz}(q)\) has an irreducible complex character of
   degree \(q^2+1\);
4. **(E4)** a \(p\)-defect-zero irreducible character vanishes on nonidentity
   \(p\)-singular elements;
5. **(E5)** the applicable cases of the Bang--Zsigmondy theorem: \(2^a-1\)
   has a prime divisor whose multiplicative order of \(2\) is exactly \(a\) for
   odd \(a\ge3\), and \(2^{4n}-1\) has one whose order is exactly \(4n\).
6. **(E6)** for a prime \(p\mid q^2+1\), a Sylow \(p\)-subgroup of
   \(\operatorname{Sz}(q)\) is cyclic (equivalently for this use, the relevant
   Suzuki maximal-torus input supplies an element of order \((q^2+1)_p\)).
7. **(E7)** for nonabelian finite simple \(T\),
   \(\operatorname{Aut}(T^k)=\operatorname{Aut}(T)\wr S_k\).

Subject to these explicit inputs, Theorem 4 applies to \(S\).

### Verification of Theorem 4's hypotheses

- Since \(n\) is odd, \(q\equiv-1\pmod3\). Hence neither \(q-1\) nor
  \(q^2+1\) is divisible by three, so \(3\nmid m\).
- By **(P1)**, \(2^{2n}\equiv-1\pmod p\), so \(p\mid q^2+1\). Put
  \(p^e=(q^2+1)_p=m_p\); no first-power assumption is needed.
- If a finite simple group \(T\) has order \(m\), it is nonabelian because
  \(m\) is composite. By **(E1)** it is \(\operatorname{Sz}(2^a)\). Comparing
  the 2-parts \(2^{2a}=2^{2n}\) gives \(a=n\), establishing
  **(Simple-order uniqueness)**.
- Let \(A=T^k\) be a proper nonabelian characteristically simple group with
  \(|A|\mid m\). Input **(E1)** makes
  \(T=\operatorname{Sz}(2^a)\). By **(E5)** choose a prime \(z\) with
  \(\operatorname{ord}_z(2)=a\) and \(z\mid 2^a-1\). Divisibility
  \(|T|\mid m\) puts \(z\) into either \(2^n-1\) or \(2^{2n}+1\).
  In the first case \(a\mid n\); in the second, \(a\mid4n\), and oddness again
  gives \(a\mid n\). Properness forces \(a<n\). Condition **(P1)** then prevents
  \(p\) from dividing either \(2^a-1\) or \(2^{2a}+1\), so \(p\nmid|T|\),
  establishing **(CS-p)**.
- For this nonabelian \(A=T^k\),
  \(\operatorname{Aut}(A)=\operatorname{Aut}(T)\wr S_k\). We have
  \(p\nmid|T|\), while **(P1)** gives \(4n\mid p-1\) and hence
  \(p>4n>a\). Since \(T\) is centerless, its inner automorphism group has
  order \(|T|\), so **(E2)** gives
  \(p\nmid|\operatorname{Aut}(T)|\). Comparison of 2-parts gives
  \(2ak\le2n\), hence \(k\le n/a<p\). Thus
  \(p\nmid|\operatorname{Aut}(A)|\).
- If \(A=C_r^d\) is abelian characteristically simple and \(p\nmid|A|\), then
  \(d\le v_r(m)\). Since
  \(|\operatorname{GL}_d(r)|=r^{d(d-1)/2}\prod_{i=1}^d(r^i-1)\), the prime
  \(p\) divides this automorphism-group order exactly when
  \(\operatorname{ord}_p(r)\le d\). For \(r=2\), **(P1)** gives
  \(4n>v_2(m)=2n\). For odd \(r\), **(P2)** applies. This completes
  **(Aut-p)**.
- By **(E3)** there is \(\theta\in\operatorname{Irr}(S)\) of degree
  \(q^2+1\). Its \(p\)-part is \(p^e=|S|_p\), so it is
  \(p\)-defect zero. Input **(E6)** supplies an element of order \(p^e\), and
  **(E4)** makes that element vanishing. This establishes
  **(Target-vanishing)** at the full Sylow order.

### Exact limitation: no proved infinite family in this blind run

Bang--Zsigmondy supplies a prime satisfying **(P1)**, and the full-Sylow-order
version removes any squarefreeness requirement. The work above still does not show
that a primitive prime can always be chosen with all simultaneous linear conditions
**(P2)**. It also does not ground **(E0)--(E7)** with permitted sources. Therefore
this is a uniform conditional criterion for odd parameters, not evidence that
infinitely many Suzuki groups are covered.

The cyclic simple groups \(C_\ell\) do form an unconditional infinite recognition
family for the original question, because every group of prime order is cyclic.
They are not covered by this prime-separator mechanism: no element of an abelian
group is vanishing, so **(Target-vanishing)** fails.

## Uncovered scope

The universal target remains open in this run. In particular, the criterion does
not address:

- simple groups for which no full Sylow order \(m_p\) is attained by a vanishing
  element;
- orders having an admissible proper characteristically simple divisor on which
  the separator prime acts;
- nonisomorphic simple groups of the same order unless simple-order uniqueness is
  separately supplied;
- Suzuki parameters for which **(P2)** is not established; or
- any family whose required classification, outer-automorphism, character-degree,
  or defect-zero input is not independently grounded.
