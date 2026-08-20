---
title: "RANK4-H3-SHEAR-ORBIT-SUPPORT working log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: RANK4-H3-SHEAR-ORBIT-SUPPORT
direction: counterexample
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, topic/power-maps, project/kourovka, status/draft]
---

# Active-time ledger

- `2026-08-17T22:15:39Z` — active work begins at official cumulative minute 648.
- `2026-08-17T22:23:12Z` — interim checkpoint; approximately 8 active minutes,
  cumulative 656.  Required protocol/scope/brief/portfolio/inbox read; frozen
  matrices re-entered.  No computation run and no hard gate reached.

# Scope lock

Odd prime `p>2`; finite same-`p` group; exponent exactly `p^2`; literal actual
set `{g^p:g in G}` itself a subgroup; ask whether that literal set is abelian.
The `p=2`/exponent-eight sibling and generated verbal subgroup substitutes are
excluded.  This run fixes `p=3` only as one bounded counterexample construction
family.  Submitted `6,561/27/135/729` outputs are provisional motivation only
and are not input evidence.

# Reconstruction note

The 56 residual coordinates were rederived directly from the frozen triple law.
Lift-change translations and simultaneous kernel-conjugation formulas were
derived before code was frozen.  Hand centralizer reduction gives exactly
`D_a:f1->f1+a e1` and `U_d:t->t+d c`, hence nine discrete stabilizer pairs.
The exact code and pre-run contract are in `manifest.md`.  No central factor
system or group enumeration is present.

- `2026-08-17T22:30:22Z` — checker and manifest frozen at approximately 15
  active minutes, cumulative 663.  SHA-256
  `8b33f11c261c78aad8f8d5e54d52b9aa7c7fb3a449301c283a49d26d57f4f969`.
  Research stops while the compute lease is pending; waiting time is uncharged.

- `2026-08-17T22:32:14Z` — read the current Lead roster and corrected the run
  directory spelling to its canonical
  `2026-08-17-r27-rank4-shear-orbit-support`.  No checker byte changed; the
  checker hash remains the frozen value.  A superseding lease request carries
  the canonical path.

# Final active-time accounting

Whole-minute charges are conservatively rounded up within each uninterrupted
active block:

| UTC interval | charged minutes | official cumulative | activity |
|---|---:|---:|---|
| `2026-08-17T22:15:39Z--22:30:22Z` | 15 | `648--663` | required reads, independent matrix/equation derivation, gauge/stabilizer derivation, checker and manifest freeze |
| `2026-08-17T22:30:22Z--22:33:47Z` | 4 | `663--667` | canonical run-dir audit/correction, complete role-inbox processing, exact lease-path blocker |
| `2026-08-17T22:33:47Z--22:34:33Z` | 0 | `667` | waiting for corrected lease; uncharged |
| `2026-08-17T22:34:33Z--22:41:34Z` | 8 | `667--675` | single leased run, output inspection, slot release, complete tables, seven-row limitation matrix, Validator/Lead packaging |

Final charge: exactly **27 active minutes**, official cumulative
`648--675`.  Exactly **28 of 55 granted minutes are unused and returned to
Lead**.  Research stops at `2026-08-17T22:41:34Z`; no cohomology or replacement
strategy was opened.

# Final result

The leased checker exited zero and classified all `3^19` shear rows into three
genuine orbits.  Their projected literal-cube supports have sizes `15,15,13`
and each contains `e2,f2` while omitting `e2+f2`, so this frozen family has zero
support-pass orbits.  Outcome: `PARTIAL_RESULT`; universal
`active_assignment_answered:no`.
