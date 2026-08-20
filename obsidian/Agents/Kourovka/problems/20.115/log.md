---
title: "Problem 20.115 counterexample reconnaissance log"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: counterexample
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-tables
  - project/kourovka
  - status/draft
---

# Problem 20.115 counterexample reconnaissance

## Active-time ledger

- Work start: `2026-08-17T18:47:52Z`; cumulative active time: 0 minutes.
- Work stop: `2026-08-17T18:50:10Z`; cumulative active time: 3 minutes (rounded up). Stop reason: mandatory staleness gate found a plausible exact-subject partial result; Lead's assignment requires `PARTIAL_STALE` and no mathematics after such a match.

## Staleness check — 2026-08-17

Outcome: `PARTIAL_STALE`.

`source_transcription_checked: yes`

`active_scope_checked: yes`

`active_assignment_answered: no`

### Source and corpus checks

- Resolved the configured source through `_meta/agents/Kourovka/paths.env`; the PDF was readable.
- Ran `pdftotext -f 161 -l 161 -layout "$KOUROVKA_PDF" -` for navigation, rendered page 161 at 200 dpi with `pdftoppm`, and visually inspected the rendered page.
- Corrected source transcription, with line breaks normalized: “Let \(\chi\) be a complex irreducible character of a finite group \(G\). If \(\chi(x)\ne0\) for some \(x\in G\), must the order \(o(x)\) of \(x\) divide \(|G|/\chi(1)\)? This is known to be true if \(G\) is solvable, and it is known that \((o(x)\chi(1))^4\) divides \(|G|^5\) for arbitrary \(G\).” Proposer: T. Wilde.
- The rendered source is unstarred and has no editor answer or later comment.
- Corpus record command: `rg -n '20\\.115' 'Research/Group theory/Open problems/Kourovka/corpus/kourovka-20-corpus.jsonl'`. Observed flags: `answered: false`, `has_editor_comment: false`, `has_later_comment: false`. The corpus says page 162 while the displayed and configured PDF page is 161; the rendered page controls.

### Current literature searches (performed before mathematics)

Searched the open web and arXiv on 2026-08-17 for:

- `"Kourovka 20.115"`;
- `"Problem 20.115" Kourovka character`;
- `T. Wilde irreducible character nonzero order divides character degree group`;
- `arXiv irreducible character nonzero "o(x)" "chi(1)" finite group`;
- `Kourovka Notebook 21 20.115 character Wilde` and current-edition variants;
- the exact paper/conjecture titles found by those searches.

The searches found the original conjecture paper, Tom Wilde, “Orders of elements and zeros and heights of characters in a finite group,” arXiv:math/0604337 (submitted 14 April 2006), whose abstract states the exact conjecture and only partial bounds: <https://arxiv.org/abs/math/0604337>.

More importantly, they found a post-source-date paper on the exact active question: Gunter Malle, Gabriel Navarro, and Pham Huu Tiep, “Zeros of characters and orders of elements in finite groups,” arXiv:2605.04513v1 (submitted 6 May 2026): <https://arxiv.org/abs/2605.04513>, full HTML <https://arxiv.org/html/2605.04513v1>. Its Conjecture A is verbatim the active universal implication. Theorem B reduces it to Condition (1.1) for nearly simple groups, and Theorems C and D establish substantial families/prime cases. The abstract explicitly says that a few cases remain and require unavailable character-extension information. Therefore it is a strong partial result, not a solution or counterexample to the universal active scope.

Checked the editors' current July 2026 No. 21 PDF, <https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/07/21tkt.pdf>, and its July update-only PDF, <https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/07/21upd.pdf>. Problem 20.115 remains unstarred and unchanged on displayed page 161; the update-only file has no `20.115` entry. This independently agrees that the active universal question was not marked answered by that edition/update.

No other search result found a paper claiming a universal proof or an admissible counterexample. This negative statement is limited to the named searches above.

### Source/literature clause matrix

| source clause | equivalent formulation | active scope? | Wilde 2006 | Malle–Navarro–Tiep 2026 | July 2026 No. 21 | staleness decision |
|---|---|---:|---|---|---|---|
| `c-question`: if \(\chi(x)\ne0\), must \(o(x)\mid |G|/\chi(1)\)? | For every finite \(G\), ordinary \(\chi\in\operatorname{Irr}(G)\), and \(x\in G\), exact nonvanishing implies the integer divisibility \(o(x)\chi(1)\mid |G|\). | yes | States it as a conjecture; does not settle it. | Conjecture A is the exact clause. Theorem B gives a conditional reduction to nearly simple groups; Theorems C/D prove many families and prime-local cases, but the abstract and introduction retain remaining cases. | Lists the question unstarred and without comment. | `PARTIAL_STALE`; exact-subject substantial progress, but no full answer. |
| `c-solvable-context`: assertion holds for solvable \(G\). | Universal implication restricted to finite solvable groups. | no; context only | Source for the known solvable case (the 2026 paper invokes Wilde Corollary 4.2 in its reduction). | Uses the already-known solvable case; does not enlarge this row into the full active scope. | Repeats it as known context. | Already-known/excluded contextual row, not an answer to active scope. |
| `c-general-bound-context`: \((o(x)\chi(1))^4\mid |G|^5\). | A weaker universal divisibility bound, not the requested first-power divisibility. | no; context only | Gives partial universal bounds, including the abstract's statement \(o(x)\mid (|G|/\chi(1))^2\); it does not claim the active first-power conclusion. | Pursues the stronger active conjecture via reductions and family cases rather than claiming a universal first-power theorem. | Repeats the fourth/fifth-power bound as known context. | Contextual partial knowledge only; excluded from active success criterion. |

### Admissibility reconciliation

| constraint id | source requirement | treatment in the 2026 paper | result for stale-match gate |
|---|---|---|---|
| `20.115-forall-G-chi-x` | Universal implication over all admissible triples. | Conjecture A has the same universal quantification, but the paper proves only a reduction and many cases. | incomplete |
| `20.115-G-finite` | \(G\) finite. | Explicit in Conjecture A. | match |
| `20.115-chi-complex-irreducible` | Ordinary complex irreducible \(\chi\). | Written \(\chi\in\operatorname{Irr}(G)\) in ordinary character theory. | match |
| `20.115-x-in-G` | \(x\in G\) with exact order \(o(x)\). | Written \(g\in G\) and exact element order \(o(g)\). | match |
| `20.115-character-value-nonzero` | Exact \(\chi(x)\ne0\). | Exact \(\chi(g)\ne0\). | match |
| `20.115-order-degree-divisibility` | \(o(x)\chi(1)\mid |G|\). | Exact same conclusion in Conjecture A, but it is not established in remaining cases. | not established universally |

The canonical scope and source agree. The 2026 result matches the object class, hypothesis, and desired conclusion exactly, but leaves the universal quantifier and conclusion incomplete. Hence `STALE_MATCH` is forbidden and `PARTIAL_STALE` is required.

### Gate consequence

Per the Lead decision, stopped before freezing or running any character-table screen. No GAP/CTblLib sweep, floating-point test, Brauer-character test, or solvable-only inference was performed. No heavy-compute lease was requested because the staleness gate terminated the reconnaissance first.

## Ledger correction — 2026-08-17T18:51:53Z

The preliminary stop entry above was recorded before the required clause matrix and bus reports were finished. Counting that writing time, the final work stop is `2026-08-17T18:51:53Z`; cumulative active time is 5 minutes (elapsed 4 minutes 1 second, rounded up). This correction supersedes only the earlier 3-minute stop total; the staleness outcome is unchanged.
