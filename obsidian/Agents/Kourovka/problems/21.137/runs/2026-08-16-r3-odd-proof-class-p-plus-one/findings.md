---
title: "Partial result for 21.137: commuting p-th powers through class p+1"
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
ended_utc: 2026-08-16T14:36:27Z
block_active_minutes_used: 19
shared_active_minutes_at_end: 115
---

# Partial result: the class-at-most-\(p+1\) family

## Active target

Scope: `21.137/odd-prime-exponent-p2`

Assignment revision: 2

Target statement: Let \(p\) be an odd prime and \(G\) a finite \(p\)-group of exponent exactly \(p^2\). If the set \(P=\{g^p:g\in G\}\) of \(p\)-th powers is a subgroup of \(G\), then \(P\) is abelian.

## The partial-result claim

For every odd prime \(p\), if a group \(G\) has exponent dividing \(p^2\) and nilpotency class at most \(p+1\), then
\[
[x^p,y^p]=1\qquad\text{for all }x,y\in G.
\]
Consequently the active target has an affirmative answer for the additional class-bounded family \(\operatorname{cl}(G)\le p+1\), without needing the actual-power-set closure hypothesis.

This strengthens the previously reviewed class-at-most-\(p\) partial result by one class layer. It does not answer the unrestricted target.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / proof use | evidence | result |
|---|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every qualifying \(p,G\) | Uniform for every odd \(p\) and every qualifying \(G\) **with the extra restriction** \(\operatorname{cl}(G)\le p+1\). | Argument §§1–4 | pass for partial family; not the unrestricted quantifier |
| `21.137-odd-p-not-2` | admissibility | \(p>2\) prime | Primality gives \(p\mid\binom pi\) for \(0<i<p\); oddness gives \(p\mid\binom p2\). | §§1–2 | pass |
| `21.137-odd-finite-p-group` | admissibility | finite \(p\)-group for the same \(p\) | The source family is included; the submitted argument is stronger and uses neither finiteness nor the same-prime order condition beyond the source application. | Fixed hypotheses and §5 | pass for partial family |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly \(p^2\) | The argument assumes the stronger-inclusive condition \(\exp G\mid p^2\), so it applies when the source exponent is exactly \(p^2\). | §§1–2 and §4 | pass |
| `21.137-odd-power-set-definition` | admissibility | \(P\) is the actual value set | The final identity is pairwise for the actual values \(x^p,y^p\). The auxiliary \(K=\langle g^p:g\in G\rangle\) is explicitly distinguished from the value set. | Fixed notation and §§2–5 | pass |
| `21.137-odd-power-set-subgroup` | admissibility | the actual value set \(P\) is a subgroup | Not needed for pairwise commutation; under the source hypothesis it makes \(P=K\), hence an abelian subgroup. | §5 | pass |
| `21.137-odd-P-abelian` | target conclusion | \(P\) abelian | Obtained only when \(\operatorname{cl}(G)\le p+1\); no conclusion is submitted for higher class. | §§4–5 | established by submitted argument for partial family; **not proved unrestricted** |

## What I computed in

No computation was run. This is a hand Hall-collection argument in an arbitrary group of exponent dividing \(p^2\) and class at most \(p+1\). Integral coordinates are formed first in the torsion-free free two-generator nilpotent group and only then specialized to \(G\).

## Argument

Use
\[
[u,v]=u^{-1}v^{-1}uv,
\qquad u^v=v^{-1}uv,
\]
with higher commutators left-normed.

### 1. Integral Hall-coordinate divisibility

Fix an ordered Hall basis in the torsion-free free nilpotent group on \(X,Y\) of class \(p+1\). For a mixed basic commutator \(b\) of multidegree \((r,s)\), write its coordinate in \([X^m,Y^n]\) as \(f_b(m,n)\). The separate Hall degree bounds and the integral binomial basis give
\[
f_b(m,n)=
\sum_{i=1}^{r}\sum_{j=1}^{s}
a_{b,i,j}\binom mi\binom nj,
\qquad a_{b,i,j}\in\mathbb Z.
\tag{1}
\]
The zero-index terms are absent because the whole commutator is trivial when either power parameter is zero, and Hall coordinates are unique in this torsion-free free object.

If \(r+s\le p\), then \(r,s\le p-1\), so (1) makes \(f_b(p,p)\) divisible by \(p^2\). Therefore, after specializing to an exponent-dividing-\(p^2\) group,
\[
[x^p,y^p]\in\gamma_{p+1}(G).
\tag{2}
\]
At weight \(p+1\), all non-extreme multidegrees still have \(r,s<p\), so their coordinates are divisible by \(p^2\). The only exceptional multidegrees are \((p,1)\) and \((1,p)\); (1) still makes each exceptional coordinate divisible by \(p\).

### 2. The generated-power subgroup has exponent dividing \(p\)

Put
\[
S=\{g^p:g\in G\},\qquad K=\langle S\rangle.
\]
The equalities
\[
(g^p)^{-1}=(g^{-1})^p,
\qquad (g^p)^h=(g^h)^p
\]
show that \(S\) is inverse-closed and conjugacy-invariant, hence \(K\unlhd G\).

Every \(s\in S\) has \(s^p=1\). By (2), for \(s,t\in S\),
\[
[s,t]\in\gamma_{p+1}(G)\le Z(G).
\]
Thus \(K'\le Z(G)\), and centrality gives
\[
[s,t]^p=[s^p,t]=1.
\tag{3}
\]

It remains to cover arbitrary products, not just generators. Write \(k=s_1\cdots s_n\) with \(s_i\in S\), possible because \(S\) is inverse-closed. Induct on \(n\). If \(a=s_1\cdots s_{n-1}\), then \([s_n,a]\) is a product of the central order-dividing-\(p\) commutators in (3). Hence, using the class-two product formula,
\[
(a s_n)^p
=a^p s_n^p [s_n,a]^{\binom p2}=1,
\]
because \(p\mid\binom p2\). Therefore
\[
\exp K\mid p.
\tag{4}
\]
This proves (4) before any extreme commutator is placed in \(K\), so the argument is not circular.

### 3. The unique multidegree \((p,1)\) term lies in \(K\)

Let \(H=G/K\). It has exponent dividing \(p\). Collect
\[
1=[\bar y,\bar x^p]
\tag{5}
\]
in \(H\). If a coordinate in (5) has \(X\)-degree \(r<p\), formula (1), with the \(X\)-parameter set to \(p\), makes that coordinate divisible by \(p\); its factor is therefore trivial in \(H\). If \(r=p\), the class bound forces the other degree to be 1.

The multidegree-\((p,1)\) free-Lie component has rank
\[
\frac1{p+1}\binom{p+1}{p,1}=1.
\tag{6}
\]
Its one coefficient in (5) is a unit. To see this integrally, kill all commutators containing at least two copies of \(Y\), and put \(c_k=[Y,{}_{k}X]\). Induction from \(u^X=u[u,X]\) gives
\[
[Y,X^m]\equiv\prod_{k\ge1}c_k^{\binom mk}.
\tag{7}
\]
The coefficient of \(c_p\) at \(m=p\) is \(\binom pp=1\), up to inversion if the Hall orientation is reversed. By (5), every other factor has already died individually, so this unique factor is trivial in \(H\). Consequently
\[
[y,{}_{p}x]\in K.
\tag{8}
\]
Swapping \(x,y\) gives the same conclusion for the unique multidegree \((1,p)\) basic commutator.

### 4. Final collection

Return to the collected form of \([x^p,y^p]\) in \(G\). Every non-extreme coordinate is divisible by \(p^2\), so its factor vanishes under \(\exp G\mid p^2\). The two extreme coordinates are divisible by \(p\); their underlying basic commutators lie in \(K\) by (8) and its swapped form, and vanish by (4). Thus
\[
[x^p,y^p]=1
\]
for arbitrary \(x,y\in G\).

### 5. Application to the active partial family

For a source-admissible finite \(p\)-group of exact exponent \(p^2\) and class at most \(p+1\), all actual \(p\)-th-power values commute pairwise. If their value set \(P\) is a subgroup, then \(P=K\) and \(P\) is abelian.

## Exact first obstruction at class \(p+2\)

The above quotient isolation no longer works from Hall divisibility alone. In class at most \(p+2\), both multidegrees \((p,1)\) and \((p,2)\) can survive in (5), and the latter has free-Lie rank
\[
\frac1{p+2}\binom{p+2}{p,2}=\frac{p+1}{2}.
\]
The binomial expansion of a \((p,2)\) coordinate can include an \(X\)-index-\(p\), \(Y\)-index-1 term, so divisibility no longer removes it.

At \(p=3\) the contamination is explicit. In class at most 5, let
\[
c_1=[y,x],\quad c_2=[c_1,x],\quad c_3=[c_2,x],\quad d=[c_2,c_1].
\]
Since \(d\) has weight 5 it is central, and direct collection gives
\[
[y,x^3]=c_1^3c_2^3c_3d.
\tag{9}
\]
In an exponent-3 quotient, (9) reduces to \(c_3d=1\), not \(c_3=1\). Thus the extreme \((3,1)\) term is coupled to a terminal \((3,2)\) term. Further exponent identities might repair or cancel this coupling; this submission makes no class-\(p+2\) assertion.

## What this does NOT establish

- It does not prove the active target for groups of class greater than \(p+1\).
- It does not show that the class-\(p+2\) lemma is false; it identifies the precise failure of this isolation argument.
- It does not use actual-value closure to control roots in higher class.
- It does not provide a counterexample, a finite coverage result, or a solution to any excluded \(p=2\) clause.
- No computation or external literature search supports this claim; Validator must check the hand collection argument independently.

## How I could be wrong

1. The Hall coordinate formula (1) could have been applied with an incorrect separate multidegree bound; it must be checked in the torsion-free free nilpotent group before specialization.
2. The passage from (7) to a unit coordinate could fail if killing the two-\(Y\) subgroup changed the unique \((p,1)\) coordinate; multidegree separation is meant to prevent this and should be checked explicitly.
3. The arbitrary-product induction for (4) requires every commutator of power generators to be central in \(G\), not merely central modulo a lower-central term; this is exactly where the class bound \(p+1\) is used.
4. A Hall-order or commutator-orientation mismatch can invert the two extreme factors. Only unit status and membership in \(K\) are used, so inversion should not affect the conclusion, but the conventions should be reconstructed.
5. Formula (9) may acquire the inverse of \(d\) under a different collection order. Its role is only to show a nonzero coupled top coordinate; Validator should check the sign/order independently.

## Evidence

The full source gate, curated-context record, active-time ledger, terminal-exponent audit, and derivations are in `Agents/Kourovka/problems/21.137/runs/2026-08-16-r3-odd-proof-class-p-plus-one/log.md`. The rendered source page is `scratch/source-page-184.png` below this run directory. No mathematical computation was run.
