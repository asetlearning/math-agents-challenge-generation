---
title: "CHAR-GALOIS-WEYL — exact Clifford scalarization failure"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: CHAR-GALOIS-WEYL
direction: proof
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/character-theory
  - topic/power-maps
  - project/kourovka
  - status/conjectured
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/ideas/2026-08-18-post-r4-faithful-character-portfolio.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T181302Z-minimal-central-obstruction.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T164459Z-grad-pimage-jordan-reduction.md
---

# Outcome

`CHAR-GALOIS-WEYL` meets its first hard kill.  The faithful irreducible
representation exists, and the Weyl and Galois identities are exact, but equal
restricted characters canonically yield only an `End_P(V)^x`-valued nonabelian
cocycle.  Promoting it to a scalar cocycle would require an additional
irreducibility/inertia hypothesis.  Clifford multiplicity and block permutation
are both uncontrolled.  The explicit gauge below preserves all derived rows and,
in an unexcluded block-permutation case, changes the root discrepancy
non-scalarly.

This is minute-18 alternative **(B)**.  No three-root residual or universal
bridge is licensed.  The unrestricted source target remains unanswered.

## 1. Minimum-counterexample reconstruction

Assume, only to test the proof strategy, that an in-scope counterexample exists
and choose one `G` of minimum order.  Use

`[u,v]=u^{-1}v^{-1}uv` and `u^v=v^{-1}uv`.

Put `P={g^p:g in G}`.  The following deductions are reconstructed rather than
imported as slogans.

1. Every automorphism sends an actual `p`th power to an actual `p`th power.
   Because this set is assumed to be a subgroup, `P` is characteristic.
2. For `t in P`, literal actual-valuedness gives `t=g^p`, hence
   `t^p=g^(p^2)=1`.  Thus `exp(P)<=p`.  Since `P` is assumed nonabelian,
   `exp(P)=p`.
3. `P'` is a nontrivial normal subgroup of `G`.  Conjugation of the finite
   `p`-group `G` on `P'` has a nontrivial fixed point, so
   `P' intersect Z(G)` contains an order-`p` subgroup `N`.
4. Here `N<=P'<=P`.  In `G/N`, elementwise,

   `Pow_p(G/N)={(gN)^p:g in G}=P/N`.

   If `G/N` had exponent at most `p`, then every `g^p` would lie in `N`, so
   `P=N`, contradicting nonabelianity.  Thus the quotient still has exponent
   exactly `p^2`.
5. Minimality makes `P/N` abelian.  Since `N<=P'`, this gives `P'=N`; hence
   `N<=Z(G)` and `|N|=p`.
6. If `1 != M normal G` and `N` were not contained in `M`, then
   `Pow_p(G/M)=PM/M` would again be a subgroup.  Its exponent is exactly
   `p^2`, because exponent at most `p` would imply `P<=M` and hence `N<=M`.
   Its power subgroup has derived group `NM/M != 1`.  This is a smaller
   counterexample, impossible.  Therefore every nontrivial normal subgroup
   contains `N`.
7. Every order-`p` subgroup of `Z(G)` is normal and so equals `N`.  A finite
   abelian `p`-group with a unique subgroup of order `p` is cyclic.  Since
   `N<=Z(G)` and `exp(G)=p^2`, `Z(G)` is cyclic of order `p` or `p^2`.

These are all minimum-counterexample facts used below.

Because `P'=N`, choose `a,b in P` with

`n=[a,b] != 1`.

Then `n` generates `N`.  Literal actual-valuedness supplies roots `x^p=a` and
`y^p=b`.  Subgroup closure gives `ab in P`, and only then literal
actual-valuedness supplies `z^p=ab`.

## 2. Faithful irreducible representation, reconstructed

Let `Z=Z(G)`.  Since `Z` is cyclic, choose a faithful linear character
`lambda:Z->C^x`.  Let `chi` be any irreducible constituent of
`Ind_Z^G(lambda)` and let `rho` afford `chi`.

Because `Z` is central, Schur's lemma says that an irreducible constituent has
a single central character.  Frobenius reciprocity with `lambda` forces that
central character to be `lambda`.  Thus `rho(t)=lambda(t)I` for `t in Z`.

If `ker(rho)` were nontrivial, it would be a nontrivial normal subgroup of a
finite `p`-group.  Conjugation on that kernel shows that it intersects `Z`
nontrivially.  But `ker(rho) intersect Z=ker(lambda)=1`.  Hence `rho` is
faithful.  No external faithful-character theorem is needed.

In particular,

`rho(n)=zeta I`,

where `zeta=lambda(n)` is a primitive `p`th root.  With `A=rho(a)` and
`B=rho(b)`, the convention `n=a^{-1}b^{-1}ab` gives `ab=ban`; therefore

`AB=zeta BA`.                                                   `(W)`

## 3. Exact cyclotomic identity

Let `xi` be a primitive `p^2`th root and let `sigma(xi)=xi^(1+p)`.  Every
eigenvalue of `rho(g)` is a `p^2`th root, so eigenvalue-by-eigenvalue

`chi^sigma(g)=chi(g^(1+p))=chi(g g^p)`.                         `(G1)`

Every element of `P` has order dividing `p`, and `1+p` is congruent to `1`
modulo `p`.  Hence

`chi^sigma|P=chi|P`.                                            `(G2)`

Equation `(G1)` is a trace identity.  It does not imply the matrix identity
`rho^sigma(g)=rho(g)rho(g^p)` in any common basis.

## 4. Complete Clifford decomposition

Choose an irreducible constituent `theta` of `rho|P` and put

`I={g in G:theta^g=theta}`.

Clifford theory gives

`rho|P = e direct-sum over t in G/I of theta^t`,                 `(C1)`

for one multiplicity `e>=1`.  Let `Omega=G/I`, `r=|Omega|`, and let `W_t`
be the `theta^t`-isotypic block.  Because `exp(P)=p`, every character value of
`P` lies in `Q(zeta_p)`, on which `sigma` acts trivially.  Thus `(G2)` really
identifies the same isotypic types and multiplicities.

The full commutant is

`E=End_P(V) isomorphic to product over Omega of M_e(C)`.         `(C2)`

The quotient `G/P` acts on `E` by

`alpha_g(T)=rho(g)^{-1} T rho(g)`,                              `(C3)`

permuting the factors according to its action on `Omega` and acting by inner
conjugation on each multiplicity algebra.

## 5. The discrepancy is a nonabelian cocycle

Let `rho_sigma` afford `chi^sigma`.  By `(G2)`, choose a `P`-isomorphism

`S:(V,rho|P)->(V_sigma,rho_sigma|P)`.

Transport `rho_sigma` back to `V`:

`tilde_rho(g)=S^{-1}rho_sigma(g)S`.

Then `tilde_rho(u)=rho(u)` for `u in P`.  Define

`D(g)=rho(g)^{-1}tilde_rho(g)`.                                 `(D1)`

For `u in P`, conjugating `rho(u)` by the two factors in `(D1)` shows
directly that `D(g)` commutes with `rho(u)`.  Hence

`D(g) in E^x`.                                                   `(D2)`

Writing `tilde_rho(g)=rho(g)D(g)` and comparing products gives the exact
right-cocycle rule

`D(gh)=alpha_h(D(g))D(h)`.                                     `(D3)`

Also `D(u)=1` for `u in P`, and `(D3)` shows that `D` is constant on both
left and right `P`-cosets.  It is therefore an `E^x`-valued nonabelian
`1`-cocycle on `G/P`.

The choice of `S` is not harmless.  Every other `P`-isomorphism is `S'=SC`
with `C in E^x`.  Substitution into `(D1)` gives

`D'(g)=alpha_g(C)^{-1}D(g)C`.                                  `(D4)`

Thus only the nonabelian cohomology class of `D` is choice-independent.

## 6. Minute-18 dichotomy: alternative (B)

A scalar discrepancy would follow if `E=C`, equivalently if `rho|P` were
irreducible.  No minimum-counterexample row above implies this.  More
generally, on a chosen inertia block one obtains a `GL_e(C)`-valued cocycle;
it is scalar only after the additional, unproved condition `e=1`.  Even when
`e=1`, elements outside `I` permute blocks, so an inertia scalar cannot be
evaluated on an arbitrary root.

Here is an explicit permutation ambiguity.  Since `x^p=a in P`, the
permutation of `Omega` induced by `x` can have cycles of length `1` or `p`.
None of the reconstructed facts forces fixed points.  On an allowed `p`-cycle

`W_0 -> W_1 -> ... -> W_(p-1) -> W_0`,

choose the perfectly valid commutant element `C` which is `2I` on `W_0` and
`I` on every other block.  If the old discrepancy of `x` is block-scalar with
entries `d_i` (a non-block-scalar entry is already alternative (B)), formula
`(D4)` changes it by the telescoping edge ratios

`d_i -> d_i c_i/c_(i+1)`, with `(c_0,c_1,...,c_(p-1))=(2,1,...,1)`. `(B1)`

Thus two entries acquire factors `2` and `1/2`, while the product around the
cycle is unchanged.  The new tuple is not a global scalar even if the old one
was.

Expanding `(D3)` for `x^p=a` shows that the product around this cycle is
exactly the corresponding component of `D(x^p)=D(a)=1`.  Thus the sole
gauge-invariant cycle product is already trivial; redistributing it as in
`(B1)` loses no nontrivial root datum.

This is not a second representation or a guessed group.  It is a change from
`S` to another equally valid `P`-intertwiner for the same `rho` and
`rho_sigma`.  Consequently it preserves automatically:

- the characters and every trace identity `(G1)`;
- the fixed restriction `(G2)`;
- the root identity `x^p=a` and its cocycle norm `D(x^p)=1` (the ratios in
  `(B1)` telescope);
- the analogous root identities for `y` and `z`;
- the Weyl identity `(W)`, because `C` commutes with all of `rho(P)`.

This is the requested explicit matrix/permutation ambiguity.  The root action
can be a `p`-cycle, and no reviewed hypothesis gives a common block fixed by
`x,y,z`.  Therefore equal restricted characters do not provide a
choice-independent scalar `1`-cocycle on which the three roots can be
compared.

Multiplicity gives a second version of the same defect: if `e>1`, `(D4)` is
a genuine `GL_e` coboundary on an inertia block.  Choosing a multiplicity
matrix `C` not commuting with the inner action changes a scalar discrepancy
to a non-scalar matrix.  The strategy was explicitly forbidden to assume
`e=1`.

## 7. Why determinant is not an (A) pass

The global scalar shadow `det D(g)` is indeed gauge-independent and
multiplicative, since conjugation preserves determinant.  It does not
scalarize `D`.  More importantly, taking determinants in `(W)` gives

`zeta^(dim V)=1`,

and similarly on every `P`-isotypic block.  Thus the determinant has already
annihilated the nontrivial Weyl multiplier.  It recovers only the familiar
degree divisibility by `p`, exactly the degree-bound output forbidden as
progress in this strategy.

## 8. Hard kill and exact reach

The first gate returns alternative **(B)**.  `CHAR-GALOIS-WEYL` is exhausted
at the scalarization step.  In accordance with the selected portfolio:

- the three-root Weyl residual was not evaluated;
- no root-choice- or block-choice-independent residual was obtained;
- the universal bridge was not opened;
- no fallback strategy, parameter change, computation, or web search was
  used.

The defect is stronger than “multiplicity one was not proved”: formula `(D4)`
and example `(B1)` give the exact gauge action that absorbs any proposed
edge scalar while all available root and Weyl rows remain intact.

## 9. Constraint-and-conclusion matrix

| constraint_id | role | required condition | use/result in this run | evidence | result |
|---|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every admissible `p,G` | tested by assuming an arbitrary minimum counterexample; the scalarization gate fails in an unexcluded Clifford case | Sections 1 and 6 | unknown |
| `21.137-odd-p-not-2` | admissibility | odd prime `p>2` | retained throughout; `sigma:xi->xi^(1+p)` and `exp(P)=p` use this same prime | Sections 1 and 3 | pass for method audit |
| `21.137-odd-finite-p-group` | admissibility | finite same-`p` group | used in minimality, normal-center intersection, and Clifford theory | Sections 1, 2, and 4 | pass for method audit |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | used to obtain `exp(P)=p`, preserve quotient exponent, and define the cyclotomic power automorphism | Sections 1 and 3 | pass for method audit |
| `21.137-odd-power-set-definition` | admissibility | literal set of actual powers | used for `exp(P)=p` and for existence of each of `x,y,z` | Section 1 | pass for method audit |
| `21.137-odd-power-set-subgroup` | admissibility | literal set itself is a subgroup | used to make `P` characteristic and to infer `ab in P` before choosing `z` | Section 1 | pass as assumed hypothesis |
| `21.137-odd-P-abelian` | target conclusion | `P` is abelian | not reached; the Clifford method hard-kills before the three-root gate | Sections 6 and 8 | not proved |

`active_assignment_answered: no`.

## 10. What this does not establish

- It does not show that a minimum counterexample exists.
- It does not refute the target assertion.
- It does not rule out a separate theorem forcing `rho|P` irreducible, but no
  such theorem follows from the reconstructed rows and none may be assumed.
- It does not rule out a different invariant extracted from the full
  nonabelian Clifford cocycle.
- It says nothing about the excluded `p=2`, exponent-eight sibling.

## 11. Active-time charge

- start: `2026-08-18T00:12:04Z` at official cumulative minute `717`;
- stop: `2026-08-18T00:19:56Z`;
- actual charge: `8` active minutes;
- resulting official cumulative minute: `725`;
- unused allocation returned to Lead: `40` active minutes.

The exact alternative-(B) deliverable was obtained before active minute 18.
