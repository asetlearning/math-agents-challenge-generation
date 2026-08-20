---
title: "Problem 17.76 — cycle 1 log"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/commutators
  - project/kourovka
  - status/draft
problem_id: "17.76"
cycle: 1
---

# Problem 17.76 — working log

## 2026-08-12T03:15:46Z — work start

- Assignment: cycle 1, 180 active-minute budget.
- Cumulative active minutes: 0.
- Inbox poll: no messages present.

## Staleness check — 2026-08-12T03:17Z

### Source and transcription gate

- Resolved the configured source PDF through `_meta/agents/Kourovka/paths.env`; it was readable.
- The corpus record is in `Research/Group theory/Open problems/Kourovka/corpus/kourovka-20-corpus.jsonl` and records printed page 109, `answered: false`, `has_editor_comment: false`, and `has_later_comment: false`.
- The problem is on physical PDF page 110 (whose printed page header is also 110), rather than physical page 109. I rendered physical page 110 to `Agents/Kourovka/problems/17.76/scratch/source-physical-110.png` and visually inspected the rendered page, including the star, inequality, and answer note.
- Corrected transcription: “Does there exist a finite group \(G\), with \(|G|>2\), such that there is exactly one element in \(G\) which is not a commutator?”
- `source_transcription_checked: yes`

The current configured PDF marks 17.76 with a star and prints an affirmative answer: such groups exist, with infinitely many examples. It cites S. V. Skresanov, *On finite groups with exactly one noncommutator*, preprint (2025), arXiv:2509.17587, and O. Hatem–D. Siniora, *A Group with Exactly One Noncommutator*, *International Journal of Group Theory* 15(3) (2026), 161–167. Thus the corpus flags are stale relative to the configured PDF.

### Literature searches

Searched the web for:

- `"Kourovka" "17.76" commutator`;
- `"Problem 17.76" "Kourovka Notebook"`;
- `D. MacHale exactly one element not a commutator`;
- `site:arxiv.org unique non-commutator finite group Skresanov`.

The searches found the exact-title arXiv records:

1. S. V. Skresanov, *On finite groups with exactly one noncommutator*, arXiv:2509.17587 (submitted 22 September 2025), https://arxiv.org/abs/2509.17587. Its abstract explicitly identifies MacHale's question and says it answers it affirmatively with an infinite series; the smallest group in that construction has order 16,609,443,840.
2. O. Hatem and D. Siniora, *A Group with Exactly One Noncommutator*, arXiv:2511.00541 (submitted 1 November 2025), https://arxiv.org/abs/2511.00541. Its abstract explicitly identifies Problem 17.76 and reports two nonisomorphic examples of order 368,640, claimed minimal.

No contrary result appeared in these searches. The current configured Kourovka PDF itself contains the answered annotation and both references.

### Gate outcome

`REPORT: DEAD (already solved)`. This is an exact bibliographic match to the same existence question, not merely a related commutator result. Per the immediate stale-result exception, no new mathematics was attempted.

## 2026-08-12T03:17:57Z — work stop

- Cumulative active minutes: 2.
- Outcome: DEAD (already solved); sent for Lead disposition and Validator match confirmation.
