---
title: "Verification — Kourovka 12.15 — R3 defect-size correction"
problem: "12.15"
scope_id: 12.15/normal-closure-fibres
scope_record: Agents/Kourovka/scopes/12.15-normal-closure-fibres.json
assignment_revision: 1
claim: "The order-128 two-generator regime R3 remains a possible qualifying least-counterexample regime with |D_G(c)|=16 and nonzero-line image in H/A."
claimant: Problem-12.15
target_statement: "For every finite 2-group G in which equal normal closures imply conjugacy, G' is abelian."
excluded_scopes: ["none"]
target_object: "A hypothetical least counterexample to the exact source statement, specialized to order-128 regime R3"
witness_object: "The same symbolic R3 specialization; no concrete group or computational witness is used"
witness_equals_target: proven-with-citation
citation: "Direct conditional derivation in this note from the source hypothesis and the defining R3 data"
verification_method: computation-free line-by-line hand proof and dependency audit
tools_used: ["GAP 4.12.1 (probed, unused)", "Python 3.12.3 (probed, unused)", "pdftotext 24.02.0"]
scope_answered: ["order-128 regime R3 is eliminated"]
scope_not_answered: ["order-128 regimes R1 and R2", "possible least counterexamples of order greater than 128", "12.15/normal-closure-fibres"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/commutators, project/kourovka, status/refuted]
---

# Verification — Kourovka 12.15 — R3 defect-size correction

## Verdict

**The orbit bound eliminates R3.** The old order-(16), nonzero-line defect row is not to be replaced by (D_G(c)=A); it is a correct conditional consequence of the exact fibre lemma and normal generation. The previous claim that R3 remained a surviving order-128 regime is `status/refuted`.

This is only a bounded structural correction. `active_assignment_answered: no`: R1, R2, and all relevant larger orders remain open.

## The claim and exact scope

The source PDF, page 58, visually states one clause: in a finite 2-group, equal normal closures imply conjugacy; does it follow that the derived subgroup is abelian? The canonical record faithfully represents that clause as revision 1. The present claim concerns only the R3 specialization of a hypothetical least counterexample:

\[
H=G',\quad A=Z(H),\quad |G:H|=4,\quad |H|=32,\quad |A|=8,
\quad H/A\cong C_2^2,
\]

where (G) is two-generated and (c=[x,y]) is the basic commutator of a minimal generating pair.

No `claim-checks/*.json` accompanied the correction request. This is a correction of one previously reviewed bounded dependency, not a routed whole-scope solution claim; no whole-scope certification is inferred.

## Clause matrix

| source clause / branch | active? | result of this audit | remains |
|---|---:|---|---|
| Full finite-2-group implication | yes | not answered | R1, R2, larger orders |
| First possible order 128, R1 | subordinate | not audited here | open |
| First possible order 128, R2 | subordinate | not audited here | open |
| First possible order 128, R3 | subordinate | eliminated | none within R3 |

## Constraint-and-conclusion matrix

| constraint_id | role | proof use / candidate value | evidence | result |
|---|---|---|---|---|
| `12.15-forall-G` | admissibility | R3 is only one conditional branch | clause matrix | partial only |
| `12.15-finite` | admissibility | finite indices, maximal invariant subgroups, and orbit-stabilizer | direct proof below | pass |
| `12.15-two-group` | admissibility | relative Frattini quotient has order 2; R3 sizes are powers of 2 | direct proof / defining R3 row | pass conditionally |
| `12.15-normal-closure-fibre` | admissibility | identifies (D_G(c)) exactly and forces index 2 in (H) | direct reconstruction below | pass conditionally |
| `12.15-derived-abelian` | target conclusion | eliminating R3 does not establish (G''=1) universally | no proof supplied | not established |

## Target versus witness and circularity

There is no separate witness. The object tested is exactly the symbolic R3 specialization of a hypothetical least counterexample in the source class. All groups and subgroups used below are derived from that conditional object: (H=G'), (A=Z(H)), and (c=[x,y]). The contradiction does not build a group from the desired conclusion, assume (G''=1), or infer sufficiency from a quotient condition. It shows that the defining R3 conditions and the source hypothesis cannot hold simultaneously.

## Subclaims and what each method proves

1. Direct relative-Frattini reasoning proves the exact fibre identity and \(|H:D_G(c)|=2\); it does not prove the universal target.
2. The two-generator commutator argument proves \(\langle c\rangle^G=H\); it does not assert that every rank branch is two-generated.
3. Centralizer indices compute the \(H\)-orbit and bound the \(G\)-orbit; they do not use or classify extensions.
4. The induced \(E=G/H\)-action computes the image of \(D_G(c)\) in \(H/A\); it proves the old line row, not existence of a compatible full group.
5. Dependency tracing identifies exactly which order-128 statements must be corrected; it does not alter R1, R2, the order lower bound, or the universal status.

## Exact fibre identity, reconstructed

Use ([a,b]=a^{-1}a^b). For a nonidentity element (u) of a qualifying finite 2-group put

\[
N=\langle u\rangle^G,\qquad R=N^2[N,G].
\]

The quotient \(N/R\) is central elementary abelian and is generated by the single image \(uR\), because all \(G\)-conjugates of \(u\) have that image. It is nontrivial: if \(R=N\), choose a maximal proper \(G\)-invariant subgroup \(L<N\). Then \(N/L\) is a minimal normal subgroup of the finite 2-group \(G/L\), hence central of order 2, so \(N^2[N,G]\le L<N\), a contradiction. Therefore

\[
|N:R|=2,\qquad u\notin R.
\]

If \(v\in N\setminus R\), then \(\langle v\rangle^G R=N\). A maximal proper \(G\)-invariant subgroup containing a hypothetical proper \(\langle v\rangle^G\) would also contain \(R\) by the same minimal-normal-factor argument, contradicting \(\langle v\rangle^G R=N\). Thus \(\langle v\rangle^G=N\), and the source hypothesis gives \(v\sim_G u\). Conversely every conjugate of \(u\) lies in \(uR\). Hence

\[
u^G=N\setminus R=uR,
\qquad
D_G(u):=\{[u,g]:g\in G\}=u^{-1}u^G=R. \tag{1}
\]

In particular,

\[
u^G=uD_G(u),\qquad |D_G(u)|=|u^G|=|N|/2. \tag{2}
\]

This verifies the exact identity as a value-set identity, not merely an equality after taking generated subgroups.

## Why the basic commutator normally generates (H)

For \(G=\langle x,y\rangle\) and \(c=[x,y]\), let \(N=\langle c\rangle^G\). Since \(c\in G'\) and \(G'\lhd G\), \(N\le G'\). In \(G/N\), the images of \(x\) and \(y\) commute and generate, so \(G/N\) is abelian; hence \(G'\le N\). Therefore

\[
\langle c\rangle^G=G'=H. \tag{3}
\]

Applying (2) in R3, where (|H|=32), gives

\[
|D_G(c)|=|c^G|=16. \tag{4}
\]

Thus \(D_G(c)=A\), of order 8, is impossible even before considering centralizers.

## The (H)-orbit: both cases

Because (A=Z(H)), (A\le C_H(c)).

### Case (c\in A)

Then (C_H(c)=H) and

\[
|c^H|=1.
\]

Moreover this case is already inconsistent with (3): (A=Z(H)) is characteristic in (H\lhd G), hence (A\lhd G); therefore (c\in A) would imply (\langle c\rangle^G\le A<H), contrary to (\langle c\rangle^G=H).

### Case (c\notin A)

Since (H/A\cong C_2^2), the coset (cA) has order 2. Hence

\[
|A\langle c\rangle|=2|A|=16.
\]

Every element of (A) centralizes (c), and (c) centralizes its own powers, so

\[
A\langle c\rangle\le C_H(c),\qquad |c^H|=|H:C_H(c)|\le2. \tag{5}
\]

This is the only viable case under normal generation, but both cases give a contradiction below.

## Relating the (H)- and (G)-orbits

For (H\lhd G), the exact index factorization is

\[
|c^G|=[G:C_G(c)]
=[G:HC_G(c)]\,[H:C_H(c)]. \tag{6}
\]

The first factor is at most ([G:H]=4). Thus the (c\in A) case gives (|c^G|\le4), and the (c\notin A) case gives

\[
|c^G|\le4\cdot2=8. \tag{7}
\]

Equations (4) and (7) contradict one another. Hence R3 cannot occur.

## The old line image in (H/A)

The old line-image deduction is also correct. Put (V=H/A\cong C_2^2), (E=G/H\cong C_2^2), and (v=cA). Since (H) has class two, its conjugation action on (V) is trivial, so the (G)-action factors through (E). Equation (3) says that the (E)-orbit of (v) spans (V).

The image of the elementary abelian group \(E\) in \(\operatorname{Sp}(V)\cong S_3\) has order at most 2. It cannot be trivial, since then the orbit of one vector would span at most one dimension. Let \(T\) be its nontrivial element. The vector \(v\) is not fixed, for the same cyclic-span reason, and

\[
\pi(D_G(c))
=\{v+e(v):e\in E\}
=\{0,v+T(v)\}, \tag{8}
\]

a nonzero line of order 2. Combining (4) and (8),

\[
|D_G(c)\cap A|=|D_G(c)|/2=8=|A|,
\]

so \(A\le D_G(c)\), \(|D_G(c):A|=2\), and \(D_G(c)\) is abelian because \(A=Z(H)\). Thus every part of the old cross-layer row is sound conditionally. Precisely because it is sound, (7) eliminates R3. Replacing it by \(D_G(c)=A\) would contradict both (4) and the nonzero image (8).

## Downstream order-128 and central-lift audit

| dependency | correction | unaffected content |
|---|---|---|
| `verification/2026-08-16T123910Z-cycle-close-central-lift-audit.md` | Its statements that three regimes survive and that the R3 row causes no coverage change are superseded. The R3 row is sound but internally contradictory with the omitted centralizer bound. | The order lower bound, numerical four-to-three prefilter, R1/R2 descriptions, and generic reconstruction equations are untouched. |
| `runs/2026-08-16-r1-proof/central-lift-spec.md` | The current surviving table must contain only R1 and R2. The R3 paragraph and rows G7/H5 should be marked eliminated, not searched. References to action sizes “R1–R3” become “R1–R2”. | Layers H1–H4, G1–G6, and P1–P4 remain a valid certificate specification for R1/R2. |
| `runs/2026-08-16-r1-proof/log.md` | The historical order-16/line calculation is valid; the later description “three surviving” must be read as pre-centralizer filtering. R3 is now eliminated. | The dimension lemma and all earlier reductions remain as stated. |
| `runs/2026-08-16-r1-proof/findings.md` | “Three exact size patterns remain” is only an intermediate numerical statement; “three surviving regimes” as the current endpoint is obsolete. The current order-128 remainder is R1 and R2. | The intrinsic fibre and minimum-counterexample results are unaffected. |
| `ideas/2026-08-16-mixed-fibre-obstruction-and-central-lift.md` | M1 is unnecessary and must stop; M3, if ever authorized, ranges over two regimes rather than three. | M2's general mixed-fibre assessment and the universal-scope warning are unaffected. |
| `runs/2026-08-17-r2-mixed-fibre/m1-r3-precondition-blocker.md` and its log | Its orbit calculation is correct; its stated fork resolves to immediate R3 elimination. The action-orbit enumeration remains diagnostic and irrelevant. | No other run result is upgraded. |
| Lead's R3 M1 pivot | Same-scope, same-revision R3 square-orbit work must stop. | R1/R2 or a separately authorized larger-order strategy is not stopped. |

The earlier verification note is therefore corrected, not globally discarded: its false terminal survival count is refuted, while the cross-layer row it checked supplies half of the contradiction.

## Evidence transcript

Tool probe used before the audit:

```text
$ gap -q -c 'Print(GAPInfo.Version,"\\n");QUIT;'
4.12.1
$ python3 --version
Python 3.12.3
$ pdftotext -v
pdftotext version 24.02.0
Copyright 2005-2024 The Poppler Developers - http://poppler.freedesktop.org
```

Source command:

```bash
source _meta/agents/Kourovka/paths.env
pdftotext -f 58 -l 58 -layout "$KOUROVKA_PDF" -
```

Relevant exact output, also checked against the rendered page:

```text
12.15. Suppose that, in a finite 2-group G, any two elements are conjugate whenever
their normal closures coincide. Is it true that the derived subgroup of G is abelian?
                                                                E. A. Golikova, A. I. Starostin
```

No GAP, Python, catalogue, or discovery computation is used as mathematical evidence. The verification is the displayed hand proof.

## Why this verdict

The two cardinalities concern the same set: (1) gives \(c^G=cD_G(c)\), hence \(|c^G|=|D_G(c)|=16\); (6)–(7) give \(|c^G|\le8\). Every premise is either the exact source hypothesis, a defining R3 datum, or a direct two-generator/group-index identity. The alternative \(D_G(c)=A\) violates two independently derived consequences. Therefore the only one of the three proposed outcomes consistent with all dependencies is: **the orbit bound eliminates R3**.

## What is NOT established

This does not eliminate R1 or R2, improve the general lower bound beyond recording that an order-128 counterexample cannot lie in R3, address any order above 128, prove (G''=1), or answer the active assignment.

## What would upgrade it

To strengthen the order-128 result, R1 and R2 must also be eliminated by valid hand arguments or an independently reproducible exact finite certificate. To close the source scope, all larger-order least-counterexample possibilities must also be excluded (or a qualifying counterexample supplied), followed by the full review circle and human review.
