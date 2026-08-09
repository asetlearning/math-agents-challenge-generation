---
title: Connected-shell falsification — data, constants and run paths
date: 2026-08-07
domain: group-theory
project: b26
instance: B(2,6)
experiment_type: relative-shell-falsification
status: conjectured
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b26, topic/burnside-infiniteness, topic/small-cancellation, topic/van-kampen, project/b26, status/conjectured, data]
---

# Connected-shell falsification — data, constants and run paths

Inputs and artifacts for [[connected-shell-falsification-results-2026-08-07]], run under
[[connected-shell-falsification-2026-08-07]].

## Provenance

| Leg | Value |
|---|---|
| git SHA | `17b6068b395a35f89c0b05aa0f5048cd6961170c` (branch `feat/patternboost-b25-loop-v1`) |
| `uv.lock` sha256 | `978fe9e2d4809ac5cad3bf2814e01b6948076ce79512621d6a3c7b29994126fe` |
| encoder receipt | `20260805T091512Z`, payload sha256 `b6d0ab50a62f7f30a6517fd3fb0a19da2b189c570397d7a64e846dd54388bec8`, 51/51 conformance |
| frozen Stage-1 receipt | `20260805T080305Z` — 58 period classes, 32 trivial-fifth-power drops, 26 survivors |

`mixer-core` is not on this experiment's path; the encoder receipt payload hash is the third
provenance leg in its place.

**Encoder re-verified independently before the experiment was designed** (not taken on trust):

```
cd infinite_b25/r6_encoder && shasum -a 256 -c artifacts/SHA256SUMS_20260805T091512Z.txt
  -> 11/11 OK
uv run pytest infinite_b25/r6_encoder/tests/ -q
  -> 137 passed in 0.17s
```

The manifest is package-relative, so it must be run from `infinite_b25/r6_encoder/`; running it from
the repo root fails on every entry. Recorded because it cost a cycle.

## Constants

| Constant | Value | Source |
|---|---|---|
| `RANK6_BOUNDARY_LEN` | 30 | `schema.py`, hard-coded (see fork assessment) |
| `PERIOD_LEN` | 6 | `schema.py` |
| `FIFTH_POWER` | 5 | `schema.py` |
| `literal_piece_bound` | 5 = `ell-1` | Validator theorem, via `ShellParameters` |
| `max_internal_contacts` | 3 | nonmetric `C(6)` disc classification; not exponent-dependent |
| `min_connected_arc` | 15 at `n=5`; 9 at `n=4`; 21 at `n=6` | `(n-3)*ell + 3` |
| survivor period classes | 26 | frozen Stage-1 receipt |
| E7 protected word | length 138 | `infinite_b25/avenues/e7_witness.txt` |
| CPU slots | 2 max | Lead |

## Data used

- **Period classes** — the 26 survivors of the frozen Stage-1 corrected receipt, consumed as an
  *enumeration only*. No receipt field is treated as a certificate.
  `AABAAb, AABABB, AABAbb, AABBAB, AABBAb, AABBaB, AABBab, AABaBB, AABaab, AABabb, AAbABB, AAbAbb,
  AAbaBB, AAbabb, AAbbAB, AAbbAb, AAbbaB, AAbbab, ABABab, ABAbaB, ABAbab, ABBaBB, ABBabb, ABaBAb,
  ABaBab, ABabAb`
- **E7 word** — used only in the literal census (a screen; see the results note). Not used in F1.
- **Oracle** — `SoundOnlyOracle`, which cannot emit `NOT_EQUAL` by construction. Every contact in
  every candidate is a *literal* shared arc, so realization is certified by free reduction of
  `u·v^{-1}`; the certificate pins the encoder payload sha256 and carries
  `requires_gpaxioms_ec0 = False`.

## Scripts

Source of truth is the repo; nothing is copied into the vault.

- Runner: `experiments/burnside/r6_shell_falsification/run.py`
- Encoder (read-only, unmodified): `infinite_b25/r6_encoder/`

```sh
uv run python experiments/burnside/r6_shell_falsification/run.py \
    --max-k 3 --out runs/b26_shell/r6_shell_falsification/<TS>/result.json
```

## Run artifacts

| Path | Contents |
|---|---|
| `runs/b26_shell/r6_shell_falsification/20260807T102633Z/` | `v0` — discarded, harness bug (kept, not deleted) |
| `runs/b26_shell/r6_shell_falsification/20260807T102831Z/result.json` | `v1` — full census, 26,376 scored diagrams, 42.7 MB |
| `runs/b26_shell/r6_shell_falsification/20260807T102831Z/witness_W1.json` | witness W1, full diagram record, 8.3 KB |

`result.json` carries the complete two-sided census (both the 13,118 falsifying and the 13,258
non-falsifying diagrams), not a hit list. Per [[project_big_data_policy|the big-data policy]] it
stays local and structured under `runs/`; it is not copied to the vault.

## Enumeration bound actually run

Declared in the pre-registration and not widened post-hoc:

- `k in {2, 3}` cells (the pre-reg declared `2..6`; **`v1` ran `2..3`** — see below);
- contact degree 2 per cell; contact lengths `l in {1..5}` on both contacts;
- **every** split `(gap_out, gap_in)` with `gap_out + gap_in = 30 - 2l`, so both failing
  (`gap_out < 15`) and passing (`gap_out >= 15`) configurations are enumerated;
- period classes: all `C(26, k)` distinct-class combinations; equal classes on adjacent cells are
  rejected up front (they invite classical cancellation).

**What was dropped, stated rather than sampled**: `k in {4, 5, 6}` and contact degree 3 were not
run. They are unnecessary for the verdict — a witness exists at `k=2`, and the degree dichotomy in
the results note shows degree 3 fails a fortiori (Arm B confirms it arithmetically at every
exponent). They are *not* claimed to have been covered. 336,375 candidate configurations were
attempted at `k in {2,3}`; 26,376 were constructible (the rest fail the literal-match requirement
between two distinct period classes).

## W1's failure mechanism — named explicitly (Lead request, 2026-08-07)

Asked: is the mechanism base-region interposition making the external arc **absent**, or merely
**split**? Measured answer: **neither.**

```
C0: contacts=2  externalArc=14  baseInterface=14  sum=30/30  externalRuns=1
C1: contacts=2  externalArc=14  baseInterface=14  sum=30/30  externalRuns=1
```

The external arc is **present and connected** — exactly one run per cell, no splitting, no
interposition hiding it. It is simply **short**: 14 < 15. The base region does not separate the cell
from `∂D`; it **absorbs boundary length** that the shell arithmetic assumes is exposure.

The load-bearing consequence, stated as a partition claim:

> `min_connected_arc = 30 - 3*5 = 15` is derived from a **two-bucket** partition of the cell
> boundary — contacts ⊔ exterior. The adopted R6 category has **three** buckets: contacts ⊔
> exterior ⊔ **base interfaces**. A `BaseInterface` is excluded from `i(Pi)` (gate (i), checklist G
> item 1) *and* from `exposure_runs`, so it consumes boundary while being invisible to both sides of
> the inequality. W1 spends 14 of 30 slots there.

So the arithmetic has no purchase: with a base interface of length `t`, the exposure available is
`n*ell - (contacts) - t`, and `t` is unbounded. This is the same defect
[[2026-08-07-b25-W1-connected-shell-verdict|Validator's W1 verdict]] identified independently, and it
is why the predicate was ruled `#status/disproven` as written rather than merely unproven.

**Scope limit, stated rather than implied.** Every candidate in the `v1` census has
`externalRuns = 1` by construction — the ring builder gives each cell exactly one external arc. So
this harness explored only the **shortened-arc** mode and has *not* explored the **split-arc** mode
(a cell meeting `∂D` in `>=2` components), which is the mode Validator's original falsification
wording named. Note that within simply-connected diagrams the split mode appears hard to reach
without base regions anyway: every exposed cell needs contact-degree `>=2`, which makes the contact
graph leaf-free, hence cyclic, hence in need of a filled region. That observation is *not* a proved
claim and is offered only as a search note.

## Related material

- [[connected-shell-falsification-results-2026-08-07]] — outcomes scored from these artifacts
- [[connected-shell-falsification-2026-08-07]] — pre-registration defining the bound above
- [[Relative Shell Falsification/_type|_type]] — experiment-type root
- [[B26/_progress]] — B(2,6) umbrella
- [[2026-08-05-b25-R6-definition-gates]] — the category these records encode
