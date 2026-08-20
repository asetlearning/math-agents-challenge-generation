---
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
cycle: 14
strategy: MINIMAL-NORMAL-FULL-LIFT-GATE
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

# Cycle 14 log: minimal-normal full-lift gate

## Active-time ledger

- `2026-08-18T05:51:21Z`: active work began from inherited detailed cumulative time `02:47:01`.
- `2026-08-18T05:54:28Z`: protocol, scope, source, and portfolio gate completed; detailed cumulative time `02:50:08`.
- `2026-08-18T06:19:25Z`: `PARTIAL_RESULT` filed and bus handoff completed; new active time `00:28:04`, detailed cumulative time `03:15:05`. Charged research stopped in `awaiting_lead`.

## 2026-08-18T05:54:28Z — source, scope, and staleness gate

The source PDF resolved through `_meta/agents/Kourovka/paths.env`. I rendered and
visually inspected PDF page 161 (not merely `pdftotext`). Correct transcription:

> Let \(\chi\) be a complex irreducible character of a finite group \(G\). If
> \(\chi(x)\ne0\) for some \(x\in G\), must the order \(o(x)\) of \(x\) divide
> \(|G|/\chi(1)\)? This is known to be true if \(G\) is solvable, and it is known
> that \((o(x)\chi(1))^4\) divides \(|G|^5\) for arbitrary \(G\).

`source_transcription_checked: yes`. The corpus row records `answered: false`,
`has_editor_comment: false`, and `has_later_comment: false` (its page field is 162,
whereas the canonical record and rendered PDF locate the statement on PDF page
161). `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
I did not inspect open-web results or prior solution-bearing run artifacts.

### Clause matrix

| source clause | equivalent formulation | active? | external-result treatment in this blind run |
|---|---|---:|---|
| If \(\chi(x)\ne0\), must \(o(x)\mid |G|/\chi(1)\)? | \(o(x)\chi(1)\mid |G|\) | yes | deferred; this is the universal target |
| Assertion holds for solvable \(G\) | solvable special case | no | contextual only |
| \((o(x)\chi(1))^4\mid |G|^5\) for arbitrary \(G\) | weaker universal bound | no | contextual only |

`active_scope_checked: yes`.

### Six-row admissibility/conclusion checklist

| constraint_id | use in this proof-direction gate |
|---|---|
| `20.115-forall-G-chi-x` | a least counterexample, if assumed, must be among all admissible triples; any reduction must return a universal implication or an explicitly delimited subclass |
| `20.115-G-finite` | all normal-subgroup, quotient, Clifford, and central-extension objects begin from a finite ordinary group \(G\) |
| `20.115-chi-complex-irreducible` | \(\chi\in\operatorname{Irr}(G)\); projective constituents are auxiliary proof vehicles and cannot replace this row |
| `20.115-x-in-G` | \(x\in G\), and every order is the exact group-element order in the named group or quotient |
| `20.115-character-value-nonzero` | only exact \(\chi(x)\ne0\) is usable; constituent/nonzero-projective-trace claims must be related back to it without cancellation errors |
| `20.115-order-degree-divisibility` | target is the integer divisibility \(o(x)\chi(1)\mid |G|\), not the weaker fourth-power statement or a degree-only condition |

The checklist matches all six canonical rows; no scope mismatch was found.

## 2026-08-18T05:54:28Z — strategy portfolio

1. **Theoretical/minimal-counterexample audit (first):** derive, without using
   historical run claims, the exact consequences of least \(|G|\), kernel
   reduction, Clifford theory over a proper minimal normal subgroup \(N\), and
   induction/imprimitivity. Then test each of the three requested transfer inputs
   prime by prime. Kill this route at the first explicit counterexample to an
   input or first theorem not implied by the reductions.
2. **Structured obstruction construction:** use small semidirect/direct/central
   products to falsify an allegedly forced scalar-kernel, order-lift, or
   multiplicity assertion while preserving as many least-counterexample
   reductions as logically available as possible. A valid failure certificate is
   an exact \((G,\chi,x,N)\), not a statement that Clifford homogeneity alone is
   weak.
3. **Abelian-versus-nonabelian split:** for abelian minimal \(N\), exploit the
   linear constituent and inertia action; for \(N=S^t\), exploit tensor-product
   constituents and factor permutation. Identify which primewise statements
   survive in each branch.
4. **Bounded catalogue mode:** no catalogue expansion is authorized or useful for
   a universal structural implication. Tiny named groups may be hand-checked only
   as exact certificates falsifying a proposed intermediate input.
5. **Certificate plan:** Validator can reconstruct every ordinary character from
   an explicit linear representation or standard character table, compute
   \(N\), inertia, restriction multiplicity, quotient order, lift orders, scalar
   kernel, and each divisibility by hand. Any positive reduction will be stated as
   a lemma with all hypotheses and a primewise valuation proof.

## 2026-08-18T06:17:33Z — theoretical gate and exact obstructions

Detailed cumulative time: `03:13:13` (new active time `00:26:12`). The full
derivation and certificates are in `findings.md` in this run directory.

The least-counterexample deductions are faithful \(\chi\), primitive \(\chi\),
and homogeneous restriction \(\chi_N=a\theta\) to every normal subgroup. For a
proper minimal normal \(N\), \(\theta\) is faithful. Thus the abelian branch is
exactly central \(C_p\), while the nonabelian branch is perfect \(S^t\).

For the Clifford class of order \(n\), determinant arguments independently give
\(n\mid a\), and, in the perfect branch, \(n\mid\theta(1)\). Hence
\(n<|N|\) is valid for nonabelian minimal \(N\), but it fails in the central
branch when the class is nontrivial: there \(n=p=|N|\). A trivial class in the
central branch lets minimality in \(G/N\) finish the source divisibility, so only
the equality case can survive in a least counterexample.

The exact transfer arithmetic exposed a mismatch in the assigned third input.
Writing \(q=o(xN)\), \(r=o(x)/q\), \(f=\theta(1)\), and
\(o(\widehat x)=qt\) for an effective kernel of order \(n\), minimality gives
\(qa\mid(n/t)|G/N|\). The corresponding sufficient kernel condition is
\(rf(n/t)\mid|N|\), not \(ra\mid|N|\). Under full lift it is \(rf\mid|N|\).

Two exact ordinary obstructions were derived:

- In `2.A6`, a faithful degree-four spin row at the central involution has value
  `-4`; the unique proper minimal normal subgroup is \(C_2\), the effective
  Clifford kernel has order two, and \(r a=2\cdot4=8\nmid2\).
- In \(A_5^8\rtimes A_8\), with the tensor-permutation extension of a degree-three
  \(A_5\) row tensored by the standard degree-seven \(A_8\) row, the base
  \(N=A_5^8\) is the unique minimal normal subgroup and the character is faithful,
  primitive, and quasiprimitive. At a complement double transposition the value is
  \(3^6(4-1)=3^7\ne0\), but \(r a=7\nmid60^8\). Here the scalar class is trivial,
  so this isolates the multiplicity failure in the nonabelian branch.

Target self-check: all objects are finite and all characters used on the source
side are ordinary irreducible complex characters; every named value is exactly
nonzero. Neither example violates \(o(x)\chi(1)\mid|G|\), and no universal claim is
made. The strategy representation remains productive only after replacing the
false \(ra\)-condition by the exact \(rf\)-condition.

### Commands actually run

The source page was rendered with `pdftoppm` and visually inspected. The only
algebra computations were sub-minute GAP/CTblLib inspections. In particular:

```text
timeout 30s gap -q -c 't:=CharacterTable("2.A6");;
Display(CharacterTable("2.A6"));;
Print("orders=",OrdersClassRepresentatives(t),"\n");;
Print("fusions=",ComputedClassFusions(t),"\n");; QUIT;'
```

Observed relevant output: table order `720`; class orders beginning
`[1,2,4,3,6,...]`; quotient fusion sends classes `1a,2a` to the identity class of
`A6`; rows `X.8`, `X.9` have degree `4` and value `-4` on `2a`.

An exploratory exact matrix check of the qutrit Heisenberg--Clifford group used
generators of orders `[3,3,3,4]` and returned group size `648`, center size `3`,
and a nonzero trace on the order-three phase element. This was not needed for the
reported obstruction and supports no claim in `findings.md`.

No heavy computation, catalogue expansion, or leased resource was used.

## 2026-08-18T06:19:25Z — cycle outcome

`PARTIAL_RESULT`. The full three-input package is false, and its third input is
not the arithmetic input required by the character-triple transfer. The exact
surviving nonabelian scalar-kernel lemma and two ordinary obstruction certificates
were routed to Lead and Validator; the next-strategy choice was routed to
MathExpert. The universal source target remains open. State: `awaiting_lead`.
