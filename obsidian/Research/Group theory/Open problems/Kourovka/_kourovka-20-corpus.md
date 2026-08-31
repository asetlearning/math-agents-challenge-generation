---
title: "Kourovka Notebook No. 20 (2022) — open-problem corpus"
type: corpus-index
source: "Unsolved Problems in Group Theory: The Kourovka Notebook, No. 20"
source_editors: ["E. I. Khukhro", "V. D. Mazurov"]
source_year: 2022
source_arxiv: "arXiv:1401.0300v23 [math.GR], 7 Feb 2022"
source_pdf: "$KOUROVKA_PDF (see _meta/agents/Kourovka/paths.env)"
extracted: 2026-08-11
extractor: "_meta/scripts/kourovka-extract.py"
problem_count: 1213
answered_flagged: 65
open_count: 1148
author: maumayma
tags:
  - agent/lead
  - user/maumayma
  - domain/group-theory
  - topic/kourovka
  - topic/open-problems
  - project/kourovka
  - status/reference
  - reference
status: reference
domain: group-theory
---

# Kourovka Notebook No. 20 — open-problem corpus

Machine-readable extraction of **every problem in the main (unsolved) part** of the
Kourovka Notebook No. 20. This is the raw material the Kourovka crew selects from.
It is a **reference artefact**, not a research note: no interpretation, no ranking.

## Provenance

| Field | Value |
|---|---|
| Source PDF | `$KOUROVKA_PDF` — resolved from `_meta/agents/Kourovka/paths.env` (269 pages, 1.9 MB) |
| Source identity | arXiv:1401.0300v23 [math.GR], 7 Feb 2022 |
| Editors | E. I. Khukhro, V. D. Mazurov |
| Extraction tool | `pdftotext -layout` (poppler) → `_meta/scripts/kourovka-extract.py` |
| Pages parsed | printed pp. 5–163 (PDF page index 4–162), i.e. the **main part only** |
| Explicitly excluded | *Archive of Solved Problems* (pp. 164–253), *Index of Names* (pp. 254–269) |
| Extraction date | 2026-08-11 |

## Counts

| | |
|---|---|
| Problems parsed | **1213** |
| Flagged answered (leading `∗` + editors' answer note) | 65 |
| **Genuinely open** | **1148** |
| Problems with no machine-recovered proposer | 215 (name is present in the statement text, just not split out) |

Per issue:

| Issue | Year | Problems | Answered (`∗`) |
|---|---|---|---|
| 1 | 1965 | 20 | 0 |
| 2 | 1966 | 22 | 0 |
| 3 | 1969 | 18 | 1 |
| 4 | 1973 | 28 | 0 |
| 5 | 1976 | 24 | 0 |
| 6 | 1978 | 27 | 0 |
| 7 | 1980 | 28 | 1 |
| 8 | 1982 | 50 | 1 |
| 9 | 1984 | 51 | 2 |
| 10 | 1986 | 55 | 0 |
| 11 | 1990 | 90 | 1 |
| 12 | 1992 | 65 | 6 |
| 13 | 1995 | 46 | 1 |
| 14 | 1999 | 80 | 5 |
| 15 | 2002 | 85 | 4 |
| 16 | 2006 | 80 | 9 |
| 17 | 2010 | 106 | 7 |
| 18 | 2014 | 104 | 5 |
| 19 | 2018 | 111 | 22 |
| 20 | 2022 | 123 | 0 |

**Validation anchor:** the preface states the 20th issue "contains 123 new problems".
The extractor independently recovers exactly 123 for issue 20. That is the primary
signal that the section-boundary logic is correct.

## Files

- `corpus/kourovka-20-corpus.jsonl` — **canonical machine-readable form**, one JSON
  object per problem, sorted by issue then number.
- `corpus/kourovka-issue-NN-YYYY.md` × 20 — the same content as readable Obsidian
  notes, one per issue, each problem an `## N.M` heading. Use these for grep and for
  reading; use the JSONL for programmatic selection.

### JSONL schema

| Key | Type | Meaning |
|---|---|---|
| `id` | string | Problem number, e.g. `"11.48"` |
| `issue` | int | Issue number 1–20 |
| `year` | int | Year of that issue |
| `page` | int \| null | Printed page number in the PDF |
| `answered` | bool | `true` ⇒ carries an editors' `∗` answer note; **not open** |
| `has_editor_comment` | bool | Contains an explicit "Editors' comment" |
| `has_later_comment` | bool | Contains a "Comment of YYYY" — partial progress exists |
| `statement` | string | Problem text, paragraphs joined, attribution stripped where recoverable |
| `proposers` | string[] | Proposing author(s); empty if not machine-separable |
| `chars` | int | Length of `statement` |

## Known limitations — read before trusting a statement

> [!warning] This is a plain-text extraction of typeset mathematics
> 1. **Notation is mangled.** `hx, yi` = `⟨x, y⟩`; `⩽`, `π`, `∩`, subscripts and
>    superscripts are flattened; displayed formulas lose their layout;
>    `7→` = `↦`. **Never quote a statement from this corpus in a write-up.** Re-read
>    the problem in the source PDF (`$KOUROVKA_PDF`) at the recorded page first.
> 2. **`answered: true` is a floor, not a ceiling.** It catches the editors' `∗`
>    convention inside this PDF only. A problem can have been solved in the
>    literature since Feb 2022 and still read as open here. **Every candidate
>    problem must get a fresh literature check** (arXiv, MathSciNet, the current
>    Kourovka edition — No. 21 exists) before any work starts.
> 3. **Multi-part problems are one record.** Problems with parts a)/b)/c) are stored
>    as a single entry; parts can have independent status.
> 4. **215 proposers unrecovered.** In those the name is still inside `statement`,
>    usually because an editors' comment follows the attribution line.
> 5. **Cross-references to "Archive, N.M"** point into the excluded solved section;
>    resolve them against the PDF.

## Reproducing

```bash
source "_meta/agents/Kourovka/paths.env"
python3 "_meta/scripts/kourovka-extract.py" \
  "$KOUROVKA_PDF" \
  "Research/Group theory/Open problems/Kourovka/corpus"
```

Requires `pdftotext` (`brew install poppler`). The script prints per-issue counts to
stderr; compare them against the table above — any drift means the parse changed.

## Related material in vault

- [[kourovka-2022]] — paper note for the notebook itself
- [[kourovka-11.48-kostrikin-1990]] — the worked example of a single-problem
  synthesis note; the model every Kourovka problem note should imitate
- [[kourovka-crew-setup]] — how to stand up the agent crew that works this corpus
- [[lead-kourovka]] — the Lead agent that selects from this corpus
- [[group-theory-overview]] — domain hub
