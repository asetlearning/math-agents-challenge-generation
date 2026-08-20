---
title: "21.137 fresh proof audit: class at most p+1"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/hall-collection
  - project/kourovka
  - status/draft
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
run_dir: Agents/Kourovka/problems/21.137/runs/2026-08-16-r3-odd-proof-class-p-plus-one
direction: proof
---

# Working log

## Context boundary and active-time ledger

- `2026-08-16T14:17:16Z` — Work block opened at the assigned shared ledger value `96/180` active minutes. This block is capped at 60 further active minutes and at wall-clock `2026-08-16T15:17:16Z`.
- `2026-08-16T14:17:16Z–2026-08-16T14:28:23Z` — cumulative active minutes: `107` (11 minutes in this block). Read the specified Lead decision first, then only the common protocol, canonical scope record, rendered source page, reviewed proof findings, and the two named archived specialist messages. Did not inspect synthesis, historical logs, verification scratch, counterexample artifacts, JSONL transcripts, filenames beyond the named paths, or the web.
- Assignment restrictions obeyed: no delegation, no web, no mathematical computation, no wreath-shaped route. The proposed class-\(p+1\) lemma is being treated as adversarially unverified.

## Staleness check and source gate

`DISCOVERY_BLIND: yes` is inherited from the canonical scope record and reinforced by Lead's curated boundary.

- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`
- Open-web and arXiv searches: not performed, by instruction.
- Source: rendered Kourovka Notebook issue 21 (2026), PDF page 184, visually inspected from `scratch/source-page-184.png`; the source PDF resolved through `_meta/agents/Kourovka/paths.env`.
- Corrected transcription: “If the \(p\)-th powers in a finite \(p\)-group form a subgroup, must that subgroup be powerful? That is, for \(p\ne2\), if the \(p\)-th powers in a \(p\)-group of exponent \(p^2\) form a subgroup, must that subgroup be abelian? For a 2-group of exponent 8, if the squares form a subgroup, must that subgroup be abelian?”
- The rendered statement attaches no editor or later comment to Problem 21.137 on that page. Corpus flags were not re-read because Lead's curated boundary excludes the corpus in this continuation.
- `source_transcription_checked: yes`
- `active_scope_checked: yes`

### Clause matrix

| source clause | equivalent formulation | active scope? | literature status in this blind continuation |
|---|---|---:|---|
| If \(p\)-th powers in a finite \(p\)-group form a subgroup, must it be powerful? | General powerfulness question. | no | Not checked; web and solution-bearing history excluded. |
| For \(p\ne2\), exponent \(p^2\), must the power-value subgroup be abelian? | For every odd prime \(p\) and qualifying finite \(p\)-group, actual value set \(P=\{g^p:g\in G\}\le G\) implies \([P,P]=1\). | **yes** | No external result considered in this blind continuation. |
| For a 2-group of exponent 8, must the square-value subgroup be abelian? | Separate \(p=2\) clause. | no; expressly excluded | Not checked. |

### Canonical admissibility checklist

| constraint_id | source requirement | audit treatment |
|---|---|---|
| `21.137-odd-forall-p-G` | Uniformly every qualifying \(p,G\). | A class-bounded lemma is only a partial family, not the unrestricted target. |
| `21.137-odd-p-not-2` | \(p>2\) prime. | Retained; oddness is needed for \(p\mid\binom p2\). |
| `21.137-odd-finite-p-group` | Finite \(p\)-group for the same \(p\). | Retained in application; the proposed lemma is formally stronger and does not use finiteness. |
| `21.137-odd-exponent-p2` | Exponent exactly \(p^2\). | Retained in application; proof attempts the stronger assumption \(\exp G\mid p^2\). |
| `21.137-odd-power-set-definition` | Actual values, not just their generated subgroup. | Retained in target; class-bounded lemma does not need value-set closure and defines \(K=\langle g^p:g\in G\rangle\) only as an auxiliary subgroup. |
| `21.137-odd-power-set-subgroup` | Actual value set is a subgroup. | Retained in target but unused in the proposed class-bounded lemma. |
| `21.137-odd-P-abelian` | \(P\) abelian. | To be established only under the extra restriction \(\operatorname{cl}(G)\le p+1\); unrestricted conclusion remains unproved. |

No source/scope mismatch was found.

## Strategy portfolio

Ranked by expected certifiable information per active hour:

1. **Theoretical hostile Hall audit.** Work in the torsion-free free two-generator nilpotent group through class \(p+1\), then specialize. Audit separately: lower-weight divisibility; \(K=\langle g^p\rangle\) having class at most two; exponent of all of \(K\), not just its generators; the exponent-\(p\) quotient; and isolation of the unique multidegree \((p,1)\) coordinate. Kill if any step assumes \(\exp K\mid p\), uniqueness of coordinates in a quotient, or unproved divisibility.
2. **Certificate plan.** If the argument survives, give Validator a dependency-explicit proof with a separate normal-generation/arbitrary-product lemma for \(\exp K\mid p\), plus a Hall-coordinate lemma stated integrally before specialization. Evidence is a hand-reconstructible argument; no computation or unexplained constants.
3. **Adversarial structured falsifier.** Attempt on paper to preserve an extreme weight-\(p+1\) basic commutator of order \(p^2\) in an exponent-\(p^2\), class-\(p+1\) quotient. Abandon if the independently derived exponent lemma forces every element of \(K\), including the extreme coordinate once shown to lie in \(K\), to have order \(p\).
4. **Catalogue/small-case mode.** Disabled by the assignment's no-computation rule. In any event, bounded examples could only falsify the lemma or give data, never certify the uniform result.

Representation-changing pivot already imposed by Lead: replace construction search by integral Hall coordinates in the relatively free nilpotent object and the auxiliary generated-power subgroup \(K\).

## Command/output ledger

All paths below are vault-relative in the actual commands.

1. Read the specified Lead decision with `sed -n '1,240p'`. Output: the decision orders a 60-active-minute hostile class-\(p+1\) proof audit, gives the curated reading boundary, and requires the terminal exponent, Hall-coordinate, and class-\(p+2\) checks.
2. Read `_common-kourovka.md` through EOF, the canonical scope JSON, the reviewed proof `findings.md` through EOF, and the two named archived messages with `sed`. Output: the exact scope and the proposed proof/gap reproduced in the cited files; no other mathematical context was opened.
3. Source command: `source '_meta/agents/Kourovka/paths.env'; kv_now; test readability; pdftotext -f 184 -l 184 -layout "$KOUROVKA_PDF" -; pdftoppm -f 184 -l 184 -singlefile -png -r 180 "$KOUROVKA_PDF" <RUN_DIR>/scratch/source-page-184`. Real status/output: `2026-08-16T14:26:01Z`, `KOUROVKA_PDF_READABLE=yes`, and the page text containing the transcription recorded above; rendered image created at `scratch/source-page-184.png` (440004 bytes).
4. Visual inspection of `scratch/source-page-184.png`: the printed formula is exponent \(p^2\), the prime restriction is \(p\ne2\), and the separate 2-group exponent is 8.
5. `rg --files <RUN_DIR> | sort`. Output before this log was created: the two system JSONL transcript files and `scratch/source-page-184.png`. The JSONL files were not opened.

## Hostile audit of the class-\(p+1\) lemma

### Fixed notation

Use
\[
[u,v]=u^{-1}v^{-1}uv,\qquad u^v=v^{-1}uv,
\]
and left-norm higher commutators. Let \(p\) be an odd prime, let \(G\) have exponent dividing \(p^2\), and suppose \(\operatorname{cl}(G)\le p+1\). Put
\[
S=\{g^p:g\in G\},\qquad K=\langle S\rangle.
\]
Here \(K\) is the generated power subgroup, not an assertion that the value set \(S\) is closed.

### Audit A: integral Hall coordinates and lower-weight divisibility

In the torsion-free free nilpotent group on \(X,Y\) of class \(p+1\), fix an ordered Hall basis. If a basic commutator \(b\) has multidegree \((r,s)\), with both entries positive, its coordinate in the collected word \([X^m,Y^n]\) is an integer-valued polynomial
\[
f_b(m,n)=\sum_{i=1}^{r}\sum_{j=1}^{s}
a_{b,i,j}\binom mi\binom nj,
\qquad a_{b,i,j}\in\mathbb Z.
\]
The integral binomial form follows from the separate finite-difference degree bounds \(r,s\); the zero-index terms vanish because \([X^0,Y^n]=[X^m,Y^0]=1\) and Hall coordinates are unique in the torsion-free free object. This is applied before mapping to \(G\); no coordinate uniqueness is assumed in \(G\) or a quotient.

If \(r+s\le p\), then \(1\le r,s\le p-1\), so every summand of \(f_b(p,p)\) has two factors divisible by \(p\). Hence every coordinate below weight \(p+1\) is divisible by \(p^2\), and specialization to an exponent-dividing-\(p^2\) group gives
\[
[x^p,y^p]\in\gamma_{p+1}(G)\qquad(x,y\in G).
\]

At weight \(p+1\), every non-extreme multidegree still has \(r,s\le p-1\), hence a \(p^2\)-divisible coordinate. The only exceptions are \((p,1)\) and \((1,p)\); their coordinates are still divisible by \(p\), since the coordinate belonging to the degree-one variable supplies \(\binom p1=p\). No coefficient division modulo \(p\) has been used.

### Audit B: normal generation, central generator commutators, and all of \(K\)

The set \(S\) is inverse-closed and conjugacy-invariant:
\[
(g^p)^{-1}=(g^{-1})^p,\qquad (g^p)^h=(g^h)^p.
\]
Thus \(K\unlhd G\) independently of any exponent claim.

Every \(s=g^p\in S\) has \(s^p=1\). Audit A and \(\gamma_{p+1}(G)\le Z(G)\) give
\[
[s,t]\in Z(G)\qquad(s,t\in S).
\]
Consequently \(K'\) is generated by these central pair commutators, so \(K'\le Z(G)\) and \(K\) has class at most two. Centrality now makes
\[
[s,t]^p=[s^p,t]=1.
\]

This still only covers generators and their pair commutators, so arbitrary products require a separate step. Since \(S\) is inverse-closed, write any \(k\in K\) as \(s_1\cdots s_n\) with \(s_i\in S\). Induct on \(n\). If \(a=s_1\cdots s_{n-1}\), then \([s_n,a]\) is a product of central pair commutators and has order dividing \(p\). The class-two formula gives
\[
(a s_n)^p=a^p s_n^p [s_n,a]^{\binom p2}=1,
\]
because \(p\mid\binom p2\) for odd \(p\). Therefore
\[
\exp K\mid p.
\]
This derivation does not assume its conclusion and covers every arbitrary product in \(K\).

### Audit C: quotient relation and isolation of the unique extreme coordinate

Let \(H=G/K\). Normality was established above, and \(H\) has exponent dividing \(p\) because every \(p\)-th power lies in \(K\). For \(x,y\in G\), collect
\[
1=[\bar y,\bar x^p]
\]
in \(H\). For a coordinate whose \(X\)-degree is \(r<p\), the integral binomial expansion at the \(X\)-parameter \(p\) is divisible by \(p\), so that factor dies in the exponent-\(p\) group \(H\). If \(r=p\), the class bound \(r+s\le p+1\) forces \(s=1\).

There is exactly one Hall basis element of multidegree \((p,1)\): the multigraded Witt rank is
\[
\frac1{p+1}\binom{p+1}{p,1}=1.
\]
Its coefficient is a unit, not merely an unverified Hall-polynomial constant. Indeed, modulo the subgroup generated by commutators containing at least two copies of \(Y\), put \(c_k=[Y,{}_{k}X]\). Induction from \(u^X=u[u,X]\) gives
\[
[Y,X^m]\equiv\prod_{k\ge1}c_k^{\binom mk}.
\]
Hence the unique \((p,1)\) coordinate in \([Y,X^p]\) is \(\binom pp=1\) (or \(-1\) after a different Hall orientation). All other collected factors are already trivial in \(H\), so the unique extreme commutator itself is trivial in \(H\). Therefore
\[
[y,{}_{p}x]\in K,
\]
and the same argument after swapping \(x,y\) handles multidegree \((1,p)\). This step uses no uniqueness of Hall coordinates inside \(H\); after the other ordered factors individually die, the displayed group identity has only one factor left.

### Audit D: return to \([x^p,y^p]\)

Collect \([x^p,y^p]\) in \(G\). Every non-extreme coordinate is divisible by \(p^2\) and vanishes because \(\exp G\mid p^2\). Each of the two extreme coordinates is divisible by \(p\), and its underlying unique basic commutator lies in \(K\) by Audit C; it therefore vanishes because \(\exp K\mid p\). Thus
\[
[x^p,y^p]=1\qquad(x,y\in G).
\]

The proposed lemma survives this hostile audit. It is a class-bounded partial result only: it adds the layer \(\operatorname{cl}(G)=p+1\) to the previously reviewed class-at-most-\(p\) family and does not answer the unrestricted Kourovka scope.

## First obstruction at class \(p+2\)

The quotient-isolation step, not merely a vague “extra term,” is the first point at which the above proof no longer closes. In an exponent-\(p\) quotient of class at most \(p+2\), collection of \([y,x^p]=1\) still kills every coordinate of \(X\)-degree below \(p\), but now both multidegrees
\[
(p,1)\quad\text{and}\quad(p,2)
\]
fit under the class bound. The integral formula does not force the latter coordinates to be divisible by \(p\): their binomial expansion may contain the term with \(X\)-index \(p\) and \(Y\)-index 1. Moreover the free-Lie component of multidegree \((p,2)\) has rank
\[
\frac1{p+2}\binom{p+2}{p,2}=\frac{p+1}{2},
\]
so uniqueness of the surviving coordinate is lost.

This is an actual collection phenomenon already at \(p=3\), not just a degree-count possibility. In class at most 5 put
\[
c_1=[y,x],\quad c_2=[c_1,x],\quad c_3=[c_2,x],\quad d=[c_2,c_1].
\]
Here \(d\) has multidegree \((3,2)\), weight 5, and is central. Direct conjugation and collection give
\[
\begin{aligned}
y^x&=yc_1,\\
y^{x^2}&=yc_1^2c_2,\\
y^{x^3}&=y c_1(c_1c_2)^2(c_2c_3)
          =y c_1^3c_2^3c_3d,
\end{aligned}
\]
and hence
\[
[y,x^3]=c_1^3c_2^3c_3d.
\]
In an exponent-3 quotient the relation reduces to \(c_3d=1\), not to \(c_3=1\). Thus the current proof can only couple the extreme \((3,1)\) factor to a terminal \((3,2)\) factor. Extra exponent relations might still kill or cancel both; no class-\(p+2\) truth claim is made.

The terminal-subgroup argument itself is not being silently extrapolated. At class \(p+2\), \(\gamma_{p+1}\) is no longer central in \(G\), so its class-\(p+1\) proof cannot simply be copied. A repair would have to use the additional \(p\)-divisibility of the weight-\(p+1\) coordinates and check commutation with power generators. That repair is outside this assigned lemma and is unnecessary once quotient isolation has already failed.

- `2026-08-16T14:32:47Z` — cumulative active minutes: `112` (16 minutes in this block). Completed the terminal-exponent, integral-coordinate, unique-coordinate, and class-\(p+2\) obstruction audits. Current candidate passes the source constraints only for the explicitly narrower class-at-most-\(p+1\) family; unrestricted row `21.137-odd-forall-p-G` and conclusion row `21.137-odd-P-abelian` remain open outside that family.

## Final cycle disposition

- `2026-08-16T14:36:27Z` — work stopped at cumulative active minutes `115/180`: `19` active minutes used in this block, within the assigned 60-minute cap. No waiting time was charged.
- Exactly one outcome: `PARTIAL_RESULT`.
- Submitted artifact: `findings.md`, tagged `status/conjectured`, with all seven canonical constraint rows and `active_assignment_answered: no`.
- Validator report: `Agents/Kourovka/bus/inbox/Validator/2026-08-16T143515Z__Problem-21.137__REPORT__partial-class-p-plus-one-hall-lemma.md`.
- Lead report: `Agents/Kourovka/bus/inbox/Lead/2026-08-16T143515Z__Problem-21.137__REPORT__partial-class-p-plus-one-hall-lemma.md`.
- The processed Lead decision was marked done and moved to `Agents/Kourovka/bus/archive/2026-08-16T141529Z__Lead__DECISION__switch-proof-audit-class-p-plus-one.md` as required by the file-bus protocol.
- No claim-check JSON or state-checker run was made because this is a class-bounded `PARTIAL_RESULT`, not a `CLAIM` or `STALE_MATCH`, and the assignment forbade computation.

### Remaining command/output ledger

6. `find Agents/Kourovka/bus/inbox/Problem-21.137 ... | sort` listed the current inbox filenames. Only the assigned 14:15:29 Lead decision was opened in this run; older historical files remained unopened under the curated boundary. The archive collision check returned `ARCHIVE_COLLISION=no`.
7. The two file-bus reports were created by patch application. Real result: both patch additions returned success and the referenced files exist in Validator's and Lead's inboxes.
8. The assigned Lead decision's frontmatter was changed from `status: unread` to `status: done` and it was moved to the archive. Real output: `MOVED_TO_ARCHIVE=yes`.
9. Final readback displayed `findings.md` and the audit tail of `log.md`; no missing section or unintended context read was observed.
10. Final `kv_now` output: `2026-08-16T14:36:27Z`.
11. Final handoff presence check tested the two run artifacts, both inbox reports, and the archived Lead decision. Real output: all five paths returned `PRESENT`; none returned `MISSING`.
