---
title: "NON-EVIDENTIARY SCRATCH — triage — even PSL(2,q) revision-2 partial theorem"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claim: "For every q=2^f with f>=2, and also for the identical PSL(2,5)=A5 pair transported from q=4, the unique involution-class product-order colouring satisfies Aut(Gamma)=Aut_2(Gamma) intersect Aut_3(Gamma)=PGammaL(2,q)."
claimant: Problem-21.53-Proof
active_assignment_answered: pending
evidentiary_status: invalid-clean-context
not_a_verdict: true
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# NON-EVIDENTIARY SCRATCH

This triage belongs to a validator context later invalidated by an unauthorized
read of prior solution-bearing verification notes.  It is preserved only as
scratch, is not a protocol triage artifact, and must not be cited as evidence or
as a mathematical verdict.

# Draft triage — even-characteristic `PSL(2,q)` partial theorem

## Locked scope and claim

The current canonical record is `21.53/two-minimal-prime-colours`, assignment
revision 2.  Its active target quantifies over every finite nonabelian simple
group `L` and every one of its involution conjugacy classes `D`.  The submitted
claim is deliberately narrower: all `PSL(2,2^f)`, `f>=2`, and the one abstract
`A5` pair represented both by `PSL(2,4)` and `PSL(2,5)`.  It is therefore an
infinite-family partial result even if every proof step passes.

Excluded are Problem 21.52, unions of involution classes, replacement of the
second-smallest prime by an arbitrary prime, and any inference from a bounded
list to the universal target.

The routed artifact hashes agree with the messages:

```text
166e06dd864c2ee612c7bbaadcf03b4b58f60371f3779b3bdaadbf55a7eb911b  Agents/Kourovka/problems/21.53/runs/2026-08-17-r4-psl2q-two-colour-rigidity/partial-result.md
6968a5a73278031d5d01742add87a9c38d5cfcffe40c04ab8b9599d04004e02e  Agents/Kourovka/problems/21.53/claim-checks/21.53-psl2-even-r2-partial-001.json
```

## Source clause matrix

| source clause | exact role | submitted claim | state before deep check |
|---|---|---|---|
| inherited 21.52 notation | `L` finite nonabelian simple; `D` one involution class; complete graph coloured by exact product order | exact for the asserted even-`PSL_2` subfamily and transported `A5` pair only | pending |
| `Aut_t` | permutations carrying every exact `t`-edge to an exact `t`-edge; empty relation is vacuous | claimant says it uses the literal implication and finite bijectivity | pending |
| full `Aut(Gamma)` | intersection of every exact-colour stabilizer | claimant says all determinant/trace colours are preserved | pending |
| question | equality with colours at the two smallest distinct prime divisors | claimant identifies these as `2,3` throughout its subfamily | pending |

`active_assignment_answered: pending` at triage; it cannot become `yes` from
this bounded claim.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | independent gate at triage |
|---|---|---|---|
| `21.53-forall-L-D` | admissibility | every canonical pair `(L,D)` | not answered canonically; only the named strict subfamily is claimed |
| `21.53-L-finite-nonabelian-simple` | admissibility | finite nonabelian simple `L` | must check simplicity for `PSL(2,2^f)`, `f>=2`, and `A5` |
| `21.53-D-single-involution-class` | admissibility | one complete class of order-2 elements | must reconstruct exhaustiveness, injectivity, and conjugacy of the vector model |
| `21.53-Gamma-product-order-colouring` | admissibility | every unordered distinct pair coloured by exact product order | must check the product trace/characteristic-polynomial argument, including repeated-root cases |
| `21.53-Aut-t-definition` | admissibility | literal one-way source implication and vacuous absent labels | must justify conversion to setwise equality by finite bijectivity and audit empty relations |
| `21.53-two-minimal-primes` | admissibility | `2` and least prime greater than `2` dividing `|L|` | must derive the order and show `3` divides it in every asserted case |
| `21.53-full-colour-group-definition` | admissibility | intersection over all exact product-order colours | must prove the proposed semilinear group preserves exact order, not merely trace or selected relations |
| `21.53-two-colours-determine-all` | target conclusion | full group equals the `2/3` intersection | must audit the coordinate functional equation without using zero vertices or loops |

## Target versus witness

- Source target: every admissible pair `(L,D)` from Problem 21.53.
- Active assignment: the same universal revision-2 target.
- Witness family: exact matrix groups `SL(2,F_q)=PSL(2,F_q)` for `q=2^f`,
  `f>=2`, acting on the asserted full involution class; plus the abstract `A5`
  pair transported from `q=4` to `q=5`.
- Witness equals canonical target: **false**.  It is a strict infinite
  subfamily.  This is compatible with a partial-result verdict only.

No finite discovery computation is a witness for the theorem.  The submitted
proof is a hand derivation in the exact matrix groups.

## Subclaims and methods inventory

| subclaim | method authorized for this audit | what a pass proves | what it does not prove |
|---|---|---|---|
| the second prime is `3` | hand check of `|PSL(2,q)|` | correct source parameter in the asserted family | nothing outside `PSL_2` |
| vertices are exactly one complete involution class | direct matrix and conjugacy calculation | target-object fidelity for even `q` | odd `q` or other simple groups |
| order 2 is dependence and order 3 is determinant one | direct multiplication and Cayley--Hamilton | exact identification of the two selected edge sets | recovery of all other colours |
| every two-relation permutation is semilinear determinant-one | line-by-line audit of the normalized coordinate functional equations | the upper bound `Aut_2 intersect Aut_3 <= GammaSL(2,q)` | preservation of every product-order colour |
| the semilinear group preserves every colour | eigenvalue/field-conjugacy argument | the reverse inclusion into the full colour group | any odd-characteristic shell rigidity |
| `q=5` gives the identical pair | abstract group/class transport | that one additional pair only | the general odd family |
| claim-check completeness | frozen repository state checker | all revision-2 IDs are present and mechanically coherent | truth of any row |

The state checker exited zero with seven unrelated legacy/old-revision warnings
and no errors.  No nontrivial computation is authorized or planned: any such run
would first need a frozen manifest and a Lead lease.

## Tool probe

```text
/usr/bin/gap
/usr/bin/python3
/usr/bin/pdftotext
4.12.1
Python 3.12.3
pdftotext version 24.02.0
```

`sage` and `magma` were absent.  These tools are not needed for the submitted
hand proof.

## Hard limits and recommendation

Proceed with full line-by-line hand verification of the bounded theorem.  Do not
inspect or rerun the claimant's discovery computation.  The odd-characteristic
trace reduction culminates in an expressly unproved orthogonal-shell rigidity
lemma and cannot receive a family verdict here.  The leased `q=27` result, if
mentioned at all, is one finite stress test only.  Neither limitation can change
the required final value `active_assignment_answered: no`.
