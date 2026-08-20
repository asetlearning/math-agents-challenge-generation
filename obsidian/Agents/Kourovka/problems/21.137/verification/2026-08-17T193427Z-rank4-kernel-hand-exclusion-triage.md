---
title: "Verification triage — Kourovka 21.137 — rank-four kernel hand exclusion"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

# Triage — rank-four kernel hand exclusion

## Claim restated

For every finite extension
\(1\to P\to G\to A\to1\), where
\(P=3_+^{1+4}\times C_3^2\) and \(A\) is elementary abelian, every pair of
literal actual cubes in \(G\) commutes.

This is a proper-family theorem only. It does not answer the active universal
odd-prime assignment.

## Scope and clause matrix

Source PDF page 184 was independently rendered and read. The active source clause
is: for odd \(p\), if the actual \(p\)-th powers in a finite \(p\)-group of
exponent \(p^2\) form a subgroup, must that subgroup be abelian?

| source clause | active | claim answers | remains open |
|---|---:|---:|---|
| General powerfulness question | no | no | excluded from this atomic scope |
| Odd-prime exponent-\(p^2\) abelianity clause | yes | only the stated \(p=3\) extension family | every other admissible group |
| \(p=2\), exponent-eight clause | no | no | explicitly excluded |

`active_assignment_answered: pending` at triage, with `yes` already impossible
because the bounded family is proper.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | candidate/proof use | triage result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | fixes \(p=3\), one kernel, elementary quotient | fail for universal coverage |
| `21.137-odd-p-not-2` | admissibility | \(p=3>2\) | pass in family |
| `21.137-odd-finite-p-group` | admissibility | finite extension of finite 3-groups | pass in family |
| `21.137-odd-exponent-p2` | admissibility | bounded proof applies to exact-exponent-nine members; exponent is at most nine | pending derivation |
| `21.137-odd-power-set-definition` | admissibility | claim uses every element in every coset, not generated powers | pending derivation |
| `21.137-odd-power-set-subgroup` | admissibility | not assumed for pairwise-commutation theorem; used only in final implication | pending derivation |
| `21.137-odd-P-abelian` | target conclusion | follows in family if every two actual cubes commute | pending derivation |

The routed item is `REPORT`/`PARTIAL_RESULT`, not a full-scope `CLAIM`; no linked
claim-check JSON is required or supplied. This cannot be upgraded into a scope
answer by the state gate.

## Target versus witness

- Source target: all finite same-prime odd-\(p\) groups of exact exponent \(p^2\)
  satisfying literal power-set closure.
- Checked object: the symbolic class of all finite elementary-quotient extensions
  of \(3_+^{1+4}\times C_3^2\).
- Witness equals target: false. The checked class is a proper subclass.

## Subclaims

1. The BCH kernel law and automorphism form are exact, with no omitted nonlinear
   term.
2. The section-cube formula and cube-inner shear equation have the claimed order
   and signs.
3. Every order-three element of \(\operatorname{Sp}_4(3)\) has square-zero
   nilpotent part; commuting actions also satisfy \(N_uN_v=0\).
4. The common image/fixed-space trichotomy and global label invariance are complete.
5. The square-zero center branch has no hidden rank or division assumption.
6. The regular \(J_3\) center branch, its centralizer, the \(b=0\) branch, and the
   outer-commutation shear equations are exact.
7. Orthogonality of projected labels implies commutation for arbitrary central
   cube coordinates, using the literal all-coset cube set.
8. The checked family is proper and therefore does not answer revision 2.

## Tools and methods inventory

Available: GAP 4.12.1, Python 3.12.3, `pdftotext` 24.02.0; Sage and Magma are not
installed. Source PDF page 184 was also inspected as a rendered image.

| method | subclaims | a pass proves | a pass does not prove |
|---|---|---|---|
| line-by-line finite-field algebra | 1--8 | the bounded universal extension theorem, if every identity closes | the unrestricted Kourovka clause |
| independent Python enumeration over \(\mathbb F_3\) | 3, 4, regular-center centralizer | the exact finite linear-algebra classifications encoded | arbitrary factor-set existence or the group theorem by itself |
| literal-coset audit | 2, 7 | every actual cube is included and central coordinates are harmless | closure of the cube set in an arbitrary member |

## Hard limits and recommendation

No heavy computation or lease is needed. A small bounded checker is authorized only
for the finite symplectic and \(3\times3\) centralizer subclaims; the main theorem
must stand by hand. Proceed to full verification of the bounded theorem only, with
final outcome necessarily `PARTIAL_RESULT` and
`active_assignment_answered: no`.
