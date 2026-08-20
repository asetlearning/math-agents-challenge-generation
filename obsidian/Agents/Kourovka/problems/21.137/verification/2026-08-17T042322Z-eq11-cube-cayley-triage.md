---
title: "Verification triage — Kourovka 21.137 — EQ11-CUBE-CAYLEY/E_12"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "The fixed family E_12 has exactly eleven rows and contains no row whose actual cube-value set is both a subgroup and nonabelian."
claimant: Problem-21.137
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/algebra-groups, project/kourovka, status/draft]
---

# Triage

## Scope and exact target

The rendered source says: for odd `p`, if the actual `p`-th powers in a finite `p`-group of exponent exactly `p^2` form a subgroup, must that subgroup be abelian? The active scope is revision 2 of `21.137/odd-prime-exponent-p2`. Excluded are the general powerfulness clause, the separate `p=2` exponent-8 clause, every odd-prime group of exponent other than exactly `p^2`, and every group outside the fixed `E_12` family for purposes of this bounded audit.

| source clause | active? | what this audit could answer |
|---|---|---|
| general powerfulness question | no | nothing |
| odd-prime, exponent-`p^2`, abelian-power-subgroup question | yes | only a strict finite subfamily at `p=3` |
| `p=2`, exponent-8 square question | no | nothing |

`active_assignment_answered: pending`, with an a priori ceiling of `no` because `E_12` is a strict subfamily.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | audit status at triage |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | universal assertion over all admissible odd `p` and finite `p`-groups | cannot be discharged by this family |
| `21.137-odd-p-not-2` | admissibility | prime `p>2` | proposed `p=3`; pending artifact check |
| `21.137-odd-finite-p-group` | admissibility | finite `p`-group for the same `p` | proposed `G_tau=1+J_tau`; pending basis/closure check |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2=9` | pending nilpotence and explicit order-9 element check |
| `21.137-odd-power-set-definition` | admissibility | actual cube-value set, not generated subgroup | pending complete-domain and cube-map check |
| `21.137-odd-power-set-subgroup` | admissibility | actual cube-value set is a subgroup | pending eight boundary and three equality checks |
| `21.137-odd-P-abelian` | target conclusion | every admissible row's cube subgroup is abelian | pending exact generator/table check for closure-passing rows |

This is a `STRATEGY_EXHAUSTED` audit, not a `CLAIM`; the absence of a claim-check JSON is therefore not a gate failure.

## Target versus witness

The source target is the universal class of all finite odd-prime `p`-groups of exponent exactly `p^2` satisfying actual-power-set closure. The witnesses computed are the eleven algebra groups `G_tau=1+J_tau` for `tau` in the proposed fixed family `E_12`. Thus the witness family is not equal to the source target. At most the bounded family can be exhausted.

## Subclaims and method inventory

| subclaim | method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| `E_12` has exactly eleven rows | independently recompute all `tau in F_3^6`, generated-algebra dimensions, endpoint equality | completeness of the frozen family | anything outside `E_12` |
| each saved basis is the generated algebra | independent matrix-algebra closure and RREF comparison | the encoded finite group is the stated `1+J_tau` | universal relevance |
| every row has exponent exactly 9 | prove `J_tau^7=0`, check all ninth powers, and exhibit `1+S` of order 9 | exact exponent for each row | power-set closure |
| saved cube map is the complete actual cube map | verify every basis coordinate occurs once and recompute `(1+x)^3` | exact actual-value set for each row | subgroup closure by itself |
| eight rows fail closure | replay roots, cubes, circle product, and absence from complete value set | those rows violate the hypothesis | any conclusion about abelianness |
| three rows have actual-set/Cayley equality | compare independently generated Cayley state set with complete actual-value set | those three actual value sets are subgroups | commutativity by itself |
| the three closed rows are abelian | verify the complete claimed generator table and/or the scalar-row algebra derivation | their cube subgroups are abelian | endpoint-equal rows outside `E_12`, or the active scope |
| all eleven outcomes partition as eight plus three | cross-check row certificates, manifest, summary, and hashes | bounded exhaustion of exactly `EQ11-CUBE-CAYLEY/E_12` | a solution or counterexample to 21.137 |

## Tools and hard limits

Available: GAP at `/usr/bin/gap` (version probe emitted no version line), Python 3.12.3 at `/usr/bin/python3`; Sage and Magma are absent. Static certificate, hash, source, and hand-algebra checks can proceed. No categorical or all-input enumeration will run until Lead grants a compute lease for the separately designed bounded checker.

## Recommendation

Proceed with hostile static inspection now; request a short lease for a separate fixed-family checker. The maximum possible verdict is a bounded `PARTIAL_RESULT`/`STRATEGY_EXHAUSTED` finding with `active_assignment_answered: no`.

