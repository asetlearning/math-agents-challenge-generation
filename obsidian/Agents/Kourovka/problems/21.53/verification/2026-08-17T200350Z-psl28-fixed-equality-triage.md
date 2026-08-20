---
title: "Triage — Kourovka 21.53 — fixed PSL(2,8) two-colour equality"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claimant: Problem-21.53
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# Triage — fixed `PSL(2,8)` two-colour equality

## Claim restated

For the unique conjugacy class `D` of 63 involutions in the finite nonabelian
simple group `L = PSL(2,8)`, the complete product-order-coloured graph has colours
`2,3,7,9`, and its full colour-preserving permutation group equals
`Aut_2(Gamma) intersect Aut_3(Gamma)`; both are reported to have order 1512.

This is a bounded fixed-pair statement only. It does not answer the universal
revision-2 assignment.

## Scope lock and source clause matrix

Canonical scope: `21.53/two-minimal-prime-colours`, revision 2.

The rendered source PDF, page 172, was inspected directly. Problem 21.53 inherits
from 21.52: a finite nonabelian simple group, one conjugacy class `D` of
involutions, and the complete graph on `D` coloured exactly by `|ab|`. It defines
`Aut_t(Gamma)` for every positive integer `t` by preservation of `t`-edges, states
`Aut(Gamma)=intersection_t Aut_t(Gamma)`, and asks whether the intersection can
always be reduced to the two smallest distinct prime divisors `{2,p}` of the group
order.

| source row | active | fixed claim addresses | remains open |
|---|---:|---|---|
| inherited finite-nonabelian-simple `L`, one involution class `D`, exact product-order colouring | yes | the proposed pair `(PSL(2,8),D)` | every other admissible pair |
| `Aut_t` for every positive integer, vacuous when no `t`-edge occurs | yes | labels `2,3` and all occurring labels must be encoded exactly | general absent-label cases |
| full group is the intersection over all occurring product-order colours | yes | reported comparison for colours `2,3,7,9` | universal statement |
| `{2,p}` are the two smallest distinct prime divisors | yes | reported `|L|=504`, hence `p=3` | universal statement |
| equality question for every admissible `(L,D)` | yes | one positive instance only | universal assignment |

`active_assignment_answered: pending` at triage, and it is mechanically incapable
of becoming `yes` from this fixed-pair equality alone.

Excluded: Problem 21.52's separate induction-by-`Aut(L)` question, unions of
involution classes, arbitrary choices of `p`, and any inference from a bounded list
to the universal conclusion.

## Independently reconstructed constraint-and-conclusion matrix

| constraint id | role | required condition | proposed fixed-pair value/use | triage result |
|---|---|---|---|---|
| `21.53-forall-L-D` | admissibility/quantifier | every admissible pair is quantified | claim explicitly restricts to one pair | partial only |
| `21.53-L-finite-nonabelian-simple` | admissibility | finite nonabelian simple `L` | matrix model asserted to be `PSL(2,8)` | pending reconstruction and simplicity theorem |
| `21.53-D-single-involution-class` | admissibility | exactly one involution class | 63-element orbit asserted equal to all involutions | pending reconstruction |
| `21.53-Gamma-product-order-colouring` | admissibility | every unordered distinct pair labelled by exact product order | complete 63-by-63 matrix supplied | pending independent rebuild |
| `21.53-Aut-t-definition` | admissibility | exact implication definition for every `t` | incidence encodings asserted for `t=2,3,7,9` | pending encoding audit |
| `21.53-two-minimal-primes` | admissibility | `2,p` are two least distinct prime divisors | `504=2^3*3^2*7`, so `p=3` | arithmetic passes if group order passes |
| `21.53-full-colour-group-definition` | admissibility | preserve every occurring colour | full encoding asserted to include all four relations | pending audit |
| `21.53-two-colours-determine-all` | conclusion | full group equals `Aut_2 intersect Aut_p` | equality and common order 1512 asserted | pending independent completeness proof |

No `Agents/Kourovka/problems/21.53/claim-checks/` directory or linked clean
claim-check JSON was found. The routed item is a `REPORT` of bounded partial
progress rather than a universal `CLAIM`, but this is still a protocol completeness
gap to record before any certification.

## Target versus witness

- Source target: a universal assertion over every finite nonabelian simple group and
  every involution class inherited from 21.52.
- Active assignment: exactly that universal revision-2 assertion.
- Fixed witness under review: an explicit 504-matrix model over
  `F_2[x]/(x^3+x+1)`, with its asserted 63-element involution class.
- Status of witness equals the claimed fixed object: pending independent proof.
- Status of witness equals the universal target: false as a matter of scope; it is
  one admissible instance, not the quantified class.

The witness was generated from the independent field/group definition, not from the
desired equality, so the equality is not true by construction. The claimant's
automorphism computation was, however, run on a product-order matrix made by its
own model builder; the validator must rebuild that matrix independently.

## Subclaims

1. `F_2[x]/(x^3+x+1)` is `GF(8)` and the listed determinant-one matrices form
   `SL(2,8)=PSL(2,8)` of order 504.
2. This group is finite, nonabelian, and simple.
3. Its nonidentity involutions form one conjugacy class of size 63.
4. `p=3` is the second-smallest distinct prime divisor of 504.
5. The complete unordered product-order matrix has exactly colours `2,3,7,9`,
   edge counts `189,252,756,756`, and valencies `6,8,24,24`.
6. The two-colour incidence object encodes exactly the order-2 and order-3
   relations; the full incidence object encodes exactly all four relations, with
   no accidental part or colour permutations.
7. The supplied explicit generator lists are permutations on the same 63 labelled
   vertices and have the claimed preservation properties.
8. The complete automorphism groups of the two incidence structures are equal,
   not merely two exhibited subgroups of equal-looking generators.
9. None of these fixed-pair checks answers the universal scope.

## Tool probe

- GAP 4.12.1: available.
- Python 3.12.3: available.
- `dreadnaut`: available.
- Poppler `pdftotext` 24.02.0 and `pdftoppm`: available.
- Sage and Magma: not found.

## Methods inventory

| subclaims | independent method | what a pass proves | what it does not prove |
|---|---|---|---|
| 1--5 | fresh bounded checker using a separately written `GF(8)`/matrix representation and complete enumeration | exact fixed group/class/product matrix and prime | simplicity without the classical theorem; any other pair |
| 2 | classical theorem: `PSL(2,q)` is simple for `q>3`, plus explicit noncommuting elements | finite nonabelian simplicity of this reconstructed group | the graph-group equality |
| 6--7 | parse claimant certificates, recompute hashes, and directly test every listed image against the independently rebuilt matrix | correctness of encodings and exhibited generators | completeness of either automorphism group |
| 8 | separately designed block/matching backtracker exploiting the nine order-2 cliques and order-3 perfect matchings, or a direct structural upper bound | complete equality for this one finite pair | universal equality |
| 9 | scope matrix | bounded nature of the verdict | any progress on untested pairs |

## Hard limits and recommendation

A claimant-script rerun cannot yield an independent verdict. Any computation
expected to exceed 60 seconds or 1 GB requires a Lead lease. A compact bespoke
certificate checker is authorised only if its semantics are auditable and its
search is explicitly bounded.

Recommendation: proceed with partial fixed-pair verification only, first by an
independent reconstruction and then by a bespoke completeness argument for the
two-colour automorphism group. Retain `active_assignment_answered: no` under every
outcome. Do not promote the universal scope. The missing claim-check gate must be
reported in the final protocol verdict.
