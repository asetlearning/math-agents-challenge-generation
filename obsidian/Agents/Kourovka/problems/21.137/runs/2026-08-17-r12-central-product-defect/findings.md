---
title: "Kourovka 21.137 — anti-diagonal cube-image formula and MON15 seed exclusion"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
direction: counterexample
outcome: PARTIAL_RESULT
previous_outcome: BLOCKER
run_state: awaiting_lead
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/central-products, topic/algebra-groups, project/kourovka, status/conjectured]
---

# Anti-diagonal cube-image formula and one finite seed exclusion

## Active target

Scope: `21.137/odd-prime-exponent-p2`  
Assignment revision: 2

Target: for an odd prime `p`, a finite `p`-group `G` of exponent exactly `p^2` whose complete actual power set `P={g^p:g in G}` is a subgroup; decide whether `P` must be abelian. The counterexample direction requires one admissible group with nonabelian `P`.

## Partial result

For an anti-diagonal quotient of two seed groups, the complete actual-power set and its closure obstruction admit the exact formulas below. Applying them to one fully frozen `p=3` monomial-algebra seed gives a hand-checkable noncentral closure defect. The seed central product retains noncommuting actual cubes, has exact exponent `9`, but its complete cube set is not a subgroup. It is therefore ruled out as an `OUT_OF_SCOPE_EXAMPLE`.

## Exact anti-diagonal formula

Let `C_i=<z_i><=Z(A_i)` have order `p`, let

`D=<(z_1,z_2^{-1})>`, `H=(A_1 x A_2)/D`,

and let `q` be the quotient map. With `S_i={a^p:a in A_i}` as actual value sets,

`Pow_p(H)=q(S_1 x S_2)`

and

`q^{-1}(Pow_p(H))=union_{k in F_p}(z_1^kS_1)x(z_2^{-k}S_2)`.  (1)

For `x,x' in S_i`, put

`Delta_i(x,x')={k in F_p:z_i^{-k}xx' in S_i}`.

The sets `S_i`, hence `q(S_1 x S_2)`, contain the identity and are inverse-closed. Therefore `Pow_p(H)` is a subgroup exactly when

`Delta_1(x,x') intersect (-Delta_2(y,y')) != empty`  (2)

for every `x,x' in S_1` and `y,y' in S_2`. Also

`[q(x,y),q(x',y')]=q([x,x'],[y,y'])`.  (3)

Thus this construction can cancel only errors in the chosen central directions; (3) separately tests whether noncommuting actual values survive.

In fibre language, if `T_i=S_iC_i/C_i` and `F_{i,t} subset F_p` is the central support over `t`, the residual central support over `(t,u)` is `F_{1,t}+F_{2,u}` up to section translation. For a self-product at `p=3`, supports of size at least two have full sum by the three-element case of Cauchy–Davenport, but the projected actual-cube set `T` must still be a subgroup.

## Frozen row `MON15-SELF`

Let

`J=span_F3{x^i y^j:0<=i,j<=3,(i,j)!=(0,0)}`

with `x^4=y^4=yx=0`. Set `A=1+J`, `c=x^3y^3`, `C=1+F_3c`, and

`H=(A x A)/<((1+c),(1-c))>`.

This is one exact finite row, independent of any UT7 or wreath-shaped material.

- `dim_F3 J=15`, so `|A|=3^15` and `|H|=3^29`.
- `J^7=0`, hence `(1+X)^9=1`; `(1+x)^3=1+x^3 !=1`, so both `A` and `H` have exponent exactly `9` (the first factor embeds in `H`).
- `c` annihilates `J` on both sides, so `C` is central of order `3`.
- Every actual cube in `A` is exactly `1+R^3`.

Write `R=a+b+m`, where `a` is x-pure, `b` is y-pure, and `m` is mixed. The defining products give

`R^3=a^3+b^3+a^2b+ab^2+a^2m+amb+mb^2`.  (4)

If `alpha=[x]R` and `beta=[y]R`, then

`[x^3]R^3=alpha`, `[y^3]R^3=beta`,

`[x^2y]R^3=alpha^2*beta`, `[xy^2]R^3=alpha*beta^2`.  (5)

Take

`r=2y+2xy+x^2`, `s=y^2+x+xy^3`.

Equation (4) yields

`u=r^3=2y^3+2xy^3+x^2y^2+x^3y^2`,

`v=s^3=x^3+x^2y^2+c`.

Modulo `F_3c`, `u+v` has `alpha=1,beta=2` but zero `x^2y` and `xy^2` coordinates; (5) would require `2` and `1`. Hence `u+v` is not a cube modulo `F_3c`. Since `uv=0`,

`(1+u)(1+v)=1+u+v`.

The two actual cubes `q((1+r)^3,1)` and `q((1+s)^3,1)` in `H` therefore have a product outside `Pow_3(H)`, even after every possible anti-diagonal central correction.

The desired noncommutativity does survive:

`[1+x^3,1+y^3]=1+c`,

and `q(1+c,1)` is nonidentity. Thus the exact failure is closure, not loss of the noncommuting-cube observable.

## Constraint-and-conclusion matrix for the tested row

| constraint_id | role | candidate value / evidence | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | only one explicit candidate row was tested; it does not refute the universal assertion | not a scope claim |
| `21.137-odd-p-not-2` | admissibility | `p=3` | pass |
| `21.137-odd-finite-p-group` | admissibility | `H` is a finite group of order `3^29` | pass |
| `21.137-odd-exponent-p2` | admissibility | `exp(H)=9=3^2` | pass |
| `21.137-odd-power-set-definition` | admissibility | equations (1), (4), and the exact enumerator use every actual cube | pass |
| `21.137-odd-power-set-subgroup` | admissibility | the displayed two-cube product is outside the actual cube set | **fail** |
| `21.137-odd-P-abelian` | target conclusion | noncommuting actual cubes survive, but there is no subgroup `P` under the hypothesis | not eligible / out of scope |

Because one admissibility row fails, this is not a candidate counterexample and no claim-check file is created.

## Computation record

Script: `scratch/monomial_seed.py`  
Interpreter: Python 3.12.3  
SHA-256: `03f99aec99519ea2133def089f3a033526ecfb2de367ea5df7016d0c58e25bd5`

Command:

`timeout 30s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/monomial_seed.py`

It enumerates the exact cube image as 729 affine-linear mixed-coordinate images. Observed summary:

```text
cube_image_size=1947
quotient_cube_image_size=649 span_rank=9
quotient_cube_image_additive_subspace=False
central_fibre_size_histogram={3: 649}
identity_central_fibre=[0, 1, 2]
x3y3_minus_y3x3_equals_c=True
all_central_fibres_at_least_two=True
seed_gate=FAIL: quotient actual-cube image is not a subgroup
```

The explicit calculation above independently explains the failure without relying on the global counts.

## What this establishes and what it does not

It establishes a reusable exact closure formula for anti-diagonal central products and excludes the single frozen row `MON15-SELF`. It shows why abundant central fibres alone do not help: quotient-level closure must be checked first.

The seed exclusion does **not** establish that every anti-diagonal central product fails and does not answer the unrestricted active scope. The refinement below classifies the formal two-point-fibre pattern and isolates the remaining realization gap. A potentially viable new seed would need, before gluing, a projected actual-cube set that is a subgroup, central supports large enough to fill sums, and a nonzero commutator surviving the anti-diagonal kernel.

## REFINE: exact `F_3` support-family classification

For a seed actual-cube set `S`, central `C=<z>` of order 3, and

`Delta(x,y)={k:z^{-k}xy in S}`,

let `D` be the family of distinct nonempty supports that occur. Actual powers give

`Delta(y^{-1},x^{-1})=-Delta(x,y)`, `Delta(y,x)=Delta(x,y)`,

and `Delta(1,1)` is either `{0}` or `F_3`. Thus `D` is negation-closed and contains an allowed identity support. Under negation closure, the self-product condition `A intersect (-B) != empty` is equivalent to ordinary pairwise intersection of the supports.

With `O={0}`, `A={0,1}`, `Abar={0,2}`, `B={1,2}`, and `U=F_3`, the exact formal list is:

| row | occurrence family | common intersection |
|---|---|---|
| F1 | `{U}` | `U` |
| F2 | `{O}` | `O` |
| F3 | `{O,U}` | `O` |
| F4 | `{B,U}` | `B` |
| F5 | `{A,Abar,U}` | `O` |
| F6 | `{O,A,Abar}` | `O` |
| F7 | `{O,A,Abar,U}` | `O` |
| F8 | `{A,Abar,B,U}` | empty |

`scratch/defect_family_classifier.py`, SHA-256 `56a9629e39329160f376a33dbcf22b8396b132e2902e1a59b8e90f9329827f13`, exhausts all 127 nonempty families and returns exactly these eight.

### Common-shift rows

A single correction works for every ordered defect pair exactly when the global intersection is nonempty (negation closure supplies both `k` and `-k`). For an actual inverse-closed `S`, such a shift forces `S` itself to be a subgroup. For `k=0` this is immediate. For `k!=0`, `z^{-k}S` contains the identity and is closed under products and inverses; because it contains `z^{-k}`, its central translate `S` is the same subgroup. It then follows that every `Delta(x,y)` equals `Delta(1,1)`. Consequently the only realizable common-shift occurrence families are the constant rows `{O}` and `{U}`; all other common-shift rows are formal set systems that collapse under seed multiplication. They offer no novel closure repair.

### Unique triangle row

The only no-common-shift family is

`TRI3={ {0,1}, {0,2}, {1,2}, F_3 }`.

It has the following exact set-level realization criterion. Put `T=SC/C` and, after choosing representatives `r_t`, let `F_t={a:z^a r_t in S}`. Then TRI3 occurs exactly when:

1. `T` is a subgroup of `A/C`;
2. every occupied central fibre has size 2 or 3;
3. at least one fibre has size 2.

TRI3 forces the identity fibre to be full, so `C subset S`. Conversely, two subsets of `F_3` of size at least two always meet after negation; a two-point fibre and its three central translates give all three two-point supports. This is precisely the only formal defect-cancellation pattern not reducible to an already-closed seed.

Conditional constructor: if a finite exponent-9 `3`-group `A` has `S=Pow_3(A)`, a central order-3 `C`, the TRI3 fibre criterion, and a noncommuting pair in `S`, then `(A x A)/<((z),(z^{-1}))>` is an in-scope counterexample. This is a criterion, not an exhibited group.

Indeed, for the natural map `rho:H->(A/C)x(A/C)`, every fibre of `Pow_3(H)=q(SxS)` over `T x T` has support `F_t+F_u=F_3`; hence `Pow_3(H)=rho^{-1}(T x T)`, a subgroup. A factor `A` embeds in `H`, so exact exponent 9 and any noncommuting pair of seed cube values survive.

### Realization gap

No actual cube map realizing TRI3 is supplied. A formal support table does not enforce cube roots, exact exponent, conjugacy, commutators, or associativity. In particular, associativity requires equality of the two total-correction sets

`union_{k in Delta(x,y)}(k+Delta(z^{-k}xy,w))`

and

`union_{m in Delta(y,w)}(m+Delta(x,z^{-m}yw))`

for every `x,y,w in S`. The frozen `MON15-SELF` row has only full central fibres and its projected cube image is not a subgroup, so it misses TRI3 at the separate quotient gate.

Pointwise, `Delta(x,1)` always contains zero, so TRI3's `{1,2}` support must occur on a genuine two-input product. Also, whenever actual cubes `x,y` satisfy `1 != [x,y] in C`, their conjugacy orbits fill `xC` and `yC`; those fibres have size three. Thus in the reviewed minimum-central configuration, any required size-two fibres must lie in the radical of the central commutator pairing. This is a necessary realization constraint, not an existence or impossibility result.

## Official order-2187 SmallGroups exhaustion

Lead authorized an exhaustive screen of every SmallGroups group of order `3^7=2187`. The deterministic script `scratch/tri3_order2187.g` has SHA-256

`446e78854e3b91e3ccce726d28b8ae04e8761d7a94303488aeebe7cc987a96d0`.

It contains all mandated gates and, on a seed hit, the independent full central-product validation. Two initial leased commands stopped at the availability guard because Ubuntu's `gap-smallgrp-extra 1.5.3-1` does not contain SmallGrp group-data layer 11. Lead then provisioned the official SmallGrp 1.6.0 release locally, including `small11`, and granted one fresh lease for the unchanged hash under the rooted GAP path.

Exact command:

`timeout 55s gap -l 'Agents/Kourovka/tools/gaproot;/usr/share/gap' -q < Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/tri3_order2187.g`

It exited normally with code 0 after about 31.8 seconds. Salient complete output was:

```text
TRI3_ORDER2187_BEGIN gap_version=4.12.1 smallgrp_loaded=true
library_order=2187 group_count=9310
PROGRESS i=9300 exp9=8296 noncomm=0 fibre_gate=0
COMPLETE_SCAN=yes groups=9310 exp9=8302 noncomm_cube_seed=0 central_C_in_S=0 projected_subgroup=0 fibre_gate=0 seed_hits=0
STATUS=NO_SEED_IN_ORDER_2187_LAYER
```

Every official ID `1..9310` completed. Exactly 8302 groups passed `Exponent(G)=9`. For every such group, the script enumerated all 2187 elements and formed the complete actual-cube set. None of those complete cube sets contained a noncommuting pair. Consequently:

- no group of order 2187 in the official SmallGrp 1.6.0 catalogue is a direct revision-2 counterexample, because every exact-exponent-9 row has pairwise commuting actual cubes;
- no such group realizes the TRI3 seed criterion with the required noncommuting seed cubes, so the order-2187 seed layer is exhausted.

The later counters are zero because the noncommuting-cube gate precedes them; this run does not separately assert that no central order-3 subgroup lies in a cube set or that no projected cube set is a subgroup. The exhaustion is strictly order 2187 at `p=3`. It says nothing about larger 3-groups, other odd primes, or the unrestricted existence question.

## Order-6561 TRI3 seed reduction

Let `A` be a hypothetical exponent-9 TRI3 seed of order `3^8`, let `S=Pow_3(A)`, and choose noncommuting `s,t in S`, with `c=[s,t] !=1` under `[u,v]=u^-1v^-1uv`.

For every `N<=Z(A)` of order 3, `A/N` has order 2187 and exponent 3 or 9. In the exponent-3 case its cubes are trivial; in the exponent-9 case the completed official catalogue result says its complete cube set is pairwise commuting. Thus `c in N` for every such `N`. In particular `c` is central of exact order 3. Distinct order-3 subgroups intersect trivially, so `Z(A)` has a unique one and is cyclic. Since `exp(A)=9`, its centre is `C3` or `C9`.

The TRI3 subgroup `C` is the unique central order-3 subgroup. If `Z(A)=<z>` has order 9, then `C=<z^3>` and, for every actual cube `x^3`,

`(xz^k)^3=x^3z^(3k)` for `k=0,1,2`.

This fills every occupied `C`-fibre with all three points, independently of section translation, contradicting the required two-point fibre. Therefore

`Z(A)=C=C3`.  (Z)

### Projective closure excludes class at most five

The reviewed integral class-five identity remains effective under the weaker TRI3 hypothesis. Put `U=SC`, the preimage of `T=SC/C=Pow_3(A/C)`. Since `T` is a conjugacy-invariant subgroup, `U` is normal. Every `u in U` is `u=x^3d` with `d in C`, so centrality and exponent 9 give `u^3=1`.

The four terminal elements in the identity all lie in `U`: `[y,x^3]=(x^-3)^yx^3 in U`, stripping the actual cubes `c^3,a^3` gives `T_A in U`, and normality gives `S_A=[T_A,y] in U`; likewise `[x,y^3]=(y^-3)^xy^3 in U`, stripping `q_1^3,q_2^3` gives `T_B in U`, and normality gives `Q=[T_B,x] in U`. In the reviewed identity

`[x^3,y^3]=c^-9a^-9b^-9beta^-9delta^54epsilon^27 T_A^-3S_A^-3T_B^3Q^3`,

the first factors vanish by exponent 9 and the terminal factors vanish because `exp U=3`. Thus projective cube closure already forces cube commutativity in class at most 5. A TRI3 seed of order `3^8` has class 6 or 7 only.

### Exact quotient bases and extension parameters

With (Z), put `Q=A/C`. Then `|Q|=2187`, `exp Q=9` (exponent 3 would force `S<=C`), and the nontrivial complete set `Pow_3(Q)=SC/C` is a subgroup. If `cl(A)=6` or 7, then `gamma_cl(A)(A)=C` and `cl(Q)=5` or 6 respectively. Hence the only quotient bases are official `(2187,i)` rows with:

1. exponent 9;
2. class 5 or 6;
3. nontrivial complete actual-cube set;
4. that set itself a subgroup.

For each base `Q`, every remaining seed lift is covered by a normalized central cocycle `f in Z^2(Q,F_3)` via `A_f=F_3 x_f Q`. With

`kappa_f(q)=f(q,q)+f(q^2,q)`, every lift of `q` has cube `(kappa_f(q),q^3)`, so the exact fibre support is `F_t(f)={kappa_f(q):q^3=t}`. This supplies the complete TRI3 fibre gates. The condition `Z(A_f)=F_3` is exactly that no nonidentity `q in Z(Q)` has `f(q,r)=f(r,q)` for every `r`. Exponent, class, and noncommuting complete-cube gates finish the finite test. Equivalently, a seven-generator pc presentation has at most 28 central tail coordinates—seven power and 21 conjugation tails—subject to consistency; all consistent tails cover all central extensions, with coboundary/isomorphism duplicates allowed.

### Complete base filter: the residual order-6561 lift family is empty

Under a one-command Lead lease, `scratch/tri3_order2187_quotient_base_filter.g` (SHA-256 `a4919904da10d49cce1e29e311c1631774261fc726e16f45b0d116b9d94cd1ef`) visited every official SmallGrp 1.6.0 ID `1..9310`. It exited normally after `16.909420981` seconds with:

```text
COMPLETE_BASE_FILTER=yes groups=9310 exp9=8302 class56=26 nontrivial_cube=26 cube_subgroup=0
STATUS=QUOTIENT_BASE_FILTER_COMPLETE
```

Complete stdout is preserved at `scratch/tri3_order2187_quotient_base_filter.out`, SHA-256 `bb6af353acd79474fdbb3a43815e7efed54f4e4b52cb8d9de0c931a29d18df30`. Exactly 26 exponent-9 rows had class 5 or 6; all had nontrivial complete cube sets, but none of those sets was a subgroup. Therefore there is no quotient base and hence no order-6561 TRI3 seed. No central extension or descendant enumeration is needed for this layer.

The same empty base list excludes a direct order-6561 counterexample. For such a group with a nonabelian cube subgroup, the central-quotient proof gives a unique central order-3 subgroup `N`; class at most 5 is already excluded. For class 6 or 7, `Q=G/N` has exponent 9, class 5 or 6, and a nontrivial complete cube subgroup, contradicting the filter. (Exponent 3 would put every cube in central `N`.) Thus any direct `p=3` counterexample has order at least `3^9`: orders through `3^7` have commuting cube values by the official scan (lower orders embed after direct product with elementary abelian factors), and order `3^8` is excluded here. This is only a finite `p=3` floor.

## Equality structure at the first possible direct order `3^9`

Assume a quotient-minimal direct counterexample `H` has order `3^9`, and put `P=H^3`. Equality in the reviewed affine bound forces `|P|=3^5` and `|H/P|=3^4`: if `|P|=3^m`, then `m>=5` and the order logarithm is at least `2m-floor((m-1)/3)`, which already exceeds 9 at `m=6`.

The quotient-minimal rows give `exp P=3`, class 2, and `P'=C3`. The common-flag bound gives `dim Z(P)>=3`. Since the nonzero alternating commutator form on `P/Z(P)` has even positive dimension, total dimension 5 forces `dim Z(P)=3` and `dim P/Z(P)=2`. Its radical is zero by the definition of the full centre. Splitting the three-dimensional centre into `P'` and a two-space identifies

`P ~= H_3(3) x C3^2`.  (M1)

Put `R=H/P`. It has order `3^4` and exponent 3. If `d=dim R/R'`, then `d=4` gives `R=C3^4`; `d=1` would make `R` cyclic of order at most 3; `d=2` is impossible because every two-generated exponent-3 group is a quotient of `B(2,3)=H_3(3)` and has order at most 27; and `d=3` gives `|R'|=3`, class 2, and a rank-two alternating form with one-dimensional radical. Hence exactly

`R in {C3^4, H_3(3) x C3}`.  (M2)

Neither row in (M2) is eliminated formally. The complete finite residual gate fixes (M1), one row (M2), an outer action `R->Out(P)`, left-conjugation lifts `alpha_r`, and a normalized nonabelian factor system `f` satisfying

`alpha_r alpha_s=Inn_left(f(r,s))alpha_(rs)`,

`f(r,s)f(rs,t)=alpha_r(f(s,t))f(r,st)`.

The resulting 81-by-243 finite extension must have exponent 9; complete actual cube image exactly `P`; `P'=C` as the unique central order-3 subgroup; and, for every `x` with `a=x^3`, the right-conjugation action must satisfy `(A_x-I)^3=D_a`. For noncentral `a`, equality forces Jordan type `J4+J1` and fixed space `<C,a>`. These conditions are a complete outer-action/factor-system parameterization for both quotient types, not a computation authorization and not a reopening of the old NS3 family.

On the three-space `Z(P)`, every root action for a noncentral cube restricts to a single `J3` block with fixed line `C`: the length-4 chain has its last two positions in the centre, while the only other full-space fixed vector is the noncentral cube itself. Thus a bounded next step is to enumerate outer-action homomorphism orbits for the two fixed `R` types, retaining exactly those with common central fixed space `C` and a `J3` element, before any factor-system classes are considered.

Concretely, writing the Lie algebra as `V direct_sum C direct_sum W` with dimensions `2+1+2`, every automorphism is encoded by `g in GL(V)`, `h in GL(W)`, a map `W->C`, and a central shear `V->C direct_sum W`, with `c` scaled by `det(g)`; quotienting the two-dimensional `V->C` inner-shear space gives `Out(P)`. On `Z(P)=C direct_sum W`, an eligible action lies in `UT_3(3)` and contains a regular unipotent. The abelian quotient type has central-module image in the `C3^2` centralizer of that block; the nonabelian type may also have full `UT_3(3)` image. This makes the proposed next orbit enumeration finite and convention-explicit.

The three central-module image branches (cyclic regular, its `C3^2` centralizer, or full `UT_3(3)`) leave respectively 54, 54, or 36 quotient cosets acting regularly. Covering the 216 noncentral elements of `P` needs only 24 cosets at the nine-values-per-coset bound, so this count eliminates none; full outer shears and factor systems remain essential.

## Outcome

Latest outcome: `PARTIAL_RESULT`. The official order-2187 layer and the entire order-6561 TRI3 lift layer are exhausted; no direct `p=3` counterexample exists below order `3^9`. At equality, its power subgroup and quotient are restricted by (M1)–(M2), with the complete finite extension gate stated above. No extension was enumerated and neither quotient type is yet eliminated. The run is `awaiting_lead`; the scope and counterexample direction remain active and unanswered, and this is not a park recommendation.

## MIN9 central-module action gate: conditional order-`3^9` family is empty

The factor-independent action gate has now been completed for the two conditional equality quotient types. This is a `PARTIAL_RESULT`, not an unrestricted-scope claim, and it awaits independent reconstruction of the equality dependencies and capacity implication.

### Exact finite object

Fix the conditional equality kernel and quotient types

`P=H_3(3)xC3^2`, `R in {C3^4,H_3(3)xC3}`.

The explicit bracket-preserving matrix model reconstructed

`|Aut(P)|=15116544=48^2*3^8`, `|Inn(P)|=9`,

`|Out(P)|=1679616=48^2*3^6`, with a Sylow-3 subgroup `S` of order `6561`.

Every 3-subgroup image in `Out(P)` is conjugate into `S`. GAP returned all 17,409 `S`-conjugacy classes of subgroups. The two quotient-image type lists and the necessary common-fixed-`C`/regular-`J3` central restriction gave:

| quotient type | permitted `S`-classes | represented subgroups in `S` | central-pass classes | represented central-pass subgroups |
|---|---:|---:|---:|---:|
| `C3^4` | 8,797 | 96,163 | 500 | 11,892 |
| `H_3(3)xC3` | 12,258 | 133,410 | 2,366 | 36,738 |

Their union has exactly 2,398 central-pass `S`-classes: 468 occur in both quotient lists, 32 only in the `C3^4` list, and 1,898 only in the `H_3(3)xC3` list.

For every union class and every outer element `u`, the script inspected all nine matrices in the inner fibre over `u^-1`. It counted a lift for `abar!=0` only after all three exact tests:

1. ranks `(rank N,rank N^2,rank N^3,rank N^4)=(3,2,1,0)`;
2. `N^3=D_abar` with the fixed right-conjugation sign convention;
3. the projection of `ker N` to `P/Z(P)` is exactly `<abar>`.

It then evaluated the eight-demand capacity network with `k=81/|U|`. Every one of the 2,398 classes failed. The exact max-flow distribution is

| max flow | number of `S`-classes |
|---:|---:|
| 0 | 158 |
| 54 | 1,736 |
| 108 | 336 |
| 162 | 168 |
| 216 | 0 |

Thus `PREFUSION_LIFT_PROFILE_COMPLETE survivors=0`. Because the flow value is invariant under full `Out(P)` conjugacy, fusion after this filter is vacuous: both quotient-type survivor counts are zero. No epimorphism or factor-system choice can repair an action image that already fails this necessary capacity bound.

### Reproducible command and hashes

Frozen script: `scratch/min9_central_module_action.g`  
SHA-256: `ba0b74b5f3d3e0ba6604c8d4399f925cd9decbd2fc8f3803753fb78b62241cdd`  
Length: 508 lines, 18,475 bytes.

Leased command, run exactly once:

`timeout 900s gap -q Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_central_module_action.g > Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_profile_before_fusion.out 2>&1`

Observed exit code: `0`.  
Complete output: `scratch/min9_profile_before_fusion.out`  
SHA-256: `b1b187eb3add7ef6154ff3aa1b32eda390c1e1c50877bb23043a26eee01b17ab`  
Length: 22,408 lines, 1,504,811 bytes.

The sole warning is GAP's top-level lexical warning that the already assigned global `profile` is read in an immediately evaluated anonymous function used only to sort label counts. All 2,398 rows executed and printed; the flow function uses the assigned profile directly; the script reached its normal completion marker. The warning is not a runtime failure and does not affect the zero-survivor result.

### Hand simplification of the lift fibre

The elementwise computation has a direct audit. For a lift `A=I+N`, write

```text
N = [ G      0    0 ]
    [ alpha  0  lambda ]
    [ T      0    H ] .
```

The nine inner lifts vary only `alpha`. Since `G^2=H^2=0`,

`N^3|_V=(lambda(TG+HT),HTG)` in `C direct_sum W`,

independently of `alpha`. Under regular central `J3`, the full lift criterion is equivalent to `HTG=0` and nonzero `r=lambda(TG+HT)`, with `r=(abar_2,-abar_1)`. These conditions force `J4+J1` and the required projected fixed line, so all nine inner lifts pass for that one `abar`, or none does. This independently explains the observed `0/9` lift counts and reduces the flow to

`sum_(abar!=0) min(27,9k*m_abar)`.

It also immediately excludes image orders 3 and 9: they have at most two and six centrally regular elements, so flow is at most 54 and 162 respectively.

### Conditional consequence and exact limitation

Assuming the reviewed quotient-minimal equality reduction and the stated capacity implication, neither `R=C3^4` nor `R=H_3(3)xC3` can occur at order `3^9`. Combined with the independently replicated floor through order `3^8`, this would raise the direct `p=3` counterexample floor to `3^10`.

This does **not** answer the active assignment. It says nothing about 3-groups of order at least `3^10`, any prime `p>3`, or a proof that every admissible power subgroup is abelian. No factor system, cocycle, extension, descendant, or candidate group was opened. `active_assignment_answered: no`.
