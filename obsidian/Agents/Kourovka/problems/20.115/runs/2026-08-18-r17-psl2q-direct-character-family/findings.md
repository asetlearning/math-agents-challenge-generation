---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# Candidate family theorem: all nonabelian simple `PSL(2,q)`

## Active target and exact status

The canonical target quantifies over **all** finite groups.  The result below is
only the assigned infinite-family partial:

> If \(q\) is a prime power and \(L=\operatorname{PSL}_2(q)\) is nonabelian
> simple, then for every ordinary \(\chi\in\operatorname{Irr}(L)\) and every
> \(x\in L\), \(\chi(x)\ne0\) implies
> \(o(x)\chi(1)\mid |L|\).

This does **not** answer the universal Kourovka question.

## Constraint-and-conclusion matrix

| constraint id | role | proof use / candidate value | evidence | result |
|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | Notebook target is all finite \(G\); this note treats exactly \(G=\operatorname{PSL}_2(q)\) simple. | theorem and inventories below | **partial only** |
| `20.115-G-finite` | admissibility | \(L\) has order \(q(q-1)(q+1)/d\), \(d=(2,q-1)\). | class inventory below | pass in family |
| `20.115-chi-complex-irreducible` | admissibility | Every row in the three generic tables below is an ordinary complex irreducible, and all rows are listed. | character inventories and multiplicity checks | pass in family |
| `20.115-x-in-G` | admissibility | Identity, unipotent, split semisimple, and nonsplit semisimple classes are exhaustive; exact orders are listed. | class inventories | pass in family |
| `20.115-character-value-nonzero` | admissibility | Identically zero cells are marked; accidental root-sum cancellation is treated by a support-superset argument and an exact order-four criterion. | cancellation audit | pass in family |
| `20.115-order-degree-divisibility` | target conclusion | For every cell that can be nonzero, the exact integer quotient \(|L|/(o(x)\chi(1))\) is displayed. | quotient tables | established in family |

## Exact generic table theorem used

Let \(q=p^f\), \(d=(2,q-1)\), and
\[
  |L|=\frac{q(q-1)(q+1)}d.
\]
Write \(\zeta_N=e^{2\pi i/N}\), and for odd \(q\) put
\[
 B_q=\frac12\sum_{j=1}^{q-1}\zeta_q^{j^2}.
\]
The following is the full ordinary table, stated with parameter ranges.  It is
the exact specialization theorem encoded by GAP 4.12.1 / CTblLib 1.3.7 in the
package data file `data/ctgeneri.tbl.gz` (SHA-256
`c73d3506b64277e5ebdca2dbfd22c0de6e7bf6a5afcc5b6d86d8d8a2cddc2313`),
records `SL2even`, `PSL2odd`, and `PSL2even`.  The formulas are reproduced here
so the result does not rest on an opaque table identifier.

The element-type list is structurally exhaustive: a lift to \(\mathrm{SL}_2(q)\)
has a quadratic characteristic polynomial.  A repeated root gives a scalar
(identity in the projective quotient) or a nontrivial unipotent; two roots in
\(\mathbb F_q\) give a split semisimple element; conjugate roots in
\(\mathbb F_{q^2}\setminus\mathbb F_q\) give a nonsplit semisimple element.
Quotienting the two tori by the scalar center gives torus orders
\((q-1)/d\) and \((q+1)/d\), which explains every exact order below.

### Characteristic two

Here \(d=1\).  The classes and their exact orders are

| class | parameter | exact order |
|---|---:|---:|
| \(1\) | — | \(1\) |
| unipotent \(u\) | — | \(2\) |
| split \(a_k\) | \(1\le k\le(q-2)/2\) | \((q-1)/(q-1,k)\) |
| nonsplit \(b_k\) | \(1\le k\le q/2\) | \((q+1)/(q+1,k)\) |

All irreducibles and values are

| character (parameter) | degree | \(u\) | \(a_k\) | \(b_k\) |
|---|---:|---:|---:|---:|
| \(1_L\) | \(1\) | \(1\) | \(1\) | \(1\) |
| \(A_i\), \(1\le i\le q/2\) | \(q-1\) | \(-1\) | \(0\) | \(-\zeta_{q+1}^{ki}-\zeta_{q+1}^{-ki}\) |
| \(\mathrm{St}\) | \(q\) | \(0\) | \(1\) | \(-1\) |
| \(C_i\), \(1\le i\le(q-2)/2\) | \(q+1\) | \(1\) | \(\zeta_{q-1}^{ki}+\zeta_{q-1}^{-ki}\) | \(0\) |

Every row takes its degree at \(1\).  There are \(q+1\) rows/classes, and
\[
1+\frac q2(q-1)^2+q^2+\frac{q-2}2(q+1)^2=q(q^2-1)=|L|,
\]
so no degree family is omitted.

### Odd \(q\equiv3\pmod4\)

Put \(s=(q-1)/2\), \(n=(q+1)/2\).  The classes are

| class | parameter | exact order |
|---|---:|---:|
| \(1\) | — | \(1\) |
| \(u_+,u_-\) | — | \(p\) |
| split \(a_k\) | \(1\le k\le(q-3)/4\) | \(s/(s,k)\) |
| nonsplit \(b_k\) | \(1\le k\le(q-3)/4\) | \(n/(n,k)\) |
| nonsplit involution \(b_{n/2}\) | \(k=n/2=(q+1)/4\) | \(2\) |

For \(r=1,\ldots,(q-3)/4\), put \(i=2r\).  The complete rows are

| character | degree | \(u_+\) | \(u_-\) | \(a_k\) | \(b_k\) | \(b_{n/2}\) |
|---|---:|---:|---:|---:|---:|---:|
| \(1_L\) | \(1\) | \(1\) | \(1\) | \(1\) | \(1\) | \(1\) |
| \(A_i\) | \(q-1\) | \(-1\) | \(-1\) | \(0\) | \(-\zeta_{q+1}^{ki}-\zeta_{q+1}^{-ki}\) | \(-\zeta_4^i-\zeta_4^{-i}\) |
| \(\mathrm{St}\) | \(q\) | \(0\) | \(0\) | \(1\) | \(-1\) | \(-1\) |
| \(C_i\) | \(q+1\) | \(1\) | \(1\) | \(\zeta_{q-1}^{ki}+\zeta_{q-1}^{-ki}\) | \(0\) | \(0\) |
| \(E_+\) | \(s\) | \(B_q\) | \(-1-B_q\) | \(0\) | \((-1)^{k+1}\) | \((-1)^{n/2+1}\) |
| \(E_-\) | \(s\) | \(-1-B_q\) | \(B_q\) | \(0\) | \((-1)^{k+1}\) | \((-1)^{n/2+1}\) |

The \(A_i\) and \(C_i\) rows each occur \((q-3)/4\) times; the two
exceptional rows occur once each.  Thus both the number of rows and classes is
\((q+5)/2\).  Their displayed degree squares satisfy
\[
 1+\frac{q-3}{4}(q-1)^2+q^2+\frac{q-3}{4}(q+1)^2
   +2\left(\frac{q-1}{2}\right)^2=\frac{q(q^2-1)}2=|L|.
\]

### Odd \(q\equiv1\pmod4\)

Again put \(s=(q-1)/2\), \(n=(q+1)/2\).  The classes are

| class | parameter | exact order |
|---|---:|---:|
| \(1\) | — | \(1\) |
| \(u_+,u_-\) | — | \(p\) |
| split \(a_k\) | \(1\le k\le(q-5)/4\) | \(s/(s,k)\) |
| split involution \(a_{s/2}\) | \(k=s/2=(q-1)/4\) | \(2\) |
| nonsplit \(b_k\) | \(1\le k\le(q-1)/4\) | \(n/(n,k)\) |

For \(A_i\), take \(i=2r\) with \(1\le r\le(q-1)/4\); for \(C_i\),
take \(i=2r\) with \(1\le r\le(q-5)/4\).  The complete rows are

| character | degree | \(u_+\) | \(u_-\) | \(a_k\) | \(a_{s/2}\) | \(b_k\) |
|---|---:|---:|---:|---:|---:|---:|
| \(1_L\) | \(1\) | \(1\) | \(1\) | \(1\) | \(1\) | \(1\) |
| \(A_i\) | \(q-1\) | \(-1\) | \(-1\) | \(0\) | \(0\) | \(-\zeta_{q+1}^{ki}-\zeta_{q+1}^{-ki}\) |
| \(\mathrm{St}\) | \(q\) | \(0\) | \(0\) | \(1\) | \(1\) | \(-1\) |
| \(C_i\) | \(q+1\) | \(1\) | \(1\) | \(\zeta_{q-1}^{ki}+\zeta_{q-1}^{-ki}\) | \(\zeta_4^i+\zeta_4^{-i}\) | \(0\) |
| \(E_+\) | \(n\) | \(1+B_q\) | \(-B_q\) | \((-1)^k\) | \((-1)^{s/2}\) | \(0\) |
| \(E_-\) | \(n\) | \(-B_q\) | \(1+B_q\) | \((-1)^k\) | \((-1)^{s/2}\) | \(0\) |

There are \((q-1)/4\) rows \(A_i\), \((q-5)/4\) rows \(C_i\), and
two exceptional rows, hence \((q+5)/2\) rows/classes.  Again their degree
squares satisfy
\[
 1+\frac{q-1}{4}(q-1)^2+q^2+\frac{q-5}{4}(q+1)^2
   +2\left(\frac{q+1}{2}\right)^2=\frac{q(q^2-1)}2=|L|.
\]

## Cancellation audit

A root sum \(\zeta_N^a+\zeta_N^{-a}\) is zero exactly when
\(\zeta_N^a\) has order four, equivalently
\[
  \frac{N}{(N,a)}=4.
\]
Thus the generic formulas above are not being treated as automatically nonzero.
In characteristic two, \(q-1\) and \(q+1\) are odd, so these sums never vanish.
For odd \(q\), the criterion detects all accidental cancellations (for example,
the degree-six row of \(\operatorname{PSL}_2(7)\) vanishes on its order-four
class, and the degree-ten row of \(\operatorname{PSL}_2(9)\) does likewise).

The involution values \(\pm(\zeta_4^i+\zeta_4^{-i})\) have even \(i\), hence
are \(\pm2\), never zero.  Also \(G_q=1+2B_q=\sum_{j=0}^{q-1}\zeta_q^{j^2}\)
is the quadratic Gauss sum and has absolute value \(\sqrt q\).  For the relevant
odd simple parameters \(q\ge5\), \(G_q\ne\pm1\), so every displayed
exceptional unipotent value \(B_q,-1-B_q,1+B_q,-B_q\) is nonzero.

More importantly, the divisibility audit below is a **support-superset audit**:
it proves the required integer quotient for every cell not identically zero in
the generic table, before asking whether its root sum cancels.  An accidental
cancellation can therefore only remove a pair; it cannot hide an unchecked
nonzero pair.

## Exact divisibility audit — characteristic two

Put \(S=q-1\), \(N=q+1\), so \(|L|=qSN\).  The identity-cell quotients for
degrees \(1,S,q,N\) are respectively \(|L|,qN,SN,qS\), all integers.
For nonidentity types the following table lists every degree that can have a
nonzero value (apart from degree one, which follows from Lagrange) and the exact
quotient.  Here \(m=o(x)\).

| type | order condition | possible nontrivial degree | \(|L|/(m\chi(1))\) |
|---|---|---:|---:|
| unipotent | \(m=2\) | \(q-1=S\) | \((q/2)N\) |
| unipotent | \(m=2\) | \(q+1=N\) | \((q/2)S\) |
| split | \(m\mid S\) | \(q\) | \((S/m)N\) |
| split | \(m\mid S\) | \(q+1=N\) | \(q(S/m)\) |
| nonsplit | \(m\mid N\) | \(q\) | \(S(N/m)\) |
| nonsplit | \(m\mid N\) | \(q-1=S\) | \(q(N/m)\) |

Since \(q=2^f\), \(q/2\in\mathbb Z\); every quotient is integral.

## Exact divisibility audit — odd characteristic

Now \(d=2\), \(|L|=q(q-1)(q+1)/2=q\,s(q+1)=q(q-1)n\).
The identity-cell quotients for degrees \(1,q-1,q,q+1,s,n\) (using only the
degree that exists in the relevant congruence case) are
\[
 |L|,\quad qn,\quad s(q+1),\quad qs,\quad q(q+1),\quad q(q-1),
\]
respectively.

For a unipotent element \(m=p\), every possible nonzero nontrivial degree has
the following exact quotient:

| degree | congruence case | \(|L|/(p\chi(1))\) |
|---:|---|---:|
| \(q-1\) | both | \((q/p)n\) |
| \(q+1\) | both | \((q/p)s\) |
| \(s=(q-1)/2\) | \(q\equiv3\pmod4\) | \((q/p)(q+1)\) |
| \(n=(q+1)/2\) | \(q\equiv1\pmod4\) | \((q/p)(q-1)\) |

The Steinberg value is zero on unipotent classes.  Since \(q=p^f\), all four
displayed quotients are integers.

For a split semisimple element, \(m\mid s\).  The possible nonzero nontrivial
degrees and quotients are

| degree | congruence case | \(|L|/(m\chi(1))\) |
|---:|---|---:|
| \(q\) | both | \((s/m)(q+1)\) |
| \(q+1\) | both | \(q(s/m)\) |
| \(n=(q+1)/2\) | \(q\equiv1\pmod4\) | \(2q(s/m)\) |

The last line includes the two exceptional characters; when
\(q\equiv3\pmod4\) their split values are zero.  The split involution for
\(q\equiv1\pmod4\) is included because its exact order \(2\) divides \(s\).

For a nonsplit semisimple element, \(m\mid n\).  The possible nonzero
nontrivial degrees and quotients are

| degree | congruence case | \(|L|/(m\chi(1))\) |
|---:|---|---:|
| \(q\) | both | \((q-1)(n/m)\) |
| \(q-1\) | both | \(q(n/m)\) |
| \(s=(q-1)/2\) | \(q\equiv3\pmod4\) | \(2q(n/m)\) |

The last line includes the two exceptional characters; when
\(q\equiv1\pmod4\) their nonsplit values are zero.  The nonsplit involution for
\(q\equiv3\pmod4\) is included because its exact order \(2\) divides \(n\).

Each displayed quotient is an integer.  Equivalently, for every prime \(\ell\),
its nonnegative \(\ell\)-valuation proves
\(v_\ell(o(x))+v_\ell(\chi(1))\le v_\ell(|L|)\).  This is the requested
primewise check; the factor \(d=(2,q-1)\) is not suppressed—its value is exactly
\(1\) in characteristic two and \(2\) in odd characteristic throughout the
two audits.

## Small simple parameters

The simplicity range is \(q\ge4\) (the nonsimple \(q=2,3\) are excluded).
The boundary specializations require no extra rows:

| \(q\) | identification | degrees from the displayed inventory |
|---:|---|---|
| 4 | \(\operatorname{PSL}_2(4)\cong A_5\) | \(1,3,3,4,5\) |
| 5 | \(\operatorname{PSL}_2(5)\cong A_5\) | \(1,3,3,4,5\); the \(q+1\) family is empty |
| 7 | simple | \(1,3,3,6,7,8\); the order-four root-sum cancellation is explicitly excluded |
| 8 | simple | \(1,7,7,7,7,8,9,9,9\) |
| 9 | \(\operatorname{PSL}_2(9)\cong A_6\) | \(1,5,5,8,8,9,10\); the order-four root-sum cancellation is explicitly excluded |

All quotient formulas above remain integral at these endpoints.  The empty
\(C_i\)-range at \(q=5\) is genuinely empty and creates no missing character.

## What this does not establish

- It does not prove the canonical statement for arbitrary finite groups.
- It does not transfer the family theorem to automorphism groups, central covers,
  or groups having a `PSL(2,q)` section.
- It uses the stated exact generic ordinary-table theorem.  Validator should
  independently reconstruct that theorem (or specialize the three formulas and
  check their generic derivation); the degree-square and class counts alone do not
  prove irreducibility or the value formulas.
- No prior Clifford/block lemma and no bounded character-table screen is used as a
  premise.

## How this could be wrong

1. The generic-table source might have a parameter convention different from the
   reproduced one; this should be checked directly against the three named records.
2. A semisimple quotient class order might have lost the central factor two; the
   explicit orders \(s/(s,k)\) and \(n/(n,k)\) are the critical audit point.
3. One exceptional row or endpoint parameter range could have been transcribed
   incorrectly; \(q=4,5,7,9\) are good independent boundary tests.
4. The quadratic Gauss-sum nonvanishing paragraph is supplementary: even if its
   normalization were wrong, the support-superset quotient proof remains valid.
