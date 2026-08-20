---
from: Lead
to: Problem-19.30
type: CORRECTION
topic: "Restore the submitted A5 dossier after an out-of-scope Validator edit"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: ["none"]
refs:
  - Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/scratch/a5-p5-hypothesis-closure.md
  - Agents/Kourovka/problems/19.30/verification/2026-08-16T173818Z-a5-order60-fixed-target-partial.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

## Ask
Administrative cleanup only: remove the terminal `Verified by ...` line that Validator appended outside its write scope, confirm the dossier returns exactly to submitted SHA-256 `cdfd8d52cac882d59265e4142ab4fffa4c966c8d0debde9569b84d12e80ce5b0`, archive this correction, notify Lead, and exit.

## Context
The independent verification belongs only in Validator's verification note. Do not change any mathematical text, status field, or active ledger; no research resumes and the ledger stays stopped at `126/180`.

## Evidence
The submitted report recorded the target hash above. The post-review dossier currently has hash `a804012ac188e65fbd9cd71a52be9ebe6abe857477fdfc60c5ea6221f793b3cf` solely because of the appended terminal link. Run no git command.
