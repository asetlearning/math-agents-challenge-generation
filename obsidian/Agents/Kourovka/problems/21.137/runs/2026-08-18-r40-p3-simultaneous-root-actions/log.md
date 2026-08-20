---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/draft
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy: P3-SIMULTANEOUS-ROOT-ACTIONS
cycle: 28
---

# Cycle 28 log — simultaneous root actions at p=3

## Active-time ledger

- 2026-08-18T06:25:44Z — work start at official cumulative minute 824; cap 45 new active minutes.

## 2026-08-18T06:34:32Z — source and exact-scope gate

Read the common protocol, problem-agent protocol, canonical revision-2 scope,
current roster entry, and the binding Lead decision.  This fresh run does not use
the historical problem log, findings, verification notes, scratch artifacts, or
solution-bearing external material.

Resolved the configured source PDF through `paths.env`.  Command:

```text
source _meta/agents/Kourovka/paths.env
pdftotext -f 184 -l 184 -layout "$KOUROVKA_PDF" -
pdftoppm -f 184 -l 184 -png -r 180 "$KOUROVKA_PDF" /tmp/kourovka21137-page
```

I visually inspected the rendered page, not only the text extraction.
Correct source transcription of the assigned clause:

> For p != 2, if the p-th powers in a p-group of exponent p^2 form a
> subgroup, must that subgroup be abelian?

`source_transcription_checked: yes`.  The statement has no source answer marker
or later comment at 21.137 on the rendered 2026 issue page.  The configured local
corpus is the issue-20 corpus and has no issue-21 JSONL row to audit; the canonical
scope's independently audited source record supplies the seven exact rows.
Because this is a discovery-blind continuation, `external_staleness_check:
deferred_to_lead_or_human_for_discovery_blind_run`.

### Clause and admissibility matrix

| Source clause | Active? | Exact use in this run |
|---|---:|---|
| p-th-power set subgroup powerful? | no | Excluded; no powerfulness conclusion is asserted. |
| p != 2, exponent p^2, p-th-power set subgroup => abelian? | yes | Restricted experiment at p=3; the universal odd-prime scope remains broader. |
| p=2, exponent 8, square-set subgroup => abelian? | no | Explicitly excluded. |

| constraint_id | role | run check |
|---|---|---|
| 21.137-odd-forall-p-G | admissibility | The source target is universal; this p=3 run can at most prove the complete p=3 subfamily or give a p=3 witness. |
| 21.137-odd-p-not-2 | admissibility | p=3, hence odd and not 2. |
| 21.137-odd-finite-p-group | admissibility | Any candidate must be a complete finite 3-group. |
| 21.137-odd-exponent-p2 | admissibility | Exact exponent 9 is mandatory. |
| 21.137-odd-power-set-definition | admissibility | P means the literal set `{g^3:g in G}`, not its generated subgroup. |
| 21.137-odd-power-set-subgroup | admissibility | Literal cube-set closure is mandatory. |
| 21.137-odd-P-abelian | target conclusion | Proof must force P abelian; witness must exhibit a noncommuting literal-cube pair. |

`active_scope_checked: yes`.  No candidate exists at this point.

## Strategy portfolio (binding 45-minute increment)

1. **Global extension datum (assigned; first).**  Derive the normalized section,
   action-lift, factor, associativity, cube-label, and complete cube-fibre laws for
   every element of `H=G/P`.  Test the full normalized one-cochain gauge before
   treating any center-action-square term as an obstruction.
2. **Structured construction.**  Only if the simultaneous equations freeze a
   finite row, reconstruct its complete group and literal cube set.  No local
   factor row or selected fibres qualify.
3. **Theoretical contradiction.**  In a least p=3 counterexample, reduce `P'` and
   audit whether global action multiplication makes the square term
   gauge-invariant.  Kill immediately if it remains a section coboundary.
4. **Certificate plan.**  A proof claim would need a gauge-independent identity
   plus all seven scope rows.  A witness would need a finite presentation,
   independent normal-form/order check, exact exponent 9, exhaustive cube image,
   Cayley closure, and a named noncommuting pair.  A method-failure result is
   certified by explicit transformation formulae showing every simultaneous law
   is preserved by an arbitrary normalized central one-cochain.

## 2026-08-18T06:36:16Z — independent least-counterexample reduction

Assume only for this reduction that `G` is a least-order counterexample in the
complete p=3 subfamily.  Then:

1. Every element of `P` is a cube, so every element of `P` has order at most 3.
   Thus `P` has exponent 3.  The literal cube set is automorphism invariant and,
   by hypothesis, a characteristic subgroup.
2. `H=G/P` has exponent 3.
3. Choose a minimal nontrivial `G`-normal subgroup `N <= P'`.  A minimal normal
   subgroup of a finite 3-group has order 3 and lies in `Z(G)`.
4. In `G/N`, the literal cube set is exactly `P/N`, hence is a subgroup.  The
   quotient still has exponent exactly 9: exponent 3 would put every cube in `N`,
   giving `P <= N`, impossible because `P` is nonabelian.
5. Minimality makes `P/N` abelian.  Hence `P' <= N`; consequently
   `P'=N` has order 3 and is central in `G`.  In particular `P` has class 2.

This reduction was rederived here and is not imported from an earlier run.  It is
conditional on the least-counterexample assumption and does not answer the source
target.

## 2026-08-18T06:36:16Z — the complete normalized extension datum

Fix the convention

```text
iota_x(q) = x q x^-1,
sigma(1)=1,
alpha_h = iota_{sigma(h)},
f(h,k) = sigma(h) sigma(k) sigma(hk)^-1 in P.
```

Every element of `G` has a unique normal form `u sigma(h)`.  Direct multiplication
and associativity give, simultaneously for all `h,k,l in H`,

```text
(u,h)(v,k) = (u alpha_h(v) f(h,k), hk),                         (E1)
alpha_h alpha_k = iota_{f(h,k)} alpha_{hk},                    (E2)
f(h,k) f(hk,l) = alpha_h(f(k,l)) f(h,kl),                      (E3)
f(1,h)=f(h,1)=1.                                               (E4)
```

Since `H` has exponent 3, define the selected section cube label

```text
a_h = sigma(h)^3 = f(h,h) f(h^2,h).                            (E5)
```

Then

```text
alpha_h^3 = iota_{a_h},     alpha_h(a_h)=a_h.                  (E6)
```

Crucially, one selected label per quotient element is not the literal cube map.
The complete cube fibre over `h` is

```text
F_h = { u alpha_h(u) alpha_h^2(u) a_h : u in P }.              (E7)
```

The exact source hypothesis that the designated kernel is the literal cube set is
the global coverage equation

```text
P = union_{h in H} F_h.                                       (COV)
```

Equations `(E1)--(E7)` plus `(COV)` keep the literal set distinct from its generated
subgroup.  No commutativity has been used.

## 2026-08-18T06:36:16Z — global central one-cochain gauge

Put `Z=Z(P)`, written additively when convenient.  It is an elementary abelian
3-group.  Restriction of the action lifts gives a genuine representation
`rho:H -> GL(Z)`: the inner correction in `(E2)` acts trivially on `Z`.  For every
`h`, `rho_h^3=1`; if `D_h=rho_h-1`, then

```text
D_h^3=0,
1 + rho_h + rho_h^2 = D_h^2                                 (char 3).  (G0)
```

Now take an *arbitrary* normalized function `z:H -> Z`, `z_1=0`, and replace the
whole section at once by `sigma'(h)=z_h sigma(h)`.  Direct collection gives

```text
alpha'_h = alpha_h,                                           (G1)
f'(h,k) = z_h + rho_h(z_k) + f(h,k) - z_hk,                   (G2)
a'_h = ((1+rho_h+rho_h^2)z_h) a_h
     = (D_h^2 z_h) a_h,                                       (G3)
```

These are global formulas for every quotient element, not separate local ansatzes.
Because `(G2)` is the central two-coboundary of `z`, `(E1)--(E6)` and every
associativity equation remain true (`d^2 z=0`).  More strongly, the complete fibres
do not change.  Algebraically, centrality lets the norm of `u-z_h` cancel the
added norm of `z_h`; geometrically, `u sigma(h)=(u-z_h)sigma'(h)`.  Therefore

```text
F'_h=F_h for every h, and (COV) is unchanged.                  (G4)
```

where the parenthesized factor is interpreted additively in `Z` and multiplied
centrally with `a_h` in `P`.  Thus every term of the form `D_h^2 z_h` is a pure
global section gauge.  Imposing
all action, multiplication, associativity, cube-label, and literal-coverage laws
simultaneously does not constrain it.  The freedom is the full normalized
one-cochain group `C^1(H,Z)`, not a collection of incompatible local choices.

## 2026-08-18T06:36:16Z — noncommuting triple test and exact missing bridge

If `P` is nonabelian, choose actual cube values `A,B` with `[A,B]!=1`; closure gives
the third actual cube value `C=AB`.  Let their roots lie over quotient elements
`h,k,l`.  The global data records all three through `(E7)`, even if two roots lie
in the same quotient coset.  However `(COV)` imposes **no relation at all** between
`l` and `hk`.  The coherence law `(E2)` couples the indices `h,k,hk`, whereas the
root of `AB` may lie over any `l` whose fibre contains `AB`.

Equivalently, define the gauge-invariant incidence relation

```text
R = { (h,A) in H x P : A in F_h }.
```

`(COV)` says only that `R -> P` is onto.  For `A,B,AB`, it supplies three unrelated
incidences.  To turn `(E2)--(E3)` into a relation among these values one would need
the extra matching statement

```text
there are incidences (h,A), (k,B), (hk,AB),                    (MATCH)
```

or a comparably strong multiplicative selector.  Literal cube-set closure does not
state `(MATCH)`.  Indeed `(xy)^3` belongs to `F_hk`, but it need not equal
`x^3 y^3`.

The center-square term cannot repair this missing bridge.  By `(G1)--(G4)` a
nonzero `D_h^2 z_h` changes only the selected section coordinate while preserving
all complete fibres.  It also cannot destroy a noncommuting pair: central label
shifts leave `[A,B]` unchanged, and in the least-counterexample reduction even
`alpha_h^3=iota_{a_h}` is blind to central changes because `P'<=Z(P)`.

Therefore noncommuting values `A,B,AB` survive the complete simultaneous coherence
system *conditionally whenever they occur in the literal fibres*, even in the
presence of a nonzero center-action-square.  This is not an existence result for a
counterexample.  It is an exact failure certificate for the proposed obstruction:
the standard global extension laws are section-gauge invariant and closure gives
surjective incidence, not quotient-index multiplication.

## 2026-08-18T06:39:41Z — sign and circularity audit

- The convention is `alpha_h(q)=sigma(h)q sigma(h)^-1`; with it the correction
  order in `(E2)` and `(E3)` is exactly as displayed.  Both equations were also
  checked by multiplying three normal forms in the two associations.
- Multiplicatively, the potentially ambiguous gauge formula is
  `f'(h,k)=z_h rho_h(z_k) f(h,k) z_hk^-1`.  All `z` terms are central in `P`, so
  the additive version in `(G2)` has no hidden ordering assumption.
- `(G3)` follows directly from `(z_h sigma(h))^3`; it does not assume the desired
  cube-set closure.  `(G4)` is a reparametrization of every element in the same
  quotient coset, so it covers the entire literal fibre rather than selected roots.
- The least-counterexample reduction is used only to identify the central layer
  in which noncommutativity lives and to make the action-square formula transparent.
  The gauge failure itself holds for any class-2 exponent-3 kernel with the stated
  central action.  No least-counterexample consequence was smuggled into `(COV)`.
- A pass of the simultaneous coherence equations proves only that a datum is a
  group extension.  It does **not** prove that its literal cubes cover the kernel;
  that remains the separate equation `(COV)`.  Conversely, `(COV)` is only a set
  cover and does not prove `(MATCH)`.

No computation, catalogue, factor-row enumeration, or external search was run.
No finite candidate exists.

## 2026-08-18T06:40:46Z — strategy stop

- Work stop after 15 newly elapsed active minutes.
- Official cumulative ledger proposed: 824 -> 839; 30 granted minutes unused.
- Outcome: `STRATEGY_EXHAUSTED` for `P3-SIMULTANEOUS-ROOT-ACTIONS` only.
- Exact kill: the full simultaneous extension datum has an arbitrary normalized
  central `C^1(H,Z(P))` gauge; its `D_h^2z_h` label terms preserve every extension
  law and every literal cube fibre.  Cube-set closure supplies no multiplicative
  matching of root quotient indices.
- Active assignment answered: no.  The complete p=3 subfamily and universal
  odd-prime scope remain open.
- State: `awaiting_lead`; no replacement strategy starts in this session.

## 2026-08-18T06:42:13Z — ledger correction after notation audit

- 2026-08-18T06:41:00Z — packaging briefly resumed to remove an ambiguity between
  additive notation in `Z(P)` and multiplication in `P` from formula `(G3)`.
- 2026-08-18T06:42:13Z — packaging stopped.
- Conservatively charge two further completed active minutes.  Final proposed
  charge is 17 minutes, official cumulative 824 -> 841, with 28 granted minutes
  unused.  This supersedes only the 15-minute ledger line above; the mathematical
  outcome and `awaiting_lead` state are unchanged.
