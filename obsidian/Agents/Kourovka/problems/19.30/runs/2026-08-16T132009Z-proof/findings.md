---
title: "Kourovka 19.30 — minimal-normal prime-power separator"
author: operator
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
cycle_outcome: PARTIAL_RESULT
validator_status: pending
witness_equals_target: false
active_assignment_answered: no
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
---

# Minimal-normal prime-power separator

## Active target

Scope: `19.30/vanishing-order-simple-recognition`

Assignment revision: 1

Target statement: For every finite group G and finite simple group S, if
\(|G|=|S|\) and G and S have the same set of orders of vanishing elements, then
G is isomorphic to S.

## Candidate partial result

Let \(S\) be finite simple of order \(m\), and let \(p^a=m_p\). If

1. every proper nonabelian characteristically simple divisor \(A\) of \(m\)
   has \(p\nmid|A|\);
2. every characteristically simple \(p'\)-group \(A\) with \(|A|\mid m\)
   has \(p\nmid|\operatorname{Aut}(A)|\);
3. \(S\) has a vanishing element of order \(p^a\); and
4. \(S\) is the unique finite simple group of order \(m\),

then every finite \(G\) of order \(m\) with the same vanishing-element-order set
as \(S\) is isomorphic to \(S\).

The proof draft is
`scratch/minimal-normal-prime-separator.md`. Its two central steps are:

- the minimal-normal hypotheses force every nonsimple same-order group to have a
  normal Sylow \(p\)-subgroup;
- if a Sylow \(p\)-subgroup \(P\triangleleft G\) has order \(p^a\), then
  \(p^a\notin V_o(G)\): a noncyclic \(P\) has no element of that order, while
  for cyclic \(P\), Clifford orbit sizes are prime to \(p\) and cyclotomic
  divisibility prevents their root sums from vanishing on a generator.

For \(a=1\), the argument gives the requested exact prime-order statement. A
normal or even characteristic subgroup of order \(p\) alone is insufficient to
exclude \(p\) from the invariant unless it contains every order-\(p\) element.
The draft records \(C_2\times S_3\) as a hand-checkable warning example.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | partial theorem use | evidence | result for universal target |
|---|---|---|---|---|---|
| 19.30-forall-GS | admissibility | every admissible pair \((G,S)\) | replaced by an explicit sufficient subclass of \(S\) | theorem statement in proof draft | not established universally |
| 19.30-G-finite | admissibility | \(G\) finite | minimal normal subgroups, Sylow theory, and ordinary characters | Lemmas 2–3 | used in covered subclass |
| 19.30-S-finite-simple | admissibility | \(S\) finite simple | assumed; simple-order uniqueness is an added sufficient hypothesis | Theorem 4 | used in covered subclass |
| 19.30-vanishing-definition | admissibility | zero of some irreducible complex character | used exactly through Clifford restriction and the target zero | Lemmas 1–2 and Theorem 4 | used exactly |
| 19.30-equal-orders | admissibility | \(|G|=|S|=m\) | transfers the full \(p\)-part and divisor conditions | Lemma 3 and Theorem 4 | used in covered subclass |
| 19.30-equal-vanishing-order-sets | admissibility | equality of sets, without multiplicity | contradicted by presence/absence of the single integer \(p^a\) | Theorem 4 | used in covered subclass |
| 19.30-isomorphic | target_conclusion | \(G\cong S\) | follows under four added sufficient hypotheses only | Theorem 4 | not established universally |

This matrix forbids a scope-wide `CLAIM`: the universal quantifier and universal
conclusion rows remain open.

## Conditional Suzuki substitution

For \(S=\operatorname{Sz}(2^n)\), odd \(n\ge3\), the draft substitutes a
primitive prime \(p\) with \(\operatorname{ord}_p(2)=4n\) and the explicit
linear condition

\[
  \operatorname{ord}_p(r)>v_r(|S|)
\]

for every odd \(r\ne p\) dividing \(|S|\). The substitution is conditional on
the eight named inputs **(E0)--(E7)** in the draft: Suzuki simplicity/order,
prime-to-three simple-group classification, outer automorphisms, an irreducible
degree, defect-zero vanishing, Bang--Zsigmondy, cyclic relevant Sylow subgroups,
and the automorphism wreath formula.

The full-Sylow-order refinement removes any requirement that the primitive prime
occur to the first power. A bounded arithmetic probe for odd
\(3\le n\le15\) found at least one prime passing the two arithmetic conditions
at each tested exponent; exact code and output are in `scratch/parameter_probe.py`
and `log.md`. This is finite arithmetic data only.

## Exact coverage and noncoverage

Covered by the abstract partial theorem: precisely those finite simple \(S\) for
which some prime \(p\) satisfies all four displayed sufficient hypotheses.

Not established here:

- that every finite simple group satisfies the sufficient hypotheses;
- that even one Suzuki specialization is unconditional under the discovery-blind
  evidence boundary;
- that infinitely many odd Suzuki parameters satisfy the simultaneous linear
  condition;
- any conclusion for a nonisomorphic simple order-twin without the separate
  simple-order-uniqueness hypothesis; or
- the universal target statement.

The cyclic simple groups form an elementary infinite family for the original
scope because every group of prime order is cyclic, but they are not covered by
the separator: abelian groups have no vanishing elements.

## Concrete fixed-target specialization: \(A_5\)

The five-row hand dossier in
`scratch/a5-p5-hypothesis-closure.md` supplies a conjectured, review-pending
specialization at \((S,p)=(A_5,5)\). It derives, without a character table,
classification theorem, mathematical computation, web/history, or delegation:

1. \(|A_5|=60\) and \(A_5\) is simple;
2. the six-point action on Sylow-5 subgroups gives an explicit irreducible
   degree-five character vanishing at \((12345)\);
3. every proper nonabelian characteristically simple divisor of \(60\) has
   order prime to \(5\);
4. every characteristically simple \(5'\)-divisor has automorphism-group order
   prime to \(5\); and
5. every finite simple group of order \(60\) is isomorphic to \(A_5\).

Together with the reviewed separator, these rows give exactly

\[
  \forall G\text{ finite},\qquad
  |G|=60\ \text{and}\ V_o(G)=V_o(A_5)\Longrightarrow G\cong A_5.
\]

This is a singleton fixed-target partial result. It neither quantifies over an
arbitrary finite simple \(S\) nor supplies an infinite family. Its status remains
`status/conjectured`; `witness_equals_target: false` and
`active_assignment_answered: no` continue to control.

## What this does NOT establish

It does not solve Kourovka 19.30, does not provide a counterexample, does not
ground the named Suzuki inputs, does not turn bounded parameter data into an
infinite-family theorem, and does not assert that the sufficient conditions are
necessary.

## How this could be wrong

1. Clifford restriction might have been used with an orbit-size or multiplicity
   hypothesis that fails for a normal cyclic Sylow subgroup.
2. The minimal-normal induction might fail when the minimal normal subgroup is a
   non-full elementary abelian \(p\)-group or when lifting the quotient Sylow
   subgroup across a \(p'\)-kernel.
3. The cyclotomic argument might not justify integrality of the quotient needed
   to infer that a zero sum has length divisible by \(p\).
4. The conditional Suzuki branch could have an incorrect composition-factor,
   automorphism, torus, or character input; none is treated as grounded in this
   blind run.
