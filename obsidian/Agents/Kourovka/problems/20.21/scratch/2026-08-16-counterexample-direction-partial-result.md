---
title: "Kourovka 20.21 — minimum-witness and characteristic-section reductions"
problem: "20.21"
scope_id: 20.21/two-index-twelve-kernels
assignment_revision: 1
direction: counterexample
cycle_outcome: PARTIAL_RESULT
active_assignment_answered: no
external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/group-extensions
  - project/kourovka
  - status/conjectured
---

# Minimum-witness and characteristic-section reductions

## Active target and boundary

Scope: `20.21/two-index-twelve-kernels`, assignment revision 1.

The active target asks for a finite (G) with normal isomorphic (K,L) of index 12 such that (G/K\cong C_{12}) and (G/L\cong A_4).

This note does **not** answer that existence question. It records a computation-free candidate partial reduction for independent review. It uses the Validator-reviewed Goursat alternatives but does not generalize the earlier bounded Q8/D8 exclusions.

## Candidate partial result

If a witness to the active target exists, then a minimum-order witness exists and can be chosen so that, with (N=K\cap L), all of the following hold:

1. It is in the common-(C_3) Goursat branch:
   \[
   K/N\cong V_4,\qquad L/N\cong C_4.
   \]
2. (|N|) is even.
3. (O_{2'}(N)=1).
4. (K\cong L) is nonabelian; in particular (N\not\le Z(L)).

The first row is a strict self-descent from the other Goursat branch. The other rows are intrinsic necessary conditions within the surviving branch.

## 1. Strict descent from the full-product branch

Suppose a witness is in the full-product branch. The reviewed orientation is

\[
K/N\cong A_4,\qquad L/N\cong C_{12}.
\]

Choose an abstract isomorphism θ from (K) to (L). In the smaller ambient group (Q=K), let

\[
K_1=\theta^{-1}(N),\qquad L_1=N.
\]

Both are normal in (Q), and restriction of θ gives (K_1\cong L_1). Moreover,

\[
Q/K_1\cong L/N\cong C_{12},\qquad
Q/L_1=K/N\cong A_4,
\]

and both indices are 12. Since (|Q|=|G|/12), this is a strictly smaller witness to exactly the active target. Therefore a minimum-order witness cannot be in the full-product branch and must be common-(C_3).

This does not assert that a larger full-product witness is impossible if a smaller common-(C_3) witness exists.

## 2. Odd (N) is incompatible with isomorphic kernels

Now assume the common-(C_3) branch. If (|N|) were odd, a Sylow 2-subgroup (P) of (K) would have order 4 and meet (N) trivially. Its image in (K/N\cong V_4) would therefore have order 4, so (P\cong V_4). The same argument makes every Sylow 2-subgroup of (L) isomorphic to (C_4). An isomorphism (K\cong L) must carry a Sylow 2-subgroup to a Sylow 2-subgroup, a contradiction.

Thus (|N|) is even in every common-(C_3) witness.

## 3. The common normal odd core can be removed

Because both $K/N$ and $L/N$ are 2-groups,

\[
O_{2'}(K)=O_{2'}(N)=O_{2'}(L)=:O.
\]

For example, a normal odd-order subgroup of (K) maps trivially to (K/N) and hence lies in (N); conversely (O_{2'}(N)) is characteristic in (N\triangleleft K), so it is normal in (K). The same reasoning applies to (L).

Thus (O) is the same actual subgroup and is characteristic in both (K) and (L). Every isomorphism (K\to L) preserves (O), so it descends to an isomorphism (K/O\cong L/O). If (O\ne1), then

\[
(G/O,K/O,L/O)
\]

is a strictly smaller witness with the same two quotients and indices. Hence a minimum-order witness has (O_{2'}(N)=1).

This condition does not force (N) to be a 2-group.

## 4. The coordinate kernels cannot be abelian

Continue in the common-(C_3) branch and choose θ as above. Within (Q=K), put (M=\theta^{-1}(N)). Then (N\cong M), with quotient maps

\[
f_N:Q\twoheadrightarrow V_4,\qquad
f_M:Q\twoheadrightarrow C_4.
\]

Assume for contradiction that (Q) is abelian. Choose (g\in G) whose image in (G/L\cong A_4) is a 3-cycle. Conjugation by (g) preserves (Q=K) and (N), and its induced action on (Q/N\cong V_4) cycles the three nonidentity elements. Consequently the only invariant subgroups of this (V_4) are (1) and (V_4).

For every (j\ge1), let (Q[2^j]) be the characteristic subgroup of elements killed by (2^j). Then

\[
|f_N(Q[2^j])|\in\{1,4\}.
\]

The kernel formula gives

\[
|N[2^j]|=\frac{|Q[2^j]|}{|f_N(Q[2^j])|},\qquad
|M[2^j]|=\frac{|Q[2^j]|}{|f_M(Q[2^j])|}.
\]

Since (N\cong M), the two image orders are equal for every (j).

Because (f_M) is onto (C_4), a 2-power-order element of (Q) maps to a generator: from any preimage, raise to its odd-order part, which changes the image only by an odd power. Let (j\ge2) be least such that (f_M(Q[2^j])=C_4). Squaring such an element shows that (f_M(Q[2^{j-1}])) contains the involution of (C_4); minimality shows it is not all of (C_4). Therefore its order is 2, contradicting the possible orders 1 and 4 for the corresponding (f_N)-image.

Thus (K), and hence (L\cong K), is nonabelian. If (N\le Z(L)), the cyclic quotient (L/N\cong C_4) would make (L/Z(L)) cyclic and hence (L) abelian. Therefore (N\not\le Z(L)).

## Why the global characteristic route stops here

The induced index-four pair alone admits the hand example

\[
Q=C_4\times C_2,\qquad
N_0=\langle a^2\rangle\cong C_2,\qquad
M_0=\langle b\rangle\cong C_2,
\]

with (Q/N_0\cong V_4) and (Q/M_0\cong C_4). In this example the square and Frattini subgroup lies in one selected kernel but not the other. Thus derived, power, Frattini, Fitting, or transfer placement cannot be treated as intrinsic unless one first justifies that the abstract isomorphism respects the selected common kernel.

No arbitrary-(N) invariant eliminating the full common-(C_3) branch was found. Under Lead's strict 30-minute kill criterion, this direction therefore stops with `PARTIAL_RESULT` rather than reformulating the same obstruction.

## What this does not establish

- It does not construct a witness.
- It does not show that no witness exists.
- It does not eliminate the common-(C_3) branch for nonabelian coordinate kernels with even, odd-core-free (N).
- It does not turn the reviewed Q8/D8 order-128 template exclusions into a statement about arbitrary kernels or arbitrary extensions.
- Validator review of the new hand arguments was requested and was still pending when this direction stopped.
