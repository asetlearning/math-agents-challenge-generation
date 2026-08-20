---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/draft
---

# Working log — Kourovka 21.137

## Active-time ledger

- 2026-08-14T13:10:14Z — work started; cumulative active minutes: 0.

## Staleness check

### 2026-08-14T13:11:09Z

`source_transcription_checked: yes`

I visually inspected rendered PDF page 184 (not merely `pdftotext`) and compared every clause and formula. Corrected transcription:

> **21.137.** If the \(p\)-th powers in a finite \(p\)-group form a subgroup, must that subgroup be powerful? That is, for \(p\ne 2\), if the \(p\)-th powers in a \(p\)-group of exponent \(p^2\) form a subgroup, must that subgroup be abelian? For a \(2\)-group of exponent \(8\), if the squares form a subgroup, must that subgroup be abelian? — L. Wilson

The item is unstarred and has no editor or later comment attached on the rendered page. The configured corpus is explicitly the older issue-20/2022 corpus and contains no record for 21.137, so its JSON flags `answered`, `has_editor_comment`, and `has_later_comment` are unavailable; the issue-21 source page itself supplies the relevant negative visual check.

Searches performed:

- exact web search `"Kourovka" "21.137"`;
- exact web search `"Problem 21.137" "Kourovka Notebook"`;
- web search `L. Wilson "p-th powers" subgroup powerful finite p-group`;
- arXiv-oriented search `arXiv "p-th powers" "form a subgroup" powerful group`;
- web search `"If the p-th powers" "must that subgroup be abelian"`;
- checked the configured issue-21 PDF, where 21.137 is still printed without an answer marker or comment;
- checked James Williams, *Quasi-powerful p-groups*, arXiv:1912.08906: nearby regular-power-structure results, not a solution of 21.137.

The exact-number searches were not negative: they found a public Lean file created 2026-04-14, Elias Judin / Aristotle (Harmonic), **“Kourovka Notebook Problem 21.137 Lean proof”**, https://gist.github.com/eliasjudin/3e74b54004d82cb86651a14ecf082463 . It explicitly constructs
\[
W=(D_8\times D_8)\rtimes_{\mathrm{swap}} C_2=D_8\wr C_2,
\]
where its notation is `DihedralGroup 4` for the order-eight dihedral group. The file states and formalizes: `Fintype.card WreathD4 = 128`; every element has eighth power one and some element has nontrivial fourth power; for every `a b`, there is `c` with `a^2*b^2=c^2`; and two explicit square witnesses do not commute. Thus it purports to be an exact counterexample to the even-prime clause, rather than a bounded search or finite quotient of another target.

Because this is an externally existing solution/counterexample found at the mandatory staleness gate, I stop mathematical work and report `DEAD (already solved)`, pending Validator's independent confirmation of the match and artifact.

## Outcome

### 2026-08-14T13:11:09Z — REPORT: DEAD (already solved)

- Citation/artifact: Elias Judin / Aristotle (Harmonic), `21_137.lean`, “Kourovka Notebook Problem 21.137 Lean proof,” created 2026-04-14, https://gist.github.com/eliasjudin/3e74b54004d82cb86651a14ecf082463 .
- Reason: the artifact supplies an explicit order-128 exponent-8 counterexample to the second clause.
- Certification status: not independently certified here; sent to Validator under the immediate stale-result protocol.
- 2026-08-14T13:11:09Z — work stopped; cumulative active minutes: 1.
