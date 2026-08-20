---
title: "Partial reduction — SU3(q) central-height family at 3"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
outcome: PARTIAL_RESULT
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/conjectured]
---

# Partial reduction — `SU_3(q)` central height at three

## Active target

For every finite `G`, every ordinary complex irreducible `chi`, and every
`x in G`, `chi(x)!=0` should imply the exact divisibility
`o(x)chi(1) | |G|`.

This note does not answer that target.  It derives the exact parameter gate for
one auxiliary family and identifies the generic block theorem still missing.

## Candidate partial result

Let `q` be a prime power with `3|(q+1)`, put `a=v_3(q+1)`,
`L=SU_3(q)`, and `Z=Z(L)=C3`.  A Sylow three-subgroup is

```text
P ~= (C_(3^a) x C_(3^a)) semidirect C3,
|P/Z|=3^(2a),   exp(P/Z)=3^a.
```

For a 3-block with defect group `D`, write `|D|=3^d`,
`exp(D/Z)=3^e`, and let an ordinary character have height `h`.  Then

```text
exp(D/Z) <= (|L:Z|/theta(1))_3
iff h <= d-1-e.                                      (*)
```

Thus the principal block requires exactly `h<=a`.  Abelian-defect blocks pass
`(*)` by Brauer height zero.  The only possible failures are therefore:

1. a principal-block character of height greater than `a`; or
2. a nonprincipal block with nonabelian defect and a character of height
   greater than `d-1-e`.

## Exact missing theorem

The following sufficient theorem is not supplied or derivable from the admitted
`q=5` evidence:

> For every `q>2` with `3|(q+1)`, all nonprincipal ordinary 3-blocks of
> `SU_3(q)` have abelian defect, and the maximum height in the principal
> 3-block is at most `v_3(q+1)`.

Any citation used for this must cover `SU_3(q)` itself, not only generic
`GU_3(q)` data: restriction/splitting of characters and blocks and disconnected
projective semisimple centralizers at the central prime three must be included.
Without that input, extrapolating the seven `q=5` blocks would invent generic
block data.  The assigned strategy therefore stops at this gate.

## Conditional bounded-family consequence

If that missing theorem is supplied, the reviewed Proposition 3.2 applies for
`q>2` only, retaining every hypothesis: `H` finite,
`[H,H]=L=SU_3(q)` quasi-simple, `Z(L)=Z(H)`, `chi in Irr(H)` faithful,
`h in H`, `chi(h)!=0`, and `H=<L,h>`.  Its conclusion is only

```text
o(hZ(H))_3 | (|H:Z(H)|/chi(1))_3.
```

The case `q=2` is excluded because `SU_3(2)` is not quasi-simple.  Even after
the missing theorem, this remains a prime-three order-mod-center family, never
the universal Kourovka conclusion.

## Constraint-and-conclusion matrix

| constraint id | role | use/result |
|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | fail for the active scope: only a conditional `SU_3(q)`-derived family |
| `20.115-G-finite` | admissibility | retained only for conditional finite `H` |
| `20.115-chi-complex-irreducible` | admissibility | retained, with Proposition 3.2's extra faithfulness hypothesis |
| `20.115-x-in-G` | admissibility | narrowed to the 3-part of the order of `hZ(H)` |
| `20.115-character-value-nonzero` | admissibility | retained exactly |
| `20.115-order-degree-divisibility` | target conclusion | not established; only the conditional prime-part statement above |

## What this does not establish

- It does not establish the missing generic block theorem.
- It does not prove any new unconditional `q`-family beyond the independently
  replicated `q=5` case.
- It does not remove any hypothesis of Proposition 3.2.
- It does not imply full element-order divisibility or the universal target.

## How this could be wrong

- The torus/Weyl model must use the correct finite `SU_3(q)` convention; the
  order computation and explicit norm calculation are included in the log for
  checking.
- A source might classify blocks only for `GU_3(q)` or only away from primes
  dividing the center; that would not fill the stated gap.
- The assertion about abelian-defect character heights uses Brauer height zero;
  Validator should insist on the standard theorem in the exact ordinary-block
  form.
- Proposition 3.2 could have an additional hypothesis omitted by the reviewed
  bridge; the conditional consequence intentionally repeats every hypothesis
  listed in that independently replicated note.

