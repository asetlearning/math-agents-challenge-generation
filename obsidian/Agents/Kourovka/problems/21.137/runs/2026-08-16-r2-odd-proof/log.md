---
title: "Problem-agent log: 21.137 odd-prime exponent-p-squared proof, revision 2"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/draft
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
context_mode: clean
discovery_blind: true
---

# Cycle 1 working log

## Active-time ledger

- 2026-08-16T11:51:20Z — work start; cumulative active minutes: 0. Began mandatory protocol, scope, source, and staleness audit.
- 2026-08-16T12:20:38Z — cumulative active minutes: 29 (approximately 30); continuous source audit, theory, writing, and supervised inspection. No waiting time deducted yet.
- 2026-08-16T12:50:19Z — cumulative active minutes: 59 (approximately 60); continuous hand research, review processing, and certificate writing. No reviewer-wait time was charged separately because other active work continued.
- 2026-08-16T12:54:47Z — work stop; cumulative active minutes: 63. Lead ordered the accepted proof-direction partial packaged and this representation stopped; no new strategy was started.

## Staleness check

### 2026-08-16T11:52:10Z — source and scope gate

- Read `_meta/agents/Kourovka/_common-kourovka.md` in full, then the canonical revision-2 scope record, then the clean-context safe brief. Did not inspect the ordinary synthesis, historical log/findings, verification note, archived messages, transcripts, or historical scratch.
- Current inbox `Agents/Kourovka/bus/inbox/Problem-21.137/` contained no files.
- Sourced `_meta/agents/Kourovka/paths.env`: the configured PDF resolves; `KOUROVKA_AUTHOR=operator`.
- Read PDF page 184 with `pdftotext`, rendered that page at 180 dpi with `pdftoppm`, and visually inspected the rendered page. The visual check, rather than the text extraction, controls the transcription below.
- The expected issue-21 JSONL corpus record is not present in this checkout: the configured path `Research/Group theory/Open problems/Kourovka/corpus/kourovka-21-corpus.jsonl` does not exist, the corpus directory only exposes issue files through issue 20, and an exact search for `21.137` under that corpus directory returned no match. Therefore no machine-readable `answered`, `has_editor_comment`, or `has_later_comment` fields were available to inspect. On the rendered 2026 issue-21 source page, problem 21.137 has no answer asterisk, no editor comment, and no later comment after the proposer line.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`. Per the assignment, I did not use the open web, arXiv, later editions, or solution-bearing local artifacts.
- The canonical record says the independent scope audit is required and has status `passed`, with auditor `Validator`, at revision 2. I did not open its verification note because that path is excluded from this clean run.
- `source_transcription_checked: yes`
- `active_scope_checked: yes`

### Corrected source transcription

> **21.137.** If the \(p\)-th powers in a finite \(p\)-group form a subgroup, must that subgroup be powerful? That is, for \(p\ne 2\), if the \(p\)-th powers in a \(p\)-group of exponent \(p^2\) form a subgroup, must that subgroup be abelian? For a 2-group of exponent 8, if the squares form a subgroup, must that subgroup be abelian? — L. Wilson

The rendered exponent is \(p^2\), not `p2`. The active clause is only the middle, odd-prime clause. Finiteness is inherited from the opening sentence and is explicit in the canonical target. “The \(p\)-th powers” means the actual word-value set \(\{g^p:g\in G\}\), not merely its generated verbal subgroup.

### Clause matrix

| source clause | equivalent formulation | in active scope? | literature/staleness status in this run |
|---|---|---:|---|
| If the \(p\)-th powers in a finite \(p\)-group form a subgroup, must it be powerful? | General powerfulness question. For odd \(p\), powerful means \([P,P]\le P^p\); in the exponent-\(p^2\) specialization every element of \(P\) has order dividing \(p\), so powerfulness reduces to abelianness. | No; context only. | External check deferred; no source-page answer/comment. |
| For \(p\ne2\), if the \(p\)-th powers in a finite \(p\)-group of exponent \(p^2\) form a subgroup, must that subgroup be abelian? | For each odd prime \(p\) and finite exponent-exactly-\(p^2\) group \(G\), closure of \(P=\{g^p:g\in G\}\) under the group law should imply \([P,P]=1\). | **Yes:** `21.137/odd-prime-exponent-p2`. | External check deferred; no source-page answer/comment. |
| For a 2-group of exponent 8, if the squares form a subgroup, must it be abelian? | Separate \(p=2\), exponent-8 square-set clause. | No; explicitly excluded. | External check deferred; no source-page answer/comment. |

No source/scope mismatch was found. In particular, the canonical constraints preserve the odd-prime restriction, finiteness, exact exponent \(p^2\), actual power-value set, subgroup hypothesis, and abelian conclusion.

### Admissibility and conclusion checklist

| constraint_id | source requirement | proof obligation in this run | reconciliation |
|---|---|---|---|
| `21.137-odd-forall-p-G` | Universal question over the qualifying \(p,G\). | Do not prove only a fixed prime, bounded order, class, or family without labeling it partial. | Matches source/canonical target. |
| `21.137-odd-p-not-2` | \(p\ne2\), with \(p\) prime. | Every identity must be valid for all odd primes, including \(p=3\). | Matches. |
| `21.137-odd-finite-p-group` | \(G\) is a finite \(p\)-group. | Any minimal-counterexample or induction argument may use finiteness; no infinite surrogate may be identified with the target. | Matches. |
| `21.137-odd-exponent-p2` | \(\exp(G)=p^2\). | Use both the upper bound \(g^{p^2}=1\) and existence of an element of order \(p^2\); an exponent-dividing-\(p^2\) lemma alone covers a larger class but does not by itself encode exactness. | Matches. |
| `21.137-odd-power-set-definition` | \(P\) is exactly \(\{g^p:g\in G\}\). | Preserve word-value surjectivity; never replace the hypothesis by statements only about \(G^p=\langle g^p:g\in G\rangle\). | Matches. |
| `21.137-odd-power-set-subgroup` | The actual value set \(P\) is a subgroup. | Translate closure and inverses exactly; inverses are automatic because \((g^p)^{-1}=(g^{-1})^p\), while product closure is substantive. | Matches. |
| `21.137-odd-P-abelian` | \(P\) is abelian. | Establish \([x^p,y^p]=1\) for arbitrary \(x,y\in G\). | Matches. |

## Strategy portfolio

### 2026-08-16T11:52:10Z — ranked before mathematical work

1. **Theoretical mode — minimal nonabelian power subgroup plus Hall–Petrescu.** Assume \(P\) is a subgroup and seek exact consequences of product-surjectivity: for every \(x,y\) there is \(z\) with \(z^p=x^p y^p\). Combine this with exponent \(p^2\), quotients, and commutator collection to force \([x^p,y^p]=1\). First target is a rigorously stated reduction rather than a full collection formula. Kill criterion: 30 active minutes without a checkable identity or a well-defined minimal-counterexample quotient.
2. **Structured-construction/reparametrisation mode — associated graded or class-2/3 Lie model.** Express the \(p\)-power map as a linear/quadratic map on a central series; translate “its image is a subgroup” into closure of a polynomial image, and see whether nonzero brackets on that image are impossible. This can either prove a structural family or expose the precise high-class obstruction. Kill criterion: the model silently assumes class \(<p\), regularity, or central powers and therefore loses the full scope without yielding a certified partial lemma.
3. **Catalogue/small-case mode — bounded GAP probe at odd primes.** Check selected SmallGroups or finitely presented families at \(p=3\) for exact exponent 9, equality of the actual cube-value set with a subgroup, and abelianness. A negative bounded search would establish only finite coverage at named orders/library identifiers, never the universal statement. Use only a bounded sub-60-second probe unless Lead grants a heavy-compute lease. Kill criterion: library coverage or runtime grows without producing an informative near miss or testing a proposed identity.
4. **Certificate plan.** A successful proof must be line-by-line, with every commutator convention and collection identity stated and independently checkable, and it must include \(p=3\). A structural-family partial result needs a precise theorem with hypotheses. A computation needs exact GAP version, commands, group identifiers/presentations, coverage bounds, and a second reconstruction route that does not trust the discovery script.

Expected information per active hour ranks 1, then 2, then 3. The cheapest certifiable first experiment is to isolate quotient-closure and commutator consequences of the actual-value-set hypothesis before enumerating groups.

## Working reductions and bounded probes

### 2026-08-16T11:53:25Z — early review questions sent

- Sent a fresh-proof question to MathExpert asking for exact closure-to-commutator lemmas valid at \(p=3\).
- Sent Validator a certificate-design question about a structural-family partial result. Both messages identify the clean-context boundary and revision 2.

### 2026-08-16T12:00:56Z — elementary reduction from value-set closure

Let \(P=\{g^p:g\in G\}\), assumed to be a subgroup.

1. Then \(P=G^p\), where the right side is the verbal subgroup generated by all \(p\)-th powers: one inclusion is true by definition and the reverse follows because \(P\) is already a subgroup containing all values.
2. Every \(u\in P\) has \(u^p=1\), since \(u=g^p\) and \(g^{p^2}=1\). Thus \(\exp(P)\mid p\). Exact exponent of \(G\) supplies a nontrivial \(p\)-th power, so in fact \(\exp(P)=p\).
3. Therefore the active conclusion is exactly the remaining assertion \([G^p,G^p]=1\) under the stronger, value-set-derived fact \(\exp(G^p)=p\). This does not follow merely because the generators \(g^p\) individually have order \(p\): products of order-\(p\) elements can have larger order, and nonabelian exponent-\(p\) groups exist.

**Quotient inheritance.** If \(N\unlhd G\), the actual power-value set in \(G/N\) is
\[
\{(gN)^p:g\in G\}=PN/N,
\]
so it remains a subgroup. Moreover \(\exp(G/N)=p\) exactly when \(P\le N\); if \(P\not\le N\), the quotient still has exponent exactly \(p^2\). This is an exact use of the actual value set, not a replacement by a generated subgroup.

**Minimal-counterexample consequence under development.** If a counterexample of minimal order exists, take an order-\(p\) subgroup \(C\le P'\cap Z(G)\), which exists because \(P'\ne1\) is normal in the finite \(p\)-group \(G\). Since \(P\not\le C\), \(G/C\) retains exact exponent \(p^2\) and has power-value subgroup \(P/C\). Minimality makes \(P/C\) abelian, hence \(P'\le C\), while \(C\le P'\); consequently
\[
P'=C\cong C_p\quad\text{and}\quad P'\le Z(G).
\]
This is a genuine reduction if every quotient step and the stronger central uniqueness consequence survive checking; it is not yet being reported as a final claim.

### 2026-08-16T11:58:19Z — bounded SmallGroups probe

Created `scratch/scan-small-3groups.g`. The final command was:

```bash
timeout 55s gap -q 'Agents/Kourovka/problems/21.137/runs/2026-08-16-r2-odd-proof/scratch/scan-small-3groups.g'
```

The run completed with exit code 0 in 2.8 seconds. Verbatim final output:

```text
GAP_VERSION=4.12.1
ORDER=9 TOTAL=2 EXPONENT_9=1 POWER_SET_SUBGROUP=1 NONABELIAN_POWER_SUBGROUP=0 NONABELIAN_GENERATED_POWER=0 NONCLOSED_NONABELIAN_GENERATED_POWER_EXP3=0 CLASS_COUNTS=[ 1 ]
ORDER=27 TOTAL=5 EXPONENT_9=2 POWER_SET_SUBGROUP=2 NONABELIAN_POWER_SUBGROUP=0 NONABELIAN_GENERATED_POWER=0 NONCLOSED_NONABELIAN_GENERATED_POWER_EXP3=0 CLASS_COUNTS=[ 1, 1 ]
ORDER=81 TOTAL=15 EXPONENT_9=10 POWER_SET_SUBGROUP=10 NONABELIAN_POWER_SUBGROUP=0 NONABELIAN_GENERATED_POWER=0 NONCLOSED_NONABELIAN_GENERATED_POWER_EXP3=0 CLASS_COUNTS=[ 2, 4, 4 ]
ORDER=243 TOTAL=67 EXPONENT_9=49 POWER_SET_SUBGROUP=39 NONABELIAN_POWER_SUBGROUP=0 NONABELIAN_GENERATED_POWER=0 NONCLOSED_NONABELIAN_GENERATED_POWER_EXP3=0 CLASS_COUNTS=[ 2, 19, 12, 6 ]
ORDER=729 TOTAL=504 EXPONENT_9=401 POWER_SET_SUBGROUP=260 NONABELIAN_POWER_SUBGROUP=0 NONABELIAN_GENERATED_POWER=0 NONCLOSED_NONABELIAN_GENERATED_POWER_EXP3=0 CLASS_COUNTS=[ 3, 94, 139, 24 ]
SUMMARY EXPONENT_9=463 POWER_SET_SUBGROUP=312 NONABELIAN_POWER_SUBGROUP=0
```

The script enumerates every GAP SmallGroups library group of orders \(3^2,\dots,3^6\), retains exact exponent 9, constructs the actual cube-value set by evaluating every element, constructs the subgroup generated by that set, and declares set closure exactly when the two cardinalities agree. Within this explicitly bounded catalogue, 463 groups have exponent exactly 9, 312 have a cube-value set that is a subgroup, and all 312 resulting subgroups are abelian. In fact the generated cube subgroup is abelian for all 463 in this bound.

What this proves, subject to independent rerun/library trust: no counterexample occurs for \(p=3\) and \(|G|\le729\). What it does **not** prove: anything at larger order, any other odd prime, or the universal assertion. The first version omitted order 9 and wrapped output; it was corrected and rerun. No output from the superseded run is used in the coverage total.

### Tool availability note

I checked whether GAP's `nq` or `anupq` packages were available for symbolic free-nilpotent collection. Both package loads returned `fail`, and the core session had neither `FreeNilpotentGroup` nor `NilpotentQuotient` bound. I am not reimplementing either package and do not treat it as a blocker: the active theoretical reductions and bounded SmallGroups checks do not require it. No symbolic output was inferred from the missing tools.

### 2026-08-16T12:05:50Z — independent direct-set verification through order 2000

Created `scratch/verify-all-odd-pgroups-order-le-2000.g`. Unlike the first script, this implementation does not infer closure by comparing a generated subgroup's size and does not call `IsAbelian` on that subgroup. It:

- independently checks exponent exactly \(p^2\) by evaluating \(x^{p^2}=1\) for every element and requiring at least one \(x^p\ne1\);
- forms the actual value set element-by-element;
- tests every product of two values for membership in that set;
- tests every ordered pair of values for commutation;
- mechanically checks that its hard-coded order list equals every odd prime-power order at most 2000.

Final command:

```bash
timeout 55s gap -q 'Agents/Kourovka/problems/21.137/runs/2026-08-16-r2-odd-proof/scratch/verify-all-odd-pgroups-order-le-2000.g'
```

It completed with exit code 0 in 3.1 seconds. Verbatim output:

```text
GAP_VERSION=4.12.1
COVERAGE_AUDIT=all_odd_prime_power_orders_le_2000 ORDERS=[ 9, 25, 27, 49, 81, 121, 125, 169, 243, 289, 343, 361, 529, 625, 729, 841, 961, 1331, 1369, 1681, 1849 ]
P=3 ORDER=9 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
P=3 ORDER=27 TOTAL=5 EXPONENT_P2=2 POWER_SET_SUBGROUP_DIRECT=2 NONABELIAN_DIRECT=0
P=3 ORDER=81 TOTAL=15 EXPONENT_P2=10 POWER_SET_SUBGROUP_DIRECT=10 NONABELIAN_DIRECT=0
P=3 ORDER=243 TOTAL=67 EXPONENT_P2=49 POWER_SET_SUBGROUP_DIRECT=39 NONABELIAN_DIRECT=0
P=3 ORDER=729 TOTAL=504 EXPONENT_P2=401 POWER_SET_SUBGROUP_DIRECT=260 NONABELIAN_DIRECT=0
P=5 ORDER=25 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
P=5 ORDER=125 TOTAL=5 EXPONENT_P2=2 POWER_SET_SUBGROUP_DIRECT=2 NONABELIAN_DIRECT=0
P=5 ORDER=625 TOTAL=15 EXPONENT_P2=9 POWER_SET_SUBGROUP_DIRECT=9 NONABELIAN_DIRECT=0
P=7 ORDER=49 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
P=7 ORDER=343 TOTAL=5 EXPONENT_P2=2 POWER_SET_SUBGROUP_DIRECT=2 NONABELIAN_DIRECT=0
P=11 ORDER=121 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
P=11 ORDER=1331 TOTAL=5 EXPONENT_P2=2 POWER_SET_SUBGROUP_DIRECT=2 NONABELIAN_DIRECT=0
P=13 ORDER=169 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
P=17 ORDER=289 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
P=19 ORDER=361 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
P=23 ORDER=529 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
P=29 ORDER=841 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
P=31 ORDER=961 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
P=37 ORDER=1369 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
P=41 ORDER=1681 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
P=43 ORDER=1849 TOTAL=2 EXPONENT_P2=1 POWER_SET_SUBGROUP_DIRECT=1 NONABELIAN_DIRECT=0
SUMMARY EXPONENT_P2=490 POWER_SET_SUBGROUP_DIRECT=339 NONABELIAN_DIRECT=0
```

This independently reproduces the first script's \(p=3\) counts and expands the exact finite coverage: among all odd-prime groups of order at most 2000, 490 have exact exponent \(p^2\), 339 satisfy the actual-value-set subgroup hypothesis, and none of those 339 has a nonabelian value set. The uncovered scope is every qualifying group of order greater than 2000. The result depends on GAP's SmallGroups catalogue and the scripts, so it remains computational evidence until Validator independently reruns or reconstructs it.

### 2026-08-16T12:08:34Z — Hall-polynomial low-class exclusion (candidate lemma)

**Candidate lemma.** Let \(p\) be prime and let \(G\) have exponent dividing \(p^2\) and nilpotency class at most \(p\). Then
\[
[x^p,y^p]=1\qquad(x,y\in G).
\]
Thus the subgroup generated by the \(p\)-th powers is abelian even without assuming that the value set is a subgroup.

**Collection argument to be checked.** Work first in the torsion-free free nilpotent group \(N_{2,c}\) of class \(c\le p\) on \(x,y\), with a Hall basis. For a basic commutator \(b\) containing \(r\ge1\) copies of \(x\) and \(s\ge1\) copies of \(y\), its Mal'cev-coordinate exponent in the collected form of \([x^m,y^n]\) is an integer-valued polynomial \(f_b(m,n)\) of bidegree at most \((r,s)\). The whole commutator is the identity if \(m=0\) or \(n=0\); uniqueness of collected coordinates therefore gives \(f_b(0,n)=f_b(m,0)=0\). Expanding an integer-valued polynomial in the binomial basis gives
\[
f_b(m,n)=\sum_{i=1}^{r}\sum_{j=1}^{s}
             a_{ij}\binom mi\binom nj,
\qquad a_{ij}\in\mathbb Z.
\]
Because \(r+s\le c\le p\) and both are positive, \(r,s\le p-1\). For \(1\le i,j\le p-1\), each of \(\binom pi,\binom pj\) is divisible by \(p\); hence every \(f_b(p,p)\) is divisible by \(p^2\). Mapping the free nilpotent group to \(\langle x,y\rangle\le G\), every collected basic-commutator factor is consequently raised to a multiple of \(p^2\), and it vanishes under the exponent assumption.

The point requiring independent scrutiny is the standard Hall-polynomial assertion that the coordinate belonging to multidegree \((r,s)\) has the stated separate degree bounds and integral binomial-basis coefficients. I have not replaced this with a citation or a computer output. If that collection fact is accepted, the lemma is a line-by-line reduction.

**Elementary class-3 cross-check.** For class at most 3, the same result follows without the general Hall-polynomial language. With weight-3 commutators central, collection gives, up to convention-dependent inversion of the named commutators,
\[
[x^p,y]=[x,y]^p[x,y,x]^{\binom p2},\qquad
[x^p,y,y]=[x,y,y]^p,
\]
and
\[
[x^p,y^p]=[x^p,y]^p[x^p,y,y]^{\binom p2}.
\]
All resulting exponents are either \(p^2\) or \(p\binom p2\). For odd \(p\), \(p\binom p2\) is divisible by \(p^2\), so exponent \(p^2\) kills every factor.

**Consequences if the general collection step passes review.** A counterexample must have nilpotency class at least \(p+1\). Since a finite \(p\)-group of class \(c\ge2\) has order at least \(p^{c+1}\), it must have
\[
|G|\ge p^{p+2}.
\]
For \(p=3\), the independent catalogue exclusion through \(3^6=729\) improves the numerical lower bound to \(|G|\ge3^7=2187\). These are necessary conditions only, not evidence that a counterexample exists at either boundary.

**First uncontrolled collection layer.** The binomial-divisibility proof stops sharply at weight \(p+1\): a basic commutator of multidegree \((p,1)\) can receive a term \(\binom pp\binom p1=p\), not \(p^2\). Thus “continue the same collection argument” is not a live proof strategy unless closure of the actual value set supplies a new relation killing these unbalanced weight-\((p+1)\) terms.

### 2026-08-16T12:12:56Z — minimal quotient and root-action lower bound

This route uses the full actual-value hypothesis rather than only low-class collection.

#### Step A: reduce any counterexample to a quotient-minimal one

Suppose \(G\) is a counterexample, and choose a quotient \(H\) of \(G\) of smallest order whose actual \(p\)-power set \(Q\) is still a nonabelian subgroup. Quotient inheritance above shows that \(H\) is again a finite \(p\)-group of exact exponent \(p^2\): nonabelian \(Q\) cannot be contained in the quotient kernel, so some \(p\)-th power remains nontrivial. We may therefore work in \(H\), where every proper quotient having nonabelian power image is forbidden by minimality.

The set \(Q\) equals \(H^p\) and has exponent \(p\). Its nontrivial derived subgroup \(Q'\) is normal in \(H\). Choose \(C\le Q'\cap Z(H)\) with \(|C|=p\). The quotient \(H/C\) retains exact exponent \(p^2\), its actual power set is \(Q/C\), and minimality forces \(Q/C\) abelian. Hence
\[
Q'=C\cong C_p,\qquad C\le Z(H).
\]
In particular \(Q\) has nilpotency class exactly 2.

If \(D\le Z(H)\) also has order \(p\) and \(D\ne C\), then \(H/D\) retains exact exponent \(p^2\), and its power subgroup \(QD/D\) has derived group \(CD/D\ne1\). That is a smaller counterexample, impossible. Thus \(C\) is the unique order-\(p\) subgroup of \(Z(H)\). Consequences:

- \(Z(H)\) is cyclic, of order \(p\) or \(p^2\);
- \(Q\cap Z(H)=C\);
- every nontrivial normal subgroup of \(H\) contains \(C\), because it meets \(Z(H)\) nontrivially.

#### Step B: linearize the class-2 exponent-\(p\) subgroup

Choose \(a\in Q\setminus Z(Q)\). Because \(Q\) is the **actual** power-value set, there is \(x\in H\) with \(x^p=a\). Let \(\alpha\) be conjugation by \(x\) on \(Q\).

For odd \(p\), a class-2 group of exponent \(p\) has its standard Lazard/Baer Lie algebra structure \(L\) over \(\mathbb F_p\): its bracket is the group commutator and its addition is the class-2 BCH operation (equivalently \(u\oplus v=uv[v,u]^{1/2}\), with \(2^{-1}\) taken modulo \(p\)). Group automorphisms act linearly on \(L\). Write \(A\) for the linear map induced by \(\alpha\), and \(N=A-I\).

Because \(x^p=a\),
\[
A^p=\operatorname{Inn}(a)=I+\operatorname{ad}(a)
\]
on the class-2 Lie algebra. In characteristic \(p\), the commuting-binomial identity gives
\[
N^p=(A-I)^p=A^p-I=\operatorname{ad}(a)\ne0,
\]
where nonzero follows from \(a\notin Z(Q)\). Since \(Q'=C\), the nonzero image of \(\operatorname{ad}(a)\) is exactly the one-dimensional subspace \(C\).

Pick \(v\in L\) with \(N^p v=[a,v]=c\ne0\), where \(c\in C\). Conjugation by \(x\) fixes both \(a=x^p\) and \(C\le Z(H)\), so
\[
Na=0,\qquad Nc=0.
\]
Therefore \(v,Nv,\ldots,N^pv=c\) form a Jordan chain of length \(p+1\). The vector \(a\) is another kernel vector and is independent of the chain: the kernel within that chain is spanned by \(c\), whereas \(a\) is noncentral. Consequently
\[
\dim_{\mathbb F_p}L\ge p+2,qquad |Q|\ge p^{p+2}.
\]
Finally \(Q<H\), since \(Q\) has exponent \(p\) while \(H\) has exponent \(p^2\). Hence
\[
|H|\ge p^{p+3}.
\]
Every original counterexample has such a quotient \(H\), so it too must satisfy \(|G|\ge p^{p+3}\).

For \(p=3\), this theoretical bound is \(3^6=729\); the independent catalogue calculation also excludes equality, so a 3-group counterexample would have order at least \(3^7=2187\). For \(p\ge5\), the theoretical bound is already far beyond the order-2000 catalogue.

#### Fragility audit

1. The quotient power set is exactly the image \(QN/N\), so no surjectivity is lost.
2. Exact exponent \(p^2\) survives precisely because a nonabelian power image cannot be trivial or contained in the kernel.
3. The Lie linearization is used only for the class-2 exponent-\(p\) group \(Q\), where \(p>2\) makes \(1/2\) valid; it is not being applied to the potentially high-class group \(H\).
4. \(A^p=\operatorname{Inn}(a)\), not \(A=\operatorname{Inn}(a)\). The nonzero \(p\)-th difference \(N^p\) is the source of the long chain.
5. The extra dimension beyond the length-\((p+1)\) chain is justified by the fixed noncentral vector \(a\); it cannot equal the chain's fixed endpoint \(c\in Z(Q)\).

This reduction does not establish that \(Q\) is abelian. It narrows the shape and minimum order of any counterexample and is a candidate `PARTIAL_RESULT` for Validator.

### 2026-08-16T12:16:10Z — root-fibre count strengthens the order bound

The index \([H:Q]\) in the quotient-minimal reduction is at least \(p^3\), not merely \(p\).

- The fibre of the \(p\)-power map over \(1\) contains all of \(Q\), hence has at least \(|Q|\) elements.
- If \(a\in Q\setminus C\) and \(x^p=a\), then \(x\) commutes with its own power \(a\) and with \(C\le Z(H)\). Since \(Q\) has exponent \(p\) and \(a\notin C\), the subgroup \(\langle a,C\rangle\) has order \(p^2\), and every
  \[
  xd\quad(d\in\langle a,C\rangle)
  \]
  is a distinct root of \(a\): \((xd)^p=x^p d^p=a\). Thus every one of the \(|Q|-p\) target values outside \(C\) has at least \(p^2\) roots.
- If \(1\ne a\in C\), multiplying one root by the central subgroup \(C\) gives at least \(p\) roots. There are \(p-1\) such target values.

The fibres are disjoint, so
\[
|H|\ge |Q|+p^2(|Q|-p)+p(p-1)
      =(p^2+1)|Q|-p^3+p^2-p.
\]
Since nonabelian \(Q\) has \(|Q|\ge p^3\), the right side is strictly greater than \(p^2|Q|\). The index \([H:Q]\) is a power of \(p\), hence
\[
[H:Q]\ge p^3.
\]
Combining this with the root-action bound \(|Q|\ge p^{p+2}\) yields the stronger necessary condition
\[
\boxed{|G|\ge |H|\ge p^{p+5}}.
\]
For \(p=3\), this is \(3^8=6561\); the catalogue search through order 2000 is consistent but no longer sets the leading lower bound. This count still does not show that an object at the lower bound exists.

### 2026-08-16T12:17:49Z — Lead compute correction; catalogue evidence relabeled

Lead sent `CORRECTION: all-enumeration-requires-lease`: under common protocol §4, **every** GAP/Sage/solver/enumeration run counts as heavy, regardless of its observed sub-60-second runtime. I had incorrectly applied only the time/RAM branch of the heavy-job definition. Effective immediately:

- no further GAP, Sage, solver, catalogue, or enumeration command will be run without an explicit current Lead lease;
- the two completed GAP screens and all displayed outputs remain preserved as real observations, but are **procedurally provisional** because they ran without leases;
- their catalogue-coverage interpretations are not being offered as certified or universal partial results unless independently rerun under a lease;
- the theoretical quotient, Lie-action, Hall-collection, and root-fibre arguments do not depend on those screens and remain the active strategy.

Validator separately reported that a line-by-line class-\((<p)\) result is certifiable in principle and requires exact collection terms, a separate \(p=3\) audit, and an explicit final \([x^p,y^p]=1\) obligation. The linked detailed verification note is under an excluded historical/verification path, so I did not open it in this clean run; I will meet the requirements stated in the current inbox message directly. Validator's wording only endorses class \(<p\) in principle, not my stronger candidate class \(\le p\) Hall-polynomial step, so that endpoint remains conjectural pending direct audit.

The protocol-required moves of both processed messages to `bus/archive/` then failed verbatim with `Read-only file system`. I restored their inbox status to `blocked`, appended the reason to each, and sent Lead a `BLOCKER` asking Lead or the filesystem owner to archive them. This filesystem issue does not block theoretical work.

### 2026-08-16T12:19:15Z — structured near-miss tests sharpness of the action argument

The dimension bound \(\dim L\ge p+2\) cannot be improved using only the single-root automorphism equation \((A-I)^p=\operatorname{ad}(a)\). An exact linear model exists:

- take a class-2 Lie algebra over \(\mathbb F_p\) with basis \(a,u_0,\ldots,u_p\), only nonzero basic bracket \([a,u_0]=u_p\), and hence derived algebra \(\langle u_p\rangle\);
- let \(N(a)=N(u_p)=0\) and \(N(u_i)=u_{i+1}\) for \(0\le i<p\), and put \(A=I+N\);
- then \(A\) preserves the bracket, \(A^p=I+N^p=I+\operatorname{ad}(a)\), and the dimension is exactly \(p+2\).

Via the class-2 exponent-\(p\) group correspondence, the consistency equations \(A^p=\operatorname{Inn}(a)\) and \(A(a)=a\) permit adjoining an element \(x\) acting as \(A\) with \(x^p=a\). The resulting extension has exact exponent \(p^2\) and index \(p\) over the nonabelian class-2 base group. It **cannot** satisfy the active actual-value-set hypothesis: the root-fibre count above forbids index \(p\) when every base element must be a \(p\)-th power. Thus it is a structured near-miss, not a candidate counterexample. It pinpoints why simultaneous root-surjectivity, rather than one noncentral root, is the next proof resource.

No computational system was used for this model; the displayed bracket and linear maps are checked directly.

### Automorphism-quotient reformulation

For the quotient-minimal \(H,Q\), put \(S=H/C_H(Q)\). Then the actual \(p\)-power set of \(S\) is exactly
\[
\{(hC_H(Q))^p:h\in H\}=\operatorname{Inn}(Q)\cong Q/Z(Q).
\]
The forward inclusion follows from \(h^p\in Q\); surjectivity follows because every \(q\in Q\) is an actual \(p\)-th power in \(H\). Since \(Q\) has class 2, this value subgroup is elementary abelian. It is nontrivial, so \(S\) has exact exponent \(p^2\), not merely exponent \(p\). Thus the next obstruction can be phrased as a finite \(p\)-subgroup of the automorphism group of a class-2 Lie algebra whose actual \(p\)-power image is all inner automorphisms. This is an exact representation change, but by itself it is consistent with the desired conclusion because that inner subgroup is already abelian.

## Thirty-minute self-check

### 2026-08-16T12:20:38Z — cumulative active minutes 29 (approximately 30)

- **Target scope:** still exactly revision 2, all odd primes, finite groups of exact exponent \(p^2\), actual value set a subgroup, proof direction. No \(p=2\) or exponent-mismatched object has been used.
- **Current hypothesis:** a full proof, if accessible, must exploit simultaneous root-surjectivity after reducing to a quotient-minimal class-2 exponent-\(p\) power subgroup. One-root automorphism data alone is consistent, as the explicit Lie model shows.
- **Checkable evidence:** exact quotient inheritance; candidate minimal-quotient structure \(Q'=C_p\le Z(H)\); direct Lie/Jordan lower bound \(|Q|\ge p^{p+2}\); direct root-fibre count \([H:Q]\ge p^3\), giving candidate \(|G|\ge p^{p+5}\). These have been routed to Validator. The Hall-polynomial class-\(\le p\) lemma is separately labeled candidate and awaits audit.
- **Computation status:** all earlier GAP outputs are preserved but procedurally provisional after Lead's correction; no further computation is authorized or planned without a lease.
- **Representation productivity:** the quotient/Lie-action representation has produced checkable reductions within 30 minutes and exposes the next exact object \(S\le\operatorname{Aut}(Q)\). It remains productive. Kill criterion for the next block: if simultaneous root-surjectivity yields no new identity, dimension constraint, or fibre relation by the one-hour checkpoint, stop enlarging the automorphism formalism and pivot to a fully self-contained certificate of the partial bound.

### Validator hand-audit report received

Validator reported from a computation-free audit that the hand mathematics passes for: the class-\(\le p\) boundary (including \(p=3\)); the quotient-minimal deductions; the Lie/Jordan-chain dimension bound; the root-fibre count; and the resulting necessary bound \(|G|\ge p^{p+5}\). Validator explicitly said the active scope remains unanswered and requested two presentation repairs before `PARTIAL_RESULT`: fix one commutator convention and spell out the multidegree Hall-collection justification. I did not open the linked verification note because verification paths are excluded in this clean run; the current-inbox report contains the operative review result.

Lead subsequently accepted those reviewed hand results as a `PARTIAL_RESULT` and directed continued hand work on simultaneous-root affine covering. Lead explicitly left the stronger proposed \(p^{2p+2}\) bound unaccepted pending its independent audit. The fixed convention and expanded Hall-coordinate justification are now in `findings.md`; all active hypotheses remain explicit and no further computation is being used.

### 2026-08-16T12:23:00Z — affine coset-image covering bound

Simultaneous root-surjectivity yields more than the single-root Jordan chain. Continue with quotient-minimal \(H\), its actual power subgroup \(Q\), and \(C=Q'\cong C_p\le Z(H)\). Put
\[
m=\log_p|Q|,
\qquad V=Q/C\cong\mathbb F_p^{m-1}.
\]

Fix a coset \(xQ\) of \(Q\) in \(H\). Let \(a=x^p\in Q\), let \(A\) be conjugation by \(x\) on the abelian group \(V\), and put \(N=A-I\). Since \(A^p\) is conjugation by \(a\in Q\), it acts trivially on \(Q/C\); hence
\[
A^p=I,
\qquad N^p=(A-I)^p=0.
\]

For \(q\in Q\), the exact semidirect-product expansion is
\[
(xq)^p=x^p q^{x^{p-1}}q^{x^{p-2}}\cdots q^xq.
\]
Passing to additive notation in \(V\) gives
\[
\overline{(xq)^p}
=\bar a+(I+A+\cdots+A^{p-1})\bar q
=\bar a+N^{p-1}\bar q,
\]
because over \(\mathbb F_p\), \(1+T+\cdots+T^{p-1}=(T-I)^{p-1}\). Thus the power values contributed by one coset \(xQ\), after projection modulo \(C\), lie in the affine subspace
\[
\bar a+\operatorname{im}N^{p-1}.
\]

Every Jordan block of \(N\) has size at most \(p\), and \(N^{p-1}\) has rank equal to the number of size-\(p\) blocks. Therefore
\[
\operatorname{rank}N^{p-1}\le
\left\lfloor\frac{m-1}{p}\right\rfloor.
\]
One coset consequently contributes at most
\[
p^{\lfloor(m-1)/p\rfloor}
\]
values modulo \(C\), and at most
\[
p^{\lfloor(m-1)/p\rfloor+1}
\]
actual values in \(Q\), since each projected value has only \(|C|=p\) lifts.

All \([H:Q]\) cosets together must cover the entire actual power set \(Q\) of size \(p^m\). Hence
\[
[H:Q]\,p^{\lfloor(m-1)/p\rfloor+1}\ge p^m,
\]
so
\[
[H:Q]\ge p^{m-1-\lfloor(m-1)/p\rfloor}.
\]
The Jordan argument already gives \(m\ge p+2\). The exponent
\[
2m-1-\left\lfloor\frac{m-1}{p}\right\rfloor
\]
is increasing for integral \(m\), so its minimum on \(m\ge p+2\) occurs at \(m=p+2\). Therefore every counterexample would satisfy the stronger necessary condition
\[
\boxed{|G|\ge |H|\ge p^{2p+2}}.
\]
For \(p=3\), this agrees with the earlier \(3^8\) bound. For every \(p\ge5\), it strictly improves \(p^{p+5}\).

**What this does not prove.** A union of sufficiently many such affine subspaces can cover \(V\); the inequality is only a lower bound on the required number of cosets. No incompatibility between the affine maps has yet been established.

### 2026-08-16T12:25:08Z — powers from one coset commute

The affine subspaces above have extra geometry. Retain the fixed coset \(xQ\), write \(a=x^p\), and now let \(A\) and \(N=A-I\) act on the full class-2 Lie algebra \(L\) of \(Q\). We have
\[
N^p=\operatorname{ad}(a).
\]
Conjugation by \(x\) fixes \(a=x^p\), and it fixes \(C=Q'\) pointwise because \(C\le Z(H)\). Hence \(A\) commutes with \(\operatorname{ad}(a)\) and \(N\) kills the image \(C\), giving
\[
N^{p+1}=N\operatorname{ad}(a)=0.
\]

The commutator form on \(U=Q/Z(Q)\) is a nondegenerate alternating \(\mathbb F_p\)-form preserved by \(A\). The adjoint of \(N=A-I\) is
\[
N^*=A^{-1}-I=-A^{-1}N,
\]
so \(\ker((N^*)^i)=\ker(N^i)\) and therefore
\[
(\operatorname{im}N^i)^\perp=\ker N^i.
\]
For \(i=p-1\), the inequality \(2p-2\ge p+1\) (valid because \(p\ge3\)) and \(N^{p+1}=0\) give
\[
\operatorname{im}N^{p-1}\le\ker N^{p-1}.
\]
Thus \(\operatorname{im}N^{p-1}\) is totally isotropic on \(U\). Also, for \(w=N^{p-1}u\),
\[
[a,w]=\operatorname{ad}(a)N^{p-1}u=N^{2p-1}u=0.
\]

Modulo \(C\), all power values from \(xQ\) lie in \(a+\operatorname{im}N^{p-1}\), and changes by \(C\) do not affect commutators. It follows that **any two \(p\)-th powers whose roots lie in the same coset of \(Q\) commute**.

This is exact but not yet decisive: the hypothesis gives roots for every element of \(Q\), not roots for every pair in a common coset. A nonabelian \(Q\) could in principle be covered by many commuting affine pieces, consistent with the affine lower bound.

### 2026-08-16T12:30:30Z — identity-coset refinement of the affine bound

The previous affine count used the maximum per-coset image size for all cosets, but the identity coset \(Q\) contributes only the value \(1\), because \(\exp Q=p\). Put
\[
k=\left\lfloor\frac{m-1}{p}\right\rfloor,
\qquad r=[H:Q],
\qquad M=p^{k+1}.
\]
Each nonidentity coset contributes at most \(M\) actual values, while \(Q\) contributes one. Therefore the exact covering inequality is
\[
p^m=|Q|\le1+(r-1)M.
\]
The earlier estimate gave \(r\ge p^{m-1-k}\). Equality there is impossible: if \(r=p^{m-1-k}\), then
\[
1+(r-1)M=p^m-M+1<p^m.
\]
Since \(r\) is a power of \(p\), it follows that
\[
[H:Q]\ge p^{m-k}
=p^{m-\lfloor(m-1)/p\rfloor}.
\]
Consequently
\[
|G|\ge|H|\ge
p^{2m-\lfloor(m-1)/p\rfloor}.
\]
The exponent is increasing with integral \(m\), and \(m\ge p+2\), so the refined universal necessary bound is
\[
\boxed{|G|\ge p^{2p+3}}.
\]
This supersedes the proposed \(p^{2p+2}\) affine bound but remains under independent audit. It does not affect the already accepted \(p^{p+5}\) partial if the affine argument is rejected.

### 2026-08-16T12:32:25Z — cyclic-coset commuting pieces

The same-coset lemma extends across all root cosets in one cyclic subgroup of \(H/Q\). Let \(xQ\) be nontrivial and keep \(A=I+N\), \(a=x^p\), and \(W=\operatorname{im}N^{p-1}\) on the relevant quotient. For \(1\le j\le p-1\),
\[
(x^j)^p=a^j,
\qquad A^j-I=N\bigl(jI+\tbinom j2N+\cdots\bigr).
\]
The parenthesized polynomial has nonzero constant term \(j\), hence is invertible and commutes with \(N\). Therefore
\[
\operatorname{im}(A^j-I)^{p-1}=W.
\]
All power values whose root coset is \(x^jQ\) project into \(ja+W\). The union over the cyclic subgroup \(\langle xQ\rangle\) consequently projects into \(\langle a,W\rangle\). The previous proof gives that \(W\) is isotropic and \(a\perp W\); hence \(\langle a,W\rangle\) is isotropic. Changes by central elements do not alter commutators. Thus:

> Any two \(p\)-th power values commute whenever their root cosets lie in the same cyclic subgroup of \(H/Q\).

This supplies a cover of \(Q\) by commuting pieces indexed by cyclic subgroups of the exponent-\(p\) group \(H/Q\). It does not force a single piece to contain roots for every pair, so it remains a structural reduction rather than a proof of global abelianness.

### 2026-08-16T12:33:23Z — canonical module-cover formulation

Let
\[
E=H/C,\qquad V=Q/C,\qquad R=H/Q.
\]
Then \(V\) is an elementary abelian normal subgroup of \(E\), \(R\) has exponent \(p\), and \(E/V\cong R\). For \(r\in R\), choose a lift \(\tilde r\in E\), let \(A_r\) be its action on \(V\), and put \(\alpha(r)=\tilde r^{,p}\in V\). The set
\[
\mathcal A_r
=\alpha(r)+\operatorname{im}(A_r-I)^{p-1}
\]
is independent of the chosen lift: replacing \(\tilde r\) by \(\tilde r v\) changes \(\alpha(r)\) by exactly the norm
\[
(I+A_r+\cdots+A_r^{p-1})v=(A_r-I)^{p-1}v.
\]
It is exactly the projection modulo \(C\) of the \(p\)-th powers whose roots lie over \(r\). Hence actual-value surjectivity becomes the finite-dimensional cover condition
\[
V=\bigcup_{r\in R}\mathcal A_r,
\qquad \mathcal A_1=\{0\}.
\]

The missing nonabelian information is the central extension \(1\to C\to Q\to V\to1\), encoded by the alternating commutator form, together with lifted actions satisfying
\[
(\widetilde A_r-I)^p=D_{\alpha(r)}.
\]
Thus a full proof would follow from showing that a canonical affine norm-cover satisfying these lift identities forces the commutator form to vanish. The current argument proves small ranks and isotropy for each \(\mathcal A_r\), but not global vanishing. This is the precise representation-changing pivot; merely enlarging a catalogue would not address it.

### Review-state split for affine results

Validator's first affine audit accepted the computation-free \(|G|\ge p^{2p+2}\) bound and the same-root-coset commutativity lemma; Lead accepted both as structural `PARTIAL_RESULT`s and directed cross-coset intersection/orthogonality work. Those reviews predate and do not address the later identity-coset refinement. Accordingly:

- accepted partial: \(|G|\ge p^{2p+2}\);
- accepted partial: each root-coset power image is pairwise commuting;
- pending audit: the refined \(|G|\ge p^{2p+3}\) inequality from the identity coset;
- `active_assignment_answered: no`.

### 2026-08-16T12:36:17Z — cross-piece geometry alone cannot finish the proof

Intersections and individual isotropy do not by themselves force the global commutator form to vanish. A concrete finite-geometric obstruction is available. Let
\[
U=\mathbb F_{p^d}^2
\]
viewed over \(\mathbb F_p\), with nondegenerate alternating form
\[
B((x,y),(x',y'))=\operatorname{Tr}_{\mathbb F_{p^d}/\mathbb F_p}(xy'-x'y).
\]
For \(t\in\mathbb F_{p^d}\), define
\[
L_t=\{(x,tx):x\in\mathbb F_{p^d}\},
\qquad
L_\infty=\{(0,y):y\in\mathbb F_{p^d}\}.
\]
Each \(L_t\) is totally isotropic, distinct members intersect only at 0, and the \(p^d+1\) members cover all of \(U\). Thus a nonzero symplectic space can be covered perfectly by commuting linear pieces. Two isotropic affine pieces may also intersect without their direction spaces being mutually orthogonal.

This is **not** a group counterexample and supplies no forbidden \(p=2\) data. It is a kill result for the naive geometric strategy: the proof must use compatibility among the actions \(A_r\), the canonical basepoints \(\alpha(r)\), and the extension 2-cocycle, not merely the fact that each \(\mathcal A_r\) is commuting or that the pieces cover/intersect.

### 2026-08-16T12:37:44Z — optimal cross-piece symplectic cover bound

Although isotropic covering cannot force the form to vanish, it gives a sharp structural count. Let
\[
2d=\dim_{\mathbb F_p} Q/Z(Q).
\]
For every order-\(p\) cyclic subgroup \(K\le R=H/Q\), the cyclic-coset lemma places all projected power values with root coset in \(K\) inside one totally isotropic linear subspace of the symplectic space \(Q/Z(Q)\). These subspaces cover \(Q/Z(Q)\), because every element of \(Q\) is an actual \(p\)-th power and the identity coset contributes no nonzero value.

A totally isotropic subspace has at most \(p^d\) points. If \(t\) cyclic subgroups supply the cover, all their subspaces contain 0, so
\[
p^{2d}-1\le t(p^d-1),
\qquad t\ge p^d+1.
\]
Because \(R\) has exponent \(p\), its nonidentity elements partition into its order-\(p\) cyclic subgroups, and
\[
t=\frac{|R|-1}{p-1}.
\]
It follows that
\[
|R|\ge(p-1)(p^d+1)+1>p^d.
\]
Since \(|R|\) is a power of \(p\),
\[
\boxed{[H:Q]\ge p^{d+1}}.
\]

This bound is generally weaker than the affine rank bound in terms of \(m=\log_p|Q|\), because a large center can make \(d\) small. The explicit symplectic spread above attains the underlying \(p^d+1\) cover number, so no stronger conclusion can come from isotropic-subspace cardinality alone.

### 2026-08-16T12:39:28Z — explicit cross-pairing incidence identity

The cyclic-piece lemma gives one exact control across distinct root cosets. Let \(u,v\in Q\), and suppose
\[
u=x^p,\qquad uv=z^p.
\]
If the cosets \(xQ\) and \(zQ\) lie in the same cyclic subgroup of \(H/Q\), then the cyclic-piece lemma says that \(u\) and \(uv\) commute. Since \(Q\) has class 2,
\[
[u,uv]=[u,v].
\]
Therefore
\[
\boxed{zQ\in\langle xQ\rangle\quad\Longrightarrow\quad [u,v]=1.}
\]
Symmetrically, if \(v=y^p\) and \(zQ\in\langle yQ\rangle\), then \([u,v]=1\).

In canonical-cover notation, if
\[
u\in\mathcal A_r,
\quad v\in\mathcal A_s,
\quad u+v\in\mathcal A_t,
\]
then
\[
t\in\langle r\rangle\ \text{or}\ t\in\langle s\rangle
\quad\Longrightarrow\quad B(u,v)=0.
\]
Thus any nonzero cross-pairing forces a strict root-coset separation: every chosen root coset for the product must avoid the cyclic root subgroups used for both factors. Closure guarantees a root for the product but does not guarantee the required cyclic incidence, so this identity narrows rather than closes the remaining case.

### 2026-08-16T12:41:54Z — extraspecial minimal power subgroup is impossible

Assume, for contradiction within the quotient-minimal model, that
\[
Z(Q)=Q'=C\cong C_p.
\]
Then \(Q\) is extraspecial of exponent \(p\). Its class-2 Lie algebra has the form
\[
L=V\oplus C,
\]
where \(V=Q/C\) carries the nondegenerate alternating commutator form \(B:V\times V\to C\).

Every conjugation automorphism induced by \(H\) fixes \(C\) pointwise and therefore has a unique form
\[
(v,t)\longmapsto(Av,t+\lambda(v)),
\qquad A\in\operatorname{Sp}(V,B),\quad\lambda\in V^*.
\]
Let \(S\) be the finite \(p\)-subgroup of these automorphisms induced by \(H\), and let \(T\) be its image on \(V\). A finite \(p\)-group acting on an \(\mathbb F_p\)-space admits a complete invariant flag
\[
0=V_0<V_1<\cdots<V_n=V
\]
with every \(A\in T\) acting trivially on each successive quotient; equivalently,
\[
(A-I)V_i\le V_{i-1}.
\]
This follows inductively from the nonzero fixed space of every nonzero \(\mathbb F_pT\)-module.

For \(s=(A,\lambda)\in S\), choose \(x\in H\) inducing it. Since \(x^p\in Q\), the induced map \(A^p\) on \(V=Q/C\) is the identity. Direct iteration gives
\[
s^p=(I,\mu),
\qquad
\mu=\lambda(I+A+\cdots+A^{p-1})
=\lambda(A-I)^{p-1}.
\]
By the invariant flag, \((A-I)^{p-1}\) kills \(V_{p-1}\) (and if \(n<p-1\), it kills all of \(V\)). Hence every such \(\mu\) annihilates one fixed nonzero subspace \(V_{p-1}\).

Under the nondegenerate form, the inner automorphism induced by \(a\in V\) corresponds to the functional
\[
\beta_a(v)=B(v,a).
\]
Thus every \(p\)-th power in \(S\) belongs to the proper subspace
\[
(V_{p-1})^\perp<V
\]
of inner automorphisms. But actual-value surjectivity in \(H\) says the opposite: for every \(a\in V=Q/C\), choose a representative \(q\in Q\) and a root \(x^p=q\); the induced automorphism then satisfies
\[
s_x^p=\operatorname{Inn}(q)=\beta_a.
\]
So the \(p\)-th powers in \(S\) must cover all of \(V\), a contradiction.

Therefore a quotient-minimal counterexample must satisfy
\[
\boxed{Z(Q)>Q'=C.}
\]
This excludes the entire extraspecial exponent-\(p\) family for the minimal power subgroup. It does not rule out class-2 \(Q\) with a larger center; in that case central automorphisms need not all be inner, and the nondegenerate identification \(V\cong V^*\) used in the contradiction fails.

### 2026-08-16T12:43:10Z — common-flag argument forces \(\dim Z(Q)\ge p\)

The simultaneous-root hypothesis strengthens the extraspecial exclusion and gives a cleaner explanation of the earlier dimension bound. Let \(L\) be the class-2 Lie algebra of \(Q\), and let \(S\) be the finite \(p\)-subgroup of \(\operatorname{Aut}(L)\) induced by \(H\). Over \(\mathbb F_p\), choose a complete common invariant flag
\[
0=F_0<F_1<\cdots<F_m=L
\]
such that
\[
(A-I)F_i\le F_{i-1}
\qquad(A\in S).
\]

For every \(a\in Q\), actual-value surjectivity supplies \(x\in H\) with \(x^p=a\). If \(A\in S\) is conjugation by \(x\) and \(N=A-I\), then, with the fixed convention,
\[
N^p=D_a,\qquad D_a(v)=[v,a]_L.
\]
For \(v\in F_p\), the flag-lowering property gives \(N^pv=0\). Since this holds for the root action attached to **every** \(a\in Q\),
\[
[v,a]_L=0\qquad(v\in F_p,\ a\in Q).
\]
Therefore
\[
F_p\le Z(L)=Z(Q),
\]
and
\[
\boxed{\dim_{\mathbb F_p}Z(Q)\ge p.}
\]

Because nonabelian class-2 \(Q\) has \(\dim Q/Z(Q)\ge2\), this immediately recovers
\[
\dim Q\ge p+2.
\]
It also strictly excludes the extraspecial case \(\dim Z(Q)=1\). The bound is structurally sharp for the one-root linear near-miss, whose center has dimension \(p\), but simultaneous affine covering still imposes the separate index bounds.

MathExpert reported a fresh computation-free audit: the class-\(\le p\) Hall mechanism is credible with the explicit separate-degree lemma, \(p=3\) has no endpoint exception, and the first weight-\((p+1)\) obstruction consists of the two extreme multidegrees. MathExpert independently identified the same remaining issue: closure supplies a compatible root of the product of two powers, not triviality of the obstruction. I did not open the linked ideas note because this clean run uses the current-inbox summary rather than solution-bearing side artifacts.

### Candidate next block: sharp-center upper-unitriangular analysis

The common-flag lemma reduces the first unresolved central case to
\[
\dim Z(Q)=p,
\qquad F_p=Z(Q),
\qquad F_1=C.
\]
Relative to \(L/Z(Q)\oplus Z(Q)\), a root action difference has a block-upper-unitriangular form: a nilpotent action on the symplectic quotient, a nilpotent length-at-most-\(p\) action on the center, and a cross map from the quotient into the center. Its \(p\)-th power must be the rank-one inner map \(D_a:L/Z(Q)\to C\), and these rank-one maps must be attained for every noncentral \(a\).

A bounded next experiment is to write the exact \(p\)-th power of this block matrix and use closure under products inside the common p-subgroup to test whether all symplectic functionals can occur when the central flag has exactly \(p\) dimensions. Success would either force \(\dim Z(Q)>p\) or expose a consistent sharp model. Kill criterion: if the block identity reduces only to unconstrained choices of cross maps and gives no relation between two different roots within 30 active minutes, stop; it would be another one-root parametrisation rather than a global proof mechanism.

### Log corrections and command-accounting note

- In the canonical module-cover entry, the displayed `\(\tilde r^{,p}\)` is a typographical comma; the intended and subsequently used definition is `\(\alpha(r)=\tilde r^p\)`.
- While removing an accidental zero-width character from `findings.md`, the command
  `perl -CSDA -pi -e 's/\\x{200B}//g' .../findings.md` failed with `Cannot make temp name: Read-only file system`. No change was inferred from that failure. A targeted `apply_patch` then removed the character, and a subsequent `rg -n 'dim_' .../findings.md` displayed the two corrected `\dim_{\mathbb F_p}` lines.

### 2026-08-16T12:49:26Z — sharp-center block identity has a consistent automorphism-level model

Write the sharp case as \(L=U\oplus Z\), with \(\dim Z=p\), and express a root-action difference as
\[
N=
\begin{pmatrix}
M&0\\
\lambda&K
\end{pmatrix}.
\]
Then
\[
N^p=
\begin{pmatrix}
M^p&0\\
\displaystyle\sum_{i=0}^{p-1}K^{p-1-i}\lambda M^i&K^p
\end{pmatrix}.
\]
The root equation \(N^p=D_a\) asks for \(M^p=K^p=0\) and for the bottom-left block to be the symplectic functional \(B(-,a)\) with image in \(C\).

This identity alone is consistent with attaining every such functional. Take \(U\) two-dimensional symplectic, take \(Z\) of dimension \(p\) with a regular nilpotent \(K\) satisfying \(K^{p-1}Z=C\), and let \(B_0=I+K\). The p-group of bracket-preserving automorphisms
\[
S=\operatorname{Hom}(U,Z)\rtimes\langle B_0\rangle
\]
acts trivially on \(U\), acts by \(B_0\) on \(Z\), and adds arbitrary central cross maps \(\lambda:U\to Z\). For an element with nontrivial \(B_0^j\)-component, its \(p\)-th power has central cross map
\[
(I+B_0^j+\cdots+(B_0^j)^{p-1})\lambda
=(B_0^j-I)^{p-1}\lambda
=K^{p-1}\lambda.
\]
As \(\lambda\) varies, these are all maps \(U\to C\), which the symplectic form identifies with all inner automorphisms of the corresponding class-2 group \(Q\). Thus the automorphism-level power set can equal \(\operatorname{Inn}(Q)\) even with nonzero commutator form.

This is **not a group counterexample**. It is only action data. Turning it into an admissible \(H\) would require a compatible group extension that identifies the inner-automorphism subgroup of \(S\) with \(Q/Z(Q)\), preserves exact exponent \(p^2\), and makes the actual power values in \(H\) equal the embedded \(Q\). None of those extension conditions has been constructed. As an active-scope candidate it is `OUT_OF_SCOPE_EXAMPLE`: it fails `21.137-odd-finite-p-group`, `21.137-odd-power-set-definition`, and `21.137-odd-power-set-subgroup` because it is not yet a group \(H\) at all.

It meets the sharp-center block strategy's kill criterion: the one-action/cross-map equations do not force global abelianness. Any continuation must use the nontrivial extension/cocycle compatibility, not more block parametrisation.

**Immediate scope correction.** The automorphism group \(S\) just displayed is itself a finite \(p\)-group, and suitable elements show its exponent is exactly \(p^2\). Its own actual \(p\)-th-power set is \(\operatorname{Hom}(U,C)\), which is an abelian subgroup, so \(S\) is a positive in-scope example consistent with the target. What fails is the attempted use of the *nonabelian external group* \(Q\) as the power subgroup of \(S\): that identification violates `21.137-odd-power-set-definition`. Thus the action datum is not a counterexample candidate; the preceding sentence naming the finite-group and subgroup rows as failed was overbroad and is superseded by this correction.

## One-hour checkpoint

### 2026-08-16T12:50:19Z — cumulative active minutes 59 (approximately 60)

- **Active scope and revision:** `21.137/odd-prime-exponent-p2`, revision 2, proof direction. The argument always assumes \(p>2\), a finite \(p\)-group of exact exponent \(p^2\), and closure of the actual power-value set. The \(p=2\), exponent-8 clause remains excluded.
- **New accepted facts:** class \(\le p\) is excluded without needing closure; any counterexample has a quotient-minimal model with \(Q'=C_p\le Z(H)\); the reviewed affine argument gives \(|G|\ge p^{2p+2}\); and values rooted in one coset commute. Lead/Validator accept these as `PARTIAL_RESULT`s, not an answer.
- **New facts pending audit:** identity-coset refinement \(|G|\ge p^{2p+3}\); cyclic-subgroup isotropic cover and \([H:Q]\ge p^{d+1}\); common-flag bound \(\dim Z(Q)\ge p\), excluding extraspecial \(Q\).
- **Current named strategy:** **canonical affine cover plus central-extension lift**. It converts root-surjectivity to affine norm images and now isolates the missing datum as a crossed extension identifying inner automorphisms with the embedded nonabelian \(Q/Z(Q)\).
- **What was ruled out:** affine intersections/isotropy alone cannot force global commutativity (explicit symplectic spreads attain such covers); one-root and sharp-center block equations also cannot, because the hand-built p-subgroup \(\operatorname{Hom}(U,Z)\rtimes C_p\) realizes all inner functionals as its own powers while keeping them abelian.
- **Cross-pairing identity obtained:** if \(u=x^p\), \(uv=z^p\), and \(zQ\in\langle xQ\rangle\), then \([u,v]=1\). A nonzero cross-pairing forces product-root cosets away from both factor-root cyclic subgroups.
- **Bottleneck:** closure guarantees a root of \(uv\) but gives no reason for its coset to have the required incidence. The action-level model shows that only the group-extension/2-cocycle compatibility could supply it.
- **Alternative A:** derive the explicit crossed-extension cocycle equation for lifting the sharp-center automorphism model to a group \(H\) with embedded \(Q\), then show exact exponent \(p^2\) obstructs the lift.
- **Alternative B:** stop the affine representation and polish the accepted low-class/minimal-quotient/affine partial certificate; a later direction could investigate compatible extensions as a constructor problem under Lead authority.
- **Recommended next 60-minute experiment:** spend at most 30 active minutes writing the exact extension/lift equations for the sharp-center action model, focusing on whether identifying \(S^p=\operatorname{Inn}(Q)\) with \(Q/Z(Q)\) forces an element of order \(p^3\) or loses actual-value surjectivity. Use the remaining time only if one checkable obstruction appears.
- **Kill criterion:** if the extension equations admit a formally consistent cocycle or merely restate the original power-surjectivity condition without controlling cross-pairings, stop this strategy and finalize `PARTIAL_RESULT`.
- **Admissibility status:** there is no all-scope proof candidate. The automorphism group \(S\) is a positive in-scope instance whose actual power subgroup is abelian; attempting to designate the external nonabelian \(Q\) as its power set fails `21.137-odd-power-set-definition`. The target conclusion row `21.137-odd-P-abelian` remains unproved globally. `active_assignment_answered: no`.

### Lead decision after one-hour checkpoint

Lead reported that Validator passes the identity-coset refinement \(|G|\ge p^{2p+3}\), cyclic-root-subgroup commutativity, the cross-pairing incidence statement, and the common-flag bound \(\dim Z(Q)\ge p\) as partial results. Lead authorized one bounded hand block comparing compatible roots of \(a,b,ab\) at the first Hall weight-\((p+1)\) obstruction. Kill criterion: if closure still supplies only an unconstrained root of \(ab\), declare this proof representation exhausted. The active scope remains unanswered.

### 2026-08-16T12:52:38Z — compatible-root comparison and representation kill

Let \(a=x^p\), \(b=y^p\), and choose \(z\) with \(z^p=ab\). In the class-2 Lie algebra of the quotient-minimal power subgroup, write the logarithms of \(a,b\) as \(u,v\). With the fixed BCH convention,
\[
\log(ab)=u+v+\tfrac12[u,v].
\]
For the three root actions, with \(N_x=A_x-I\), etc.,
\[
N_x^p=D_u,
\qquad N_y^p=D_v,
\qquad N_z^p=D_{u+v+\frac12[u,v]}.
\]
But \([u,v]\in C\le Z(Q)\), so its inner derivation is zero. Therefore the entire compatible-root identity visible to conjugation is only
\[
\boxed{N_z^p=N_x^p+N_y^p.}
\]
The desired cross-pairing \([u,v]\) has disappeared: it lies exactly in the kernel of \(Q\to\operatorname{Inn}(Q)\). The sharp-center automorphism model above realizes every functional \(D_u,D_v,D_u+D_v\) as a \(p\)-th power while allowing a nonzero symplectic pairing \([u,v]\). Thus the three compatible action equations are formally consistent with noncommutativity.

The same loss appears in Hall coordinates. If
\[
t=(xy)^{-1}z,
\]
then the compatibility equation is
\[
(xyt)^p=x^py^p.
\]
Closure gives no restriction on the coset \(tQ\). At the first weight-\((p+1)\) Hall layer, the two extreme multidegree terms from \(x,y\) can be balanced by the independent Hall coordinates involving \(t\); equivalently, the free central coordinate of the chosen root \(z\) absorbs the term \(\tfrac12[u,v]\). Only an additional incidence such as \(zQ\in\langle xQ\rangle\) removes that freedom, and that is precisely the separately proved conditional cross-pairing identity—not a consequence of closure.

**Kill conclusion.** The authorized comparison still supplies only an unconstrained root of \(ab\). The canonical affine/Hall/action representation is therefore exhausted as a route to a full proof. It has yielded accepted structural partials, but a global argument would require new extension-theoretic information not encoded by the current hypotheses in these coordinates.

## Cycle outcome — `PARTIAL_RESULT`

### 2026-08-16T12:54:47Z — stopped by Lead after 63 active minutes

Lead ordered a clean stop so the remaining cycle budget can be switched atomically to a fresh counterexample direction. The single outcome of this proof-direction run is `PARTIAL_RESULT`:

- all qualifying groups of nilpotency class at most \(p\) satisfy the conclusion;
- any counterexample has the quotient-minimal structure recorded in `findings.md`, including \(Q'=C_p\le Z(H)\), \(\dim Z(Q)\ge p\), and \(|G|\ge p^{2p+3}\);
- same- and cyclic-root-coset power values commute, with the recorded conditional cross-pairing identity;
- the canonical affine/Hall/action proof representation met its kill criterion and is exhausted for a full proof;
- `active_assignment_answered: no`; arbitrary high-class qualifying groups remain uncovered.

The procedurally provisional unleased GAP screens are preserved in this log but are not part of the result. No claim-check JSON was created because this is not a `CLAIM`, and the target conclusion row remains unproved.

### 2026-08-16T12:55:52Z — final packaging-time correction

The read-only final inspection and outcome-message packaging continued for one minute after the research stop. Final cumulative active time is therefore **64 minutes**, not 63. No mathematical work or new strategy occurred in that minute; this entry supersedes only the timing number above.
