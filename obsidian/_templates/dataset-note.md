---
title: <dataset name — what the records are and the property they share>
dataset_id: ds-<instance>-<slug>-<YYYYMMDD>   # = filename without .md; never reused
date: <YYYY-MM-DD>                            # date the files were produced
domain: <group-theory | ai | cs | methodology>
project: <project tag>                        # producing project; others go in used_by
instance: <e.g. B(2,5)>
kind: <trivial-words | presentations | relator-set | instances | corpus | ...>
format: <e.g. "text, one word per line, letters a A b B (A = a⁻¹)">
records: <count>
files:
  - path: "<repo>:data/<file>"               # repo:path form, never a machine path
    sha256: <hex>
    bytes: <n>
    role: <data | sources | certificates | labels>
storage: <git (<vault repo> data/) | code repo | rjob put-data sha256 | external URL>
obtain: "<how to get the files if not in git; omit when git-tracked>"
derived_from:
  - "`[[<parent dataset note>]]`"            # registered parent, or for an unregistered parent:
  - "<repo>:data/<file> sha256 <hex> — origin: <what produced it, or 'unknown'>"
produced_by: "<repo>@<sha>:<script> (+ run dir / rjob job id)"
property_claimed: "<the property every record has, and in which object>"
vetting:
  - check: <what was checked>
    tool: <tool + version / build>
    scope: "<which object, e.g. free B(2,5) (proof) | B₀(2,5) quotient (consistency only) | syntactic>"
    result: <e.g. 820/820 pass>
    date: <YYYY-MM-DD>
    by: <agent/handle>
stats: {min_len: <n>, max_len: <n>, mean_len: <x>}
used_by: ["`[[<experiment or data note>]]`"]
supersedes: ""                                # dataset_id this replaces, if any
superseded_by: ""
author: <handle>
status: <draft | validated | superseded | rejected>
tags: [agent/<who>, user/<handle>, domain/<...>, topic/<one+>, project/<...>, status/<...>, dataset]
---

# <dataset name>

> [!info] Plain English
> <Two or three sentences: what these records are, why they exist, what they may and may not be used for.>

## What it is
<Records, format, one example record, what the companion files contain (e.g. a sources CSV mapping each record to parent records).>

## Derivation
<Numbered pipeline from the parent data to these files: every filter, transformation and dedup rule, with the exact function/tool and version. Enough to regenerate the files byte-for-byte.>

## Vetting
| Check | Tool | Object / scope | Result |
|---|---|---|---|
| <check> | <tool + version> | <free group / quotient / syntactic> | <n/n> |

<State plainly which claims are **proved** and which are only **consistent** (e.g. checked in a finite quotient). A property nobody checked is listed under Caveats, not here.>

## Caveats
- <What the vetting does not establish; known biases; records kept that a stricter filter would drop.>

## How to load
```python
# <minimal loader; verify sha256 first>
```

## Used by
- `[[<experiment / data note>]]` — <how>

## Related material
- `[[datasets-convention]]`
- `[[<project progress note>]]`
- `[[<producing experiment or verification note>]]`
