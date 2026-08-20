---
title: "Kourovka 20.115 post-block three-route portfolio"
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

# Post-block strategy portfolio

## Locked target and completed exclusions

- Scope/revision: `20.115/nonzero-character-order-divisibility`, revision 1.
- Exact universal target: for every finite group `G`, ordinary
  `chi in Irr(G)`, and `x in G`, exact `chi(x) != 0` should imply the exact
  integer divisibility `o(x)chi(1) | |G|`.
- The May-2026 paper is partial. **Cited — G. Malle, G. Navarro, and
  P. H. Tiep, _Zeros of characters and orders of elements in finite groups_,
  arXiv:2605.04513v1 (2026):** Theorem B reduces the universal target to
  Condition (1.1) on all triples `(*)`; Theorems C/D and Section 4 cover proper
  prime/family regions, not the universal target.
- Do not repeat the complete ordinary-table scan of `L4(3)`, the faithful
  outer-class scans of `2.L4(3).2_2` and `2.L4(3).2_3`, or the replicated
  `L4(3)` prime-2 block bridge. The last supplies only the 2-part of
  Condition (1.1) for triples with derived subgroup `L4(3)`.
- Failure of `(double-dagger)` or `(double-dagger-star)` is failure of a
  sufficient block route only. It is not a counterexample to the source.

The fixed paper artifact used below is `/tmp/2605.04513v1.pdf`, SHA-256
`a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`.
Planning statements not explicitly attributed to that paper or to installed
CTblLib metadata are **general knowledge, unverified** and remain gates for a
solver and Validator.

## Rank 1 — `R5-SU35-DIRECT` — selected

**Mode and direction.** Counterexample-oriented, direct source-predicate scan
of one new ordinary table.

**Exact object.** Freeze `CharacterTable("3.U3(5)")`, intended to be the
simply connected group `SU_3(5)` of order

```text
5^3 (5^2-1)(5^3+1) = 378000,
```

with center of order `3` and simple quotient `U3(5)`. This identity is a
prerequisite, not something to infer from the short table name. Installed
CTblLib 1.3.7 metadata in `dlnames/uctype2A.g` labels exactly `3.U3(5)` as
type `2A`, rank parameter `l=2`, field parameter `q=5`, and isogeny type
`sc`; it separately labels `U3(5)` as `simple` and `U3(5).3` as `ad`.

**Paper nonduplication gate.** **Cited — Malle--Navarro--Tiep (2026):**

- The defining prime `5` is in Corollary 4.2/Theorem D.
- The prime `2` is in the consequence following Proposition 4.17 because
  `n=3` is odd.
- Theorem 4.3 covers the other odd cross-characteristic primes except the
  critical prime `3`, since `3 | gcd(3,5+1)`.
- Proposition 4.16 treats the linear `SL_n(q)` Coxeter case, not this unitary
  case. The paragraph following it names restriction/extension control for
  `SU_n(q)` as missing. Proposition 4.17 treats `GU_n(q)`, not the
  simply connected `SU_n(q)` table frozen here.

Thus the novelty is the critical `3`-part, although the computation must test
the full integer source predicate so that any hit is an actual source
counterexample candidate.

**Exact observable.** After the identity and ordinary-table gates, enumerate
every `chi_i in Irr(t)` and every conjugacy-class column `C_j`, using exact GAP
cyclotomic equality and exact class-representative orders, and emit precisely
the pairs satisfying

```text
chi_i(C_j) <> 0 and Size(t) mod (chi_i(1)*Order(C_j)) <> 0.
```

Also emit total row count, class count, total grid size, exact nonzero count,
and violation count. No floating approximation and no replacement by a block
criterion is admissible.

**Prerequisites.** GAP 4.12.1 and CTblLib 1.3.7 are installed; the local
metadata explicitly contains the named simply connected table. The solver
must still check `IsOrdinaryTable`, group order, class orders, degree-square
sum, center/quotient identification, and the distinction among `3.U3(5)`,
`U3(5)`, and `U3(5).3`. No heavy slot is expected for a single stored table.

**Success certificate.** Preserve the frozen GAP script, raw output, software
versions, script/output hashes, table identifier and provenance, order, row and
class counts, all exact nonzero/violation totals, and the complete deterministic
record for every hit: row/class indices and labels, degree, class order, exact
cyclotomic value, product, and nonzero remainder. A hit also needs the six-row
canonical constraint-and-conclusion matrix. A zero-hit certificate states only
complete bounded coverage of this one ordinary table.

**Active cost and hard kill.** At most 25 active minutes: five for paper and
identity gates, five for a frozen exact scan, and fifteen for audit/certificate
packaging. Kill by minute 7 if the table cannot be identified as the ordinary
table of the simply connected group with exact order and center. Kill as a
duplicate if the paper gate finds a result covering the critical prime `3` for
this object. Otherwise stop after this single table, hit or zero; do not add
`U3(5)`, `U3(5).2`, `U3(5).3`, or any cover/extension table. If runtime
unexpectedly approaches 60 seconds, stop and request a lease rather than
silently turning it into heavy compute.

**Falsification/self-critique.** The most likely outcome is zero hits, which
has narrow reach. Library identity or provenance may also fail the required
reconstruction gate. Neither outcome addresses the universal quantifier.

## Rank 2 — `R6-CENTRAL-HEIGHT-STAR-U35`

**Mode and direction.** Proof-oriented modular/block bridge, using the
nontrivial central `3`-subgroup rather than direct character values.

**Proposed lemma.** **General knowledge, unverified:** let `B` be a `p`-block
of a finite group `L`, with defect group `D`, and let
`Z <= Z(L)` be a central `p`-subgroup (hence contained in a defect group).
If `theta in Irr(B)` has height `h(theta)`, then exact block-defect arithmetic
should give

```text
(|L:Z|/theta(1))_p = |D/Z| / p^h(theta).
```

Consequently `(double-dagger-star)` for `B` is equivalent to the height bound

```text
p^h(theta) <= |D/Z| / exp(D/Z)  for every theta in Irr(B).
```

The first solver observable would be a line-by-line derivation of this identity
from the definition of block defect and character height; it needs Validator
review before use.

**Exact finite application.** Take `L=SU_3(5)=3.U3(5)`, `p=3`, and
`Z=Z(L)=C3`. Reconstruct every ordinary 3-block, its character heights, an
explicit defect group `D`, and `exp(D/Z)`, then check the displayed height
bound for every block. If every block passes, **cited — Malle--Navarro--Tiep
(2026), Proposition 3.2** would transfer the 3-part of Condition (1.1) to all
triples `(*)` with derived subgroup `L`, a strictly broader conclusion than
the one-table direct scan.

**Certificate.** A written central-height lemma; exact ordinary and 3-modular
table identifiers; full block membership and heights; an explicit matrix or
permutation model of `SU_3(5)` with its central `C3`; defect-group generators,
orders, quotient orders and quotient exponents; every height-threshold row;
and the exact Proposition 3.2 implication with all `(*)` hypotheses retained.

**Prerequisites and hard kill.** The ordinary table is locally named, but the
availability of a reconstructible 3-Brauer decomposition and explicit defect
representatives is not yet established. Budget 35--45 active minutes. Kill at
minute 8 if either block membership or explicit defect representatives cannot
be obtained from sanctioned installed data. Kill on the first failed height
bound and report only failure of this sufficient bridge. Do not infer a source
counterexample and do not reimplement block algorithms.

**Falsification/self-critique.** A critical block may have height too large for
the quotient exponent threshold even though all of its offending characters
vanish on large-order 3-elements. The central-height identity can be useful
while its application fails; explicit defect-group identification is the main
tooling risk.

## Rank 3 — `R7-SU3-COXETER-3-FAMILY`

**Mode and direction.** Symbolic nearly-simple family proof, replacing table
enumeration by a value-support statement.

**Exact family.** Let `q>2` be a prime power with `q == -1 mod 3`, let
`L=SU_3(q)`, set `H=L`, and work only at `ell=3`. Focus on the characters in
the first Coxeter-torus exceptional shape isolated by Corollary 4.13 and
Remark 4.14. For `n=3`, the second two-factor shape cannot occur because both
positive dimensions `n1,n2` would be powers of `3` greater than one and hence
sum to at least six. This route does not claim anything about arbitrary outer
extensions of `L`.

**Proof observable.** Produce an exact unitary rank-two value-support lemma:
for every faithful critical constituent `theta in Irr(L)` under the relevant
Coxeter Deligne--Lusztig character and every `h in L`,

```text
theta(h) != 0  =>
o(h Z(L))_3 divides (|L:Z(L)|/theta(1))_3.
```

The first gate must compute the right-hand 3-part exactly from the character
degree formula. The proof should then give a symbolic conjugacy-class
parametrisation and an exact vanishing/value formula on every class whose
3-part exceeds that bound.

**Why it might work.** **Cited — Malle--Navarro--Tiep (2026), Corollary 4.13,
Remark 4.14, Proposition 4.16, and the following paragraph:** this is the
unitary analogue of the paper's first exceptional Coxeter shape, and the
missing step concerns restriction/extension information. **General knowledge,
unverified:** fixing `H=L` and rank two may permit an explicit `SU_3(q)` class
and Green-function calculation without developing the disconnected-group
machinery needed for arbitrary automorphisms.

**Certificate.** A parameter-complete lemma for all stated `q`, an exact list
of critical character parameters and class types, the degree/codegree
calculation, exact character-value or vanishing formulas, and a clause matrix
showing that only `H=L` and the prime `3` are covered.

**Prerequisites, cost, and hard kill.** This requires a citable exact
`SU_3(q)` character-value/restriction formula, which is not supplied by the
local May-2026 paper artifact. Budget 40--45 active minutes for a source/formula
gate and one rank-two derivation. Kill at minute 12 if the exact formula cannot
be sourced locally or reconstructed in a short self-contained calculation.
Do not start a general disconnected Lusztig-restriction program.

**Falsification/self-critique.** Restriction from `GU_3(q)` may split the
critical character in a way that destroys a uniform support formula; this is
close to the paper's explicit bottleneck. The missing local formula makes this
high-reach route less executable than the two finite routes.

## Recommendation and exact handoff

Select exactly `R5-SU35-DIRECT` for one at-most-25-minute solver increment.
Do not authorize `R6` or `R7` concurrently. `R5` has installed exact ordinary
data, attacks the only paper-residual prime for this fixed simply connected
group, and evaluates the source predicate itself. If it returns zero hits,
record only the named-table partial result and return to Lead before choosing
another route.

## This MathExpert session

No character values, class orders, block data, defect groups, or divisibility
predicates were computed. Work was limited to reading the fixed paper and prior
review artifacts and inspecting installed CTblLib naming metadata.
