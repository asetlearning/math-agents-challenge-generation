---
title: "Triage — Kourovka 20.115 — L4(3) prime-2 block-defect bridge"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
claimant: Problem-20.115-Proof
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

# Triage — finite `L4(3)` prime-2 block-defect bridge

## Claim, restated

For the centerless simple group (L=\operatorname{PSL}_4(3)) at (p=2), every
ordinary (2)-block (B) has a defect group (D_B) satisfying

\[
\exp(D_B)\leq (|L|/\theta(1))_2
\quad\text{for every }\theta\in\operatorname{Irr}(B),
\]

and the exact hypotheses of Malle--Navarro--Tiep Proposition 3.2 therefore imply
the (2)-part of Condition (1.1) for the nearly-simple triples covered by that
proposition whose derived subgroup is (L). This is a bounded sufficient bridge,
not the universal assertion in Kourovka 20.115.

## Locked scope

- `scope_id`: `20.115/nonzero-character-order-divisibility`.
- `assignment_revision`: `1` (the routed claim also names revision 1).
- Exact active target: for every finite group (G), every ordinary irreducible
  complex character (\chi\), and every (x\in G), (\chi(x)\ne0) implies the
  exact integer divisibility (o(x)\chi(1)\mid |G|).
- Excluded: Brauer characters, zero values, reducible characters, the already-known
  solvable restriction, the weaker fourth/fifth-power bound, and any bounded
  character-table screen presented as a universal proof.
- Source check: page 161 of the rendered 20th Issue (2022) was visually inspected;
  its question and both contextual sentences agree with the scope record.

## Clause matrix

| source clause | active? | what this claim addresses | state before verification |
|---|---:|---|---|
| `c-question`: universal exact divisibility | yes | only the prime-2 part for a proposition-defined nearly-simple family with derived subgroup (L_4(3)) | partial only; universal row unanswered |
| `c-solvable-context` | no | nothing | excluded context |
| `c-general-bound-context` | no | nothing | excluded context |

`active_assignment_answered: pending` at triage; even a complete pass of the
bounded claim must result in `active_assignment_answered: no`.

## Independently reconstructed constraint-and-conclusion matrix

| constraint id | role | source requirement | bounded claim's use | triage result |
|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | every admissible triple | restricts to a proper nearly-simple family and one prime | does not answer universal quantifier |
| `20.115-G-finite` | admissibility | (G) finite | proposition concerns finite nearly-simple groups (H), exact hypotheses still to be checked | pending theorem audit |
| `20.115-chi-complex-irreducible` | admissibility | ordinary irreducible complex (\chi\) | proposition is claimed for (\chi\in\operatorname{Irr}(H)) | pending theorem audit |
| `20.115-x-in-G` | admissibility | (x\in G), exact order | proposition uses an element (h\in H) and a quotient order | pending theorem audit |
| `20.115-character-value-nonzero` | admissibility | exact (\chi(x)\ne0) | claimed hypothesis in Condition (1.1) / Proposition 3.2 | pending theorem audit |
| `20.115-order-degree-divisibility` | target conclusion | full (o(x)\chi(1)\mid |G|) | only its (2)-part for the restricted family | universal conclusion unproved |

## Target versus witness

- Source target: all finite triples ((G,\chi,x)) satisfying the nonzero-value
  hypothesis.
- Active assignment: the same universal target.
- Computed witness: CTblLib's ordinary table named `L4(3)`, GAP's degree-40
  permutation group returned by `PSL(4,3)`, and the six ordinary (2)-blocks at
  (p=2); the theorem bridge then concerns a restricted class of finite groups
  (H).
- Witness equals universal target: **false** as a scope statement. Identity of the
  explicit permutation model with centerless (\operatorname{PSL}_4(3)), and
  applicability of the theorem to the claimed family, remain to be certified.

## Subclaims

1. The cited PDF artifact is the stated Malle--Navarro--Tiep paper and Theorem 3.5
   has exactly the claimed defect-group/nonvanishing equivalence with no omitted
   hypotheses.
2. Proposition 3.2 has exactly the claimed hypotheses and conclusion; all notation
   from Conjecture 2.3, Condition (1.1), ((\ddagger)), and
   ((\ddagger^\star)) is used correctly.
3. The ordinary table/model is precisely centerless (L=\operatorname{PSL}_4(3)).
4. There are exactly six ordinary (2)-blocks, with the asserted 29-row partition
   and defects (7,2,0,0,0,0).
5. The principal block has an explicit Sylow (2)-defect group of order (128)
   and exponent (8).
6. The displayed order-4 element represents table class `4a`; row 16 belongs to
   block 2 and is nonzero there; Theorem 3.5 and the defect order then prove that
   its cyclic subgroup is a block-2 defect group, rather than merely a subgroup of
   the correct order.
7. The four defect-zero blocks have trivial defect groups.
8. All 29 character (2)-defects and all six block-exponent inequalities are exact.
9. Centerlessness converts the required starred block condition correctly, and
   Proposition 3.2 yields precisely the claimed (2)-local conclusion—no more.

## Tool probe

- GAP `4.12.1`; CTblLib `1.3.7` loaded successfully.
- Python `3.12.3`.
- Poppler `pdftotext` `24.02.0`; `pdftoppm` is installed.
- `sage` and `magma` were not found.
- The cited local paper artifact exists, has 28 pages, and its SHA-256 agrees with
  the claimant's recorded digest
  `a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`.

## Methods inventory

| subclaim | method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| 1, 2, 9 | line-by-line reading of the fixed local PDF, including all referenced definitions | exact theorem statement and logical applicability | truth of unstated library data or universal Kourovka claim |
| 3 | inspect the documented GAP constructor and independently check defining projective action/model invariants | equality of the finite model used with (\operatorname{PSL}_4(3)), if the construction chain is established | equality from order/name alone |
| 4, 7, 8 | fresh bounded GAP script, structurally different from the claimant's script, plus hand (2)-adic arithmetic | independent reconstruction of finite CTblLib records and inequalities | mathematical provenance/correctness of CTblLib data absent a source certificate |
| 5 | explicit reconstruction from printed generators and exhaustive enumeration of the 128 elements | subgroup order and exact exponent; principal-block identification then gives a defect group | the universal character-order conjecture |
| 6 | explicit permutation checks plus the independently audited Theorem 3.5 | cyclic subgroup is conjugate/equal to a block-2 defect group under the theorem hypotheses | that correct order alone identifies a defect group |

## Hard limits and gate

The routed `CLAIM` does not link a `claim-checks/<claim-id>.json`; indeed
`Agents/Kourovka/problems/20.115/claim-checks/` is absent. The Validator protocol
requires that file and a clean state-check as a completeness gate before deep
verification. No theorem certification or nontrivial GAP reconstruction will start
until Lead supplies or routes a clean check. If supplied, the proposed independent
GAP work is a genuinely lightweight exact rerun expected well below 60 seconds;
otherwise a manifest/lease will be requested before computation.

## Recommendation

`send back / partial only` until the missing claim-check gate is repaired. After
that repair, proceed with full verification of the bounded lemma only; preserve
`active_assignment_answered: no` regardless of whether it passes.
