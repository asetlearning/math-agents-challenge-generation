---
title: "ALG3-UT7-CUBE-IMAGE — frozen F_12 family exhausted"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: ALG3-UT7-CUBE-IMAGE
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/algebra-groups
  - project/kourovka
  - status/conjectured
---

# Frozen-family outcome

`STRATEGY_EXHAUSTED` for `ALG3-UT7-CUBE-IMAGE/F_12` only. The complete 729-row manifest contains no target-equal candidate. This does not answer the unrestricted scope `21.137/odd-prime-exponent-p2`, gives no affirmative evidence beyond this family, and does not authorize scope retirement.

## Exact family exhausted

Over `F_3`, for every `tau in F_3^6`, set

- `S=E12+E23+E34+E45+E56+E67`;
- `T_tau=sum_i tau_i E_{i,i+1}`;
- `J_tau=<S,T_tau>` as a nonunital associative algebra;
- `G_tau=1+J_tau`.

The frozen family is exactly the rows satisfying

`tau_1 tau_2 tau_3 != tau_4 tau_5 tau_6` and `dim(J_tau)<=12`.

Of all 729 rows, 719 are outside that family. Exactly 10 rows lie in it; each has `dim(J_tau)=11`, and each fails the necessary leading-layer additivity gate for `C_tau={v^3:v in span_F3{S,T_tau}}`. Consequently the actual cube set cannot be a subgroup in any of those 10 rows. No row survives to the full `X_tau,K_tau` computation.

## Exact constraint-and-conclusion matrix

| constraint_id | role | required condition | frozen-family audit | evidence | result |
|---|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | One fully admissible witness would refute the universal target | No witness exists in the frozen `F_12` family; failure of this family does not address all admissible groups | Complete 729-row manifest | `not-satisfied`; universal target unresolved |
| `21.137-odd-p-not-2` | admissibility | `p` prime and `p>2` | Base field fixed exactly to `F_3`, so `p=3` | Script constants and hand audit | pass for every tested row |
| `21.137-odd-finite-p-group` | admissibility | finite same-prime `p`-group | Each `G_tau=1+J_tau` has order `3^dim(J_tau)`; the 10 retained rows have order `3^11` | Exact algebra bases/dimensions in manifest computation | pass for every retained row |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `9` | `S^3!=0`, while every ninth power is `1+x^9=1` because `J_tau^7=0` | Hand-audited identities and exact `S^3` self-test | pass for every retained row |
| `21.137-odd-power-set-definition` | admissibility | `P` is the set of actual cubes | `(1+x)^3=1+x^3`, so its degree-three projection is in `C_tau`; no generated-subgroup substitution is made | Hand audit and exact leading-cube evaluation | pass as the definition used |
| `21.137-odd-power-set-subgroup` | admissibility | actual cube set is a subgroup | Every retained row has saved `v,w` with `v^3+w^3 notin C_tau`; circle products change degree three by that sum, so actual cube closure is impossible | Ten explicit manifest witnesses | fail for every retained row |
| `21.137-odd-P-abelian` | target_conclusion | `P` is abelian | The endpoint inequality makes `1+S^3` and `1+T_tau^3` noncommuting in every retained row, but those rows fail the subgroup hypothesis | Endpoint products in every manifest row | violated as a raw value-set property, but never in an admissible witness |

There is therefore no row for which all six admissibility rows pass and the target-conclusion row is violated. This is not a `CLAIM`, and no claim-check JSON is appropriate.

## The ten retained rows and explicit rejection witnesses

The witness coefficients mean `v=aS+bT_tau` and `w=cS+dT_tau`. Matrix codes use the manifest's canonical 21-coordinate base-3 encoding.

| tau | dim J | size(C_tau) | `(a,b)` | `(c,d)` | code(v^3) | code(w^3) | code(v^3+w^3), absent from C_tau |
|---|---:|---:|---|---|---:|---:|---:|
| `(0,1,1,1,1,1)` | 11 | 7 | `(0,1)` | `(1,1)` | 130741047 | 261482103 | 9 |
| `(0,2,2,2,2,2)` | 11 | 7 | `(0,2)` | `(1,2)` | 130741047 | 261482103 | 9 |
| `(1,1,1,1,1,0)` | 11 | 7 | `(0,1)` | `(1,1)` | 1600893 | 132341949 | 129140163 |
| `(1,1,1,1,1,2)` | 11 | 7 | `(2,2)` | `(0,2)` | 1600893 | 132341949 | 129140163 |
| `(1,2,1,2,1,2)` | 11 | 5 | `(1,0)` | `(0,1)` | 130741056 | 132335388 | 258293448 |
| `(1,2,2,2,2,2)` | 11 | 7 | `(2,1)` | `(0,1)` | 130741047 | 261482103 | 9 |
| `(2,1,1,1,1,1)` | 11 | 7 | `(2,2)` | `(0,2)` | 130741047 | 261482103 | 9 |
| `(2,1,2,1,2,1)` | 11 | 5 | `(1,0)` | `(0,2)` | 130741056 | 132335388 | 258293448 |
| `(2,2,2,2,2,0)` | 11 | 7 | `(0,2)` | `(1,2)` | 1600893 | 132341949 | 129140163 |
| `(2,2,2,2,2,1)` | 11 | 7 | `(2,1)` | `(0,1)` | 1600893 | 132341949 | 129140163 |

### Hand-readable leading-layer certificate

Write a third-superdiagonal vector in coordinates `(E14,E25,E36,E47)`. The ten rows reduce, under reversing the six edges and invertible rescaling/reparametrizing of `span{S,T_tau}`, to three displayed patterns:

1. For `tau=(0,1,1,1,1,1)`, put `r=a` and `s=a+b`. Then
   `(aS+bT)^3=(r s^2,s,s,s)`.
   Thus `C_tau` consists of zero together with `(r,1,1,1)` and `(r,2,2,2)` for `r in F_3`, so it has size `7`. The saved values `(0,1,1,1)` and `(1,2,2,2)` sum to `(1,0,0,0)`, which is absent because a member with last three coordinates zero must have `s=0` and hence first coordinate zero.
2. Reversing the edges gives the rows with the exceptional coordinate at the right endpoint. Their saved values `(1,1,1,0)` and `(2,2,2,1)` sum to `(0,0,0,1)`, absent by the reversed argument. These are exactly the code triple `1600893`, `132341949`, `129140163`.
3. For `tau=(1,2,1,2,1,2)`, the invertible change `(a,b)->(r,s)=(a+b,a+2b)` gives
   `(aS+bT)^3=(r^2s,rs^2,r^2s,rs^2)`.
   Its image is zero plus the four vectors `(s,r,s,r)` with `r,s` nonzero, hence has size `5`. The saved values `(1,1,1,1)` and `(2,1,2,1)` sum to `(0,2,0,2)`, which is absent. Swapping `1` and `2` gives the other alternating row.

The manifest's other endpoint-constant rows are obtained from the first two patterns by the same invertible coefficient changes; the explicit saved coefficients in the table instantiate the witnesses rather than relying on the symmetry assertion.

### Hand audit of `dim(J_tau)=11` for the retained rows

The algebra is graded by superdiagonal, and its degree-`k` piece is spanned by the path-weight vectors of the `2^k` words of length `k` in `S,T_tau`.

- In an endpoint-constant row, five consecutive edge weights of `T_tau` are equal and only the first or last edge is exceptional. Every degree-`k` word is therefore constant on all starting positions except possibly the one whose length-`k` path meets that exceptional endpoint in the relevant letter. Hence its path vectors span at most the all-ones vector and one endpoint indicator. `S^k` and a word using `T_tau` at the exceptional endpoint show that both occur for `1<=k<=5`; degree `6` has only the `E17` coordinate. The degree ranks are `(2,2,2,2,2,1)`.
- In an alternating row, every word's path-weight sequence is two-periodic in the starting position, so the degree-`k` span has rank at most `2`. The all-ones word `S^k` and a word with one `T_tau` factor are independent while at least two starting positions remain, again giving ranks `(2,2,2,2,2,1)`.

Thus every retained row has `dim(J_tau)=2+2+2+2+2+1=11`, agreeing with the exact manifest. The exhaustive classification that no other endpoint-unequal row has dimension at most `12` remains computational evidence in the 729-row rank audit, not a claimed symbolic classification theorem.

## Reproducible evidence

- Primary exact enumerator: `Agents/Kourovka/problems/21.137/scratch/ut7_cube_image.py`.
- Approved command: `timeout 600s python3 Agents/Kourovka/problems/21.137/scratch/ut7_cube_image.py`.
- Exit status `0`; script wall time `2.6640472412109375` seconds.
- Complete manifest: `manifest.jsonl`, exactly 729 rows, SHA-256 `66a3825559b07c7a87691d64ce5ca9c35bb151427248faa04014a10ddb2534e2`.
- Summary: `summary.json`.
- Independent graded checker: `Agents/Kourovka/problems/21.137/scratch/ut7_cube_image_audit.py`. Its first sub-second run is explicitly non-evidentiary because it occurred after slot release. The exact sanctioned rerun `timeout 60s python3 Agents/Kourovka/problems/21.137/scratch/ut7_cube_image_audit.py` then exited `0` in `0.405591576` seconds under compute slot 1 and returned `PASS` on all 729 dimensions, statuses, and saved witnesses.
- Sanctioned independent output: `sanctioned-independent-audit.json`, SHA-256 `dc8f45aee5f784ddfb6c4a3c6f2a6765e25263c5ae9d724c227b11eac734107d`.

## What this does not establish

- It does not prove the active universal assertion.
- It does not construct an admissible counterexample.
- It says nothing about two-generator algebra groups in this template with `dim(J_tau)>12`.
- It says nothing about other algebras inside `UT_7(F_3)`, other generator choices, more generators, other odd primes, or non-algebra groups.
- A leading-layer rejection is only a necessary-condition failure for the tested row; no converse is claimed.

## Recommended pivot

Do not enlarge this frozen family within the present strategy. The hard kill is met exactly. Any further work should be a Lead-selected, materially different representation or a direction switch; it should not raise the dimension cutoff, add a generator, or reinterpret the absence of a witness as evidence for the unrestricted theorem.

Verified by [[Agents/Kourovka/problems/21.137/verification/2026-08-17T035316Z-alg3-ut7-family-exhaustion]].
