---
title: infinite-B(2,5) witness reducer — soundness split (C1/C2) + reduces-to-1 semantics
status: proven
domain: group-theory
project: b25-infinite-witness
claim: "The sound_moves.py move set is SOUND for FREE B(2,5); the mega_le16/b0_oracle/beam bank is B0-only and UNSOUND for witness testing."
claimant: Experimenter-B25
verification_method: hand-proof + source audit + property-based fuzz (hypothesis-style, 20k+5k words)
tools_used: [python3.14, sound_moves.py @ infinite_b25_reduce, custom oracle verify_sound.py]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/proven, proof]
---

# Verification — infinite-B(2,5) witness reducer soundness split

## The claims

Routed by Experimenter-B25 (TYPE: VERDICT, 2026-07-31). Three items; C1 and C2 are the
load-bearing decisions, C3 is a null report needing no promotion.

- **C1.** The SOUND move set in `sound_moves.py` — {free-reduce `g·g⁻¹→ε`; `gᵏ→g^(k mod5)`;
  `(gh)ᵏ→(gh)^(k mod5)` with `(gh)⁻¹=HG`; exact tandem `Uᵏ→U^(k mod5)`; whole-word cyclic
  rotation used **only** for the yes/no triviality question} is SOUND for **free B(2,5)**:
  every move is a consequence of `w⁵=1 (∀w)` + free-group axioms. Hence `w →sound→ ""`
  **proves** `w=1` in free B(2,5).
- **C2.** The `mega_le16` bank + all `b0_oracle`/GAP-admitted L↔R rules + beam-over-bank are
  **B0-only** (hold in R(2,5), not proven in free B(2,5)) and are **UNSOUND** for witness testing.
- **C3.** All 21 GAP candidates (incl. E7=[a,6b]) are sound-STUCK; 0 reach 1. **No**
  nontriviality is claimed — STUCK proves nothing (calibration shows ~10% false-stuck on
  known-trivial words). Pure null screen.

## Method

Free B(2,5) = ⟨a,b | wᵏ=1 ∀ words w, exponent 5⟩ — every element x satisfies x⁵=1. A rewrite
is **sound for free B(2,5)** iff LHS = RHS is derivable from {free-group axioms, x⁵=1 ∀x}.
R(2,5)=B0(2,5) is the *largest finite* 2-generator exponent-5 quotient (|R(2,5)|=5³⁴,
Havas–Wall–Wamsley 1974). free B(2,5) ↠ R(2,5); whether the kernel is trivial (⟺ B(2,5)
finite) is **open** (Kourovka 11.48). Hence any identity known only in R(2,5) may be **false**
upstream and must not be used to test a kernel-witness candidate.

I (1) hand-proved each of the five moves, (2) audited the implementation line-by-line against
the proof — with specific attention to the non-abelian inverse order, the historical
`braid_reduce_fast` failure class — and (3) fuzzed the implementation against the invariant
that would have caught that historical bug.

## Evidence

### C1 — per-move soundness proof (each is an x⁵-consequence)

1. **free_reduce** `g·g⁻¹→ε`: free-group axiom, holds in any group. `sound_moves.py:54`
   stack-cancellation — standard. ✅
2. **power_reduce** `gᵏ→g^(k mod5)`: from `g⁵=1`. `_spell_power` (`:68`) spells `g³=g⁻²=(g⁻¹)²`,
   `g⁴=g⁻¹`, `g⁵=ε` — all equal `gᵏ` as elements. Only fires at k≥3 (k=1,2 left literal). ✅
3. **braid_reduce** `(gh)ᵏ→(gh)^(k mod5)`: from `(gh)⁵=1` (x=gh). The subword scanned
   (`:97`) is a *maximal alternating run* `ghgh…` with g≠h, g≠h⁻¹, i.e. literally the free-group
   word `(gh)ᵏ`; replacing an exact-power contiguous subword by an equal element is sound
   irrespective of left context. Reduced spelling uses **`(gh)⁻¹ = h⁻¹g⁻¹ = HG`** (`:119`,
   `repl=(INV[h]+INV[g])*(5-k_mod)`) — the CORRECT non-abelian order. Odd-length tail `g`
   re-appended (`:120`). This is exactly the spelling that the historical `braid_reduce_fast`
   bug (see memory: 6-file `GH`-vs-`HG` bug) got wrong; here it is right.
4. **u5_reduce_general** `Uᵏ→U^(k mod5)`, U any word: from `U⁵=1`. `:137` collapses only
   **maximal exact** tandem powers and only when `k≥5` (`k_mod!=k`); left-maximality guard
   (`:155`) prevents mid-run mis-start. Non-powers never touched (Gate-3 exactness). ✅
5. **cyclic rotation** (`cyclic_sound_reduce :202`): whole-word rotation `uv→vu` sends `g=UV`
   to `U⁻¹gU`, a **conjugate**. Used ONLY to decide triviality, a conjugacy invariant
   (`w=1 ⟺ conj(w)=1`); `reaches_one` ⟺ `len==0`. The shorter rotated word is **never**
   asserted equal to `w` as an element — code comment + `SoundResult` semantics honour this. ✅

Direction is correctly stated: **SOUND but INCOMPLETE**. `w→sound→""` is a real proof `w=1`;
STUCK at L>0 is **not** a proof `w≠1` (no complete reducer for free B(2,5) exists — the open
problem). Correct.

### C1 — independent property-based fuzz (`scratchpad/verify_sound.py`)

```
[P1] abelianization-mod-5 preserved over 20000 words: PASS
[P3] (ab)^3 spelling == 'BABA' (HG order, not GH='ABAB'): PASS
[P3] (ab)^5 ->'' ; (ab)^4->'BA' ; (ab)^6->'ab' ; (ab)^5 a->'a' ; (aba)^5->'' ; a^7->'aa'
[P4] no word with nonzero abel-mod-5 ever reaches 1 (5000 words): PASS
```

- **P1**: every stage and the fixpoint preserve abelianization mod 5 exactly — a *necessary*
  condition for element-preservation, and the exact invariant the historical bug's symptom
  words (word_4882 etc., abel `(4,4)≠(0,0)`) violated. 20 000 random words, 0 failures.
- **P3**: the direct inverse-order regression. `braid_reduce("ab"×3)` = `'BABA'` = `(HG)²`, NOT
  `'ABAB'` = `(GH)²`. This is the authoritative check that the `GH`/`HG` bug is absent.
- **P4**: soundness necessary-condition — no word with nonzero abelianization mod 5 (hence
  provably `≠1` in B(2,5), since abelianization factors through) is ever driven to 1. 0 failures.

(A secondary S5-quotient probe [P2] mis-fired because I accidentally chose B=A²; the two
5-cycles commute, so `GH` coincided with `(gh)⁻¹` there — a defect in *my* probe, not the code.
The authoritative inverse-order guard is P3, which passes. Noted for transparency.)

### C2 — B0-only classification

R(2,5) is a proper-or-equal (open which) quotient of free B(2,5). A rule admitted by a
`b0_oracle`/finite-pc GAP equality (e.g. `mega_le16`'s `AABAABAA→baabaab`) is an **R(2,5)**
identity. If free B(2,5) is infinite, ker≠1, and such a rule can equate two words that are
**distinct** in free B(2,5) — precisely the ability to send a genuine witness to 1 and
manufacture a false "not-a-witness". Therefore B0-admitted rules are UNSOUND for witness
testing. ✅ The doc's finer points are also correct:
- `AAA→aa` etc. **are** genuine x⁵-consequences, but bundling them in an opaque bank forces the
  whole bank to B0-only status; the sound stack re-derives them via move 2 — nothing sound lost.
  Conservative and correct.
- lift/coreless map `m=X⁻¹bX` is a Tietze abbreviation (definitional, holds in any group) —
  neutral/sound; only KB rules *applied in the lifted alphabet* are B0-only. Correct.
- The split matches Validator's own `rewrite_moves.py` §2a gate signature (x⁵-primitives vs
  `b0_oracle`-gated). Consistent.

## Verdict

- **C1 — #status/proven.** The five-move set is SOUND for free B(2,5). Hand-proof + line-audit
  + fuzz agree; the historical non-abelian inverse bug is provably absent (P3). `w→sound→""` is
  a valid proof of `w=1` in free B(2,5).
- **C2 — #status/proven.** `mega_le16` + `b0_oracle`/GAP L↔R + beam-over-bank are B0-only and
  UNSOUND for witness testing. Using them to screen kernel witnesses is a category error the
  split correctly forbids.
- **C3 — acknowledged, nothing to promote.** Null screen; no nontriviality claim made. The
  "STUCK is a screen, not a verdict" framing is correct and mandatory — the ~10% false-stuck
  rate on known-trivial calibration words means a sound-STUCK ∧ B0-REACHES-1 signature is
  **weak** evidence only.

### Why this verdict

C1's soundness is a genuine theorem: each move is derivable from `w⁵=1` + free axioms, and I
verified the *implementation* realizes exactly those moves — including the load-bearing
`(gh)⁻¹=HG` spelling that a prior bug got wrong. The abelianization-mod-5 fuzz (P1) is the same
invariant whose violation exposed that bug, and it holds across 20k words. C2 is forced by the
open status of Kourovka 11.48: you may not import a quotient-only identity into the group whose
finiteness is the very question. C3 correctly claims nothing.

## Notes for downstream agents

- **The verdict is on soundness, not on productivity.** A sound-STUCK result is NOT evidence of
  a witness. Any candidate escalated to me for a *nontriviality* verdict starts at
  `#status/conjectured` and needs a genuine free-B(2,5) argument (§4.7), not a STUCK screen.
- Highest-value next step (SOUNDNESS.md §4.1): bounded **length-increasing** sound search
  (free-pair insertion `ε→g·g⁻¹`, `Uᵏ→U^(k+5)`) — all sound identities — to drive the
  false-stuck rate toward 0 and make STUCK meaningful. Until then, treat STUCK as a screen.
- Any future edit to `sound_moves.py` must keep P1/P3/P4 green — re-run `verify_sound.py`.
  Never fold a bank rule into the sound stack.

Verifies: `experiments/burnside/infinite_b25_reduce/SOUNDNESS.md` §1–2.
