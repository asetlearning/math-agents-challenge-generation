---
title: "Verification triage — Kourovka 21.137 — order-6561 TRI3 layer"
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "At p=3, no exponent-9 group of order 3^8 is a TRI3 seed with noncommuting actual cubes, and no direct revision-2 counterexample has order below 3^9."
claimant: Problem-21.137
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

# Triage — order-6561 TRI3 layer

## Locked scope and claim

The active assignment is revision 2 of `21.137/odd-prime-exponent-p2`: for every odd prime `p` and finite `p`-group `G` of exponent exactly `p^2`, if the set of actual `p`-th powers is a subgroup, prove that subgroup abelian or exhibit an admissible counterexample. Excluded are the general powerful-subgroup clause, every `p=2` case, the exponent-8 square clause, and odd-prime groups of any other exponent.

The submitted outcome is only a bounded `p=3` partial claim: (i) the order-`3^8` TRI3 seed family is empty; (ii) the claimed direct-counterexample consequence is that a `p=3` counterexample must have order at least `3^9`. It does not answer the active universal assignment. No claim-check JSON is linked or present; the common protocol requires that file for `CLAIM` and `STALE_MATCH`, while the claimant labels this `PARTIAL_RESULT`. Therefore this audit cannot promote it into a whole-scope claim.

## Source and clause matrix

The source PDF, page 184, was independently rendered and visually checked. It asks:

| source row | in active scope | answered by bounded claim |
|---|---:|---:|
| General finite-`p`-group power-set subgroup powerful? | no | no |
| `p != 2`, exponent `p^2`, actual `p`-th powers form a subgroup: must it be abelian? | yes | no; only a bounded `p=3` order floor is claimed |
| `p=2`, exponent 8, squares form a subgroup: must it be abelian? | no | no |

`active_assignment_answered: pending` at triage and cannot become `yes` from the submitted bounded result.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | bounded candidate/proof use | triage result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every odd prime and every admissible finite group | freezes only `p=3`, orders at most `3^8` | fail for full scope / compatible with partial |
| `21.137-odd-p-not-2` | admissibility | prime `p>2` | `p=3` | pass |
| `21.137-odd-finite-p-group` | admissibility | finite group of order a power of the same `p` | official order-`3^7` catalogue rows and hypothetical/order-`3^8` groups | pending catalogue and reduction audit |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | exact exponent 9 filter | pending independent rerun |
| `21.137-odd-power-set-definition` | admissibility | all actual cubes, not generated subgroup | script claims `Set(Elements(G),x->x^3)` | pending code audit/rerun |
| `21.137-odd-power-set-subgroup` | admissibility | actual cube set is a subgroup | quotient-base filter uses exact set closure; direct consequence assumes subgroup | pending code and hand audit |
| `21.137-odd-P-abelian` | target conclusion | actual cube subgroup abelian | no counterexample found in bounded layer | not a proof of universal conclusion |

No `p=2` or exponent-8 evidence is admissible or will be used.

## Target versus witnesses

- Source target: all finite odd-prime groups satisfying the revision-2 hypotheses.
- Hand witness class: hypothetical exponent-9 groups `A` of order `3^8`, first with TRI3 data and then with a nonabelian actual-cube subgroup.
- Computational witness space: every official SmallGroups group of order `3^7`, used directly and as a quotient-base catalogue.
- Witness equals target: false for the universal target. The computational catalogue may equal the bounded order-`3^7` witness space only after the installed official dataset, full ID range, and loop completion are independently checked.

## Subclaims

1. Quotienting an order-`3^8` exponent-9 group with noncommuting cubes by every central subgroup of order 3 forces the centre to be cyclic.
2. TRI3 then forces that cyclic centre to be exactly `C3`, not `C9`.
3. The reviewed class-at-most-five integral identity remains applicable when only projective cube closure modulo the central `C3` is assumed, hence a TRI3 seed has class at least 6.
4. Quotienting by the cyclic centre drops class exactly one, has exponent 9, and produces an order-`3^7` quotient whose nontrivial complete actual-cube set is a subgroup; therefore only the exact exponent/class/subgroup catalogue rows are eligible bases.
5. The frozen script visits all 9310 official IDs and finds 26 exponent-9 class-5/6 rows, all with nontrivial cube sets and none with a cube set that is a subgroup.
6. The preceding facts exclude all order-`3^8` TRI3 seeds.
7. The same facts, with no hidden TRI3 assumption, exclude every direct order-`3^8` counterexample and, together with the order-`3^7` exhaustive scan plus a valid lower-order bridge, yield the direct floor `|G| >= 3^9` for `p=3` only.
8. The bounded witness family is not the active universal target.

## Tool probe

- GAP found at `/usr/bin/gap`; package metadata reports GAP/core 4.12.1-2build2. GAP itself was not executed because no Validator lease has yet been granted.
- Sage and Magma were not found.
- Python 3.12.3 found.
- Poppler `pdftotext` 24.02.0 found.

## Methods inventory

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| 1, 2, 4 | adversarial hand proof using central quotients, fibre sizes, lower central series, and exponent | the stated reductions for order `3^8` under their exact hypotheses | catalogue completeness or universal odd-prime claim |
| 3 | line-by-line dependency audit against the earlier reviewed integral identity | the class-at-most-five exclusion if every terminal membership and exponent step is valid | class 6/7 exclusion or existence/nonexistence generally |
| 5 | hash check, frozen-script semantic audit, output check, then an independently leased rerun | independent replication of the bounded official-catalogue filter | a proof outside that catalogue/order or a universal theorem |
| 6, 7 | implication audit separating TRI3 from direct counterexamples | only the exact bounded consequences whose hypotheses are established | the full revision-2 answer, other odd primes, or order at least `3^9` groups |
| 8 | source/scope comparison | correct scope limitation | any mathematical truth beyond it |

## Hard limits and recommendation

The direct-floor claim depends on two distinct finite scans, the previously reviewed class-five identity, exact class drop through the cyclic centre, and a lower-order coverage bridge. A successful rerun still gives at most a replicated bounded partial, because the computational witnesses are not the universal source target. Recommendation: continue full verification of the bounded partial only; request a short Lead lease before any GAP execution; send back or lower the direct floor if its class/lower-order bridge does not survive hand audit.
