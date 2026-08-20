---
title: "Problem 20.115 cycle 15 partial - component-cycle trace transfer"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
outcome: PARTIAL_RESULT
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
---

# Component-cycle trace transfer: exact reduction and remaining overlap

## Active target

Scope: `20.115/nonzero-character-order-divisibility`, revision 1.

The source asks whether, for every finite G, ordinary chi in Irr(G), and x in G,
the exact condition chi(x) != 0 implies o(x) chi(1) divides |G|.

This note does **not** answer that universal question. It treats the branch of a
hypothetical least-order counterexample in which a proper minimal normal subgroup
is N = S^t with S nonabelian simple and

    chi restricted to N = a theta.

The conclusion is an exact component-cycle formula, a kernel reduction, and the
first scalar-overlap gate that the formula does not itself settle.

## Constraint-and-conclusion matrix

| constraint id | role | use here | result |
|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | Assume a least-order counterexample only to invoke the source implication for strictly smaller ordinary groups. | branch reduction only |
| `20.115-G-finite` | admissibility | All groups, quotient orders, component orbits, and central extensions used below are finite. | pass in branch |
| `20.115-chi-complex-irreducible` | admissibility | chi is always ordinary irreducible. Projective P and D arise only from Clifford factorization; every minimality invocation is on an ordinary irreducible character. | pass in branch |
| `20.115-x-in-G` | admissibility | x is in G and q, k below use its exact quotient and kernel orders. | pass in branch |
| `20.115-character-value-nonzero` | admissibility | Exact nonvanishing factors into nonvanishing of the multiplicity trace and every component-cycle trace. No statement about chi(x^m) is used. | pass in branch |
| `20.115-order-degree-divisibility` | target conclusion | Reduced to the explicit primewise absorption inequality in the final section. | not established universally |

## 1. Clifford tensor factorization, derived directly

Homogeneity makes theta G-invariant. Let V afford theta and identify the
chi-module as V tensor W as an N-module, where dim W = a and N acts trivially on
W. For each g in G choose an intertwiner P(g) on V satisfying

    P(g) rho(n) P(g)^(-1) = rho(g n g^(-1))

and P(n) = rho(n) for n in N. Schur's lemma gives a scalar factor set alpha,
inflated from Q = G/N:

    P(g) P(h) = alpha(gN,hN) P(gh).

After removing P(g) from the ordinary operator affording chi(g), what remains
centralizes rho(N), hence is I_V tensor D(gN). Thus

    R(g) = P(g) tensor D(gN),

where D is an irreducible alpha^(-1)-projective representation of Q of degree a.
Consequently

    chi(x) = Tr(P(x)) Tr(D(xN)).                         (1)

In particular chi(x) != 0 makes both factors in (1) nonzero.

## 2. Exact trace formula on the component cycles

Write N = S_1 x ... x S_t and

    theta = phi_1 tensor ... tensor phi_t,

with phi_i in Irr(S_i), afforded on V_i. Minimal normality makes G transitive on
the S_i, so all phi_i have a common degree d and theta(1) = d^t.

Let sigma be the permutation of the components induced by x. Choose intertwiners

    U_i : V_i -> V_{sigma(i)}

implementing conjugation by x. Up to one nonzero global scalar, P(x) is the tensor
of the U_i followed by the tensor-factor permutation sigma.

For a cycle

    C = (i_0 i_1 ... i_(ell-1)),   sigma(i_j) = i_(j+1),

put

    B_C = U_(i_(ell-1)) ... U_(i_1) U_(i_0) : V_(i_0) -> V_(i_0).

A basis coefficient contributes to the trace exactly when its indices agree all
the way around every cycle. Summing those coefficients gives the exact identity

    Tr(P(x)) = lambda_x product_C Tr(B_C),               (2)

where lambda_x is a nonzero scalar depending only on the initial normalization.
Thus (1)--(2) imply

    Tr(D(xN)) != 0  and  Tr(B_C) != 0 for every cycle C. (3)

This is the required noncancellation statement. It is not an assertion that
chi(x^ell) is nonzero.

For a fixed component (ell = 1), B_C is just its single intertwiner U_i. For a
nontrivial permutation cycle (ell > 1), it is the ordered product of all
intertwiners around that cycle; none of the individual traces is relevant.

Let gamma_C be the automorphism of S_(i_0) induced by x^ell. Then B_C intertwines
phi_(i_0) with gamma_C. Set

    L_C = < Inn(S_(i_0)), gamma_C > <= Aut(S_(i_0)).

The quotient L_C/S_(i_0) is cyclic. Therefore phi_(i_0) extends to an ordinary
irreducible character phi_tilde_C of L_C; rescaling B_C gives an extension
operator. Equation (3) says exactly

    phi_tilde_C(gamma_C) != 0.                            (4)

If gamma_C is inner, say gamma_C = Inn(s_C), then (4) specializes to the ordinary
component value phi_(i_0)(s_C) != 0, up to a nonzero scalar. If gamma_C is outer,
the precise nonzero datum is instead the ordinary extension value in (4), not a
fictional value of phi_i on an element outside S_i.

## 3. What smaller-group minimality gives

Put

    q = o(xN),    k = o(x)/q,    x^q = (n_1,...,n_t) in N.

For cycle C of length ell, let m_C = q/ell and write

    r_C = o(gamma_C),
    c_C = o(gamma_C S_(i_0)) in L_C/S_(i_0),
    h_C = r_C/c_C.

We have c_C divides m_C and

    gamma_C^(m_C) = Inn(n_(i_0)).

Since S is centerless, if k_C = o(n_(i_0)), then

    k_C = r_C / gcd(r_C,m_C)
        = h_C / gcd(h_C,m_C/c_C),

so k_C divides h_C. The coordinates n_i on one x-cycle are conjugate and have
the same order, and therefore

    k = lcm_C k_C divides lcm_C h_C.                     (5)

Suppose each L_C has order strictly smaller than |G|. This is automatic when
t > 1: the stabilizer in G of one component has index t, and L_C is an image of a
subgroup of that proper stabilizer. It also holds for t = 1 whenever the relevant
component automorphism group is a proper quotient/subgroup of G. The possible
t = 1, C_G(S) = 1, L_C = G almost-simple equality case is not covered.

Apply least-order minimality to the ordinary triple

    (L_C, phi_tilde_C, gamma_C).

By (4),

    r_C d divides |L_C| = |S| c_C,

and cancellation of c_C gives

    h_C d divides |S|.                                  (6)

Let M = |S| and b = M/d. Equations (5)--(6) yield the clean kernel conclusion

    k divides b,
    k theta(1) = k d^t divides M^t = |N|.               (7)

This treats fixed and nontrivial component cycles uniformly while deriving their
trace inputs separately.

## 4. Exact scalar-lift deficiency from the Clifford cocycle

The projective data now enter only as a proof vehicle. Let z be the order of the
cohomology class of alpha. Determinants of P and D show

    z divides both theta(1) and a.

On the cyclic subgroup generated by y = xN, the exact restriction scalar is

    c_x = P(x)^q rho(x^q)^(-1),

which is scalar by Schur's lemma. In tensor-cycle coordinates, c_x is obtained by
raising each B_C through q/ell turns and comparing the resulting operator with
rho_(i_0)(n_(i_0)); the product of those local comparison scalars, together with
the chosen global normalization of P(x), is c_x. Nonzero traces in (3) do not
control the order of this scalar. Passing to the inverse factor set replaces c_x
by its inverse and hence preserves its order.

The tensor construction also localizes the source of alpha. Embed the action of
G/C_G(N) in `Aut(S) wr Sym(t)`. Choose projective intertwiners for the inertia
group of one component character phi, with local factor set beta, and transport
them to the other components. Tensor-factor permutation operators compose
genuinely, with no scalar factor. Therefore alpha is the restriction of a product
of transported beta-values, and

    order([alpha]) divides order([beta]).

In particular permutation cycles themselves create no new scalar prime. Every
prime in Delta comes from a local outer-automorphism Clifford obstruction for phi.
The determinant of the degree-d local intertwiner representation also gives
`order([beta]) | d`; hence z and Delta divide d, a sharper tensor bound than
`z | d^t`.
What is *not* obtained formally is the needed codegree bound
`order([beta]) | |S|/phi(1)`; that is precisely the remaining theorem check.

Realize alpha on a cyclic scalar extension

    1 -> Z -> Q_hat -> Q -> 1,   |Z| = z,

and lift D to an ordinary irreducible character D_hat of Q_hat. Among the lifts
of y = xN, choose y_hat so that the order e of y_hat^q is maximal (primewise,
possible because Z is cyclic). Then o(y_hat) = q e, e divides z, and

    D_hat(y_hat) != 0.

Also |Q_hat| = z|Q| < |N||Q| = |G|, because z <= theta(1) < |N|. Least-order
minimality, now applied to the ordinary triple (Q_hat,D_hat,y_hat), gives

    q e a divides z |Q|.                                 (8)

For this minimal scalar extension and this optimized exact lift, define the assigned
**scalar-lift deficiency** by

    Delta = z/e.                                         (9)

Thus e Delta = z. If the kernel supplies

    k theta(1) Delta divides |N|.                         (11)

then multiplying this divisibility by (8) gives

    (q e a)(k theta(1) Delta)
      = q k a theta(1) z
      divides z |Q| |N|.

Cancellation of z proves o(x) chi(1) divides |G|. This is why the full factor
Delta = z/e, rather than the false multiplicity factor a, belongs in the corrected
kernel gate.

For comparison only, the gauge-independent *quotient divisor deficit*

    delta_Q = q a / gcd(q a, |Q|)

satisfies delta_Q divides Delta by (8). It can be smaller than Delta and therefore
cannot be substituted for the assigned scalar-lift condition (11).

No multiplicity factor a belongs in (11).

## 5. Exact remaining overlap and conditional families

Using M = d b, condition (11) is equivalent to

    k Delta divides b^t.                                 (12)

The component-cycle argument proves k divides b, but gives no relation between
the unused p-parts of b^t/k and the global scalar-lift deficiency Delta. Prime by
prime, (12) is exactly

    v_p(k) + v_p(Delta) <= t v_p(M/d).                   (13)

Therefore this branch is completed under any of the following explicit conditions:

1. Delta = 1 (the chosen scalar lift uses the entire scalar kernel);
2. Delta divides (M/d)^(t-1);
3. more generally, the exact inequalities (13) for all primes;
4. when t >= 2, the convenient sufficient condition Delta divides M/d;
5. using Delta divides d, the checkable condition d divides (M/d)^(t-1).

### Exact projective trace family showing Delta need not be 1

The nonzero multiplicity trace cannot by itself force the scalar lift to use all
of Z. For every r >= 1, let

    Q = (C_2 x C_2) x C_(2^r).

Inflate to Q the nontrivial factor-set class of C_2 x C_2 represented by the
central extension Q_8 -> C_2 x C_2. Its scalar center is Z = {+1,-1}, so z = 2.
Let D_0 be the faithful ordinary degree-2 representation of Q_8, viewed as the
corresponding irreducible projective representation of C_2 x C_2, and put

    D = D_0 tensor lambda,

where lambda is any linear character of C_(2^r). For y = (1,c), with c a generator
of C_(2^r),

    D(y) = lambda(c) I_2,
    Tr(D(y)) = 2 lambda(c) != 0.

The scalar extension is Q_8 x C_(2^r). Both lifts (+1,c) and (-1,c) have q-th
power 1 because q = 2^r is even. Hence e = 1 for every lift and

    Delta = z/e = 2.                                    (14)

Thus exact nonzero projective trace is compatible with a genuine leftover scalar
factor. This family is a proof-vehicle obstruction only: it is not asserted to be
the Clifford quotient of a simple-component character triple and is not a source
counterexample. It shows why replacing Delta by 1 from trace nonvanishing would be
invalid.

The first unavoidable overlap loss is also exact. If phi has p-defect zero,
meaning v_p(d) = v_p(M), then v_p(M/d) = 0. Equations (6)--(7) force p not to
divide k, but **any** p-part of Delta makes (11) impossible, for every t. More
generally the excess

    max(0, v_p(k) + v_p(Delta) - t v_p(M/d))

is precisely the missing p-power. The cycle traces cannot see it: they determine
the B_C and gamma_C restrictions, whereas Delta is the part of the global scalar
kernel not generated by the q-th power of the chosen lift of y. The cyclic
extension of each local phi_i removes the local cocycle only on that one cyclic
component group; it does not trivialize the global Clifford class on Q.

Accordingly, a sharp conditional obstruction family is:

- a G-invariant tensor theta = phi^tensor t with phi of p-defect zero;
- all component-cycle extension values in (4) nonzero;
- a multiplicity projective character D with Tr(D(y)) != 0 and p dividing Delta.

Every such character triple fails the corrected kernel gate by exactly the
p-part of Delta. This is an inference obstruction, not an asserted existence
family and not a counterexample to the source problem.

## What this establishes

- An exact basis-level tensor-permutation trace formula.
- Exact nonzero ordinary extension-character values on every component cycle.
- The kernel divisor k theta(1) divides |N| under the stated strict-smaller local
  group hypothesis.
- The exact scalar-lift Delta = z/e and the exact absorption criterion (13).
- Conditional orbit/coprimality families in which the corrected transfer closes.

## What this does not establish

- It does not show (13) for every Clifford character triple.
- It does not settle the t = 1 almost-simple equality case.
- The conditional p-defect-zero obstruction above is not claimed to be realized by
  a finite group with all stated nonzero traces.
- It does not prove the universal source conclusion and supplies no counterexample.

## Recommended next theorem check

The most targeted continuation is to determine whether the Clifford obstruction
for an Aut(S)-invariant irreducible phi has p-part zero whenever phi has p-defect
zero, or more generally whether its scalar deficiency always satisfies (13). A
positive theorem of the form

    Delta divides (|S|/phi(1))^(t-1)

would close the t > 1 branch immediately. A single exact invariant defect-zero
character with p dividing Delta and a nonzero multiplicity trace would show that
component-cycle transfer alone cannot close it.
