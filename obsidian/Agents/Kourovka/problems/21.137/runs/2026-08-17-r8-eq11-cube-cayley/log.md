---
title: "Problem 21.137 run 8 — EQ11-CUBE-CAYLEY"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: EQ11-CUBE-CAYLEY
direction: counterexample
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/algebra-groups
  - project/kourovka
  - status/draft
---

# Run 8 — EQ11-CUBE-CAYLEY

## Active-time ledger

- Work start: `2026-08-17T04:07:15Z`; canonical prior cumulative active time: `181` minutes; current cumulative active time: `181` minutes.
- Allocation: exactly `59` active minutes, cumulative minutes `181` through `240`; stop immediately on a target-equal candidate or on an exact family certificate, and never run past minute `240`.

## Frozen family

Use exactly

`E_12={tau in F_3^6 : dim J_tau<=12 and tau_1 tau_2 tau_3=tau_4 tau_5 tau_6}`,

where `S=E12+E23+E34+E45+E56+E67`, `T_tau=sum_i tau_i E_{i,i+1}`, `J_tau=<S,T_tau>` as a nonunital associative algebra, and `G_tau=1+J_tau`. The curated Validator report establishes that this has exactly eleven rows: three of dimension `6` and eight of dimension `11`. Unequal-endpoint rows, dimension above `12`, every third generator, other primes, wreath material, Hall-span enlargement, and the split ansatz are excluded.

## Exact seven-row target matrix

| constraint_id | role | required condition | experiment gate / candidate value | evidence required | current result |
|---|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | Universal assertion ranges over every admissible `p,G` | One fully admissible `G_tau` would refute it; exhaustion of eleven rows would not address the universal target | A row passing the next five admissibility gates and violating the conclusion | pending |
| `21.137-odd-p-not-2` | admissibility | `p` prime and `p>2` | Base field exactly `F_3`, hence `p=3` | Frozen script metadata and exact field arithmetic | fixed-pass |
| `21.137-odd-finite-p-group` | admissibility | finite same-prime `p`-group | `G_tau=1+J_tau` has order `3^d`, with `d in {6,11}` | Canonical RREF basis and multiplication table | pending per row |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `9` | `S^3!=0`; strict upper triangularity gives `J_tau^7=0`, hence every ninth power is `1` | Exact `S^3`, basis audit, and hand identity | hand identity passed; row artifacts pending |
| `21.137-odd-power-set-definition` | admissibility | `P` is the actual set `{g^3:g in G}` | Exhaustively enumerate every `x in J_tau`, save every map entry `x -> x^3`, and retain the least encoded root per value; `(1+x)^3=1+x^3` | Complete compressed cube map, unique-value/root manifest, counts, and hashes | pending |
| `21.137-odd-power-set-subgroup` | admissibility | actual cube-value set is a subgroup | Boundary-sensitive positive-generator Cayley BFS: require no transition out of the actual value set and exact equality between that set and the discovered monoid/group | Direct boundary triple with roots, or complete Cayley transition table and state equality | pending |
| `21.137-odd-P-abelian` | target_conclusion | actual cube subgroup is abelian | Only after closure equality, test the deterministic Cayley generator list pairwise; a noncommuting pair violates the conclusion | Roots, two values, unequal products, and nonzero matrix commutator; otherwise complete commuting table | pending |

Endpoint equality is not evidence for abelianness. A raw noncommuting pair without actual-set closure, generated-subgroup equality without equality to the exhaustively enumerated actual set, or any omitted row cannot produce a candidate.

## Hand audit of the new observable

Timestamp: `2026-08-17T04:07:15Z`; cumulative active minute `181`.

1. Every element of `G_tau` is uniquely `1+x` with `x in J_tau`, and in characteristic `3`, `(1+x)^3=1+x^3`. Therefore a complete enumeration of the finite vector space `J_tau` gives the actual cube-value set exactly, and a saved map entry supplies an actual cube root rather than only verbal-subgroup membership.
2. The algebra-coordinate circle law is exact: `(1+u)(1+v)=1+(u+v+uv)`. Thus a saved `u,b` in the actual value set with `u circle b` absent is a direct failure of actual-value-set closure.
3. For a deterministic list `B` of positive generators, right-Cayley BFS from the identity enumerates the generated monoid. In a finite group that monoid is the generated subgroup: for each generator `b`, finiteness gives a positive power equal to the identity, so a positive power also realizes `b^{-1}`.
4. During BFS, requiring every transition endpoint to remain in the exhaustively indexed actual set preserves `H subseteq V_tau`. Scanning every value and adjoining any value outside the current `H` ensures `V_tau subseteq H` at termination. If no boundary occurs, the two explicit finite sets are equal, so the actual value set is a subgroup; neither cardinality alone nor abstract generated-subgroup size is substituted for this set equality.
5. Only under that equality, pairwise commutation of every generator in `B` makes the generated group abelian. Conversely, one saved pair `b_i,b_j` with unequal circle products is a noncommuting pair of actual cubes and violates the target conclusion.
6. The exponent audit is unchanged and direct: `S^3=E14+E25+E36+E47 !=0`; every product of seven strict-upper-triangular `7 x 7` matrices is zero, so `(1+x)^9=1+x^9=1`. Hence `1+S` has order `9` and every tested group has exponent exactly `9`.

Hand-audit result: the Cayley boundary, exact-equality, and conditional generator-commutator implications are valid. Every target row remains explicit and no endpoint-pair inference is used.

## Implementation and short self-check

Timestamp: `2026-08-17T04:13:17Z`; cumulative active minute `187`.

- Implemented the single exact enumerator at `Agents/Kourovka/problems/21.137/scratch/eq11_cube_cayley.py`.
- The program derives `E_12` from all `tau in F_3^6` inside the leased command, asserts exactly eleven selected rows with dimension distribution `{6:3,11:8}`, and processes no unequal-endpoint or dimension-above-12 row.
- For each row it saves a deterministic complete `x -> x^3` gzip manifest, a unique value/canonical-root manifest, basis and multiplication table, then either a replayed direct Cayley boundary or exact Cayley set equality plus a complete generator-commuting table. All compressed streams have fixed gzip metadata and both compressed-byte and canonical-text hashes.
- Short self-check command and observed output:

```text
$ python3 Agents/Kourovka/problems/21.137/scratch/eq11_cube_cayley.py --self-test
self-test: PASS
```

- Lead granted compute slot 1 through `2026-08-17T05:10:01Z` for the unchanged exact command `timeout 600s python3 Agents/Kourovka/problems/21.137/scratch/eq11_cube_cayley.py`, one core, below 1 GB RAM.

## Full frozen-family run and immediate slot release

Timestamp: `2026-08-17T04:16:26Z`; cumulative active minute `190`.

Observed exact command outcome:

```text
$ timeout 600s python3 Agents/Kourovka/problems/21.137/scratch/eq11_cube_cayley.py
exit status: 0
script elapsed_wall_seconds: 19.986400842666626
execution-tool wall_time_seconds: 22.914664754
selected_row_count: 11
rows_processed: 11
complete_11_row_manifest: true
status_counts: {"actual cube set not subgroup": 8, "actual cube subgroup abelian": 3}
candidate_row: null
active_assignment_answered: no
```

Primary artifact identities:

- `selected-rows.json`: SHA-256 `a8725dcadb2a361fb2cfce5e4cf340003ec609ea63808bc512012ca4bbad782a`;
- `family-manifest.jsonl`: SHA-256 `42d0d723adfc86b74d8e90aae9d78a9a0b9326b0ea31f877214fe0268d95ad34`;
- `summary.json`: SHA-256 `4c899765f15dc0c579469f7c849a8a6b1f4207dbf09a0bd8f4a80b3f5f095fc9`.

Compute slot 1 was released immediately. The exact eleven rows are three scalar rows `(000000),(111111),(222222)` of dimension `6`, and eight non-scalar rows `(000001),(000002),(010101),(020202),(100000),(101010),(200000),(202020)` of dimension `11`.

The scalar rows each have exactly nine actual cube values, exact Cayley equality on all nine states with two generators, matching value/state code hashes, and a complete three-entry pair table (including diagonal) with every pair commuting. Each non-scalar row has a complete `177147`-input cube map and a direct boundary triple with canonical roots. Their actual-value-set sizes are `171` for the four single-endpoint rows and `123` for the four alternating rows.

## Artifact replay and integrity audit

Timestamp: `2026-08-17T04:16:26Z`; cumulative active minute `190`.

- All eleven row-certificate SHA-256 values were recomputed with `sha256sum` and match the values recorded in `family-manifest.jsonl`.
- Exactly eight row certificates record `177148` cube-map lines (header plus `3^11` inputs), and exactly three record `730` lines (header plus `3^6` inputs). There are exactly eleven complete cube-map files and eleven actual-value/root manifests.
- `gzip -t Agents/Kourovka/problems/21.137/runs/2026-08-17-r8-eq11-cube-cayley/rows/*/*.gz` exited `0` with no output.
- For each of the three closure-equal rows: actual-value count equals Cayley-state count `9`; their canonical code hashes are identical; final transition count is `9*2=18` plus header; and the complete pair table says all generator pairs commute.
- Each of the eight saved boundary records replays both canonical roots, their cubes, and the circle product, and records the product absent from the complete actual-value index. No generated-subgroup-only inference is used.

The exact family-level hard kill is met: all eleven rows now have one of the two required failure certificates, and no target-equal candidate exists.

## Cycle outcome and final ledger

- Work stop: `2026-08-17T04:19:06Z`.
- Active time this run, including implementation, leased computation, integrity audit, and packaging: approximately `12` minutes.
- Final cumulative active time: `193` minutes (`181+12`).
- Unspent allocation preserved after the exact family hard kill: `47` minutes.
- Outcome: `STRATEGY_EXHAUSTED` for `EQ11-CUBE-CAYLEY/E_12` only.
- Active assignment answered: `no`.
- No target-equal candidate, no `CLAIM`, and no claim-check JSON.
- Validator package: `Agents/Kourovka/bus/inbox/Validator/2026-08-17T041818Z__Problem-21.137__REQUEST__audit-eq11-cube-cayley-exhaustion.md`.
- Lead outcome report: `Agents/Kourovka/bus/inbox/Lead/2026-08-17T041819Z__Problem-21.137__REPORT__eq11-cube-cayley-strategy-exhausted.md`.

No mathematical search or parameter broadening continued after the eleven exact row certificates were complete.
