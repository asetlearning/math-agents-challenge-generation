---
title: "Uniform Step Audit — G4 Period-Band Machinery"
date: 2026-08-04
domain: group-theory
project: b25
instance: b25-infinite-witness
author: maumayma
status: draft
tags: [agent/math-expert, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/burnside-infiniteness, topic/small-cancellation, topic/uniformity, project/b25, status/draft]
---

# Uniform Step Audit — G4 Period-Band Machinery

This note audits whether the certified G4 proof can become a uniform inductive
step

`E7 survives G_L => E7 survives G_{L+1}`

with constants independent of `L`.

Scope discipline: this note does not re-prove the G4 rung. The G4 result is
settled in [[assembled-proof]] and [[e7-survives-g4-2026-08-03]]. This audit
asks which G4 constants survive when the new periods have length

`ell = L+1`

and the new relators have length

`N = 5 ell`.

Reading sources used:

- [[b25-infiniteness-methodology-index]]
- [[assembled-proof]]
- [[b25-infiniteness-results-synthesis]]
- [[2026-08-04-b25-uniform-step-audit-gate]]: Validator audit gate;
  arithmetic replicated, package still conjectural.
- [[uniform_literal_period_profile_summary_20260804T120001Z]]
- data receipts cited there, especially [[setup_and_orientation_receipt]],
  [[cancellable_pair_receipt]], and [[cap_conjugator_receipt]]

## Executive Verdict

The G4 machinery is not uniform as written. The main obstruction is the
ordinary-piece constant.

At G4, `ell=4`, relator length is `20`, and the piece bound is `3`, so

`3/20 < 1/6`.

For general `ell`, the naive worst-case literal overlap between two distinct
length-`ell` periods is `ell-1`. Then

`(ell-1)/(5 ell) -> 1/5 > 1/6`.

The strict `C'(1/6)` core therefore fails asymptotically. More sharply,

`ell-1 < (5 ell)/6`

holds exactly for `ell < 6`. Thus this arithmetic still allows `ell=5` but
breaks at `ell=6` if the actual distinct-period piece profile is `ell-1`.

This is a real obstruction unless one of the following is true:

1. in `G_L`, genuinely new length-`ell` periods have sublinear realized
   overlaps;
2. large-overlap period pairs are not both genuinely new because one fifth
   power is already trivial in `G_L`;
3. large-overlap pairs can be grouped into a larger "period family" with a
   cancellable-pair/band theorem replacing ordinary `C'(1/6)`;
4. the proof abandons classical `C'(1/6)` and uses a graded contiguity theorem
   with different curvature accounting.

The most valuable uniform target is therefore not the cap or annulus constant.
It is a uniform separation theorem for genuinely new periods, or a replacement
for `C'(1/6)` that tolerates overlaps of order `ell`.

## Constant Audit Table

| Constant / object | G4 value | Exact role in assembled proof | L-dependence verdict | What would make it uniform |
| --- | ---: | --- | --- | --- |
| New period length | `ell=4` | Root length; relator perimeter is `N=5ell` | Linear by definition | Harmless; all inequalities should be written in ratios relative to `ell` or `N` |
| Relator perimeter | `N=20` | Cell perimeter for Greendlinger and strict-arc complement | Linear: `N=5ell` | Harmless if piece ratio is uniformly `<1/6` of `N` |
| Distinct-period piece bound | `<=3` | Supplies realized-piece `C'(1/6)` after same-period bands vanish | **Main nonuniform risk.** Naive worst case is `ell-1`; ratio tends to `1/5` of relator length, above `1/6` | Prove actual `G_L` realized pieces for genuinely new periods satisfy `P_ell <= (5/6 - eps) ell`, preferably `O(1)`; or replace C'(1/6) with a large-overlap period-family theory |
| Same-period band threshold | `>=4=ell` | Contacts containing a full period block are sent into the band/cancellable-pair system | Linear: threshold should be `>=ell` | Uniform as a definition if ordinary contacts `<ell` still satisfy the C'(1/6) ratio; otherwise threshold alone is not enough |
| Cap length | `<=3=ell-1` | Phase caps between rotated period coordinates | Linear; cap census grows exponentially in `ell` if brute-forced | Replace finite cap census by algebra: `E(p)=<p>` plus root-primitivity forces canonical rotation caps |
| Orientation theorem SO | No self-inverse/cross-inverse among five periods | Ensures long same-period contacts are opposite-oriented, enabling cancellable pairs | Literal self-inverse obstruction is absent at reachable lengths checked so far. Validator notes no cyclically self-inverse cyclically reduced words for `ell<=6` by abelianization; Delta extends literal zero self-inverse/cross-inverse through `ell=10`. Group-level inverters are still part of `E(p)=<p>` | Choose period classes modulo cyclic shift/inverse; include explicit "no genuinely new period is cyclically self-inverse"; prove no `G_L` inverter through `E(p)=<p>` |
| Aligned cancellable-pair contour | All aligned opposite contacts length `4..19` cancel | Kills aligned same-period bands of any topology while preserving the external boundary | **Validator-certified PROVEN UNIFORM THEOREM.** For any `ell`, aligned `p^5`/`p^{-5}` cells sharing any proper contact have inverse outer contours | Requires only opposite orientation and phase alignment; no `ell=4` special input |
| Annulus bound | `B_ann=24` | Excludes same-period annuli via `E(p)=<p>` | Unknown/nonuniform. Natural geometric bounds scale like `O(delta_L + ell)` | Uniform theorem that every new period is maximal elementary in `G_L`, with no roots/inverters; or a uniform hyperbolicity/malnormal-axis bound |
| `E(p)=<p>` | Verified for five periods | Excludes annuli; powers cap absorption; no inverters | Unknown for all new periods | Make it an inductive hypothesis, or prove new periods are primitive/maximal elementary in `G_L` |
| All-powers geodesic axis | Verified for five periods | Gives straight period axes and infinite order; supports annulus/cap logic | Unknown for all L | Inductive "straight new periods" axiom; finite-state or geometric proof that genuinely new length-`ell` periods are straight in `G_L` |
| Cap transporter census | `|c|<=3`, zero exotic | Absorbs phase offsets into aligned coordinates | Brute force is nonuniform (`|c|<=ell-1`) | General cap lemma: if `c rot_k(p)c^-1=p`, then `c u_k^-1 in E(p)=<p>`; with `|c|<ell` and primitive geodesic `p`, only canonical caps survive |
| H2 single-cell caps | Cap length `<ell` | Separates true phase caps from bridges | Uniform as topology after block boundaries are label-determined/canonical | Need block-normalized pocket definitions for all `ell` |
| H2 beaded bridges | Each bead `<=3` at G4 | Beads are ordinary `C'(1/6)` pieces, not band obstructions | Uniform iff ordinary piece bound is uniform in ratio. For general `ell`, bead length bound is the same `P_ell` problem | Same as distinct-piece row: `P_ell < 5ell/6` |
| Internal BR2 contraction | Area drops by pocket compression/deletion | Removes equal-chord internal pockets and preserves the external boundary | Topological part uniform; partly redundant once aligned cancellable pairs are available, but still useful as normalization bookkeeping. Piece ledger depends on piece separation | Uniform if post-compression new contacts obey the same ordinary-piece bound or are re-banded/cancelled |
| Greendlinger exposure | `>=12` at G4 | Produces boundary strict Dehn arc | Formula depends on `P_ell`: exposure `>= 5ell - 3P_ell` | Need `P_ell < 5ell/6`; for E7-specific contradiction, also need no strict `G_L` arc on `E7` |
| E7 strict-arc scan | zero hits length `11..20`; max nonreducing `7/20` | Final contradiction after Greendlinger | Per-level finite check against new relators; not uniform by itself | A uniform proof that `E7` contains no new strict arcs, or note that if exposure threshold eventually exceeds `|E7|_{G_L}`, the contradiction becomes automatic |
| Previous-rung oracle | `G_3` automatic/geodesic structure | Decides geodesics, equality, caps, E7 strict arcs, period straightness | Inherent L-dependence; automatic structure already strained at G4 | Replace "automatic structure" by an inductive certified oracle for only the regular languages used in the proof |
| Number of new periods | Five at G4 | Finite receipts over all genuinely new periods | Grows exponentially in `ell` before quotient/redundancy | Need theorem-level period selection/separation; brute-force per-level checks are not a uniform proof |

## Detailed Findings

### A. Distinct-Period Pieces Are The Central Obstruction

Let `P_ell` be the maximum length of an ordinary realized piece after
same-period aligned bands have been removed.

The G4 proof needs

`P_ell < N/6 = 5ell/6`.

Greendlinger then gives a boundary exposure at least

`N - 3P_ell = 5ell - 3P_ell`.

This is longer than half the relator precisely when

`P_ell < 5ell/6`.

If the actual worst-case distinct-period piece is `ell-1`, then strict
`C'(1/6)` fails from `ell=6` onward:

`ell-1 < 5ell/6  <=>  ell < 6`.

This is exactly Maria/Lead's arithmetic flag. In relator-length units,

`(ell-1)/(5ell) -> 1/5`,

which is bigger than `1/6`.

I regard this as a genuine negative for uniformity of the literal G4 proof.
The remaining caveat is that "literal worst case among all free words" may not
be the same as "realized piece among genuinely new `G_L`-geodesic period
classes." Delta's oracle-filtered profile is therefore now the load-bearing
next input.

Delta's literal/free-level receipt
[[uniform_literal_period_profile_summary_20260804T120001Z]] now answers this
question before any `G_L` filtering: `max_piece = ell-1` is realized for every
`ell=4..10`. The strict `C'(1/6)` inequality holds literally only for
`ell<=5`; it is exact equality at `ell=6` and fails for `ell>=7`.

The receipt also records zero full-block collisions for all `ell=4..10`. That
keeps the same-period band threshold intact, but it does not rescue ordinary
`C'(1/6)`. The critical witnesses are distinct classes with no full block in
common. Sample records have the expected form

`p = s x`, `q = s y`, `|s|=ell-1`, `x != y`,

for example `AAAAAB` versus `AAAAAb` at `ell=6`, sharing `AAAAA`.
Many witnesses are the same one-letter-different phenomenon after cyclic
rotation rather than only literal common-prefix examples.

### B. Orientation Is Mostly Uniform, But Do Not Confuse Two Notions

In a van Kampen diagram, two cells sharing an edge read inverse labels along
that edge. If a full-period same-period contact were same-oriented, a cyclic
rotation of `p` would coincide with a cyclic rotation of `p^{-1}`. The needed
condition is therefore explicit:

`p` is not cyclically self-inverse.

Validator's audit gate reports this as automatic for the reachable `ell<=6`
case by abelianization, and Delta's literal/free-level profile extends zero
self-inverse and zero cross-inverse violations through `ell=10`. Cross-inverse
periods are also eliminated at the period-list level by choosing period
classes modulo inverse. I therefore no longer list literal SO as an independent
uniform hypothesis for the near-term package; it remains a receipt to keep in
the period-profile table.

This does not automatically exclude a group-level inverter in `G_L`, i.e. an
element `x` with `xpx^{-1}=p^{-1}`. That is part of the annulus/elementary
subgroup package. Uniform orientation for literal contacts is easy; uniform
`E(p)=<p>` is not.

### C. The Cancellable-Pair Move Is The Best Uniform Feature

The aligned cancellable-pair theorem is genuinely period-length agnostic.
Validator's audit gate upgrades this from an inductive hypothesis to a
Validator-certified PROVEN UNIFORM THEOREM.

For any cyclic word `p` of length `ell`, an aligned opposite-oriented contact
between a `p^5` cell and a `p^{-5}` cell has inverse complementary contours.
This does not use `ell=4`; it is a formal boundary-word identity. It applies
for every proper contact length `1..5ell-1`, and in particular for every
long contact containing a full `p`-block.

Thus if phases are aligned and orientation is opposite, same-period pockets
vanish uniformly by local area reduction. The move is boundary-preserving:
the complementary contours cancel inside the diagram, and replacing the
two-cell pocket by the area-zero contour leaves the external boundary word
unchanged. BR2 has partial redundancy once this move is available, but BR2
still remains useful as a normalization/compression operation for equal-chord
internal pockets.

The problem is not the aligned cancellation. The problem is proving that all
dangerous large overlaps are either aligned same-period pockets or ordinary
pieces below the `C'(1/6)` ratio.

### D. Annuli And Elementary Subgroups Are Not Uniform Yet

At G4, annuli closed by a finite `B_ann=24` connector check and the conclusion
`E(p_i)=<p_i>` for the five periods. For general `ell`, any hyperbolic
bounded-conjugacy argument will usually have a bound depending on the
hyperbolicity constant of `G_L`, the quasi-axis constants of `p`, and `ell`.
A natural scale is `O(delta_L + ell)`, not an L-independent constant.

The G4 number `24` should not be treated as a universal constant. It is a
receipt for five periods over `G_3`.

What could make annuli uniform:

1. a theorem that every genuinely new period is maximal elementary in `G_L`;
2. a uniform no-inverter/no-root theorem for new periods;
3. a uniform hyperbolicity and axis-malnormality package for the ladder.

Absent that, annulus closure remains a per-level finite check.

### E. Cap Census Becomes Algebraic Or It Does Not Scale

At G4, phase caps have length at most `3`. At general period length `ell`, a
cell-boundary cap has length at most `ell-1`.

Brute force over all caps is then exponential in `ell`. This is not a
uniform proof method.

However the transporter argument itself can be uniform if `E(p)=<p>` is
available. For `p=u_k v_k` and `rot_k(p)=v_k u_k`, the canonical cap `u_k`
satisfies

`u_k rot_k(p) u_k^{-1} = p`.

If another cap `c` satisfies

`c rot_k(p)c^{-1}=p`,

then `c u_k^{-1}` commensurates `<p>`. Under `E(p)=<p>`, it lies in `<p>`.
If `p` is geodesic, primitive, and `|c|<ell`, this should force `c` to be the
canonical cap up to the obvious short axis-power ambiguity.

So the cap part is not the main obstruction. It reduces to the same elementary
subgroup package as annuli.

### F. H2 Beaded Pieces Are Uniform Only In The Piece Ratio

The corrected beaded argument is per-piece. Beaded paths may have many beads;
that does not matter. Each bead must be an ordinary realized piece. Therefore
the beaded part is harmless exactly when ordinary pieces satisfy

`length(piece) < 5ell/6`.

So H2 does not introduce a new independent constant. It inherits the
distinct-piece problem from row A.

### G. The Previous-Rung Oracle Is An Inherent Dependence

The G4 proof uses `G_3` as an ambient certified metric object:

- `E7` normal form is geodesic;
- new periods are geodesic and straight for all powers;
- cap transporters are checked in `G_3`;
- strict Dehn arcs are checked by `G_3` equality/geodesic data;
- annulus connectors are checked in `G_3`.

For an induction, `G_L` must supply the same services. Requiring a full
automatic structure at every level is probably too strong as an engineering
condition; the G4 automatic build already strains tooling. But some certified
oracle is mathematically inherent. The proof is not purely syntactic over the
free group.

A weaker oracle might suffice:

1. equality of pairs in a finite list of regular languages: period powers,
   cap transporters, connector candidates, and `E7` strict-arc candidates;
2. geodesicity/straightness certificates for new period powers;
3. normal form/geodesicity of the protected boundary word in `G_L`.

That is still L-dependent, but it is narrower than "construct a full automatic
structure for `G_L`."

## Arithmetic Chain For A General Step

Let:

- `ell = L+1`;
- `N = 5ell`;
- `P_ell` be the maximum length of an ordinary realized piece after all
  aligned same-period pockets are cancelled and phase caps are absorbed.

The classical `C'(1/6)` input is:

`P_ell < N/6 = 5ell/6`.

Greendlinger gives a cell whose external boundary contains all but at most
three pieces, hence exposure

`E_ell >= N - 3P_ell = 5ell - 3P_ell`.

This is a strict Dehn arc if

`E_ell > N/2 = 2.5ell`,

equivalent to the same condition `P_ell < 5ell/6`.

If `P_ell=ell-1`, then

`E_ell >= 2ell+3`,

which is less than `2.5ell` for `ell>6` and equal to the strict threshold
failure at `ell=6`. Thus the proof breaks exactly where the `C'(1/6)`
inequality breaks.

For E7 specifically, if `P_ell` were bounded independently of `ell`, then
`E_ell` would grow linearly and eventually exceed the fixed boundary length
`|E7|_{G_L}`. In that regime no null diagram could even fit the Greendlinger
exposure. But this optimistic simplification depends entirely on a bounded or
strongly sublinear piece profile.

## Route Analysis 2026-08-04

Delta's literal/free-level curve changes the strategic picture. It gives one
bounded target with real headroom, and one genuine research frontier.

### Track A: Rung 5 By The Existing Method

For the next concrete rung, `ell=5` and `N=25`. The literal profile gives
`P_5=4`, hence

`4/25 < 1/6`.

The integer margin is small but positive:

`ceil(5ell/6)=ceil(25/6)=5`, while `P_5=4`.

Greendlinger exposure would be at least

`25 - 3*4 = 13`,

which is strictly larger than half the perimeter. Thus the G4 method should
still have enough classical `C'(1/6)` room at rung 5 if the `G_4` oracle does
not create longer realized equalities.

The receipts that must be regenerated over `G_4` are:

1. **Base oracle.** A replayable `G_4` equality/geodesic oracle, ideally a
   full automatic/geodesic package, but a targeted oracle for the listed
   languages would suffice for this proof.
2. **Period selection.** Canonical primitive cyclically reduced length-5
   period classes modulo rotation/inversion; record which fifth powers are
   already trivial in `G_4` and which are genuinely new.
3. **Primary redundancy.** The main criterion should be
   `reduce_{G_4}(p^5)=IdWord`. Conjugacy to a prior shorter root is useful
   diagnostic metadata, but it should not replace the direct fifth-power
   test because the prior normal closure can kill `p^5` without exposing the
   obvious root-conjugacy witness.
4. **Straight axes.** For each genuinely new period `p`, certify
   `|NF_{G_4}(p^k)|=5k` for all `k` by a finite automaton/pumping argument,
   not by a bounded scan only.
5. **Realized pieces.** For each genuinely new pair, enumerate all boundary
   arcs of `p^5` and `q^5/q^{-5}`; reduce arcs to `G_4` shortlex normal form;
   group equal normal forms; record the maximum raw boundary arc length
   producing equal `G_4` normal forms. The curvature proof consumes raw
   boundary length, while normal-form length explains whether the oracle
   killed a literal overlap.
6. **Orientation.** Keep the literal self-inverse/cross-inverse receipt. Per
   Validator, this is automatic at the near lengths, but the receipt prevents
   accidental period-list mistakes.
7. **Elementary subgroups and annuli.** Regenerate `E_{G_4}(p)=<p>` or the
   finite connector surrogate for all genuinely new length-5 periods. The G4
   `B_ann=24` number should not be silently reused unless the same bound is
   justified over `G_4`.
8. **Caps.** Rerun the cap-transporter census over `G_4` for `|c|<=4`, or
   replace it by the algebraic cap lemma using `E(p)=<p>`. Delta's literal
   ell-5 cap census is clean (`30,912` equations, `384` canonical caps, zero
   exotic), but group-level equalities can create new transporters.
9. **Aligned cancellation and BR2.** Reuse the Validator-certified uniform
   aligned contour theorem verbatim. State boundary preservation explicitly;
   BR2 is then mostly normalization bookkeeping but should still be listed.
10. **H2 beaded paths.** Reuse the corrected per-piece argument, with
    `P_5=4`.
11. **Protected boundary.** Compute the `G_4` normal form of `E7`; scan for
    strict exposed arcs against genuinely new length-5 relators. The relevant
    strict-exposure lower bound is `13`.

The dry-run Delta proposed with base oracle `G_3` for `ell=4,5` is valuable as
a verifier rehearsal and as an acid test for near-identical pairs. It is not
the rung-5 proof, because the actual rung-5 ambient group is `G_4`.

For Delta's filtered profile, I want these fields treated as load-bearing:
`base_oracle`, `ell`, `p`, `q`, chosen rotations/orientations, `piece_word`,
`raw_arc_len`, `arc_nf`, `arc_nf_len`, `nf(p)`, `nf(q)`, `nf(p^5)`,
`nf(q^5)`, `new_flag`, `redundancy_reason`, `contains_full_block`,
`maximal_left_extend`, `maximal_right_extend`, and a two-cell
`outer_contour_nf` for critical almost-equal pairs. The key field split is
`raw_arc_len` versus `arc_nf_len`: the former enters curvature; the latter
shows whether `G_L` reduction destroys the literal overlap.

### Track B: Replacing C'(1/6) From `ell=6` Onward

At `ell=6`, literal `P_ell=ell-1=5` gives equality with the `C'(1/6)`
threshold. At `ell>=7`, it violates the strict inequality. Therefore the
classical curvature core cannot be the uniform induction unless the
`G_L`-geodesic filter removes the critical pairs.

The critical witnesses in Delta's JSON have a consistent shape:

- `pair_relation = distinct`;
- `contains_full_block = false`;
- maximal extension left/right is `0` in the sampled critical records;
- the common arc has length `ell-1`;
- after cyclic rotation, the model example is `p=sx`, `q=sy`, with
  `|s|=ell-1` and `x != y`.

So the obstruction is not same-period banding. It is an almost-equal
distinct-period family. In graph language, these are adjacent edges in the
length-`ell` de Bruijn-type period graph: same long context, different exit
letter.

#### B1. Mixed Period-Family Bands

I propose treating critical `p/q` overlaps as their own family of bands rather
than as ordinary pieces. This is an Ol'shanskii-style graded move, but the
family is much narrower than arbitrary large overlap: it is an `ell-1`
same-context/different-letter overlap.

The same-period cancellable-pair theorem does not naively extend. If
`p=sx` and `q=sy`, a `p^5`/`q^{-5}` two-cell contact along `s` leaves defect
letters `x` and `y` on the complementary contour. When `x != y`, the contour
is not the period-length-agnostic epsilon contour from the aligned same-period
case. So a mixed theorem must account for the defect letters, not pretend they
cancel.

A plausible theorem shape is:

> For a maximal mixed `p/q` band built from `ell-1` contacts, either the
> accumulated defect contour has a shorter `G_L` replacement, or each mixed
> contact contributes enough charged defect corners that the modified
> curvature argument still produces a strict boundary arc.

This needs Validator scrutiny. The falsifier is concrete: a reduced mixed
band annulus or disc pocket whose defect contour is not shorter in `G_L` and
whose boundary accounting leaves no strict exposed face.

The useful finite experiment is to compute, for each critical pair, the
normal form of the two-cell complementary contour after gluing along the
`ell-1` witness. If that contour is always strictly shorter than the retained
boundary chord, the mixed band can be turned into a cancellation/compression
rule. If not, record the defect words by family; those are the objects a
new curvature theorem must charge.

#### B2. Oracle Filtering Of Critical Pairs

Before inventing a mixed-band theorem, the next oracle should test whether the
critical literal pairs actually survive as critical `G_L` pieces.

For each literal critical pair `p=sx`, `q=sy` at level `ell`, check:

1. Are `p` and `q` both `G_L`-geodesic of length `ell`?
2. Are `p^5` and `q^5` both nontrivial in `G_L`?
3. Are both fifth powers genuinely new, rather than killed by the earlier
   normal closure?
4. Does the common arc `s` retain raw-length `ell-1` as a realized
   `G_L`-equal arc after shortlex reduction?
5. Are `p` and `q` equal, inverse, conjugate, or power-related in `G_L`?
6. Does the two-cell mixed outer contour reduce strictly in `G_L`?

If the answer to 1-4 is yes and 5-6 are no for even one representative family
at `ell=6`, the current proof skeleton really has hit the `C'(1/6)` wall.
If the oracle kills all such pairs, the uniform proof should chase the
filtering theorem: "genuinely new geodesic periods cannot differ in only one
letter over `G_L`."

My current expectation is cautious: literal counts grow quickly, so I would
not bet on all critical pairs disappearing under the oracle. But this is
exactly the right next measurement because it separates a computationally
salvageable route from a genuine graded small-cancellation problem.

#### B3. The Strongest Candidate Uniform Replacement

Here is the conjectural replacement I would route to Validator after the
filtered data lands:

Let `P_{L+1}` be the genuinely new length-`ell` periods over `G_L`. Build a
graph whose vertices are length-`ell-1` cyclic subwords and whose labelled
edges are periods `p=sx` using that subword as context. Maximal contacts of
length `ell-1` between distinct periods are treated as mixed-family contacts,
not ordinary pieces.

The desired theorem is:

Every reduced diagram over `G_L + {p^5 : p in P_{L+1}}`, after same-period
aligned cancellation and phase absorption, either

1. contains a mixed-family pocket with strictly shorter `G_L` boundary
   replacement, or
2. has all remaining ordinary pieces of length `<5ell/6`, with mixed-family
   contacts charged by non-cancelling defect letters so that Greendlinger
   still produces a strict boundary arc.

Fatal check: find a mixed-family corridor made only of critical `ell-1`
contacts whose defect contour is geodesic/nonshortenable in `G_L` and whose
outer boundary can sit on `E7` or inside a minimal disc without producing a
strict arc. That object would force a move beyond the current G4 machinery.

## Strongest Survivable Inductive Hypothesis

The following is the strongest induction package I currently believe is
survivable after Validator's audit-gate refinements. It is intentionally
conditional except where a clause is explicitly attributed to Validator as
already certified.

Fix a constant `eta < 5/6`, preferably independent of `L`. Suppose:

1. **Survival and boundary oracle.** `E7 != 1 in G_L`, with a certified
   `G_L`-geodesic cyclic normal form `e_L` for `E7`.
2. **Targeted `G_L` oracle.** We have a sound equality/geodesic oracle for the
   regular languages used in the proof: new period powers, cap transporters,
   annulus connectors, cancellable-pair contours, and strict-arc candidates
   on `e_L`.
3. **New-period list and literal orientation.** The genuinely new relators at
   level `L+1` are represented by cyclically reduced `G_L`-geodesic period
   classes `P_{L+1}` of length `ell=L+1`, chosen modulo cyclic shift and
   inverse. No genuinely new period is cyclically self-inverse. Validator
   reports this last condition automatic for `ell<=6` by abelianization, and
   Delta's literal profile extends zero self-inverse/cross-inverse violations
   through `ell=10`.
4. **Straight primitive axes.** For every `p in P_{L+1}`, all powers `p^k`
   are `G_L`-geodesic of length `kell`, and `p` has no proper root relevant
   to the elementary subgroup.
5. **Elementary subgroup / annulus package.** For every `p in P_{L+1}`,
   `E_{G_L}(p)=<p>`: no exotic centralizer, no inverter, no root extension.
6. **Uniform realized-piece separation.** After aligned same-period contacts
   are sent to the cancellable-pair system and phase caps are absorbed, every
   ordinary realized piece has length at most `eta ell`.
7. **H2 block-normalization.** Every phase connector is either a single
   cell-boundary cap of length `<ell` handled by the transporter lemma, or a
   beaded path whose beads satisfy the ordinary realized-piece bound in (6).
8. **Standing aligned-cancellation theorem.** Per Validator's audit gate,
   aligned opposite-oriented same-period contacts cancel by the uniform
   `p^5/p^{-5}` contour identity. I record it here as a standing theorem in
   the package, not as an unproved hypothesis of the induction.
9. **Protected boundary.** The word `e_L` has no strict Dehn arc for the new
   relators, where strict means an exposed arc of length at least
   `5ell - 3 eta ell` with a shorter complementary `G_L` path.

Conclusion:

`E7 != 1 in G_{L+1}`.

Proof template:

Assume a minimal relative diagram over `G_L + {p^5 : p in P_{L+1}}` with
boundary `e_L`. Annuli are excluded by (5). Phase offsets are absorbed by
(7) and (5). Aligned same-period pockets cancel by the boundary-preserving
uniform contour theorem (8), contradicting minimality. Remaining internal
disc pockets compress by BR2; this compression is also boundary-preserving
and partly redundant once (8) is in force, but it keeps the diagram
block-normalized. Every remaining realized piece has length at most
`eta ell < 5ell/6`, so the ordinary `C'(1/6)` Greendlinger argument gives a
strict boundary arc. This contradicts (9). Therefore no diagram exists.

## What Must Be Proved To Make This Uniform

The induction above reduces uniformity to four mathematical targets.

1. **Uniform period separation.**
   Prove clause (6) for genuinely new periods. This is the main obstacle.
   Delta's literal/free profile realizes `ell-1` through `ell=10`, so the
   free-level G4 proof does not scale past `ell=5`. The remaining hope for
   this exact route is a `G_L`-oracle filtering theorem showing that
   genuinely new geodesic periods have smaller realized overlaps than literal
   free words.
2. **Uniform elementary axes.**
   Prove clause (5) without a per-period `B_ann` scan, or with a bound whose
   verification is uniform. This likely needs a uniform hyperbolicity or
   malnormal-axis theorem for the ladder.
3. **Targeted oracle replacement.**
   Replace full automatic structures by a replayable finite-state/regular
   proof package exactly for the languages in clause (2). This is engineering
   and mathematics together, but it is probably necessary because full
   automatic structures may fail at later rungs.
4. **Mixed almost-equal period families.**
   If `G_L` filtering does not remove `ell-1` overlaps, build a graded
   period-family theory for pairs `p=sx`, `q=sy`, `|s|=ell-1`, `x != y`.
   The existing aligned contour theorem does not cancel these pairs for free;
   a new defect-contour or charged-curvature argument is needed.

## Bottom Line

The G4 proof contributes a plausible uniform skeleton, and one of its core
moves, the aligned cancellable-pair theorem, is genuinely L-independent per
Validator's audit gate.

But the proof is not uniformly iterable with current constants. The literal
ordinary-piece constant is the likely breaking point: if distinct new periods
can share `ell-1` geodesic letters, strict `C'(1/6)` fails starting at
`ell=6`. Delta's literal/free-level curve realizes exactly that obstruction
for every `ell=4..10`.

The bounded concrete plan is rung 5 by the existing method once the `G_4`
oracle lands. The uniform research frontier begins at `ell=6`: either
oracle-filtered genuinely new periods avoid the critical `ell-1` overlaps, or
the program needs a mixed almost-equal period-family replacement for ordinary
`C'(1/6)`.
