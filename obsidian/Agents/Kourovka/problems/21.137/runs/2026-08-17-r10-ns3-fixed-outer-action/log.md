---
title: "Kourovka 21.137 — NS3 fixed outer action run log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
cycle: extension-2
strategy_id: NS3-FIXED-OUTER-ACTION
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - project/kourovka
  - status/draft
---

# Run log

## Scope lock

This run uses exactly `p=3`,
`Q=H_3(3) x C_3^2`, `H=H_3(3) x C_3`, the four frozen actions in
`NS3-FIXED-OUTER-ACTION`, and the ten central `N=<z>` correction coordinates.
There are exactly `3^10=59,049` labelled factor rows.  The target is a finite
3-group of exponent exactly 9 whose complete actual cube-value set itself is a
subgroup and is nonabelian.  Generated verbal subgroups, `p=2`, exponent 8,
the general powerfulness clause, web/history, catalogues, wreath/quarantined
material, UT7 variations, and family enlargement are excluded.

## Active-time ledger

Shared cumulative ledger enters this run at minute `240`.  Research/search
hard-kills at cumulative minute `288`; minutes `288`--`300` are packaging only.

| UTC start | UTC stop | active minutes this interval | cumulative scope active minutes | activity |
|---|---|---:|---:|---|
| 2026-08-17T06:04:26Z | open | open | 240 at start | protocol, full assigned inbox/refs, action/sign gate |

## 2026-08-17T06:11:17Z — protocol and reference gate

Read in full the common protocol, problem-agent role, every current inbox
message, the canonical revision-2 scope, the MathExpert strategy note, the
authorized MCO verification, and the authorized original counterexample log.
No excluded history, web resource, catalogue, computation artifact, or
quarantined/wreath source was inspected.  No categorical row or element
enumeration has run.

The seven canonical rows are unchanged.  A successful row must pass `p=3`,
finite same-prime group, exact exponent 9, equality with the complete actual
cube set, actual-set subgroup closure, and failure of abelianity.

## Strategy and certificate plan

1. Rederive the matrices, commutator convention, inner defects, and quotient
   order; kill immediately if the frozen lift relations already violate the
   action equation independently of the ten central coordinates.
2. Freeze a purpose-built exact checker for the ten-row factor system.  It must
   separately expose the action equation, cocycle equation, `(C5)`, relator
   checks, and the complete actual cube set.
3. Request an exact Lead compute lease before any categorical enumeration.
4. If admitted rows exist, record actual-set cardinality, subgroup closure,
   abelianity, first closure defect, and first noncommuting actual cubes with
   roots.  If none exist, preserve an exact inconsistency certificate.

The certificate is limited to `NS3-FIXED-OUTER-ACTION/F_3^10`; no outcome from
this family answers the unrestricted scope unless a row is a target-equal
witness satisfying every canonical row.

## 2026-08-17T06:15:24Z — action/sign gate and early search stop

The open ledger marker above is closed at `2026-08-17T06:15:24Z`: 11 active
minutes, cumulative scope minute `251`.  Packaging begins at that instant.
No compute lease was requested because the common pre-enumeration action gate
already eliminates every frozen row.

### Conventions and frozen actions

Use `[r,s]=r^(-1)s^(-1)rs`, `q^g=g^(-1)qg`, and column BCH coordinates
`(a,b,u,v,z)`.  Matrix products are ordinary composition, so the action of
`XY` is `B A`.  In `Q`,

`(r_a,r_b,...,r_z)^(q_a,q_b,...,q_z)` differs only in its `z` coordinate by
`r_a q_b-r_b q_a`.  Thus `Inn(q)` has final-row coefficients
`(q_b,-q_a,0,0,1)`.

Direct calculation gives

- `A^3=Inn(a)` and `B^3=Inn(b)`;
- `C=A^(-1)B^(-1)AB`, `C^3=I`, and `T=I`;
- `[C,A]=[C,B]=Inn(a-b)`, so the required zero-`(u,v,z)` representatives are
  exactly `q_X=q_Y=a-b`;
- the quotient presentation collects uniquely to
  `x^i y^j c^k t^l`, `0<=i,j,k,l<3`, hence is
  `H_3(3) x C_3` of order `3^4=81`.

These facts establish the advertised outer action: the action of `[Y,X]`
differs from `C` only by an inner automorphism.  The precise inner difference,
however, is fatal to the narrower frozen lift family.

### Hand audit of the decisive pair

Take `h=y,j=x`.  Since `[y,x]=c`, one has `yx=xyc` and
`s(yx)=XYK`.  The frozen lift relation gives

`YX=XYK z^e_YX=s(yx)z^e_YX`,

so `u(y,x)=z^e_YX`.  The right-action equation is therefore

`A B = Inn(z^e_YX) C B A = C B A`,

because `z` is central in `Q`.  Direct multiplication gives

```text
A B =
1 0 0 0 0
0 1 0 0 0
1 2 1 0 0
1 0 2 1 0
0 0 1 2 1

C B A =
1 0 0 0 0
0 1 0 0 0
1 2 1 0 0
1 0 2 1 0
1 1 1 2 1
```

Hence

`A B(C B A)^(-1)=Inn(a-b)`,

whose last row is `(2,2,0,0,1)` and which is nonidentity (it sends `a` to
`a-z`).  Equivalently, the action of the word `[Y,X]` is
`A B A^(-1)B^(-1)=Inn(a-b)C`.  The missing correction is the noncentral
kernel element `a-b`; no permitted central power `z^e_YX`, and none of the
other nine central coordinates, can absorb it.

This is a hand sign check independent of the categorical search.  It confirms
the anti-action order and does not silently replace `C` by the reverse
commutator.

### Checker and observed output

Ran only the pre-lease command

```text
python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r10-ns3-fixed-outer-action/scratch/ns3_fixed_outer_action.py --sign-gate-only
```

It returned all ten advertised matrix/action assertions as true, identified
`q_X=q_Y=a-b`, found the decisive equality false with missing
`Inn(a-b)`, and explicitly recorded
`categorical_rows_enumerated: 0` and `group_elements_enumerated: 0`.
The verbatim JSON is `scratch/sign-gate-output.json`.

```text
dc44143d0649259d5e8065aadeeff5c06e43ad49e24b2b96be3840a68c8b4046  scratch/ns3_fixed_outer_action.py
925e6abf912fca6e53111dba3f5c66d55286ba6c546b10dda45e6e34db4b7254  scratch/sign-gate-output.json
```

### Exact consequence and limitation

All `3^10=59,049` frozen central rows fail the first action equation, before
`(C2)--(C5)`, associativity, exponent, or actual-cube-set testing can arise.
This exhausts only `NS3-FIXED-OUTER-ACTION/F_3^10`.  It does not exclude an
extension with the necessary `a-b` correction in `[Y,X]`, a different
representative for `C`, any larger factor family, or any group in the
unrestricted revision-2 target.  Repair or enlargement is explicitly outside
this run.

## Cycle outcome — 2026-08-17T06:19:09Z

`STRATEGY_EXHAUSTED` for exactly
`NS3-FIXED-OUTER-ACTION/F_3^10`; `active_assignment_answered: no`.

Final ledger closure:

| UTC start | UTC stop | active minutes this interval | cumulative scope active minutes | activity |
|---|---|---:|---:|---|
| 2026-08-17T06:04:26Z | 2026-08-17T06:15:24Z | 11 | 251 | protocol/refs, frozen checker, independent action/sign gate |
| 2026-08-17T06:15:24Z | 2026-08-17T06:19:09Z | 4 | 255 | findings, evidence hashes, bus routing, inbox archival |

The run consumed 15 of the 60 granted active minutes and preserves 45 unspent
minutes for Lead scheduling.  Research stopped well before cumulative minute
288.  No categorical row or group-element enumeration ran, no compute lease
was used, and no forbidden family repair was attempted.

