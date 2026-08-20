---
title: "Scope audit — Kourovka 21.53 — revision 2"
problem: "21.53"
audit_type: source-fidelity
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
source_pdf_page: 172
source_transcription_checked: yes
result: PASS
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

# Scope audit — Kourovka 21.53 — revision 2

## Result

**PASS.** Revision 2 completely and faithfully serializes the statement rendered
on local PDF page 172, including all notation inherited from Problem 21.52. Every
source clause, quantifier, object-class condition, definition, prime convention,
conclusion, exclusion, and success-certificate branch passes independently.

This is a source-fidelity audit only. I did not inspect a proposed solution,
perform a literature search, or read solution-bearing Problem 21.52 research. The
canonical scope, board, and roster were not edited.

## Independent source reconstruction

Problem 21.52 supplies all of the following notation to 21.53:

- `L` is a finite non-abelian simple group.
- `D` is one conjugacy class of involutions in `L`.
- `Gamma` is the complete simple graph whose vertex set is `D`; its edges are
  unordered pairs of distinct elements of `D`.
- The edge equivalence relation is exact equality of element product orders:
  `(a,b) ~ (c,d)` if and only if `|ab|=|cd|` in `L`.
- `Aut(Gamma)` consists of the permutations `tau in S_D` that preserve this
  equivalence class, hence the product-order colour, on every edge.

Problem 21.53 defines `Aut_t(Gamma)` as the permutations `tau in S_D` satisfying

`|ab|=t  =>  (a,b) ~ (a^tau,b^tau)`.

By the inherited equivalence relation, the consequent is exactly
`|a^tau b^tau|=t`. Here `t` is a positive integer because it denotes an element
order. If no edge has product order `t`, the conditional is vacuous and
`Aut_t(Gamma)=S_D`. Revision 2 records all of this explicitly, including distinct
endpoints and the possibly empty `2`- or `p`-edge sets.

The source's displayed intersection can be taken over all positive integers `t`
or, equivalently, only over the product-order values that occur on edges. Every
nonoccurring value contributes `S_D`, so it does not change the intersection.
Thus

`Aut(Gamma) = intersection_t Aut_t(Gamma)`

is exactly the full colour-preserving permutation group.

## Quantifiers and notation conventions

The question's `G` is a rename of the group called `L` in Problem 21.52. Reading
it as an independent group would leave `Gamma` and `D` attached to `L` while the
prime `p` came from an unrelated `G`, so the formula would not be a coherent
continuation of the inherited notation. The inherited condition therefore remains
“finite non-abelian simple,” despite the shorter phrase “finite simple group `G`”
in the final sentence.

The initially arbitrary class `D` is universally quantified. Accordingly, the
assertion ranges over every finite nonabelian simple `L` and every involution
conjugacy class `D` in `L`, exactly as the target statement and quantifier row say.

The phrase “the two minimal prime divisors” means the two numerically least
distinct prime divisors of the group order. With the source notation `{2,p}`, `p`
is the least prime divisor of `|L|` greater than `2`. These primes divide `|L|`;
they are not selected from the occurring edge-product orders, and neither is
assumed by the statement to occur as an edge colour.

## Source-clause audit

| Clause | Canonical serialization | Audit |
|---|---|---|
| `c-inherited-notation` | finite nonabelian simple `L`, one involution class `D`, complete graph, exact product-order colouring | PASS |
| `c-aut-t` | every positive integer `t`, permutations of `D`, preservation of all `t`-edges, and the vacuous empty-colour case | PASS |
| `c-full-intersection` | full colour group is the intersection of the individual colour stabilizers | PASS |
| `c-question` | equality with `Aut_2 intersect Aut_p`, with `2,p` the two least distinct prime divisors of the group order | PASS |

## Constraint audit

| Constraint ID | Required source content | Audit |
|---|---|---|
| `21.53-forall-L-D` | universal quantification over admissible pairs and `G=L` rename | PASS |
| `21.53-L-finite-nonabelian-simple` | inherited group class | PASS |
| `21.53-D-single-involution-class` | exactly one conjugacy class, every member of order 2 | PASS |
| `21.53-Gamma-product-order-colouring` | complete simple graph on `D`; unordered-edge colour is exactly `|ab|` | PASS |
| `21.53-Aut-t-definition` | the source implication for every positive `t`, including vacuity when the `t`-edge set is empty | PASS |
| `21.53-two-minimal-primes` | `2` and the next distinct prime divisor `p` of `|L|` | PASS |
| `21.53-full-colour-group-definition` | preservation of every occurring product-order colour, equivalently the full intersection | PASS |
| `21.53-two-colours-determine-all` | the exact displayed group equality | PASS |

All seven definition, object, parameter, and quantifier rows correctly have role
`admissibility`; the equality row correctly has role `target_conclusion`. All are
required, and every row is linked to the appropriate source clause.

## Exclusions

The exclusions are complete and non-distorting:

- Problem 21.52's induced-automorphism question is separate from the two-colour
  equality in 21.53.
- `D` cannot be replaced by a union of involution classes.
- `p` cannot be replaced by an arbitrary prime divisor.
- Equality on a bounded list of pairs cannot be presented as the universal
  conclusion.

The positive constraints additionally rule out treating `G` as independent of
`L` or treating `{2,p}` as the two least occurring edge colours.

## Success criteria and certificates

The proof criterion has the correct universal burden: every finite nonabelian
simple `L` and every involution class `D`. The counterexample criterion has the
correct existential burden: one admissible pair and a permutation in
`Aut_2(Gamma) intersect Aut_p(Gamma)` that changes an occurring product-order
colour.

Both partial-progress entries are genuinely partial. An exact infinite-family
determination need not cover all finite simple groups, and a structurally explained
positive finite case does not establish the universal equality. Revision 2 also
states correctly that a finite strict inequality is a counterexample, not partial
progress.

The two certificate branches are now logically separate and sufficient:

- A universal proof must be line-by-line and cover every admissible pair,
  including any empty `2`- or `p`-edge set.
- A counterexample certificate verifies the finite nonabelian simple group, the
  single involution class, complete product-order matrix, correct prime `p`, an
  explicit permutation, exhaustive `2`- and `p`-edge preservation, and one edge
  whose product order changes. Exact full permutation groups are helpful but are
  not needed when those membership and separation checks are exhaustive.

These checks establish all admissibility rows before testing failure of the sole
target-conclusion row. No source-fidelity correction remains.

## Evidence boundary

I freshly rendered and visually inspected PDF page 172. Text extraction was used
only for navigation and was checked against the page image, including the
subscripts on `Aut_t`, `Aut_2`, and `Aut_p`, the intersection subscript, the
superscript action notation, and the braces in `{2,p}`. Revision 2 was then audited
row by row without importing the earlier verdict as evidence.
