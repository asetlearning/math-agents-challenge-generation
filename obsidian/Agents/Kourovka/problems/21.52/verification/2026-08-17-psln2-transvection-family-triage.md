---
title: "Verification triage — Kourovka 21.52 — PSL_n(2) transvection family"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
scope_record: Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
assignment_revision: 1
claimant: Problem-21.52-Proof
audit_type: family-partial-hand-proof
active_assignment_answered: no
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/projective-geometry
  - project/kourovka
  - status/draft
---

# Verification triage — Kourovka 21.52 — PSL_n(2) transvection family

## Claim restated

For every integer \(n\geq 3\), if
\(L=\operatorname{PSL}_n(2)=\operatorname{GL}_n(2)\) and \(D\) is the one
conjugacy class of rank-one transvections, then every permutation of \(D\)
preserving \(|xy|\) for all distinct \(x,y\in D\) is induced on \(D\) by an
automorphism of \(L\) stabilizing \(D\).

This is explicitly a family partial. It does not quantify over every finite
nonabelian simple \(L\) and every involution class \(D\), so it cannot answer the
active assignment.

## Locked scope and revision

- `scope_id`: `21.52/involution-class-product-order-colouring`
- `assignment_revision`: `1`
- Exact active target: for every finite nonabelian simple group \(L\) and every
  conjugacy class \(D\) of involutions in \(L\), every product-order-colour
  preserving permutation of \(D\) is induced by an automorphism of \(L\)
  stabilizing \(D\) setwise.
- Excluded: Problem 21.53; the union of all involution classes; the uncoloured
  complete graph; colouring by the conjugacy class of \(ab\); and any bounded
  family offered as a proof of the universal assertion.

The request is a `QUESTION` asking for an audit of a partial theorem, not a
universal `CLAIM`. No family-specific `claim-checks` JSON is linked. The existing
`21.52-psl27-colour-r1-partial-001.json` concerns the separate fixed
\(\operatorname{PSL}(2,7)\) computation and is not a completeness gate for this
argument.

## Source clause matrix

The configured PDF page 172 was independently rendered and visually inspected.

| source clause | exact role | active here? | family claim answers? |
|---|---|---:|---:|
| `c-objects` | \(L\) finite nonabelian simple; \(D\) one involution class | yes | only for the stated \(\operatorname{PSL}_n(2)\) family/class |
| `c-colouring` | complete graph on \(D\), with colour exactly \(|ab|\) | yes | yes within the family |
| `c-colour-automorphism` | every edge colour is preserved by \(\tau\in S_D\) | yes | yes within the family |
| `c-question` | every such \(\tau\) is induced by an automorphism of \(L\) | yes | claimed only within the family |

`active_assignment_answered: no` is fixed at triage: the universal object clause
is not covered even if every family argument passes.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate/proof use | triage result |
|---|---|---|---|---|
| `21.52-forall-L-D` | admissibility | every admissible pair \((L,D)\) | only \(L=\operatorname{PSL}_n(2)\), \(n\ge3\), and rank-one transvections | **unknown / uncovered** |
| `21.52-L-finite-nonabelian-simple` | admissibility | \(L\) finite nonabelian simple | standard simplicity theorem plus \(\operatorname{GL}_n(2)=\operatorname{PSL}_n(2)\) | pending hand audit |
| `21.52-D-single-involution-class` | admissibility | one conjugacy class of elements of order two | incident flags parameterize one class of rank-one transvections | pending hand audit |
| `21.52-Gamma-complete-on-D` | admissibility | all unordered pairs of distinct vertices | derivation consistently restricts to distinct flags | pending hand audit |
| `21.52-edge-colour-exact-product-order` | admissibility | exact colour is \(|xy|\) | exact proposed table \(2,3,4\) from two cross-incidences | pending hand audit |
| `21.52-tau-preserves-all-edge-colours` | admissibility | \(\tau\) preserves every product order | only preservation of order 2 is used to reconstruct incidence | pending hand audit |
| `21.52-tau-induced-by-AutL` | target conclusion | every such \(\tau\) extends | proposed conjugation or inverse-transpose composition | pending hand audit for family only; **not proved universally** |

## Target versus witness

- Source target: the universal class of all pairs \((L,D)\) in Problem 21.52.
- Witness/model actually used: the symbolic exact matrices
  \(t_{u,f}=I+u\otimes f\) in \(\operatorname{GL}(\mathbb F_2^n)\), with
  \(u,f\ne0\) and \(f(u)=0\), for arbitrary \(n\ge3\).
- Witness equals the claimed family: pending verification of the flag
  parametrization and \(\operatorname{GL}_n(2)=\operatorname{PSL}_n(2)\).
- Witness equals the source target: **false**; it is a strict family/class
  specialization. Therefore `active_assignment_answered: no` regardless of the
  internal proof outcome.

The model is defined independently from the property under test: it is the
ordinary rank-one transvection class in the ambient linear group, not a structure
manufactured by imposing colour-automorphism relations. No circular object
construction is apparent at triage.

## Subclaims and methods inventory

| subclaim | authorised method | what a pass proves | what it does not prove |
|---|---|---|---|
| the matrix model is precisely the stated class in \(L\) | direct linear-algebra proof and standard PSL simplicity theorem | family admissibility | anything about other involution classes/groups |
| the order table is exactly \(2,3,4\) | independent algebraic expansion, including both asymmetric cases | colour 2 is exactly mutual cross-incidence | universal colour behaviour |
| every maximal colour-2 clique is a unique \(K_U\), and every \(K_U\) is maximal | two-inclusion hand proof | intrinsic clique classification | any assertion about unrelated classes |
| minimum maximal cliques are point/hyperplane stars, including \(n=3\) | exact size comparison and low-dimensional check | recovery of endpoint types | that their incidence graph is already connected |
| clique intersections recover a connected bipartite incidence graph | direct projective-space incidence argument | bipartition recoverable up to global swap | realization by group automorphisms |
| every type-preserving incidence automorphism is linear | direct \(\mathbb F_2\)-additivity proof | conjugation realizes it | type-swapping actions |
| every type-swapping incidence automorphism is inverse-transpose composed with conjugation | explicit action calculation with composition order | realization on all flags/transvections | universal Problem 21.52 |
| witness equals universal target | scope comparison | a pass would be needed for universal closure | it is already false for this family-only artifact |

No computation is needed. A pass of the line-by-line hand audit can establish a
family theorem, but cannot establish the active universal assignment.

## Tools probed

Bounded availability probe on 2026-08-17:

- GAP 4.12.1: available at `/usr/bin/gap`.
- Python 3.12.3: available at `/usr/bin/python3`.
- `pdftotext` and `pdftoppm` 24.02.0: available; page 172 was rendered.
- Sage: unavailable.
- Magma: unavailable.

These tools are not needed for the proposed hand verification, and no heavy job
is authorised or planned.

## Hard limits and recommendation

The audit can decide the exact family theorem by hand. It cannot promote the
universal notebook assertion because the row `21.52-forall-L-D` remains unknown.
The missing family-specific claim-check prevents treating this `QUESTION` as a
machine-gated universal claim, but does not prevent answering the requested
mathematical audit.

**Recommendation:** proceed with full line-by-line verification of the family
partial only, with hostile checks of the two asymmetric order-four expansions,
maximal-clique converse and maximality, \(n=3\), connectivity/bipartition,
direct additivity, and the order of the type-swapping composition.
