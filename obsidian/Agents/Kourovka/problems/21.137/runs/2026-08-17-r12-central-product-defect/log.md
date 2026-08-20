---
title: "Kourovka 21.137 r12 — central-product defect cancellation"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
direction: counterexample
run_state: awaiting_lead
allocation_active_minutes: 144
scope_cumulative_start_minutes: 267
scope_cumulative_cap_minutes: 411
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/central-products, project/kourovka, status/conjectured]
---

# Run log

## 2026-08-17T08:24:09Z — work start

Active minutes this run: 0. Scope cumulative charged minutes at entry: 267. Hard stop: 33 additional active minutes; exploration stops near run minute 27 so packaging finishes by run minute 33.

Resources obeyed: canonical revision-2 scope, rendered source page 184, and only the two reviewed facts named by Lead (`minimal-central-obstruction` and `class-p-plus-one-hall-lemma`). No web/history search, delegate, wreath-shaped/quarantined material, `p=2`, exponent-8, UT7, NS3 repair, affine-cover, or CPTR artifact was used.

## Source and scope gate

The configured PDF was rendered to `scratch/source-page-184.png` and inspected visually. Correct active transcription:

> For an odd prime `p`, if the actual set of `p`-th powers in a finite `p`-group of exponent exactly `p^2` is a subgroup, must that subgroup be abelian?

`source_transcription_checked: yes`  
`active_scope_checked: yes`  
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

Clause matrix:

| source clause | active? | this run |
|---|---:|---|
| general powerfulness question | no | excluded |
| odd-prime, exact exponent `p^2`, actual-power-set subgroup, abelianity | yes | target |
| `p=2`, exponent-8 square question | no | excluded |

Admissibility checklist reconciled to the canonical record:

| constraint_id | required reading |
|---|---|
| `21.137-odd-forall-p-G` | a counterexample may use one explicit admissible odd prime and finite group |
| `21.137-odd-p-not-2` | freeze `p=3` only |
| `21.137-odd-finite-p-group` | any witness must be a finite `3`-group |
| `21.137-odd-exponent-p2` | its exponent must be exactly `9` |
| `21.137-odd-power-set-definition` | compute the complete set `{g^3:g in G}`, never just its generated subgroup |
| `21.137-odd-power-set-subgroup` | that complete set itself must be closed |
| `21.137-odd-P-abelian` | a witness must violate this: two actual cubes must not commute |

No source/scope mismatch was found.

## Strategy portfolio

1. **Structured construction — CENTRAL-PRODUCT-DEFECT-CANCELLATION (selected).** For two exponent-9 seed groups with central order-3 subgroups, derive the complete cube image of their anti-diagonal central quotient. Encode closure by exact central-defect sets. Test whether independent coordinate choices make defect cancellation impossible, or freeze the smallest surviving seed data.
2. **Catalogue/small-case probe.** If the structural gate leaves finitely many defect patterns over `F_3`, enumerate those patterns only. A negative result would exclude the frozen central-product repair mechanism, not arbitrary finite groups.
3. **Theoretical obstruction.** Use the reviewed minimum-counterexample reduction: quotient projections of any putative central-product witness have actual cube sets that are subgroups; isolate when noncommutativity is merely inherited from a smaller quotient/seed rather than created by defect cancellation.
4. **Certificate plan.** Validator can check the quotient preimage identity and the closure equivalence line by line. Any finite pattern screen will list every pattern and a direct witness tuple for failure; any group candidate would require a presentation plus independent complete elementwise cube enumeration.

Ranking: derive the quotient formula first; then exhaust the exact `p=3` singleton-central-fibre seed family by hand or a tiny independent pattern enumerator. Kill the strategy if the formula shows defect cancellation cannot repair that family and no finite group seed presentation is mechanically frozen by run minute 27.

## 2026-08-17T08:30Z — exact anti-diagonal quotient formula

Let `A_1,A_2` be finite `p`-groups, let `C_i=<z_i><=Z(A_i)` have order `p`, put

`D=<(z_1,z_2^{-1})>` and `H=(A_1 x A_2)/D`,

and write `q` for the quotient map and `S_i={a^p:a in A_i}` for the complete actual-power sets. Directly,

`Pow_p(H)=q(S_1 x S_2)`,

and

`q^{-1}(Pow_p(H))=(S_1 x S_2)D`

`= union_{k in F_p} (z_1^k S_1) x (z_2^{-k} S_2)`.

For `x,x' in S_i`, define the exact central-defect set

`Delta_i(x,x')={k in F_p : z_i^{-k}xx' in S_i}`.

Because each `S_i` contains `1` and is inverse-closed, `Pow_p(H)` is a subgroup if and only if it is product-closed, and product-closure is exactly

`Delta_1(x,x') intersect (-Delta_2(y,y')) != empty`

for every `x,x' in S_1` and `y,y' in S_2`. Thus the two coordinate defects are independent choices; anti-diagonal cancellation can repair only defects lying in the designated central directions.

The commutator observable is also exact:

`[q(x,y),q(x',y')]=q([x,x'],[y,y'])`.

It is nontrivial exactly when the displayed commutator pair is outside `D`.

Equivalent fibre form: if `T_i=S_i C_i/C_i` and `F_{i,t} subset F_p` is the set of central coordinates of actual powers over `t in T_i`, then the actual-power fibre in `H` over `(t,u)` has residual central-coordinate support `F_{1,t}+F_{2,u}` (up to the harmless translation caused by section choice). In a self-product at `p=3`, `|F_t|>=2` for every `t` would make every sum equal `F_3`; closure would then reduce to the necessary gate that `T` itself be a subgroup.

## 2026-08-17T08:35Z — frozen finite seed row `MON15-SELF`

Freeze `p=3` and the 15-dimensional associative nilpotent algebra

`J=<x^i y^j : 0<=i,j<=3, (i,j)!=(0,0)>_{F_3}`

with relations `x^4=y^4=yx=0`. Let `A=1+J`, `c=x^3y^3`, `C=1+F_3 c`, and

`H=(A x A)/<((1+c),(1-c))>`.

This is one fully fixed finite seed row, not a catalogue or UT7 family. The algebra has `J^7=0`, so every element of `A` has order dividing `9`; `1+x` has order exactly `9`. Hence `A` is a finite `3`-group of order `3^15`, `C` is central of order `3`, and `H` is a finite `3`-group of order `3^29` and exact exponent `9` because the first factor embeds.

For `R=a+b+m`, with `a` x-pure, `b` y-pure, and `m` mixed, the multiplication rules give the exact cube polynomial

`R^3=a^3+b^3+a^2b+ab^2+a^2m+amb+mb^2`.  (E1)

In particular, writing the coefficients of `x` and `y` in `R` as `alpha,beta`, respectively, the four lowest coordinates are

`[x^3]R^3=alpha`, `[y^3]R^3=beta`,

`[x^2y]R^3=alpha^2 beta`, `[xy^2]R^3=alpha beta^2`.  (E2)

Now take

`r=2y+2xy+x^2`,

`s=y^2+x+xy^3`.

Direct substitution in (E1) gives

`u=r^3=2y^3+2xy^3+x^2y^2+x^3y^2`,

`v=s^3=x^3+x^2y^2+c`.

Modulo `F_3 c`, the sum `u+v` has x- and y-leading coordinates `alpha=1,beta=2`, but both its `x^2y` and `xy^2` coordinates are zero. Formula (E2) requires them to be `2` and `1`. Therefore no `R` has `R^3 congruent u+v (mod F_3 c)`. Also `uv=0` from `yx=0`, so `(1+u)(1+v)=1+u+v`. Consequently the two actual cubes

`q((1+r)^3,1)` and `q((1+s)^3,1)`

have a product which is not an actual cube in `H`: even an arbitrary anti-diagonal central correction cannot repair the noncentral quotient defect.

The row nevertheless retains the desired noncommutativity observable. The actual cubes `(1+x)^3=1+x^3` and `(1+y)^3=1+y^3` satisfy

`[1+x^3,1+y^3]=1+c`,

and `q(1+c,1)` is nonidentity because `(1+c,1)` is not in the anti-diagonal kernel. Thus the row fails only the subgroup gate relevant here; it is an `OUT_OF_SCOPE_EXAMPLE`, not a counterexample.

## Reproducible bounded enumeration

`scratch/monomial_seed.py` (Python 3.12.3; SHA-256 `03f99aec99519ea2133def089f3a033526ecfb2de367ea5df7016d0c58e25bd5`) independently enumerates the exact cube image by splitting (E1) into 729 affine linear maps on the nine mixed coefficients. Exact command:

`timeout 30s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/monomial_seed.py`

Salient observed output:

```text
cube_image_size=1947
quotient_cube_image_size=649 span_rank=9
quotient_cube_image_additive_subspace=False
missing_sum_u_root=2*x^0y^1+2*x^1y^1+1*x^2y^0
missing_sum_u_root_cube=2*x^0y^3+2*x^1y^3+1*x^2y^2+1*x^3y^2
missing_sum_v_root=1*x^0y^2+1*x^1y^0+1*x^1y^3
missing_sum_v_root_cube=1*x^2y^2+1*x^3y^0+1*x^3y^3
central_fibre_size_histogram={3: 649}
identity_central_fibre=[0, 1, 2]
central_c_root=1*x^0y^2+1*x^1y^1+1*x^2y^0
x3y3_minus_y3x3_equals_c=True
all_central_fibres_at_least_two=True
seed_gate=FAIL: quotient actual-cube image is not a subgroup
```

The cardinality `649` is itself incompatible with an additive `F_3`-subspace; the explicit pair above supplies a hand-checkable closure defect and does not rely on that cardinality argument.

## Early method checkpoint and self-check

Target/revision remain `21.137/odd-prime-exponent-p2`, revision 2. The general quotient formula is exact, and one fully frozen finite `p=3` seed row has been excluded. Its constraint check is: odd prime pass; finite same-prime group pass; exact exponent `9` pass; complete actual cube set computed pass; actual cube set subgroup **fail**; noncommuting actual cubes pass but cannot be treated as the conclusion violation because the subgroup hypothesis fails.

Current bottleneck: central gluing can cancel only the designated one-dimensional central coordinate. In `MON15-SELF`, every central fibre is already full, while a forced degree-three polarization coordinate makes the quotient cube image fail closure. The seed is therefore killed before any larger central-product search.

Two qualitatively different alternatives for Lead are: (1) a new finite associative-algebra coefficient family designed first to make the quotient cube image a subgroup while leaving some central fibres of size exactly two; (2) a theoretical self-product obstruction classifying which `F_3` fibre-support patterns are compatible with an actual cube map and a nonzero cube commutator. A bounded continuation should test quotient closure before any full central-product enumeration and kill immediately on a noncentral defect.

The named strategy has met its finite-row kill criterion. No replacement method is started. Outcome is `PARTIAL_RESULT`; run state becomes `awaiting_lead`, not parked and not terminated.

## 2026-08-17T08:40:05Z — work stop

Charged active time this run: 16 minutes. Scope cumulative charged time: 283 minutes. Seventeen minutes of the at-most-33-minute allocation remain unspent because the frozen row met its exact early kill. Waiting for an explicit Lead decision.

## 2026-08-17T08:42:54Z — REFINE work start

Lead assigns the remaining 17 active minutes to the finite `F_3` support-family classification only. No new seed is started. Goal: classify all nonempty-subset families satisfying the self-product intersection condition, incorporate formal inversion and identity symmetries of an actual power set, separate common correcting shifts from triangle exceptions, and state the realization gap.

## Finite `F_3` defect-family classification

Retain `S=Pow_3(A)`, central `C=<z>` of order 3, and

`Delta(x,y)={k in F_3:z^{-k}xy in S}`.

Formal actual-value symmetries are:

- `Delta(y^{-1},x^{-1})=-Delta(x,y)` because `S` is inverse-closed;
- `Delta(y,x)=Delta(x,y)` because `z^{-k}xy` and `z^{-k}yx` are conjugate;
- `K=Delta(1,1)` contains 0 and is negation-invariant, hence `K={0}` or `F_3`;
- `0 in Delta(x,1)` for every `x in S`.

Let `D` be the family of distinct supports which occur. Negation closure turns the self-product condition

`A intersect (-B) != empty` for all `A,B in D`

into ordinary pairwise intersection: apply the condition to `A,-B`, and use `-B in D`. Conversely pairwise intersection plus negation closure gives the original condition.

Writing `O={0}`, `A={0,1}`, `Abar={0,2}`, `B={1,2}`, and `U=F_3`, exhaustive classification gives exactly eight formal occurrence families:

| family | supports | global intersection |
|---|---|---|
| F1 | `U` | `U` |
| F2 | `O` | `O` |
| F3 | `O,U` | `O` |
| F4 | `B,U` | `B` |
| F5 | `A,Abar,U` | `O` |
| F6 | `O,A,Abar` | `O` |
| F7 | `O,A,Abar,U` | `O` |
| F8 | `A,Abar,B,U` | empty |

The reason no other family occurs is elementary. Negation swaps `{1}` with `{2}` and `A` with `Abar`, while fixing `O,B,U`; the singleton supports `{1},{2}` fail even self-intersection against their negatives. `O` is incompatible with `B`. All remaining negation-orbit selections give precisely the table.

`scratch/defect_family_classifier.py` (SHA-256 `56a9629e39329160f376a33dbcf22b8396b132e2902e1a59b8e90f9329827f13`) enumerates all 127 nonempty support families and returns the same eight. This is a finite set-system audit only.

## Common shifts collapse to an already-closed seed

A uniform correcting shift exists exactly when the global intersection `I=intersect D` is nonempty: negation closure makes `I=-I`, so one may choose `k` with both `k,-k in I`. Seven formal rows have such a shift.

For an actual inverse-closed seed set, every common-shift row collapses. If `k=0`, `xy in S` for all `x,y`, so `S` is a subgroup. If `k!=0`, set `T=z^{-k}S`. The common inclusions `k,-k in Delta(x,y)` give:

- `T*T subset T`;
- `1 in T` because `z^k in S`;
- `(z^{-k}x)^{-1}=z^{-k}(z^{-k}x^{-1}) in T`, using `2k=-k` in `F_3`.

Thus `T` is a subgroup. Since `z^{-k}=z^{-k}*1 in T`, also `z^k in T`, and `S=z^kT=T`. Therefore `S` itself is a subgroup. Then every defect support equals the fixed identity support `K`: `Delta(x,y)=K` for all `x,y`. Hence among the seven formal common-shift rows, an actual seed occurrence family can only be the constant family `{O}` or `{U}`. Such a seed needs no central-product repair.

## The unique triangle exception and exact realization gap

The sole no-common-shift row is

`{ {0,1}, {0,2}, {1,2}, F_3 }`.  (TRI3)

It forces `K=U`, hence `C subset S`. Let `pi:A->A/C`, `T=pi(S)`, choose a representative `r_t` for each `t in T`, and put

`F_t={a in F_3:z^a r_t in S}`.

There is an exact set-level equivalence:

`TRI3 occurs` iff `T` is a subgroup, every occupied fibre `F_t` has size 2 or 3, and at least one has size 2.

Forward: nonempty defects make `T` product-closed; inversion makes it a subgroup. Every defect is a translate/reflection of the product fibre, so TRI3 gives sizes 2 or 3. At least one size-2 support occurs. Reverse: two subsets of `F_3` of size at least 2 always meet after negation, so the self-product condition holds. The full central identity fibre and one size-2 fibre, translated by the three central inputs in `C subset S`, produce all three two-point supports; full fibres produce `U`.

Therefore the only potentially novel central-product mechanism is a `2-or-3 fibre cover` of a subgroup in `A/C`, with at least one two-point fibre. If a finite exponent-9 `3`-group `A` realizes this with `S=Pow_3(A)` and two noncommuting members of `S`, then the self anti-diagonal quotient is an in-scope counterexample: its complete cube set is a subgroup by the fibre-sum criterion, its exponent remains 9 because a factor embeds, and the noncommuting pair survives in that embedded factor.

This is not a witness. The unresolved realization gap is to produce such an `A,C` from an actual complete cube map while also satisfying finiteness, exact exponent 9, conjugacy/inversion symmetries, associativity coherence, and noncommutativity. For example, associativity forces the exact total-correction identity

`union_{k in Delta(x,y)} (k+Delta(z^{-k}xy,w))`

`= union_{m in Delta(y,w)} (m+Delta(x,z^{-m}yw))`,

for all `x,y,w in S`; a bare TRI3 support table need not satisfy it. The support classification also says nothing about the existence of cube roots or commutators. `MON15-SELF` has full size-3 fibres but fails the separate quotient-subgroup gate, so it does not realize TRI3.

Two additional pointwise restrictions are explicit. First, `Delta(x,1)` always contains 0, so the support `B={1,2}` required by TRI3 must occur on a genuine two-input product, never on an identity pair. Second, if `[x,y]=z^a` is nontrivial for actual cubes `x,y in S`, conjugacy invariance fills the entire central fibres `xC` and `yC`; hence any size-2 fibre must lie away from such a nonradical pair. In the reviewed minimum-central situation where cube commutators take values in `C`, the needed two-point fibres must therefore occur in the radical of the commutator pairing. This narrows realization but does not forbid it.

## 2026-08-17T08:51:02Z — REFINE work stop

Charged active time for REFINE: 8 minutes. Total charged active time this run: 24 minutes. Scope cumulative charged time: 291 minutes. Nine minutes of the original at-most-33-minute allocation remain unspent because the finite support classification and realization-gap statement are complete. Outcome remains `PARTIAL_RESULT`; session returns to `awaiting_lead` without starting another seed or parking the direction.

## 2026-08-17T09:01:53Z — TRI3-SMALLGROUP-SEED work start

Lead grants a new one-hour increment from scope cumulative minute 291 and leases compute slot 1 for exactly one `timeout 55s gap -q <frozen-script>` command. The frozen layer is every GAP SmallGroups entry of order `3^7=2187`; only exact-exponent-9 seeds are eligible. The complete cube set, every central order-3 subgroup contained in it, the projected subgroup gate, 2-or-3 fibre gate with a genuine 2-fibre, and rooted noncommuting cube pair must all be checked. A timeout is a checkpoint, not a negative result.

## Frozen script and leased command

Script: `scratch/tri3_order2187.g`  
Frozen SHA-256: `446e78854e3b91e3ccce726d28b8ae04e8761d7a94303488aeebe7cc987a96d0`  
Length: 218 lines.

The script is deterministic and, when the order-2187 catalogue is installed, loops over every id `1..NumberSmallGroups(2187)`. For each exact-exponent-9 group it constructs the complete cube image from all 2187 elements, finds rooted noncommuting cube values, enumerates every distinct central order-3 subgroup contained in that image, and applies the quotient-subgroup and exact fibre gates. A seed hit triggers construction of the self anti-diagonal quotient and an independent full elementwise cube enumeration there.

The one leased command was run exactly once:

`timeout 55s gap -q < Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/tri3_order2187.g`

Observed exit code: `0`. Observed wall time: `3.134319642` seconds. Verbatim output:

```text
2187
function( S ) ... end
function( G ) ... end
function( seed ) ... end
true
TRI3_ORDER2187_BEGIN gap_version=4.12.1 smallgrp_loaded=true
STATUS=BLOCKER reason=SmallGroups_library_order_2187_not_installed
```

No SmallGroup was loaded and zero catalogue rows were screened. This output is not a negative search result.

Read-only package diagnostics identify the missing data layer precisely: `gap-smallgrp` version `1.5.3-1` is installed, `gap-smallgrp-extra` is not installed, and the local package index offers candidate `gap-smallgrp-extra 1.5.3-1`. The installed SmallGrp tree is only 6.3 MB and has `small2` but no extra data directory. Installing the extra data requires Lead/human authority and likely privileged package/network access.

## 2026-08-17T09:07:48Z — blocked work stop

Outcome: `BLOCKER`. Charged active time in this increment: 6 minutes. Scope cumulative charged time: 297 minutes. Compute slot 1 is released; the GAP process exited normally. The exact blocker is the absent order-2187 SmallGroups data, not a timeout, mathematical obstruction, or absence of TRI3 seeds. Session returns to `awaiting_lead`; no alternate seed, smaller order, or unsanctioned catalogue layer is started.

## 2026-08-17T09:46:37Z — catalogue rerun start

Lead reports the blocker cleared and leases compute slot 1 for one fresh 55-second rerun. Read-only checks give `gap-smallgrp-extra: install ok installed 1.5.3-1` and reproduce the unchanged frozen SHA-256 `446e78854e3b91e3ccce726d28b8ae04e8761d7a94303488aeebe7cc987a96d0`. Work resumes from scope cumulative minute 297; the same exact script and no altered seed family will be used.

## 2026-08-17T09:49Z — frozen rerun returns the same availability blocker

The one newly leased command was run exactly once, unchanged:

`timeout 55s gap -q < Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/tri3_order2187.g`

Observed exit code: `0`. Observed wall time: about `2.94` seconds. Verbatim output:

```text
2187
function( S ) ... end
function( G ) ... end
function( seed ) ... end
true
TRI3_ORDER2187_BEGIN gap_version=4.12.1 smallgrp_loaded=true
STATUS=BLOCKER reason=SmallGroups_library_order_2187_not_installed
```

The process therefore stopped at its pre-scan availability guard. Zero IDs were loaded or screened. The output is neither a timeout nor a negative catalogue result, and the single command lease is now consumed; it was not rerun.

## Exact installed-layer diagnosis

The reported package installation succeeded, but the package does not contain the required catalogue layer:

- `dpkg-query` reports `gap-smallgrp-extra 1.5.3-1` installed.
- The Ubuntu package description says this package contains groups of order `p^n` only for `n<=6`; it does not claim the `p^7` layer.
- The installed SmallGrp tree has group-construction drivers `small2/smlgp2.g.gz` through `small9/smlgp9.g.gz`, but no `small10` or `small11` directory and no `smlgp11.g` driver. There is no `sml2187.*` data file anywhere in that tree.
- The installed SmallGrp manual identifies the order-`p^7` catalogues for `p=3,5,7,11` as library layer 11. Its layer list says layer 9 ends with the remaining `p^n`, `4<=n<=6`, while layer 11 contains the remaining `p^7` groups.
- The actual installed availability functions corroborate this split: `smlgp9.g` accepts prime powers only when the factor-list length is 4, 5, or 6 and otherwise returns `fail`; none of `smlgp2.g` through `smlgp9.g` claims pure order `3^7`. The occurrence of `size=3^7` in `smlgp3.g` is only an ID-permutation branch in a generic selector; that driver's availability predicate is for orders `2^n*p` and rejects 2187.
- A local filesystem and package-cache search found no separate layer-11 archive or order-2187 data.

Thus the blocker was not cleared by `gap-smallgrp-extra`: the exact missing resource is SmallGrp group-data layer 11 (and a loadable driver path reaching it), not the already-installed Debian/Ubuntu extra package. Provisioning the full upstream data through layer 11, or an equivalent sanctioned order-2187 catalogue, is required before the frozen scan can cross its availability guard. Because `read.g` loads construction layers consecutively and stops at the first missing availability function, a provisioned installation should expose the required layer through the normal SmallGrp loader, rather than merely dropping an isolated data file into the current tree.

## 2026-08-17T09:53Z — second blocked work stop

Outcome remains `BLOCKER`. Charged active time for this rerun/diagnosis: 6 minutes. Scope cumulative charged time: 303 minutes. Forty-eight minutes remain in the increment ending at cumulative minute 351. Compute slot 1 is released because GAP exited normally. The prior exact anti-diagonal formula, `MON15-SELF` exclusion, and TRI3 realization criterion remain `PARTIAL_RESULT`; the active odd-prime scope remains unanswered. Session returns to `awaiting_lead` without changing the frozen script, starting another seed, or claiming an order-2187 exhaustion.

## 2026-08-17T09:58:42Z — official layer-11 rerun start

Lead provisions the official GAP SmallGrp 1.6.0 release at `Agents/Kourovka/tools/gaproot/pkg/SmallGrp-1.6.0`, reports that the rooted GAP invocation sees all 9310 groups of order 2187, and leases compute slot 1 for one fresh 55-second run. Read-only checks find both `small10` and `small11` in that root and reproduce the unchanged frozen script SHA-256 `446e78854e3b91e3ccce726d28b8ae04e8761d7a94303488aeebe7cc987a96d0`. Work resumes from scope cumulative minute 303 with 48 minutes remaining.

## Official layer-11 scan completes

The one fresh leased command was run exactly once:

`timeout 55s gap -l 'Agents/Kourovka/tools/gaproot;/usr/share/gap' -q < Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/tri3_order2187.g`

It exited normally with code `0` after about `31.8` seconds, before the timeout. The rooted invocation used GAP 4.12.1 and the local `PackageInfo.g` confirms SmallGrp 1.6.0. GAP emitted four nonfatal syntax warnings about global variables captured inside anonymous predicates, then completed all counters. Salient output:

```text
TRI3_ORDER2187_BEGIN gap_version=4.12.1 smallgrp_loaded=true
library_order=2187 group_count=9310
PROGRESS i=100 exp9=18 noncomm=0 fibre_gate=0
...
PROGRESS i=9300 exp9=8296 noncomm=0 fibre_gate=0
COMPLETE_SCAN=yes groups=9310 exp9=8302 noncomm_cube_seed=0 central_C_in_S=0 projected_subgroup=0 fibre_gate=0 seed_hits=0
STATUS=NO_SEED_IN_ORDER_2187_LAYER
```

Thus every ID `1..9310` completed. Of the 9310 official catalogue groups of order `3^7`, exactly 8302 passed the exact-exponent-9 gate. For each of those groups the script formed the complete set `{g^3:g in G}` from all 2187 elements. None of the 8302 complete cube sets contained a noncommuting pair, so all candidates failed before the central-subgroup and fibre gates. The zero values for `central_C_in_S`, `projected_subgroup`, and `fibre_gate` therefore mean those later counters were not reached, not that those properties were separately tested for every group.

This exhausts the official SmallGrp 1.6.0 order-2187 layer as follows: no order-2187 exact-exponent-9 group is a direct revision-2 counterexample, because every complete cube set is pairwise commuting; and no such group can be a TRI3 seed for the anti-diagonal constructor, because that constructor requires noncommuting seed cube values. It does not exclude larger orders, other odd primes, or a non-catalogue realization beyond this order, and it does not answer the active scope.

## 2026-08-17T10:00:42Z — layer exhaustion checkpoint

Outcome returns from tooling `BLOCKER` to `PARTIAL_RESULT`. Charged active time for the provisioned rerun and packaging: 2 minutes. Scope cumulative charged time: 305 minutes. Forty-six minutes remain in the increment ending at cumulative minute 351. Compute slot 1 is released after normal exit. The order-2187 method is exhausted, so the run returns to `awaiting_lead` without starting another seed or parking the counterexample direction.

## 2026-08-17T10:07Z — `TRI3-ORDER6561-CYCLIC-CENTRE-LIFT` start

Lead accepts the exact order-2187 exhaustion and assigns the first possible larger seed layer, order `3^8=6561`. Three supplements are incorporated before freezing any family: strengthen the quotient filter to `Z(A)=C3`; reconstruct the reviewed class-five identity using only projective cube closure; and, if those pass, freeze but do not run the exact order-2187 quotient-base filter. No descendant generation or GAP computation is launched in this work segment.

## Quotient filter: noncommuting seed cubes force cyclic centre

Use `[u,v]=u^-1 v^-1 u v`. Let `A` have order `3^8`, exponent 9, and actual-cube set `S`. Suppose `s=x^3,t=y^3 in S` have `c=[s,t] != 1`. For every subgroup `N<=Z(A)` of order 3, the quotient `A/N` has order `3^7` and exponent dividing 9.

- If `exp(A/N)=3`, every cube in `A/N` is the identity.
- If `exp(A/N)=9`, `A/N` is isomorphic to one of the 9310 completed official SmallGrp rows, and the complete order-2187 screen says every two actual cubes commute.

In either case the images of `s,t` commute, so `c in N`. A finite nontrivial 3-group has nontrivial centre and hence at least one such `N`. Membership in one `N` proves `c in Z(A)` and `c^3=1`; since `c!=1`, its order is exactly 3. Since `c` lies in every central order-3 subgroup, any two such subgroups meet nontrivially and hence are equal. Therefore `Z(A)` has a unique order-3 subgroup.

The finite abelian 3-group `Z(A)` is consequently cyclic: in its invariant-factor decomposition, the subgroup of elements killed by 3 has `F_3`-dimension equal to the number of cyclic factors, and uniqueness forces that number to be one. Since `exp Z(A)` divides 9, only `Z(A)=C3` and `Z(A)=C9` remain. This also verifies rather than assumes both the centrality and the exact order of the cube commutator.

## TRI3 strengthens the centre to exactly its eligible `C3`

The eligible subgroup `C` in the TRI3 criterion is central of order 3, so the uniqueness just proved forces it to be the unique order-3 subgroup of `Z(A)`.

Suppose `Z(A)=<z>` has order 9. Then `C=<z^3>`. For any occupied `C`-fibre choose `s=x^3 in S` in that fibre. Centrality gives, for `k=0,1,2`,

`(x z^k)^3=x^3 z^(3k)=s z^(3k)`.

These are the three distinct elements of `sC`, so every occupied fibre is full. Changing the chosen section only translates its support in `F_3`, preserving cardinality three. This contradicts the TRI3 requirement of at least one two-point fibre. Hence every surviving seed satisfies

`Z(A)=C`, with `|C|=3`.

## Projective cube closure already kills class at most five

Write `C_0` for the central subgroup above to avoid collision with the Hall commutator named `c` in the reviewed identity. Let `pi:A->A/C_0`, and assume only the TRI3 projective closure condition

`T=Pow_3(A)C_0/C_0=Pow_3(A/C_0)` is a subgroup.

Put `U=Pow_3(A)C_0=pi^-1(T)`. The actual cube set of the quotient is conjugacy-invariant; because it is a subgroup, `T` is normal, so `U` is a normal subgroup of `A`. Every element of `U` has the form `s d` with `s=w^3` an actual cube and `d in C_0`. Since `exp(A)=9` and `C_0` is central of order 3,

`(s d)^3=s^3 d^3=w^9=1`.  (P1)

Thus `U` has exponent 3 even though the actual cube set need not itself be closed.

Now reconstruct the four membership rows used by the reviewed integral class-five identity. With its notation,

`A_H=[y,x^3]=(x^-3)^y x^3` lies in `U`, because both displayed factors are conjugates/products of actual cubes and `U` is a subgroup. The elements `c^3,a^3` are actual cubes, so

`T_A=(c^3 a^3)^-1 A_H in U`.

Normality gives `S_A=[T_A,y] in U`. Similarly,

`B_H=[x,y^3]=(y^-3)^x y^3 in U`;

the elements `q_1^3,q_2^3` are actual cubes, hence

`T_B=(q_1^3 q_2^3)^-1 B_H in U`,

and normality gives `Q=[T_B,x] in U`. These are exactly the original membership operations—multiplication, inversion, conjugation, and commutation—but performed in the normal subgroup `U`, not incorrectly in the unclosed value set.

For class at most 5, the independently reviewed integral identity is

`[x^3,y^3]=c^-9 a^-9 b^-9 beta^-9 delta^54 epsilon^27 T_A^-3 S_A^-3 T_B^3 Q^3`.  (I)

Exponent 9 kills the first six factors (all exponents are multiples of 9), while (P1) kills the four terminal cubes. Therefore `[x^3,y^3]=1` for all `x,y`. A TRI3 seed, which requires noncommuting actual cubes, must have class at least 6.

An order-`3^8` group has class at most 7. Hence the only surviving classes are 6 and 7, i.e. coclass 2 and 1.

## Exact quotient-base reduction

For a surviving seed put `Q=A/C`. Then `|Q|=3^7` and `exp Q` divides 9. If `exp Q=3`, then `pi(x^3)=pi(x)^3=1` for every `x`, so `S<=C`; all seed cubes would commute. Thus `exp Q=9`.

Moreover `Pow_3(Q)=pi(S)=T` is a nontrivial subgroup: it is a subgroup by TRI3, and triviality would again imply `S<=C`. The completed order-2187 scan separately guarantees that this subgroup is abelian.

If `cl(A)=d in {6,7}`, then the last nontrivial term `gamma_d(A)` lies in `Z(A)=C` and hence equals `C`. Also `gamma_(d-1)(A)` is not contained in `C`, since otherwise the lower central series would stabilize nontrivially before terminating. Therefore `cl(A/C)=d-1`. The quotient bases have exactly:

- class 5 when `A` has class 6;
- class 6 when `A` has class 7.

So the complete finite base list consists precisely of SmallGroup rows `(2187,i)` with exponent 9, class 5 or 6, and a nontrivial complete actual-cube set which is itself a subgroup.

## Complete finite central-extension parameterization after the base filter

For each surviving base `Q`, all relevant lifts are covered by normalized central extensions

`A_f=F_3 x_f Q`, `(a,q)(b,r)=(a+b+f(q,r),qr)`,

where `f` ranges over normalized 2-cocycles for the trivial `Q`-module `F_3`. Changing section changes `f` by a coboundary; taking all classes in `H^2(Q,F_3)` covers every central extension with distinguished kernel `C3`, with harmless automorphism duplicates.

This gives exact seed gates directly. Define

`kappa_f(q)=f(q,q)+f(q^2,q)`.

Because `3a=0`, every lift `(a,q)` has cube `(kappa_f(q),q^3)`. Hence the complete central support over `t in Pow_3(Q)` is exactly

`F_t(f)={kappa_f(q):q^3=t}`.

Section/coboundary changes translate these supports and preserve their sizes. The TRI3 fibre gate is `|F_t(f)| in {2,3}` for every occupied `t`, with `F_1(f)=F_3` and at least one size-two fibre. Full centre is the exact cocycle condition that there is no `q!=1` in `Z(Q)` satisfying `f(q,r)=f(r,q)` for every `r in Q`. The remaining direct gates are `|A_f|=6561`, exponent 9, class 6 or 7 as matched above, and a noncommuting pair among the complete cube values.

Equivalently, with a seven-generator relative-order-3 pc presentation for `Q`, adjoin a central generator `z` of order 3 and attach one `F_3` tail to each of the seven power relations and 21 conjugation/commutator relations. The at most 28 tail coordinates satisfying the pc consistency relations give all such central extensions; changing generator lifts gives coboundaries. This is a complete finite parameterization, not permission to enumerate up to `3^28` raw vectors. The number of quotient bases must be known first so a bounded cohomology/tail plan can be costed.

## Frozen quotient-base filter; not run

Script: `scratch/tri3_order2187_quotient_base_filter.g`  
SHA-256: `a4919904da10d49cce1e29e311c1631774261fc726e16f45b0d116b9d94cd1ef`  
Length: 65 lines, 2238 bytes.

It deterministically visits every official SmallGrp 1.6.0 ID `1..9310` and applies exactly the four base conditions: exponent 9; class 5 or 6; nontrivial complete cube set from all 2187 elements; and equality of that set with the subgroup it generates. It prints every surviving ID, class, and cube-subgroup size. It deliberately does not retest noncommuting cubes and does not construct any central extension.

Proposed leased command:

`timeout 55s gap -l 'Agents/Kourovka/tools/gaproot;/usr/share/gap' -q < Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/tri3_order2187_quotient_base_filter.g`

Resource estimate: one compute slot, at most 55 wall seconds, and ordinary GAP memory well below 1 GiB. The earlier strictly heavier full-element/noncommuting-pair scan of the same 9310 IDs completed in 31.8 seconds, so this class-restricted filter is expected to finish within roughly 35 seconds. No command has been run; a Lead lease is required.

## 2026-08-17T10:36:00Z — bounded-filter lease checkpoint

Outcome remains `PARTIAL_RESULT`. Charged active time for the cyclic-centre proof, projective-closure audit, quotient reduction, cocycle parameterization, and frozen filter: 29 minutes. Scope cumulative charged time: 334 minutes. Seventeen minutes remain in the current increment ending at cumulative minute 351. The requested computation has not been run and no compute slot is occupied. The run returns to `awaiting_lead`, with the exact bounded lease request sent separately; neither the problem nor counterexample direction is parked.

## 2026-08-17T10:39:10Z — quotient-base filter lease start

Lead verifies the frozen hash/length and leases compute slot 1 through `2026-08-17T10:47:00Z` for exactly the proposed rooted 55-second command. Work resumes from scope cumulative minute 334. The grant excludes all central-extension and descendant enumeration.

## Quotient-base filter result

The authorized command was run exactly once and exited normally with code `0` after `16.909420981` seconds, before the timeout:

`timeout 55s gap -l 'Agents/Kourovka/tools/gaproot;/usr/share/gap' -q < Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/tri3_order2187_quotient_base_filter.g`

Complete stdout is preserved verbatim at `scratch/tri3_order2187_quotient_base_filter.out`, SHA-256 `bb6af353acd79474fdbb3a43815e7efed54f4e4b52cb8d9de0c931a29d18df30`. Its final counters are:

```text
COMPLETE_BASE_FILTER=yes groups=9310 exp9=8302 class56=26 nontrivial_cube=26 cube_subgroup=0
STATUS=QUOTIENT_BASE_FILTER_COMPLETE
```

Every official ID `1..9310` completed. Among the 8302 exact-exponent-9 groups, exactly 26 had class 5 or 6; all 26 had a nontrivial complete actual-cube set, and none of those 26 sets was a subgroup. Hence the quotient-base list is empty. No `BASE_HIT` line occurred.

This kills the entire order-6561 TRI3 lift layer before any cocycle or descendant enumeration: every such seed was proved to require one of these quotient bases, and there are none.

There is also a stronger direct-witness corollary. Suppose `G` itself had order `3^8`, exponent 9, and a nonabelian complete cube set which was a subgroup. The central-quotient argument still forces a unique central order-3 subgroup `N` and cyclic centre; the reviewed subgroup theorem forces `cl(G)>=6`. Put `Q=G/N`. If `exp Q=3`, all cubes of `G` lie in the central `N`, impossible. Otherwise `exp Q=9`, and the image of the cube subgroup is a nontrivial complete cube subgroup in `Q`. If `cl(G)=6`, central quotienting gives `cl(Q)=5` or 6; if `cl(G)=7`, it gives `cl(Q)=6` (the lower central series cannot drop by two through an order-3 central kernel without stabilizing). Thus `Q` would be one of the empty filtered bases. Therefore no order-`3^8` direct revision-2 counterexample exists either.

Together with the complete order-`3^7` noncommuting-cube screen (and direct products with elementary abelian 3-groups for lower orders), any `p=3` direct counterexample must have order at least `3^9`. This is a finite catalogue floor, not the unrestricted answer and not a statement for other odd primes.

## 2026-08-17T10:43:10Z — order-6561 layer exhausted

Compute slot 1 is released immediately after normal process exit. Outcome remains `PARTIAL_RESULT`. Charged active time for the leased scan, preservation, and bounded deduction: 4 minutes. Scope cumulative charged time: 338 minutes. Thirteen minutes remain in the current increment ending at cumulative minute 351. No central extension or descendant was enumerated. The order-6561 TRI3 method is exhausted with empty residual family, and the run returns to `awaiting_lead` without parking the active counterexample direction or claiming the unrestricted scope answered.

## 2026-08-17T10:45Z — `MIN9-EQUALITY-QUOTIENT-TYPE`

Assume a quotient-minimal direct counterexample `H` at the reviewed `p=3` lower-bound equality `|H|=3^9`. Write `P=H^3` for the complete actual cube subgroup and `|P|=3^m`. The reviewed quotient-minimal reduction gives `exp(P)=3`, `P'=C=C3<=Z(H)`, and `P` has class 2. It also gives

`m>=5`, `[H:P]>=3^(m-floor((m-1)/3))`.

If `m>=6`, the logarithm of the resulting order bound is at least `2m-floor((m-1)/3)>=11`, contradicting `|H|=3^9`. Thus equality forces

`|P|=3^5`, `[H:P]=3^4`.  (E1)

The common invariant flag gives `dim Z(P)>=3`. Since `P` is nonabelian, `P/Z(P)` is a nonzero even-dimensional space under the alternating commutator form, so in total dimension 5 the centre has dimension exactly 3 and the quotient dimension exactly 2. The form

`B:P/Z(P) x P/Z(P)->P'=C`

has zero radical by the definition of the full centre and is nonzero; on a two-dimensional space it is the unique symplectic form up to basis. In the class-2 exponent-3 BCH Lie algebra, choose a symplectic basis `e,f`, let `[e,f]` span `C`, and complement `C` by two central vectors. This splits the Lie algebra as the three-dimensional Heisenberg algebra plus a central two-space. Hence

`P ~= H_3(3) x C3^2`, `Z(P)~=C3^3`, `P'=C3`.  (E2)

## Complete exponent-3 quotient list

Put `R=H/P`. Equation (E1) gives `|R|=3^4`, and `(hP)^3=P` for every `h`, so `exp(R)=3`.

For completeness, here is the needed two-generator exponent-3 calculation rather than a classification citation. From `(xy)^3=1`, moving the three `x` factors left gives `y^(x^2)y^x y=1`; applying the same formula to `xy^-1` and inverting gives `y y^x y^(x^2)=1`. Hence `y` commutes with `y^x`, so `[y,x]` commutes with `y`. Swapping `x,y` shows the same basic commutator commutes with `x`. Thus every two-generated exponent-3 subgroup is class at most 2; its derived group is generated by the single central commutator and has order at most 3, so it has order at most 27 and is a quotient of `H_3(3)`. Since `Phi(R)=R'`, let `d=dim R/R'`.

- If `d=4`, then `R'=1` and `R=C3^4`.
- `d=1` is impossible by the Burnside basis theorem: `R` would be cyclic, and exponent 3 would force order at most 3.
- `d=2` is impossible: it would make `R` two-generated, hence of order at most 27.
- If `d=3`, then `|R'|=3`. The lower central series cannot have class 3, since then nontrivial `gamma_3(R)<=R'` would equal `R'` and stabilize. Thus `R` is class 2. Its nonzero alternating commutator form from the three-space `R/R'` to the one-space `R'` has one-dimensional radical. Choosing a symplectic pair and a radical vector gives `R~=H_3(3)xC3`.

Therefore precisely

`R in {C3^4, H_3(3) x C3}`.  (E3)

## Complete outer-action/factor-system gate

Neither type in (E3) is eliminated by the equality count alone. A complete finite realization gate is as follows, and does not reuse the old fixed NS3 family.

Fix `P=H_3(3)xC3^2` with Lie algebra `L`, and one of the two groups `R`. Every extension is represented by:

1. an outer action `theta:R->Out(P)`;
2. chosen lifts `alpha_r in Aut(P)` of `theta(r)`, normalized at `1`, where `alpha_r(q)=sigma(r)q sigma(r)^-1` is explicitly left conjugation by a section representative;
3. a normalized factor system `f(r,s) in P` defined by `sigma(r)sigma(s)=f(r,s)sigma(rs)`, satisfying
   `alpha_r alpha_s=Inn_left(f(r,s)) alpha_(rs)` and
   `f(r,s)f(rs,t)=alpha_r(f(s,t))f(r,st)`.

With multiplication `(p,r)(q,s)=(p alpha_r(q) f(r,s),rs)`, these data cover every group extension `1->P->H->R->1`, up to the usual change-of-lifts equivalence. Retain exactly the finite data satisfying all of:

- `exp(H)=9`, `H^3=P`, and the complete cube map from all pairs `(p,r)` is surjective onto `P` (actual values, not just generation);
- `P'=C` is fixed pointwise by every `alpha_r`, and `C` is the unique order-3 subgroup of `Z(H)` (equivalently `Omega_1(Z(H))=C`);
- for every represented element `x=p sigma(r)` with `a=x^3`, its right-conjugation action is explicitly `A_x=alpha_r^-1 o (q |-> p^-1 q p)` and obeys `(A_x-I)^3=D_a` on `L`;
- for noncentral `a`, equality in the Jordan-chain argument forces `A_x-I` to have type `J4+J1`, with fixed space exactly `<C,a>`; central cubes have `(A_x-I)^3=0`;
- the quotient-minimal rows `P'=C`, `P cap Z(H)=C`, and nonabelianity of the actual cube subgroup hold.

The cube formula is finite and explicit from the displayed multiplication: for each of the 81 quotient elements and 243 kernel elements, multiply `(p,r)` three times. Thus the two fixed isomorphism types and the full finite outer-action/factor-system data are the precise residual equality family. No computation or family enumeration is authorized or performed.

There is one sharper action-only gate. For a noncentral cube `a=x^3`, equality makes `N=A_x-I` have one length-4 chain ending in `c in C` and the independent fixed vector `a`. On `L/Z(P)` (dimension 2), `N^2=0`, so the last two nonzero positions of that chain lie in `Z(P)`. Since the full fixed space of `N` is `<c,a>` and `a` is noncentral, the restriction to the three-space `Z(P)` has fixed space exactly `C` and Jordan type `J3`. Actual-cube surjectivity therefore requires outer-action elements whose induced action on `Z(P)` is regular unipotent `J3`; inner automorphisms act trivially on the centre, so this is well-defined at the outer-action level.

A precise bounded next step for a fresh increment is consequently: construct `Out(H_3(3)xC3^2)` once; enumerate, up to `Aut(R)` and `Out(P)` conjugacy, homomorphisms from each of the two groups in (E3); retain exactly those whose induced `Z(P)`-module has common fixed space `C` and contains a `J3` element; only then enumerate compatible factor-system classes and apply the 81-by-243 cube/action gates. This is disjoint from the old fixed NS3 action family and avoids raw group-descendant generation.

The outer-action target itself has a closed coordinate model. Write `L=V direct_sum C direct_sum W`, with `dim V=dim W=2`, `C=<c>`, and `[e,f]=c` on `V`. Every automorphism is uniquely described by

- `g in GL(V)`, acting on `C` by `det(g)`;
- `h in GL(W)` and `lambda in Hom(W,C)`;
- an arbitrary central shear `tau in Hom(V,C direct_sum W)`.

Inner automorphisms are exactly the two-dimensional subspace of shears `V->C` arising from the symplectic form. Thus this matrix model gives all of `Out(P)` without a group catalogue. For a 3-group outer action the determinant on `C` is automatically 1. On `Z(P)=C direct_sum W` the action has unipotent block form `[[1,lambda],[0,h]]`. A fixed-line-`C` image containing `J3` lies in a conjugate of `UT_3(3)`: for `R=C3^4` its central-module image is an abelian subgroup of the `C3^2` unipotent centralizer of a regular block, whereas for `R=H_3(3)xC3` it may additionally have the full nonabelian `UT_3(3)` image. These are action-image cases for a next audit, not existence claims.

Numerically `|Aut(P)|=|GL_2(3)|^2*3^8` and `|Out(P)|=|GL_2(3)|^2*3^6`; a Sylow-3 subgroup of `Out(P)` has order `3^8`. The central-module stage is much smaller. Up to change of basis in an abelian `R=C3^4`, an eligible image is either the cyclic group generated by one regular `J3`, or the full elementary-abelian `C3^2` unipotent centralizer of that block. For `H_3(3)xC3`, the image is either one of those abelian cases (factoring through the abelianization) or all of `UT_3(3)`, since every proper subgroup of the order-27 Heisenberg group has order at most 9 and is abelian. These three central-module branches are the first exact partition for the next outer-action orbit filter.

The elementary coverage count does not kill any branch. A noncentral cube can occur only over a quotient element acting as `J3` on `Z(P)`, and there are 216 noncentral elements of `P`; at at most nine cube values per root coset, at least 24 such cosets are necessary. In the cyclic-image and `C3^2`-image branches, exactly 54 of the 81 quotient elements map to regular blocks. For full `UT_3(3)` image, 12 of its 27 elements are regular (`a,b!=0` in `I+aE12+bE23+cE13`), giving 36 quotient preimages when the kernel has order 3. Thus all three branches pass this necessary count. The residual obstruction genuinely lies in the full outer shears/factor system and cube-surjectivity equations.

## 2026-08-17T10:57:00Z — equality-structure checkpoint

Outcome remains `PARTIAL_RESULT`. Charged active time for the equality reconstruction, quotient classification, and finite outer-action/factor-system gate: 13 minutes. Scope cumulative charged time: 351 minutes, reaching the current increment cap. No computation, extension enumeration, descendant generation, or old NS3-family repair was performed. The two quotient types and three central-module action branches are the precise residual equality family. A bounded next-step request is on the file bus; the run remains `awaiting_lead` and the overall counterexample direction is not parked.

## 2026-08-17T11:23:01Z — `MIN9-CENTRAL-MODULE-ACTION` work start

Lead grants exactly 60 new active minutes, from scope cumulative minute 351 to at most 411. The only live strategy is `MIN9-CENTRAL-MODULE-ACTION`. Categorical enumeration stops by increment minute 45 and packaging begins by minute 48. This increment opens no factor system, cocycle, descendant, catalogue, or previously stopped construction family.

Scope remains revision 2 and counterexample-directed: `p=3>2`, a finite 3-group of exact exponent 9, the complete actual cube-value set itself a subgroup, and nonabelianity of that subgroup. The equality analysis is conditional on a quotient-minimal direct counterexample of order `3^9`; an action survivor is only a finite handoff and cannot answer the unrestricted scope.

The relevant Validator verdict was read first and preserves only the independently replicated direct floor `|H|>=3^9` at `p=3`, with the corrected central-quotient class drop of zero or one. The stale CPTR inbox item remains unopened because CPTR material is expressly excluded.

### Coordinate reconstruction before enumeration

Write the exponent-three class-two Lie algebra of `P=H_3(3) x C3^2` as

`L=V direct_sum C direct_sum W`, `dim(V,C,W)=2+1+2`, `[v,v']=omega(v,v')c`.

With column coordinates in the block order `(V,C,W)`, every automorphism has matrix

```text
[ g          0       0 ]
[ tau_C   det(g)   lambda ]
[ tau_W      0       h ]
```

where `g,h in GL_2(3)`, `lambda:W->C`, and `tau_C,tau_W` are arbitrary maps from `V`. Direct bracket checking gives `[gv,gv']=det(g)omega(v,v')c`, while every added `C direct_sum W` component is central, so these matrices preserve the bracket. Conversely an automorphism preserves `Z(L)=C direct_sum W`, its derived line `C`, and the induced nondegenerate two-space `V`; this forces exactly the displayed blocks. The two-dimensional `tau_C:V->C` subgroup is precisely `Inn(P)`, since `a in V` induces the shear `v |-> v+[v,a]` and the symplectic form identifies `V` with `V^*`.

Therefore

`|Aut(P)|=|GL_2(3)|^2 3^(2+4+2)=|GL_2(3)|^2 3^8`,

`|Out(P)|=|GL_2(3)|^2 3^6`, and a Sylow-3 subgroup of `Out(P)` has order `3^(2+6)=3^8`. On `Z(P)=C direct_sum W`, a Sylow-3 element restricts to `[[1,lambda],[0,h]]`. The frozen script will reconstruct every one of these orders and test the bracket on the five basis vectors before any subgroup lattice call; a mismatch is the minute-12 hard kill.

For a prospective noncentral cube vector `abar=(a_1,a_2) in V`, the right-inner nilpotent shear convention is

`D_abar(e)=a_2 c`, `D_abar(f)=-a_1 c`,

because right conjugation gives `v |-> v+[v,abar]`. For every outer element `u`, the script will inspect exactly the nine matrices in the `Inn(P)`-fibre over `u^-1`, test ranks `(3,2,1,0)`, exact equality `N^3=D_abar`, and equality of the projected fixed space with `<abar>`. This fixes the sign and the `u^-1` convention before the capacity test.

### 2026-08-17T11:28:54Z — frozen script and heavy-lease request

Frozen script: `scratch/min9_central_module_action.g`  
SHA-256: `80d0f3dc8684b7cb6cdf5fa7b7c367986658adb95fb7d2c72ee3f9f4c2911f4c`  
Length: 492 lines, 17,341 bytes.

The script constructs the matrix automorphism group and its exact inner quotient, enumerates Sylow-3 subgroup classes and full-outer fusion, partitions epimorphisms for both quotient types, checks all nine inner lifts against the `J4+J1` profile, and evaluates the eight-demand max-flow gate. Every categorical and orbit-size partition is printed. It contains no factor-system or cocycle construction.

A heavy-slot request was sent for exactly one run of the frozen command with `timeout 900s`, output redirected to `scratch/min9_central_module_action.out`, one slot, RAM estimated below 1 GiB. No GAP command has been run. Charged position is increment minute 6, scope cumulative minute 357; lease waiting is uncharged.

Static inspection then replaced the convenience `UnitriangularGroup`/direct-product constructor for `R=H_3(3)xC3` by explicit tracked block matrices `I+E12`, `I+E23`, `I+E45`, removing a constructor-version dependency without changing the enumeration. The superseding frozen SHA-256 is `dd447897dff2b864b4877b74e7adc3b16607e9a77f77f5265b5971a74ac4dd18`, length 490 lines and 17,262 bytes. A corrected request supersedes the first hash. No GAP command has been run.

### 2026-08-17T11:34:37Z — first leased command: parser/global-name frontier

Lead's grant matched the original hash `80d0f3dc...`, so that exact 492-line file was restored and the authorized command was run once. GAP exited before constructing `Aut(P)` because the attempted private helper name `LieBracket` collides with a pre-existing read-only GAP global. The complete six-line output is preserved at `scratch/min9_central_module_action.out`, SHA-256 `e27608d700b9cb0d8d858dee956b9f753d94c288a436049e3ba5d49ae317d825`:

```text
Error, Variable: 'LieBracket' is read only
not in any function at Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/\
scratch/min9_central_module_action.g:41
type 'quit;' to quit to outer loop
Reading file "Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-prod\
uct-defect/scratch/min9_central_module_action.g" has been aborted.
```

No coordinate, subgroup, epimorphism, lift, flow, factor-system, or cocycle row was evaluated. Slot 1 is released immediately. This is an operational failure and supplies no mathematical evidence.

The observed collision alone was corrected to the private name `MIN9LieBracket`; the explicit tracked block constructor was retained. New frozen SHA-256: `ea38b134c043978c28f423d65255e4c90a208059c4923ab53449564920ccbd10`, 490 lines, 17,274 bytes. A fresh hash-matched lease request was sent. Charged position is increment minute 12, scope cumulative minute 363; lease waiting is uncharged.

### 2026-08-17T11:55:05Z — fresh leased run: complete prefusion timeout frontier

The fresh lease matched SHA-256 `ea38b134...`. The command ran once and exited with code `124` at the exact 900-second timeout. Slot 1 is released. Complete output is preserved at `scratch/min9_central_module_action.out`, SHA-256 `73545fc241689ae1b45c3fa035612c179a1f6f83e6da164e4ead0fb3b396048e` (11 lines, 595 bytes).

The coordinate reconstruction passed: bracket preservation on every generator, `|Aut(P)|=15116544`, `|Inn(P)|=9` and normal, `|Out(P)|=1679616`, and Sylow-3 order `6561`. The complete Sylow subgroup lattice has 17,409 conjugacy classes. The exact prefusion partitions are:

| quotient type | permitted Sylow classes | actual subgroups represented | central-gate classes | central-gate subgroups represented |
|---|---:|---:|---:|---:|
| `C3^4` | 8,797 | 96,163 | 500 | 11,892 |
| `H_3(3)xC3` | 12,258 | 133,410 | 2,366 | 36,738 |

The timeout occurred inside the naive pairwise full-`Out(P)` fusion loop. No fusion completion marker, epimorphism partition, lift profile, max flow, survivor count, factor system, or cocycle was produced. Thus neither quotient type is eliminated and the active assignment is unanswered.

Charged position is increment minute 27, scope cumulative minute 378. The concrete representation-preserving optimization is to apply the conjugacy-invariant nine-lift/flow gate to all 2,366 retained Sylow classes first, discard failures, then bucket survivors by image type, central branch, and lift-profile multiset before any full-outer conjugacy call. This changes the order of exact filters, not the family. No rerun is made without a fresh Lead decision and hash-matched lease.

### Closed lift-fibre reduction

Let a lift over an outer element inverse have `N=A-I` in blocks

```text
N = [ G      0    0 ]
    [ alpha  0  lambda ]
    [ T      0    H ] .
```

The inner fibre varies exactly `alpha in Hom(V,C)`. Since the outer element lies in a 3-subgroup, `G^2=H^2=0`. Multiplication gives

`N^3(V)=(lambda(TG+HT), HTG)` in `C direct_sum W`,

and zero on `C direct_sum W`; crucially this is independent of `alpha`.

For a regular `J3` restriction on `C direct_sum W`, `rank H=1` and `lambda H!=0`. Hence `im H=ker H`, and `lambda` is nonzero on that line. Put `r=lambda(TG+HT)`. Exact equality `N^3=D_abar` is equivalent to

`HTG=0`, `r!=0`, and `r=(abar_2,-abar_1)`.

These rows automatically imply the remaining lift tests. First `rG=lambda HTG=0`, so `N^4=0`; nonzero rank-one `N^3` on dimension five forces Jordan partition `J4+J1`. Second, projecting `ker N` to `V` gives

`K={v in ker G:T v in im H}`,

because the free `ker H` coordinate solves the central equation for every `alpha`. If `G=0`, then `K=ker((lambda H)T)=ker r=<abar>`. If `rank G=1`, then `im G=ker G=L`; `HTG=0` gives `T(L)<=imH`, hence `K=L`, while `rG=0` gives `L=ker r=<abar>`.

Thus all nine inner lifts pass for one uniquely determined nonzero `abar`, or none passes: `n_u(abar)` is always 9 or 0. The flow reduces to the histogram formula

`sum_(abar!=0) min(27,9k*m_abar)`, `k=81/|U|`,

where `m_abar` counts eligible outer elements with that label. This exact hand reduction removes the inner-fibre loop and network algorithm from the optimized profile-first pivot. It is not yet a quotient elimination.

### Small action images fail capacity

Each centrally regular `u` can feed only its unique label, and the demand-node cap limits its contribution to at most 27. A cyclic regular central image has `2|U|/3` regular preimages; the elementary `C3^2` centralizer has `6|U|/9=2|U|/3`; full `UT3(3)` has `12|U|/27=4|U|/9`.

Hence `|U|=3` has at most two contributing elements and flow at most 54, while `|U|=9` has exactly six and flow at most 162. Both are strictly below 216. Every order-3 or order-9 action image is eliminated before fusion, for both quotient types. The residual image types are `C3^3,C3^4` for the abelian quotient and `C3^3,H_3(3),H_3(3)xC3` for the nonabelian quotient. This is only a conditional action-level exclusion.

### 2026-08-17T12:00:43Z — `PROFILE-BEFORE-FUSION` frozen

On Lead's exact continuation decision, the script was mechanically reordered within the three-minute freeze limit. It now profiles all 2,366 central-gate Sylow classes first, prints every completed row, retains flow survivors, buckets them by image order/central branch/sorted label histogram, and performs full-outer fusion and epimorphism enumeration only afterward. No family or observable changed.

Frozen SHA-256: `ba0b74b5f3d3e0ba6604c8d4399f925cd9decbd2fc8f3803753fb78b62241cdd`; 508 lines, 18,475 bytes. A fresh one-run `timeout 900s` lease was requested with output directed to `scratch/min9_profile_before_fusion.out`, preserving the prior timeout file. No command has been run. Charged position at freeze is cumulative minute 384 at most; lease waiting is uncharged.

### 2026-08-17T12:10:26Z — final categorical run complete; packaging

Lead matched the frozen hash and granted the final slot-1 lease. The exact authorized command ran once and exited normally with code `0` before the 900-second timeout. Slot 1 is released immediately. No rerun is authorized or attempted.

Complete output: `scratch/min9_profile_before_fusion.out`, SHA-256 `b1b187eb3add7ef6154ff3aa1b32eda390c1e1c50877bb23043a26eee01b17ab`, 22,408 lines and 1,504,811 bytes.

The coordinate and complete prefusion counts reproduce the timeout frontier. The union contains 2,398 central-pass Sylow classes: 500 eligible for `C3^4`, 2,366 eligible for `H_3(3)xC3`, with overlap 468. Every union class received its complete nine-lift table and exact max flow. The distribution is:

`flow 0: 158`, `flow 54: 1736`, `flow 108: 336`, `flow 162: 168`, `flow 216: 0`.

Thus all 2,398 classes fail, and the terminal output is:

```text
PREFUSION_LIFT_PROFILE_COMPLETE survivors=0 survivor_C3^4_sclasses=0 survivor_H3xC3_sclasses=0
FULL_OUTER_FUSION_COMPLETE prefusion_survivors=0 full_outer_classes=0
SURVIVOR_COUNTS quotient_C3^4_outer_orbits=0 quotient_H3xC3_epimorphism_orbits=0
STATUS=MIN9_CENTRAL_MODULE_ACTION_COMPLETE active_assignment_answered=no factor_systems_opened=0 cocycles_opened=0
```

The single lexical warning concerns the already assigned global `profile` captured by an immediately evaluated anonymous function which only constructs a sorted label histogram. All rows ran, the flow uses `profile` directly, and normal completion occurred.

Conditional on Validator reconstruction of the equality dependencies and capacity implication, the order-`3^9` equality family is empty and the direct `p=3` floor rises to `3^10`. This is a bounded conditional partial, not an answer for larger 3-groups or `p>3`. No factor system or cocycle was opened.

Packaging begins immediately, well before the active cap. Conservative charged position at run exit is scope cumulative minute 390; the remaining budget is not spent on a new method. Run state returns to `awaiting_lead` after the Validator/Lead report.
