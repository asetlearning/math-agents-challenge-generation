---
title: "Kourovka 21.137 — O310 equivariant-label structural gate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
direction: counterexample
strategy: O310-EQUIVARIANT-LABEL
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

# O310-EQUIVARIANT-LABEL structural gate

## Active-time ledger

- `2026-08-17T13:58:50Z` — research start; scope cumulative active time `441m`; this gate may charge at most `19m`.
- `2026-08-17T14:06:08Z` — early hard kill and packaging stop; charge `8m` (rounded upward), scope cumulative active time `449m`; state `awaiting_lead`.

## Scope lock

- Prime is fixed to `p=3`, so it satisfies the active odd-prime row.
- Any eventual object must be a finite `3`-group of exact exponent `9`.
- `P` always denotes the complete actual cube-value set `{g^3:g in G}` itself, assumed to be a subgroup; generation by cubes is insufficient.
- Counterexample target is `P' != 1`.
- This gate constructs no group and opens no factor system, cocycle, descendant, catalogue, or heavy computation.

## Evidence boundary

Used only the canonical revision-2 scope, the current Lead decision, the reviewed conditional minimum-counterexample/equality deductions in `verification/2026-08-17T122251Z-min9-action-family-empty.md`, and the MathExpert strategy record named by Lead. No excluded history, web, computation, or stopped construction family was used.

## Structural derivation

Write `|P|=3^m` and `|R|=3^n`. The inherited rows give `m>=5` and

`n >= m-floor((m-1)/3)`.

At `m+n=10`, `m=5,n=5` is forced; `m>=6` gives total logarithmic order at least `11`. The inherited class-two, exponent-three, `P'=C3`, and `dim Z(P)>=3` rows then force

`P ~= H_3(3) x C3^2`.

Also `R=G/P` has order `3^5` and exponent `3`. Put `d=dim R/R'`; since `Phi(R)=R'`, `|R'|=3^(5-d)`. The complete resulting list is:

| name | `d` | `R'` | alternating commutator data |
|---|---:|---:|---|
| `A5` | 5 | `1` | `R=C3^5` |
| `H32` | 4 | `C3` | rank-two form; `H_3(3) x C3^2` |
| `E5` | 4 | `C3` | rank-four form; extraspecial exponent-three group of order `3^5` |
| `K32` | 3 | `C3^2` | unique surjection `Lambda^2(F3^3)->F3^2` up to bases |

The cases `d<=2` are impossible because a two-generated exponent-three group has order at most `27`. For `d=4`, nilpotence makes `R'` central and alternating forms to a line have ranks two or four. For `d=3`, a class-three case is impossible: a nonzero weight-three symbol `[[x,y],z]` makes `[x,y]`, `[x,z]`, and `[y,z]` independent modulo `gamma_3` (bracket a putative relation successively with `z,y,x`; repeated-variable weight-three brackets vanish in two-generated exponent-three subgroups). It would give at least three dimensions in `gamma_2/gamma_3` plus one in `gamma_3/gamma_4`, contradicting `|R'|=3^2`. Thus `R` is class two, and `GL_3(3)` is transitive on the one-dimensional kernels in `Lambda^2(F3^3)`, giving the unique `K32` type.

All four types admit one exact coordinate template. Let `V=F3^d`, `W=F3^e`, and use the alternating map `beta:Lambda^2 V->W` given by

- `A5`: `(d,e)=(5,0)`;
- `H32`: `(4,1)`, `beta(e1,e2)=z1`;
- `E5`: `(4,1)`, `beta(e1,e2)=beta(e3,e4)=z1`;
- `K32`: `(3,2)`, `beta(e1,e2)=z1`, `beta(e1,e3)=z2`;

with omitted basic values zero. Then

`(v,z)(v',z')=(v+v', z+z'+(1/2)beta(v,v'))`

is an exact `243`-element model, and `[(v,z),(v',z')]=(0,beta(v,v'))`. It supplies the complete Cayley and quotient-conjugacy relations without a catalogue.

## Exact homomorphism-row schema

The reviewed block model gives a Sylow `3`-subgroup `S<=Out(P)` of order `3^8`; every outer-action image is simultaneously conjugate into `S`. For one of the four rows above, a homomorphism `rho:R->S` is exactly a tuple

`(a_1,...,a_d,c_1,...,c_e)`

such that every entry has cube one, the `c_j` commute with all entries, and

`[a_i,a_j]=product_k c_k^(beta_ij,k)`.

Conversely these relators define a unique homomorphism. A map-complete equivariant-label row must retain, not merely infer from the abstract image subgroup:

1. all `243` values `rho(r)` in the canonical coordinate model;
2. `U=rho(R)`, the exact kernel, and `k=|ker rho|=243/|U|`;
3. the element-indexed multiplication/conjugacy table, equivalently the commutator multiplicities induced by `beta` on every pair of map fibres;
4. for every `r`, all nine inner-action lifts above `rho(r)^(-1)`, each occurring for `|Z(P)|=27` actual lifts in the quotient coset, together with its nonzero-label and central-supply data;
5. the exact equivariance rows `L(s^-1 r s)=rho(s)^(-1)L(r)` and the eight noncentral-label demands of size `27`.

## Hard-kill obstruction

The pair list is short and complete under the reviewed premises, but the required map manifest is not. The exact raw tuple cover has size at most `|S|^5=3^40`, and completeness requires a new orbit classification under simultaneous `Out(P)` conjugacy and `Aut(R)` precomposition. No reviewed theorem or supplied record gives that orbit reduction. The previous image-subgroup census cannot be reused as a map manifest: it retained image subgroups and a kernel size, while this strategy expressly distinguishes homomorphisms through the `243` quotient-element values and their relation/conjugacy multiplicities. Treating one image row as one map would violate the assignment.

Therefore the 19-minute structural gate cannot produce a short, proved-complete `(P,R,rho)` row list. No computation, factor system, cocycle, descendant, or extension work is opened. This exhausts only `O310-EQUIVARIANT-LABEL` at its mandated precomputation gate; the exact scope remains unanswered and the session enters `awaiting_lead`.
