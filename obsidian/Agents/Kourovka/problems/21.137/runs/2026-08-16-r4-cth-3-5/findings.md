---
title: "Partial result for 21.137: CTH-3-5 cube-subgroup abelianity"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/hall-collection
  - project/kourovka
  - status/conjectured
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
outcome: PARTIAL_RESULT
active_assignment_answered: no
review_state: awaiting_validator
experiment: CTH-3-5
ended_utc: 2026-08-16T15:10:27Z
block_active_minutes_used: 13
shared_active_minutes_at_end: 128
---

# Partial result: the \(p=3\), class-at-most-5 family

## Active target

Scope: `21.137/odd-prime-exponent-p2`

Assignment revision: 2

Target statement: Let \(p\) be an odd prime and \(G\) a finite \(p\)-group of exponent exactly \(p^2\). If the set \(P=\{g^p:g\in G\}\) of \(p\)-th powers is a subgroup of \(G\), then \(P\) is abelian.

## The partial-result claim

Let \(G\) be a finite 3-group of exponent exactly 9 and nilpotency class at most 5. If the actual cube-value set
\[
P=\{g^3:g\in G\}
\]
is a subgroup, then \(P\) is abelian.

This adds the first closure-dependent layer beyond the reviewed general class-at-most-\(p+1\) theorem when \(p=3\). It does not answer the unrestricted active target.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / proof use | evidence | result |
|---|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every qualifying odd \(p,G\) | Only \(p=3\) and the extra family \(\operatorname{cl}(G)\le5\). | Claim and argument | fail unrestricted; pass for stated partial family |
| `21.137-odd-p-not-2` | admissibility | \(p>2\) prime | \(p=3\). | Fixed specialization | pass |
| `21.137-odd-finite-p-group` | admissibility | finite \(p\)-group for the same prime | \(G\) is a finite 3-group. The word identity itself does not need finiteness. | Claim | pass |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly \(p^2\) | \(\exp G=9=3^2\); kills all displayed ninth powers and makes every actual cube have order dividing 3. | §§1 and 5 | pass |
| `21.137-odd-power-set-definition` | admissibility | actual values, not merely the generated verbal subgroup | Every auxiliary \(T_A,S_A,T_B,Q\) is shown to belong to the actual value set via displayed cubes, conjugacy invariance, and closure. | §§2–3 | pass |
| `21.137-odd-power-set-subgroup` | admissibility | the actual cube set is a subgroup | Essential for products, inverses, and commutators of displayed actual cubes to remain in \(P\). | §§1–3 | pass |
| `21.137-odd-P-abelian` | target conclusion | \(P\) abelian | The integral identity gives \([x^3,y^3]=1\) for all \(x,y\) in the stated class-at-most-5 family. | §§4–5 | claimed for partial family; unproved unrestricted |

## What I computed in

No algebraic computation was run. The hand calculation takes place in the torsion-free free two-generator nilpotent group
\[
F=F(x,y)/\gamma_6F.
\]
It gives an integral word identity through weight 5, which can then be specialized to every source-admissible group in the additional \(p=3\), class-at-most-5 family.

## Argument and certificate

Use \([u,v]=u^{-1}v^{-1}uv\) and \(u^v=v^{-1}uv\). Fix the following Hall basis coordinates:
\[
\begin{array}{c|l}
2&c=[y,x]\\
3&a=[c,x],\quad b=[c,y]\\
4&\alpha=[a,x],\quad \beta=[a,y],\quad \gamma=[b,y]\\
5&r=[\alpha,x],\quad s=[\alpha,y],\quad t=[\beta,y],\quad
u=[\gamma,y],\quad \delta=[a,c],\quad \varepsilon=[b,c].
\end{array}
\tag{H}
\]
Weight 5 is central. The top-weight Jacobi relation is
\[
[\gamma,x]=t\varepsilon.\tag{J}
\]

### 1. Consequences of actual-value closure

In a group of exponent 9, every element of the actual cube set has order dividing 3. If that set \(P\) is a subgroup, then it is normal because cube values are conjugacy-invariant. Thus
\[
z\in P\Longrightarrow z^{-1},z^g,[z,g]\in P.
\tag{P}
\]

### 2. The first coupled terminal vector

Direct collection gives
\[
A=[y,x^3]=c^3a^3\alpha\delta.
\tag{A}
\]
Also
\[
A=(x^{-3})^yx^3\in P,
\]
and \(c^3,a^3\in P\) are actual cubes. Hence
\[
T_A=(c^3a^3)^{-1}A=\alpha\delta\in P,
\qquad
S_A=[T_A,y]=s\in P.
\tag{TA}
\]

### 3. The swapped coupled vector and its closure-certified conjugate

Put
\[
q_1=[x,y]=c^{-1},qquad
q_2=[q_1,y]=b^{-1}\varepsilon.
\]
Collection gives
\[
B=[x,y^3]=q_1^3q_2^3\gamma^{-1}\varepsilon.
\tag{B}
\]
Since \(B=(y^{-3})^xy^3\in P\), while \(q_1^3,q_2^3\) are actual cubes,
\[
T_B=\gamma^{-1}\varepsilon\in P.
\tag{TB}
\]
Using (J) and (P),
\[
Q=[T_B,x]=t^{-1}\varepsilon^{-1}\in P.
\tag{Q}
\]

Thus all four vectors \(T_A,S_A,T_B,Q\) used below have explicit membership in the actual value subgroup. No verbal-subgroup inference is used.

### 4. Integral Hall vector of \(C=[x^3,y^3]\)

Let \(v_1=[x^3,y]=A^{-1}\), \(v_2=[v_1,y]\), and \(v_3=[v_2,y]\). Collection through weight 5 gives
\[
\begin{aligned}
v_1&=c^{-3}a^{-3}\alpha^{-1}\delta^8,\\
v_2&=b^{-3}\beta^{-3}s^{-1}\varepsilon^6,\\
v_3&=\gamma^{-3}t^{-3},\\
[v_2,v_1]&=\varepsilon^9.
\end{aligned}
\tag{C1}
\]
Since
\[
C=v_1^3v_2^3v_3[v_2,v_1],
\]
one obtains the integral Hall form
\[
C=c^{-9}a^{-9}b^{-9}\alpha^{-3}\beta^{-9}\gamma^{-3}
  s^{-3}t^{-3}\delta^{51}\varepsilon^{27}.
\tag{C2}
\]
The exponent 51 is independently exposed by
\[
v_1^3=c^{-9}a^{-9}\alpha^{-3}\delta^{,3\cdot8+\binom32\cdot9}
     =c^{-9}a^{-9}\alpha^{-3}\delta^{51}.
\]

Thus, in the fixed terminal coordinate order
\[
(\alpha,\beta,\gamma;r,s,t,u;\delta,\varepsilon),
\]
the requested integral vectors are
\[
\begin{array}{c|c}
A\text{ after stripping }c^3,a^3
  &(1,0,0;0,0,0,0;1,0)\\
B\text{ after stripping }q_1^3,q_2^3
  &(0,0,-1;0,0,0,0;0,1)\\
C\text{ before deleting ninth powers}
  &(-3,-9,-3;0,-3,-3,0;51,27).
\end{array}
\tag{T}
\]

remove ninth-power entries, divide the remainder by 3, and reduce modulo 3. This gives
\[
\bar v_C=(-1,0,-1;0,-1,-1,0;-1,0).
\]
The closure-certified terminal vectors satisfy
\[
\bar v_C=-v_{T_A}-v_{S_A}+v_{T_B}+v_Q.
\tag{R}
\]
There is no coordinate outside the certified span; the assigned hard-kill criterion does not fire.

### 5. Integral success identity and specialization

The vector relation lifts to the explicit integral identity in \(F\):
\[
\boxed{
[x^3,y^3]
=c^{-9}a^{-9}b^{-9}\beta^{-9}\delta^{54}\varepsilon^{27}
  T_A^{-3}S_A^{-3}T_B^3Q^3.}
\tag{I}
\]
Every factor preceding \(T_A^{-3}\) is a ninth power. Every subsequent factor is a cube or inverse cube of an element explicitly shown in (TA), (TB), and (Q) to lie in the actual cube subgroup \(P\).

After specialization to \(G\), exponent 9 kills the first six factors. Since \(P\) has exponent dividing 3, it kills the remaining four. Therefore
\[
[x^3,y^3]=1\qquad(x,y\in G).
\]
Every pair of actual cubes commutes, so the subgroup \(P\) is abelian.

## What this does NOT establish

- It does not handle any odd prime \(p>3\).
- It does not handle 3-groups of class greater than 5.
- It does not answer the unrestricted revision-2 target or the broader powerfulness question.
- It does not say that cube closure follows from the exponent or class assumptions; closure is essential to certify \(T_A,S_A,T_B,Q\in P\).
- It makes no use of, and no claim about, compatible-root, Jennings, counterexample, or wreath constructions.
- The identity is a hand derivation awaiting independent reconstruction; no algebraic collector was run.

## How I could be wrong

1. Inverting \(A=c^3a^3\alpha\delta\) could give the wrong central correction; the submitted value \(A^{-1}=c^{-3}a^{-3}\alpha^{-1}\delta^8\) uses \(a^{-3}c^{-3}=c^{-3}a^{-3}\delta^9\).
2. The top Hall relation could have a sign error. With the stated convention, the graded Jacobi calculation gives \([\gamma,x]=[\beta,y][b,c]=t\varepsilon\); this controls the cancellation of the \(\varepsilon\)-coordinate.
3. The cube of \(v_1\) could miss a class-two correction. The displayed \(\delta^{51}\) includes both \(3\cdot8\) and \(\binom32\cdot9\).
4. A product asserted to lie in \(P\) would be invalid without actual-value closure. The proof therefore displays separately how each of \(T_A,S_A,T_B,Q\) is obtained from known members of the actual set and its normal subgroup operations.
5. Identity (I) could fail if reordering created a weight-at-most-5 term. All its terminal factors lie in \(\gamma_4F\), which commutes with \(\gamma_2F\) modulo \(\gamma_6F\), and all weight-5 factors are central; Validator should reconstruct this explicitly.

## Evidence

The timestamped derivation, full intermediate coordinates, scope restrictions, and command record are in `Agents/Kourovka/problems/21.137/runs/2026-08-16-r4-cth-3-5/log.md`. No web search, historical solution material, compatible-root route, wreath route, GAP, bespoke collector, or other algebraic computation was used.
