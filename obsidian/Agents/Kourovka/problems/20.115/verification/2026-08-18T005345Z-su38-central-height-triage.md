---
title: "Triage — Kourovka 20.115 — SU3(8) central-height obstruction"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
claimant: Problem-20.115-Proof
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

# Triage — Kourovka 20.115 — `SU3(8)` central-height obstruction

## Claim restated

For the ordinary character table of the perfect triple cover
`L=SU_3(8)=3.U3(8)` at `p=3`, the proposed auxiliary central-height
threshold holds for 76 of the 82 ordinary irreducible rows and fails exactly
for principal-block rows 35--40: these six rows have degree `189`, height
`3`, and `3^3=27>|P/Z|/exp(P/Z)=81/9=9`.

The submission explicitly claims only an obstruction to the proposed generic
central-height bridge. It does not claim to answer Kourovka 20.115 or to refute
Proposition 3.2.

## Scope lock

- `scope_id`: `20.115/nonzero-character-order-divisibility`
- `assignment_revision`: `1`
- Active target: for every finite group `G`, ordinary complex irreducible
  character `chi`, and `x in G`, prove or disprove
  `chi(x) != 0 => o(x)chi(1) divides |G|`.
- Excluded: Brauer characters, zero character values, reducible characters,
  the solvable-only result, the weaker fourth-power bound, and any bounded
  table screen presented as a universal proof.

The source PDF, page 161, independently renders the same question and the two
contextual statements. The canonical scope agrees with it.

## Clause matrix

| source clause | in active scope | submitted result | status |
|---|---:|---|---|
| Universal nonzero-value order divisibility question | yes | Tests an auxiliary block-height sufficient condition for one group and one prime | unanswered |
| Known solvable-group case | no | Not addressed | excluded context |
| Known fourth-power general bound | no | Not addressed | excluded context |

`active_assignment_answered: pending` at triage; the expected final value is
`no` because no source-target triple `(G,chi,x)` is asserted and the universal
conclusion is neither proved nor violated.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | submitted candidate/proof use | evidence status | result |
|---|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | All admissible triples | One group, one prime, auxiliary block rows only | explicit submission limitation | fail for active target |
| `20.115-G-finite` | admissibility | `G` finite | `SU_3(8)` is finite | order formula/table order to check | pass for bounded claim |
| `20.115-chi-complex-irreducible` | admissibility | Ordinary complex irreducible `chi` | Ordinary CTblLib rows | table identity/ordinary-table semantics to check | pending |
| `20.115-x-in-G` | admissibility | Exact element `x in G` and exact `o(x)` | Matrix elements are used only to model defect groups | no Kourovka witness asserted | not used toward target |
| `20.115-character-value-nonzero` | admissibility | Exact `chi(x) != 0` | Support values only enter a defect-support argument | no Kourovka witness asserted | not used toward target |
| `20.115-order-degree-divisibility` | target conclusion | `o(x)chi(1) | |G|` | Neither proved nor violated | submission says so | unanswered |

## Target versus witness

- Source target: a universal statement about every admissible triple
  `(G,chi,x)`.
- Active assignment: exactly that universal statement, revision 1.
- Computed witness: the ordinary table named `3.U3(8)` together with the
  matrix group `SU(3,8)`, used to test a separate sufficient block-theoretic
  inequality at `p=3`.
- Witness equals target: false as a scope claim. `SU_3(8)` is one admissible
  finite group, but no `(chi,x)` counterexample to the source predicate is
  submitted. The narrower object-identity claim
  `SU_3(8)=3.U3(8)` remains a verification sub-claim.

## Sub-claims

1. The source target, canonical scope, and submitted bounded claim are
   distinguished correctly.
2. `SU(3,8)` is the standard perfect central triple cover denoted
   `3.U3(8)`, with order `16547328`, center `C3`, quotient order `5515776`,
   and the table has 82 ordinary irreducible rows.
3. The ordinary 3-block defects are exactly
   `[5,2,2,2,1,1,1,1,1,1]`, with 37, 9, 9, 9, 3, 3, 3, 3, 3, 3 rows.
4. For the principal defect group `P`, `|P|=243`, `Z<=P`,
   `|P/Z|=81`, and `exp(P/Z)=9`.
5. The claimed quotient exponents for defect-two and defect-one blocks are
   respectively `3` and `1`; the defect-two representative assignment uses
   an additional block-support theorem and is not needed for the principal
   obstruction.
6. Heights derived from degrees and block defects agree with the stored
   ordinary heights.
7. Exactly rows 35--40 lie in the principal block with degree `189`,
   `v_3(189)=3`, and height `3`; their threshold comparison is `27>9`.
8. Every other row passes its block threshold, so the exact count is 76
   passes and six failures.
9. Failure of this auxiliary sufficient condition refutes neither Kourovka
   20.115 nor Proposition 3.2.

## Tool probe

- GAP executable: `/usr/bin/gap`; Debian package version `4.12.1-2build2`.
  It has not been started in this validation because all GAP runs require a
  compute lease.
- Python: `/usr/bin/python3`, version `3.12.3`.
- Sage: not found.
- Magma: not found.
- Submitted artifact hashes independently recomputed and matched:
  checker `1f0610791c3cd7f7671804123cbc42076ea38091316807ac734b85c185f89d3b`;
  output `2e8545a02303a51cb63261f1ead9a52af086aa3b0bd4192de070992e6b2e8768`.
  The output has 294 lines; the checker has 192 lines.

## Methods inventory

| sub-claim | method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| Scope distinction | Source PDF and canonical-row hand audit | The bounded claim does not answer the active assignment | Any mathematics about the auxiliary inequality |
| Table/matrix identity | Standard `SU_3(q)` center/order quotient calculation plus independent GAP identifiers/invariants | The computed matrix group and named cover table agree on the defining cover identity and invariants, subject to the standard naming theorem | That mere equality of order alone identifies groups |
| Blocks, defects, rows, heights | Fresh short GAP checker designed independently from the submitted script | Independent reproduction of installed ordinary table data and all 82 row calculations | Independent correctness of CTblLib's underlying published table |
| Sylow quotient | Fresh matrix-group construction and quotient exponent in GAP; hand order arithmetic | Independent concrete verification for the chosen `SU(3,8)` model | A theorem about all `SU_3(q)` |
| Defect-two/one representatives | Hand audit of orders and containment, plus independent GAP checks if leased | The stated quotient thresholds for the exhibited groups | Assignment of those groups to all nonprincipal blocks without the named support theorem |
| Exact 76/6 split | Independent checker plus a separate text/arithmetical count | The bounded threshold truth value for every installed row | The source divisibility predicate for any row/class pair |
| Logical consequence | Direct implication audit | The generic proposed sufficient bridge fails while Proposition 3.2 and the Kourovka target remain untouched | Any replacement bridge or universal result |

## Hard limits

- No GAP computation may be run without a Lead compute lease. An exact-command
  lease will be requested before deep verification.
- The submitted script may be audited but may not count as the Validator's
  independent implementation; a new bounded checker is required for
  `status/replicated`.
- The three submitted refs contain only a self-report that the claimant had a
  slot-2 lease. No independently named roster or lease record is among the
  permitted clean-context evidence, so lease provenance can presently be
  reported only as claimant-stated, not independently certified.
- Without outside literature or a separately supplied theorem reference, the
  CTblLib publication provenance and the block-support theorem cannot be
  independently literature-certified. The requested no-web boundary will be
  respected.

## Recommendation

Proceed with partial verification after obtaining one bounded GAP lease. Design
a fresh checker that reconstructs the table/block/height rows and matrix Sylow
quotient without re-running the claimant's script. Regardless of its result,
record `active_assignment_answered: no`.
