---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
cycle: 17
direction: proof
strategy: PSL2Q-DIRECT-CHARACTER-FAMILY
---

# Cycle 17 log — direct `PSL(2,q)` character family

## 2026-08-18T10:06:50Z — work start

Detailed cumulative time at entry: `06:54:54`. New active-time allowance: at most
`00:45:00`; research stop no later than detailed cumulative `07:39:54`.

Read in order the common protocol, problem-agent protocol, canonical scope record,
current proof roster, and the sole current inbox decision. The scope record marks
this as a discovery-blind run. I did not inspect the historical synthesis, log,
findings, verification notes, transcripts, archived messages, or the preceding
unreviewed proof lanes. The run directory was empty at entry.

## Source and staleness gate

Resolved the configured source PDF through `_meta/agents/Kourovka/paths.env`.
Rendered and visually inspected source-PDF page 161 (printed page 161), not merely
the `pdftotext` output.

Corrected source transcription:

> **20.115.** Let \(\chi\) be a complex irreducible character of a finite group
> \(G\). If \(\chi(x)\ne0\) for some \(x\in G\), must the order \(o(x)\) of \(x\)
> divide \(|G|/\chi(1)\)? This is known to be true if \(G\) is solvable, and it is
> known that \((o(x)\chi(1))^4\) divides \(|G|^5\) for arbitrary \(G\).

`source_transcription_checked: yes`

Corpus record
`Research/Group theory/Open problems/Kourovka/corpus/kourovka-20-corpus.jsonl:1205`
has `answered:false`, `has_editor_comment:false`, and `has_later_comment:false`.
Because `blind_run.enabled:true` and
`blind_run.solution_bearing_history_allowed:false`, no web or solution-bearing
local-history search was made:
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.

Clause matrix:

| source clause | equivalent formulation | active? | literature status in this run |
|---|---|---:|---|
| If \(\chi(x)\ne0\), must \(o(x)\mid |G|/\chi(1)\)? | \(o(x)\chi(1)\mid |G|\) (using the standard fact \(\chi(1)\mid |G|\)) | yes | external check deferred |
| Assertion known for solvable \(G\) | contextual established subfamily | no | not used |
| \((o(x)\chi(1))^4\mid |G|^5\) for arbitrary \(G\) | weaker contextual bound | no | not used |

`active_scope_checked: yes`

Admissibility reconciliation (all six canonical rows agree with the rendered
source):

| constraint id | use in this assigned family audit |
|---|---|
| `20.115-forall-G-chi-x` | The notebook target is universal; the assigned result can cover only triples with \(G=\operatorname{PSL}_2(q)\), and must be labelled a family partial. |
| `20.115-G-finite` | \(\operatorname{PSL}_2(q)\) is finite. |
| `20.115-chi-complex-irreducible` | Inventory only ordinary complex irreducible characters. |
| `20.115-x-in-G` | Inventory every conjugacy type and use exact order in the quotient group. |
| `20.115-character-value-nonzero` | Check formulas and exceptional cancellations before invoking divisibility. |
| `20.115-order-degree-divisibility` | Establish \(o(x)\chi(1)\mid |G|\) for every surviving pair. |

No scope mismatch found.

## Strategy portfolio

1. **Theoretical/direct-table mode (selected):** reconstruct the generic ordinary
   character tables for even and odd \(q\), organized by identity, unipotent,
   split torus, and nonsplit torus. Reduce each nonzero cell to elementary order
   divisibility. Expected to certify an infinite simple family if the exceptional
   half-degree rows are handled correctly.
2. **Structured mode:** derive principal/discrete series via induction from the
   Borel and the two tori, so that zeros and root-of-unity sums have a conceptual
   source. Use only if it shortens rather than obscures the exact table audit.
3. **Small-case mode:** hand-isolate the exceptional simple parameters excluded by
   generic parametrization (especially \(q=4,5,9\)); a finite check here patches a
   generic theorem but never substitutes for one.
4. **Certificate plan:** state a complete parameterized table theorem, exact class
   orders, degree multiplicities, parameter identifications, all possible zero
   conditions, and a primewise divisibility table. Validator can reconstruct from
   the same formulas and test the small exceptions independently.

Kill criterion: if the exact exceptional-character values or parameter exclusions
cannot be reconstructed reliably within the cap, stop with the precise missing
table theorem; do not assert completeness from memory.

## 2026-08-18T10:10:52Z — generic table reconstruction

Located the installed exact generic ordinary-table records rather than using a
catalogue sample.  Commands read (without modifying) the `SL2even`, `PSL2odd`, and
`PSL2even` records from CTblLib's `data/ctgeneri.tbl.gz`, chiefly source lines
468--556, 560--681, and 685--811 of the decompressed file.  Environment: GAP 4.12.1,
CTblLib 1.3.7; compressed-data SHA-256
`c73d3506b64277e5ebdca2dbfd22c0de6e7bf6a5afcc5b6d86d8d8a2cddc2313`.

Reconstructed all class parameter ranges, exact orders, character parameter
ranges, degrees, and values in `findings.md`.  The decisive simplification is that
for each congruence case, every table cell which is not identically zero belongs
to a class type whose torus order supplies exactly the degree's missing factor.
Thus one can audit a superset of the actual support and accidental cyclotomic
cancellation is harmless.

No heavy computation was used.  A light endpoint sanity check (not a premise of
the family proof) specialized only `q=4,5,7,8,9` and enumerated exact ordinary
values.  Observed output:

```text
4 size=60 degrees=[ 1, 3, 3, 4, 5 ] orders=[ 1, 2, 3, 5, 5 ] nz=20 bad=[ ]
5 size=60 degrees=[ 1, 4, 5, 3, 3 ] orders=[ 1, 5, 5, 2, 3 ] nz=20 bad=[ ]
7 size=168 degrees=[ 1, 6, 7, 8, 3, 3 ] orders=[ 1, 7, 7, 3, 4, 2 ] nz=28 bad=[ ]
8 size=504 degrees=[ 1, 7, 7, 7, 7, 8, 9, 9, 9 ] orders=[ 1, 2, 7, 7, 7, 9, 9, 3, 9 ] nz=56 bad=[ ]
9 size=360 degrees=[ 1, 8, 8, 9, 10, 5, 5 ] orders=[ 1, 3, 3, 4, 2, 5, 5 ] nz=36 bad=[ ]
```

Here `bad` means exact nonzero cells failing the requested integer divisibility.
This finite output checks transcription at the boundary only; it is not offered as
family evidence.

## 2026-08-18T10:15:47Z — research stop and outcome

Charged active time this run: `00:08:57`.  Detailed cumulative active time is now
`07:03:51` (entry `06:54:54` plus `00:08:57`).  Research stopped well before the
45-minute cap; subsequent activity is packaging only.

Outcome: `PARTIAL_RESULT`.

Candidate result under independent review: for every prime power \(q\) for which
\(\operatorname{PSL}_2(q)\) is nonabelian simple, every ordinary irreducible
\(\chi\) and every \(x\) with \(\chi(x)\ne0\) satisfy
\(o(x)\chi(1)\mid |\operatorname{PSL}_2(q)|\).  `findings.md` contains the complete
three-case generic character tables, exact class orders, root-sum cancellation
criterion, exceptional Gauss-period values, primewise integer quotient tables, and
small simple endpoints.

Scope status: `active_assignment_answered: no`, because the canonical target is all
finite groups and this is only one infinite simple family.  No prior unreviewed
Clifford/block lemma or bounded table screen is a premise.

Continuation recommendation: have Validator independently reconstruct the three
generic tables—especially the half-degree rows and the central factor two—and then
check the displayed quotient tables.  If that passes, preserve this as a reviewed
exact simple-family exclusion and ask MathExpert whether it feeds a classified
almost-simple reduction.  Do not spend more solver time sampling additional
\(q\)-values.
