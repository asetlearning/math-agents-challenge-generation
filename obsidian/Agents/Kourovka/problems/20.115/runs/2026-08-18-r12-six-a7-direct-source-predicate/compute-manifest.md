---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-tables, project/kourovka, status/draft]
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
frozen_utc: 2026-08-18T04:54:01Z
---

# Frozen compute manifest — exact `6.A7` audit

- Script: `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.g`
- Script SHA-256: `d1621a51b80d33391102122db9ae912b9e9976a4454f13de223921b8159827d2`
- Exact command:
  `/usr/bin/time -v timeout 45s gap -q Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.g > Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.out 2>&1`
- Expected runtime: under 10 seconds; hard wall timeout 45 seconds.
- Expected resources: one CPU, under 250 MB RAM.
- Requested lease duration: 5 minutes.
- Output paths were absent when frozen.
- The checker loads only `CharacterTable("6.A7")` and its certified quotient table
  `CharacterTable("A7")`; it does not enumerate any table identifier.
- Static installed identity cross-checks:
  - CTblLib 1.3.7 package metadata SHA-256
    `10b1c0ee07ac98fa7fd9f852cee256db91b109e1d50aeed210ae6317117f75f3`.
  - AtlasRep `atlasprm.json` SHA-256
    `99fba4783d0a82c6cb53473d2d5634438ba464758f7a01e76b29abbf88375bbf`;
    its installed records name `6.A7`, ATLAS alias `6A7`, and order `15120`.
  - CTblLib examples `doc2/chap3.txt` SHA-256
    `e667dffafb7283b96bc16607a60ad6a2e99fedceab3ddd690e326cf37fd37641`;
    the installed manual explicitly lists `6.A7` among central extensions `M.G`
    of simple ATLAS groups and reconstructs it as the common central extension of
    `A7`, `2.A7`, and `3.A7`.

