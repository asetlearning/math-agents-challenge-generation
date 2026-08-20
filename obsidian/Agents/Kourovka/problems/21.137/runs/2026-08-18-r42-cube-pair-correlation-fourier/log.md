---
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
cycle: 30
strategy: CUBE-PAIR-CORRELATION-FOURIER
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/draft
---

# Cycle 30 log: coupled cube-pair Fourier kernel

## 2026-08-18T10:02:17Z — work start

- Official cumulative start: minute `886`.
- Current increment: at most `45` active minutes.
- Exact scope: for every odd prime `p`, every finite `p`-group `G` of exact
  exponent `p^2` whose literal value set `P={g^p:g in G}` is a subgroup must
  have `P` abelian. The general powerfulness question and the separate `p=2`,
  exponent-eight clause are excluded.
- Primitive datum in the assigned first lane (`p=3`):
  `K(a,b,c)=#{(x,y):x^3=a,y^3=b,(xy)^3=c}`.

## Source and scope gate

The configured source PDF is readable. I inspected rendered PDF page 184, not
only `pdftotext`. The displayed source statement is:

> If the p-th powers in a finite p-group form a subgroup, must that subgroup be
> powerful? That is, for p != 2, if the p-th powers in a p-group of exponent
> p^2 form a subgroup, must that subgroup be abelian? For a 2-group of exponent
> 8, if the squares form a subgroup, must that subgroup be abelian?

`source_transcription_checked: yes`. The active scope is exactly the middle
clause. The source's `p != 2`, finite same-`p` group, exact exponent `p^2`,
literal power-value set, subgroup hypothesis, and abelianity conclusion agree
with all seven canonical rows. `active_scope_checked: yes`. The issue-21 source
PDF has no answer marker or later editor comment at 21.137. No issue-21 JSONL
record is present in the configured corpus directory, so there are no corpus
flags to quote. In accordance with the discovery-blind scope, open-web and
solution-bearing-history staleness checks are deferred:
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.

Clause matrix:

| source clause | active? | treatment |
|---|---:|---|
| general actual-powers subgroup is powerful | no | excluded |
| odd `p`, exponent exactly `p^2`, actual powers a subgroup implies abelian | yes | entire assignment |
| `p=2`, exponent 8, squares a subgroup implies abelian | no | excluded |

Constraint checklist:

| constraint id | role in this run |
|---|---|
| `21.137-odd-forall-p-G` | a proof must return from the initial `p=3` audit to every odd prime |
| `21.137-odd-p-not-2` | retain `p>2`; no 2-group evidence |
| `21.137-odd-finite-p-group` | all group deductions use a finite group for the same `p` |
| `21.137-odd-exponent-p2` | exact exponent `p^2`; in the first lane exact exponent 9 |
| `21.137-odd-power-set-definition` | `P` is the full literal image, never only its generated subgroup |
| `21.137-odd-power-set-subgroup` | closure makes that full image a subgroup |
| `21.137-odd-P-abelian` | target is `[P,P]=1` |

## Strategy portfolio

1. **Theoretical/coupled kernel (active, cheapest certifiable):** derive every
   marginal and the exact root-pair bijections acting on `K`; in the
   least-counterexample `P'=C_3` branch compute the central Fourier selection
   rule and test whether its surviving skew block forces `[a,b]=1`.
2. **Structured method-obstruction:** if one skew block remains free, construct
   a positive integral formal kernel satisfying all derived marginals and exact
   value-level bijections. This is explicitly only an insufficiency certificate,
   never a group or counterexample.
3. **Catalogue mode:** no catalogue computation is authorized or informative in
   this 45-minute proof lane. A negative bounded list would not address the
   universal statement.
4. **Certificate plan:** signs are fixed with `[r,s]=r^{-1}s^{-1}rs` and
   `r^s=r[r,s]`; give explicit bijections, Fourier equations, and a small exact
   checker for any formal obstruction. Validator can check the identities without
   trusting a classification theorem or selected roots.

## 2026-08-18T10:07:39Z — independent least-counterexample reduction

Assume a counterexample of least order (for its odd prime `p`) and continue to
write `P` for the literal power set, which is a subgroup by hypothesis.

1. `P` is characteristic in `G`, because the literal power set is invariant under
   every automorphism. It has exponent dividing `p`: every `a=g^p` satisfies
   `a^p=g^(p^2)=1`. Since it is a subgroup, this applies to every element of `P`.
2. `P` is nonabelian in a counterexample, so `P'` is a nontrivial characteristic
   subgroup of `G`. A nontrivial normal subgroup of a finite `p`-group meets
   `Z(G)` nontrivially. Choose `N <= P' cap Z(G)` of order `p`.
3. In `G/N`, the complete literal power set is exactly the image `PN/N`, since
   `(gN)^p=g^pN`; it is a subgroup. It is nontrivial, for otherwise `P<=N` would
   make `P` abelian. Hence `G/N` still has exponent exactly `p^2`.
4. Minimality makes `P/N` abelian. Thus `P'<=N`; the reverse inclusion was the
   choice of `N`, so `P'=N=C_p<=Z(G)`.

Therefore it is legitimate, and loses no hypothetical minimum counterexample, to
test the branch `Z=P'=C_p` central in `G`. Then `P` has class two and exponent
`p`, and

`[u,v]=z^(beta(ubar,vbar))`, `beta:(P/Z)^2 -> F_p`,

is an alternating bilinear map after fixing a generator `z` of `Z`. No earlier
minimum-counterexample note was used in this derivation.

## Exact marginals of `K`

Put `R(a)=#{x:x^3=a}`. Direct changes of variables give all three two-coordinate
marginals:

`sum_c K(a,b,c)=R(a)R(b)`,

`sum_b K(a,b,c)=R(a)R(c)`,

`sum_a K(a,b,c)=R(b)R(c)`.

For the second identity use the bijection `(x,y) <-> (x,w=xy)`; the third is
similar. Consequently the one-coordinate marginals are
`sum_(b,c)K=|G|R(a)` and its two permutations, and the total is `|G|^2`.

## Exact coupled power identities beyond every marginal

For a counted pair write `a=x^3`, `b=y^3`, `c=(xy)^3`. The following are genuine
bijections of complete root-pair sets; no root is selected.

1. `(x,y) -> (x,y^a)`. Since `x` commutes with `a=x^3`,
   `xy^a=(xy)^a`. Hence
   `K(a,b,c)=K(a,b^a,c^a)`.
2. `(x,y) -> (x^b,y)`. Since `y` commutes with `b=y^3`,
   `x^by=(xy)^b`. Hence
   `K(a,b,c)=K(a^b,b,c^b)`.
3. `(x,y) -> (x^c,y^c)`. Since `c=(xy)^3` commutes with `xy`, the product stays
   `xy`. Hence `K(a,b,c)=K(a^c,b^c,c)`.
4. The root-pair Hurwitz rotation `(x,y)->(y,(xy)^(-1))` gives
   `K(a,b,c)=K(b,c^(-1),a^(-1))`.
5. The reflection `(x,y)->(xy,y^(-1))` gives
   `K(a,b,c)=K(c,b^(-1),a)`.

Items 1--3 are the target-facing coupled power identity required by the minute-15
gate. They use the fact that the labels are the powers of the very roots being
counted, and are not consequences of `R` or of any marginal.

## Central-character blocks in the `p=3`, `P'=C_3` branch

Fix `z` generating `Z=P'` and three value cosets `A,B,C in V=P/Z`. Choose one
value (not one root) in each coset only to name the array

`K_(A,B,C)(i,j,k)=K(az^i,bz^j,cz^k)`, `i,j,k in F_3`.

Put

`delta=beta(A,B)`, `epsilon=beta(B,C)`, `zeta=beta(C,A)`.

Because `r^s=r[r,s]`, the first three exact bijections above become the three
translations

`(i,j,k) -> (i,j-delta,k+zeta)`,

`(i,j,k) -> (i+delta,j,k-epsilon)`,

`(i,j,k) -> (i-zeta,j+epsilon,k)`.

For `omega=exp(2 pi i/3)`, define

`Khat(r,s,t)=sum_(i,j,k) omega^(-ri-sj-tk) K_(A,B,C)(i,j,k)`.

Every nonzero block must therefore satisfy, with all signs fixed,

`-s delta+t zeta=0`,

`r delta-t epsilon=0`,

`-r zeta+s epsilon=0`.                                      `(F)`

If `(delta,epsilon,zeta) != (0,0,0)`, the three translation vectors span a
two-plane and `(F)` says exactly

`(r,s,t) in F_3 (epsilon,zeta,delta)`.                       `(S)`

Equivalently, the array is constant on the nine-point level sets of the skew
central coordinate

`sigma=epsilon i+zeta j+delta k`.                            `(SC)`

This coordinate and its selection rule survive the exact Hurwitz rotation and
reflection: under `(a,b,c)->(b,c^(-1),a^(-1))` and
`(a,b,c)->(c,b^(-1),a)`, direct substitution leaves `sigma` unchanged. Thus the
dihedral symmetry relates the amplitudes at transformed quotient triples but does
not kill them.

For every noncommuting pair `A,B` (`delta != 0`), taking `C=A+B` gives
`epsilon=zeta=-delta != 0`. Then both nonzero frequencies allowed by `(S)` have
all three coordinates nonzero. Consequently **none of the three marginals sees
these two blocks**. Literal-image closure says that every value in the coset `C`
has roots, but it does not say that a root of `a` times a root of `b` has cube in
that coset. Thus it supplies no equation for these amplitudes.

At this point the skew coordinate does detect the three commutators—its frequency
direction contains `delta`, the exponent of `[a,b]`—but the detection does not
force `delta=0`. The two surviving Fourier amplitudes are free under all rows so
far (complex conjugates because `K` is real).

## Exact positive formal obstruction (not a group)

To make the preceding freedom mechanical, take the Heisenberg value group
`P=H_3(3)` in BCH coordinates `(A,i) in F_3^2 x F_3`, with alternating form
`beta`, and set a formal root count `R(a)=27` (so the compatible formal total is
`|G|=729`). For a triple of values put

`h(0)=2`, `h(1)=h(2)=-1`,

`K_form(a,b,c)=27+h(sigma)` if `delta epsilon zeta != 0`, and `27` otherwise.

This is positive integral (`26,27,29`). When two values are fixed, every active
perturbation sums to zero over the remaining central coordinate because its
coefficient in `sigma` is nonzero. Hence every pair marginal is exactly
`27*27=729`. The defining condition and `sigma` are invariant under all three
value-conjugation translations and under the Hurwitz rotation/reflection, so this
formal kernel satisfies every exact coupled identity derived above.

For `A=(1,0)`, `B=(0,1)`, `C=A+B`, one has
`(delta,epsilon,zeta)=(1,2,2)` and frequency vector
`w=(epsilon,zeta,delta)=(2,2,1)`. Each skew level has nine entries, respectively
all `29`, all `26`, all `26`. The exact central transforms are

`Khat(0)=9(29+26+26)=729`,

`Khat(w)=Khat(-w)=9(29-26)=27`.

Thus a nonzero commutator form and a nonzero skew block coexist with positivity,
integrality, all marginals, and all five exact pair-bijection identities.

Reproducible checker:
`scratch/check_formal_skew_kernel.py`. Observed command:

`python3 Agents/Kourovka/problems/21.137/runs/2026-08-18-r42-cube-pair-correlation-fourier/scratch/check_formal_skew_kernel.py`

Observed output:

```text
formal_object=integer_kernel_on_H3(3)^3_not_a_group_power_map
kernel_values=26,27,29
all_three_pair_marginals=729
value_conjugation_identities=pass
hurwitz_rotation_and_reflection=pass
selected_pairings_delta_eps_zeta=1,2,2
selected_skew_level_sizes=9,9,9
selected_fourier_blocks_zero_plus_minus=729,27,27
```

This array is **not** asserted to arise from any group or cube map, and it is not
a counterexample. Its exact use is narrower: the derived `K`-only equations cannot
force the skew block, and hence cannot force `[a,b]`, to vanish.

The obstruction is prime-uniform. For any odd `p`, use `H_p`, put `R=p^3`, base
kernel `p^3`, and replace `h` by
`h_p(0)=p-1`, `h_p(s)=-1` for `s!=0`. The same translation calculation works over
`F_p`; every active pair marginal has zero perturbation, while every nonzero
frequency on the allowed line has transform `p^3`. The `p=3` checker is the first
required lane, not an accidental characteristic-three cancellation.

## Why the exact Hall route does not close on `K`

The remaining natural cube collection is

`(xy)^3=x^3 y^(x^2) y^x y`.

It depends on the conjugation action of the particular root `x`, not only on its
cube `a=x^3`. This loss can be stated exactly. For a fixed root define

`K_x(b,c)=#{y:y^3=b,(xy)^3=c}`.

The Nielsen change `y->y^x` gives

`K_x(b,c)=K_x(b^x,c^x)`.

But `K(a,b,c)=sum_(x^3=a) K_x(b,c)`, and the automorphism induced by `x` on `P`
is not determined by `a`; only its cube is fixed:

`(conj_x|P)^3=conj_a|P`.

Therefore summing over the root fibre erases exactly the intermediate action
needed by the Hall norm. No deterministic identity on the three value labels can
be obtained from this Nielsen move without adjoining an action-resolved variable.
The value-conjugation identities above are what remains after cubing that action,
and their one unconstrained skew line is precisely the lost information.

This does not prove that no deeper theorem about actual group kernels exists. It
does rigorously kill the assigned `K`-only central-Fourier mechanism: all closed
identities supplied by marginals, value powers, and the root-triangle symmetries
permit a nonzero commutator-detecting block. A continuation would need a genuinely
enlarged observable (for example, a root-action-resolved correlation), which is a
representation change and requires Lead approval.

## 2026-08-18T10:12:40Z — work stop and cycle outcome

- Elapsed active work: 10 minutes 23 seconds; conservatively charged `11` active
  minutes.
- Official cumulative stop: minute `897` (`886+11`), within the grant through
  minute `931`.
- Outcome: `STRATEGY_EXHAUSTED` for `CUBE-PAIR-CORRELATION-FOURIER` alone.
- Hard kill: the exact Fourier selection rule leaves the skew line
  `F_3(epsilon,zeta,delta)` free, and a positive integral formal kernel realizes a
  nonzero amplitude while passing every derived `K`-only identity.
- Scope status: unanswered. No group or counterexample was constructed, and no
  universal proof was claimed.
- Recommendation: only a Lead-approved representation change to an
  action-resolved root correlation can test the missing Hall information; do not
  spend the remaining grant on further `K` marginals or skew-coordinate algebra.
- State: `awaiting_lead`.

