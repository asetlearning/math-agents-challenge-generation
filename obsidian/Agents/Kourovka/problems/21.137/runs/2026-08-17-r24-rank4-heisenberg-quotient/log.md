---
title: "Kourovka 21.137 — RANK4-HEISENBERG-QUOTIENT-SEMIDIR run log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
strategy: RANK4-HEISENBERG-QUOTIENT-SEMIDIR
active_minutes_start: 556
active_budget_minutes: 60
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

## 2026-08-17T19:54:32Z — active work start

- Cumulative active minutes on entry: **556**.
- Exact locked scope: `21.137/odd-prime-exponent-p2`, revision 2: odd prime, finite same-prime group, exponent exactly (p^2), literal complete power image itself a subgroup, test abelianity.
- Frozen strategy: one canonical split extension of (K=3_+^{1+4}\times C_3^2) by (Q=H_3(3)), using a genuinely nonabelian root-unipotent action on the four-dimensional symplectic quotient. No alternate action, cocycle, descendant, or catalogue search.
- Source/staleness gates are inherited from the current audited scope record and the fresh Validator source reconstruction in `Agents/Kourovka/problems/21.137/verification/2026-08-17T194155Z-rank4-kernel-hand-exclusion.md`; the rendered page-184 image was also visually inspected in this session and agrees with the locked transcription, including `p != 2`, exponent `p^2`, and the separate exponent-eight 2-group clause. External staleness remains deferred by the discovery-blind scope setting. `source_transcription_checked: yes`; `active_scope_checked: yes`.
- Reviewed bounded fact allowed here: for (M\in\operatorname{Sp}_4(3)) with (M^3=I), ((M-I)^2=0).
- Compute status: no heavy computation started. Derive the action/lift and exact coordinate formulas by hand first; freeze any complete enumerator and request a Lead lease before running it if it reaches the heavy threshold.

### Scope constraint self-check

| constraint_id | role in this experiment |
|---|---|
| `21.137-odd-forall-p-G` | A single (p=3) witness could refute the universal assertion; a failure excludes only this frozen family member. |
| `21.137-odd-p-not-2` | Frozen prime is (3>2). |
| `21.137-odd-finite-p-group` | Candidate will have order (3^{10}) if the action exists. |
| `21.137-odd-exponent-p2` | Must establish exponent exactly (9), including one element of order (9). |
| `21.137-odd-power-set-definition` | Must compute all (59049) element cubes, not generated powers. |
| `21.137-odd-power-set-subgroup` | Must compare the literal image with its generated subgroup. |
| `21.137-odd-P-abelian` | A counterexample requires two explicit noncommuting actual cubes. |

### Strategy portfolio under the Lead freeze

1. **Structured construction (selected):** canonical Heisenberg root action, exact lift, split coordinate law, symbolic cube image.
2. **Catalogue mode (forbidden this increment):** no alternate actions or small-group search.
3. **Theoretical mode:** if the canonical action/lift exists, use the square-zero order-three symplectic identity to reduce every cube to a central coordinate; this may yield an exact obstruction rather than a witness.
4. **Certificate plan:** explicit (4\times4) matrices, coordinate multiplication/inverse, closed cube formula, and—only if symbolic coverage is incomplete—a frozen all-element checker with histogram and literal-image-versus-generated-subgroup comparison.

## 2026-08-17T19:59:14Z — exact action/lift frozen; projected obstruction

Let V be F3^4 with ordered basis (e1,e2,f1,f2) and omega(e_i,f_j)=delta_ij. The canonical root matrices are

```text
A = [1 1 0 0]    B = [1 0 0 1]
    [0 1 0 0]        [0 1 1 0]
    [0 0 1 0]        [0 0 1 0]
    [0 0 2 1]        [0 0 0 1].
```

Both are symplectic of order three. Direct multiplication gives

```text
C=[A,B]=A^-1 B^-1 A B = [1 0 2 0]
                              [0 1 0 0]
                              [0 0 1 0]
                              [0 0 0 1],
```

with C^3=I, C nonidentity, and [A,C]=[B,C]=I. Thus the action image is genuinely nonabelian. If

```text
Q={(a,b,h):a,b,h in F3},
(a,b,h)(a',b',h')=(a+a',b+b',h+h'-b a'),
```

then M_(a,b,h)=A^a B^b C^h is a faithful homomorphism Q -> Sp4(3), explicitly

```text
M_(a,b,h) = [1 a ab-h  b]
            [0 1   b   0]
            [0 0   1   0]
            [0 0  -a   1].
```

The lift has no obstruction: for the reviewed kernel law
`(v,z)(w,t)=(v+w,z+t+2 omega(v,w)c)`, define
`alpha_(a,b,h)(v,z)=(M_(a,b,h)v,z)`. Symplecticity makes this an automorphism, and the matrix homomorphism makes alpha an action of Q on K.

More strongly, enumeration is unnecessary. For **any** split extension K semidirect Q with Q an exponent-three group and any action, q^3=1 implies that the induced M_q on K/Z(K) has M_q^3=I. Its similitude multiplier has cube one in F3*, hence equals one, so M_q lies in Sp4(3). The reviewed rank-four lemma gives N_q^2=0 for N_q=M_q-I. Therefore

```text
(kq)^3 mod Z(K) = (I+M_q+M_q^2) vbar = N_q^2 vbar = 0.
```

Every literal cube lies in the abelian group Z(K), whether or not the action has central shears or moves Z(K). Hence all actual cubes commute. This excludes the entire split/exponent-three-quotient family over the fixed kernel, not just the frozen seed. It does not reach nonsplit extensions.

For the frozen seed specifically, the action fixes Z(K). Writing v=(x1,x2,y1,y2) and N=M_(a,b,h)-I, exact collection gives

```text
(v,z;a,b,h)^3 = (0, 2 omega(v,Nv)c; 0),
omega(v,Nv) = y1 (a x2 + b y2 + (h-ab)y1).
```

Thus the complete literal image over all 3^10=59049 elements is exactly <c>: containment follows from the formula, and surjectivity follows already in the A-coset by y1=1, x2=0,1,2. It equals the subgroup it generates and is abelian. Taking q=A and v=e2+f1 gives cube 2c nonzero, so this order-3^10 group has exponent exactly nine. The canonical seed passes every admissibility row but does **not** violate the target conclusion.

No heavy computation was needed or started. The only command was a constant-size matrix relation check; its observed output was:

```text
A3 True B3 True C3 True
central True True
AB=BA*C True
subgroup-size 27
```

## 2026-08-17T20:02:27Z — active work stop and outcome

- Active interval: 2026-08-17T19:54:32Z--2026-08-17T20:02:27Z.
- Charge: **8 active minutes**. Cumulative scope time: **564 minutes**.
- Unused from this increment: **52 active minutes**, returned to Lead.
- Outcome: `PARTIAL_RESULT` for the bounded theorem that every split extension of the fixed kernel by any exponent-three quotient has pairwise commuting actual cubes.
- The canonical Heisenberg action exists and lifts, but its exact literal cube image is `<c>`, so it is not a counterexample.
- State: `awaiting_lead`. No nonsplit extension, alternate action, cocycle, or catalogue branch was opened.
