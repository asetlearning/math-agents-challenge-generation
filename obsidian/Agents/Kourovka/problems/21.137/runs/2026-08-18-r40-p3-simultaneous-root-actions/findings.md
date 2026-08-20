---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/conjectured
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
outcome: STRATEGY_EXHAUSTED
strategy: P3-SIMULTANEOUS-ROOT-ACTIONS
active_assignment_answered: no
---

# P3-SIMULTANEOUS-ROOT-ACTIONS — exact gauge failure certificate

## Outcome

`STRATEGY_EXHAUSTED` for the named simultaneous-section obstruction only.  The
complete p=3 subfamily and the universal odd-prime target remain unanswered.

## Exact result of the first gate

In a least p=3 counterexample, an independent quotient argument gives
`P'=C_3 <= Z(G)` and `P` of class 2 and exponent 3.  For a normalized section
`sigma:H=G/P -> G`, put

```text
alpha_h = conjugation by sigma(h),
f(h,k) = sigma(h)sigma(k)sigma(hk)^-1,
a_h = sigma(h)^3.
```

The full simultaneous datum satisfies

```text
alpha_h alpha_k = Inn(f(h,k)) alpha_hk,
f(h,k)f(hk,l) = alpha_h(f(k,l))f(h,kl),
a_h = f(h,h)f(h^2,h),
alpha_h^3 = Inn(a_h),
F_h = {u alpha_h(u) alpha_h^2(u)a_h:u in P},
P = union_h F_h.
```

Let `Z=Z(P)`, `rho_h=alpha_h|Z`, and `D_h=rho_h-1`.  The restrictions form a
genuine `H`-module and `D_h^3=0`.  For every arbitrary normalized global
one-cochain `z:H->Z`, the simultaneous section replacement
`sigma'(h)=z_h sigma(h)` gives

```text
alpha'_h = alpha_h,
f'(h,k) = z_h rho_h(z_k) f(h,k) z_hk^-1,
a'_h = (D_h^2 z_h) a_h,
F'_h = F_h.
```

All multiplication and associativity laws survive because the change in `f` is a
central two-coboundary.  The literal coverage equation survives fibre by fibre.
Consequently a nonzero center-action-square `D_h^2z_h` is global section gauge,
not an obstruction.

For actual noncommuting cube values `A,B`, closure supplies the actual value
`AB`, but only three incidences `A in F_h`, `B in F_k`, `AB in F_l`.  It does not
give `l=hk`.  The coherence equations couple `h,k,hk`, so they do not couple the
three power values without the additional root-coset matching assertion
`AB in F_hk`.  That assertion is not a consequence of literal cube-set closure:
`(xy)^3 in F_hk` need not equal `x^3y^3`.

Thus noncommuting values `A,B,AB` are compatible with every displayed global law
conditionally whenever they occur in the complete fibres; the central square term
does not change their commutator or the fibres.  This is a method-failure
certificate, not a construction or counterexample.

## Exact bottleneck

The action/factor/associativity datum is complete for reconstructing an extension,
but the target-facing hypothesis enters only as the gauge-invariant set cover
`P=union_h F_h`.  It supplies no multiplicative selector from power values to
quotient root cosets.  Continuing would require a genuinely new gauge-invariant
consequence of the *entire literal cube map*; further section, factor, selected-root,
or center-coordinate equations repeat the exhausted mechanism.

## Constraint-and-conclusion audit

| constraint_id | role | result in this run |
|---|---|---|
| 21.137-odd-forall-p-G | admissibility | Not answered; only p=3 was assigned, and no p=3 theorem resulted. |
| 21.137-odd-p-not-2 | admissibility | Kept exactly: p=3. |
| 21.137-odd-finite-p-group | admissibility | No candidate group was asserted; the derivation is conditional for finite 3-groups. |
| 21.137-odd-exponent-p2 | admissibility | Exact exponent 9 used in deriving `exp(P)=3`; no witness asserted. |
| 21.137-odd-power-set-definition | admissibility | Kept literally as `P=union_h F_h`. |
| 21.137-odd-power-set-subgroup | admissibility | Used to make `P` a kernel/group and to infer `AB in P`; it does not imply root-coset matching. |
| 21.137-odd-P-abelian | target conclusion | Neither established nor violated by a complete candidate. |

The p=2 exponent-8 clause and the powerfulness question were not used.

## What this does not establish

- It does not prove the p=3 subfamily or the universal odd-prime statement.
- It does not construct any finite group or counterexample.
- It does not show that no other gauge-invariant consequence of literal cube-set
  saturation exists.
- It does not authorize replacing the literal cube set by its generated subgroup.

## Recommendation

Do not continue with another section/lift/factor-coordinate refinement.  Ask a
fresh MathExpert for a representation-changing route whose primitive object is the
complete literal cube map and whose first gate is gauge invariant.  Any continuation
inside extension data must first supply a proved substitute for the missing
root-coset matching statement; absent that, it repeats the killed mechanism.

Full derivation: `Agents/Kourovka/problems/21.137/runs/2026-08-18-r40-p3-simultaneous-root-actions/log.md`.
