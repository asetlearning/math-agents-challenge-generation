---
title: "Kourovka 21.137 revision 2 — ROOT-FIBRE-MARKS log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: ROOT-FIBRE-MARKS
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/burnside-marks
  - project/kourovka
  - status/draft
---

# Working log

## 2026-08-17T13:26:04Z — work start

- Scope cumulative active time on entry: 426 minutes.
- Run-local active time on entry: 0 minutes.
- Budget: at most 45 active minutes; strategy kill at 30 minutes if multiplication
  in `P` never enters or a complete feasible integral relaxation is explicit.
- Scope audit in the canonical revision-2 record: required and `passed` by
  Validator.
- Exact target: odd prime `p`, finite same-`p` group `G`, exponent exactly `p^2`,
  complete actual value set `P={x^p:x in G}` itself a subgroup; prove `P` abelian.
- Excluded: `p=2`, exponent 8, wreath material, web/history, heavy computation,
  and unreviewed construction artifacts.

## Source and staleness gate

The configured source PDF resolves. I inspected rendered page 184 and compared the
whole displayed item 21.137 visually, including `p != 2`, exponent `p^2`, and the
separate exponent-8 clause. Correct active transcription:

> For `p != 2`, if the `p`-th powers in a `p`-group of exponent `p^2` form a
> subgroup, must that subgroup be abelian?

`source_transcription_checked: yes`  
`active_scope_checked: yes`  
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

Clause matrix:

| source clause | active? | treatment |
|---|---:|---|
| general powerfulness question | no | context only |
| odd-prime, exponent-`p^2`, abelianity question | yes | exact target |
| `2`-group, exponent-8 question | no | excluded |

The seven canonical constraint rows agree with the rendered source. In particular,
the value set is the set of all actual powers, not merely the verbal subgroup it
generates.

## Strategy portfolio

1. **Theoretical / assigned route:** freeze every fixed-point fibre mark for the
   conjugation-equivariant power map and impose all mark-table rows.
2. **Structured failure certificate:** construct a nonabelian class-two
   exponent-`p` label group and an explicit formal equivariant surjection whose
   entire mark vector is feasible. This is the cheapest decisive test of whether
   the representation retains multiplication across fibres.
3. **Catalogue / compute:** not appropriate; the assignment forbids heavy compute
   and a bounded group census would not test the prime-uniform mark relaxation.
4. **Certificate plan:** give closed formulas for `m_H(a)` for every subgroup `H`,
   then give explicit orbit decompositions so Validator need not trust a solver or
   a partial mark table.

## 2026-08-17T13:32:00Z — frozen rows

For `X_a={x:x^p=a}` and `K_a=C_G(a)`, the rows forced by treating the power map as
a finite conjugation-equivariant map are:

- support `m_H(a)=0` unless `H <= K_a`;
- conjugacy `m_{H^g}(a^g)=m_H(a)`;
- partition `sum_{a in C_P(H)} m_H(a)=|C_G(H)|`;
- root-centrality `m_H(a)=m_{<H,a>}(a)` whenever `H <= K_a`;
- the complete Burnside mark-table equations for the `K_a`-set `X_a`;
- nonnegative Möbius exact-stabilizer counts and their normalizer divisibilities;
- `m_1(a)>0` for every actual label;
- `P <= X_1`, equality of counts on prime-to-`p` scalar powers, and divisibility
  by `p` of every nonidentity fibre count.

These are recorded in closed form in `findings.md`.

## 2026-08-17T13:36:00Z — feasible integral relaxation

Let `P=H_p` be the order-`p^3` Heisenberg group, with
`P'=Z(P)=<c>` of order `p`. Form a central product with a central element `t` of
order `p^2` satisfying `t^p=c`, and adjoin an elementary abelian central factor
`B=C_p^s`, `s>=1`. Every element of the resulting exponent-`p^2` group `Gamma`
has a unique form `t^i b u`, `0<=i<p`, `b in B`, `u in P`, and `Gamma/P` has
exponent `p`.

The explicit formal label map

```
f(t^i b u) = 1       if i=0,
             u       if i!=0 and u!=1,
             c^i     if i!=0 and u=1
```

is surjective, conjugation-equivariant, and satisfies `[x,f(x)]=1`. Its identity
fibre is even the true set of elements of `Gamma` whose `p`-th power is `1`.
Writing `q_H=|C_P(H)|`, all its marks are

```
m_H(1)                 = p^s q_H,
m_H(a)                 = p^(s+1)                  (1!=a in Z(P)),
m_H(a)                 = (p-1)p^s                 (a notin Z(P), a in C_P(H)),
m_H(a)                 = 0                        (a notin C_P(H)).
```

The fibre decompositions show directly that every Burnside and Möbius row is
integral. Thus the assigned hard kill is met without computation.

## 2026-08-17T13:41:00Z — self-check and stop

- Active scope and revision: `21.137/odd-prime-exponent-p2`, revision 2.
- Hypothesis tested: only the finite conjugation-equivariant/fixed-point-mark
  consequences of the actual power map, plus the elementary power-count rows
  listed above.
- Evidence: a prime-uniform closed-form mark vector for all `H` and `a`, with an
  explicit finite `Gamma`-set realization.
- Bottleneck: the rows never encode the relation `f(x)=x^p` on mixed elements, or
  equivalently the root-action/carry relation connecting multiplication in `P`
  to a particular root fibre.
- Admissibility: this is **not** a candidate group. It deliberately fails
  `21.137-odd-power-set-definition`; the true power set of `Gamma` is `<c>`, while
  the formal label group is nonabelian `P`.
- Outcome: `STRATEGY_EXHAUSTED` for `ROOT-FIBRE-MARKS` only. The unrestricted
  target remains unanswered.
- Run-local active time charged: 15 minutes. Scope cumulative time on stop: 441
  minutes. The solver enters `awaiting_lead`.

