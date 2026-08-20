---
title: "Kourovka <ID> — data and scripts"
domain: group-theory
project: kourovka
problem_id: "<ID>"
date: <YYYY-MM-DD>
author: maumayma
tags: [agent/problem, user/maumayma, domain/group-theory, topic/kourovka, project/kourovka, status/draft]
---

# Kourovka <ID> — data and scripts

The index for this directory. **The actual scripts live here as files** — not as
descriptions, not as fenced blocks in a note. Someone must be able to re-run them.

## Environment

| | |
|---|---|
| GAP version | <from `gap --version`> |
| Packages | <SmallGrp x.y, ANUPQ x.y, GRAPE x.y — the versions you actually confirmed> |
| Other tools | <Sage, Python, …> |
| Machine | <rough spec, if runtime matters> |
| Date verified | <when you ran `which gap` and checked the packages> |

Record what you **verified**, not what the setup doc claims. Last campaign the crew
designed around `SmallGroups(2187)` and ANUPQ before discovering neither was
installed.

## Scripts

| File | What it does | Runtime | Output |
|---|---|---|---|
| `scan-order-512.g` | Exhaustive `SmallGroup` scan, orders 1–512, tests <predicate> | 3m12s | `scan-order-512.out` |

Each script should be runnable as-is:

```bash
gap -q -b scan-order-512.g > scan-order-512.out 2>&1
```

## Transcripts

| File | Produced by | Contains |
|---|---|---|
| `scan-order-512.out` | `scan-order-512.g` | full output, 0 hits |

Keep transcripts **verbatim**. A result reported without the transcript that produced
it is not usable, and [[_common-kourovka]] §11 forbids reporting an output you did not
observe.

## Constructed objects

Any candidate group/object built during the work, in a form that can be reloaded.

| Object | File | Construction | Order |
|---|---|---|---|
| | | | |

## Provenance notes

<Anything a re-runner needs: random seeds, why a bound was chosen, where an
enumeration was truncated and why, known nondeterminism.>
