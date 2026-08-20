---
title: "Verification — Kourovka 12.15 — d=6 isometry exclusion"
problem: 12.15
claim: "A hypothetical minimum order-512 counterexample cannot have log2|G:G'|=6."
claimant: Problem-12.15
target_object: "all finite 2-groups satisfying the exact Strong Magnus Property"
witness_object: "a hypothetical minimum counterexample of order 512 with d=6"
witness_equals_target: false
citation: "Garonzi–Marion, arXiv:2310.19575, Lemma 2.2, for quotient closure of finite SMP groups"
verification_method: "line-by-line hand proof and light GAP sanity checks"
tools_used: ["GAP 4.12.1", "web retrieval"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Verification — Kourovka 12.15

## The claim

Conditional on the earlier minimum-counterexample reduction \(G''=Z(G)=C_2\), an order-512 minimum counterexample cannot have \(d=\log_2|G:G'|=6\).

## Target vs witness

The source problem quantifies over all finite 2-groups. The proof addresses one branch of one hypothetical minimum order, so witness equals target is false and the overall verdict remains `status/conjectured`.

The convention is correct: the PDF requires conjugacy, not conjugacy-or-inverse. Garonzi–Marion define this as SMP and state in Lemma 2.2 that finite SMP passes to quotients.

## Sub-claims and what each method proves

The hand proof was checked line by line:

1. Put \(K=G'\), \(Z=G''=Z(G)\). With \(|G|=512\) and \(d=6\), \(|K|=8\), \(|K'|=2\), so \(K\cong D_8\) or \(Q_8\), and \(Z(K)=Z\).
2. For \(C=C_G(K)\), the conjugation image is a 2-subgroup of \(\operatorname{Aut}(K)\) containing \(\operatorname{Inn}(K)\) of order 4. Its order cannot be 4: that would give \(G=KC\), while \(K\cap C=Z\), \([K,C]=1\), and \(C'\le Z\), forcing \(G'\le Z\), contrary to \(G'=K\). Hence the image has order 8, \(|C|=64\), and \(M=KC\) has index 2.
3. \(M'=K'C'[K,C]=Z\). Since \(C/Z\) embeds in the elementary abelian quotient \(G/K\cong C_2^6\), \(M/Z\) is elementary abelian.
4. The commutator pairing \(\beta:M/Z\times M/Z\to Z\cong\mathbf F_2\) is alternating bilinear. For \(t\notin M\), conjugation induces an isometry \(\alpha\) with \(\alpha^2=1\), because \(t^2\in M\) and inner automorphisms of the class-2 group \(M\) act trivially on \(M/Z\).
5. With \(N=\alpha-1\), characteristic 2 gives \(N^2=0\), so \(\alpha(Ny)=Ny\). If \(u=Nx\) and \(v=Ny\), invariance yields
   \[
   \beta(x+u,v)=\beta(\alpha x,\alpha v)=\beta(x,v),
   \]
   hence \(\beta(u,v)=0\). Thus \(\operatorname{im}N\) is totally isotropic. No nondegeneracy of \(\beta\) on all of \(M/Z\) is assumed here.
6. Since \(G=\langle M,t\rangle\),
   \[
   G'=\langle M',[M,t]\rangle.
   \]
   Modulo \(Z=M'\), the commutator \([m,t]\) represents \((\alpha-1)(mZ)\), up to the immaterial inverse convention. Therefore \(G'/Z=\operatorname{im}N\), not merely a subgroup of it.
7. Since \(G'=K\), \(\operatorname{im}N=K/Z\). But the radical of the restriction of \(\beta\) to \(K/Z\) is \(Z(K)/Z=0\), so this restriction is nondegenerate and nonzero for both \(D_8\) and \(Q_8\). It cannot be totally isotropic. Contradiction.

Both questioned steps—total isotropy and `im(alpha-1)=G'/Z`—are valid.

## Evidence

The source and primary-paper checks used rendered PDF page 58 and [Garonzi–Marion, Lemma 2.2](https://arxiv.org/pdf/2310.19575).

A first GAP sanity probe mistakenly called undefined `Inn`; it raised an error and is excluded. The corrected complete probe was:

```text
GAP_VERSION=4.12.1
K_ID=[ 8, 3 ] DESC=D8 DERIVED_SIZE=2 CENTER_SIZE=2 AUT_SIZE=8 AUT_SYLOW2_SIZE=
8 INNER_SIZE=4
K_ID=[ 8, 4 ] DESC=Q8 DERIVED_SIZE=2 CENTER_SIZE=2 AUT_SIZE=
24 AUT_SYLOW2_SIZE=8 INNER_SIZE=4
RUN_COMPLETE=true
EXIT_STATUS=0
```

The line `d <> 6` in the claimant's catalogue is not verification: it rejects the branch by construction. It is legitimate only after the hand lemma above is established and must never be cited as computational replication of that lemma.

## Verdict

`status/conjectured` for Problem 12.15 and for the compound target claim, because the witness is only a conditional branch. Within those explicit hypotheses, the `d=6` exclusion proof is gap-free.

## Why this verdict

Every group-theoretic equality and the two questioned linear-algebra steps hold. The lower overall status is forced by scope, not by a gap in the lemma.

## What is NOT established

This note does not independently re-prove every upstream minimum-counterexample reduction, exclude \(d=3,4,5\), rule out every order-512 counterexample, or answer the original universal problem. It does not turn the catalogue's hard-coded filter into independent evidence.

## What would upgrade it

Bundle this lemma with separately verified upstream reductions and complete the remaining branches. A `status/proven` treatment of the conditional lemma itself remains subject to the human-sees-proof gate.
