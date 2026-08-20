---
title: "Frozen manifest — one complete nonsplit presentation after the lift gate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

# Frozen presentation row

The lift gate in `../lift-gate.md` passed. Freeze that exact `(TX,TY,TZ)`
and `(LX,LY,LZ)` row. No alternate lift, central correction, kernel, or quotient
is admitted in this run.

Use kernel generators `(e1,e2,f1,f2,c,s,t)` of order three, with `c,s,t`
central and only nontrivial basic commutators

```
[e1,f1]=c,   [e2,f2]=c,
```

where `[u,v]=u^-1 v^-1 u v`. This is the reviewed coordinate kernel
`3_+^(1+4) x C3^2`.

Adjoin `X,Y,Z` acting by left conjugation as follows:

```
X: e1->e1*s, e2->e1*e2*s, f1->f1*f2^2, f2->f2,
   c->c, s->c^2*s, t->s*t;
Y: e1->e1*s, e2->e2, f1->e2*f1, f2->e1*f2,
   c->c, s->c*s, t->s*t;
Z: e1->e1, e2->e2*s^2, f1->e1^2*f1*c^2, f2->f2*s,
   c->c, s->s, t->c*t.
```

These words are the exact coordinate-to-ordered-word conversion of the
certified automorphism triples. Freeze zero additional central coordinates on
the six quotient relators:

```
X^3 = f2,
Y^3 = e2,
Z^3 = 1,
[X,Y] Z^-1 = e1^2 f1^2 f2 c,
[X,Z] = e2^2 f2^2 c,
[Y,Z] = e2 f2 c.
```

The right sides have precisely the six inner labels computed at the lift gate.
The presentation is genuinely nonsplit if consistent: `X^3=f2` is a
noncentral cube, whereas every split extension over this kernel by an
exponent-three quotient has all cubes in `Z(K)` by the reviewed bounded theorem.

## Gates

1. Exact presentation consistency: the seven kernel generators must embed with
   kernel order `3^7`, the quotient by them must be `H_3(3)` of order 27, and
   the group must have order `3^10` (no relator-induced collapse).
2. Exact exponent: every element has order dividing nine and at least one has
   order nine.
3. Complete literal cube set: enumerate every one of the `3^10` elements, not
   only generators/cosets or the generated cube subgroup.
4. Compare the literal set to its subgroup closure exactly.
5. If closed, test every pair of literal cubes and exhibit two noncommuting
   actual cubes.

The frozen GAP check may compute a class-bounded 3-quotient only as a diagnostic;
such a quotient is not by itself proof that the fp presentation is finite or
that the kernel embeds. A target-facing result requires an exact pc group or an
independent coordinate/factor-system construction.

