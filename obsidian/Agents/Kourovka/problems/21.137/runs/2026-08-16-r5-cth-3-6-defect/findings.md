---
title: "CTH-3-6-DEFECT failure certificate for 21.137"
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
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
experiment: CTH-3-6-DEFECT
ended_utc: 2026-08-16T15:51:07Z
block_active_minutes_used: 17
shared_active_minutes_at_end: 145
---

# CTH-3-6-DEFECT: exact nondivisible-coordinate failure

## Active target

Scope: `21.137/odd-prime-exponent-p2`

Assignment revision: 2

Target statement: Let \(p\) be an odd prime and \(G\) a finite \(p\)-group of exponent exactly \(p^2\). If the set \(P=\{g^p:g\in G\}\) of \(p\)-th powers is a subgroup of \(G\), then \(P\) is abelian.

## Outcome

`STRATEGY_EXHAUSTED`: the frozen CTH-3-5 right side cannot be lifted to class 6 by the exact ten-element closure-certified correction span prescribed by Lead.

The hard-kill certificate is an integral Hall coordinate equal to \(-1\), hence not divisible by 3.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | treatment in this outcome | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every qualifying odd \(p,G\) | Experiment fixes \(p=3\), class 6, solely to test one proof lift. | not addressed unrestricted |
| `21.137-odd-p-not-2` | admissibility | \(p>2\) prime | Fixed prime is 3. | pass for experiment |
| `21.137-odd-finite-p-group` | admissibility | finite same-prime \(p\)-group | Free-word failure certificate would specialize to the proposed partial family, but no theorem about all such groups is claimed. | contextual only |
| `21.137-odd-exponent-p2` | admissibility | exact exponent \(p^2\) | Proposed lift targets exponent 9; the lattice \(9L+3\langle U\rangle\) encodes ninth-power and cube-subgroup corrections. | pass for experiment |
| `21.137-odd-power-set-definition` | admissibility | actual values, not verbal subgroup only | Frozen \(U\) contains only commutators derived from exact words \(T_A,T_B\) whose actual-value membership was reviewed. | pass for experiment |
| `21.137-odd-power-set-subgroup` | admissibility | actual value set is a subgroup | Supplies normal-closure membership for the frozen \(U\); no new generators were added. | pass for experiment |
| `21.137-odd-P-abelian` | target conclusion | \(P\) abelian | The class-6 lift fails before producing an identity. | not established |

## Exact object

No finite group and no computational quotient was tested. The hand calculation is in
\[
F_6=F(x,y)/\gamma_7F,
\qquad L=\gamma_6F_6,
\]
where \(L\) is free abelian of Hall rank 9.

## Frozen words and defect

Use
\[
c=[y,x],\ a=[c,x],\ b=[c,y],\ \alpha=[a,x],\ \beta=[a,y],\
\gamma=[b,y],
\]
\[
s=[\alpha,y],\quad t=[\beta,y],\quad
\delta=[a,c],\quad\varepsilon=[b,c].
\]
Retain the exact reviewed definitions
\[
T_A=(c^3a^3)^{-1}[y,x^3],\quad S_A=[T_A,y],
\]
\[
T_B=(q_1^3q_2^3)^{-1}[x,y^3],\quad Q=[T_B,x],
\quad q_1=[x,y],\ q_2=[q_1,y].
\]
The frozen class-5 right side in \(F_6\) is
\[
R_5=c^{-9}a^{-9}b^{-9}\beta^{-9}\delta^{54}\varepsilon^{27}
T_A^{-3}S_A^{-3}T_B^3Q^3.
\]
Set
\[
D=[x^3,y^3]R_5^{-1}\in L.
\]

## Failure certificate

In the weight-6 Hall basis, take
\[
h_3=[[\alpha,y],y]=[s,y].
\]
Then
\[
\boxed{\operatorname{coord}_{h_3}(D)=-1.}
\tag{*}
\]

For the left side, let \(v_1=[x^3,y]\), \(v_2=[v_1,y]\), and \(v_3=[v_2,y]\). The exact three-conjugate identity is
\[
[x^3,y^3]=v_1^3v_2^3v_3[v_2,v_1].
\]
Modulo weight 6,
\[
v_2\equiv b^{-3}\beta^{-3}s^{-1}\varepsilon^6.
\]
Thus \(v_3=[v_2,y]\) contributes exactly \([s^{-1},y]=h_3^{-1}\). Every other weight-6 contribution has Hall type \(h_7=[\beta,c]\) or \(h_9=[b,a]\), not \(h_3\). Hence
\[
\operatorname{coord}_{h_3}([x^3,y^3])=-1.
\]

On the frozen right side:

- the explicit basic powers and \(T_A,T_B\) have zero \(h_3\)-coordinate;
- \(S_A=s[\delta,y]\), with \([\delta,y]=h_7h_9^{-1}\), so it has none;
- writing \([\gamma,x]=t\varepsilon K\) with \(K\in L\), a degree-6 Magnus/BCH comparison gives \(\operatorname{coord}_{h_3}(K)=0\): the \(h_3\)-coefficient of \(\log[\gamma,x]\) and of \(\log t\) is 1, while \(\log\varepsilon\) has coefficient 0;
- therefore \(Q=[T_B,x]\) and all of \(R_5\) have zero \(h_3\)-coordinate.

This gives (*).

Every element of
\[
9L+3\langle U\rangle
\]
has all Hall coordinates divisible by 3, independently of the ten frozen vectors \(U\). Since \(-1\notin3\mathbb Z\),
\[
D\notin9L+3\langle U\rangle.
\]
No linear solve or span expansion is needed or permitted.

## What this rules out

It rules out the named `CTH-3-6-DEFECT` mechanism: the reviewed class-5 identity cannot be repaired at weight 6 using ninth powers plus three times the exact frozen normal-commutator span. The failure is exact and occurs before reduction modulo 3.

## What this does NOT establish

- It does not refute the \(p=3\), class-at-most-6 theorem itself; a different identity or genuinely different mechanism could exist.
- It does not affect the reviewed \(p=3\), class-at-most-5 partial theorem.
- It does not address primes above 3, unbounded class, or the unrestricted active scope.
- It does not authorize expanding \(U\), changing class/prime, or reopening compatible-root, Jennings, counterexample, or wreath routes.
- It is a hand certificate awaiting independent reconstruction; no algebraic computation was run.

## Why this strategy is exhausted

The named strategy's mandatory lattice membership fails its first divisibility gate. Its permitted parameter set and correction span were frozen, so there is no in-strategy repair.

A next route must change representation rather than add ad hoc Hall generators. Selecting that route belongs to Lead after MathExpert review; no alternative experiment was started in this block.

## How I could be wrong

1. The \(h_3^{-1}\) contribution from \(v_3\) might be canceled by an overlooked \(h_3\) term in \(v_1^3\), \(v_2^3\), or \([v_2,v_1]\); the multidegree/weight audit excludes those terms and Validator should reconstruct it.
2. The exact word \(Q\) could contain an \(h_3\) correction if the degree-6 logarithmic comparison of \([\gamma,x]\) with \(t\varepsilon\) has a sign or coefficient error.
3. The order of factors in \(R_5\) could create a weight-6 interchange. The only out-of-Hall-order terminal moves have weights summing above 6; this should be checked independently.
4. The defect convention could be reversed. Replacing \(D=CR_5^{-1}\) by its inverse changes \(-1\) to \(+1\), which remains nondivisible by 3 and does not alter the kill.

## Evidence

The timestamped derivation, nine-element Hall basis, command record, and complete scope restrictions are in `Agents/Kourovka/problems/21.137/runs/2026-08-16-r5-cth-3-6-defect/log.md`.
