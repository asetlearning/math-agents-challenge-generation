---
title: Certificate format for ℓ=6-over-G_5 conjugacy dedup — Validator pre-ruling (ACCEPT WITH MODIFICATIONS)
status: proven
domain: group-theory
project: b25-infinite-witness
claim: "A sound-direction reduction receipt over a NON-confluent G_5 rewriting artifact is a valid certificate of conjugacy-MERGE for the ℓ=6 filtered-profile dedup; it is not valid for non-conjugacy, non-triviality, or geodesy."
claimant: Lead (proposal) / Validator (ruling)
verification_method: soundness/completeness split + independent combinatorial gate of the g1..g7 presentations
tools_used: [Agents/Validator/scratch/gate_gL_presentation.py, shasum, kbmag_v1 standalone]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, topic/uniformity, status/proven, proof]
---

# Ruling — certificate format for the ℓ=6-over-G_5 dedup

Lead's proposal: per pair (u,v), an explicit witness g plus a sound-reduction receipt that
`g⁻¹·u·g·v⁻¹` reduces to `IdWord` under a G_5 diff2 machine from a **non-confluent** `kbprog -wd`
run; sound direction only, no completeness claim.

**VERDICT: ACCEPT WITH MODIFICATIONS.** The architecture is right. The soundness/completeness
split is exactly the correct one and it is the reason this works at all.

## Why the architecture is right (and why the stakes are asymmetric)

- **Sound direction is all a MERGE needs.** Every rule a Knuth–Bendix run emits is a consequence of
  the defining relators, whether or not the run completed. A chain of such rewrites ending in the
  empty word is a derivation of `g⁻¹ugv⁻¹ =_{G_5} 1`. Confluence is needed only for the converse
  (concluding ≠1 from a stuck reduction). We never use the converse here. Non-confluence is fine.
- **The stakes justify the certificate.** An *unsound merge deletes a genuine relator*: you then
  prove E7 ≠ 1 in a group strictly LARGER than G_6, which does **not** establish rung 6. A *missed
  merge* costs only compute (a redundant relator changes nothing — `⟨⟨R'⟩⟩ = ⟨⟨R⟩⟩` either way).
  Merge-on-certificate only; never split on a failed reduction. Consistent with
  [[2026-08-04-b25-filtered-profile-dryrun-gate]] and its forward note.

## What the non-confluent artifact IS and IS NOT licensed for

| Pipeline use | Direction | Licensed? |
|---|---|---|
| conjugacy MERGE (`g·p⁵·g⁻¹·q^{∓5} → IdWord`) | sound | ✅ |
| trivial-fifth-power DROP (`w⁵ → IdWord`) | sound | ✅ |
| realized-overlap equality (found overlap is genuine) | sound | ✅ |
| "w⁵ ≠ 1 in G_5" — genuinely-new selection | complete | ❌ screen only |
| "w⁵ IS shortlex-geodesic in G_5" | complete | ❌ labeled assumption |
| non-conjugacy of the surviving pairs | complete | ❌ bounded-search only |

The last three are **not** blockers, but they must be labeled. Note that at ℓ=4,5 the oracle was a
`gpaxioms`-verified automatic structure (G_3, ec=0); at ℓ=6 it will not be. That is a real drop in
trust level and it is why M2 below exists.

Also note the R(2,5) oracle **cannot** supply non-conjugacy here: R(2,5) has exponent 5, so every
`p⁵` maps to 1 and the invariant is vacuous on the relators. Do not reach for it in that role.

## Bias analysis — pre-register the evidentiary reach BEFORE the run

Under a sound-only oracle the reported filtered max piece `M_rep` has **two opposite biases**:
missed merges inflate it, missed overlap-equalities deflate it. So `M_rep` is neither a clean upper
nor a clean lower bound, and the two possible conclusions are **not** symmetric:

- **`M_rep ≥ ℓ−1 = 5` ⇒ "filtering does NOT rescue clause 6"** — ACCEPTABLE at the same evidentiary
  level as the ℓ=4,5 pilots, provided the conjugator search bound is reported. (Weakened dedup
  biases *toward* this conclusion, so report the search depth honestly; use |g| ≤ ℓ−1 = 5 minimum,
  matching ℓ=5, and state it.)
- **`M_rep < 5ℓ/6` ⇒ "filtering RESCUES clause 6"** — **NOT ACCEPTABLE** on a non-confluent
  artifact. Missed overlap-equalities deflate `M_rep`, so a small value can be an artifact of
  incompleteness. That positive conclusion requires a verified G_5 automatic structure (rung-5
  `gpaxioms` ec = 0).

This asymmetry is pre-registered so the result is not re-read after the fact.

## Mandatory modifications

**M1 — Frozen, hashed artifact.** `.live` files are written continuously; a read while `kbprog`
runs is a torn read. Kill/snapshot deliberately, copy to `g5.rules.frozen`, `shasum -a 256`, and
use that one file for the entire campaign. Every certificate carries the hash. No mid-campaign
drift.

**M2 — Independent replay, not kbmag's word.** `wordreduce -diff2` is accepted as the **search**
tool; the **receipt** must be replayable by a non-kbmag reducer that reads the frozen rule list and
applies the listed rewrite steps. Rationale: a word-difference machine is not an explicit rule
list, so a diff2 "reduction" is not independently checkable without trusting kbmag's difference
table — at ℓ=4,5 that trust was bought by `gpaxioms` ec=0, and here it is not. If a pair cannot
produce a rewriting replay, it stays unmerged. Trust then rests on exactly one assumption
(*every rule in the frozen file is a relator consequence*), which M3 tests.

**M3 — Rule-set soundness battery, once per frozen artifact.**
- (a) **abelianization** — every rule `L→R` must satisfy `ab(L) = ab(R)` in (ℤ/5)². 100% coverage.
- (b) **R(2,5)** — every rule must hold in R(2,5) (order 5³⁴). Valid because
  `G_5 ↠ B(2,5) ↠ R(2,5)`, and non-vacuous because rules are not themselves fifth powers. 100% if
  ≤ 200k rules, else a 20k uniform sample **plus 100% of every rule used in any certificate**.
- (c) positive control — all 41 defining relators of `g5` reduce to `IdWord`.
- (d) negative control — a battery of words with nonzero (ℤ/5)² image must **not** reduce to
  `IdWord`.
Any (a)/(b) failure ⇒ **HALT** and route to me. This is a plumbing test (wrong alphabet, stale
file, truncated rule) more than a mathematics test, which is precisely where the risk actually is.

**M4 — Convention and literal word pinned.** Keep the convention already used by the four verified
ℓ=5 certificates: `g·p⁵·g⁻¹·(q^{5σ})⁻¹ → IdWord`, `σ ∈ {+1,−1}`. **σ = −1 must be supported** — all
four ℓ=5 witnesses were conjugate-to-INVERSE. The record must contain the fully expanded literal
string actually fed to the reducer, so the checker never re-derives it.

**M5 — Merge bookkeeping.** Union–find with one certificate per merge **edge** (spanning forest,
n−1 per bucket; transitivity is free). Non-merged pairs recorded as bounded-search with the
explicit bound. Downstream phrasing is `⟨⟨R'⟩⟩ = ⟨⟨R⟩⟩` justified edge-by-edge, never "there are
exactly N conjugacy classes" (a class count is an upper bound only).

**M6 — Filter direction.** The profile filter may only ever *prevent* merges (safe). If any code
path uses "different profile ⇒ not conjugate" as a positive claim, that profile must first be
proven a conjugacy invariant of G_5 — separate ruling, do not assume it.

## Record format

```json
{"cert_type":"conjugacy_merge","ell":6,"oracle":"G_5",
 "p":"<root>","q":"<root>","sigma":-1,"witness_g":"<word>",
 "cert_word_literal":"<expanded string fed to the reducer>",
 "reduction":{"search_tool":"wordreduce -diff2 g5","replay":"<checker id>",
              "result":"IdWord","steps":N,"trace":"<file>"},
 "artifact":{"presentation":"g5","pres_sha256":"b029419567...","rules_file":"g5.rules.frozen",
             "rules_sha256":"...","kbprog_cmd":"...","kbmag_version":"..."},
 "controls":{"abelianization":"pass","r25":"pass"}}
```

## Bonus gate result — the g5 presentation is ALREADY on disk and is CORRECT

Ran an independent combinatorial gate (`Agents/Validator/scratch/gate_gL_presentation.py`, written
from scratch, no kbmag and no repo code). Required set = one representative per
(rotation, inversion) class of cyclically-reduced **non-proper-power** words of length ≤ L. Each
reduction step is a sound normal-closure identity: `w` conj to its cyclic reduction `c` ⇒
`w⁵ ∈ ⟨⟨c⁵⟩⟩` with `|c| ≤ |w|`; rotation = conjugation; `(w⁻¹)⁵ = (w⁵)⁻¹`;
`(uᵏ)⁵ = (u⁵)ᵏ` with `|u| < |w| ≤ L`.

```
g1: file=  2 required=  2 missing=0 dup=0 out_of_spec=0 OK  sha256:c2052e73e0764ed8
g2: file=  4 required=  4 missing=0 dup=0 out_of_spec=0 OK  sha256:d47715e085038bcb
g3: file=  8 required=  8 missing=0 dup=0 out_of_spec=0 OK  sha256:907ec451d2f91693
g4: file= 17 required= 17 missing=0 dup=0 out_of_spec=0 OK  sha256:1ec958ec94859efa
g5: file= 41 required= 41 missing=0 dup=0 out_of_spec=0 OK  sha256:b02941956761e1cf
g6: file= 99 required= 99 missing=0 dup=0 out_of_spec=0 OK  sha256:4dfa67b0dde6d17c
g7: file=255 required=255 missing=0 dup=0 out_of_spec=0 OK  sha256:271e9a4d29f3c362
```

Every rung complete and non-redundant. `g5` = 41 relators = 2+2+4+9+**24**; the 24 length-5 roots
match the "24 candidates" of the ℓ=5 dry run exactly, and the 9 length-4 roots reproduce the known
G_4 set — an independent corroboration of the whole ladder setup.

**Consequence: no g5 rebuild is needed.** `g5` (Jul 31 21:54,
sha256 `b02941956761e1cf95a46ddc27e5433d8648a72722ca4d142ffaae6e14b6523f`) is GATED. Rebuilding
risks a silent collision; a fresh `kbprog` run will also overwrite the existing
`g5.kbprog.live` (12.7 MB, Aug 1 18:51,
sha256 `f3554eded618f8da...`) — **copy it aside before launching.**

## Rung-4 stamp — what I will require when `gpaxioms` exits 0

Not a verdict, a pre-statement so nothing is re-run later:
1. **Reboot-integrity of the resumed inputs.** `g4.wa` (Aug 2 18:52) and `g4.diff2` (Aug 2 16:27)
   both have mtimes ~2 days before the Aug 4 20:48 reboot, so they were *not* open for writing at
   shutdown — torn-write risk is low, and I record their hashes now:
   `g4.wa` `268bb111eaa3c0a1…`, `g4.diff2` `7a47f1cc8c998b47…`. Still want a structural parse
   (state counts vs the pre-reboot logged values) in the receipt.
2. `gpcheckmult` clean **and** `gpaxioms` ec = 0, with the log.
3. Same sanity battery as rungs 2/3: A⁵, B⁵, (AB)⁵ **and all 9 length-4 roots' fifth powers** →
   `IdWord`; a nonzero-abelianization word → **not** `IdWord`.
4. E7 reduced under the **verified** structure: the actual normal-form string and its length, not
   just "nonempty".
5. `g4` presentation hash pinned (`1ec958ec9485…`, gate above) as the object the structure verifies.

Standing modulo (unchanged, [[LADDER]]): correctness of kbmag's verified-automatic-structure word
problem — `gpaxioms` pass ⇒ automaticity ⇒ shortlex NF unique ⇒ word problem decided.

## Verdict

**#status/proven** for the ruling's mathematical content (soundness/completeness split; the
presentation gate). The certificate format is **ACCEPTED WITH MODIFICATIONS M1–M6**.

Scope unchanged: no program-direction claim, no B(2,5)-infinite claim; Kourovka 11.48 open.

Extends [[2026-08-04-b25-filtered-profile-dryrun-gate]].
