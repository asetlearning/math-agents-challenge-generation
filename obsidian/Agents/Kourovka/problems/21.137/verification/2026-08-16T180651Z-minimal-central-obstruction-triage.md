---
title: "Triage — Kourovka 21.137 — minimal central obstruction"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claimant: Problem-21.137
witness_equals_target: false
active_assignment_answered: no
outcome: PARTIAL_RESULT
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Triage — Kourovka 21.137 — minimal central obstruction

## Claim restated

Conditional on the existence of a counterexample in scope `21.137/odd-prime-exponent-p2`, a minimum-order counterexample is claimed to have a unique central minimal normal subgroup `N=P'` of order `p`, cyclic center of order `p` or `p^2`, and a central-extension factor set whose root fibres and stabilizer maps have the stated exact identities; this is only a reduction and does not answer the unrestricted target.

## Locked scope and source

- Scope: `21.137/odd-prime-exponent-p2`.
- Assignment revision: `2`.
- Exact active target: for every odd prime `p` and finite `p`-group `G` of exponent exactly `p^2`, if the actual value set `P={g^p:g in G}` is a subgroup, then `P` is abelian.
- Rendered source: page 184 was visually inspected. It agrees with the canonical active clause.
- Excluded: the general powerfulness question, every `p=2` case, the exponent-8 two-group clause, and every odd-prime group whose exponent is not exactly `p^2`.

## Clause matrix

| source clause | active? | claimed treatment | status before audit |
|---|---:|---|---|
| General: actual `p`th powers a subgroup implies powerful? | no | excluded | unanswered |
| `p != 2`, exponent exactly `p^2`, actual powers a subgroup implies abelian? | yes | conditional structural reduction only | `active_assignment_answered: no` |
| `2`-group of exponent `8`, squares a subgroup implies abelian? | no | excluded | unanswered |

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | rendered-source requirement | proposed proof use | pre-audit result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | universal in every admissible `p,G` | assumes a counterexample and minimizes `|G|` | conditional only |
| `21.137-odd-p-not-2` | admissibility | `p` is an odd prime | retained throughout | pending line audit |
| `21.137-odd-finite-p-group` | admissibility | `G` is a finite `p`-group | minimum order and normal/central intersection | pending line audit |
| `21.137-odd-exponent-p2` | admissibility | `exp(G)=p^2` exactly | bounds powers and is claimed to survive quotient | pending line audit |
| `21.137-odd-power-set-definition` | admissibility | `P` is the actual set `{g^p}`, not merely `G^p` | elementwise quotient and fibre claims | pending line audit |
| `21.137-odd-power-set-subgroup` | admissibility | that actual set is a subgroup | characteristicity, quotient closure, and fibre filling | pending line audit |
| `21.137-odd-P-abelian` | target conclusion | `P` is abelian | explicitly not proved | unresolved |

No concrete witness is offered. The admissibility rows are hypotheses of a conditional reduction, not checked properties of an exhibited group; the target-conclusion row is unresolved.

## Target versus witness

- Target object: the whole universal class in the active source clause.
- Witness object: a hypothetical minimum-order counterexample; existence is neither asserted nor established.
- `witness_equals_target: false`. A conditional minimum counterexample is not an exhibited target object and the reduction is not the universal conclusion.
- Circularity risk to check: none from computation, but every appeal to minimality must first show the quotient remains in the exact active class and remains a counterexample.

## Subclaim decomposition

1. The rendered clause and canonical revision agree.
2. The actual-value subgroup equals `G^p`, is characteristic, and has exponent exactly `p` in a hypothetical counterexample.
3. There exists `N<=P' intersect Z(G)` of order `p`.
4. The quotient's actual value set is exactly `P/N` elementwise.
5. The quotient retains exponent exactly `p^2`.
6. Minimality forces `P'=N`.
7. Every nontrivial normal subgroup contains `N`.
8. Consequently `N` is the unique minimal normal subgroup and `Z(G)` is cyclic of order `p` or `p^2`.
9. The normalized central factor set has the claimed cocycle and cyclic-power identities, with correct order and signs.
10. Actual-value closure is equivalent to fibrewise surjectivity of every `lambda_a`.
11. Section changes translate the fibres as claimed and preserve surjectivity.
12. `beta` is the section-independent commutator pairing on `P/N`, with the claimed orientation.
13. A central `p`th root of `N` makes every root fibre automatic in the `|Z(G)|=p^2` branch.
14. The stabilizer map is well-defined and homomorphic, restricts to the commutator row up to a stated orientation, and fills fibres off `rad(beta)`.
15. None of these statements proves the unrestricted target.

## Tool probe and methods inventory

`gap`, `python3`, `pdftoppm`, and `pdftotext` are present; `sage` and `magma` were not found. `Python 3.12.3` and Poppler `24.02.0` were identified. GAP's `--version` probe returned no version line. No mathematical engine, script, catalogue, or experiment is authorized or used.

Every mathematical subclaim will be checked by a fresh hand derivation from only the two cited run notes, the canonical scope record, and rendered page 184. A pass establishes only the corresponding conditional lemma and its formulas; it does not establish existence of a counterexample, witness equality, or the unrestricted abelianity conclusion. Visual comparison addresses source fidelity only.

## Hard limits and recommendation

The audit may not use web/history, other runs, computation, delegates, `p=2`, exponent-8, or wreath-shaped material. It therefore cannot turn this conditional reduction into a solution or certify any concrete witness. Recommendation: hostile line-by-line verification, with at most a `PARTIAL_RESULT` and `status/conjectured`; keep `active_assignment_answered: no` and the unrestricted conclusion open.
