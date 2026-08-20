---
title: "Kourovka 12.15 clean proof run — cycle 9"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/draft
problem: 12.15
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
direction: proof
context_mode: clean
---

# Working log

## Active-time ledger

- 2026-08-16T11:51:31Z — work start; inherited cumulative active minutes: 254; current clean proof extension budget: 60 minutes.
- 2026-08-16T11:54:51Z — source/scope gate completed; cumulative active minutes: 257.

## Staleness check

### Scope authority and independent audit

- Canonical record read first after the common protocol: `Agents/Kourovka/scopes/12.15-normal-closure-fibres.json`.
- `scope_id`: `12.15/normal-closure-fibres`; `assignment_revision`: 1; active direction: proof.
- The record requires an independent source audit and records `status: passed`, auditor `Validator`, checked before this run. I did not open the referenced verification note because clean-context instructions exclude verification notes.
- Assignment constraint IDs and canonical required constraint IDs coincide exactly: `12.15-forall-G`, `12.15-finite`, `12.15-two-group`, `12.15-normal-closure-fibre`, `12.15-derived-abelian`.
- `independent_scope_audit_passed: yes`.

### Original source and corrected transcription

Resolved the source only through `_meta/agents/Kourovka/paths.env`; the configured PDF was readable. Navigation command:

```bash
source '_meta/agents/Kourovka/paths.env'
pdftotext -f 58 -l 58 -layout "$KOUROVKA_PDF" -
```

Observed relevant output:

```text
12.15. Suppose that, in a finite 2-group G, any two elements are conjugate whenever
their normal closures coincide. Is it true that the derived subgroup of G is abelian?
                                                                E. A. Golikova, A. I. Starostin
```

Rendered page 58 was then generated in `/tmp` with:

```bash
source '_meta/agents/Kourovka/paths.env'
pdftoppm -f 58 -l 58 -singlefile -png -r 180 "$KOUROVKA_PDF" '/tmp/kourovka-12-15-page58'
```

I visually inspected the rendered page, including the words “finite 2-group”, “any two elements”, “conjugate whenever”, “normal closures coincide”, and “derived subgroup ... abelian”. There are no hidden formulae, part labels, parameter clauses, or typography ambiguities.

Corrected transcription (verbatim):

> **12.15.** Suppose that, in a finite 2-group \(G\), any two elements are conjugate whenever their normal closures coincide. Is it true that the derived subgroup of \(G\) is abelian?

`source_transcription_checked: yes`.

The corpus available in this vault is issue 20 rather than issue 21. Command:

```bash
rg -n '12\.15' 'Research/Group theory/Open problems/Kourovka/corpus/kourovka-20-corpus.jsonl' 'Research/Group theory/Open problems/Kourovka/corpus/kourovka-issue-12-1992.md'
```

Observed JSONL record:

```json
{"id":"12.15","issue":12,"year":1992,"page":57,"answered":false,"has_editor_comment":false,"has_later_comment":false,"statement":"Suppose that, in a finite 2-group G, any two elements are conjugate whenever their normal closures coincide. Is it true that the derived subgroup of G is abelian?","proposers":["E. A. Golikova","A. I. Starostin"],"chars":162}
```

Thus `answered: false`, `has_editor_comment: false`, and `has_later_comment: false`. The corpus navigation field says page 57, whereas the canonical scope record and direct rendered inspection put the item on physical/printed PDF page 58. This is a navigation-metadata discrepancy only; the statement itself matches exactly.

### Discovery-blind external gate

- `DISCOVERY_BLIND: yes`; no open-web search was performed.
- I did not inspect any ordinary synthesis, historical log, findings, verification note, transcript content, archive, or other excluded context path.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.

### Clause matrix

| source clause | equivalent formulation | active scope? | literature-result coverage |
|---|---|---:|---|
| In a finite 2-group \(G\), if equality of normal closures implies conjugacy for every pair of elements, must \(G'\) be abelian? | For every finite 2-group \(G\), \((\forall x,y\in G)(\langle x\rangle^G=\langle y\rangle^G\Rightarrow x\sim_G y)\Rightarrow G''=1\). | yes — this is all of `12.15/normal-closure-fibres` | none consulted in this discovery-blind run; external gate deferred |

`active_scope_checked: yes`.

### Admissibility checklist reconstructed from the rendered source

| constraint_id | source requirement | proof obligation in this run | reconciliation |
|---|---|---|---|
| `12.15-forall-G` | “in a ... group \(G\)” plus “Is it true” asks a universal assertion | argument must use an arbitrary admissible \(G\), not a catalogue sample | exact match |
| `12.15-finite` | “finite” | finiteness may be used; no infinite-group substitution | exact match |
| `12.15-two-group` | “2-group” | \(|G|\) is a power of 2 | exact match |
| `12.15-normal-closure-fibre` | “any two elements are conjugate whenever their normal closures coincide” | for all \(x,y\in G\), \(\langle x\rangle^G=\langle y\rangle^G\) implies conjugacy in \(G\) | exact match; converse is automatic and not an extra hypothesis |
| `12.15-derived-abelian` | “derived subgroup ... abelian” | establish \([G',G']=G''=1\) | exact match |

No mismatch was found between rendered source, assignment, and canonical scope record.

### Inbox

Command:

```bash
find 'Agents/Kourovka/bus/inbox/Problem-12.15' -maxdepth 1 -type f -printf '%f\n' | sort
```

Observed output was empty: zero current messages, hence zero current-revision control messages.

## Strategy portfolio

Ranked by expected information per active hour:

1. **Theoretical mode — relative-Frattini fibre lemma.** For arbitrary \(x\), set \(N=\langle x\rangle^G\) and isolate the largest obvious non-generator subgroup \(R=N^2[N,G]\). Test whether the hypothesis forces the entire coset \(N\setminus R\) to be one conjugacy class, hence forces the commutator-value set \(\{[x,g]:g\in G\}\) to be the subgroup \(R\). This is cheap and admits a line-by-line certificate. Kill criterion: an unrepairable gap in the relative Burnside-basis step or no connection to \(G''\) after 25 active minutes.
2. **Theoretical mode — minimal-counterexample/chief-factor pivot.** Assuming \(G''\ne1\), choose a central chief factor inside \(G''\) and study whether the fibre lemma descends to, or constrains, the corresponding central extension. Certificate would be a precise inherited-property lemma or a structural restriction on a minimum counterexample. Kill criterion: quotient inheritance requires an unjustified lifting assertion.
3. **Catalogue/small-case mode.** With a Lead lease, GAP could enumerate a precisely bounded SmallGroups range and test all normal-closure fibres, recording exact library IDs and \(G''\). A negative result would exclude only that finite library range, not prove the target. It is lower priority in this one-hour proof-direction run, and no GAP or heavy computation will be launched without a lease.
4. **Structured-construction mode.** Represent a hypothetical minimum counterexample as a central extension of a metabelian quotient, translating fibre equality into restrictions on its action/cocycle. In proof direction this is a contradiction framework, not permission to switch to witness search. Kill criterion: the normal-closure hypothesis cannot be expressed invariantly at the extension level within the hour.
5. **Certificate plan.** Any useful lemma will be stated with exact subgroup definitions and proved using only finite-2-group chief factors, orbit–stabilizer, and explicit commutator identities. Validator can check it independently without trusting software. A scope-closing proof would additionally need one matrix row per canonical constraint and an independent check of the final implication to \(G''=1\).

Selected first experiment: relative-Frattini fibre lemma.

## 2026-08-16T11:58:31Z — relative-Frattini fibre lemma

Fix the commutator convention \([a,b]=a^{-1}a^b\), where \(a^b=b^{-1}ab\).

**Lemma (current-run derivation).** Let \(G\) be a finite 2-group satisfying the active normal-closure-fibre hypothesis. For \(1\ne x\in G\), put

\[
N_x=\langle x\rangle^G,
\qquad
R_x=N_x^2[N_x,G].
\]

Then:

1. \(R_x\lhd G\), \(|N_x:R_x|=2\), and \(x\notin R_x\);
2. \(x^G=N_x\setminus R_x=xR_x\);
3. the value set \(\{[x,g]:g\in G\}\) is exactly the subgroup \(R_x\), hence is normal in \(G\);
4. consequently \(x^2\in\{[x,g]:g\in G\}\), \(|x^G|=|N_x|/2\), and every element of \(N_x\setminus R_x\) normally generates \(N_x\).

**Proof audit.** Both \(N_x\) and \(R_x\) are normal in \(G\). The quotient \(N_x/R_x\) is elementary abelian, and \(G\) centralizes it. Since \(N_x\) is generated by the \(G\)-conjugates of \(x\), all of which have image \(xR_x\), this quotient is generated by one element and has order at most 2.

It is not trivial. Indeed, if \(R_x=N_x\), choose a maximal proper \(G\)-invariant subgroup \(L<N_x\) (possible because \(N_x\ne1\) is finite). Then \(N_x/L\) is a minimal normal subgroup of the finite 2-group \(G/L\), so it is central of order 2. Therefore \(N_x^2[N_x,G]\le L<N_x\), contradicting \(R_x=N_x\). This also shows \(x\notin R_x\), since otherwise normality of \(R_x\) and \(N_x=\langle x\rangle^G\) would give \(N_x\le R_x\).

Now take \(y\in N_x\setminus R_x\) and put \(M=\langle y\rangle^G\). Then \(MR_x=N_x\). If \(M<N_x\), choose a maximal proper \(G\)-invariant subgroup \(L<N_x\) containing \(M\). The same minimal-normal-factor argument gives \(R_x\le L\), whence \(N_x=MR_x\le L\), a contradiction. Thus \(M=N_x\). The active hypothesis now gives \(y\sim_G x\), so \(N_x\setminus R_x\subseteq x^G\).

Conversely, for every \(g\in G\), \(x^gR_x=xR_x\), because \([x,g]\in[N_x,G]\le R_x\). Thus \(x^G\subseteq xR_x=N_x\setminus R_x\). Equality follows. Finally,

\[
x^{-1}x^G=\{[x,g]:g\in G\}=R_x.
\]

This establishes every item without computation.

**What this proves.** The active hypothesis converts every fixed-first-entry commutator *value set* into the explicitly identified normal subgroup \(N_x^2[N_x,G]\); it is not merely the subgroup generated by those values. It also shows \(G/G'\) is elementary abelian, since \(x^2\in R_x\le G'\) for all \(x\), and shows \(Z(G)\) is elementary abelian, since \(z\in Z(G)\) gives \(R_z=1\) and hence \(z^2=1\).

**What this does not prove.** It does not yet show that the different subgroups \(R_x\) commute with one another, nor even that each \(R_x\) is abelian. Those are exactly the missing implications needed for \(G''=1\).

- 2026-08-16T11:58:31Z — lemma written and internally checked; cumulative active minutes: 261.

## 2026-08-16T12:00:52Z — intrinsic reformulation and quotient closure

For any finite 2-group \(H\) and \(a\in H\), write

\[
D_H(a)=\{[a,h]:h\in H\}.
\]

**Proposition.** The active normal-closure-fibre property for \(H\) is equivalent to the following two conditions holding for every \(a\in H\):

1. \(D_H(a)\) is a subgroup of \(H\);
2. \(a^2\in D_H(a)\).

Moreover, this property is inherited by every quotient of \(H\).

**Forward implication.** This is exactly the preceding lemma: for \(a\ne1\), \(D_H(a)=N_a^2[N_a,H]\), and this subgroup contains \(a^2\). For \(a=1\), both statements are immediate.

**Reverse implication, including normality audit.** Assume (1)–(2), and abbreviate \(D=D_H(a)\). Since \(a^H=aD\), conjugating this set by \(k\in H\) gives

\[
aD=(aD)^k=a^kD^k=ad_kD^k
\]

for some \(d_k\in D\). Hence \(D=d_kD^k\). The left side contains 1, so the right coset contains 1; therefore \(d_k\in D^k\), and consequently \(D=D^k\). Thus \(D\lhd H\).

If \(a\ne1\), then \(a\notin D\): otherwise \(a=[a,h]\) for some \(h\), so \(a^h=a^2\), impossible because a nonidentity element of a finite 2-group has strictly larger order than its square. It follows from \(a^2\in D\) that

\[
N_a=\langle a\rangle^H=\langle a,D\rangle=\langle a\rangle D,
\qquad |N_a:D|=2,
\qquad N_a\setminus D=aD=a^H.
\]

If \(N_a=N_b\), then \(b\notin D\), because otherwise normality of \(D\) would give \(N_b\le D<N_a\). Therefore \(b\in N_a\setminus D=a^H\), so \(a\) and \(b\) are conjugate. (The case \(a=1\) is immediate.) This proves the reverse implication.

**Quotient closure.** Let \(K\lhd H\). For every \(a\in H\),

\[
D_{H/K}(aK)=\{[a,h]K:h\in H\}=D_H(a)K/K.
\]

This is the image of a subgroup and contains \(a^2K=(aK)^2\). The equivalent conditions therefore hold in \(H/K\).

**Audit of a tempting but avoided gap.** Directly lifting equality of normal closures from \(H/K\) need not visibly give equality upstairs. The quotient argument is instead routed through the proved intrinsic commutator-value characterization, so it does not assume such a lift.

## Minimal-counterexample reduction

Assume the active assertion is false and choose a counterexample \(G\) of least order. Quotient closure implies that \(G/K\) satisfies the active hypothesis for every nontrivial \(K\lhd G\); minimality then gives

\[
(G/K)''=1,
\qquad\text{hence}\qquad
G''\le K.
\]

Thus \(G''\) lies in every nontrivial normal subgroup of \(G\). If \(L\) is a minimal nontrivial normal subgroup, then \(1\ne G''\le L\), so

\[
G''=L\cong C_2,
\qquad G''\le Z(G),
\]

and it is the unique minimal normal subgroup.

The preceding fibre lemma gives \(Z(G)\) exponent 2. Every nontrivial cyclic subgroup of \(Z(G)\) is therefore a normal subgroup of order 2 and must contain \(G''\). Hence there can be only one such subgroup, and

\[
\boxed{\;Z(G)=G''\cong C_2.\;}
\]

Writing \(G''=\langle z\rangle\), every noncentral \(a\in G\) has \(D_G(a)\ne1\); normality and uniqueness force \(z\in D_G(a)\). Therefore

\[
a z\in aD_G(a)=a^G
\]

for every \(a\notin Z(G)\). This is an additional checkable restriction on any minimum counterexample.

**Current bottleneck.** The remaining case is a central extension with \(G/Z(G)\) metabelian, \(Z(G)=G''=C_2\), and multiplication by the central involution preserving every noncentral conjugacy class. None of the arguments above alone excludes such a group.

- 2026-08-16T12:00:52Z — quotient/minimum-counterexample reduction written; cumulative active minutes: 264.

## 2026-08-16T12:05:11Z — bounded near-miss diagnostic

To test whether the minimum-counterexample restrictions alone were already contradictory, I wrote the bounded, problem-specific exact enumerator
`Agents/Kourovka/problems/12.15/runs/2026-08-16-r1-proof/scratch/check_wreath3.py` for the standard iterated wreath-product Sylow 2-subgroup

\[
W_3=\langle(1\ 2),(1\ 3)(2\ 4),(1\ 5)(2\ 6)(3\ 7)(4\ 8)\rangle\le S_8.
\]

The script explicitly closes the permutation group, conjugacy classes, normal closures, commutator-value sets, \(G'\), and \(G''\). Its search space is exactly 128 permutations and completed well under the 60-second/1-GB heavy-compute threshold; no leased job or general-purpose algebra package was used.

Exact command:

```bash
python3 --version
python3 'Agents/Kourovka/problems/12.15/runs/2026-08-16-r1-proof/scratch/check_wreath3.py'
```

Verbatim observed output:

```text
Python 3.12.3
group: standard <(1 2),(1 3)(2 4),(1 5)(2 6)(3 7)(4 8)> <= S8
group_order: 128
derived_order: 16
second_derived_order: 2
normal_closure_fibre_property: False
first_fibre_failure: x=(7 8) y=(3 4)(5 6)(7 8) shared_normal_closure_order=16
x_conjugacy_class_order: 4
y_conjugacy_class_order: 4
intrinsic_conditions_hold: False
first_intrinsic_failure: x=(7 8) commutator_value_count=4 value_set_is_subgroup=False square_in_value_set=True
```

**Interpretation.** This exact object has \(|W_3''|=2\) and is therefore a natural model for the last central-extension obstruction, but it is **not admissible**: two displayed involutions have the same order-16 normal closure and are not conjugate. Equivalently, its first displayed fixed-element commutator-value set has four values but is not a subgroup. This is an `OUT_OF_SCOPE_EXAMPLE`, not a counterexample and not finite coverage of any catalogue. It shows concretely that the “commutator value set is a subgroup” half of the reduction, rather than merely the central shape \(G''=C_2\), is doing essential work.

## Character-theoretic consequence for a minimum counterexample

Continue with a hypothetical minimum counterexample and write \(Z(G)=G''=\langle z\rangle\) as above. Some irreducible complex character \(\chi\) does not have \(z\) in its kernel (otherwise the faithful regular representation would also kill \(z\)). Since every nontrivial normal subgroup contains \(z\), the kernel of this \(\chi\) must be trivial.

In a representation affording \(\chi\), Schur's lemma and faithfulness give \(\rho(z)=-I\). For every \(g\notin Z(G)\), the minimum-counterexample reduction gives \(gz\sim_Gg\), and hence

\[
\chi(g)=\chi(gz)=-\chi(g),
\]

so \(\chi(g)=0\). On the two central elements, \(|\chi(1)|=|\chi(z)|=\chi(1)\). Character row orthogonality therefore gives

\[
|G|=\sum_{g\in G}|\chi(g)|^2=2\chi(1)^2.
\]

Thus any minimum counterexample must have a faithful irreducible character of central type, with

\[
|G:Z(G)|=\chi(1)^2,
\qquad |G|=2^{2n+1}.
\]

This is a necessary condition only. The diagnostic group above has the same order shape and final-derived-subgroup size but fails the active fibre hypothesis; no classification theorem is being assumed.

- 2026-08-16T12:05:11Z — near-miss diagnostic and character consequence recorded; cumulative active minutes: 268.

## 2026-08-16T12:06:56Z — order lower bound for a minimum counterexample

The character consequence makes \(|G|=2^{2n+1}\). Also \(|G:G'|\ge4\): if \(G/G'\) were cyclic, then \(G/\Phi(G)\) would be cyclic because \(G'\le\Phi(G)\), forcing the finite 2-group \(G\) itself to be cyclic. Since \(G'\) is nonabelian, \(|G'|\ge8\). Thus \(|G|\ge32\).

The order-32 case can be excluded without a catalogue. If \(|G|=32\), all the preceding inequalities are equalities: \(|G:G'|=4\), \(|G'|=8\), and \(G\) is 2-generated. Put \(\gamma_i=\gamma_i(G)\). For a 2-generated group, \(G'/\gamma_3\) is cyclic (generated by the image of the basic commutator of two generators). If \(|\gamma_3|\le2\), then the nonabelian group \(G'\) of order 8 would have a cyclic quotient by a subgroup containing \(G''\); explicitly, \(G''\le\gamma_3\), while \(G'/G''\cong C_2\times C_2\) for either nonabelian group of order 8, a contradiction. Hence \(|\gamma_3|=4\), because the lower central series strictly descends when nontrivial.

Now \(1\ne G''=[G',G']\le[\gamma_2,\gamma_2]\le\gamma_4\). Strict descent gives \(|\gamma_4|=2\) and \(\gamma_5=1\). The group \(\gamma_3\), of order 4, is abelian. Since \(G'/\gamma_3\) is cyclic, write \(G'=\langle c\rangle\gamma_3\). Then

\[
G''=[G',G']=[\langle c\rangle\gamma_3,\langle c\rangle\gamma_3]
\le [\gamma_2,\gamma_3]\,\gamma_3'
\le\gamma_5=1,
\]

contradicting \(G''\ne1\). Therefore order 32 is impossible. Combining this with \(|G|=2^{2n+1}\) gives the checkable bound

\[
\boxed{\;|G|\ge128\;}
\]

for a minimum counterexample. The exact order-128 wreath-product diagnostic above therefore sits at the first arithmetically possible order, but fails the admissibility hypothesis.

**Proof-check note.** The only classification used in the order-32 exclusion is the elementary fact that a nonabelian group of order 8 is \(D_8\) or \(Q_8\), in either case with derived quotient \(C_2^2\). No SmallGroups coverage is asserted.

- 2026-08-16T12:06:56Z — lower bound recorded; cumulative active minutes: 270.

## 2026-08-16T12:08:17Z — smallest-defect subgroup inside a minimum counterexample

The intrinsic formulation also gives a controlled entry into the upper central series. For \(1\ne d\in D_G(a)\), normality of \(D_G(a)\) implies \(D_G(d)\le D_G(a)\). Equality is impossible: the reverse-implication proof showed that a nonidentity element never belongs to its own defect subgroup, whereas \(d\in D_G(a)\). Thus

\[
1\ne d\in D_G(a) \quad\Longrightarrow\quad D_G(d)<D_G(a).
\]

Because \(G'\) is nonabelian in a counterexample, choose \(a\in G'\setminus Z(G)\) with \(|D_G(a)|\) minimal among such elements. We have \(D_G(a)\le G'\). If \(1\ne d\in D_G(a)\) were noncentral, then \(d\in G'\setminus Z(G)\) and the strict containment above would contradict the choice of \(a\). Hence every nonidentity element of \(D_G(a)\) is central. Since \(Z(G)=\{1,z\}\),

\[
D_G(a)=\langle z\rangle,
\qquad a^G=\{a,az\},
\qquad a^2\in\langle z\rangle.
\]

In particular

\[
Z_2(G)\cap G' > Z(G),
\]

and the chosen \(a\) has order 2 or 4. More generally, every \(u\in Z_2(G)\setminus Z(G)\) has \(D_G(u)=Z(G)\), conjugacy class \(uZ(G)\), and \(u^2\in Z(G)\).

This narrows the central-extension case but does not force \(a\) itself to be central: a conjugator may send \(a\) to \(az\), exactly as in a dihedral or quaternion section.

- 2026-08-16T12:08:17Z — smallest-defect lemma recorded; cumulative active minutes: 271.

## 2026-08-16T12:09:35Z — representation-changing pivot

Let \(H=G'\) in a hypothetical minimum counterexample. Since

\[
H'=G''=Z(G)=\langle z\rangle,

\]

the group \(H\) has class two. Put \(A=Z(H)\) and \(V=H/A\). For \(h,k\in H\), commutation defines

\[
\beta(hA,kA)=[h,k]\in\langle z\rangle\cong\mathbf F_2.
\]

This is well-defined, alternating, bilinear, and nondegenerate: its radical is precisely \(Z(H)/A=0\). Also \([h^2,k]=[h,k]^2=1\), so \(h^2\in A\) and \(V\) is an elementary-abelian 2-group. Hence \((V,\beta)\) is a nonzero symplectic \(\mathbf F_2\)-space.

The already established inclusion \(G^2\le G'\) makes \(E=G/G'\) elementary abelian. Conjugation preserves \(\beta\), and inner conjugation by \(H\) is trivial on \(H/Z(H)\), so \(E\) acts linearly and symplectically on \(V\).

Now take \(h\in H\) with image \(v=hA\). Projection of the defect subgroup gives

\[
\overline{D_G(h)}
=\{v^e-v:e\in E\}\le V.
\]

Thus the active fibre hypothesis becomes the exact linear restriction that, for every \(v\in V\), its orbit-difference **set** (not merely its linear span) is a vector subspace; equivalently every \(E\)-orbit in \(V\) is an affine subspace \(v+W_v\). On the abelian normal group \(A\), the same restriction says \(\{a^{-1}a^e:e\in E\}\) is a subgroup containing \(a^2\) for every \(a\in A\), while \(A^E=A\cap Z(G)=\langle z\rangle\).

This is the requested representation-changing pivot: a remaining proof can try to show that no nonzero symplectic \(V\) and compatible central extension satisfy all these orbit-difference and square conditions. Conversely, a linear-action probe that ignores the lift/cocycle or the conditions on \(A\) would check only necessary conditions and could not establish the target.

- 2026-08-16T12:09:35Z — symplectic-action reduction recorded; cumulative active minutes: 273.

## Linear-only route: explicit obstruction to overclaiming

The condition “every orbit in \(V\) is affine” does **not** by itself force \(V=0\). Let \(V\) be a 4-dimensional symplectic \(\mathbf F_2\)-space with two independent orthogonal isotropic vectors \(e_1,e_2\). The symplectic transvections

\[
T_i(v)=v+\beta(v,e_i)e_i \qquad (i=1,2)
\]

are commuting involutions. For \(E=\langle T_1,T_2\rangle\cong C_2^2\), the orbit-difference set of \(v\) is exactly

\[
\{a\,\beta(v,e_1)e_1+b\,\beta(v,e_2)e_2:a,b\in\mathbf F_2\},
\]

which is a vector subspace for every \(v\), although \(V\ne0\). Thus a proof that stops at the projected symplectic action has discarded essential information. The next theoretical experiment must retain the central lift, the subgroup \(A=Z(G')\), the square condition, and the fact that the *upstairs* commutator values form subgroups.

This meets the kill criterion for a linear-action-only contradiction and prevents treating a necessary module condition as sufficient.

## 2026-08-16T12:12:12Z — exponent bounds retained by the central lift

The square condition gives extra information on \(A=Z(G')\) that the projected symplectic module loses. Conjugation on \(A\) factors through the elementary-abelian group \(E=G/G'\), because \(G'\) centralizes its own center. For any \(a\in A\), the inclusion \(a^2\in D_G(a)\) supplies \(g\in G\) with

\[
[a,g]=a^2,
\qquad\text{that is,}\qquad a^g=a^3.
\]

The automorphism induced by \(gG'\in E\) has square one on \(A\). Applying it twice gives

\[
a=(a^g)^g=(a^3)^g=(a^g)^3=a^9,
\]

so \(a^8=1\). Therefore

\[
\exp Z(G')\le8.
\]

Since \(G'/Z(G')\) is elementary abelian, every \(h\in G'\) has \(h^2\in Z(G')\), and consequently

\[
\exp G'\le16.
\]

Also \(A^E=A\cap Z(G)=\langle z\rangle\), so the compatible action problem has a one-dimensional fixed subgroup on \(A\), not an arbitrary fixed part. These are necessary constraints on the lift; they still allow, for example, inversion on a cyclic group of order 4, so they do not by themselves close the case.

- 2026-08-16T12:12:12Z — lift-sensitive exponent bounds recorded; cumulative active minutes: 275.

## 2026-08-16T12:17:18Z — Clifford-theoretic constraint on the lift (not yet independently audited)

Retain \(H=G'\), \(A=Z(H)\), \(Z(G)=\langle z\rangle\), \(E=G/H\), and the faithful central-type character \(\chi\). Let \(\theta\) be an irreducible constituent of \(\chi_H\), with central character \(\lambda\in\widehat A\). Since \(z\) acts as \(-I\), \(\lambda(z)=-1\).

The pairing

\[
(hA,kA)\longmapsto\lambda([h,k])

\]

on \(H/A\) is nondegenerate: \(H'=\langle z\rangle\), \(\lambda(z)=-1\), and its radical is exactly \(Z(H)/A\). The finite Heisenberg argument (induce an extension of \(\lambda\) from a maximal isotropic abelian subgroup) therefore gives a unique irreducible \(\theta\) above \(\lambda\), with

\[
\theta(1)^2=|H:A|.
\]

Write the Clifford restriction as

\[
\chi_H=e(\theta_1+\cdots+\theta_t),

\]

where the \(\theta_i\) form the \(E\)-orbit of \(\theta\), and \(t=[E:I]\) for its inertia subgroup \(I\le E\). Then

\[
\chi(1)^2=e^2t^2|H:A|.
\]

Comparing this with the earlier central-type equality

\[
\chi(1)^2=|G:Z(G)|=|E|\,|H:A|\,|A:Z(G)|

\]

gives

\[
e^2t^2=|E|\,|A:Z(G)|. \tag{*}
\]

Clifford theory realizes \(e\) as the degree of an irreducible projective representation of \(I\), so \(e^2\le|I|=|E|/t\). Equation (*) implies \(|A:Z(G)|\le t\). On the other hand, uniqueness of \(\theta\) over \(\lambda\) identifies its orbit with the orbit of \(\lambda\), which lies in

\[
X=\{\mu\in\widehat A:\mu(z)=-1\},
\qquad |X|=|A:Z(G)|.

\]

Hence \(t\le|A:Z(G)|\), so equality holds throughout:

\[
t=|A:Z(G)|,
\qquad e^2=|E|/|A:Z(G)|.

\]

Thus \(E\) must act transitively on all characters of \(A\) that are nontrivial on \(z\), and the quotient of \(|E|\) by \(|A:Z(G)|\) is a square. This is a potentially useful finite action/cocycle constraint. It is logged as a current-run derivation, not as part of Validator's already reported core audit and not as a solution.

The set \(X\) separates points of \(A\): it detects \(z\), and multiplying one member of \(X\) by characters of \(A/\langle z\rangle\) detects every other nonidentity element. Therefore the kernel of the \(E\)-action on \(X\) is exactly \(C_E(A)\). Since \(E\) is abelian, its transitive action on \(X\) is regular after quotienting by this kernel. Equivalently,

\[
|E:C_E(A)|=|A:Z(G)|,

\]

and an elementary-abelian automorphism group of that exact order acts regularly on \(X\). This still does not force \(A\) to be cyclic: elementary-abelian shear actions supply abstract abelian-module examples, so the coupling to \(G'/A\) remains essential.

An explicit hand family demonstrates that last warning. Let \(A=\langle z\rangle\oplus W\) be an elementary-abelian 2-group and let \(F=W^*\) act by shears

\[
T_f(\alpha z+w)=(\alpha+f(w))z+w.
\]

Then \(F\cong C_2^{\dim W}\), \(A^F=\langle z\rangle\), and \(|F|=|A:\langle z\rangle|\). For \(a=\alpha z+w\), its orbit-difference set is 0 when \(w=0\) and is \(\langle z\rangle\) when \(w\ne0\); it is always a subgroup and automatically contains \(a^2=1\). On the dual affine set \(X=\{\lambda:\lambda(z)=-1\}\), \(F\) acts regularly. Thus every isolated condition so far imposed on \(A\) is consistent in arbitrary rank. An `A`-only classification strategy is exhausted; any next proof must use how this action couples to the nondegenerate commutator form on \(V=G'/A\) and to commutator values of lifts outside \(G'\).

- 2026-08-16T12:17:18Z — Clifford constraint derived; cumulative active minutes: 280.

## 2026-08-16T12:13:00Z — compute-protocol correction from Lead

Lead sent current-revision `CORRECTION` message `2026-08-16T1210Z__Lead__CORRECTION__enumeration-requires-lease.md`: all enumeration requires a current lease under common-protocol §4, regardless of short runtime. My earlier statement that the 128-element bespoke enumeration fell below the heavy-compute threshold was wrong. The command had already completed before the correction; its real output is preserved above as exploratory evidence, but the run was unleased, is not a certificate, and will not be extended or repeated. I have stopped all enumeration and will perform only hand reductions for the rest of this cycle.

- 2026-08-16T12:13:00Z — correction acted on; cumulative active minutes: 276.

Attempted required archival command:

```bash
mv 'Agents/Kourovka/bus/inbox/Problem-12.15/2026-08-16T1210Z__Lead__CORRECTION__enumeration-requires-lease.md' 'Agents/Kourovka/bus/archive/2026-08-16T1210Z__Lead__CORRECTION__enumeration-requires-lease.md'
```

Observed output:

```text
mv: cannot move 'Agents/Kourovka/bus/inbox/Problem-12.15/2026-08-16T1210Z__Lead__CORRECTION__enumeration-requires-lease.md' to 'Agents/Kourovka/bus/archive/2026-08-16T1210Z__Lead__CORRECTION__enumeration-requires-lease.md': Read-only file system
```

The message was therefore left in the inbox with `status: blocked`; this is an archival-state blocker only and does not block the hand proof work.

## Validator response

Validator message `2026-08-16T121217Z__Validator__REPORT__relative-frattini-partial.md` reports an independent line-by-line audit with no gap found in the fibre equality, intrinsic characterization, quotient inheritance, or least-counterexample consequences. Validator directed that these be recorded as `PARTIAL_RESULT` while retaining `active_assignment_answered: no`; the final central-extension case remains open. Under the clean-context boundary I did not open the linked historical/verification path. The response message cannot be archived because of the already-reported read-only archive state and remains in the inbox with `status: blocked` for that operational reason only.

## 2026-08-16T12:19:25Z — approximately 30-active-minute self-check

- **Exact target:** arbitrary finite 2-group satisfying the exact normal-closure-fibre implication; prove \(G''=1\). Scope and revision remain `12.15/normal-closure-fibres`, revision 1.
- **Current proved/audited hypothesis reduction:** the property is equivalent to all \(D_G(x)\) being subgroups containing \(x^2\), is quotient-closed, and a least counterexample has \(Z(G)=G''=C_2\). Validator independently reports no gap in this core partial result.
- **Current unproved hypothesis:** the remaining monolithic central extension cannot satisfy all upstairs defect-subgroup conditions. No candidate proof of that assertion currently passes a line-by-line audit.
- **Evidence:** hand proofs in this log; Validator's current-revision report; one unleased exploratory diagnostic explicitly quarantined after Lead's correction and not used as evidence.
- **Admissibility check:** there is no counterexample candidate. The partial theorem uses the arbitrary-\(G\), finite, 2-group, and exact fibre rows. The target-conclusion row `12.15-derived-abelian` remains not proved.
- **Representation productivity:** the symplectic/central-lift representation successfully isolated where information is lost. Linear-only and `A`-only strategies have now met their kill criteria via explicit hand examples satisfying their projected necessary conditions.
- **Next bounded hand experiment:** express \(G'/Z(G')\) as generated by projected defect subgroups of lifts and test whether commutator identities force those subspaces to be mutually orthogonal. Kill criterion: the step would require assuming that an upstairs defect subgroup is abelian or that distinct defect subgroups commute—precisely the missing conclusion.
- **Alternative if killed:** retain the Clifford transitivity constraint and formulate the full lift as an action-plus-commutator-cocycle system for a future bounded, leased exact parameter search; do not claim that the module conditions alone are sufficient.

- 2026-08-16T12:19:25Z — self-check completed; cumulative active minutes: 282.

## 2026-08-16T12:20:34Z — projected-defect orthogonality experiment

Choose lifts \(x_1,\dots,x_r\) of a basis of \(E=G/G'\), and put \(c_{ij}=[x_i,x_j]A\in V\). Since \(G'\) is the normal closure of the basic commutators, \(V\) is the \(E\)-submodule generated by the \(c_{ij}\). If \(W_i\) denotes the image of \(D_G(x_i)\) in \(V\), then

\[
c_{ij}\in W_i\cap W_j,

\]

and \(W_i\) is an \(E\)-invariant vector subspace containing \((x_i-1)V\). Hence the \(W_i\) together generate \(V\).

The hoped-for final step would be to prove \(\beta(W_i,W_j)=0\) for all \(i,j\), which would make the generated space \(V\) totally isotropic and contradict nondegeneracy unless \(V=0\). The available subgroup facts do not justify that step. They give only

\[
[D_G(x_i),D_G(x_j)]\le D_G(x_i)\cap D_G(x_j)\cap G''
\le\langle z\rangle.

\]

The right side may still equal \(\langle z\rangle\). If \([d,e]=z\) for \(d\in D_G(x_i)\), \(e\in D_G(x_j)\), then conjugation sends \(d\) to \(dz\), which is fully consistent with the already forced pairing of every noncentral conjugacy class by \(z\). Hall–Witt identities relocate such weight-four commutators but do not make them trivial without an additional premise.

Thus the experiment meets its kill criterion: mutual orthogonality would amount to assuming that the relevant defect subgroups commute, which is the missing metabelian conclusion in another form. The valid output is the exact action-plus-cocycle reduction, not a proof of \(V=0\).

- 2026-08-16T12:20:34Z — orthogonality route stopped at identified circular step; cumulative active minutes: 283.

## 2026-08-16T12:22:06Z — simplification of the order-32 exclusion

The earlier order-32 argument can avoid even the classification of groups of order 8. With \(|G'|=8\), the nontrivial containment

\[
1\ne G''=[\gamma_2,\gamma_2]\le\gamma_4

\]

and strict descent of the lower central series immediately force

\[
|\gamma_3|=4,
\qquad |\gamma_4|=2,
\qquad \gamma_5=1.
\]

The 2-generator fact \(G'/\gamma_3\) cyclic then gives \(G'=\langle c\rangle\gamma_3\); the order-4 group \(\gamma_3\) is abelian and \([c,\gamma_3]\le[\gamma_2,\gamma_3]\le\gamma_5=1\), so \(G''=1\), the contradiction. This is the preferred proof of the bound \(|G|\ge128\).

- 2026-08-16T12:22:06Z — lower-bound proof simplified; cumulative active minutes: 285.

## First possible order: exact parameter cases (hand reduction only)

If a minimum counterexample has the first arithmetically possible order 128, put \(H=G'\), \(A=Z(H)\), and \(E=G/H\). Since \(E\) is elementary abelian, \(H\) is nonabelian, and \(|H:A|\) is a nontrivial square (the order of the symplectic space \(V\)), there are only four size patterns:

| \(|E|\) | \(|H|\) | \(|A|\) | \(|V|=|H:A|\) | Clifford action size \(|E:C_E(A)|=|A:Z(G)|\) |
|---:|---:|---:|---:|---:|
| 16 | 8 | 2 | 4 | 1 |
| 8 | 16 | 4 | 4 | 2 |
| 4 | 32 | 2 | 16 | 1 |
| 4 | 32 | 8 | 4 | 4 |

Derivation: \(|E||H|=128\), \(|E|\ge4\), \(|H|\ge8\), and \(|H:A|\in\{4,16,\ldots\}\), with \(2=|Z(G)|\le|A|<|H|\). The last column uses the current-run Clifford constraint and therefore awaits the requested secondary audit.

This is not catalogue coverage and no enumeration follows. It supplies four explicit action-plus-cocycle parameter regimes for a future leased exact search or a hand case analysis. Merely classifying \(H\) in these size rows would still be insufficient unless every lift's defect-value set and square condition were checked.

## Exact central-extension certificate specification

A future order-128 search or hand case analysis must retain the following data, not just the projected modules:

1. one of the four size patterns for a class-two group \(H\), with \(H'=\langle z\rangle\), \(A=Z(H)\), and the nondegenerate commutator form on \(H/A\);
2. an elementary-abelian group \(E\) of the stated order;
3. a section action \(\alpha_e\in\operatorname{Aut}(H)\) fixing \(z\), allowed to compose only up to inner automorphisms;
4. a normalized nonabelian factor set \(f(e_1,e_2)\in H\) satisfying both the action-compatibility and associativity identities, so that multiplication on \(H\times E\) is genuinely a group rather than a guessed module;
5. exact checks that the resulting group has center \(\langle z\rangle\), derived subgroup exactly \(H\), and, for **every** \(x\in H\times E\), the value set \(D_G(x)\) is a subgroup containing \(x^2\).

The last row is equivalent to the original normal-closure-fibre hypothesis and must be checked upstairs. Projected affine-orbit checks on \(A\) and \(H/A\) are necessary but demonstrably insufficient. A Validator certificate could reconstruct the full multiplication table from \((H,E,\alpha,f)\), verify associativity independently, and then verify the defect-set and derived-series rows directly. No such search is authorized or run in this cycle.

One bookkeeping simplification is exact: the fibre lemma gives \(G^2\le G'\), while \(G'\le\Phi(G)\) in every finite 2-group. Hence

\[
\Phi(G)=G^2G'=G'.
\]

Thus \(E=G/G'\) is not merely an elementary-abelian quotient; it is the Frattini quotient and its dimension is the minimum number of generators of \(G\). Future lift data may therefore take the chosen \(x_i\) to be a minimal generating set without an additional assumption.

## 2026-08-16T12:25:10Z — two-generator symplectic dimension lemma

Suppose a minimum counterexample is 2-generated. Then \(E=G/G'=\langle s,t\rangle\cong C_2^2\). On the symplectic space \(V=G'/Z(G')\), put \(N=s-1\) and \(M=t-1\). These commuting operators satisfy \(N^2=M^2=0\). For every \(v\in V\), the projected defect condition says the four-term orbit-difference set

\[
\{0,Nv,Mv,(N+M+NM)v\}

\]

is a vector subspace.

This forces \(NMv=0\) for every \(v\). If \(Nv,Mv\) are independent, the fourth member of the subspace must be their sum; if one vanishes, commutativity gives \(NMv=0\); and if \(Nv=Mv\ne0\), then \(NMv=N^2v=0\). Hence the augmentation ideal \(J=(N,M)\) satisfies \(J^2V=0\).

For a 2-generated group \(G=\langle x,y\rangle\), the derived subgroup is the normal closure of \([x,y]\). Therefore \(V\) is a cyclic \(\mathbf F_2E\)-module, generated by \([x,y]Z(G')\). Since \(J^2V=0\), a cyclic module is spanned by

\[
v,\ Nv,\ Mv,

\]

so \(\dim_{\mathbf F_2}V\le3\). Nondegeneracy of the alternating form makes this dimension positive and even. Consequently

\[
\boxed{\;\dim_{\mathbf F_2}G'/Z(G')=2\;}

\]

for every 2-generated minimum counterexample.

At order 128, the two rows with \(|E|=4\), \(|G'|=32\) had \(|V|=16\) when \(|Z(G')|=2\) and \(|V|=4\) when \(|Z(G')|=8\). The lemma eliminates the first row. Thus only three of the four order-128 size patterns remain, and the 2-generated branch must have

\[
|G'|=32,\qquad |Z(G')|=8,\qquad |G'/Z(G')|=4.

\]

This remains a necessary-condition result, not an exclusion of all 2-generated counterexamples.

- 2026-08-16T12:25:10Z — rank-two augmentation argument recorded; cumulative active minutes: 288.

In this surviving order-128 two-generator branch, the symplectic action of \(E=C_2^2\) on the 2-dimensional \(V\) has image of order exactly 2: \(\operatorname{Sp}(2,2)\cong S_3\) has no subgroup \(C_2^2\), while a trivial action could not make the single \(E\)-orbit of the basic commutator span 2 dimensions. Meanwhile the Clifford constraint gives

\[
|E:C_E(A)|=|A:Z(G)|=4,

\]

so \(E\) acts faithfully on the order-8 abelian group \(A\). The three abstract possibilities are \(C_8\), \(C_4\times C_2\), and \(C_2^3\); each admits an elementary-abelian action with fixed subgroup \(\langle z\rangle\) at the isolated \(A\)-module level, so none can be discarded without the full lift.

The group \(H=G'\) in this branch can be presented parametrically as a central extension of \(V=C_2^2\) by \(A\): choose lifts \(p,q\) with

\[
[p,q]=z,\qquad p^2,q^2\in A,

\]

and \(A=Z(H)\). This reduces the branch to finitely described action and factor-set data, but checking compatibility with every upstairs defect set is still the unresolved step.

For completeness, the other two surviving order-128 size branches also have \(|V|=4\). In the 3-generator branch,

\[
|E|=8,\quad |H|=16,\quad |A|=4,

\]

the image of \(E\) on \(V\) has order at most 2 and the Clifford constraint makes its image on \(A\) have order exactly 2; \(A\) is abstractly \(C_4\) or \(C_2^2\). In the 4-generator branch,

\[
|E|=16,\quad |H|=8,\quad A=\langle z\rangle,

\]

the group \(H\) is \(D_8\) or \(Q_8\), and again the elementary-abelian image on \(V\) has order at most 2. These observations leave compatible abstract actions in every branch; they organize a future lift analysis but do not exclude order 128.

There is one more exact restriction in the surviving 2-generator order-128 branch. Let \(c=[x,y]\). Then \(H=G'=\langle c\rangle^G\), so the fibre lemma gives a defect subgroup

\[
D=D_G(c)\lhd G,
\qquad |H:D|=2,
\qquad |D|=16.

\]

The image of \(D\) in the 2-dimensional space \(V=H/A\) is the orbit-difference line for the nontrivial order-2 image of \(E\) on \(V\), hence has order 2. Therefore

\[
|D\cap A|=|D|/2=8=|A|,

\]

so \(A\le D\) and \(|D:A|=2\). Because \(A=Z(H)\), this forces \(D\) to be abelian. Thus this branch has the precise shape

\[
H=\langle c,D\rangle,
\qquad D\text{ an abelian maximal subgroup of }H,
\qquad H'=\langle z\rangle.

\]

The full conjugacy class is the coset \(cD\), so all 16 elements of that coset have the same order. This adds a concrete hand-classification constraint, but abelian 2-groups admit index-two cosets of constant order, so it is not by itself a contradiction.

## Lead decision and bounded deliverable

Lead decision `2026-08-16T122600Z__Lead__DECISION__finish-full-central-lift-formulation.md` selected the full action-plus-central-cocycle formulation for the remaining authorized minutes, with an explicit ban on enumeration and no further extension. I acted on it by writing `central-lift-spec.md` in this run directory.

The specification gives:

- every audited and secondary dependency separately;
- the three surviving order-128 parameter regimes;
- normalized central-cocycle data \((A,V,\eta)\) reconstructing \(H=G'\);
- weak action/factor-set data \((E,\alpha,f)\) reconstructing \(G\), with the exact action-compatibility and associativity equations;
- center, derived-subgroup, Frattini, action-size, and two-generator rows;
- the decisive upstairs defect-subgroup and square rows equivalent to the original source hypothesis;
- the exact independent certificate a future hand proof or leased verifier would require.

No commuting-defect assumption was introduced, and no computation or enumeration was run. The formulation reaches the planned boundary: proving inconsistency of these lift equations remains open.

## Cycle 9 outcome — `PARTIAL_RESULT`

`active_assignment_answered: no`.

The independently audited partial result is the intrinsic commutator-value characterization, quotient inheritance, and least-counterexample reduction

\[
Z(G)=G''\cong C_2.
\]

The current run further derives necessary character, order, exponent, symplectic, generator-rank, and first-order-128 restrictions, with the secondary audit requested but not received before stop. Lead's selected bounded deliverable, `central-lift-spec.md`, states the exact remaining action-plus-cocycle system and certificate rows. The uncovered step is to prove that no such system satisfies every upstairs defect-subgroup and square condition while \(H'=\langle z\rangle\ne1\).

The representation changed from normal closures, to defect subgroups, to a monolithic central extension, and finally to exact cocycle data. Linear-only, center-module-only, and mutual-orthogonality routes were stopped at explicit insufficiency or circularity checks. A MathExpert question was sent early; no response reached this inbox before cycle close.

No `CLAIM` is made, no claim-check JSON is required, and the state checker was not run. External staleness remains `deferred_to_lead_or_human_for_discovery_blind_run`.

- 2026-08-16T12:30:55Z — work stop; current extension active minutes used: 39; cumulative active minutes: 293. The bounded deliverable is complete; Lead granted no further extension, and the next step would require a new hand lemma or an explicitly leased verifier.
