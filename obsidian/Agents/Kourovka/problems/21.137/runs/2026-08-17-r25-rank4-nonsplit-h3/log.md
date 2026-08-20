---
title: "Kourovka 21.137 counterexample lane — rank-four nonsplit H3 lift gate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
outcome: RUNNING
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

# RANK4-NONSPLIT-H3-AUTOMORPHISM-TRIPLE

## 2026-08-17T20:22:35Z — active work start

- Cumulative active ledger starts at 564 minutes; this increment is capped at 60 active minutes (through 624).
- Exact source scope: odd prime `p>2`; finite same-`p` group `G`; exponent exactly `p^2`; `P={g^p:g in G}` is the literal actual set, not the generated subgroup; the literal set itself is assumed a subgroup; ask whether it is abelian. The `p=2`, exponent-eight sibling is excluded.
- Bounded lane: `p=3`, `K=3_+^(1+4) x C3^2`, quotient `H_3(3)`, reviewed canonical symplectic outer action. This lane cannot answer the universal scope by itself.
- Read the common and problem-agent protocols, roster, revision-2 scope record, synthesis, the sole unread Lead decision, and the two directly relevant reviewed verification notes. No unreviewed historical work was opened.

## Source and staleness gate

- Rendered and visually inspected Notebook No. 21 PDF page 184. Correct active transcription: “For `p != 2`, if the `p`-th powers in a `p`-group of exponent `p^2` form a subgroup, must that subgroup be abelian?”
- `source_transcription_checked: yes`; `active_scope_checked: yes`.
- The page lists 21.137 unstarred, with no attached editor or later comment. The synthesis likewise records no editor comment.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run` (canonical scope has `blind_run.enabled: true` and `open_web: false`).
- Constraint reconciliation: all seven revision-2 rows match the rendered statement. This bounded `p=3` lane passes the odd-prime/object-class interpretation but does not have universal coverage and has no candidate group; `active_assignment_answered: no`.

## Frozen first-gate strategy

The first gate is exactly the finite automorphism-lift system frozen in
`scratch/lift_manifest.md`. No factor set, presentation, group enumeration,
alternative kernel, alternative quotient, or alternative label pair is opened
before this gate passes.

## 2026-08-17T20:35:27Z — compute threshold checkpoint

- Exact cheap domain count: 81 center actions, 6,561 ordered pairs, 2,673 retained Heisenberg center triples.
- The first complete checker run unexpectedly reached the 60-second heavy-job threshold before producing output. It was interrupted immediately (exit 130); no result from it is evidence.
- Sent Lead a lease request for exactly one frozen run (`timeout 180s`, one core, under 100 MB, five-minute lease). No rerun occurs without approval. Hand inspection and single-row cheap checks may continue while waiting.

## 2026-08-17T20:37:54Z — first gate passes

- A single natural center-action row already gives a complete feasible lift, so the full-domain lease request is withdrawn.
- Frozen labels: `qX=f2`, `qY=e2`; both are invariant under their own outer actions and `omega(qX,qY)=2 != 0`.
- One 56-equation/36-variable system has coefficient rank 17 and augmented rank 17. The linked solution has zero residual in every row and gives exact inner labels for all six Heisenberg relators.
- This is only an automorphism-lift checkpoint, not a factor system or group. Per Lead's decision, proceed to freeze one complete factor-system/extension gate; do not vary the lift row.

## 2026-08-17T20:47:10Z — factor gate fails; active work stop

- Froze the single zero-central six-relator presentation in `scratch/extension_manifest.md`; no action, shear, central correction, kernel, quotient, or label variation followed.
- Exact class-10 3-quotient: order `3^8`, class 4, descending ranks `[4,1,2,1]`. The quotient by the kernel image still has order 27, but the kernel image has order `3^5`, is abelian, and kills both `c` and `s`.
- Any desired extension would have order `3^10` and class at most 9, hence factor through this universal class-10 3-quotient. Therefore the required `K` cannot embed in this frozen presentation.
- An exploratory exact fp-to-pc conversion hit its explicit 30-second cap; it is non-evidence. The clean reproducible checker stops after the exact class-10 quotient certificate.
- Outcome: `STRATEGY_EXHAUSTED` for this row only. No intended finite group exists, so exponent-nine and complete literal-cube-set gates are not reached. Universal scope remains open and `active_assignment_answered: no`.
- Charge 25 integer active minutes, cumulative `564--589`; return 35 unused minutes. State: `awaiting_lead`, not parked.

## 2026-08-17T20:49:49Z — control correction and lease release

- Polling after the factor report revealed Lead's newer `20:37:09Z` compute decision. It approved exactly one SHA-pinned full checker and explicitly forbade patches and factor work.
- Current checker SHA is `68c8edab...1ba1`, not approved `bafb9bfa...c2828`; the approved command was not run. Released compute slot 1 unused.
- The factor diagnostic occurred after that unread control message and is therefore preserved only as control-incident audit material, excluded from evidence. It does not establish strategy exhaustion.
- Superseded the factor report, sent a blocker requesting an exact next decision, and left the grant message `status: blocked` in this inbox. Current outcome: `BLOCKER`, `awaiting_lead`; `active_assignment_answered: no`.
- Final accounting includes the control audit and correction writing: stop at `20:52:20Z`, charge 30 integer minutes total, cumulative `564--594`, return 30 unused.
