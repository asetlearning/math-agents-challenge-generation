---
title: "Triage — Kourovka 21.137 — r36 defect root fibre"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "In the reviewed hypothetical minimum counterexample, the Hall defect has the submitted value orbit, free root-fibre V-torsors, cyclic return law, and formally unconstrained C_p-set/V-translation data, without producing a group or answering the scope."
claimant: Problem-21.137-Proof
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Triage — Kourovka 21.137 — r36 defect root fibre

## Scope and claim lock

Canonical scope `21.137/odd-prime-exponent-p2`, revision `2`: odd prime `p`, finite same-`p` group of exact exponent `p^2`, literal actual-power set `P` assumed a subgroup, target `P` abelian. The `p=2`/exponent-`8` sibling is excluded.

The r36 submission is a conditional `PARTIAL_RESULT` inside the already reviewed hypothetical minimum-counterexample setup. No group is exhibited. The asserted freedom after (C12) is explicitly a formal incidence/V-set model, not a group-realization claim. No claim-check JSON is required for this non-`CLAIM` outcome.

## Clause and constraint gate

| row | triage result |
|---|---|
| active odd-prime clause | conditional minimum-counterexample consequences only |
| universal quantifier | unanswered |
| exact exponent and literal power set | inherited hypotheses whose uses will be checked line by line |
| subgroup closure | inherited hypothesis; does not follow from the incidence model |
| target `P` abelian | assumed false conditionally; no contradiction claimed |
| excluded sibling/general clause | untouched |

`active_assignment_answered: pending`, necessarily `no` if the submitted partial passes unchanged.

## Target versus witness

The target is the full universal group class. The submission has no witness; it reasons conditionally inside a hypothetical minimum-order counterexample and then exhibits only abstract fibre/action data satisfying selected necessary identities. Therefore `witness_equals_target: false`. A consistent incidence model cannot establish existence of a group and cannot refute or prove the target.

## Subclaim decomposition

1. (C1)--(C3): exact conjugation orientation, orbit `Delta N`, stabilizer, and conjugate-root filling.
2. (C4)--(C7): `V=<Delta,N>` has order `p^2`; roots centralize `V`; right multiplication is a free fibre-preserving V-action; root orders/cardinality divisibility; conjugation by `h` transports layers.
3. (C8)--(C9): `b` centralizes `V`, and the p-step return satisfies the ordered identity `x^(h^p)=x^b` on roots.
4. (C10)--(C11): displacement location/exponent and the exact ordered cyclic norm, including its odd-prime sign.
5. (C12): classification of the **abstract V-equivariant order-p return action** by a C_p-set and torsor translations modulo basepoint gauge.
6. The formal classification does not assert simultaneous realization by group multiplication, a power map, or an admissible counterexample.

## Methods inventory

| subclaim | method | pass proves | pass does not prove |
|---|---|---|---|
| C1--C3 | convention-fixed commutator/conjugation calculation | stated value orbit and conjugate roots | group existence |
| C4--C7 | centralizer and free finite-action audit | V-torsor fibres and divisibility | arbitrary fibre counts are realizable by a group |
| C8--C11 | ordered conjugation and telescoping norm | exact return law and absence of a contradiction from that norm | absence of other group-law constraints |
| C12 | finite V-torsor/C_p-action classification | formal freedom of the return permutation once only these action rows are retained | a group, power map, common root section, or counterexample |

Tool probe from this session: GAP `4.12.1`, Python `3.12.3`, Poppler `24.02.0`; Sage and Magma absent. Hand reconstruction is primary; a free-group word check may be used only for convention-sensitive identities.

## Hard limit and recommendation

Use only the request, its two r36 refs, the named reviewed minimum-counterexample note, and the canonical scope; no web or unrelated solution-bearing history. Recommendation: full conditional hand audit, with special attention to the right-V action, the passage from `h^p=b Delta` to the return map, norm order, and the precise logical strength of “arbitrary.”
