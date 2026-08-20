---
title: "Triage — Kourovka 21.137 — ALG3-UT7/F_12 family exhaustion"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claimant: Problem-21.137
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/algebra-groups, project/kourovka, status/conjectured]
---

# Triage — frozen ALG3-UT7/F_12 family

## Claim restated

The submitted artifact claims only that the fixed parameter family
`ALG3-UT7-CUBE-IMAGE/F_12` contains no target-equal candidate: among all
`tau in F_3^6`, exactly the rows with
`tau_1 tau_2 tau_3 != tau_4 tau_5 tau_6` and `dim <S,T_tau> <= 12` are in the
frozen family, and every such row has an explicit leading-layer obstruction to
closure of its actual cube-value set. It claims `STRATEGY_EXHAUSTED` for that
family, not an answer to the unrestricted Kourovka scope.

## Scope lock

- Canonical scope: `21.137/odd-prime-exponent-p2`.
- Assignment revision: `2`, current in the canonical scope record.
- Exact active target: for every odd prime `p` and every finite `p`-group `G`
  of exponent exactly `p^2`, if the actual value set
  `P={g^p:g in G}` is a subgroup, then `P` is abelian.
- Excluded: the general powerfulness question, every `p=2` case, the separate
  exponent-8 two-group clause, and every odd-prime group of exponent other than
  exactly `p^2`.
- Source check: the rendered PDF page 184 visibly has the three clauses above;
  the canonical transcription preserves `p != 2`, exponent `p^2`, actual
  `p`-th powers, subgroup, and abelian conclusion.

## Clause matrix

| source clause | active? | what the submission addresses | status |
|---|---|---|---|
| General question: power subgroup powerful | no | nothing | excluded |
| Odd-prime exponent-`p^2` power subgroup abelian | yes | only one fixed `p=3` algebra-group subfamily | `active_assignment_answered: pending`; family failure cannot answer the universal target |
| Two-group exponent-8 square subgroup abelian | no | nothing | excluded |

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | submitted-family use | triage result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | all odd primes and all admissible groups | tests only a fixed `p=3` subfamily; a no-pass result cannot discharge the universal row | not addressed |
| `21.137-odd-p-not-2` | admissibility | `p` prime, `p>2` | base field is exactly `F_3` | pass for tested rows |
| `21.137-odd-finite-p-group` | admissibility | finite `p`-group for the same `p` | `G_tau=1+J_tau`, with the retained rows reported as `dim J_tau=11` | pending independent dimension/finiteness check |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `9` at `p=3` | ambient nilpotence gives exponent dividing `9`; `S^3 != 0` is offered for exactness | pending hand check |
| `21.137-odd-power-set-definition` | admissibility | actual cubes, not their generated subgroup | uses `(1+x)^3=1+x^3` and the projection of all actual cube values | pending hand check |
| `21.137-odd-power-set-subgroup` | admissibility | actual cube set is a subgroup | submitted nonadditivity witnesses are intended to make this row fail for every retained row | pending witness and implication check |
| `21.137-odd-P-abelian` | target conclusion | actual cube subgroup abelian | endpoint inequality makes two raw cube values noncommute, but no row is admissible if subgroup closure fails | not a counterexample without the preceding subgroup row |

Any retained row with failed or unknown power-set subgroup closure is not an
admissible counterexample. The submission correctly makes no `CLAIM` and supplies
no claim-check JSON.

## Target versus witness

- Source target object: every finite odd-prime `p`-group of exponent exactly
  `p^2` whose actual `p`-th-power value set is a subgroup.
- Computed objects: `G_tau=1+J_tau`, where
  `J_tau=<S,T_tau>` is the nonunital associative algebra generated inside
  `UT_7(F_3)` by the two displayed first-superdiagonal matrices.
- Computed parameter universe: exactly `3^6=729` ordered tuples before the
  endpoint and dimension filters.
- Witness equals source target: false. This is a bounded subfamily only.
- Family-specific witness: the manifest plus the independent graded-word
  checker. Their equality to the frozen parameter definition remains to be
  audited below.

## Subclaim decomposition

1. The manifest has one row for each ordered tuple of `F_3^6`, in canonical
   order, and no missing or duplicate tuple.
2. The endpoint-product inequality is exactly the condition that the two
   displayed actual cubes `1+S^3` and `1+T_tau^3` do not commute.
3. The six graded word ranks sum to `dim J_tau`.
4. Exactly ten rows satisfy both the endpoint inequality and `dim J_tau<=12`.
5. For every retained row, the degree-three projection of the actual cube set
   is exactly `C_tau={(aS+bT_tau)^3:a,b in F_3}`.
6. Circle closure of the actual cube set forces additive closure of `C_tau`.
7. Each of the ten saved pairs belongs to `C_tau x C_tau`, while its displayed
   sum does not belong to `C_tau`.
8. Therefore every retained row fails the subgroup hypothesis, so the frozen
   family has no target-equal candidate.
9. This conclusion leaves the active universal assignment unanswered.

## Tool probe

- GAP `4.12.1` is installed.
- Python `3.12.3` is installed.
- GNU `sha256sum` `9.4` is installed.
- Sage, Magma, and `jq` are absent.

## Methods inventory

| method | subclaims | what a pass proves | what a pass does not prove |
|---|---|---|---|
| Rendered-PDF comparison | scope lock | exact source clause and exclusions | any mathematical assertion |
| SHA-256 and line-count check | 1 and artifact identity | the files inspected are the cited 729-line artifacts | correctness or completeness of their algorithms |
| Line-by-line audit of both implementations | 1--7 | whether the code implements the stated finite gates | that an unobserved execution produced the preserved output |
| Sanctioned preserved graded-word audit | 1, 3, 4, 7 | independent agreement on dimensions, retained rows, and saved witnesses for the cited manifest | the unrestricted target; it also cannot use the earlier unleased probe |
| Direct algebra and grading derivation | 2, 5, 6 | endpoint and leading-layer implications without relying on code | exhaustive classification of all 729 dimensions |
| Fresh bounded certificate parsing and hand checks | 1, 4, 7, 8 | internal consistency of every retained certificate | any group outside the frozen family |

## Hard limits and evidence boundary

- No current compute lease authorizes a new enumeration run. The disclosed first
  run of `ut7_cube_image_audit.py` after slot release is excluded completely from
  evidentiary weight.
- The exact sanctioned rerun and its preserved output may be audited. Static
  certificate checks and hand derivations do not enlarge the search.
- The family is not the source target, so even a successful audit must keep
  `active_assignment_answered: no` and cannot raise the unrestricted scope above
  `status/conjectured`.

## Recommendation

Proceed with full hostile verification of the bounded family-exhaustion
certificate. Accept at most a family-specific replicated partial result if every
gate above survives; otherwise return the first failed row or logical implication.
