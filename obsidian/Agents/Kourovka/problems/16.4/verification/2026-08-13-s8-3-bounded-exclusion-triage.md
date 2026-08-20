---
title: "Verification triage — Kourovka 16.4 — S8(3) bounded exclusion"
problem: "16.4"
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/conjugacy-classes, project/kourovka, status/conjectured]
---

# Verification triage — Kourovka 16.4 — S8(3) bounded exclusion

## Claim

For the specific finite simple group represented by CTblLib's ordinary character table `S8(3)`, no ordered pair of nonidentity conjugacy classes has a product that is a single conjugacy class.

## Target vs witness

- Kourovka target: an arbitrary finite nonabelian simple group (G), with two nontrivial conjugacy classes (C,D), asking whether (CD) can be one conjugacy class (source PDF, page 95).
- Bounded claim target: the finite simple group (PSp_8(3)), commonly denoted `S8(3)` in CTblLib.
- Computational witness: the ordinary character table returned by GAP/CTblLib as `CharacterTable("S8(3)")`.
- `witness = target` status: to be checked independently from table metadata and CTblLib documentation/identifiers. Even if established for (PSp_8(3)), this witness is not the universal Kourovka target; the requested verdict can cover only this group-specific exclusion.

## Sub-claims

1. The source problem is the stated conjugacy-class-product question.
2. CTblLib's `S8(3)` table is the ordinary character table of the intended simple group (PSp_8(3)), not a cover or automorphism group.
3. The table has 278 classes and indices 2 through 278 are exactly all nonidentity classes.
4. If class products (K_iK_j=K_k), then for every irreducible character \(\chi\), \(\chi(g_i)\chi(g_j)=\chi(1)\chi(g_k)\).
5. An independently written exhaustive computation checks all (277^2=76{,}729) ordered nonidentity input pairs and every possible output class, with exact cyclotomic equality.
6. No pair/output triple satisfies the necessary character identity; therefore no singleton class product exists in this table.
7. The computation is not circular: the table and its class/character data pre-exist the claimed exclusion and are not constructed from it.

## Tools available

- GAP 4.12.1, with CTblLib version to be recorded by the verification run.
- Python 3.12.3.
- `pdftotext` 24.02.0.
- Sage: unavailable.
- Magma: unavailable.

## Methods inventory

| Sub-claim | Method | What a pass proves | What a pass does not prove |
|---|---|---|---|
| 1 | Extract page 95 from configured source PDF | Exact problem statement used | Any mathematical answer |
| 2 | Query independent CTblLib table metadata and identifiers | Witness identification to the extent documented by CTblLib | A family theorem for all (PSp_8(q)) |
| 3 | Independently inspect identity class position, class count, class lengths | Exact indexing and pair count | Correctness of the whole table library |
| 4 | Hand derivation from constancy of irreducible characters on a singleton product | Necessity of the column identity | Sufficiency of the identity |
| 5–6 | New GAP script with a loop structure independent of the claimant's script; exact comparison over every output column | Exhaustive bounded exclusion in the loaded table if no compatible triple exists | Kourovka 16.4 universally; any group outside this table |
| 7 | Provenance inspection | The check is not true by construction from the desired exclusion | Independent reconstruction of the character table from a presentation |

## Hard limits

The installed tooling cannot independently reconstruct this enormous group and its full character table from generators within the verification budget. The result therefore relies on CTblLib's published table data and identification. Sage and Magma are unavailable, but neither is required for a second independently written GAP enumeration. A `replicated` verdict can apply only to the named table-specific finite computation.

## Recommendation

Full verification of the bounded `S8(3)` table exclusion, with at most `status/replicated`; no upgrade of the universal Kourovka problem.
