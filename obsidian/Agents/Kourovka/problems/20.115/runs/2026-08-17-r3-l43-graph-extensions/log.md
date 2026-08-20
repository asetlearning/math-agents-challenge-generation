---
title: "Kourovka 20.115 — cycle 3 graph-cover extension log"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: counterexample
strategy: L43-GRAPH-EXTENSIONS
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

# Cycle 3 — `L43-GRAPH-EXTENSIONS`

## Active-time ledger

- 2026-08-17T19:57:51Z — work start at inherited cumulative active time `00:10:26`; this lane has at most 35 further active minutes. Stop new mathematics after 30 further minutes and reserve the last five for packaging.

## Scope lock and admissibility

Exact target: for every finite group `G`, every ordinary irreducible complex character `chi` of `G`, and every `x in G`, exact `chi(x) != 0` implies `o(x)chi(1) | |G|`.

The only computational objects authorized in this lane are CTblLib ordinary tables `2.L4(3).2_2` and `2.L4(3).2_3`. Excluded are `L4(3).2_1`, every other table, Brauer/modular or reducible characters, block-theoretic substitutes, floating values, and catalogue expansion. A zero-hit scan is bounded outer-coset coverage only, not a universal proof.

## Strategy portfolio and kill criteria

The Lead-authorized portfolio is recorded in `Agents/Kourovka/problems/20.115/ideas/2026-08-17-post-stale-three-route-portfolio.md`. Its selected replacement strategy is `L43-GRAPH-EXTENSIONS`: certify table identity, derived subgroup `2.L4(3)`, unchanged center, subgroup fusion, non-semilinear outer type, and paper nonduplication; only then isolate outer classes, exact faithful ordinary rows, and evaluate the direct source predicate.

- Catalogue mode is intentionally closed: no identifier beyond the two named tables.
- Structured mode is the index-two extension/fusion analysis that identifies the derived subgroup and outer coset.
- Theoretical mode is only the 2026-paper theorem-hypothesis nonduplication gate; it is not used as a substitute for the direct predicate.
- Certificate plan: preserve GAP/CTblLib versions, identifiers, table/source fusion, sizes, derived and central positions, exact class labels/orders, row labels/degrees/kernels, exact cyclotomic values, products, and integer remainders.
- Hard kill: stop a table if its structure or exact nonduplication cannot be reconstructed within ten active minutes. Stop after both named identifiers regardless of outcome.

## 2026-paper nonduplication gate — preliminary reconstruction

Local artifact `/tmp/2605.04513v1.pdf` has SHA-256 `a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`, identical to the independently reviewed paper artifact. The direct text inspection records:

- Conjecture A is the exact ordinary-character source predicate.
- Theorem 4.3 assumes cross-characteristic prime `ell > 2`, so it does not cover the prime-2 boundary here.
- Proposition 4.17 treats `GL_n(epsilon q)`; for `n=4,q=3` this is the diagonal extension, locally identified as `L4(3).2_1=PGL(4,3)`, which is excluded.
- The paragraph immediately preceding Proposition 4.17 says extending Proposition 4.16 from `SL_n(q)` to extensions by arbitrary automorphisms requires disconnected reductive-group Lusztig restriction control and is more difficult. Thus graph-type extensions are not disposed of by that proposition.
- The consequence after Proposition 4.17 gives the quasi-simple `SL_n(epsilon q)` prime-2 case only for `n` odd or `q` even; `n=4,q=3` satisfies neither.

This is a nonduplication check against the cited paper's stated results, not a claim about all literature. Final admission still requires exact table metadata/fusion evidence that each retained table is a graph-type rather than diagonal extension.

## Structural reconstruction and exploratory probes

Read-only GAP probes used GAP `4.12.1` and CTblLib `1.3.7`.

1. An initial probe printed `2.L4(3).2_2` order `24261120`, source order `12130560`, and fusion source `2.L4(3)`, then stopped with the real GAP error `Variable: 'NamesOfFusionTargets' must have an assigned value`. That nonexistent helper was discarded.
2. A corrected probe returned, for `2.L4(3).2_2`, derived positions `[1..40]`, center `[1,2]`, a 51-entry fusion from `2.L4(3)` with image `[1..40]`, and outer positions `[41..69]`. For `2.L4(3).2_3` it returned derived positions `[1..34]`, center `[1,2]`, a 51-entry source fusion with image `[1..34]`, and outer positions `[35..51]`.
3. `ConstructionInfoCharacterTable` returned central projection constructions from `2.L4(3).2_2` to `L4(3).2_2` and from `2.L4(3).2_3` to `L4(3).2_3`. The same exploratory loop later stopped, as observed, when that attribute had no applicable method on `L4(3).2_1`; no conclusion uses the failed call.
4. `GroupInfoForCharacterTable` could not be used because the optional Browse package is absent; the observed result was `BROWSE fail` and empty group-info lists. The final gate instead uses CTblLib's stored construction/fusion records plus its installed basic group-type metadata.
5. The installed CTblLib `gap4/ctdbattr.g` metadata explicitly maps `L4(3).2_1` to `PGL(4,3)` and `L4(3).2_2` to `PGO(+1,6,3)`. The exact four-line extract is `scratch/ctbllib_l43_group_type_metadata.txt` (SHA-256 `de25009568d2b91e9ef3423c5555628e83c1c029ae085ffea9b7a192ed258f07`); the package source file hash is `538569a494425063596e284f426571dd1f60dfba4359133c5f5cfe9d6db415b1`.

The standard outer-automorphism structure supplies the last naming step: `Out(PSL_4(3))` has one diagonal involution and one graph involution, with no field automorphism because `F_3` has trivial field-automorphism group. Thus the three ATLAS index-two extensions are diagonal, graph, and diagonal-graph. Since CTblLib identifies `.2_1` as `PGL(4,3)` (diagonal) and `.2_2` as `PGO^+(6,3)` under `D_3=A_3` (graph), `.2_3` is the remaining diagonal-graph extension. Both retained quotient tables, and hence their central double covers, are non-semilinear graph-type cases.

## Exact faithful-row / outer-class scan

A compact preliminary exact GAP count, used only as a sanity check before freezing the full certificate, observed:

```text
2.L4(3).2_2 ROWS 69 OUTER 29 FAITHFUL 20 PAIRS 580 NONZERO 84 ZERO 496 HITS 0
2.L4(3).2_3 ROWS 51 OUTER 17 FAITHFUL 17 PAIRS 289 NONZERO 36 ZERO 253 HITS 0
```

The final script was then frozen with SHA-256 `aea034204dbe490e98245f239f7068b31c3d18f60c60598a293a3025993de3b4` and run by:

```text
timeout 55s gap -q -b Agents/Kourovka/problems/20.115/runs/2026-08-17-r3-l43-graph-extensions/scratch/l43_graph_extensions_exact_scan.g > Agents/Kourovka/problems/20.115/runs/2026-08-17-r3-l43-graph-extensions/scratch/l43_graph_extensions_exact_scan.out
```

The command exited `0` in about 2.3 seconds, far below the heavy-compute threshold. The output has 960 physical lines, 200000 bytes, and SHA-256 `439b7088ae0cffa36a6b9e341209ea13407095af00a7c47b56253df7c90a67fd`.

For both tables the recorded `structural_pass=true` entails: ordinary characteristic-zero table; exact cyclotomic values; group/class-size/degree-square sums `24261120`; a certified index-two source fusion from perfect `2.L4(3)`; fusion image equal to the table-derived commutator positions; derived-class size sum `12130560`; source and target centers both the two classes `[1,2]`; and central quotient exactly the corresponding `L4(3).2_i` table. Every complement position is therefore an outer class and every representative generates the order-two quotient with the derived subgroup.

The direct exact predicate results are:

| table | faithful ordinary rows | outer classes | pairs | exact nonzero pairs | failed divisibilities |
|---|---:|---:|---:|---:|---:|
| `2.L4(3).2_2` | 20 | 29 | 580 | 84 | 0 |
| `2.L4(3).2_3` | 17 | 17 | 289 | 36 | 0 |

The output preserves every outer-class label/order/size, faithful-row label/degree/kernel, and every exact pair value, product, remainder, divisibility flag, and violation flag.

An independent serialization/arithmetic audit was run with:

```text
awk -f Agents/Kourovka/problems/20.115/runs/2026-08-17-r3-l43-graph-extensions/scratch/audit_l43_graph_output.awk Agents/Kourovka/problems/20.115/runs/2026-08-17-r3-l43-graph-extensions/scratch/l43_graph_extensions_exact_scan.out > Agents/Kourovka/problems/20.115/runs/2026-08-17-r3-l43-graph-extensions/scratch/audit_l43_graph_output.out
```

It exited `0` and reported `AUDIT_PASS true`, zero duplicate pairs, zero membership/nonzero/product/remainder/divisibility/violation-flag errors, counts `580/84/0` and `289/36/0`. Auditor/output hashes are respectively `5dc4597f45ac6134530ecaa0ecea49ca7a7d542db2dc8385a26a07a9171a9fb2` and `fde8ca7f0d4ea8b8963e005ec26ca7c476b98b6d7dc9db586a646006634e83d2`.

## Strategy outcome

`PARTIAL_RESULT`: the two named graph-cover extension tables have zero direct-predicate violations among all exact faithful ordinary rows on all certified outer classes. This is complete bounded coverage of precisely those two outer cosets, not a proof of the universal assertion. The named strategy is complete and must not widen into a catalogue.

- 2026-08-17T20:11:03Z — new mathematics stopped after 13 minutes 12 seconds in this lane, at cumulative active time `00:23:38`. Packaging began; the unused research allocation is being returned rather than spent on another table or strategy.

## Terminal self-check

- Target and revision remain exactly `20.115/nonzero-character-order-divisibility`, revision 1.
- The evidence is a complete exact scan only of faithful rows on certified outer classes in the two assigned tables; no universal quantifier is discharged.
- The table/fusion representation was productive and produced a checkable bounded zero-hit certificate, but its named two-table lane is now exhausted by design.
- There is no admissible counterexample candidate: every one of the 120 exact nonzero retained pairs satisfies the target divisibility.
- No replacement method or additional table is authorized; state is `awaiting_lead` after handoff.

A final `git diff --check` attempt returned the observed environment error `Not a git repository` and was not used as evidence. Re-running the standalone AWK certificate audit immediately afterward again returned `AUDIT_PASS true`.

- 2026-08-17T20:15:10Z — work stop. Charged active time in this lane: `00:17:19`; final cumulative active time: `00:27:45`. Returned unused allocation: `00:17:41`. Slot released immediately with no catalogue widening.
