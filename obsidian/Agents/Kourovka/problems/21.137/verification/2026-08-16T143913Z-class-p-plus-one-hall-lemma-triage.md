---
title: "Triage — Kourovka 21.137 — class-p-plus-one Hall lemma"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "For every odd prime p, every group G of exponent dividing p^2 and class at most p+1 has commuting p-th powers."
claimant: Problem-21.137
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the actual p-th-power value set P is a subgroup, then P is abelian."
excluded_scopes: ["the general powerfulness clause", "21.137/two-group-exponent-8", "odd-prime groups of exponent other than exactly p^2"]
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/hall-collection, project/kourovka, status/conjectured]
---

# Triage — class-≤p+1 Hall lemma

## Claim and scope lock

The submitted statement is a uniform hand-proof claim for the strict subclass `cl(G) <= p+1`; it is not a claim about every group in revision 2's unrestricted active assignment. The source image and canonical scope agree on the odd-prime, exact-exponent-`p^2`, actual-value-set, subgroup, and abelianity requirements. Because this is a `PARTIAL_RESULT`, not a `CLAIM` or `STALE_MATCH`, no claim-check JSON is required by the common protocol.

## Clause matrix

| source clause | active? | submission addresses | active_assignment_answered |
|---|---:|---|---|
| General question: power-value subgroup powerful? | no | no | pending |
| Odd `p`, exponent `p^2`: actual power-value subgroup abelian? | yes | only the additional family `cl(G) <= p+1` | pending |
| `p=2`, exponent 8: square-value subgroup abelian? | no | no | pending |

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required source condition | submitted proof use | triage status |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every qualifying odd `p,G` | only groups of class at most `p+1` | fails for unrestricted scope; eligible partial family |
| `21.137-odd-p-not-2` | admissibility | odd prime `p` | uses prime binomial divisibility and oddness | pending proof check |
| `21.137-odd-finite-p-group` | admissibility | finite `p`-group for the same `p` | proof claims the stronger arbitrary-group statement | pending proof check |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | assumes exponent dividing `p^2`, which includes source objects | pending proof check |
| `21.137-odd-power-set-definition` | admissibility | `P={g^p:g in G}` | proves pairwise commutation of actual values; distinguishes `K=<P>` | pending proof check |
| `21.137-odd-power-set-subgroup` | admissibility | actual value set is a subgroup | unused by the lemma; needed only to identify the source subgroup with `P` | pending proof check |
| `21.137-odd-P-abelian` | conclusion | `P` abelian | claimed only under `cl(G) <= p+1` | pending for partial family; unproved unrestricted |

## Target versus witness

- Source target: every finite odd-prime `p`-group of exact exponent `p^2` whose actual power-value set is a subgroup.
- Proof object: an arbitrary group of exponent dividing `p^2` and class at most `p+1`.
- Witness equals target: **false as classes of objects**. The proof object is a strict additional-hypothesis family inside the active target when the source hypotheses are imposed. A correct proof can certify a partial theorem only.

## Subclaims

1. Hall coordinates of `[X^m,Y^n]` have an integral binomial expansion with separate index bounds given by multidegree.
2. Those bounds imply `[x^p,y^p] in gamma_{p+1}(G)` and give the stated divisibility at weight `p+1`.
3. For `K=<g^p:g in G>`, generator commutators being central implies `K' <= Z(G)`, and every element of `K`, not only its generators, has order dividing `p`.
4. In `G/K`, all but the single multidegree `(p,1)` factor in `[y,x^p]` die individually; that factor has coefficient `+/-1`, hence its basic commutator lies in `K`.
5. In the final collection of `[x^p,y^p]`, every factor through weight `p+1` dies for one of the asserted exponent reasons.
6. Separately, at `p=3` and class at most 5, collection gives `[y,x^3]=c_1^3 c_2^3 c_3 d` up to the orientation of the terminal factor, so quotient isolation is contaminated by multidegree `(3,2)`.

## Tools probed

Verbatim probe output:

```text
/usr/bin/gap
/usr/bin/python3
Python 3.12.3
GAP 4.12.1
```

Sage and Magma were not found. The submitted evidence is a hand proof, so the verification method will also be a hand reconstruction; no finite computation can prove its uniform claim.

## Methods inventory

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| 1–2 | finite-difference/Hall-coordinate derivation in the free nilpotent group | the required coordinate divisibilities survive specialization | the unrestricted theorem beyond class `p+1` |
| 3 | elementary commutator generation plus class-two power induction | `K' <= Z(G)` and `exp(K) | p` without assuming either | membership of the extreme commutators in `K` |
| 4 | multigraded free-Lie rank plus a one-`Y` quotient collection | uniqueness and unit coefficient of the extreme factor | any class-`p+2` isolation |
| 5 | exhaustive multidegree split at weights at most `p+1` | commuting `p`-th powers in the claimed partial family | the active assignment for higher-class groups |
| 6 | direct symbolic conjugation under the stated convention | the presence/sign of the terminal contamination term | that the class-`p+2` lemma is false |

## Hard limits and recommendation

The unrestricted active target cannot be answered by this additional-class proof. Deep hand verification is appropriate and can establish or refute the submitted partial theorem; no installation is needed. Recommendation: full line-by-line verification of the partial lemma, with the active assignment kept open regardless of outcome.
