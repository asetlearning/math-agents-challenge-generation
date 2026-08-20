---
title: "Kourovka <ID> — methodology, cycle <N>"
domain: group-theory
project: kourovka
problem_id: "<ID>"
cycle: <N>
date: <YYYY-MM-DD>
agent: Problem-<ID>
hours: <n>
author: maumayma
tags: [agent/problem, user/maumayma, domain/group-theory, topic/kourovka, project/kourovka, status/draft]
---

# Kourovka <ID> — methodology, cycle <N>

One of these per cycle. Written by the problem agent at the end of the cycle, in
prose, for a person.

## What I was trying to do

<The goal for this cycle in two or three sentences. If you were resumed with a named
next computation from the previous cycle, say so and say whether you ran it first.>

## The enumeration

Every cycle starts with an exhaustive scan of the smallest admissible cases
([[problem-agent-kourovka]]). Record it here even when it finds nothing —
**especially** when it finds nothing, because the bound is the result.

| Search space | Bound reached | Predicate tested | Hits | Runtime | Script |
|---|---|---|---|---|---|
| `SmallGroup(n,k)`, all k | n ≤ 512 | <the actual target property> | 0 | 3m12s | `data/<script>.g` |

**Was the target predicate actually evaluated?** <yes/no — if no, explain, and know
that this is the exact failure that lost 21.137 last campaign>

## What I tried, in order

### 1. <Approach name>

- **Idea:** <what it was>
- **Why:** <reason to think it would work>
- **What happened:** <the actual outcome, with commands and outputs referenced>
- **Time spent:** <n> minutes
- **Outcome:** <refuted by <what> / inconclusive / led to approach 2>

### 2. <Approach name>

<same shape>

## Candidate objects derived

Every object you constructed *or derived on paper*, and what happened to it.

| Candidate | How derived | Built? | Tested? | Result |
|---|---|---|---|---|
| <e.g. D₈ ≀ C₂, order 128> | <the reasoning> | yes | yes | fails condition (c) |

**An untested derived candidate is a protocol violation** ([[_common-kourovka]] §3.2
rule 3). If a row here says "built: no", explain why, and expect to be sent back.

## Dead ends, and how dead

| Approach | Abandoned after | Why | Provably dead? |
|---|---|---|---|
| <name> | 50 min | <reason> | yes — <the contradiction> / no — could be resumed |

Note: a line abandoned in under 45 minutes needs a *proof* it cannot work, not an
impression.

## Where the budget went

| Activity | Minutes |
|---|---|
| Staleness check | |
| Enumeration | |
| <approach 1> | |
| Write-up | |
| **Total** | |

## Next computation

<The single most concrete thing to run next, with its expected runtime. This is what
Lead reads to decide the extension, and it is the one field that must never be empty.>
