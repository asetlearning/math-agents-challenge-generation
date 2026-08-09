---
title: Relative-asphericity central-extension tower + H² spectral sequence — admissibility pre-ruling
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "The per-rung relative-asphericity schema with z_i-differential handle is admissible and the homological handle changes the Gap-1 situation."
claimant: Maria (proposal) / Lead (routing)
verification_method: admissibility-boundary application + oracle-regress analysis
tools_used: []
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, doctrine]
---

# Relative-asphericity tower — admissibility pre-ruling

## (1) Schema ADMISSIBLE in shape; the oracle requirement is sharper than PB4-R's

Relative asphericity is a legitimate per-rung target — a statement about the extension
`G_{L-1} → G_L`, uniform in `L`, with the generating set of spherical pictures (band-dipoles, caps,
annuli) as the per-rung data and `n` free to live in the constants. **Admissible under (B).**

**What the per-rung check must consume, exactly:** a **decision procedure for the word problem in
`G_{L-1}`**. Pictures must be identified, and dipole cancellation detected, and both require deciding
equality in the base. A full automatic structure is *not* needed — a Dehn-type algorithm suffices,
since the pictures at issue are finite with bounded complexity.

**But the regress is NOT automatically closed, and this is the difference from PB4-R.** PB4-R was
self-sustaining because the rung-4 curvature step delivered a *strict Dehn condition*, which yields the
algorithm directly. **Relative asphericity does not, by itself, produce a word-problem oracle** —
asphericity controls π₂ / the relation module, not the word problem. So:

> The per-rung target must be **asphericity *plus* a decision procedure**, and the proposal must say
> which of two routes supplies the latter.

- **Route A — curvature-based asphericity.** The asphericity proof goes through a curvature condition
  strong enough to give a Dehn algorithm. Then the tower self-sustains — **but it inherits the Dehn
  margin, which is `2ℓ+3` against `2.5ℓ` and dies at `ℓ = 6`.** Named obstruction, already measured.
- **Route B — non-curvature asphericity.** No oracle is produced, and Gap 2 regresses at every rung.

Either route carries a named obstruction. **Declaring which route is Claim-1 work, not development
work.**

## (2) The {3,4,6} controls are purely NEGATIVE here — state that before anyone runs them

At the known-finite exponents the towers stabilize **because the groups are finite**. So any correct
invariant will show stabilization at 3, 4, 6 — that outcome is *forced* and carries no information.

> **The controls can only refute an ingredient that wrongly predicts non-stabilization at 3, 4 or 6.
> They cannot corroborate one that correctly predicts non-stabilization at 5.** Necessary, not
> sufficient.

**Required evidence-shape**, satisfying the pre-declared-ingredient rule:

1. **Name `I(n)`** — an invariant of the `z_i`-differential system — *before* computing anything.
2. **Compute `I` at n = 3, 4, 6.** `I` must predict stabilization at all three. Any non-stabilization
   prediction refutes the ingredient against Burnside (1902), Sanov (1940), Hall (1958). **n = 3 is the
   discriminating control**, being odd: an ingredient that is really just parity survives 4 and 6 and
   dies here.
3. **The load-bearing test — substitution.** Take the `n = 5` non-stabilization argument, substitute
   `I(3)` for `I(5)`, and **confirm the argument breaks**. That is the only way to show `I` is
   load-bearing rather than decorative, and it is "failure for the right reason" run in reverse.

## (3) The handle is NOT a re-dressing — but the gain is narrower than it will look

**It does not evade Gap 1.** The uniform claim persists; it *relocates*, from "every per-rung picture
check passes" to "the spectral sequence degenerates / the `z_i`-differentials behave thus". That is
still a uniform statement, so the harness applies to it and it must fail at {3,4,6}.

Maria's own flag is the sharpest form and should be kept in the front matter: **picture-stabilization
at the limit is Shunkov-equivalent to finiteness.** So the convergence statement is *equivalent to the
theorem*. The handle therefore cannot be a shortcut to the limit.

**The real difference, and it is real:** the relocated claim changes shape from *geometric-per-rung* to
*algebraic-per-page*, and `n` enters **explicitly through the `z_i`**. A differential-vanishing
statement about a finitely generated object per page is a far more natural home for an `n`-dependent
constant than a geometric picture condition is. Under (B) the whole requirement is that `n` live in the
constants — so the handle is worth having **if and only if** the `n`-dependence can be localized in the
differentials.

**Decisive test of the value proposition:**

> Can the `n`-dependence be exhibited as a property of the `z_i` themselves, computable at
> n = 3, 4, 5, 6? If yes, the handle earns its keep. If the `n`-dependence has to be re-imported from
> the geometry, it is a re-dressing and the proposal reduces to the routes already ruled.

## AMENDMENT (2026-08-09) — the `z_i` cocycle property is itself unsourced

Researcher's opened-paper pass reports that `kuznetsov-safonov-2018` contains **zero**
cocycle / cohomology / central-extension content: the "Kuznetsov Hall-polynomial cocycles" framing is
Maria's interpretation layered on the papers' Hall-form polynomials, not a result either paper states.
(`kuznetsov-kuznetsova-2013` not re-opened this session — flagged, not asserted.)

**This changes my §3 test, which presupposed the `z_i` were differentials.** If the cocycle property is
interpretation rather than citation, then there are no differentials to name `I(n)` on until it is
established. So the value proposition has a prerequisite in front of it:

> **Prove the `z_i` are cocycles for the relevant central extension.** Until that holds, the spectral
> sequence has no differentials, `I(n)` has nothing to be an invariant of, and the algebraic-per-page
> relocation that is the handle's *entire* claimed advantage does not exist.

This is a prerequisite to Claim-1, not part of it, and it is the cheapest possible thing to settle
early: either the cocycle identity holds for these polynomials or it does not.

## Day-one gate (amended)

No ideation spend past Math-expert's Claim-1 check until **all three** are named:

1. the `z_i` cocycle property is **established, not cited** (see amendment above);
2. which route — A (curvature-based, inherits the ℓ=6 Dehn death) or B (no oracle, Gap-2 regress) —
   supplies the word-problem oracle;
3. the invariant `I(n)`.

Naming these is cheap; discovering them late costs the round. Item 1 now precedes the other two,
because items 2 and 3 are both stated in terms of an object item 1 must first supply.

Extends [[2026-08-07-b25-admissibility-boundary-doctrine]].
