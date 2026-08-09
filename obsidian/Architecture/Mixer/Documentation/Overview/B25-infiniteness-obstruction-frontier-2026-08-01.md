---
author: maumayma
tags: [agent/lead, user/maumayma, domain/group-theory, project/b25, status/replicated, overview, results]
---

# B(2,5) Infiniteness — Obstruction Frontier (2026-08-01 session)

10-hour human-directed deep dive. **No proof of infiniteness or finiteness was obtained** (the
problem remains open, as it has since 1902/1950s). The session's durable products: a
Validator-proven logical skeleton, the sharpest witness pinned, and machine-checked bounded
obstruction certificates on two orthogonal axes. Full report: `algo_mixing/infinite_b25/FINAL_REPORT.md`.

## Proven skeleton (Validator: #status/proven, [[2026-08-01-infinite-b25-kernel-engel-stallings]])

1. ker(B(2,5)→R(2,5)) = γ₁₃(B) = γω(B); **B(2,5) infinite ⟺ γ₁₃(B(2,5)) ≠ 1**.
   (Kostrikin 1959 suffices; class(R(2,5)) = 12, NOT the folklore 13 — HWW 1974 + GAP ×3.)
2. E7 = [a,b,b,b,b,b,b] (Kourovka 11.48, Kostrikin 1990, still open in v45/2026): E7 = 1 in
   R(2,5) (both conventions), [a,5b] ≠ 1 — Engel boundary exactly 6. **If E7 ≠ 1 in B(2,5),
   B(2,5) is infinite.** One-directional: E7 = 1 would NOT prove finiteness (6-Engel + exp-5 ⇒
   locally finite is open; only 4-Engel proven, Vaughan-Lee 1997).
3. No finite certificate of E7 ≠ 1 exists: every finite exponent-5 group is 6-Engel, so deciding
   the witness negatively is equivalent to the open problem (Trap 5).

## Bounded obstruction certificates (exact, machine-checked, #status/replicated)

- **Root-length axis (Stallings folding, Lead + Developer):** E7 and all 20 weight-13/14 kernel
  candidates are NOT products of fifth powers with all roots ≤ 15 (any number of factors).
  Rust/Python byte-identical cross-validation; M=15 = 1.04B path edges; positive controls catch
  16/30 known-trivial products. `infinite_b25/avenues/stallings/SUMMARY.md`.
- **Search-radius axis (sound expansion search, Experimenter-B25):** E7 radius-1 exhausted;
  all W13/W14 candidates radius-1 AND radius-2 exhausted; engine calibrated (30/30 known-trivial
  words trivialize with replay-verified certificates; false-stuck floor closed).
  `experiments/burnside/infinite_b25_reduce/REPORT_A5_final.md`.
- **G_L lottery (finiteness stop-condition):** G_L = F₂/⟨⟨w⁵, |w|≤L⟩⟩ surjects onto B(2,5);
  any finite G_L ⇒ B(2,5) finite. G₁–G₄ proven infinite (four different methods); frontier
  L* = 5 where all four methods provably close or cap. `infinite_b25/avenues/a6_bounded/SUMMARY.md`.

## State of the art (verified)

Adian n ≥ 665 proven; ART n ≥ 557 under review; nothing touches n = 5 (constants fail by ~2
orders); no formalization work exists anywhere (open niche); exponent-4 Engel analogue solved
positively (Ramsay 2024, 26 fourth powers) and its certificate layer transplants to n = 5.

## Extension session 2026-08-02: the E7 ladder + period-band program

- **Ladder (proven reformulation):** B(2,5) infinite ⟺ E7 ≠ 1 in every G_L. **Rungs 1–3 PROVEN**
  (conjugator-unbounded certificates via free-product NF + two verified automatic structures).
- **G₃ word-hyperbolic — proven at FSA level** (geodesic bigons 10-fellow-travel, gpgeowa;
  Papasoglu criterion). All 5 rung-4 periods straight for ALL powers (DFA pumping,
  Validator-independently-verified + metric cross-check k≤40).
- **No published filling theorem reaches n=5** (AGM/DGO/Coulon each formally fail; citations in
  math_expert_R2_full.md; gap 50–100×). Two independent expert models concur.
- **Period-Band Meta-Theorem v0.3** (Math-expert + Delta + Validator): bespoke Greendlinger
  criterion for E7-survival in G₄ with same-period fifth-power overlaps as Burnside bands.
  Validator: approach sound, skeleton sound-given-lemmas, #status/conjectured. E7's Dehn-arc
  layer verifier-clean (0 strict arcs, exposure ≤ 7/20, distinct pieces ≤ 3 < 20/6). Open: band
  contraction (topological part), annulus width proof, C(3) no-progress bands — last two with
  Math-expert. Evidence chain hash-frozen in Delta's REPLAY.md.
- G₄ automatic structure: -h run cleared the word-acceptor determinization wall (20.1M states
  pre-minimization) — in progress at session close of this note revision.
- New canvas agent: "Delta" (Codex, math-filling-specialist role).

## FINAL RESULT (2026-08-03): rung 4 PROVEN — E7 survives to G₄

**Theorem (#status/proven, Validator final read PASS, [[2026-08-03-b25-gate2-FINAL-RULING-E7-survives-G4]]):**
E7 ≠ 1 in G₄ — E7 is not a product of conjugates of fifth powers of words of length ≤ 4, any
conjugators, any number of factors. First certified period-band small-cancellation step at
exponent 5. Ladder proven at G₁–G₄. Scope: one rung; NOT B(2,5) infiniteness; Kourovka 11.48
remains open. Assembled proof: repo `infinite_b25/avenues/band_contraction_core.md`.

> **Link note (2026-08-04):** all wikilinked verdict notes below are real files in
> `Architecture/Mixer/Documentation/Math Validation/` under THIS vault root
> (`~/Documents/Obsidian/Math/obsidian/`). If a link renders as dangling, your Obsidian vault
> is rooted elsewhere — open that folder directly. In-vault mirrors of the repo artifacts:
> [[B25-E7-G4-assembled-proof-mirror]], [[B25-E7-ladder-mirror]], [[B25-E7-G4-provenance-mirror]].

## Reading order (vault)

1. This note (map + results).
2. [[2026-08-03-b25-gate2-FINAL-RULING-E7-survives-G4]] — the final ruling + complete proof
   chain + final-read PASS (Math Validation/).
3. The review chain, in order, same folder: [[2026-08-01-infinite-b25-kernel-engel-stallings]]
   (kernel = γ₁₃, E7 witness logic, Stallings semantics) → [[2026-08-02-b25-gate2-period-band-metatheorem]]
   (meta-theorem v0.3 gated) → [[2026-08-02-b25-gate2-curvature-core-review]] →
   [[2026-08-02-b25-gate2-unified-lemma-U-review]] → [[2026-08-02-b25-gate2-H2-decisive-review]]
   → [[2026-08-02-b25-gate2-SEI-receipts-and-batch-rulings]] →
   [[2026-08-02-b25-gate2-beaded-lemma-review-and-final-gate]] — every gap caught + fixed.
4. Session narrative: [[2026-07-31-infinite-b25-session]] (Lead log, full timeline).
5. Full technical proof + receipts: repo `algo_mixing/infinite_b25/` (band_contraction_core.md,
   LADDER.md, FINAL_REPORT.md, gap/, avenues/stallings/, Delta's REPLAY.md evidence chain).

## Open next steps (recorded, not closed)

Gate 2 geometry: annulus width proof + C(3) (Math-expert), then banded-verifier closure; G₄
gpaxioms + E7 reduction if the -h build lands; rung 5+ design. Older items: E7 radius-2
exhaustion via streamed BFS; Stallings ceiling > M=15 (batched fold); longer Lyndon pools +
nilpotent depth-c guidance; L* = 5 lottery push; Gorshkov axial-algebra fusion-law check.
