---
title: "Kourovka 21.137 — NS3 fixed outer action outcome"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: NS3-FIXED-OUTER-ACTION
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - project/kourovka
  - status/conjectured
---

# `STRATEGY_EXHAUSTED` — `NS3-FIXED-OUTER-ACTION/F_3^10`

## Active target

Scope: `21.137/odd-prime-exponent-p2`  
Assignment revision: `2`

At the fixed allowed prime `p=3`, a target counterexample must be a finite
3-group of exponent exactly 9 whose complete actual cube-value set itself is a
subgroup and is nonabelian.

## Exact bounded result

None of the `3^10=59,049` labelled central-factor rows in the frozen
`NS3-FIXED-OUTER-ACTION` family can define the proposed extension.  Every row
fails the same action equation for the single quotient pair `(h,j)=(y,x)`.
This conclusion is symbolic and does not rely on categorical row enumeration.

With `[r,s]=r^(-1)s^(-1)rs`, right conjugation `q^g=g^(-1)qg`, and column
matrices, the frozen quotient relation `[y,x]=c` gives `yx=xyc` and
`s(yx)=XYK`.  The frozen lift relation

`[Y,X]=K z^e_YX`

therefore gives `u(y,x)=z^e_YX`.  The factor-system action equation requires

`A B=Inn(z^e_YX) C B A=C B A`.

But exact matrix multiplication gives

`A B(C B A)^(-1)=Inn(a-b)!=I`.

The missing correction is the noncentral element `a-b`; a central power of
`z` has trivial inner action.  All other nine frozen parameters are irrelevant
to this pair, so the contradiction applies simultaneously to all 59,049 rows.

The same sign audit also gives

- `A^3=Inn(a)`, `B^3=Inn(b)`, `C^3=T=I`;
- `q_X=q_Y=a-b` for `[C,A]` and `[C,B]`;
- the outer classes do give `H=H_3(3) x C_3`, with 81 normal forms;
- the action of `[Y,X]` is `A B A^(-1)B^(-1)=Inn(a-b)C`, so the outer
  action is sound while the selected exact lift representative is not.

## What was computed in

Only the five-dimensional BCH coordinate model of
`Q=H_3(3) x C_3^2` and the common action equation for the frozen ten-parameter
factor family were computed.  No factor row and no element of a candidate
group was categorically enumerated.  No candidate group exists inside this
frozen family because the action equation is necessary before associativity.

## Constraint-and-conclusion disposition

| constraint_id | role | disposition in this bounded exclusion |
|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | unrestricted universal scope remains open |
| `21.137-odd-p-not-2` | admissibility | fixed allowed prime `p=3` |
| `21.137-odd-finite-p-group` | admissibility | no group is produced by any frozen row |
| `21.137-odd-exponent-p2` | admissibility | not reached because the action equation fails |
| `21.137-odd-power-set-definition` | admissibility | not reached; no generated-subgroup substitution was made |
| `21.137-odd-power-set-subgroup` | admissibility | not reached |
| `21.137-odd-P-abelian` | target conclusion | not reached; active target unanswered |

## Reproduction

Run:

```text
python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r10-ns3-fixed-outer-action/scratch/ns3_fixed_outer_action.py --sign-gate-only
```

Evidence:

- `scratch/ns3_fixed_outer_action.py`, SHA-256
  `dc44143d0649259d5e8065aadeeff5c06e43ad49e24b2b96be3840a68c8b4046`;
- `scratch/sign-gate-output.json`, SHA-256
  `925e6abf912fca6e53111dba3f5c66d55286ba6c546b10dda45e6e34db4b7254`;
- `log.md` for the independent hand anti-action/sign reconstruction.

## Exact limitation

This exhausts only the central-`N` family exactly as frozen.  It does not
exclude allowing the required `a-b` correction in `[Y,X]`, choosing a different
representative of the same outer class for `C`, adding `<u,v>` corrections,
changing the outer action, or any other extension family.  Every such repair or
enlargement was forbidden here and was not attempted.  The unrestricted
revision-2 target remains unanswered.

