---
title: "Kourovka 12.15 — R3 defect-size inconsistency blocking M1"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/conjectured
problem: "12.15"
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
direction: proof
outcome: BLOCKER
state: awaiting_lead
---

# Exact inconsistency

Let \(H=G'\), \(A=Z(H)\), and take the basic commutator \(c\in H\) used in R3. The reviewed rows give

\[
|G:H|=4,\qquad |H|=32,\qquad |A|=8,\qquad H/A\cong C_2^2.
\]

Because \(A\le C_H(c)\), and because \(c\) centralizes itself, \(A\langle c\rangle\le C_H(c)\). If \(c\notin A\), then \(cA\) has order \(2\) and \(|A\langle c\rangle|=16\); if \(c\in A\), then \(C_H(c)=H\). Therefore

\[
|c^H|\le2.
\]

Normality of \(H\) gives

\[
|c^G|
=|G:C_G(c)|
\le |G:H|\,|H:C_H(c)|
\le4\cdot2=8. \tag{1}
\]

For a qualifying group, the audited fibre identity is

\[
c^G=cD_G(c),
\]

so multiplication by \(c\) yields

\[
|D_G(c)|=|c^G|\le8. \tag{2}
\]

But the audited R3 row and the M1 assignment require

\[
A\le D_G(c),\qquad |D_G(c)|=16,
\]

equivalently that \(D_G(c)\) have a nonzero-line image in \(H/A\). This contradicts (2).

# Why this blocks the assigned M1 test

The square-orbit test assumes an abelian index-two extension \(A<D=D_G(c)\), so that \(D/A\cong C_2\) and \(q(D)\) may acquire one generator beyond \(q(A)=A^2\). Equation (2) instead forces \(D_G(c)=A\) if the containment \(A\le D_G(c)\) is retained. The permitted \(q(D)\), and hence every orbit comparison, changes.

I will not silently repair the reviewed R3 row. Validator must decide whether:

1. the line-image/order-\(16\) deduction was mistaken, in which case M1 must be reformulated with \(D_G(c)=A\); or
2. that deduction is sound, in which case (1)--(2) eliminate R3 immediately and should be audited as a partial result.

# Work completed before the stop

The exact bounded enumeration in [[scratch/m1_action_orbits.py]] found, up to \(\operatorname{Aut}(A)\)-conjugacy and relabeling of \(E\), one faithful \(E=C_2^2\) action with \(A^E=\langle z\rangle\) for each of

\[
C_8,\qquad C_4\times C_2,\qquad C_2^3.
\]

Its raw output is [[scratch/m1_action_orbits.out]]. These action calculations remain diagnostic only until the R3 defect-size row is corrected or validated.
