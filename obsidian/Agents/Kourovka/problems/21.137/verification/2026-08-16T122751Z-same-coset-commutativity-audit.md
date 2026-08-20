---
title: "Verification — Kourovka 21.137 — same-coset power commutativity"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "Any two p-th powers with roots in one coset of Q commute in the quotient-minimal counterexample model."
claimant: Problem-21.137
verification_method: line-by-line hand proof
tools_used: ["none; computation expressly excluded"]
scope_answered: ["same-root-coset commutativity lemma"]
scope_not_answered: ["21.137/odd-prime-exponent-p2"]
active_assignment_answered: no
partial_result_certifiable: yes
materially_strengthens_structure: yes
improves_current_order_bound: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.137

## Verdict

**PASS as an additional structural `PARTIAL_RESULT`.** The isotropy and orthogonality steps are valid, and the affine description modulo (C) is sufficient to deduce exact commutativity in (Q). The lemma materially sharpens the geometry of the accepted affine cover, but it does not by itself improve the numerical bound (|G|\ge p^{2p+2}).

## Nilpotence of the root action

Let (L) be the class-2 exponent-(p) Lie algebra of (Q), let (a=x^p), let (A) be conjugation by (x), and set (N=A-I). With a fixed commutator convention,

\[
N^p=\pm\operatorname{ad}(a).
\]

The sign is immaterial here. The image of (\operatorname{ad}(a)) lies in (Q'=C), and (A) fixes (C\le Z(H)) pointwise. Hence (N) kills that image and

\[
N^{p+1}=0.
\]

This remains true when (a) happens to be central, in which case (N^p=0).

## Adjoint and isotropy

The bracket induces a nondegenerate alternating (\mathbb F_p)-valued form on

\[
U=Q/Z(Q):
\]

its radical before quotienting is exactly (Z(Q)), and (Q'=C\cong\mathbb F_p). Because (A) is a group automorphism and fixes (C), it preserves this form. Therefore (A^*=A^{-1}), and

\[
N^*=A^{-1}-I=-A^{-1}N.
\]

Since (A) commutes with (N),

\[
\ker((N^*)^i)=\ker(N^i).
\]

The standard adjoint identity then gives

\[
(\operatorname{im}N^i)^\perp=\ker N^i.
\]

For (i=p-1), oddness gives (2p-2\ge p+1). From (N^{p+1}=0),

\[
N^{p-1}(\operatorname{im}N^{p-1})
=\operatorname{im}N^{2p-2}=0,
\]

so (\operatorname{im}N^{p-1}\le\ker N^{p-1}=(\operatorname{im}N^{p-1})^\perp). The affine direction is therefore totally isotropic on (U).

Moreover, for (w=N^{p-1}u),

\[
[a,w]=\pm N^pN^{p-1}u=\pm N^{2p-1}u=0,
\]

because (2p-1\ge p+1). Thus the basepoint (a) is orthogonal to the affine direction.

## From affine geometry to group commutativity

The checked coset formula says that every power value (y) from (xQ), viewed in the Lie algebra modulo (C), has the form

\[
y\equiv a+N^{p-1}u\pmod C.
\]

Hence two such values can be written in (L) as

\[
y_1=a+w_1+c_1,\qquad y_2=a+w_2+c_2,
\]

with (w_i\in\operatorname{im}N^{p-1}) and (c_i\in C\le Z(Q)). Bilinearity of the class-2 Lie bracket, isotropy of the (w_i), orthogonality to (a), and centrality of (C) give

\[
[y_1,y_2]=[a,w_2]+[w_1,a]+[w_1,w_2]=0.
\]

The corresponding group elements therefore commute.

## Material effect

This is stronger than the bare affine-cardinality statement: every piece of the cover contributed by one root coset is a pairwise commuting subset, with isotropic direction. It does not force different pieces to commute, bound their overlaps more sharply, or reduce the number of pieces needed in general. Accordingly, it adds a useful structural lemma but does not yet strengthen the uniform order exponent (2p+2) or answer the active scope.
