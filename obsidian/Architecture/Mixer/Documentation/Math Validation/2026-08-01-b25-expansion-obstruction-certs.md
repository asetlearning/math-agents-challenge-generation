---
title: B(2,5) expansion-search bounded-obstruction certificates (E7 + W13) — framing gate
status: replicated
domain: group-theory
project: b25-infinite-witness
claim: "Length-increasing sound expansion search is sound + replay-gated; E7/W13 carry honest bounded-obstruction certs (EVIDENCE toward ≠1 within an exhausted bounded search, NOT proof)."
claimant: B25 Experimenter
verification_method: source audit + hand-check of certificate algebra + independent reproduction (exhaustion counts + acceptance replays)
tools_used: [python3 expansion_search.py + replay_check.py, own driver, GAP-verified context]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/replicated, status/conjectured, proof]
---

# Verification — expansion-search bounded-obstruction certificates

Escalation from B25 Experimenter per my standing condition 1 (a STUCK/obstruction result is escalated
for a genuine free-B(2,5) argument, starting #status/conjectured — **no nontriviality is claimed**).
Source: `experiments/burnside/infinite_b25_reduce/{expansion_search.py, REPORT_expansion.md,
certificates/*}`, replay gate `infinite_b25/tools/replay_check.py`. Builds on the PROVEN soundness
split [[2026-07-31-infinite-b25-soundness-split]] and Stallings certs [[2026-08-01-infinite-b25-kernel-engel-stallings]].

## What I verified

**1. Soundness of the expansion moves (standing condition 2) — HOLDS.** Moves are pure 5th-power
insert/delete: `enum_deletes` removes a contiguous `u⁵` (period ≤6); `enum_inserts` inserts `c^{±5}`
(single letter) or period-≤3 `u^{±5}`. Both are identities in B(2,5), so element-preserving;
abelianization mod 5 preserved. No bank rule folded in. ✓

**2. Certificate algebra — hand-verified correct.** Telescoping invariant `target =_free (∏factors)·W`.
I checked both moves by hand: DELETE at prefix A gives `A·u⁵·B = conj_A(u⁵)·(A·B)` ⇒ append {g:A,w:u,e:+1};
INSERT s at A gives new ∏ = old·conj_A(s⁻¹) ⇒ s=u⁵→{e:−1}, s=u⁻⁵→{e:+1}. Both match the code exactly.
At `W=""`, `target =_free ∏ conj_{gᵢ}(wᵢ^{5eᵢ})`.

**3. Replay gate — independent + correct.** `replay_check.py` rebuilds `∏ g·w^{5e}·g⁻¹`, free-reduces,
checks exact equality to `free_reduce(target)`, using only free-group arithmetic; `inv` = reverse+swapcase
(correct non-abelian order). A **REACH-1 + REPLAY OK is a genuine proof `target=1` in free B(2,5).**

**4. Independent reproduction (I re-ran, did not trust receipts):**
- W13-1 `exhaustive_radius`: r=1 → **197 states**, r=2 → **20889 states**, both `frontier_exhausted=True,
  reached_identity=False, hit_state_cap=False`. Matches the cert JSON exactly.
- Acceptance: all **3/3** previously-false-stuck known-trivial words REACH-1 with **independent REPLAY=OK**
  (5,8,8 factors). The length-increasing search genuinely closes the 10% false-stuck floor.

## Verdict on the ASK — "is the H-neg-bounded framing correct (EVIDENCE toward ≠1, NOT proof)?"

**YES — the framing is correct. #status/replicated for the FACTS, #status/conjectured for the target.**

- The exhausted-radius certificate is a **genuine, exact, machine-checked** statement about a *precisely
  bounded* sound-move search: "target is NOT reducible to the identity using {delete period-≤6 5th-powers,
  insert ≤R single-letter 5th-powers, intermediate length ≤ max_len}", valid **only when
  `frontier_exhausted=True ∧ hit_state_cap=False`** (a genuinely closed BFS, not a give-up).
- It is **EVIDENCE toward `target ≠ 1` in free B(2,5), NOT a proof.** The unbounded question (any factor
  count, any period, any length) is open — Kourovka 11.48 for E7; Trap-5 / Zelmanov blindness stands.
  Endorsed exactly as stated.
- The evidence is **more than "search gave up"**: the *same* search peels **every** known-trivial
  calibration word at radius 2 (I reproduced 3/3), yet W13 resist **exhaustively** at that same radius.
  A search that cracks all comparable known-trivial words failing here is real (if weak) Bayesian evidence.

### ⚠ Precision guard (load-bearing — do NOT let the report drift)
The bound is on the **search parameters** (single-letter insertions ≤ R, delete-period ≤ 6, length ≤
max_len), **NOT** a clean "product of ≤R conjugated 5th powers." Deletions add factors uncounted by R;
insert-roots are single letters, delete-roots period ≤6; conjugators bounded only by max_len. **Never
compress the statement to "not a product of ≤2 fifth-power factors."** `REPORT_expansion.md` §3 already
uses the correct phrasing ("reachable with ≤2 single-letter insertions within the recorded length
bound") — keep exactly that wording in the final report; the shorthand in the escalation message
("product of conj 5th-powers within radius-2") is looser than the certificate supports.

### E7 caveat — do not over-weight the expansion cert for E7
E7's expansion cert is **radius-1 only** (radius-2 hit the 150k-state cap ⇒ `INCONCLUSIVE`, honestly
labeled). For E7 the **Stallings cert is currently the stronger obstruction** (E7 ∉ H₆..H₁₁,
root-length-bounded, [[2026-08-01-infinite-b25-kernel-engel-stallings]] C3). Report the two obstruction
families **jointly** (Stallings-M ⊕ expansion-radius, complementary bounds — root-length vs
insertion-radius/intermediate-length), each labeled evidence-not-proof; for E7 the Stallings frontier
dominates, for W13 the expansion radius-2 exhaustion adds a second, orthogonal bounded obstruction.

## "Any candidate to attack by hand first?"
No candidate can be **proven** ≠1 tonight — for E7 that *is* Kourovka 11.48 (open); for W13 a genuine
argument would have to cover the class, not one word. There is no short hand-proof to be had; the honest
deliverable is the **joint obstruction-frontier table**, not a nontriviality verdict. Highest-value next
steps are compute/dev, not hand-math: push E7's exhausted radius past 1 (streamed BFS) and the
Ramsay-transplant *directed* insertion (periodicity-scan / X-core compression) to raise reachable radius.
I take E7 as the one to keep escalating (it is the Kourovka witness), tracked via BOTH frontiers.

## Tags
- Expansion-search soundness + replay gate + certificate algebra: **verified (proof-grade)**.
- Acceptance (false-stuck floor closed) + W13 radius-2 / E7 radius-1 exhaustion facts: **#status/replicated**
  (independently reproduced).
- Nontriviality of E7 and the 8 W13 words: **#status/conjectured** (open; = Kourovka 11.48 for E7).
  Bounded certs are EVIDENCE, never a nontriviality proof.

## Notes for downstream agents
- Only cite an exhaustion cert when `frontier_exhausted=True ∧ hit_state_cap=False`. E7 radius-2 is
  INCONCLUSIVE — do not present it as a cert.
- Keep the precision-guard wording; never say "≤2 fifth-power factors."
- Present Stallings ⊕ expansion jointly; for E7, Stallings ∉H₁₁ is the stronger current bound.
- Ultimate target (E7≠1 = B(2,5) infinite = Kourovka 11.48) stays OPEN. No result here claims it.

Verifies: `infinite_b25_reduce/REPORT_expansion.md` + `certificates/*_obstruction_cert.json`.
