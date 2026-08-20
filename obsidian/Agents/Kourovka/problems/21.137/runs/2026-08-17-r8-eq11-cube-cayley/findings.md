---
title: "EQ11-CUBE-CAYLEY — frozen E_12 family exhausted"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: EQ11-CUBE-CAYLEY
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
  - status/replicated
---

# Bounded outcome

`STRATEGY_EXHAUSTED` for exactly `EQ11-CUBE-CAYLEY/E_12`. The complete eleven-row family contains no group whose actual cube-value set is simultaneously a subgroup and nonabelian:

- eight non-scalar rows have direct actual-value closure defects, each with two cube values, canonical cube roots, their circle product, and a complete actual-value manifest proving the product absent;
- three scalar rows have exact equality between the complete actual cube set and its Cayley-generated set, but a complete generator table is pairwise commuting.

This does not answer `21.137/odd-prime-exponent-p2`, supplies no candidate `CLAIM`, and gives no evidence outside the frozen family.

## Exact object computed in

Over `F_3`, for `tau in F_3^6`, let

- `S=E12+E23+E34+E45+E56+E67`;
- `T_tau=sum_i tau_i E_{i,i+1}`;
- `J_tau=<S,T_tau>` as a nonunital associative algebra of strict-upper-triangular `7 x 7` matrices;
- `G_tau=1+J_tau`.

The computed family is exactly

`E_12={tau : dim(J_tau)<=12 and tau_1 tau_2 tau_3=tau_4 tau_5 tau_6}`.

The leased selection pass found exactly the eleven frozen rows required by the assignment:

| tau | dim J | order of G | size of actual cube set | exact outcome |
|---|---:|---:|---:|---|
| `(0,0,0,0,0,0)` | 6 | `3^6=729` | 9 | exact Cayley equality; generator table commuting |
| `(0,0,0,0,0,1)` | 11 | `3^11=177147` | 171 | direct closure boundary |
| `(0,0,0,0,0,2)` | 11 | `3^11=177147` | 171 | direct closure boundary |
| `(0,1,0,1,0,1)` | 11 | `3^11=177147` | 123 | direct closure boundary |
| `(0,2,0,2,0,2)` | 11 | `3^11=177147` | 123 | direct closure boundary |
| `(1,0,0,0,0,0)` | 11 | `3^11=177147` | 171 | direct closure boundary |
| `(1,0,1,0,1,0)` | 11 | `3^11=177147` | 123 | direct closure boundary |
| `(1,1,1,1,1,1)` | 6 | `3^6=729` | 9 | exact Cayley equality; generator table commuting |
| `(2,0,0,0,0,0)` | 11 | `3^11=177147` | 171 | direct closure boundary |
| `(2,0,2,0,2,0)` | 11 | `3^11=177147` | 123 | direct closure boundary |
| `(2,2,2,2,2,2)` | 6 | `3^6=729` | 9 | exact Cayley equality; generator table commuting |

## Exact canonical constraint-and-conclusion matrix

| constraint_id | role | required condition | family evidence | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | One fully admissible witness would refute the universal target | No row in `E_12` passes subgroup closure and violates abelianness; family exhaustion cannot discharge the universal quantifier | not satisfied; unrestricted target open |
| `21.137-odd-p-not-2` | admissibility | `p` prime and `p>2` | Exact arithmetic over `F_3`; `p=3` | pass for every row |
| `21.137-odd-finite-p-group` | admissibility | finite same-prime `p`-group | Saved RREF bases give dimensions `6` or `11`, hence orders `3^6` or `3^11` | pass for every row |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `9` | `S^3=E14+E25+E36+E47 !=0`; `J_tau^7=0`, hence every `(1+x)^9=1` | pass for every row |
| `21.137-odd-power-set-definition` | admissibility | `P` is the actual set of cubes | Every one of `3^dim J_tau` inputs is recorded in the complete `x -> x^3` manifest; `(1+x)^3=1+x^3`; one canonical root is retained per value | pass for every row |
| `21.137-odd-power-set-subgroup` | admissibility | actual cube set is a subgroup | Eight rows have direct products of two actual values outside the complete value index; three scalar rows have exact Cayley-state/value-set equality | fail for eight rows; pass for three scalar rows |
| `21.137-odd-P-abelian` | target_conclusion | actual cube subgroup is abelian | The only three closure-passing rows have a complete pairwise-commuting table for their two Cayley generators; the other eight rows are tested no further after the subgroup hypothesis fails | pass for every admissible row in this family; not reached for the other eight |

No row passes all six admissibility gates and violates the target-conclusion row. A claim-check JSON is therefore neither required nor appropriate.

## Eight direct closure-boundary certificates

Matrix codes are the canonical base-3 encoding in the 21-position order saved in every row certificate. Root codes are coordinates in that row's saved canonical RREF basis. Each displayed equality was replayed exactly; each `w` is absent from that row's exhaustive actual-value/root index.

| tau rows | size(V_tau) | u code / root coord | b code / root coord | w = u circle b | sparse w |
|---|---:|---|---|---:|---|
| `(0,0,0,0,0,1)`, `(0,0,0,0,0,2)` | 171 | `3201786 / 2` | `6383862 / 19684` | 4782969 | `E37` |
| `(0,1,0,1,0,1)`, `(0,2,0,2,0,2)`, `(1,0,1,0,1,0)`, `(2,0,2,0,2,0)` | 123 | `81 / 2188` | `59049 / 738` | 59130 | `E16+E27` |
| `(1,0,0,0,0,0)`, `(2,0,0,0,0,0)` | 171 | `261482094 / 1458` | `130741056 / 730` | 9 | `E14` |

The full roots, sparse matrices, generator lists at the boundary, actual-value hashes, and row-specific replay data are in the eight `closure-boundary.json` artifacts below `rows/`.

## Three exact closure-equality and abelianness certificates

For `tau=(c,c,c,c,c,c)`, `T_tau=cS`, so `J_tau=span{S,S^2,...,S^6}` is commutative of dimension `6`. If `x=sum_{i=1}^6 a_i S^i`, Frobenius in this commutative characteristic-3 algebra gives

`x^3=a_1 S^3+a_2 S^6`.

Thus the actual cube set is exactly the nine-element plane `span_F3{S^3,S^6}`. It is circle-closed because

`(aS^3+bS^6) circle (cS^3+dS^6)=(a+c)S^3+(b+d+ac)S^6`,

and it is abelian because the ambient algebra is commutative. The computation independently records all `729` input-to-cube entries per scalar row, all nine values with roots, all nine Cayley states, all 18 generator transitions, and all three unordered generator pairs including diagonal. The actual-value and Cayley-state code hashes agree exactly:

`8d91bc54054712c7f87829a17b16b1d8d3962b50154a1efdec76cf08851787b8`.

## Reproducible evidence

- Exact enumerator: `Agents/Kourovka/problems/21.137/scratch/eq11_cube_cayley.py`.
- Leased command: `timeout 600s python3 Agents/Kourovka/problems/21.137/scratch/eq11_cube_cayley.py`.
- Exit status `0`; script wall time `19.986400842666626` seconds.
- Selection artifact: `selected-rows.json`, SHA-256 `a8725dcadb2a361fb2cfce5e4cf340003ec609ea63808bc512012ca4bbad782a`.
- Eleven-row manifest: `family-manifest.jsonl`, SHA-256 `42d0d723adfc86b74d8e90aae9d78a9a0b9326b0ea31f877214fe0268d95ad34`.
- Summary: `summary.json`, SHA-256 `4c899765f15dc0c579469f7c849a8a6b1f4207dbf09a0bd8f4a80b3f5f095fc9`.
- All eleven row-certificate hashes match the family manifest; every one of the compressed artifacts passes `gzip -t`.

## What this does not establish

- It does not prove or refute the unrestricted odd-prime assertion.
- It does not construct a target-equal counterexample.
- It does not address the ten unequal-endpoint low-dimensional rows already assigned to a separate killed strategy.
- It says nothing about dimension above `12`, a third generator, other algebra templates, other odd primes, or non-algebra groups.
- The eight raw groups with closure defects cannot be used as counterexamples even if they contain noncommuting cube values, because they fail the actual-value-set subgroup hypothesis.
- The three scalar rows are abelian only as a bounded family result; they do not imply that endpoint equality generally forces abelianness.

## Recommended next action

Do not enlarge this family inside `EQ11-CUBE-CAYLEY`. Its exact eleven-row hard kill is met. Route the bounded certificate to Validator. Any further work must be a Lead-selected materially different representation or a direction switch; the remaining allocation is not permission to add generators, raise the dimension cutoff, or import an excluded construction.

Verified by [[Agents/Kourovka/problems/21.137/verification/2026-08-17T043410Z-eq11-cube-cayley]].
