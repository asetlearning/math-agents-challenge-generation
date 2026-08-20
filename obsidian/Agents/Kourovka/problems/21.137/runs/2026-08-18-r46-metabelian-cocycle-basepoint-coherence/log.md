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
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
cycle: 34
strategy: METABELIAN-COCYCLE-BASEPOINT-COHERENCE
---

# Cycle 34 log — metabelian cocycle/basepoint coherence

## Active-time ledger

- Start: `2026-08-18T11:39:14Z`; official cumulative active minutes at start: `962`; newly elapsed active minutes: `0`.
- Hard cap: 45 newly elapsed active minutes; wall-clock safety stop `2026-08-18T12:32:53Z`.

## Source and scope gate

- Rendered source PDF page 184 visually inspected. Correct active clause: for odd `p`, if the actual set of `p`th powers in a finite `p`-group of exponent exactly `p^2` is a subgroup, must it be abelian?
- `source_transcription_checked: yes`; `active_scope_checked: yes`.
- The general powerfulness question and the `p=2`, exponent-eight square clause are excluded.
- Canonical rows reconciled: universal quantification; odd prime; finite `p`-group; exponent exactly `p^2`; literal actual value set (not generated subgroup); subgroup hypothesis; abelianity conclusion. No mismatch found.
- Discovery-blind restriction applies. `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.

## Strategy portfolio

1. **Assigned structured/theoretical route (primary):** choose a normalized section of the complete metabelian extension `A=G' -> G -> Q=G/A`, derive the normalized associative 2-cocycle, the basepoint and norm image of every `p`th-power fibre, all section-change laws, and the simultaneous closure condition over every quotient class.
2. **Smallest-support gate:** specialize the exact equations only after they are global, to the subgroup of `Q` required by two noncommuting power values and every `p`-torsion shift of their roots; identify the least `A`-submodule on which the commutator amplitude could survive.
3. **Certificate plan:** a positive result must give a section-independent identity forcing the exact commutation defect to zero for every pair of fibres. A surviving amplitude counts only if the same action and cocycle define one associative finite exponent-`p^2` group and its complete literal power set passes closure; a local module array is only a method test.

