---
title: R6 relative-category encoder — Validator schema-conformance review (PASS)
status: replicated
domain: group-theory
project: b25-infinite-witness
claim: "The r6_encoder artifact conforms to the acceptance checklist A-J and does not silently assume P_6 <= 5."
claimant: Developer (build) / Lead (code-layer MERGE)
verification_method: independent recomputation of payload_sha256; adversarial fixture run against the live encoder; source inspection of the shell predicate
tools_used: [infinite_b25/r6_encoder, python3]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/replicated, proof]
---

# R6 encoder — schema-conformance review

**Verdict: PASS on schema conformance.** This is conformance-to-contract, not mathematical evidence —
Lead stated that correctly and the artifact states it itself.

## What I verified independently

**Determinism receipt reproduced.** `payload_sha256` recomputed from the artifact by dropping
`generated_utc` and `payload_sha256` and canonicalising (`sort_keys`, compact separators):

```
claimed    = 242117652526c70e02eda9f7d8e1f4066e9744053361b4ba4f139ff10dcebebc
recomputed = 242117652526c70e02eda9f7d8e1f4066e9744053361b4ba4f139ff10dcebebc   MATCH
```

Reproduced on the first attempt at the canonicalisation, which means the scheme is the obvious one
and independently checkable by anyone. 50/50 pass, 0 fail, 0 unresolved.

**The gap I flagged before the build is closed — verified by running my own adversarial fixture, not
by reading the code.** My pre-build concern was that `exterior ≥ 15` might be *inferred* from
`i(Π) ≤ 3` plus an assumed `P_6 ≤ 5`, which gate (iii) says is uncertifiable. I built the missing
case — `i(Π) = 3` with interior cell-side lengths **5, 5, 8** (a realized contact exceeding the
literal bound), leaving exterior 12 connected — and ran it against the live encoder:

```
i(Pi)                   = 3
interior cell-side lens = [5, 5, 8]  (sum 18)
exposure runs           = [12]
max connected arc       = 12
status                  = fail
reasons                 = ('longest connected external arc is 12 < 15 (total exposure 12 across 1 arc(s))',)
```

Correct refusal. `checks.exposure_runs` computes maximal cyclic runs from actual walk positions, so
the exterior is **computed, never inferred**, and an over-length realized contact is representable
(confirmed independently by fixture I.2, `incidence_lengths {A: 5, B: 7}`). `checks.py:165` carries an
explicit refusal object for `P_6` upper-bound requests citing R6 gate (iii). Gate (iii) is honoured.

**Provenance present.** 58 frozen classes / 32 trivial drops / 26 survivors, read from the corrected
Stage-1 receipt `20260805T080305Z` (`4ee498ef…`) — matching the numbers I verified myself — plus the
frozen rule source `f3554ede…` recorded but never invoked.

**Scope block correct.** `contains_connected_shell_falsification_verdict: false`,
`contains_piece_upper_bound: false`, `contains_minimality_claim_about_any_real_diagram: false`,
`experimenter_gate_open: false`.

## Findings

**F1 — count discrepancy in the routing message, not in the artifact.** Lead's note says "4 entries
under `trusted_external_certificates`"; the artifact reports `count: 3`, with three ids in
`requiring_rung5_gpaxioms_ec0` (`fixture-base-region-trivial`, `fixture-realized-contact`,
`tabulated-equal`). The artifact is right; the summary drifted. Flagged because a trust-surface count
is exactly the number that should not drift between artifact and routing.

**F2 — `source_sha256` is `null` on all three certificates.** Correct for fixture stand-ins (there is
no external source to hash), but the schema should **reject a non-fixture certificate carrying a null
source hash**, so the field cannot stay null when real certificates replace the tables after rung-5
`gpaxioms`. Recommend as a schema invariant now, while it is cheap.

**F3 — fixture coverage gap (not a correctness gap).** The 5,5,8 case above has no fixture. The
behaviour is right by construction, but the suite does not pin it, so a future refactor could
reintroduce the inference without failing a test. Recommend adding my probe as fixture **I.10**.

**F4 — not exponent-parametric.** `SHELL_MAX_INTERNAL_CONTACTS = 3` and `SHELL_MIN_CONNECTED_ARC = 15`
are hardcoded module constants, so the standing exponent-4/6 audit cannot be run mechanically against
this category. Not a checklist item and not a blocker — but it was cheap at design time and gets
dearer, and an n=6 instantiation is the cheapest falsification harness available for anything later
built on this encoder.

**F5 — the honest limits Lead listed are real and correctly encoded.** All negative certificates are
`TabulatedOracle` fixtures tagged `requires_gpaxioms_ec0=true` and labelled "fixture-only; not a
mathematical certificate"; the short-component lemma is bucketed, not proved (checklist H item 3);
relative-cancellation negatives remain screens absent `path_completeness`. No overreach found.

## Verdict

**#status/replicated** — schema conformance PASS. F1 is a routing correction; F2–F4 are
recommendations, none blocking. **No mathematical claim is licensed by this artifact**, and the
connected-shell hypothesis remains open and unattacked, as fixture I.4's own note states.

Experimenter falsification gate is clear from my side; opening it is Lead's call.

## DELTA-NOD — regenerated set 20260805T091512Z (GRANTED)

F2–F4 landed. Verified independently, not from the delta summary:

- `payload_sha256` recomputed = `b6d0ab50a62f7f30a6517fd3fb0a19da2b189c570397d7a64e846dd54388bec8` —
  **matches**, same canonicalisation as the first set.
- 51 items, 51 pass / 0 fail / 0 unresolved (I: 9 → 10).
- **I.10 is my adversarial probe**, correctly encoded as a *fail* case, with the note "the contact
  conjunct passes and the arc conjunct fails, so the verdict is computed from both and never inferred
  from i(Pi) alone". G.2 now consumes I4-pass **and** I10-fail. F3 discharged.
- `ShellParameters(n, ell)`: `min_connected_arc = n*ell - 3*(ell-1) = (n-3)*ell + 3` → n=4:9, n=5:15,
  n=6:21. Matches my derivation exactly. F4 discharged. Note `(n-3)*ell+3` at n=6 **is** `3ell+3`
  algebraically, so reproducing §7 is implementation-consistency, not independent corroboration —
  the artifact's "arithmetic only, no lemma" framing is correct and should stay.
- All three certificates carry `is_fixture: true`; unpinned non-fixture list empty by construction.
  F2 discharged.

**Experimenter falsification gate is clear from my side.** No mathematical claim is licensed by this
artifact; the connected-shell hypothesis remains open and unattacked.

Reviews [[2026-08-05-r6-relative-encoder]] against
[[r6-relative-category-encoder-acceptance-checklist-2026-08-05]], controlled by
[[2026-08-05-b25-R6-definition-gates]].
