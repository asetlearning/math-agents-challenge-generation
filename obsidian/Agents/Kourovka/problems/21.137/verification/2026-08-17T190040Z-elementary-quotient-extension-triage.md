---
title: "Verification triage — Kourovka 21.137 — elementary-quotient extension family"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "For p=3, every finite exponent-at-most-nine extension of H_3(3) x C_3^3 by a finite elementary abelian 3-group has pairwise commuting actual cube values."
claimant: Problem-21.137-Counterexample
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

# Triage

## Claim and locked scope

The submitted bounded claim is: for every finite extension

\[
1\to K\to G\to A\to1,
\qquad K\cong H_3(3)\times C_3^3,
\]

with finite elementary abelian quotient \(A\) and \(\exp G\mid9\), all actual
cubes \(g^3\) commute pairwise.  Consequently no such extension can have its
literal cube-value set equal to the nonabelian kernel \(K\).

The locked active target is scope `21.137/odd-prime-exponent-p2`, revision 2:
for every odd prime \(p\) and finite \(p\)-group \(G\) of exponent exactly
\(p^2\), if the literal set \(\{g^p:g\in G\}\) is a subgroup, prove that it is
abelian.  The separate \(p=2\), exponent-eight clause is excluded.  The bounded
claim does not answer that universal target.

The rendered source PDF, page 184, was visually checked.  It has three clauses:

| source clause | active? | submitted claim |
|---|---:|---|
| General powerfulness question | no | not answered |
| \(p\ne2\), exponent \(p^2\), subgroup of actual \(p\)-th powers: must it be abelian? | yes | only the special \(p=3\), fixed-kernel, elementary-quotient family |
| \(p=2\), exponent 8, actual squares: must they be abelian? | no | excluded and not used |

`active_assignment_answered: pending` at triage; it must be `no` in the final
note regardless of whether the bounded theorem passes.

## Constraint-and-conclusion matrix

| constraint_id | role | candidate value / proof use | triage result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | only \(p=3\), one kernel type, and elementary abelian quotient | fail for active universal target |
| `21.137-odd-p-not-2` | admissibility | \(p=3\) | pass within bounded family |
| `21.137-odd-finite-p-group` | admissibility | finite kernel and finite elementary abelian quotient give a finite 3-group | pass within bounded family |
| `21.137-odd-exponent-p2` | admissibility | theorem assumes exponent dividing 9; a saturated nontrivial cube set would force exact exponent 9 | sufficient for the family exclusion, not universal coverage |
| `21.137-odd-power-set-definition` | admissibility | must use the full union of every coset cube image, never a generated subgroup or one norm image | pending exact reconstruction |
| `21.137-odd-power-set-subgroup` | admissibility | not assumed by the stronger bounded theorem; equality of the literal cube set with nonabelian \(K\) would imply it | pending logical bridge |
| `21.137-odd-P-abelian` | target conclusion | pairwise commuting actual cubes is claimed only in the bounded family | pending proof; universally unanswered |

No proposed group is a target witness.  The claim is a universal exclusion of a
proper subclass, so “witness equals target” is false as a scope-coverage statement.
The kernel denoted \(K\) must also not be silently identified with the source's
power set unless literal equality has been established.

## Subclaims

1. The normalized-section multiplication, associativity identities, and ordered
   cube formula are correct for every nonabelian extension in the family.
2. The literal cube set is exactly the union of all coset cube images (including
   the zero coset), and saturation with \(K\) is the correct target-facing bridge.
3. The induced maps on \(K/Z(K)\cong\mathbb F_3^2\) form a homomorphism \(M:A\to
   GL_2(3)\), and each has cube one.
4. If \(M(A)\ne1\), every coset cube image has a constant noncentral label,
   conjugation fixes that label under all of \(M(A)\), and all labels lie on one
   line.
5. If \(M(A)=1\), for any nonzero cube label \(q\), the associated action satisfies
   \(\alpha_u^3\) inner, with the correctly signed block equations \(R^3=0\) and
   \(R^2L=J_q\).
6. The full centralizer of a \(J_3+J_1\) nilpotent block, together with the outer-
   commutation equation, forces every two nonzero labels to be dependent.
7. Zero labels cause no exception, and labels on one \(V\)-line imply the actual
   cube elements—not merely their images modulo the center—commute in \(K\).

## Tools and methods inventory

Available probes: GAP at `/usr/bin/gap` (version output to be re-probed without
stderr suppression), Python 3.12.3, and Poppler `pdftotext` 24.02.0.  Sage and
Magma are absent.  No computation was submitted.

| subclaim | independent method | what a pass proves | what it does not prove |
|---|---|---|---|
| 1–2 | direct hand collection from the section law | exact factor order, associativity, cube images, literal union | no existence or universal source result |
| 3–4 | hand linear algebra in dimension two; optional exhaustive `GL_2(3)` check | the nontrivial-action branch for every finite rank of \(A\) | nothing about other kernels or primes |
| 5–6 | block calculation plus an independently designed finite-field centralizer checker | the trivial-action branch if every sign and normal-form parameter survives | no classification of arbitrary extensions outside the family |
| 7 | direct commutator formula in \(K\) | pairwise commutativity of actual cube values in this kernel | equality of the cube set with \(K\), or the active universal theorem |

There is no relevant linked claim-check JSON; the only current 21.137 claim-check
belongs to a different graded-image partial.  Because this submission is labelled
`PARTIAL_RESULT`, not a scope-closing `CLAIM`, this is recorded as a completeness
limitation rather than treated as evidence.

## Recommendation and hard limits

Proceed with full hostile verification of this bounded hand theorem.  Even a pass
can certify only the stated family exclusion and must retain
`active_assignment_answered: no`.  It cannot exclude nonabelian exponent-three
quotients, other kernels, other odd primes, or the unrestricted source scope.
