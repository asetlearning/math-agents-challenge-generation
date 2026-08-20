---
title: "Constituent-independent parity obstruction for {39,25,10;1,5,30}"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/distance-regular-graphs
  - project/kourovka
  - status/conjectured
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# Constituent-independent parity obstruction

## Claim under review

No distance-regular graph has intersection array

\[
\{39,25,10;1,5,30\}.
\]

This eliminates the current parameter array independently of the isomorphism type of its proposed `srg(300,65,10,15)` distance-3 constituent. It does not eliminate the other feasible parameter arrays and does not answer the full existential Problem 21.90.

## One-line intersection-array proof

For a distance-regular graph of valency `k=b_0=39`,

\[
a_1=k-b_1-c_1=39-25-1=13.
\]

Fix a vertex `u`. Its local graph induced on `Gamma_1(u)` has `k=39` vertices and is `a_1=13` regular: for each neighbour `v` of `u`, exactly `a_1` neighbours of `v` remain at distance one from `u`. Its degree sum would therefore be

\[
39\cdot 13=507,
\]

which is odd. This contradicts the handshake lemma. Equivalently, every feasible distance-regular intersection array must satisfy `k a_1` even.

## Same obstruction directly from the frozen incidence system

Assume the requested symmetric binary matrix `M=I+A_1` exists and satisfies

\[
M^2=25I+10M+5J-5B,
\qquad M\circ B=0,
\]

with diagonal one and row weight 40. Fix `u` and let

\[
D=C_u\setminus\{u\}=\{v\ne u:M_{uv}=1\}.
\]

Then `|D|=39`. For `v in D`, support disjointness gives `B_uv=0`, so

\[
|C_u\cap C_v|=(M^2)_{uv}=10+5=15.
\]

The intersection contains `u` and `v`. Its other 13 points are exactly the vertices `w in D\setminus\{v\}` with `M_vw=1`. Hence the off-diagonal relation induced by `M` on the 39-point set `D` is 13-regular, again contradicting the handshake lemma.

This uses only integrality, symmetry, the diagonal/support conditions, and the frozen Gram identity. Consequently there is no need to continue to `p`-rank or Smith-form tests for this array: the integral system is already inconsistent.

## Reproducibility check

The arithmetic check (not needed for the proof) was:

```bash
python3 - <<'PY'
k,b1,c1=39,25,1
a1=k-b1-c1
print(f'a1={a1}')
print(f'local_degree_sum=k*a1={k*a1}')
print(f'even_required={(k*a1)%2==0}')
PY
```

Observed output:

```text
a1=13
local_degree_sum=k*a1=507
even_required=False
```

## Scope boundary

This is a candidate `PARTIAL_RESULT` pending Validator review. It supersedes the need to study asymmetric fissions of this array but does not supersede the reviewed fixed-polar computation as historical bounded evidence. No uniqueness of `srg(300,65,10,15)` is assumed or needed.

