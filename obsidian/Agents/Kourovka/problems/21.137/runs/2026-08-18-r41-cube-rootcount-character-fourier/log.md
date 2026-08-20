---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/character-theory
  - project/kourovka
  - status/draft
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
cycle: 29
strategy: CUBE-ROOTCOUNT-CHARACTER-FOURIER
---

# Cycle 29 log — complete root-count character/Fourier transform

## 2026-08-18T06:46:45Z — active work start

- Official cumulative active minutes at start: `841`.
- This increment: at most `45` new active minutes.
- Source and control context: canonical scope revision 2, current roster, rendered source PDF page 184, and Lead decision `2026-08-18T064314Z__Lead__DECISION__cube-rootcount-character-fourier.md`.
- Clean/discovery-blind context observed: no open-web search; ordinary synthesis, historical problem log/findings, archived messages, verification notes, and solution-bearing scratch were not used as mathematical inputs in this run.

## Source, transcription, and staleness gate

Rendered source transcription (visually checked against PDF page 184):

> **21.137.** If the `p`-th powers in a finite `p`-group form a subgroup, must that subgroup be powerful? That is, for `p != 2`, if the `p`-th powers in a `p`-group of exponent `p^2` form a subgroup, must that subgroup be abelian? For a `2`-group of exponent `8`, if the squares form a subgroup, must that subgroup be abelian?

Proposer: L. Wilson.

- `source_transcription_checked: yes` (rendered page, not only `pdftotext`).
- `active_scope_checked: yes`.
- The active scope is exactly the middle, odd-prime clause. The general powerfulness question and the exponent-eight `2`-group clause are excluded.
- The vault contains no issue-21 JSONL corpus record at the protocol's legacy path, so corpus flags `answered`, `has_editor_comment`, and `has_later_comment` cannot be read there. The rendered 2026 issue has no editor/later comment attached to 21.137.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.

Clause matrix:

| source clause | equivalent formulation | active? | external-result row |
|---|---|---:|---|
| actual `p`th powers form a subgroup => powerful? | general source question | no | deferred; cannot close active scope |
| `p != 2`, exponent `p^2`, actual power set a subgroup => abelian | universal odd-prime exact-exponent clause | yes | discovery-blind search deferred |
| exponent-eight `2`-group square-set clause | separate `p=2` sibling | no | excluded |

Canonical admissibility reconciliation (all seven rows match the rendered source):

| constraint_id | use in this proof lane |
|---|---|
| `21.137-odd-forall-p-G` | final target is universal; working first at `p=3` is only a gate |
| `21.137-odd-p-not-2` | `p` odd; `p=2` excluded |
| `21.137-odd-finite-p-group` | all counting/character arguments use finite same-`p` group `G` |
| `21.137-odd-exponent-p2` | `exp(G)=p^2`, hence every `p`th power has order dividing `p`; main gate uses exponent 9 |
| `21.137-odd-power-set-definition` | `P` is the literal image `{g^p:g in G}` |
| `21.137-odd-power-set-subgroup` | only this hypothesis lets the literal image be regarded as the group `P` and gives full support of root counts |
| `21.137-odd-P-abelian` | desired conclusion; contradiction gate assumes `P' != 1` |

## Strategy portfolio

Ranked for this 45-minute increment:

1. **Theoretical / character-Fourier gate.** Derive the exact Fourier matrices of the positive integral class function `R(a)=|{g:g^p=a}|` on `P`, including central-character block formulas when `P'=C_p`, and identify every genuine word-map constraint on those matrices. Cheapest certifiable output.
2. **Certificate / obstruction model.** If the Fourier rows do not force commutativity, exhibit a concrete positive integral `G`-invariant class function on a nonabelian exponent-`p` group (preferably the Heisenberg group) satisfying all rows actually derived. This certifies only blindness of the representation, not a target counterexample.
3. **Structured construction mode.** A genuine finite exponent-9 overgroup whose cube-root count equals the model would be target-facing, but it is out of reach unless Fourier inversion itself exposes an exact word-map realization condition. No extension-section or factor-set search is authorized.
4. **Catalogue/small-case mode.** Not used: a catalogue scan would repeat bounded construction work and full character transforms can be evaluated symbolically on one exact nonabelian group. A negative small-order scan would not address the universal target.

Independent verification plan: every transform identity will be proved by finite-sum reindexing and Fourier inversion; any obstruction model will give its character table values and inverse transform explicitly so Validator can check it by hand.

Kill criterion: if an exact positive integral full-support class function on a nonabelian exponent-three `P` satisfies all integrality, Galois, positivity, scalar central-character, and power-word-sum rows derived from the literal map, and the remaining realization condition is precisely not encoded by the transform, report `STRATEGY_EXHAUSTED` for the Fourier-only method and name that missing identity.

## 2026-08-18T06:54:33Z — exact transform and least-counterexample gate (8 new active minutes)

### Independently rederived least-counterexample fact

Fix an odd prime `p` and suppose `G` is a minimum-order counterexample at that
prime. Then `P` is nonabelian and has exponent `p`, since `(g^p)^p=1`. The normal
subgroup `P'` meets `Z(G)` nontrivially. Choose `N=<z>` of order `p` in
`P' intersect Z(G)`. In `G/N`, the *literal* power image is exactly `P/N`, because

`{(gN)^p:g in G}={g^pN:g in G}=P/N`.

The quotient cannot have exponent `p`: otherwise every `g^p` lies in `N`, so
`P<=N`, contradicting nonabelianity of `P`. Thus it still has exact exponent
`p^2`. Minimality makes `P/N` abelian, hence `P'<=N`; therefore

`P'=N=<z> ~= C_p` and `P'<=Z(G)`.

This is the only least-counterexample reduction used below. In the main `p=3`
gate it gives `P'=C_3` central in `G`.

### Exact complex Fourier/indicator identities

For `chi in Irr(P)`, set

`c_chi=<R,chi>_P=(1/|P|) sum_(a in P) R(a) overline(chi(a))`.

Since `P` is normal (indeed characteristic as the literal power image), direct
reindexing gives

`c_chi=(1/|P|) sum_(g in G) overline(chi(g^p))
      =nu_p(Ind_P^G(overline(chi)))`,

where `nu_p(Theta)=|G|^(-1) sum_g Theta(g^p)` is the ordinary `p`th higher
Frobenius--Schur indicator. The induction equality uses

`Ind_P^G(overline(chi))(g^p)
 =|P|^(-1) sum_(x in G) overline(chi((x^(-1)gx)^p))`

and then sums over `g` and reindexes conjugation.

For completeness, `nu_p(Theta)` is an integer: if `W` affords `Theta` and `tau`
is the cyclic permutation of `W^(tensor p)`, then

`nu_p(Theta)=Tr(tau | (W^(tensor p))^G)`.

This is an algebraic integer. Every cyclotomic Galois automorphism `sigma_u`
with `(u,exp(G))=1` fixes it, since `g -> g^u` is a bijection and
`sigma_u Theta(g^p)=Theta((g^u)^p)`. Hence it is rational and therefore an
integer. Consequently

`R=sum_(chi in Irr(P)) c_chi chi`

is an integral virtual character, not merely an integral class function.

Use the matrix-Fourier convention

`Rhat(rho_chi)=sum_(a in P) R(a) rho_chi(a^(-1))`.

Schur's lemma and Fourier inversion give the full transform

`Rhat(rho_chi)=(|P| c_chi/chi(1)) I_(chi(1))`,

`R(a)=|P|^(-1) sum_chi chi(1) Tr(Rhat(rho_chi)rho_chi(a))`.

Thus every nonlinear block is explicitly present; the scalar is integral because
character degrees of a finite `p`-group divide `|P|`. Further exact rows are:

- `c_(1_P)=[G:P]` (the total of all fibres is `|G|`);
- `c_(chi^x)=c_chi` for `x in G`, because `R` is `G`-conjugacy invariant;
- all `c_chi` are rational integers, so Galois-conjugate irreducibles have equal
  coefficients;
- Parseval: `sum_chi |c_chi|^2=|P|^(-1)sum_a R(a)^2`;
- full support is the family of strict inverse-Fourier inequalities
  `sum_chi c_chi chi(a)>0` for every `a`.

Pointwise positivity alone does **not** make the Fourier blocks positive
semidefinite and higher indicators need not be nonnegative. The obstruction model
below nevertheless satisfies the stronger PSD/genuine-character condition.

### Central-character rows in the least case

Let `Z=P'=<z>` and let `chi(z)=chi(1)lambda_chi(z)`. For a coset representative
`t in P/Z`, define the central discrete transform

`D_lambda(tZ)=sum_(j=0)^(p-1) R(tz^j) overline(lambda(z)^j)`.

Then exactly

`c_chi=|P|^(-1) sum_(t in P/Z) overline(chi(t))D_(lambda_chi)(tZ)`.

Moreover `z` acts on `Ind_P^G(overline(chi))` as the scalar
`overline(lambda_chi(z))`, but on its `p`-fold tensor power it acts as `1`.
Therefore the central character gives no vanishing condition on the `p`th
indicator: the exponent `p` in the word is exactly what removes that obstruction.

Two elementary literal-word rows are also exact. First, `(gz^j)^p=g^p`, so the
free central `Z`-action on every root fibre gives `p | R(a)`. Second, for every
unit `u mod p`, the bijection `g -> g^u` gives `R(a^u)=R(a)`. For `a!=1`, roots
have order `p^2` and partition by their unique cyclic subgroup; hence

`R(a)/p = #{C<=G: C cyclic of order p^2 and C^p=<a>}`.

### The full-`G` character row

Extend `R` by zero from `P` to `G`, writing `Zeta_p(g)=#{x:x^p=g}`. For every
`Psi in Irr(G)`,

`<Zeta_p,Psi>_G=nu_p(overline(Psi)) in Z`.

Equivalently, because `P normal G` and `R` is `G`-invariant,

`Ind_P^G(R)=[G:P] Zeta_p`

and hence the exact Clifford/indicator divisibility row is

`<R,Res_P^G(Psi)>_P=[G:P]nu_p(overline(Psi))`.

This is stronger than coefficientwise integrality on `P`, but still does not force
a nonzero nonlinear block: the zero integer is allowed, and the central scalar
argument above explains why no nontrivial `P'`-central character is automatically
excluded at the `p`th indicator.

## Exact Fourier obstruction model

Take `P=E_n`, the extraspecial exponent-`p` group of order
`p^(1+2n)` (`n>=1`) with `P'=Z(P)=<z>~=C_p`. Put `q=|P|` and define

`F(a)=q` for every `a in P`.

This is not asserted to be a word-map distribution. It is the following exact
formal obstruction to every one-variable Fourier constraint derived above:

1. `F` is strictly positive, integral, invariant under `Aut(P)` (hence under any
   possible overgroup action), constant on conjugacy classes, and invariant under
   `a -> a^u`.
2. Its total is `q|P|=q^2`, so the formal index is `[G:P]=q`, a `p`-power.
3. `F(1)=q=|P|`, exactly meeting the mandatory inclusion `P subseteq {g:g^p=1}`.
4. Every fibre size is divisible by `p`.
5. For every nonidentity `a`, `F(a)/p=q/p` is an integer depending only on
   `<a>`, so the cyclic-order-`p^2` incidence row is satisfied. The resulting
   `q(|P|-1)` formal order-`p^2` elements plus `F(1)=q` formal order-at-most-`p`
   elements total `q|P|` exactly.
6. Character expansion: `F=q 1_P`. Thus `c_(1_P)=q` and `c_chi=0` for every
   nontrivial irreducible, **including every nonlinear irreducible with nontrivial
   central character**.
7. Full matrix transform: `Fhat(1_P)=q|P|=q^2`; every nontrivial linear and
   nonlinear block is the zero matrix. These matrices are positive semidefinite,
   so `F` is even a genuine character, stronger than pointwise positivity.
8. Every nontrivial central discrete transform is zero: on each coset of `<z>`,
   the `p` equal positive entries cancel against a nontrivial central character.
   Thus full support does not force a nonlinear central block.
9. All Galois and possible `G`-orbit equalities hold. All proposed indicator
   coefficients lie in the permitted integer set (`q` for the trivial block,
   zero otherwise).
10. At the full-`G` character level, the formal zero-extension is exactly the
    permutation character `Ind_P^G(1_P)` for any abstract normal embedding with
    index `q`: it has value `q` on `P` and zero off `P`. Therefore even the
    induction divisibility and positivity rows see no contradiction. What is not
    supplied—and cannot be inferred from this equality of class functions—is that
    this permutation character is the actual power-word root-count function.

More explicitly, for any `G`-character `Psi`, the formal row gives

`<F,Res_P(Psi)>=q dim(Psi^P)`,

which is divisible by the formal index `q`; hence the full-`G` Clifford congruence
also passes, not only the separate `P`-blocks.

For the requested main gate choose `p=3,n=2`, so `P=3_+^(1+4)` has order `243`,
exponent `3`, and `P'=Z(P)=C_3`. The formal data are

`F(a)=243` for all 243 elements, `sum F=59049=3^10`,

with one trivial Fourier scalar `59049` and all `80` nontrivial linear plus both
degree-`9` nonlinear blocks zero. There are `121` order-three lines in `P`; the
formal count assigns `243/3=81` cyclic order-nine subgroups over each line, hence
`121*81=9801` cyclic order-nine subgroups and `9801*6=58806` order-nine elements,
leaving `243` order-at-most-three roots. The total is `59049`.

This calculation is hand-checkable. The bounded arithmetic command used was

`python3 -c 'p=3;n=2;q=p**(1+2*n);lines=(q-1)//(p-1);cyclic_per_line=q//p;cyclic=lines*cyclic_per_line;order9=cyclic*(p*p-p);print({"p":p,"n":n,"P_order":q,"R_each":q,"total_roots":q*q,"lines":lines,"cyclic_per_line":cyclic_per_line,"cyclic_C9":cyclic,"order9_elements":order9,"order_le3":q,"partition_total":order9+q})'`.

Observed output:

`{'p': 3, 'n': 2, 'P_order': 243, 'R_each': 243, 'total_roots': 59049, 'lines': 121, 'cyclic_per_line': 81, 'cyclic_C9': 9801, 'order9_elements': 58806, 'order_le3': 243, 'partition_total': 59049}`.

### Exact missing word-map datum

The complete one-variable transform records only the push-forward measure of the
map `x -> x^p`. It forgets how roots interact under multiplication. The first
missing datum is the two-variable word kernel

`K(a,b,c)=#{(x,y) in G^2 : x^p=a, y^p=b, (xy)^p=c}`.

Its marginals include `sum_c K(a,b,c)=R(a)R(b)`, but `R` and all of its Fourier
blocks do not determine `K`. A target-facing continuation would need an exact
exponent-`p^2` identity for the nontrivial-central-character transform of `K`
(equivalently, a sign/vanishing constraint on the commutator word
`[x^p,y^p]`) that is stronger than its marginals. Without such a coupled
two-root identity, the constant spectrum above makes every one-variable row
compatible with nonabelian `P`.

Even the marginal commutator moment is feasible. If `lambda` is a faithful
character of `Z(E_n)`, nondegeneracy of the extraspecial commutator form gives

`sum_(a,b in P) lambda([a,b])=|Z(P)||P|=p q`.

For the constant formal distribution this makes

`sum_(x,y) lambda([x^p,y^p])=q^2(pq)=p q^3`,

a positive rational integer. Thus mere integrality or positivity of that single
commutator-word sum is also insufficient; a genuinely coupled Hall/power identity
for the full kernel `K`, not another one-point moment, is the missing observable.

## 2026-08-18T09:57:15Z — administrative stop and timing anomaly

- The last `kv_now` immediately before final bus packaging returned
  `2026-08-18T07:01:55Z`. The next `kv_now`, after one `apply_patch` that wrote the
  already-prepared Lead and MathExpert messages, returned
  `2026-08-18T09:57:15Z`.
- No new mathematical branch, file inspection, or computation was run across that
  interval; the strategy outcome had already been written at approximately
  `07:01Z`. The unexplained wall-clock gap crosses the roster safety stop, so this
  run stops immediately and does not attempt to infer that the whole gap was
  charged research time.
- Conservative official debit: the full authorized `45` active minutes. Official
  cumulative ledger: `841 -> 886`. This avoids an unsupported undercharge while
  never claiming authority beyond the granted increment. Lead should audit the
  discontinuous wall-clock observation if its scheduler has finer process-state
  data.
- State: `awaiting_lead`; exact outcome `STRATEGY_EXHAUSTED` for the named
  one-variable Fourier strategy only.
