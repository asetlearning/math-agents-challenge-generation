---
title: "Triage — Kourovka 21.137 — conditional MIN9 outer-action family"
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "Conditional on the reviewed order-3^9 equality reduction, every factor-independent outer-action row for P=H_3(3)xC3^2 and R in {C3^4,H_3(3)xC3} fails the necessary actual-cube coverage capacity gate."
claimant: Problem-21.137
target_statement: "For every odd prime p and finite p-group G of exponent exactly p^2, if the actual pth-power value set P is a subgroup, then P is abelian."
excluded_scopes: ["21.137/two-group-exponent-8", "c-general powerfulness", "odd-prime groups not of exact exponent p^2"]
target_object: "An arbitrary finite p-group satisfying the active odd-prime exact-exponent and actual-power-value-set hypotheses."
witness_object: "A computed list of Sylow-3-subgroup conjugacy classes in Out(H_3(3)xC3^2), filtered by two conditional order-3^9 quotient types and a necessary cube-coverage network."
witness_equals_target: false
citation: none
verification_method: "hand reconstruction of inherited-to-new logical bridges, static audit of GAP code, cryptographic and transcript checks, and an independently written parser/recalculator for every printed candidate row"
tools_used: ["GAP 4.12.1", "Python 3.12.3", "sha256sum", "wc"]
scope_answered: []
scope_not_answered: ["21.137/odd-prime-exponent-p2", "c-general", "c-two"]
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/module-actions, project/kourovka, status/draft]
---

# Triage

## Evidence boundary

This audit uses only the canonical revision-2 scope, the submitted message and its four exact refs, and the immediately preceding independent nine-lift verification.  No web, other history, other 21.137 note, or solver artifact is admissible.  The submission is a bounded `PARTIAL_RESULT`; no whole-scope claim-check JSON is expected.

## Clause matrix

| source clause | active? | claimed coverage | triage answer |
|---|---:|---|---|
| `c-general` powerfulness | no | none | no |
| `c-odd` odd p, exponent exactly p^2 | yes | conditional p=3, exponent-9, order-3^9 equality layer only | pending for the layer; no for the active scope |
| `c-two` p=2, exponent 8 | no | none | no |

`active_assignment_answered` cannot become `yes` in this audit.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | submission | triage result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | all qualifying odd p and G | only conditional p=3 order 3^9 | not established |
| `21.137-odd-p-not-2` | admissibility | p>2 prime | p=3 | passes for specialization |
| `21.137-odd-finite-p-group` | admissibility | finite p-group | no group is constructed; extension family is conditional | not established on a witness |
| `21.137-odd-exponent-p2` | admissibility | exact exponent p^2 | exponent 9 is an inherited equality-family premise | conditional |
| `21.137-odd-power-set-definition` | admissibility | complete actual value set | capacity must be re-derived from surjectivity of the actual cube map onto P | pending |
| `21.137-odd-power-set-subgroup` | admissibility | actual value set is a subgroup | inherited equality premise `P=H^3` must feed every one of 243 demand values | pending |
| `21.137-odd-P-abelian` | conclusion | P abelian | no universal conclusion; only a candidate order layer is claimed empty | not established |

## Target versus witness

The computed witness is neither a group nor the universal target.  It is an overcomplete Sylow-local list of possible outer action images, tested against a necessary capacity bound.  A clean failure of every row can exclude only the conditional equality-action family; it cannot establish existence/nonexistence of larger groups or any p>3 case.

## Subclaim decomposition

1. Separate inherited reviewed dependencies from deductions available in the submitted refs: the quotient-minimal bounds/flag versus the equality arithmetic and classifications of `P` and `R`.
2. Prove that the image-type predicates cover every homomorphic image of each `R` which could contain a centrally regular action.
3. Check the full automorphism coordinate model, identify `Inn(P)`, derive all group orders, and justify Sylow-local overcoverage.
4. Derive the capacity network directly from actual cube-value-set equality: 27 demanded values for each of eight nonzero labels, at most three central values per fixed lift, at most nine distinct values per quotient coset, and `k=81/|U|` cosets over each outer element.
5. Check full-outer conjugacy invariance of the lift profile and flow.
6. Audit all 508 script lines for implementation fidelity and all 2,398 printed rows for completeness, arithmetic, max-flow/min-cut agreement, and absence of survivors.
7. Reproduce frozen hashes, byte/line counts, headline counts, row distributions, and terminal markers without rerunning the claimant's heavy GAP search.

## Methods inventory

| subclaim | method | pass proves | pass does not prove |
|---|---|---|---|
| 1--2 | hand group theory | conditional equality and image-type completeness from named premises | the inherited lower bound and common-flag lemmas themselves |
| 3 | bracket-preserving matrix derivation plus code/output audit | the computed group is the intended `Out(P)` model and all 3-images are Sylow-locally represented | independent recomputation of GAP's subgroup lattice unless a new heavy lease is granted |
| 4 | direct root-coset/fixed-space counting | flow failure is a necessary obstruction to actual cube-set equality | sufficiency, factor-system existence, or exponent of an extension |
| 5 | transport the network under an arbitrary outer automorphism | prefusion failure survives full-outer fusion | subgroup-lattice correctness |
| 6--7 | independent transcript parser/recalculator and static code audit | every printed row fails and all reported aggregates follow from the frozen artifact | a second independent GAP enumeration |

## Hard limits and recommendation

The exact refs treat the quotient-minimal lower bound, quotient-minimal structure rows, and common invariant flag as already reviewed; this audit will not silently recertify them.  No heavy rerun is authorized.  Proceed with hand proof of all new bridges and a complete independent audit of the frozen script/output.  The maximum possible verdict is a conditional bounded partial with `active_assignment_answered: no`.
