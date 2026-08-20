---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/hall-collection
  - project/kourovka
  - status/conjectured
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy_id: GRAD-PIMAGE-MINIMAL-WEIGHT
outcome: PARTIAL_RESULT
---

# Minimal-weight power-image reduction

## Active target

For odd prime `p`, finite same-`p` group `G` of exponent exactly `p^2`, and the
literal value set `P={g^p:g in G}` assumed to be a subgroup, determine whether
`P` must be abelian.  The `p=2` and exponent-eight scopes are excluded.

## Candidate exact partial result

If a counterexample exists, let `Q` be the first lower-central quotient in
which the image `Pbar` of `P` is nonabelian.  Then:

1. `Pbar'` is nontrivial and central in `Q`, while `exp(Pbar)|p`.
2. `class(Q)>=p+2` by the reviewed class-at-most-`p+1` theorem.
3. `|Pbar|>=p^(p+2)`, hence `|G|>=p^(p+3)`.
4. For any noncommuting `A,B in Pbar` and any closure root `z^p=AB`, on the
   Baer Lie algebra `L(Pbar)` the operator `D=c_z-I` satisfies
   `D^p=ad(log(AB))`, `D^p(A)=[A,B] != 0`, and `D(log(AB))=0`.  Thus `D`
   contains a `J_(p+1)` block plus a fixed noncentral vector outside it.

The third and fourth assertions are one exact structural obstruction, not
independent estimates.

## Derivation

Closure gives `P=G^p`; because every element of this subgroup is itself an
actual `p`th power and `exp(G)=p^2`, `exp(P)|p`.

Choose least `c` with `P'` not contained in `gamma_(c+1)(G)` and put
`Q=G/gamma_(c+1)(G)`.  Then `Pbar'` lies in
`gamma_c(Q)<=Z(Q)`.  For noncommuting `A,B in Pbar`, closure supplies `z` with
`z^p=AB`.  The odd-prime Baer correspondence turns `Pbar` into an
`F_p`-Lie algebra.  If `q=log(AB)`, conjugation `alpha=c_z` is linear and

`alpha^p=c_(z^p)=c_(AB)=I+ad(q)`.

Writing `D=alpha-I` and using characteristic `p` gives

`D^p=alpha^p-I=ad(q)`.

Since `z` centralizes its own power, `D(q)=0`.  With `C=[A,B]`, centrality of
`Pbar'` gives `D(C)=0`, while `D^p(A)=[A,q]=C`.  Therefore
`A,D(A),...,D^p(A)` are `p+1` independent vectors.  The fixed vector `q` is
outside their span, since the kernel on that Jordan block is `<C>` but `q` is
noncentral.  This gives `dim L>=p+2`.  Also `z^p=AB !=1`, so `z` has order
`p^2` and `Q/Pbar` is nontrivial, giving the order bound for `G`.

At the Hall level the same issue is the coefficient-one extreme term in

`[A,z^p]=[A,z]^p [A,z,z]^binom(p,2) ... [A,{}_p z] * (central nonlinear terms)`.

Exponent `p` kills the earlier linear factors but not `[A,{}_p z]`, whose
coefficient is `binom(p,p)=1`.  The Lie identity above is the exact version
that retains all central nonlinear corrections.

## Why the natural induction stalls

Let `U=Q/C_Q(Pbar)`.  Exactly, as literal sets,

`{u^p:u in U}=Inn(Pbar) ~= Pbar/Z(Pbar)`.

Thus the closure hypothesis descends to a strictly smaller exponent-`p^2`
action quotient, but its power image is already abelian.  The target
commutator `Pbar'` has been killed in the kernel.  Roots of `A`, `B`, and `AB`
yield only

`D_(AB)^p=D_A^p+D_B^p=ad(A)+ad(B)`;

closure provides no coherent relation among the three unpowered operators.

## Sharpness and scope warning

The `J_(p+1)` condition has a prime-uniform hand model of dimension `p+2`:
take basis `e_0,...,e_p,q`, bracket `[e_0,q]=e_p`, and the shift
`D(e_i)=e_(i+1)`, `D(e_p)=D(q)=0`.  Then `T=I+D` is a Lie automorphism with
`T^p=I+ad(q)`, and it embeds in an exponent-`p^2` cyclic extension having a
root of `q`.  In BCH coordinates the explicit factors
`A=e_0`, `B=q-e_0-(1/2)e_p` satisfy `A*B=q` and `[A,B]=e_p`.
The extension modulo this exponent-`p` subgroup is cyclic of order `p`, so
all elements have order dividing `p^2`; the displayed root has order `p^2`.

This model is **OUT OF SCOPE as a candidate group**: its designated nonabelian
subgroup is not shown to equal the literal `p`th-power image, nor are the two
chosen factors individually shown to be values.  Its only role is to show
that the single product-root leading equation and the dimension bound are
sharp.

## What this does not establish

- It does not show `P` is abelian and does not answer the unrestricted scope.
- It does not produce an admissible counterexample.
- It does not prove that the three root operators admit a coherent section;
  the absence of such a relation is precisely the remaining gap.
- The lower bound is a candidate partial lemma pending independent Validator
  reconstruction; status remains `conjectured`.

## Evidence

The full hand derivation, exact Hall obstruction, sharpness construction, and
active-time ledger are in
`Agents/Kourovka/problems/21.137/runs/2026-08-17-r21-grad-pimage-minimal-weight/log.md`.
No computation was performed.
