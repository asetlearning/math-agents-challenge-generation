---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
---

# Cycle 19 — `REE2G2-DIRECT-CHARACTER-FAMILY`

## Active-time ledger

- `2026-08-18T10:31:11Z` — START from detailed cumulative active time `07:15:12`; this clean family lane has at most 45 newly active minutes and wall safety stop `2026-08-18T11:31:11Z`.

## 2026-08-18T10:34:17Z — source and scope gate

The source was read from the configured Kourovka PDF, printed page 161, both by
`pdftotext -f 161 -l 161 -layout "$KOUROVKA_PDF" -` and by visual inspection of a
160-dpi rendering. Correct transcription:

> Let \(\chi\) be a complex irreducible character of a finite group \(G\). If
> \(\chi(x)\ne0\) for some \(x\in G\), must the order \(o(x)\) of \(x\) divide
> \(|G|/\chi(1)\)?

The contextual sentences say this is known for solvable `G` and that
`(o(x)chi(1))^4` divides `|G|^5` for arbitrary `G`. They are not part of the active
conclusion. `source_transcription_checked: yes`; `active_scope_checked: yes`.

The issue-20 corpus row has `answered:false`, `has_editor_comment:false`, and
`has_later_comment:false`. This is a discovery-blind lane (`open_web:false` in the
canonical record), so `external_staleness_check:
deferred_to_lead_or_human_for_discovery_blind_run`.

Clause matrix:

| source clause | equivalent formulation | active? | literature status used here |
|---|---|---:|---|
| `chi(x) != 0 => o(x) | |G|/chi(1)` | `o(x)chi(1) | |G|` | yes | no external result imported |
| known for solvable groups | contextual special case | no | not used |
| fourth-power divisibility | weaker universal bound | no | not used |

Admissibility reconciliation: the six canonical rows exactly encode universal
quantification over triples, finite `G`, ordinary irreducible complex `chi`, exact
element order for `x in G`, exact nonzero character value, and the target integer
divisibility. No source/scope mismatch was found.

Assigned subfamily: all nonabelian simple small-Ree groups
`G = ^2G_2(q)`, `q=3^(2m+1)>=27`. This can yield only a family partial, not answer
the universal assignment.

## Strategy portfolio

1. **Theoretical/direct generic-table mode (selected).** Recover the complete
   generic ordinary character and class inventory for `^2G_2(q)`, then prove the
   implication cell-family by cell-family using exact orders and vanishing.
2. **Catalogue/small-case mode.** An installed table at one or more finite `q` could
   detect a counterexample or sanity-check formulas, but no finite sampling proves
   the family and no catalogue expansion is authorized.
3. **Structured mode.** Replace the full value table by Jordan decomposition:
   semisimple centralizers/tori plus the finite set of unipotent supports; this is
   useful only if it rigorously gives a support superset and all exceptional rows.
4. **Certificate plan.** A negative answer needs one exact `q`, row, degree, class,
   order, cyclotomic nonzero value, and failed divisibility. A positive family
   partial needs a parameter-complete family/class crosswalk and primewise
   divisibility for every potentially nonzero cell, suitable for independent
   comparison with a published generic table.

## 2026-08-18T10:48:53Z — generic factor/defect-zero reduction

Set `r=sqrt(3q)`, `s=r/3`, `u=(q-1)/2`, `a=(q+1)/4`,
`b=q-r+1`, and `c=q+r+1`. Then `3,u,a,b,c` are pairwise coprime,
`bc=q^2-q+1`, and `|G|=8q^3uabc`. Reconstructing the complete generic
degree list gives eleven degree families (including three exceptional pairs),
whose multiplicities total `q+8`. Reconstructing the element list gives ten
fixed classes and four semisimple series, also totaling `q+8`.

The decisive observation is that every failure of an element order to divide a
displayed codegree removes a whole coprime prime coordinate from that codegree.
The character then has defect zero for a prime in that coordinate, and the
ordinary defect-zero vanishing theorem forces the cell to be exactly zero.
This gives a complete support-superset proof without evaluating any cyclotomic
sum: all non-forced-zero cells are treated as potentially nonzero and already
satisfy divisibility.

The exact factor tables, class/degree inventories, proof, scope matrix, and
limitations are in `findings.md`. The only classification input requiring fresh
independent comparison is completeness and transcription of the two standard
generic inventories; no earlier family theorem is used.

Reproducible arithmetic command:

```
python3 Agents/Kourovka/problems/20.115/runs/2026-08-18-r19-ree2g2-direct-character-family/scratch/ree_factor_audit.py
```

Observed first and last checks:

```
sum_square_remainder_mod_r2_minus_3q= {}
...
q= 27 character_count= 35 expected= 35
q= 243 character_count= 251 expected= 251
q= 2187 character_count= 2195 expected= 2195
q= 19683 character_count= 19691 expected= 19691
```

The command also prints all 77 degree-family/element-type cells as `SAFE` or
`ZERO_BY_DEFECT:<coordinate>`.

A non-heavy exact GAP sanity check (not a generic premise) used:

```
t:=CharacterTable("R(27)");;
ord:=Size(t);; irr:=Irr(t);; co:=OrdersClassRepresentatives(t);;
```

Observed output after scanning all cells exactly:

```
identifier=R(27) order=10073444472 nchar=35 nclass=35
nonzero=641 bad=0
```

The installed degree list was
`[1,703,741,741,1443,1443,2184,2184,13832 (six times),18278 (four
times),18981,19683,19684 (twelve times),26936 (three times)]`, exactly the
`q=27,r=9` specialization. This finite check is explicitly not used to infer the
infinite family statement.

## 2026-08-18T10:52:43Z — outcome and STOP

Outcome: `PARTIAL_RESULT`. The candidate theorem covers every simple
`^2G_2(q)`, `q>=27`, by a complete factor/defect-zero support audit, conditional
only on fresh independent verification of the explicitly displayed standard
generic degree and class inventories. `active_assignment_answered: no`; the
universal all-finite-groups scope remains open. No earlier `PSL(2,q)` or Suzuki
candidate, no finite interpolation, and no heavy computation was used.

New active time charged: `00:21:32` (`10:31:11Z` through `10:52:43Z`). Detailed
cumulative active time becomes `07:36:44`. This is below the 45-new-minute cap
and before the wall safety stop. Research now stops in `awaiting_lead`; the
remaining `00:23:28` is unspent.
