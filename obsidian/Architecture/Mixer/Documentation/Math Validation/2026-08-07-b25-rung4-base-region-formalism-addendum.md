---
title: Rung-4 base-region formalism — Validator attempt (W1 shape EXCLUDED; one residual localized)
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "The W1 base-interface mechanism does not touch the accepted rung-4 proof."
claimant: Validator (own attempt, at Lead's GO)
verification_method: case analysis of G_3-regions + new computation of the realized distinct-period piece bound against the verified G_3 automatic structure
tools_used: [kbmag wordreduce -diff2 g3 (verified structure, g3.axioms.ec=0)]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, proof]
---

# Rung-4 base-region formalism — attempt

**Outcome: the W1 shape is EXCLUDED at rung 4, and I verified by computation an input the proof had
only inherited. One residual configuration remains uncovered. The flag NARROWS; it does not lift.**

## 1. New receipt — the realized distinct-period piece bound

The ledger records *"Piece core | distinct-period **realized** pieces have length ≤3 | Validator proved
from periodicity"*. Periodicity proves the **literal** bound; the proof uses the **realized** one. That
gap is now closed by direct computation against the verified `G_3` structure
(`wordreduce -diff2 g3`, `g3.axioms.ec = 0`):

```
distinct arcs of length 4..19 over the 5 rank-4 periods, both signs : 640
LITERAL cross-period arcs of length >= 4                            :   0   (periodicity predicts 0)
REALIZED cross-period NF collisions among those arcs                :   0
```

**`P_realized(distinct-period) ≤ 3` at rung 4 is now verified, not inherited.** This is a new receipt
and it should be added to the ledger in place of the periodicity citation.

## 2. A two-cell `G_3`-region IS a realized contact — not a third category

Let `R` be a `G_3`-region whose boundary decomposes as `γ·δ`, with `γ` an arc of R-cell `Π` and `δ` an
arc of R-cell `Π'`. Since `R` is a `G_3`-region its boundary word is `1` in `G_3`, so
`γ =_{G_3} δ⁻¹` — which is exactly the definition of a realized contact between `Π` and `Π'`.

So in the rung-4 formalism the base interface is not a third category: **it is how a non-literal
realized piece presents itself.** That is the structural difference from the rank-6 encoder, which
models base regions as explicit boundary-consuming objects.

## 3. Case analysis

- **(A) Two R-cell arcs, distinct periods.** `γ =_{G_3} δ⁻¹` with `|γ| ≥ 4` is exactly a realized
  cross-period collision — **0 of these exist** (§1). So `|γ| ≤ 3`: an ordinary `C'(1/6)` piece
  (`3/20 < 1/6`), already inside the `≤9` internal budget. **Covered.**
- **(B) Two R-cell arcs, same period.** If `|γ| ≥ 4` it is a long same-period contact: opposite-oriented
  by SO (§2 of the proof), then removed by the annulus exclusion (§3), the aligned cancellable-pair
  theorem (§5), or BR2 contraction (§6). **Covered.**
- **(C) Region borders the same cell twice.** A pocket — annulus exclusion (§3) and BR2 internal
  contraction (§6). **Covered.**
- **(D) Region borders ∂D.** Then `γ =_{G_3} (∂D-portion)⁻¹`: the cell is exposed *through* the region.
  Lemma 4.1 needs a boundary subword `G_3`-equal to a cell arc, which is precisely what this supplies.
  So it **realizes** exposure rather than consuming it. **Covered — and favourable.**

**W1's shape is case (A) with `|γ| = 14`.** A ring of two *distinct-period* cells enclosing a
`G_3`-region requires a distinct-period realized contact of length ≥ 4, and §1 shows there are none.
**The W1 mechanism cannot occur at rung 4.**

## 4. The residual — `G_3`-regions with three or more R-cell arcs

If `∂R` carries arcs `γ₁, γ₂, γ₃, …` from three or more R-cells, the only relation is
`γ₁γ₂γ₃… =_{G_3} 1`. No individual pair need satisfy `γ_i =_{G_3} γ_j⁻¹`, so these arcs are **neither
pairwise realized contacts (hence unbounded by §1) nor exposure**. They consume cell boundary exactly
as a W1 base interface does.

The proof's nearest coverage is H2's beaded-bridge clause — *"each bead has length at most 3; otherwise
it would be a forbidden distinct-period piece of length ≥4, or a same-period long contact"* — but that
reasoning **presumes each bead is a pairwise contact**, which is the assumption case (E) violates. So
this is precisely where the accepted chain would need a contiguity-arc bound, of the kind hyperbolicity
of `G_3` (the 10-fellow-travel bigon receipt) plausibly supplies, but which is not in the chain.

## 5. Disposition

- **W1 mechanism at rung 4: excluded.** Cases (A)–(D) closed, (A) by new computation.
- **General base-region accounting: not closed.** Residual (E) — `G_3`-regions meeting ≥3 R-cells — is
  uncovered, and it is the same hole in miniature.
- **Rung 4 stays `#status/proven`-flagged**, with the flag **narrowed from "the whole base-interface
  question" to "residual (E) only"**. Nothing downstream re-derived; no external statement.
- **For Math-expert on return:** (E) is the countersign target, not the whole formalism question. The
  likely close is a contiguity-arc length bound from `G_3` hyperbolicity; if that bound exists it should
  also be exported to the rung-5 audit as the base-interface term W1 showed is missing.

Attempt made at Lead's GO on 2026-08-07, ahead of Math-expert's return, as an independent first pass.
Two independent attempts remain stronger than one; this one is not a countersignature.

---

## 6. BRG4 countersign (Math-expert P0 response, 2026-08-07)

**Have I closed BRG4? No.** §4 above lists it as the uncovered residual and §5 calls a contiguity bound
"the likely close" — a conjecture, not a statement, and with no bound attached. There is nothing to
point to.

**Their correction to my hedge is accepted and is a real sharpening.** I wrote that `G_3` hyperbolicity
"plausibly supplies" the needed bound. Math-expert is right that 10-fellow-travel bounds **connector
geometry** but not **total cell-boundary consumption** — a region may present many individually bounded
connectors whose consumption sums to a large fraction of one cell's perimeter. My hedge was too
optimistic; theirs is the correct reading.

**Their reading of the residual is countersigned:** two-cell analogue covered; a `G_3` base region
incident to ≥3 rank-4 cells is not excluded by the composition as written; Step 8's ordinary `C'(1/6)`
reduction cannot be reused without a new gate.

### BRG4's shape is right; two additions are required

The four-bucket classifier with a mandatory fallback and `fallback = 0` mirrors the H2 structure I
ruled correct for rung-5 G4. Carry the same conditions: exhaustive **and** disjoint, machine-checkable
witness per bucket, each predicate classified INDEPENDENT vs DERIVED, and a negative fixture per
predicate at definition time.

**Addition 1 — region-facing intervals MUST count toward `i(Π)`.** This is the actual fix, and it is
cleaner than bounding total consumption. W1 broke precisely because
`base_interface.counts_toward_i_of_pi = false`. Require the accounting identity

`perimeter = exposure + Σ(all internal arcs, cell-to-cell AND cell-to-region)`

with **every** internal arc counted in `i(Π)`. Then if each arc is `≤3` the original
`20 − 3·3 = 11` is restored *by the original argument*, with no new length bound needed. The cost is
that the shell theorem must now deliver a cell with `i(Π) ≤ 3` counting both kinds — a stronger
demand on the theorem, but a sound one.

**Addition 2 — bound the per-cell interval COUNT, not only interval length.** Length-classification
alone is insufficient: a cell contributing four ordinary intervals of length 3 to regions has every
interval correctly classified "ordinary realized ≤3" and still consumes 12, breaking Greendlinger by
**count** rather than by length. BRG4 must therefore constrain how many region-facing intervals a
single cell may carry — which is exactly what Addition 1 enforces once they are inside `i(Π)`.

### Recommended cheap pre-check before building the classifier

Note that if **all** arcs of a ≥3-cell region are `≤3`, case (E) is harmless under Addition 1 — only
the count matters. So the dangerous sub-case is narrow: **does there exist a `G_3` region incident to
≥3 rank-4 cells in which some cell contributes an arc of length ≥4?**

That is a targeted search, not the full classifier: enumerate triples of arcs with at least one of
length ≥4, with bounded connectors, and test `γ₁c₁γ₂c₂γ₃c₃ =_{G_3} 1` against the verified structure.
**Zero hits collapses BRG4 to the count fix and needs no new bound at all.** This is the same
falsify-before-prove ordering that produced §1's receipt, and it is much cheaper than building the
four-bucket gate blind.

**Disposition unchanged:** rung 4 `#status/proven`-flagged, flag scoped to residual (E) / BRG4.

---

## 7. BRG4 pre-check prereg v0.1 — F1/F2/F3 ruling: ALL THREE OPEN → SCREEN label

Math-expert's refusal to authorize v0.1 as a logically complete pre-check is **correct**. I rule all
three scope items open, so the strong repair is unavailable and Delta runs under the SCREEN label.

**F3 — OPEN, and not repairable as derived.** The certified constant is a *geodesic-bigon*
fellow-travel bound: two geodesics with common endpoints stay within 10. A connector is a path between
consecutive R-cell arcs on a region boundary — a different object, and the substitution is unargued.
Worse, it is not a parameter at all: with unbounded connectors **every triple closes trivially**
(`c₁ = c₂ = 1`, `c₃ = (γ₁γ₂γ₃)⁻¹`). So the answer is determined entirely by `B_connector`, and the real
content is *how large a base region can be in a minimal diagram* — an unproven lemma, not a search
bound.

**F1 — OPEN. No reduction theorem, and I do not believe one exists.** An arbitrary `k`-arc region
satisfies only `γ₁c₁…γ_kc_k =_{G_3} 1`; nothing merges `k = 4` into the registered triple form, since
merging two arcs produces something that is not an arc of a single cell. Zero hits on `k = 3` therefore
says nothing about `k ≥ 4`. The obstruction is structural: the residual's content is **region size**,
which no fixed-`k` form captures.

**F2 — OPEN, and it is exactly the case my countersign correction was about.** Requiring three
*distinct* abstract cell slots misses a region whose boundary alternates `Π, Π′, Π, Π′` — one cell
contributing several arcs to one region. That is the interval-COUNT consumption case (Addition 2): four
length-3 intervals on one cell consume 12 with every interval correctly classified "ordinary ≤3".

### Consequence

**The pre-check cannot collapse BRG4 regardless of outcome.** So it should not be run at the registered
scale: `63,784,000,000 × 118,097` is an exhaustive-search budget spent on a screen.

### If it runs as a screen, reshape the domain first — two free reductions

1. **Dedup the arc descriptors: 4000 → 800.** Each `p⁵` has period 4, so it has only **4** distinct
   cyclic subwords per length, not 20. Distinct arcs = 5 periods × 2 signs × 4 starts × 20 lengths =
   **800**. (Verified: my §1 run found exactly 640 for the 16 lengths 4..19 = 40 per length.) The
   registered 4000 counts `(start, length)` descriptors with a 5× duplication. **125× off the triple
   count: 6.4×10¹⁰ → 5.1×10⁸.**
2. **Connectors are `G_3` elements, not free words** — the radius-10 ball has **50,613** elements, not
   118,097 (2.3×). And for a screen, drop `B_connector` to 2–3: the radius-3 ball is ~50, which with
   meet-in-the-middle on `NF(γ₁c₁)` puts the whole screen near `10⁹` — genuinely runnable.

### The strong repair needs exactly one lemma

**A bound on base-region size in a minimal relative diagram.** That single statement subsumes F1 (it
bounds `k`) and F3 (it bounds connectors). Without it there is no exhaustive domain to register, and
with it the enumeration becomes well-posed. That is the object to send to ideation — not a wider
triple scan.

---

## 8. W-BRG4-0 — NOT the hazard class. Free-cancellation degeneracy.

```
closure word            : AAAABBbbA  (9)
freely reduces to       : AAAAA = A^5  (5)
freely reduced as a path: NO
backtrack               : position 5, "Bb", spanning g3 -> c3
cyclic wrap             : A|A, no cancellation
```

The connector `c₃ = 'bbA'` **immediately doubles back over the arc it just left** (`γ₃ = AABB` ends
`BB`; `c₃` starts `bb`). The region's boundary circuit therefore contains a spur. Any van Kampen
diagram may be taken spike-free without changing the boundary word or increasing area, so region
boundary paths in a reduced diagram are freely reduced — **this configuration is not a diagram
configuration.**

Note also the closure is achieved through the **rank-1 relator `a⁵`**, not a deep `G_3` relation.

**Consequence: the routed conclusion "the ≥3-cell residual class is POPULATED" is not established.**
The screen produced an artifact, not a configuration. The class may still be populated — this witness
does not show it.

**Required filter before the screen means anything:** the closure word must be freely reduced as a
**cyclic** path, i.e. no backtrack at any arc↔connector junction nor at the wrap. This *prunes* the
domain, so it is a free reduction in cost, not an addition. Add a diagnostic recording which relator
class the region's boundary reduces to: hits closing through short rank-1/rank-2 relators are a
qualitatively different population from hits needing deep `G_3` relations.

**Second check owed:** `γ₁` and `γ₂` have **identical descriptors** `(A,+,start0,len1)`. Either they
are the same physical cell — which v0.2 declares excluded — or two cells sharing an arc descriptor.
The receipt must say which.

**Pattern, third instance.** The ℓ=6 collision generator fired on empty NFs; W1 hung on
`counts_toward_i_of_pi = false`; this fires on a spur. **A generator that admits degenerate objects
produces artifacts, not evidence** — degeneracy exclusions belong in the generator, specified before
the run, alongside the cardinality pre-registration.

Extends [[2026-08-07-b25-W1-connected-shell-verdict]],
[[2026-08-07-b25-rung5-definition-gates-preruling]].
