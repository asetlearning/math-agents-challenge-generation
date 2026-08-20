---
title: "Kourovka 21.137 — final route: K32 nonsplit root saturation"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: K32-NONSPLIT-ROOT-SATURATION
direction: counterexample
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - project/kourovka
  - status/conjectured
---

# Final 55-minute route

## Source status and exact target

Source status: **general mathematical knowledge, unverified**, except for the
status/conjectured structural facts explicitly imported from the two reviewed
verification notes in the request. This is a proposal, not a certification.

The only success target is a finite group at `p=3`, of exponent exactly `9`,
whose **complete actual** cube-value set is a subgroup and is nonabelian. A
generated cube subgroup, a nonclosed value set, or merely commuting cubes is a
failure.

## Comparison and selection

The proof direction has four recent exact observable failures: pair-root,
triple-root, complete root-fibre marks, and the prime-uniform PF capacity cell.
Another local identity or counting relaxation therefore has lower marginal
value. The split PF group and its fixed transvection have exact exponent `9`
but fail closure already in their complete value sets. I select the
**counterexample** direction and change the extension class rather than add an
automorphism generator.

## Frozen starting data

Retain the notation of the exact PF note:

`P=H_3(3) x C_3^2`, with `V=<e,f>`, `Z=<c,z_1,z_2>`, `[e,f]=c`, and the
automorphisms `U,A_e,A_f` defined there. Work in `Out(P)` and freeze

`R_0=<bar(U),bar(A_e),bar(A_f)>`.

There are no alternate generators. Gate 0 is to collect this one subgroup by
hand and either identify it with the displayed `K32` group from the order-`3^10`
note (order `3^5`, exponent `3`, two-dimensional central commutator image) or
kill the strategy. Set `R=R_0 x <tau>`, where `tau` is one extra central element
of order `3` acting trivially on `P`.

The single construction problem is the **nonsplit** extension

`1 -> P -> G -> R -> 1`

with the frozen outer action above and a central lift `z` of `tau` satisfying
`z^3=c`. All section discrepancies are the canonical ones obtained from the
fixed representatives `U,A_e,A_f`; only the forced `N=<c>`-valued corrections
may be solved for. No different representative, extra automorphism, quotient
type, or parameter family is allowed.

Mechanism: the reviewed minimal-central note records that a central order-nine
element with cube `c` translates any one root over a label through the whole
`<c>`-fibre. Thus the hard issue is reduced to the quotient label set in
`A=P/<c>`, not silently replaced by the subgroup it generates. If the exact
label set is all of `A`, the central shifts give the whole of `P` as actual
cubes; `[e,f]=c` then supplies the required nonabelianity.

## Frozen schedule and kill gates

1. **0--10 minutes — outer-action gate.** Collect exactly
   `<bar(U),bar(A_e),bar(A_f)>`. Success certificate: a five-coordinate `K32`
   normal form and complete relation table. Kill immediately if its order,
   exponent, or commutator rank differs, or if an imported inner/outer equality
   is only assumed.
2. **10--24 minutes — extension-obstruction gate.** Write the PC/Schreier
   consistency equations for the fixed representatives, with `z` central and
   `z^3=c`. Success certificate: one complete consistent presentation and its
   order. Kill if the obstruction is nonzero, consistency forces `c=1`, or any
   unlisted correction choice is needed. Do not repair the action.
3. **24--42 minutes — complete label formula.** Derive one closed formula for
   the cube of every normal-form element; reduce its image modulo `<c>` for all
   `3^5` `R_0` labels symbolically, not by image generation. Success requires
   the **actual** quotient label set to equal `A=P/<c>`. One missing label kills
   the construction.
4. **42--50 minutes — fibre and exponent audit.** Use `(gz^k)^3=g^3c^k` to
   prove every central fibre is filled, and prove no cube lies outside `P`.
   Check `P` has exponent `3`, `[e,f]=c!=1`, every element of `G` has ninth
   power one, and `z` has order `9`.
5. **50--55 minutes — certificate.** Write the presentation, full cube formula,
   value-set equality, order, exact exponent, and every canonical constraint row.

Absolute stop is **55 active minutes**. A gate failure is an exact
`STRATEGY_EXHAUSTED` certificate for this one outer action and nonsplit lift; it
does not authorize a whole-scope park, a new PF generator, or a second cocycle
ansatz.

## Exact success certificate

A hit must contain all of the following, with no inferred substitution:

- a reconstructible finite PC presentation and order of `G`;
- `p=3` and `exp(G)=9` exactly;
- a closed formula whose image is the complete set `{g^3:g in G}`;
- equality of that image with `P`, not with `<{g^3}>`;
- subgroup closure of `P` from that equality;
- the explicit nontrivial commutator `[e,f]=c` inside the same `P`;
- the seven-row revision-2 constraint-and-conclusion matrix.

## Self-critique

The likeliest failure is that the fixed outer action has a nonzero extension
obstruction, or that its exact quotient cube labels occupy a proper subset of
`A`; the central order-nine lift fills only the `<c>` coordinate and cannot
repair a missing quotient label. This is why both are early hard gates. The
route is still preferable to another proof relaxation: it tests the full value
set on one fixed nonsplit construction, and it is not another holomorph-generator
search.

## References

- `Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json`
- `Agents/Kourovka/problems/21.137/verification/2026-08-16T181302Z-minimal-central-obstruction.md`
- `Agents/Kourovka/problems/21.137/runs/2026-08-17-r17-o310-equivariant-label/findings.md`
- `Agents/Kourovka/problems/21.137/runs/2026-08-17-r18-pf-holomorph-cube/findings.md`
- `Agents/Kourovka/problems/21.137/runs/2026-08-17-r19-pf-holomorph-transvection/findings.md`
