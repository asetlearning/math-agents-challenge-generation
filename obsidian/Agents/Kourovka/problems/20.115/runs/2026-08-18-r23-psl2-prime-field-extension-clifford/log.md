---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
cycle: 23
strategy: PSL2-PRIME-FIELD-EXTENSION-CLIFFORD
---

## Active-time ledger

- 2026-08-18T11:35:26Z: cycle started; detailed inherited cumulative active time `08:02:07`; new cap 45 active minutes and wall safety stop `2026-08-18T12:35:26Z`.
- 2026-08-18T11:44:33Z: protocol, scope, roster, decision, current inbox, source PDF, and corpus gate completed; approximately `00:09:07` newly elapsed.

## Source and staleness gate

Rendered source PDF page 161 was inspected directly. Correct transcription:

> Let chi be a complex irreducible character of a finite group G. If chi(x) is nonzero for some x in G, must the order o(x) of x divide |G|/chi(1)?

The contextual sentences say that this holds for solvable G and that `(o(x)chi(1))^4` divides `|G|^5` for arbitrary G. The canonical scope has exactly the universal question and correctly excludes both contextual statements. `source_transcription_checked: yes`; `active_scope_checked: yes`.

Corpus flags from `kourovka-20-corpus.jsonl`: `answered: false`, `has_editor_comment: false`, `has_later_comment: false`. This discovery-blind clean context did not perform open-web searching (`blind_run.open_web: false`); the canonical record already records Lead/Validator's current partial-staleness gate. No solution-bearing historical finding was opened.

| source clause | active? | reconciliation |
|---|---:|---|
| universal nonzero ordinary-character divisibility question | yes | exactly canonical target and six constraints |
| known solvable case | no | contextual/excluded |
| weaker fourth-power arbitrary-group bound | no | contextual/excluded |

The six canonical rows were reconciled: universal quantifier; finite G; ordinary complex irreducible chi; exact order of x in G; exact nonzero value; divisibility conclusion. No mismatch found.

## Strategy portfolio

1. **Theoretical/Clifford-Shintani (selected):** parameterize `Irr(PSL(2,q))`, Frobenius orbits, invariant extensions, generalized Shintani norms and outer supports; then make the divisibility audit degree-by-degree.
2. **Structured representation models:** recover outer traces from the projective-line permutation representation, induced Borel models, and the two exceptional Weil constituents. This is the independent check on the dangerous claim that restriction determines outer support.
3. **Small-case catalogue probe:** `q=4,9` could test exceptional isomorphisms, but a negative finite test proves no family theorem, so no computation is being used as evidence here.
4. **Certificate plan:** a symbolic table of all orbit/degree/support/order cases, plus the six-row scope matrix; Validator can reconstruct each row from the rank-one table and cyclic Clifford theory without trusting numerical sampling.

