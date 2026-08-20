---
title: "Scope audit — Kourovka 21.53"
problem: "21.53"
audit_type: source-fidelity
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 1
source_pdf_page: 172
source_transcription_checked: yes
result: FAIL_WITH_EXACT_CORRECTIONS
audited_record_modified: no
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/graph-automorphisms
  - project/kourovka
  - status/draft
---

# Scope audit — Kourovka 21.53

## Result

**FAIL_WITH_EXACT_CORRECTIONS.** The universal group-theoretic target, inherited
object class, prime convention, and displayed equality are faithfully captured.
Revision 1 nevertheless leaves one source case outside its atomic definition of
`Aut_t(Gamma)`, misclassifies an actual counterexample as partial progress, and
conjoins the proof and counterexample certificate branches. The scope should not
be activated until the three replacements under **Exact corrections required**
are made.

This is only a source-fidelity audit. No proposed solution, literature result, or
solution-bearing Problem 21.52 research was read or assessed. The canonical scope,
board, and roster were not edited.

## Source and inherited notation

I visually inspected rendered local PDF page 172. Problem 21.53 says “In the
notation of 21.52,” so the following data and definitions are inherited in full:

- `L` is a finite non-abelian simple group.
- `D` is one conjugacy class of involutions in `L`.
- `Gamma` is the complete simple graph with vertex set `D`; an edge is an
  unordered pair of distinct vertices.
- Two edges `(a,b)` and `(c,d)` have the same colour exactly when the element
  orders `|ab|` and `|cd|` in `L` are equal.
- `Aut(Gamma)` is the group of permutations `tau in S_D` preserving that colour
  on every edge.

Problem 21.53 then defines `Aut_t(Gamma)` by the one-way conditional

`|ab| = t  =>  (a,b) ~ (a^tau,b^tau)`

for `tau in S_D`. By the inherited equivalence relation, this is exactly
`|a^tau b^tau|=t` whenever `|ab|=t`. Because `tau` permutes the finite edge set,
this setwise preservation condition does define the stabilizer of the `t`-edge
set. Crucially, the definition is still meaningful when there is no edge of
product order `t`: the condition is then vacuous and
`Aut_t(Gamma)=S_D`.

The displayed source identity

`Aut(Gamma) = intersection_t Aut_t(Gamma)`

means intersection over all product-order labels. It is equivalent to intersecting
only over labels that actually occur, because every nonoccurring label contributes
the harmless factor `S_D`. That equivalence does **not** permit the definition of
`Aut_t` itself to be restricted to occurring colours: the conclusion explicitly
uses `Aut_2` and `Aut_p`, and the source does not assert that either label occurs
on an edge of every admissible `(L,D)`.

## Quantifiers, names, and primes

The letter `G` in the final question is a rename of the inherited group `L`, not a
second independently chosen group. That is the only typed reading: `Gamma`, `D`,
and their product orders otherwise remain attached to `L`, while `p` would be
attached to an unrelated `G`. The phrase “for every finite simple group `G`”
therefore remains subject to the inherited non-abelian-simple condition from
21.52. It does not add cyclic simple groups, for which the inherited involution
class/two-prime setup can fail to exist.

The initially arbitrary class `D` is also universally quantified. Thus the target
is for every admissible pair `(L,D)`, not merely for one selected class per group.

The set `{2,p}` consists of the two least **distinct prime divisors of the group
order** `|L|`. Hence `p` is the least prime divisor of `|L|` greater than `2`.
These are not the two least occurring product-order colours of `Gamma`, and the
source contains no occurrence hypothesis for either edge label.

## Clause-and-constraint audit

| Source item | Canonical treatment | Audit |
|---|---|---|
| Inherited `L` | finite nonabelian simple `L` | exact |
| Inherited `D` | one conjugacy class, all members of order exactly 2 | exact |
| Inherited graph | complete simple graph on `D`, unordered distinct pairs | exact |
| Inherited colouring | edge colours agree iff the element product orders agree | exact |
| Universal quantifier | every admissible pair `(L,D)` | exact |
| Source `G` versus inherited `L` | treated as a rename | exact and necessary |
| `Aut_t(Gamma)` conditional | preservation of every `t`-edge by a permutation of `D` | incomplete domain: the constraint says only “for each product-order colour” and omits the nonoccurring-label/vacuous case |
| Full intersection | intersection over occurring product-order colours | exact, once nonoccurring `Aut_t=S_D` is recorded |
| “two minimal prime divisors” | `2` and the next distinct prime divisor `p` of `|L|` | exact |
| Target conclusion | `Aut(Gamma)=Aut_2(Gamma) intersection Aut_p(Gamma)` | exact |

The role assignments are otherwise sound: all object, definition, prime, and
quantifier rows are admissibility rows, while the displayed equality is the sole
target-conclusion row.

## Exclusions

All four listed exclusions preserve the source scope:

- Problem 21.52 asks the separate induced-group-automorphism question and is not a
  clause of 21.53.
- `D` is one conjugacy class, not a union of involution classes.
- `p` is fixed by the two least prime divisors of `|L|`, not chosen arbitrarily.
- A bounded catalogue cannot establish the universal equality.

The constraints also correctly prevent two further common misreadings: `G` is not
independent of `L`, and `{2,p}` is not chosen from the occurring edge-colour
orders. It would be useful, but is not necessary for source fidelity, to repeat
the latter warning in `excluded_scopes`.

## Success criteria and certificates

The proof criterion is faithful: it requires the equality for every admissible
`(L,D)`. The counterexample criterion is also logically sufficient: one
admissible pair and one permutation in `Aut_2 intersect Aut_p` that changes an
occurring edge colour disproves the universal equality.

Two later fields are not sound as written:

1. The second `partial_progress` item asks for a complete finite determination
   “distinguishing the two-colour group from the full colour group.” If
   “distinguishing” means the groups differ, this is already a counterexample and
   answers the universal question negatively; it must not be reported as partial.
2. The single `certificate` sentence first requires a reconstructible finite
   `(L,D)`, full matrices, and exact groups, and then appends “either ... or a
   line-by-line universal proof.” Grammatically this requires the finite-witness
   package even for a universal proof. Conversely, it does not explicitly demand
   the finite witness's simplicity, single-class condition, correct prime, or
   exhaustive preservation checks. Proof and counterexample certificates must be
   separate alternatives.

## Exact corrections required

1. Replace the statement of constraint `21.53-Aut-t-definition` with:

   > For every positive integer `t` (in particular `t=2`, `t=p`, and every
   > occurring product-order value), `Aut_t(Gamma)` consists exactly of the
   > permutations `tau` of `D` satisfying `|a^tau b^tau|=t` whenever `a` and `b`
   > are distinct elements of `D` with `|ab|=t`. If no edge has product order
   > `t`, then `Aut_t(Gamma)=S_D` vacuously.

   Make the same domain/vacuity explicit in source clause `c-aut-t`. Keep
   `21.53-full-colour-group-definition` as the equivalent intersection over
   occurring colours.

2. Replace `success_criteria.partial_progress[1]` with:

   > A complete finite determination for a nontrivial pair `(L,D)` for which
   > `Aut(Gamma)=Aut_2(Gamma) intersection Aut_p(Gamma)`, together with a
   > reproducible structural explanation. Any finite determination proving strict
   > inequality is a counterexample, not partial progress.

3. Replace `success_criteria.certificate` with:

   > For a universal proof: a line-by-line proof covering every finite
   > nonabelian simple `L` and every involution class `D`, including cases in which
   > a `2`- or `p`-edge set is empty. For a counterexample: a reconstructible
   > finite nonabelian simple `L`; a verified single conjugacy class `D` of
   > involutions; the complete product-order matrix on unordered distinct pairs;
   > verification that `p` is the second-smallest distinct prime divisor of
   > `|L|`; an explicit `tau in S_D`; exhaustive checks that `tau` preserves every
   > edge of product order `2` and `p` (vacuously if the relevant edge set is
   > empty); and one explicit edge whose product order `tau` changes. Exact full
   > permutation groups may be supplied but are not required when those membership
   > and separation checks are exhaustive.

No target, quantifier, object-class, prime-selection, conclusion, or exclusion
correction is required.

## Evidence boundary

The rendered page was inspected directly after rendering PDF page 172. Plain-text
extraction was used only to locate the statement and was checked against the page
image, including the subscripts on `Aut_t`, `Aut_2`, and `Aut_p`, the subscript on
the intersection, the superscript action notation, and the braces around
`{2,p}`.
