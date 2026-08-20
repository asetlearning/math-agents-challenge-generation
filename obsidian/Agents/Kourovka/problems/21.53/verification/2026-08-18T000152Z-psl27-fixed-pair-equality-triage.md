---
title: "Verification triage — Kourovka 21.53 — PSL(2,7) fixed-pair equality"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claimant: Problem-21.53
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

# Triage — PSL(2,7) fixed-pair equality

## Claim restated

For the single admissible pair consisting of `L=PSL(2,7)` and its involution
class `D`, the set `D` has size 21, the complete product-order scheme has exactly
the colours `2,3,4`, and therefore
`Aut(Gamma)=Aut_2(Gamma) intersection Aut_3(Gamma)` under the source's one-way
definition.  This is not a claim about every admissible pair.

## Locked scope and clean-context boundary

- `scope_id`: `21.53/two-minimal-prime-colours`.
- `assignment_revision`: 2.
- Active target: for every finite nonabelian simple `L` and every involution
  conjugacy class `D`, determine whether the full product-order-colour group is
  `Aut_2(Gamma) intersection Aut_p(Gamma)`, where `p` is the second-smallest
  distinct prime divisor of `|L|`.
- Excluded here: Problem 21.52's induction-by-`Aut(L)` question, unions of
  involution classes, arbitrary choices of `p`, and presentation of a bounded list
  as the universal answer.
- Clean input inspected: the rendered source-PDF page 172, the revision-2 scope
  record, and only the submitted cycle-7 `partial-result.md`, its `log.md`, and the
  three artifacts explicitly linked there.  No prior 21.53 verification note or
  solution-bearing history was inspected.

## Source-clause matrix

| source clause | active target meaning | submitted claim | triage result |
|---|---|---|---|
| inherited notation from 21.52 | finite nonabelian simple `L`; one conjugacy class `D` of involutions; complete graph on `D`; colour is exact product order | instantiates `L=PSL(2,7)` and one alleged 21-element involution class | verify independently |
| `Aut_t(Gamma)` | a permutation need only send every `t`-edge to a `t`-edge; an absent `t`-relation gives the vacuous full symmetric group | complement argument explicitly uses this one-way convention | verify by finite-set argument |
| full colour group | intersection over every positive-integer label, equivalently every occurring colour plus vacuous absent labels | alleged occurring labels are exactly `2,3,4` | verify inventory independently |
| question | equality for every admissible `(L,D)`, with `p` the second-smallest distinct prime divisor | equality for one fixed pair only | bounded partial result; `active_assignment_answered: no` regardless of a successful check |

The rendered page uses `G` in the final question while saying "in the notation of
21.52"; revision 2 canonically identifies that group with the inherited `L`.  The
submitted fixed pair follows that audited interpretation.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | submitted value / proof use | evidence to check | triage state |
|---|---|---|---|---|---|
| `21.53-forall-L-D` | admissibility | every admissible pair is quantified | only `PSL(2,7)` and its involution class | scope and bounded wording | not answered |
| `21.53-L-finite-nonabelian-simple` | admissibility | `L` finite, nonabelian, simple | projective group of order 168; noncommuting pair; alleged exhaustive simplicity certificate | independent permutation model and normal-closure test | pending |
| `21.53-D-single-involution-class` | admissibility | one conjugacy class, all elements of exact order 2 | alleged unique class of size 21 | independent order and conjugacy enumeration | pending |
| `21.53-Gamma-product-order-colouring` | admissibility | all 210 unordered pairs coloured by exact order of the product | displayed `21 x 21` matrix and linked certificate | independent 210-product reconstruction | pending |
| `21.53-Aut-t-definition` | admissibility | one-way preservation for every label, with vacuous absent-label case | finite-injection/complement argument | direct hand proof after colour inventory | pending |
| `21.53-two-minimal-primes` | admissibility | `p` is the least prime divisor above 2 | `|L|=168=2^3*3*7`, so `p=3` | independent group order and arithmetic | pending |
| `21.53-full-colour-group-definition` | admissibility | preserve every occurring colour; absent labels impose nothing | alleged colours `2,3,4` | inventory plus source definition | pending |
| `21.53-two-colours-determine-all` | target conclusion | full group equals the 2/`p` intersection | colour 4 is the complement of colours 2 and 3 | direct finite-set proof | pending for this pair only |

## Target versus witness

- Source target: the universal class of all admissible pairs `(L,D)`.
- Exact bounded claim target: `PSL(2,7)` and its one involution class.
- Computational witness proposed by the claimant:
  `SL(2,7)/{+I,-I}` with canonical matrix representatives.
- Planned independent witness: the faithful permutation image on
  `P^1(F_7)` generated by `x -> x+1` and `x -> -1/x`.
- Witness identity status: pending.  The verification will include the elementary
  proof that the projective action of `SL(2,7)` has kernel `{+I,-I}`, and that the
  two displayed transformations generate its image.  Thus a successful run checks
  the exact fixed-pair claim rather than a quotient or lookalike.  It cannot turn
  that fixed pair into the universal source target.

## Sub-claims

1. The independently generated permutation group is exactly `PSL(2,7)`.
2. It has 168 elements and contains a noncommuting pair.
3. Every nonidentity conjugacy-class representative has full normal closure, so
   the group is simple.
4. Its exact order distribution is `1:1, 2:21, 3:56, 4:42, 7:48`.
5. Its 21 involutions form one conjugacy class.
6. All 210 products of distinct involutions have orders only `2,3,4`, with counts
   `42,84,84`.
7. The claimant's 21 matrix labels induce these same projective permutations and
   the claimant's complete matrix, CSV, and edge list agree entry by entry with the
   independent products.
8. Under the one-way convention, a permutation preserving `E_2` and `E_3` maps
   each finite relation onto itself; it therefore preserves the complementary
   relation `E_4` and hence every colour.
9. These facts establish one bounded equality only, not the universal assertion.

## Tool probe

- Python: `/usr/bin/python3`, version `3.12.3`.
- GAP: `/usr/bin/gap`, version `4.12.1` (available but not needed by the planned
  checker).
- Sage and Magma: not found.
- GNU `sha256sum`: coreutils `9.4`.

## Methods inventory

| sub-claim | method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| 1 | hand proof of the projective action plus a separately written 8-point permutation closure checker | the independent finite model is the exact fixed group | any statement for other simple groups |
| 2--5 | exhaustive permutation multiplication, orders, conjugation, and normal closures | finiteness, nonabelianity, simplicity, and the unique involution class for this model | a classification theorem or family result |
| 6--7 | exhaustive products in the permutation model and entrywise comparison with the frozen certificate | the full fixed-pair product-order scheme and agreement of two independent implementations | automorphism-group orders or generators |
| 8 | hand proof using injectivity on the finite edge set and set complement | fixed-pair equality once `2,3,4` exhaust the colours | equality when another colour occurs |
| 9 | scope and quantifier audit | correct bounded interpretation | the universal target |

## Hard limits and recommendation

The proposed checker is a small, bounded certificate checker, not an
automorphism-group search.  Before it is executed, its source will be frozen and a
Lead compute lease will be requested with the exact command, resource estimate,
and timeout.  No mathematical verification computation has been run in this
validation session.  If the independent run and hand proof pass, recommend
`status/replicated` for the fixed-pair partial result and
`active_assignment_answered: no`; otherwise report the first failing sub-claim.
