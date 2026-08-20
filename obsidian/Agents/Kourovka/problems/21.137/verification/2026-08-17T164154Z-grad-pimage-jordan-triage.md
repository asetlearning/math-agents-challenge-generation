---
title: "Triage — Kourovka 21.137 — first power-image quotient and Jordan obstruction"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claimant: Problem-21.137-Proof
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/lie-methods, project/kourovka, status/draft]
---

# Triage — first power-image quotient and Jordan obstruction

## Claim restated

For a hypothetical counterexample in the active odd-prime exponent-
\(p^2\) scope, the first lower-central quotient in which the literal
\(p\)-power image stays nonabelian has a class-two exponent-\(p\) Baer Lie
algebra containing a forced \(J_{p+1}\) chain and one further fixed noncentral
vector, hence its power-image subgroup has order at least \(p^{p+2}\) and the
ambient group has order at least \(p^{p+3}\); the displayed dimension-
\(p+2\) cyclic extension realizes only the local product-root equation and is
not submitted as a target witness.

This is routed as `PARTIAL_RESULT`, not as a scope-closing proof.  The linked
claim check contains all seven revision-2 rows, has
`ready_for_validator:false`, and the state checker exits with zero errors
(seven unrelated migration warnings).

## Scope and source clause matrix

- Scope: `21.137/odd-prime-exponent-p2`.
- Assignment revision: `2`.
- Active target: for every odd prime \(p\) and finite \(p\)-group \(G\) of
  exponent exactly \(p^2\), if the actual value set
  \(P=\{g^p:g\in G\}\) is a subgroup, then \(P\) is abelian.
- Excluded: the general powerfulness question, the \(p=2\) exponent-eight
  clause, generated-power-subgroup substitutes, and wrong-exponent groups.

The source was independently read with `pdftotext` and visually checked on
rendered PDF page 184.

| source clause | active? | submitted result |
|---|---:|---|
| If the power values form a subgroup, must it be powerful? | no | not addressed |
| For \(p\ne2\), exponent \(p^2\), must a subgroup of actual \(p\)-power values be abelian? | **yes** | only a necessary condition for a hypothetical counterexample |
| For a 2-group of exponent 8, must a subgroup of squares be abelian? | no | not addressed |

`active_assignment_answered: pending` at triage; it cannot become `yes` on the
submitted claim.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | submitted use | triage result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every qualifying \(p,G\) | assumes a hypothetical counterexample and derives a necessary condition | unknown for the universal conclusion |
| `21.137-odd-p-not-2` | admissibility | odd prime \(p\) | needed for class-two Baer/BCH coordinates and \(1/2\) | pass for the partial lemma |
| `21.137-odd-finite-p-group` | admissibility | finite same-\(p\) group | lower-central quotient remains a finite \(p\)-group | pass for the partial lemma |
| `21.137-odd-exponent-p2` | admissibility | exact exponent \(p^2\) | inherited with exponent dividing \(p^2\); exactness in the quotient must be rechecked from the chosen product root | pending hand audit |
| `21.137-odd-power-set-definition` | admissibility | literal value set, not generated subgroup | image under the quotient map must equal the quotient's literal power-value set | pending hand audit |
| `21.137-odd-power-set-subgroup` | admissibility | literal set is a subgroup | subgroup property should descend under the quotient map | pending hand audit |
| `21.137-odd-P-abelian` | target conclusion | \(P\) abelian | explicitly not proved | not proved |

## Target versus witness

- Target object: the universal source class above.
- Main proof object: a quotient \(Q=G/\gamma_{c+1}(G)\) of an assumed
  counterexample, together with its image \(\bar P\).
- Sharpness object: a dimension-\(p+2\) class-two exponent-\(p\) Baer group
  with one cyclic root extension.
- `witness_equals_target: false`.  Neither object is a submitted
  counterexample, and the sharpness extension is not claimed to have its
  designated nonabelian subgroup equal to the actual \(p\)-power image.

## Subclaims and methods inventory

| subclaim | method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| quotient retains the literal power image and nonabelianity | direct quotient/power-map calculation | \(\{(gN)^p\}=PN/N\), with a surviving central commutator | the universal target |
| Baer correspondence applies | class-two, exponent-\(p\), class-\(<p\) hand check | a functorial \(\mathbb F_p\)-Lie algebra and linear automorphism action | any coherence among independently chosen roots |
| \(D^p\) identity and signs | fix conjugation and adjoint conventions, then reconstruct BCH conjugation | the exact transgression equation | vanishing of the transgression |
| Jordan chain and extra vector | elementary cyclic-module argument | dimension at least \(p+2\) | a stronger global order bound or abelianity |
| two order bounds | subgroup index and exact-order hand checks | \(|\bar P|\ge p^{p+2}\), \(|G|\ge p^{p+3}\) | optimality for actual counterexamples |
| action-quotient equality | identify powers in \(Q/C_Q(\bar P)\) in both directions | literal power image equals `Inn(Pbar)` | recovery of the killed derived subgroup |
| sharp local model | check the bracket, automorphism, central quotient, BCH product, exponent, and actual power-image location | sharpness of the single-root linear obstruction | an admissible source witness |

## Tools and hard limits

- Available: GAP 4.12.1, Python 3.12.3, `pdftotext`, and `pdftoppm`.
- Not available in the probe: Sage and Magma.
- No mathematical computation is needed or authorized.  This is a hand-proof
  audit.  It can certify only the stated necessary condition/local sharpness,
  never the unrestricted conclusion.

## Recommendation

Proceed with a hostile line-by-line hand reconstruction.  Preserve
`witness_equals_target:false` and `active_assignment_answered:no`.  In
particular, normalize `ad` against the declared right-conjugation convention
instead of silently accepting the displayed sign, and compute enough of the
sharpness extension's actual power image to rule out accidental promotion to
an in-scope witness.

