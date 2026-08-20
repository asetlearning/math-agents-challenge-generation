---
title: "Verification triage — Kourovka 20.115 — claimed partial stale match"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
claim: "Malle--Navarro--Tiep, arXiv:2605.04513v1, states the exact universal divisibility question in active scope but proves it only partially, so it is PARTIAL_STALE rather than STALE_MATCH."
claimant: Problem-20.115
target_statement: "For every finite group G, every complex irreducible character chi of G, and every x in G, chi(x) nonzero implies o(x)chi(1) divides |G|."
excluded_scopes:
  - modular or Brauer characters
  - reducible characters
  - rows with chi(x)=0
  - the already-known solvable-group case
  - the weaker fourth-power bound
  - bounded character-table screens as universal proofs
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

# Triage

## Claim restated

The submitted bibliographic claim is that arXiv:2605.04513v1 addresses exactly the active ordinary-character implication for all finite groups but does not prove that implication for all finite groups.

## Locked scope

- `scope_id`: `20.115/nonzero-character-order-divisibility`
- `assignment_revision`: 1
- Active target: for every finite group `G`, every ordinary irreducible complex character `chi` of `G`, and every `x in G`, if the exact value `chi(x)` is nonzero, then `o(x)` divides `|G|/chi(1)` (equivalently, `o(x)chi(1)` divides `|G|`).
- Excluded: the contextual solvable theorem, the weaker fourth-power bound, modular/reducible characters, zero values, and finite table screens treated as universal proofs.

The rendered source PDF was visually inspected at PDF/printed page 161. The source has one question clause and two contextual known-result clauses.

## Clause matrix

| source clause | active? | claimed paper coverage | status before inspection |
|---|---:|---|---|
| Universal nonzero ordinary irreducible-character divisibility question | yes | exact conjecture; allegedly partial proof only | pending |
| Assertion known for solvable `G` | no | not relevant to closing active target | pending |
| `(o(x)chi(1))^4` divides `|G|^5` for arbitrary `G` | no | not relevant to closing active target | pending |

`active_assignment_answered: pending`.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | submitted literature result must show | status |
|---|---|---|---|---|
| 20.115-forall-G-chi-x | admissibility | universal quantification over all admissible triples | the paper's conjecture has these quantifiers; its theorem would have to cover all of them for STALE_MATCH | pending |
| 20.115-G-finite | admissibility | `G` finite | exact object class | pending |
| 20.115-chi-complex-irreducible | admissibility | ordinary complex irreducible `chi in Irr(G)` | exact character class | pending |
| 20.115-x-in-G | admissibility | `x in G`, with exact order `o(x)` | exact element and order | pending |
| 20.115-character-value-nonzero | admissibility | exact `chi(x) != 0` | exact hypothesis | pending |
| 20.115-order-degree-divisibility | target conclusion | `o(x)chi(1)` divides `|G|` | universal proof for STALE_MATCH; a restricted theorem is only partial | pending |

## Target versus witness

- Source target: the universal implication above.
- Witness under review: the exact statements proved in arXiv:2605.04513v1 and the current-edition status of Notebook problem 20.115.
- `witness = target`: pending primary-source inspection. Merely restating the target as a conjecture does not answer it.

## Subclaims

1. The paper's conjecture has exactly the source quantifiers, object class, nonzero-value hypothesis, and divisibility conclusion.
2. The paper does not prove that conjecture universally.
3. The paper identifies its proved families/reduction and the remaining nearly-simple cases precisely enough to delimit the partial result.
4. The July 2026 current Notebook edition does not carry an answer/later comment that independently closes 20.115.
5. Therefore the correct staleness label is PARTIAL_STALE, not STALE_MATCH.

## Tool probe

- GAP executable: `/usr/bin/gap`; version query still to be recorded (not needed for this literature-only verdict).
- Python 3.12.3.
- Sage and Magma absent.
- Poppler `pdftotext` and `pdfinfo` 24.02.0; `pdftoppm` available for rendered-page inspection.

## Methods inventory

| subclaim | method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| exact source clause | rendered source-PDF inspection | source transcription and all active rows | truth of the conjecture |
| exact paper statement | inspect arXiv v1 PDF/TeX line by line | what v1 actually conjectures and proves | later-version or unpublished progress |
| remaining cases | inspect theorem/reduction statements and authors' explicit remarks | the paper's own residual bottleneck | that those cases remain open beyond all later literature |
| July 2026 status | inspect official current Notebook edition and metadata | whether that edition marks 20.115 answered | exhaustive worldwide literature status |
| classification | clause-by-clause comparison | PARTIAL_STALE versus STALE_MATCH under the protocol | a mathematical solution by this crew |

## Hard limits and recommendation

No mathematical computation is needed. Full bibliographic verification is authorised, using the source PDF, arXiv v1 primary text, and the official current Notebook edition. If the official July 2026 edition cannot be obtained or inspected, the edition-status subclaim must remain unknown and be reported explicitly rather than inferred from search snippets.

Recommendation: proceed with full primary-source verification.
