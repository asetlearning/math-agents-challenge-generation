---
title: "Problem 20.115 cycle 18 — direct Suzuki character family"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
cycle: 18
direction: proof
strategy: SUZUKI-DIRECT-CHARACTER-FAMILY
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
---

# Cycle 18 log

## Active-time ledger

- Work start: `2026-08-18T10:19:07Z`; inherited detailed cumulative active time `07:03:51`.
- New-active-time cap: `00:45:00`; wall safety stop: `2026-08-18T11:19:07Z`.
- Work stop: `2026-08-18T10:30:28Z`; newly elapsed active time `00:11:21`;
  detailed cumulative active time `07:15:12`. The cap and safety stop were respected.

## Source and staleness gate

The configured Notebook PDF resolves and was inspected both as layout text and as
a rendered image of printed page 161. The source reads:

> Let chi be a complex irreducible character of a finite group G. If chi(x) is
> nonzero for some x in G, must the order o(x) of x divide |G|/chi(1)?

It then records the solvable case and the weaker fourth-power bound as context.
The displayed exponent is on the entire product `(o(x)chi(1))`, and the displayed
right side is `|G|^5`. Visual transcription check: `yes`.

The 2022 corpus row has `answered: false`, `has_editor_comment: false`, and
`has_later_comment: false`. The configured current Notebook prints 20.115
unstarred. The canonical scope has `blind_run.enabled: true` and
`open_web: false`, so the external search is recorded as
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
No solution-bearing historical 20.115 notes were consulted. The prior PSL(2,q)
candidate is not used.

### Clause matrix

| source clause | active? | use in this run |
|---|---:|---|
| nonzero ordinary irreducible value implies `o(x)chi(1) | |G|` | yes | audited for every simple `Sz(q)`, `q=2^(2m+1)>=8` |
| assertion known for solvable groups | no | not used |
| fourth-power universal bound | no | not used |

The six canonical constraint rows agree with the rendered source. The present
family theorem is partial because the universal quantifier over all finite groups
is not discharged. `active_scope_checked: yes`; `active_assignment_answered: no`.

## Strategy portfolio

1. **Theoretical / exact generic-table mode (selected).** Extract the generic
   ordinary Suzuki table, prove that its class and character parameter sets are
   complete, determine its exact support (including cyclotomic cancellation), and
   compare each support block with the factored group order.
2. **Catalogue mode (not selected).** Exact checks of `Sz(8)` and `Sz(32)` could
   detect a formula transcription error but could never establish the family.
3. **Structured mode.** Reconstruct the same support from the three cyclic maximal
   tori and the Suzuki 2-local classes. This is useful as a conceptual check, but
   the generic ordinary table already gives a shorter certificate.
4. **Certificate plan.** Validator can replay the hand factorization and compare
   the seven row/column family formulas with CTblLib's generic `Suzuki` record;
   no finite sampling and no heavy computation are needed.

Kill criterion: stop if any irreducible family has a potentially nonzero torus
cell whose torus factor is cancelled from `|S|/chi(1)`, or if a missing class/row
family prevents a complete support audit.

## Exact generic-table source

The ordinary table formulas were read directly from the installed GAP CTblLib
1.3.7 generic record `Suzuki` in `data/ctgeneri.tbl.gz` (decompressed lines
808--917). SHA-256 of the compressed data file:
`c73d3506b64277e5ebdca2dbfd22c0de6e7bf6a5afcc5b6d86d8d8a2cddc2313`.
The record cites R. Burkhardt, *Journal of Algebra* 59 (1979), and explicitly
states that its parameter sets correct the last two character/class ranges in
that paper. This run uses the record's corrected orbit parameters.

### Commands and observed outputs

- `pdftotext -f 160 -l 163 -layout "$KOUROVKA_PDF" -` printed the source
  statement reproduced above; a `pdftoppm` rendering of printed page 161 was
  visually inspected.
- Decompressing CTblLib's package-relative `data/ctgeneri.tbl.gz` and selecting
  lines 808--917 printed the seven class types, orders, corrected parameters,
  and seven ordinary row-family formulas transcribed below.
- `sha256sum` on that compressed package file returned
  `c73d3506b64277e5ebdca2dbfd22c0de6e7bf6a5afcc5b6d86d8d8a2cddc2313`.
- An optional symbolic sum-of-squares check using Python `sympy` stopped with
  `ModuleNotFoundError: No module named 'sympy'`. No result relies on it; the
  displayed polynomial identity was instead reduced by hand. No install or
  substitute general-purpose algebra system was attempted.

Put

`q=2^(2m+1)`, `m>=1`, `r=2^(m+1)`, so `r^2=2q`, and

`a=q-1`, `b=q-r+1`, `c=q+r+1`.

Then

`|Sz(q)|=q^2 a b c`, because `bc=q^2+1`.

The three odd integers `a,b,c` are pairwise coprime. For example, an odd common
divisor of `a` and `b` gives `q=1` and `r=2` modulo that divisor, hence
`q=r^2/2=2`, forcing the divisor to be one; the other pairs are analogous, and
`gcd(b,c)` divides the power of two `2r`.

## Complete conjugacy-class inventory

Columns are ordered as follows.

| type | parameter count | centralizer | exact order |
|---|---:|---:|---:|
| `1` | 1 | `|S|` | 1 |
| `A0(l)` | `(q-2)/2` | `a` | `a/gcd(a,l)` |
| `A1(l)` | `(q+r)/4` | `c` | `c/gcd(c,l)` |
| `A2(l)` | `(q-r)/4` | `b` | `b/gcd(b,l)` |
| `u2` | 1 | `q^2` | 2 |
| `u4+` | 1 | `2q` | 4 |
| `u4-` | 1 | `2q` | 4 |

For `A0`, nonzero residues modulo `a` are taken modulo inversion. For `A1`
and `A2`, nonzero residues modulo `c` and `b` are taken modulo multiplication
by `q`; this action contains inversion because `q^2=-1` modulo both `b` and
`c`. Its nonzero orbits have size four. Indeed, for `N=b` or `c`, both
`gcd(N,q-1)` and `gcd(N,q+1)` are one, so no nonzero residue is fixed by `q`
or `-q`; oddness excludes a fixed point of inversion. Thus the displayed
counts are exact. They sum to `q+3`.

## Complete irreducible-character inventory and values

Let `zeta_n=exp(2 pi i/n)`. The row families, with the same column order, are:

| row family | count; degree | `A0(l)` | `A1(l)` | `A2(l)` | `u2` | `u4+` | `u4-` |
|---|---|---|---|---|---:|---:|---:|
| `1_S` | `1; 1` | 1 | 1 | 1 | 1 | 1 | 1 |
| `St` | `1; q^2` | 1 | -1 | -1 | 0 | 0 | 0 |
| `W+` | `1; r a/2` | 0 | 1 | -1 | `-r/2` | `ri/2` | `-ri/2` |
| `W-` | `1; r a/2` | 0 | 1 | -1 | `-r/2` | `-ri/2` | `ri/2` |
| `X_i` | `(q-2)/2; bc=q^2+1` | `zeta_a^(il)+zeta_a^(-il)` | 0 | 0 | 1 | 1 | 1 |
| `Y_j` | `(q+r)/4; ab` | 0 | `-(z+z^-1+z^q+z^-q)`, `z=zeta_c^(jl)` | 0 | `r-1` | -1 | -1 |
| `Z_k` | `(q-r)/4; ac` | 0 | 0 | `-(z+z^-1+z^q+z^-q)`, `z=zeta_b^(kl)` | `-r-1` | -1 | -1 |

At the identity each row has the displayed degree. Character parameters use
the same inversion/four-cycle orbit sets as the corresponding torus. There are
again `q+3` rows. As a consistency check, their degree squares give

`1 + q^4 + 2(ra/2)^2 + ((q-2)/2)(q^2+1)^2`

`+ ((q+r)/4)(ab)^2 + ((q-r)/4)(ac)^2 = q^2abc`

after `r^2=2q` and `bc=q^2+1`.

## Cyclotomic cancellation audit

Every displayed two-term or four-term torus value is nonzero; hence the zero
pattern in the table is exact, not merely a support upper bound.

- A two-term sum of roots of unity can vanish only when the two roots are
  negatives. This is impossible for roots of odd order `a`.
- If four unit complex numbers `z1,...,z4` sum to zero, then for
  `P(T)=product(T-zi)` both the cubic coefficient and the linear coefficient
  vanish: the latter because
  `sum zi^-1 = conjugate(sum zi)=0`. Thus `P` is even and its roots occur in
  opposite pairs. Four roots of odd order cannot contain an opposite pair.
  This applies, with multiplicity allowed, to the `Y_j` and `Z_k` sums because
  `b,c` are odd.

Therefore no special composite parameter or nonprimitive class order creates
an unrecorded zero or a new support cell.

## Primewise divisibility audit

For each row, compare the exact nonzero support with `|S|/chi(1)`:

| row | quotient `|S|/chi(1)` | exact nonidentity support | reason every supported order divides quotient |
|---|---:|---|---|
| `1_S` | `q^2abc` | all types | torus orders divide `a,b,c`; `4|q^2` |
| `St` | `abc` | `A0,A1,A2` | orders divide `a,b,c` respectively |
| `W+`,`W-` | `qrbc` | `A1,A2,u2,u4+,u4-` | odd orders divide `c` or `b`; `4|qr` for `m>=1` |
| `X_i` | `q^2a` | `A0,u2,u4+,u4-` | odd order divides `a`; `4|q^2` |
| `Y_j` | `q^2c` | `A1,u2,u4+,u4-` | odd order divides `c`; `4|q^2` |
| `Z_k` | `q^2b` | `A2,u2,u4+,u4-` | odd order divides `b`; `4|q^2` |

Here `|S|/(ra/2)=qrbc` follows from `r^2=2q`. Identity has order one.
Thus the exact source implication holds on every ordinary irreducible row and
every class of each simple Suzuki group in the assigned family.

## Outcome

`PARTIAL_RESULT`: candidate exact infinite-family theorem for every simple
`Sz(2^(2m+1))`, `m>=1`. The named strategy did not meet its kill criterion.
The universal all-finite-groups statement remains open, so
`active_assignment_answered: no`. Stop in `awaiting_lead` after routing the
candidate family theorem to a fresh Validator.
