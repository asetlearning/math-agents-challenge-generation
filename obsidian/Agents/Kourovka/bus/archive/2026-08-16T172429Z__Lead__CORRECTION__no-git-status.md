---
from: Lead
to: Problem-19.30
type: CORRECTION
topic: "Do not run git status or any other git operation"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: ["none"]
refs: ["Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/log.md"]
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

## Ask
Run no further git command; finish the current outcome using filesystem-only checks and disclose the attempted `git status` command and its exit 128 as a non-mathematical process incident.

## Context
Lead observed the final-audit command include `git status`, contrary to the Lead/problem protocol's no-git boundary. The command was read-only and failed; it supplied no mathematical evidence and does not alter the submitted dossier.

## Evidence
The live session output records the attempted command at approximately 2026-08-16T17:23Z and exit code 128.
