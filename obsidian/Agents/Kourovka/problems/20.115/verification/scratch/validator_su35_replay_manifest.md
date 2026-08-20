---
title: "Frozen manifest — independent Validator replay of 3.U3(5)"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, topic/compute-lease, project/kourovka, status/draft]
---

# Frozen replay manifest

## Boundary

The replay opens exactly `CharacterTable("3.U3(5)")`. It performs no catalogue
enumeration and opens no neighbouring table. It checks the installed table's
identity/invariants, ordinary irreducible semantics, all class and degree data,
all 1,600 exact cyclotomic values, and exact integer divisibility. It then compares
every coordinate against the claimant's frozen transcript.

## Frozen inputs

- Independent GAP script:
  `Agents/Kourovka/problems/20.115/verification/scratch/validator_su35_scan.g`
  SHA-256 `89f8a811b5025295b6efeb9bd934fe7a0b0ea2ece6f6227fcb6ea09303c2ff5c`.
- Independent comparison/audit script:
  `Agents/Kourovka/problems/20.115/verification/scratch/validator_su35_compare.py`
  SHA-256 `b5d90db106d394cf30f076634253a2936316c57821e8aaeab760d1d47bcc86ef`.
- Claimant script expected SHA-256:
  `47b67f1ee3a23f7e954c5dbbe7a35d2d10671e5743ba1e80a2ddf9c8effffeaa`.
- Claimant raw output expected SHA-256:
  `313d8c9fcabc541ccf1ca88cf724241a4f1f1404a940e7b4caa70ce1b84bcfce`.

Neither independent output existed when this manifest was frozen.

## Exact authorized commands requested

Run once, in this order:

```bash
timeout 30s gap -q -A -r Agents/Kourovka/problems/20.115/verification/scratch/validator_su35_scan.g
timeout 30s python3 Agents/Kourovka/problems/20.115/verification/scratch/validator_su35_compare.py
```

Expected total CPU time: under 15 seconds. Expected peak RAM: under 256 MiB.
Requested lease duration: five minutes. The Python command is included in the
lease because the assignment requires a lease for any checker replay.

## Output targets

- `Agents/Kourovka/problems/20.115/verification/scratch/validator_su35_scan.out`
- `Agents/Kourovka/problems/20.115/verification/scratch/validator_su35_compare.json`

No patch or rerun is authorized by this manifest. A failure stops the replay and
is reported to Lead before any change.

## What a pass means

A pass independently replicates the exact stored-table computation and permits at
most `status/replicated` for this one-table bounded `PARTIAL_RESULT`. It does not
prove the universal target, any paper family, or any neighbouring group/table;
`active_assignment_answered` remains `no`.
