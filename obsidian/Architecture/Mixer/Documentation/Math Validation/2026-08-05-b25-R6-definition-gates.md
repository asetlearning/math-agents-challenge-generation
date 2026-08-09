---
title: R6 definition gates (i)-(iv) — Validator pre-rulings
status: disproven
domain: group-theory
project: b25-infinite-witness
claim: "The four R6 definition gates in ELL6-THEORY section 8 are well-posed and can be adopted as the category for routes (1) R6-shell and (2) CE6."
claimant: Math-expert (via Lead)
verification_method: definition analysis + exhaustive enumeration of length-5 cross-class pieces at ell=6
tools_used: [exhaustive window/root enumeration L=5,6]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, topic/uniformity, status/disproven, proof]
---

# R6 definition gates — pre-rulings

Gates as posed in section 8 of [[ell6-theory-barrier-analysis-2026-08-05]]; the CC6 carrier finding
below refutes a premise of that note's section 4. **This note is the durable authority for these
four rulings.**

Headline: **(i) RULED, with a forced choice. (iii) DISSOLVES under (i) — and in dissolving it
relocates the blocker onto rung-5 `gpaxioms`, not Delta. (ii) accept only as a hypothesis to prove,
falsify-first. (iv) FALSIFIED as stated — 84 of 308 length-5 pieces have no rank-5 carrier.**

---

## (i) R6 relative category — RULED

**Cells.** Two kinds: **rank-6 cells** with boundary label a cyclic rotation of `p^{±5}`,
`p` a length-6 root; and **base regions**, 2-cells whose boundary label is any word `=_{G_5} 1`.
G_6 = G_5 / ⟨⟨p⁵ : p in S⟩⟩ with |S| ≤ 26.

**Pieces — the forced choice. Define pieces as G_5-REALIZED contacts, measured by arc length on the
rank-6 cell boundary (i.e. as a subword of `p⁵`), never by diagram path length.** Both halves matter:
- *realized, not literal* — otherwise (iii) becomes a real and probably false lemma (below);
- *measured on the cell boundary* — a diagram path has no canonical length (any G_5-equal
  representative will do), and the shell arithmetic (`exterior ≥ 30 − 3·5 = 15`) is an accounting in
  the relator's own letters. Mixing the two units makes `P_6 ≤ 5` and `exterior ≥ 15` incommensurable.

**Reduced.** Must exclude *both* (a) classical cancelling pairs of rank-6 cells, and (b) **relative**
reducedness: no two rank-6 cells joined by a path whose label conjugates one boundary to the other's
inverse *in G_5*. (b) is not optional — without it minimal-area diagrams are not reduced in the sense
the shell classification needs.

**Band moves.** Must be declared as an equivalence that (1) does not increase the rank-6 cell count,
(2) preserves the label of ∂D, (3) terminates. **Area = number of rank-6 cells**, and minimal-area
diagrams must be shown to exist.

**The structural consequence, and it forces (ii).** Base regions have unbounded boundary length and
no piece bound whatsoever. So every count in this category is a count of *rank-6 boundary letters
only*, and base regions are invisible to it. That is exactly why a shell can fail to touch ∂D at
all: a base region may separate it. Gate (ii) is therefore not independent of (i) — it is the debt
(i) incurs.

---

## (iii) Piece preservation — DISSOLVES, and relocates the blocker

**Under the realized definition ruled in (i), gate (iii) is not a lemma.** If contraction or phase
absorption merges two arcs into one contact, that contact is *by definition* a realized piece, hence
`≤ P_6`. Preservation is automatic. All the content migrates into the measurement of `P_6`.

**But the measurement is the completeness direction, and that is the real finding.** `P_6 ≤ 5` says:
for every pair of rank-6 cells and every pair of boundary subwords `u, v` of length ≥ 6,
`u ≠_{G_5} v`. That is a **non-equality** claim, quantified universally. A non-confluent artifact
certifies equalities only; "no equal pair found" is a SCREEN, exactly as ruled in
[[2026-08-05-b25-g5-conjugacy-certificate-format-ruling]]. **A sound-only oracle can certify
`P_6 ≥ k`; it can never certify `P_6 ≤ 5`.**

**Consequence for scheduling — this is the item Lead should act on.** Routes (1) R6-shell and (2)
CE6 both require a certified `P_6` upper bound, so **both are blocked on a verified G_5 automatic
structure (rung-5 `gpaxioms` ec = 0), not on Delta's Stage 2.** Delta's Stage 2 produces merge
certificates and realized-overlap *lower* bounds; it cannot produce the bound either theory route
consumes. This is the same asymmetry I pre-registered — "filtering rescues" needs completeness — now
showing up as the gating dependency for the theory work. The finite check is genuinely decidable once
the structure verifies (finitely many subword pairs over ≤26 relators), so this is a real target, not
a wall.

---

## (ii) Connected-shell lemma — HYPOTHESIS ONLY, and falsify before proving

Do **not** inherit it from Strebel. Classical shells have a single outer arc because the diagram is a
disk over a free-group presentation with a simple boundary; base regions break both premises.

**Required statement, in full:** *in a minimal-area, band-reduced relative diagram D for E7, there
exists a rank-6 cell Π with i(Π) ≤ 3 whose contact with ∂D is a **single connected arc** of length
≥ 15.* Note ≥15 needs **both** conjuncts — `i(Π) ≤ 3` alone gives total exposure 15 split across up
to 3 components, longest ≥ 5, which supports no scan.

**Recommendation: try to falsify it computationally first.** The ℓ=6 objects are explicit and finite;
exhibiting one band-reduced relative diagram in which every boundary rank-6 cell meets ∂D in ≥2
components kills the route at a fraction of the cost of proving it. Cheaper to kill than to prove.

**Cut-vertex flag.** Minimal-area diagrams need not have simple boundary. If the argument decomposes
at cut vertices, the relevant boundary is the **component's**, not the full 138 — so a component with
boundary < 15 admits no shell with a ≥15 outer arc, and that case must be closed separately (it
should force ≤1 rank-6 cell in the component). State the decomposition explicitly.

---

## (iv) Critical-carrier definition — FALSIFIED AS STATED

Section 4 asserts: *"at ℓ=6, every literal critical piece has length 5, so it is a complete root from
the previous rung, whose fifth power already lies in the base relator family."* The first clause is
right (I proved literal `P_ℓ ≤ ℓ−1` and it is attained). **The second does not follow, and is false.**
A length-5 subword of a length-30 relator is a length-5 *word*; it is a rung-5 root only if it is
cyclically reduced and not a proper power. Exhaustive enumeration over all 58 length-6 classes:

```
distinct length-5 cross-class pieces            : 308
  ARE rung-5 roots (cyc-reduced, non-proper-power): 224   (72.7%)
  NOT cyclically reduced -> no s^5 relator exists :  80   e.g. AAABa AAAba AABBa AABaa AAbaa AAbba
  cyc-reduced but a proper power                  :   4   AAAAA BBBBB aaaaa bbbbb
```

**84 of 308 pieces (27.3%) have no rank-5 carrier.** For the 80 non-cyclically-reduced ones there is
no relator `s⁵` in the base family at all — `s⁵` is not freely reduced as written and the cell simply
does not exist. The 4 proper powers (`A⁵` and friends) do have a carrier, but it is the **rank-1**
cell `a⁵`, not a rank-5 one; assigning them to rank 5 would misgrade the curvature.

**Ruling: the corridor labeling is not total, so CC6 as written is ill-defined on 27% of its own
objects.** Before any enumeration or write-up, Math-expert must either (a) restrict corridors to the
224 root-carrier pieces and prove the other 84 are separately controlled — noting they are *not* a
negligible tail — or (b) redefine the carrier so it exists for every length-5 contact, e.g. by
carrying the cyclic reduction of `s` together with the conjugator that produced it, and then re-derive
the curvature charge in the new grading.

**Second requirement, independent of the above — non-double-counting must be exhibited, not asserted.**
The carrier assignment must be a function of the **arc**, not of the cell pair, and the note must
display an explicit **partition**: the charged corners of distinct corridors form a disjoint union. A
single arc serving as a piece for several cell pairs is the double-count risk, and "assigned
canonically" is not a proof that it does not happen.

---

## Standing conditions on all four

The **exponent-4/6 audit** (their own item 5) is confirmed as mandatory and I will apply it to every
lemma routed to me: state which hypothesis fails at n = 4 and n = 6. Survival at n = 6 disproves
Hall 1958, so survival means the lemma is wrong. See
[[2026-08-05-b25-ell6-theory-preruling]].

## Verdict

- (i) **#status/proven** as a ruling — category adopted with the realized-piece definition forced.
- (iii) **#status/proven** that it dissolves under (i); **#status/conjectured** that `P_6 ≤ 5` holds,
  and **blocked on rung-5 `gpaxioms` ec = 0** — a sound-only oracle cannot certify it.
- (ii) **#status/conjectured**, hypothesis only, falsify-first, cut-vertex case to be closed.
- (iv) **#status/disproven** as stated (84/308 carrierless); repairable via (a) or (b), plus an
  explicit partition for the curvature charge.

Scope unchanged: no program-direction claim, no B(2,5)-infinite claim; Kourovka 11.48 open.

Gates [[ell6-theory-barrier-analysis-2026-08-05]] (section 8; section 4 premise refuted by (iv)).
Extends [[2026-08-05-b25-ell6-theory-preruling]],
[[2026-08-05-b25-g5-conjugacy-certificate-format-ruling]].
