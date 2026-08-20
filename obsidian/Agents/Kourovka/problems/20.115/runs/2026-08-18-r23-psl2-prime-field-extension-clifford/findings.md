---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/conjectured]
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
outcome: PARTIAL_RESULT
---

# Prime-degree field extensions of `PSL(2,q)`: exact reduction and remaining Shintani gate

## Active target

Scope: `20.115/nonzero-character-order-divisibility`, revision 1.

Target: for every finite `G`, every ordinary complex `chi in Irr(G)`, and every `x in G`, prove `chi(x) != 0 => o(x)chi(1) | |G|`.

## Partial claim

Let `q=p^r`, where `r` is prime, let `L=PSL(2,q)` be nonabelian simple, and let `G=L semidirect <sigma>` for the order-`r` field automorphism. Cyclic Clifford theory, the complete rank-one table on `L`, and the projective norm calculation reduce the source predicate for `G` to one sharply stated generalized-Shintani support lemma. The predicate is established unconditionally for every non-invariant Clifford row and for every invariant row on `L`; the outer-coset arithmetic is complete conditional on that one support lemma. I do **not** claim the family theorem because I have not supplied a first-principles proof of the exceptional-character part of that lemma.

## Six-row constraint-and-conclusion matrix

| constraint_id | role | proof use in this run | evidence/result |
|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | specialized to `G=PSL(2,p^r).r`; this does not cover every finite group | **partial only** |
| `20.115-G-finite` | admissibility | `G` has order `r q(q^2-1)/d`, `d=(2,q-1)` | pass in the family |
| `20.115-chi-complex-irreducible` | admissibility | all rows are obtained by cyclic Clifford theory from the full ordinary `Irr(L)` inventory | pass in the family |
| `20.115-x-in-G` | admissibility | inside elements are treated by the four rank-one class types; `g sigma^i` by its exact projective Shintani norm | pass in the family |
| `20.115-character-value-nonzero` | admissibility | exact table support is used on `L`; outer support is reduced to the stated Shintani lemma, not inferred from restriction | pass except for the named unresolved exceptional Shintani gate |
| `20.115-order-degree-divisibility` | target conclusion | proved for non-invariant rows and invariant rows on `L`; outer invariant rows follow from the displayed support lemma and arithmetic | partial / conditional outer conclusion |

## 1. Full rank-one inventory, values needed for support, and the `L` audit

Put `d=(2,q-1)`, `A_q=C_{(q-1)/d}` (split torus) and `B_q=C_{(q+1)/d}` (nonsplit torus). Apart from `1_L` and `St_q` of degrees `1,q`, all irreducibles are:

- `P_alpha`, degree `q+1`, for nontrivial `alpha in Irr(A_q)`, modulo `alpha~alpha^{-1}`, excluding the quadratic parameter when `|A_q|` is even;
- `C_beta`, degree `q-1`, for nontrivial `beta in Irr(B_q)`, modulo inversion, excluding the quadratic parameter when `|B_q|` is even;
- if `q=1 mod 4`, two exceptional rows `E_+,E_-` of degree `(q+1)/2` from the quadratic split parameter;
- if `q=3 mod 4`, two exceptional rows `F_+,F_-` of degree `(q-1)/2` from the quadratic nonsplit parameter.

For even `q`, both torus orders are odd and there are no exceptional halves. The counts are `(q-2)/2` rows of degree `q+1` and `q/2` rows of degree `q-1`. For odd `q=1 mod 4` the counts are `(q-5)/4`, `(q-1)/4`, and two exceptional rows; for odd `q=3 mod 4` they are `(q-3)/4`, `(q-3)/4`, and two exceptional rows.

On identity / nontrivial unipotent / split semisimple / nonsplit semisimple classes, the values relevant to exact support are

| row | `1` | unipotent | split `s(a)` | nonsplit `t(b)` |
|---|---:|---:|---:|---:|
| `St_q` | `q` | `0` | `1` | `-1` |
| `P_alpha` | `q+1` | `1` | `alpha(a)+alpha(a)^{-1}` | `0` |
| `C_beta` | `q-1` | `-1` | `0` | `-(beta(b)+beta(b)^{-1})` |
| `E_±` (`q=1 mod 4`) | `(q+1)/2` | `(1 ± sqrt(q))/2` on the two square classes | quadratic split value | `0` |
| `F_±` (`q=3 mod 4`) | `(q-1)/2` | `(-1 ± sqrt(-q))/2` on the two square classes | `0` | minus the quadratic nonsplit value |

The displayed cyclotomic sums can themselves vanish; no stronger support assertion is used. Element orders are `p` on nontrivial unipotents, divisors of `(q-1)/d` on split classes, and divisors of `(q+1)/d` on nonsplit classes. Direct cancellation gives, row by row,

- `St_q`: nonzero excludes the only `p`-class, so `o(x)q | q(q^2-1)/d`;
- `P_alpha`: only identity, unipotent, and split support occur, so `o(x)(q+1) | |L|`;
- `C_beta`: only identity, unipotent, and nonsplit support occur, so `o(x)(q-1) | |L|`;
- `E_±` and `F_±`: the same argument with the half degree gives the divisibility.

Thus the source implication holds for every ordinary row of `L`, derived here rather than imported from another run.

## 2. Every Frobenius orbit and every Clifford row

Field Frobenius acts by

`P_alpha -> P_{alpha^p}`, `C_beta -> C_{beta^p}`,

with parameters read modulo inversion. It fixes `1_L`, `St_q`, and fixes each exceptional half individually: Frobenius preserves the square/nonsquare unipotent parameter because `u^p/u=u^{p-1}` is a square.

Because `r` is prime, every orbit has length `1` or `r`. Precisely,

- `P_alpha` is invariant iff `alpha^p=alpha` or `alpha^p=alpha^{-1}`;
- `C_beta` is invariant iff `beta^p=beta` or `beta^p=beta^{-1}`.

If `r` is odd, a non-exceptional invariant split parameter necessarily satisfies `alpha^p=alpha`, while a non-exceptional invariant nonsplit parameter necessarily satisfies `beta^p=beta^{-1}`. This follows from `p^r=1` on `A_q`, `p^r=-1` on `B_q`, and `gcd(2,r)=1`.

If `r=2` and `p` is odd, both signs occur for split parameters, while there is no nontrivial invariant nonsplit parameter: `|B_q|=(p^2+1)/2` is odd and has gcd `1` with each of `p-1,p+1`. The same absence holds at `(p,r)=(2,2)`.

For a non-invariant orbit represented by `theta`, Clifford theory gives the single irreducible `Ind_L^G(theta)` of degree `r theta(1)`, zero on `G-L`, with restriction `sum_j theta^{sigma^j}`. If that sum is nonzero at `x in L`, at least one summand is nonzero. Hence the `L` audit implies

`o(x) r theta(1) | r|L|=|G|`.

For invariant `theta`, choose an intertwiner `T`. Schur's lemma gives `T^r=cI`; rescaling `T` by an `r`th root of `c^{-1}` gives `T^r=I` and hence an extension. All extensions are `hat(theta) tensor lambda_k`, `k=0,...,r-1`, where `lambda_k(sigma)=zeta_r^k`. On `L` they have value `theta(x)` and degree `theta(1)`, so the `L` audit again proves the source implication there. On `L sigma^i`, their values differ by the exact nonzero factor `zeta_r^{ki}`; therefore extension choice never changes zero support. This proves the scalar statement rather than assuming it.

## 3. Exact semilinear orders and the projective correction

For `x=g sigma^i`, `1<=i<r`, set

`N_i(g)=g sigma^i(g) ... sigma^{(r-1)i}(g)`.

Then `x^r=N_i(g)`. Generalized Lang conjugacy places `N_i(g)` in an `L`-class represented by an element `n_i` of

`H=L^{<sigma>} = PSL(2,p)`, except that `H=PGL(2,p)` when `p` is odd and `r=2`.

The exception is forced by the fixed-point sequence for `1 -> {±I} -> SL(2,q) -> L -> 1`: `H^1(C_r,{±I})` is trivial except for odd `p,r=2`, when it has order two and supplies the diagonal coset of `PGL(2,p)`. Thus the scalar/projective correction is not omitted. For `(p,r)=(2,2)`, `H=PSL(2,2)=S_3`.

Since `xL` has order `r`, if `o(x)=rm` then `o(x^r)=m`; consequently

`o(g sigma^i)=r o(n_i)`

with no coprimality assumption. In particular, when `r=p` and `n_i` is unipotent, the exact order is `p^2`, not `p`.

The possible `o(n_i)` are `1,p`, divisors of `(p-1)/d,(p+1)/d` in `PSL(2,p)`, and divisors of `p-1,p+1` in `PGL(2,p)`.

## 4. The exact Shintani support lemma that remains to be justified

For a preferred extension of invariant `theta`, transport the class function on `L sigma^i` along the norm bijection. The needed lemma is:

1. For odd `r`, this transported function is, up to a nonzero root of unity, the row of `PSL(2,p)` of the same rank-one type. Split parameters descend through the ordinary norm `A_q -> A_p`; nonsplit parameters descend through `z -> z^{(q+1)/(p+1)}`. Thus its values are exactly the preceding table with `q` replaced by `p` (and possibly the two exceptional signs interchanged).
2. For odd `p,r=2`, the transported rows on `PGL(2,p)` are: `1 -> 1`, `St_q -> St_p`; a split parameter pulled back from `F_p^*` goes to the principal row `P_alpha`; an anti-invariant split parameter pulled back from the norm-one torus goes to the cuspidal row `C_beta`; and the unordered exceptional pair goes to `{delta, delta St_p}`, where `delta` is the diagonal linear character. The exact `PGL(2,p)` values are

| row | `1` | unipotent | split ratio `a` | nonsplit ratio `b` |
|---|---:|---:|---:|---:|
| `St_p` | `p` | `0` | `1` | `-1` |
| `P_alpha` | `p+1` | `1` | `alpha(a)+alpha(a)^{-1}` | `0` |
| `C_beta` | `p-1` | `-1` | `0` | `-(beta(b)+beta(b)^{-1})` |
| `delta` | `1` | `delta(u)` | `delta(a)` | `delta(b)` |
| `delta St_p` | `p` | `0` | `delta(a)` | `-delta(b)` |

3. For `(p,r)=(2,2)`, the invariant rows of degrees `1,4,5` descend to the three rows `1,St_2,delta` of `S_3`.

The generic principal/cuspidal assertions follow directly from the semilinear Borel fixed-point sum and the anisotropic-torus sum. The unresolved point in this run is a first-principles derivation that the two exceptional constituents descend individually as stated, rather than merely that their sum does. Restriction to `L` cannot decide this, and cancellation between the two outer traces is exactly the forbidden shortcut in Lead's instruction. A citation-free proof requires writing the exceptional Weil intertwiners (including their Gauss-sum phase) or an independently supplied generalized-Shintani theorem for the central quotient.

## 5. Completed arithmetic once that support lemma is supplied

For odd `r`, `q` and `p` have the same parity and `p-1 | q-1`, `p+1 | q+1`. The transported supports therefore give:

| invariant degree | nonzero norm types needed | required divisor after cancelling outer `r` |
|---:|---|---|
| `1` | all | `o(n)| |L|` |
| `q` | identity or semisimple; unipotent value `0` | `o(n)q | |L|` |
| `q+1` | identity, `p`-unipotent, split | `o(n)(q+1) | |L|` |
| `q-1` | identity, `p`-unipotent, nonsplit | `o(n)(q-1) | |L|` |
| `(q+1)/2` | identity, unipotent, split | `o(n)(q+1)/2 | |L|` |
| `(q-1)/2` | identity, unipotent, nonsplit | `o(n)(q-1)/2 | |L|` |

For odd `p,r=2`, invariant degrees are only `1,q,q+1,(q+1)/2`. Every element order of `PGL(2,p)` is `p` or divides `p-1` or `p+1`. All such orders divide `q(q-1)/2` for degree `q+1`, and divide `q(q-1)` for degree `(q+1)/2`; for degree `q`, the only bad type would be unipotent and `St_p` is zero there. At `q=4`, degrees `1,4,5` and norm orders `1,2,3` give the same result, with the degree-four row zero on norm order two.

Finally, `o(g sigma^i)=r o(n_i)` and `|G|=r|L|`, so the outer `r` cancels exactly. This includes `r=p`.

## What this establishes and does not establish

Established without finite sampling: the complete Frobenius-orbit/Clifford inventory; exact extension multiplicity and scalar behavior; the full source predicate on `L`; exact semilinear order including `r=p`; the `PSL/PGL` fixed-group correction; and a finite row-by-row arithmetic reduction of every outer case.

Not established: the exceptional-constituent Shintani trace lemma (including its phase on every `sigma^i` coset). Consequently this note is not a theorem for `PSL(2,p^r).r`, and certainly not a proof of the universal Kourovka scope.

## Recommended next bounded experiment

Write the two exceptional representations in the standard finite-field Weil model and compute `Tr(rho(g)T^i)` by the quadratic Gauss sum. Kill the route if the trace does not separately vanish on the forbidden torus, or if the central quotient changes the norm target beyond the already identified `PGL(2,p)` correction. This is a representation-changing, one-lemma continuation; no catalogue computation is needed.

