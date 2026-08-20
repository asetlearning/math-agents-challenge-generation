---
title: "Kourovka 20.115 post-stale three-route portfolio"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
---

# Post-stale strategy portfolio

## Locked target and obstruction

- Scope/revision: `20.115/nonzero-character-order-divisibility`, revision 1.
- Exact target: for every finite `G`, ordinary `chi in Irr(G)`, and `x in G`,
  `chi(x) != 0` should imply `o(x)chi(1) | |G|`.
- Excluded: modular or reducible characters, zero rows, the solvable case, the
  fourth/fifth-power bound, and any bounded screen advertised as universal.
- **Cited — Malle--Navarro--Tiep, arXiv:2605.04513v1 (2026):** Theorem B reduces
  the target to Condition (1.1) on triples satisfying `(*)`; Theorems C/D and
  later propositions cover named proper cases. Corollary 4.13 gives an exhaustive
  exceptional-shape statement only for primes greater than five. Proposition 4.16
  handles part of its first linear Coxeter-torus shape. The paper names
  disconnected-extension Lusztig restriction as a remaining bridge.
- Obstruction: the general route needs character-extension/restriction control that
  is unavailable. A direct finite residual can still give an exact target witness or
  bounded positive coverage. Nothing below asserts that the Corollary 4.13 shapes
  exhaust the unresolved cases at primes `2,3,5`.

Mathematical planning statements not explicitly attributed to the paper below are
**general knowledge, unverified** and are gates for the solver/Validator, not
certifications.

## Rank 1 — `R1-L43-DIRECT` (selected)

**Mode:** counterexample-oriented exact residual nearly-simple case.

**Idea.** Screen exactly the ordinary table `CharacterTable("L4(3)")`, interpreted
after an identity gate as `PSL_4(3)`, against the active predicate. Restrict the
novelty analysis to the prime `2`, but evaluate the full integer divisibility so any
hit is an actual source counterexample candidate, not a failure of `(double-dagger)`
or `(double-dagger-star)`.

**Why this is nonduplicative.** **Cited — Malle--Navarro--Tiep (2026), Theorem 4.3
and the paragraph after Proposition 4.17:** the cross-characteristic theorem is
stated for `ell>2`, while the stated `ell=2` consequence for groups of type
`SL_n(epsilon q)` assumes `n` odd or `q` even. The boundary `n=4,q=3` has neither
property. Before computation, recheck that no other proposition or exceptional
isomorphism in the paper disposes of this simple quotient. The earlier 20.115 agent
stopped at the staleness gate and ran no table screen.

**Target observable.** For every exact ordinary row `chi_i` and class `C_j`, record
whether

```text
chi_i(C_j) != 0  and  Size(table) mod (chi_i(1)*Order(C_j)) != 0.
```

GAP cyclotomic equality, not a floating approximation, decides nonvanishing. The
first gate also checks the table identifier, ordinary status, group order, class
orders, and that the intended group is centerless/simple; do not infer these merely
from the short name.

**Prerequisites available.** A read-only environment probe found GAP `4.12.1`,
Debian `gap-character-tables`/CTblLib `1.3.7`, and installed metadata explicitly
listing `L4(3)`. This should be a sub-minute, non-heavy job; no compute lease is
needed unless the actual command unexpectedly approaches 60 seconds.

**Active-time cost.** 15--20 minutes: 5 minutes for coverage/identity gates, 5 for
the exact scan and deterministic output, 5--10 for certificate packaging.

**Success certificate.** Preserve the GAP script and raw output; GAP/CTblLib
versions; table identifier and order; row/class counts; exact row and class labels;
degree; representative order; exact cyclotomic value; product and remainder; and a
hash of the output. A hit also needs the six-row active constraint matrix. Zero hits
mean only complete coverage of this named finite table (and, after the paper-coverage
gate, its residual `2`-part), never a universal proof.

**Hard kill.** Kill as duplicate if the five-minute paper gate finds this case is
already covered. Kill at ten minutes if the table identity or exact ordinary data
cannot be reconstructed. Otherwise stop after this one table, whether the result is
a hit or zero hits; do not widen into a catalogue.

**Most likely failure.** The table has no violating pair. That still yields a compact
partial result, but its mathematical reach is one simple group.

## Rank 2 — `R3-L43-GRAPH-EXTENSIONS`

**Mode:** bounded computational alternative, changing the target from the base
simple table to outer-coset extension data.

**Idea.** Audit only those installed central-cover extension tables among
`2.L4(3).2_2` and `2.L4(3).2_3` whose table metadata and fusion maps certify a
non-semilinear index-two extension with derived subgroup `2.L4(3)` and unchanged
center. Exclude `L4(3).2_1` at the outset: local metadata labels it `PGL(4,3)`, so it
has an immediate duplication risk with Proposition 4.17's `GL_n` result. Recheck
paper coverage for every retained table before scanning.

**Target observable.** Use the certified fusion from the derived subgroup to isolate
outer classes `C`. For every faithful ordinary `chi` with exact `chi(C) != 0`, check
the direct active integer predicate `Order(C)*chi(1) | |H|`. Separately record the
quotient/center data proving that an outer representative generates `H` with the
derived subgroup. Do not report failure of Condition (1.1) alone as a source
counterexample.

**Prerequisites available.** GAP/CTblLib and AtlasRep are installed; local CTblLib
documentation lists the two cover-extension identifiers. Exact subgroup fusion,
center, derived-subgroup, and character-kernel data remain prerequisite gates.

**Active-time cost.** 25--35 minutes, no heavy slot expected.

**Success certificate.** Script/output/version hash, exact table and fusion IDs,
structural checks for `(*)`, outer class label/order, faithful character kernel,
exact cyclotomic value, degree, and integer remainder. A zero-hit certificate is
limited to the audited outer cosets in the retained named tables.

**Hard kill.** Stop at ten minutes if table fusions do not reconstruct the extension
and outer cosets, or if paper coverage makes the retained table duplicative. In all
events stop after the two named identifiers; do not add other automorphism groups.

**Most likely failure.** Table names alone may not certify all structural rows, and
a zero-hit result still covers only two finite extensions.

## Rank 3 — `R2-L43-BLOCK-BRIDGE`

**Mode:** proof-oriented residual bridge.

**Idea.** Attempt the finite lemma that every `2`-block of the centerless simple
group represented by `L4(3)` satisfies `(double-dagger)`. **Cited —
Malle--Navarro--Tiep (2026), Proposition 3.2:** for a centerless derived subgroup,
that block statement would imply Condition (1.1) at `2` for every triple `(*)` with
that derived subgroup. This would cover more than one table and is distinct from a
row-by-row active-predicate scan.

**Target observable.** Produce one row per `2`-block `B`, an explicit defect group
`D_B`, its exact exponent, and the minimum `2`-defect of characters in `Irr(B)`;
check `exp(D_B) <= 2^def(chi)` for every row in `B`.

**Prerequisites available.** CTblLib and AtlasRep are installed, and AtlasRep local
metadata lists a degree-40 permutation representation for `L4(3)`. The missing
gate is whether the environment supplies a reconstructible `2`-block partition and
explicit defect-group representatives rather than only defect orders.

**Active-time cost.** 35--40 minutes if the prerequisite gate passes. Request a
heavy-compute lease before any subgroup calculation forecast above 60 seconds.

**Success certificate.** A written finite lemma plus exact table/block identifiers,
permutation generators, defect-group generators/order/exponent, every character
degree and defect inequality, and the explicit Proposition 3.2 implication.

**Hard kill.** Stop after eight minutes if exact block membership and defect-group
representatives are unavailable. Stop immediately on one violated exponent bound:
that kills only this sufficient bridge and is not evidence against the active
conjecture. Stop rather than reimplement block algorithms or begin a disconnected
Lusztig program.

**Most likely failure.** Ordinary tables need not determine defect-group exponents,
and the sufficient block inequality may fail even where the source conjecture holds.

## Recommendation and exact handoff

Run `R1-L43-DIRECT` only. It is the sole route whose target data are already present,
whose negative/positive output has a reconstructible meaning, and whose direct
predicate avoids the sufficient-condition trap. The first experiment is one frozen
`L4(3)` manifest and an exact all-row/all-class scan, with a hard stop at 20 active
minutes. If its identity/coverage gate fails, do not improvise: return to Lead and
consider `R3-L43-GRAPH-EXTENSIONS`. Do not close 20.115 on any zero-hit outcome.

## Environment evidence (no problem computation)

- `gap -q -c 'Print(GAPInfo.Version,...)'` reported `4.12.1`.
- Package metadata reported `gap-character-tables 1.3.7-1` and AtlasRep `2.1.8-1`.
- Read-only searches of installed metadata found `L4(3)`, its three index-two
  extension labels, and the two named central-cover extension tables.
- No character values, class orders, block data, or divisibility predicates were
  computed in this MathExpert session.
