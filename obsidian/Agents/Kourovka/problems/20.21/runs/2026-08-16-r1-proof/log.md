---
title: "Problem 20.21 clean constructive run log"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/extensions
  - project/kourovka
  - status/draft
problem: "20.21"
scope_id: "20.21/two-index-twelve-kernels"
assignment_revision: 1
direction: proof
context_mode: clean
---

# Run log

## Active-time ledger

- 2026-08-16T11:56:01Z — work start; cumulative active minutes brought forward from the assignment: 43. Current run actions: protocol, scope, safe-brief, inbox, source, and corpus audit.

## Staleness check

### Source and corpus audit

- Source PDF resolved only through `_meta/agents/Kourovka/paths.env`.
- Visually inspected rendered PDF page 148, not merely `pdftotext` output.
- Corrected transcription from the rendering:

  > **20.21.** (G. Verret). Does there exist a finite group \(G\) with two normal subgroups \(K\) and \(L\), each with index \(12\) in \(G\), such that \(K\) is isomorphic to \(L\), but \(G/K\) is isomorphic to \(C_{12}\), while \(G/L\) is isomorphic to \(A_4\)? (M. Conder)

- `source_transcription_checked: yes`
- Corpus record flags: `answered: false`; `has_editor_comment: false`; `has_later_comment: false`.
- Locator note: the JSONL corpus row records `page: 150`, whereas the canonical scope and the rendered PDF page containing the statement are page 148. The mathematical transcription agrees; this is a locator-metadata discrepancy, not a statement discrepancy.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`
- Per `DISCOVERY_BLIND: yes`, no open-web, arXiv, current-edition, or local solution-bearing-history search was performed. Thus no literature result is asserted to answer any row below.

### Clause matrix

| source clause | equivalent formulation | active scope? | literature-status comparison |
|---|---|---:|---|
| There exists a finite group \(G\) with normal \(K,L\), both of index 12, with \(K\cong L\), \(G/K\cong C_{12}\), and \(G/L\cong A_4\). | There are surjections \(\alpha:G\twoheadrightarrow C_{12}\) and \(\beta:G\twoheadrightarrow A_4\) whose kernels are abstractly isomorphic (and hence both have index 12). | yes — this is exactly `20.21/two-index-twelve-kernels` | deferred; no result inspected in this discovery-blind run |

- There is one source question and one active clause. The excluded variants—nonnormal kernels, wrong indices, or wrong quotient types—are not equivalent to it.
- `active_scope_checked: yes`

### Admissibility and conclusion checklist

| constraint_id | source requirement | canonical requirement | reconciliation |
|---|---|---|---|
| `20.21-exists-GKL` | existential triple \((G,K,L)\) | one triple satisfying all rows | match |
| `20.21-G-finite` | \(G\) finite | \(G\) finite | match |
| `20.21-KL-normal` | \(K,L\trianglelefteq G\) | both normal | match; automatic if exhibited as kernels, but must still be stated |
| `20.21-both-index-12` | each has index 12 | \([G:K]=[G:L]=12\) | match |
| `20.21-kernels-isomorphic` | \(K\cong L\) | abstract group isomorphism | match; equality/order equality alone is insufficient |
| `20.21-quotient-K-C12` | \(G/K\cong C_{12}\) | same | match |
| `20.21-quotient-L-A4` | \(G/L\cong A_4\) | same | match |
| `20.21-existence-conclusion` | affirmative existence | at least one such triple exists | match |

- All source quantifiers, object-class restrictions, normality conditions, exact indices, abstract-isomorphism condition, quotient types, and the requested conclusion are represented. No parameter, prime, exponent, or order condition occurs beyond these rows.
- Canonical `independent_scope_audit.required` is `true` and its status is `passed`, with Validator identified as auditor. The assignment revision and all eight supplied constraint IDs exactly match the canonical record.
- **Independent scope audit gate: passed.** No scope mismatch blocks mathematics.

## Strategy portfolio

Ranked by expected information per remaining active hour:

1. **Structured construction — equivariant index-four kernel pair.** Seek a finite 2-group \(P\), epimorphisms \(f:P\twoheadrightarrow C_4\) and \(h:P\twoheadrightarrow V_4\), and \(\sigma\in\operatorname{Aut}(P)\) of order 3 such that
   \[
   f\sigma=f,\qquad h\sigma=\tau h,
   \]
   where \(\tau\) cycles the three nonzero elements of \(V_4\), and such that \(\ker f\cong\ker h\). Then for \(G=P\rtimes_\sigma C_3\),
   \[
   G/\ker f\cong C_4\times C_3\cong C_{12},\qquad
   G/\ker h\cong V_4\rtimes_\tau C_3\cong A_4.
   \]
   This is the first strategy because success has a compact presentation or permutation certificate and no catalogue growth is needed. Initial kill criterion: if targeted extension families through order \(2^6\) force nonisomorphic kernels by elementary invariants, change the representation rather than enlarge a blind bound.
2. **Theoretical mode — Goursat/extension reduction.** For any candidate, combine the two quotient maps. Their image is a subdirect product of \(C_{12}\) and \(A_4\). The only common quotients are \(1\) and \(C_3\), so the image is either the full product (order 144) or the fibre product over \(C_3\) (order 48). In the latter case the fibre product is isomorphic to \(C_4\times A_4\), and the two kernel images over the common intersection are \(V_4\) and \(C_4\). This explains the index-four 2-group construction above. A reusable exact obstruction or extension classification would count as a partial result.
3. **Catalogue/small-case mode — targeted, not blind.** If needed, enumerate only a finite parametrised family of 2-group extensions/presentations selected by Strategy 1, testing automorphism equivariance and kernel isomorphism. A negative result would exclude only that declared family and order bound, not all finite groups. No GAP/Sage/catalogue job will run without a current Lead lease.
4. **Alternative structured mode — noncentral amalgam.** Build two copies of a common 2-group kernel as normal index-four subgroups in a larger 2-group, then extend an order-three automorphism. This is qualitatively different from enumerating existing groups and may be attacked through class-two presentations or cocycles.

### Certificate plan

- Give \(P\) by an explicit finite presentation or faithful permutation generators, and give formulas for \(f,h,\sigma\).
- Independently enumerate the resulting finite set of normal forms (or the permutation group) to establish finiteness and order.
- Exhibit generators for \(K=\ker f\) and \(L=\ker h\), together with an explicit isomorphism checked on defining relations and a surjectivity/order argument.
- Verify \(\sigma^3=1\), \(f\sigma=f\), and \(h\sigma=\tau h\); then verify the two quotient presentations as \(C_{12}\) and \(A_4\).
- Validator can reconstruct the same object from the presentation/permutations without trusting a discovery script or opaque database identifier.

## First constructive reduction

Let \(P\), \(f\), \(h\), and \(\sigma\) satisfy Strategy 1 and write \(C_3=\langle s\rangle\). Define
\[
\alpha:P\rtimes\langle s\rangle\longrightarrow C_4\times C_3,
\quad \alpha(p s^i)=(f(p),s^i),
\]
and
\[
\beta:P\rtimes\langle s\rangle\longrightarrow V_4\rtimes_\tau C_3,
\quad \beta(p s^i)=(h(p),s^i).
\]
The two equivariance identities make these homomorphisms; both are onto. Their kernels are respectively \(\ker f\) and \(\ker h\), viewed inside \(P\). Therefore isomorphic kernels give the desired triple. This is a sufficient construction template, not yet a witness.

### Early family check

The tempting abelian kernel model \(H=C_4\times C_2\) has isomorphic order-two subgroups whose quotients are respectively \(V_4\) and \(C_4\), but it cannot carry the required order-three action on the \(V_4\) quotient: automorphisms preserve the unique nonzero quotient coset consisting only of involutions. Thus this is an `OUT_OF_SCOPE_EXAMPLE`/design near miss, not a candidate.

- 2026-08-16T12:01:45Z — cumulative active minutes: approximately 49. Portfolio and sufficient equivariant reduction recorded; Math Expert question sent while construction work continues.

## Thirty-minute self-check

- The assignment brought forward 43 active minutes, so the first available clean-context self-check is recorded now.
- Active target remains exactly revision 1 of `20.21/two-index-twelve-kernels`; no excluded scope has been substituted.
- Current hypothesis: a witness may be obtained from an equivariant pair of index-four kernels in a finite 2-group \(P\).
- Evidence: the semidirect-product reduction above is a direct homomorphism calculation; it is sufficient but does not assert existence of \(P\).
- Representation assessment: productive. It converts two order-12 quotient requirements into a finite 2-group extension/automorphism problem and yields a direct certificate route.
- Candidate status: no candidate exists yet, so no admissibility row is claimed to pass. The abelian \(C_4\times C_2\) near miss is explicitly out of scope.

## One-hour checkpoint

- **Active scope/revision:** `20.21/two-index-twelve-kernels`, revision 1, proof direction.
- **New facts:** (i) the combined quotient has only the full-product or common-\(C_3\) fibre-product form; (ii) the fibre product is \(C_4\times A_4\); (iii) the sufficient equivariant 2-group reduction gives the desired \(G=P\rtimes C_3\) immediately; (iv) the smallest abelian near miss cannot support the required \(C_3\)-action.
- **Current named strategy:** equivariant index-four kernel pair.
- **What it ruled out:** the naive abelian central-amalgam model based on \(C_4\times C_2\); it also prevents undirected growth of a SmallGroups bound.
- **Bottleneck:** find one nonabelian 2-group \(P\) whose two index-four kernels are isomorphic and are stabilized by the same order-three automorphism with different quotient actions.
- **Alternative A:** derive a class-two presentation backwards from two isomorphic kernel embeddings and solve the automorphism relations by hand.
- **Alternative B:** use coprime-action/Frattini-module theory to prove an obstruction for abelian \(P\) and narrow the nonabelian structure before any further computation.
- **Recommended next experiment (bounded):** targeted GAP scan of 2-groups of orders 16, 32, and 64 only. Filter first for isomorphic normal index-four kernels with quotients \(C_4,V_4\); only then compute the ordered-pair stabilizer in the automorphism group and test its Sylow-3 elements for the two induced actions. This fits within 20 minutes of wall time and produces an exact family-level certificate or a concrete witness.
- **Kill criterion:** if there is no witness through order 64, or automorphism-group construction becomes the dominant cost, stop the scan; do not extend to order 128. Pivot to the class-two presentation/cocycle formulation.
- **Admissibility status:** there is no current candidate. Consequently none of the eight scope rows is marked pass/proved, and no `CLAIM` is permitted.
- 2026-08-16T12:05:41Z — cumulative active minutes: approximately 53. Early one-hour checkpoint sent because the next choice requires a compute lease; only cheap script design and hand analysis continue pending Lead.

## Leased computation 1

- Lead granted compute slot 2 through 2026-08-16T13:08:10Z for exactly one run of:

  ```bash
  timeout 1200s gap -q Agents/Kourovka/problems/20.21/runs/2026-08-16-r1-proof/scratch/search-equivariant-p.g
  ```

- Executed once. Tool wall time: 1.648386206 seconds; shell exit code: 0. The exit code is not a successful mathematical run: GAP aborted on the first filtered pair because `OnPoints` has no method for a subgroup acted on by an automorphism.
- Exact observed stdout/stderr:

  ```text
  GAP_VERSION 4.12.1
  COVERAGE orders=[16,32,64]
  CRITERION quotient(P/K)=C4; quotient(P/L)=V4; K~=L; sigma order 3 stabilizes K\
  ,L; sigma is identity mod K and nonidentity mod L
  Syntax warning: Unbound global variable in Agents/Kourovka/problems/20.21/runs\
  /2026-08-16-r1-proof/scratch/search-equivariant-p.g:24
      indexFour := Filtered(normals, N -> Index(P, N) = 4);
                                                ^
  Syntax warning: Unbound global variable in Agents/Kourovka/problems/20.21/runs\
  /2026-08-16-r1-proof/scratch/search-equivariant-p.g:26
        N -> IdGroup(FactorGroup(P, N)) = [4, 1]);
                                 ^
  Syntax warning: Unbound global variable in Agents/Kourovka/problems/20.21/runs\
  /2026-08-16-r1-proof/scratch/search-equivariant-p.g:28
        N -> IdGroup(FactorGroup(P, N)) = [4, 2]);
                                 ^
  ORDER_START 16 groups=14
  Error, no method found! For debugging hints type ?Recovery from NoMethodFound
  Error, no 1st choice method found for `^' on 2 arguments at /usr/share/gap/lib/methsel2.g:249 called from
  act( pnt, id ) at /usr/share/gap/lib/oprt.gd:438 called from
  TestIdentityAction( acts, pnt, act ) at /usr/share/gap/lib/oprt.gd:834 called from
  CallFuncList( StabilizerFunc, arg ) at /usr/share/gap/lib/oprt.gi:3041 called from
  Stabilizer( A, K, OnPoints
   ) at Agents/Kourovka/problems/20.21/runs/2026-08-16-r1-proof/scratch/search-e\
  quivariant-p.g:38 called from
  <function "unknown">( <arguments> )
   called from read-eval loop at Agents/Kourovka/problems/20.21/runs/2026-08-16-r1-proof/scratch/search-equi\
  variant-p.g:71
  type 'quit;' to quit to outer loop
  Reading file "Agents/Kourovka/problems/20.21/runs/2026-08-16-r1-proof/scratch/\
  search-equivariant-p.g" has been aborted.
  ```

- What this proves: nothing about any group or bounded family. The scan did not complete order 16 and therefore has zero declared coverage.
- Static repair made after the run: replace `OnPoints` by the explicit subgroup-image action `(N,a) -> Image(a,N)`, following installed GAP library examples. The repaired script has **not** been executed.
- Slot 2 is released; a fresh lease is required for any rerun.
- Operational note: the two processed inbox messages were changed to `status: done`, but moving them into `Agents/Kourovka/bus/archive/` failed with the real output `Read-only file system`. No archive content was inspected.
- Protocol incidents: two auxiliary pure-reasoning helpers independently launched unrequested in-memory GAP enumerations. Neither had a Lead-approved exact command. Both were stopped from further compute, and none of those outputs is used as evidence or as a basis for a mathematical conclusion. Only their hand arguments are eligible for inspection.
- 2026-08-16T12:18:59Z — cumulative active minutes: approximately 66. Failed leased run documented; slot release and corrected-rerun request sent.

## Leased computation 2 — completed bounded result

- Lead granted a fresh slot-2 lease through 2026-08-16T12:48:12Z after static inspection of the repaired action.
- Exact command, executed exactly once:

  ```bash
  timeout 1200s gap -q Agents/Kourovka/problems/20.21/runs/2026-08-16-r1-proof/scratch/search-equivariant-p.g
  ```

- Final exit status: 0. GAP-reported runtime: 110835 ms. The job completed well before the hard timeout and printed all three `ORDER_DONE` markers.
- Exact observed output, concatenated in arrival order:

  ```text
  GAP_VERSION 4.12.1
  COVERAGE orders=[16,32,64]
  CRITERION quotient(P/K)=C4; quotient(P/L)=V4; K~=L; sigma order 3 stabilizes K\
  ,L; sigma is identity mod K and nonidentity mod L
  Syntax warning: Unbound global variable in Agents/Kourovka/problems/20.21/runs\
  /2026-08-16-r1-proof/scratch/search-equivariant-p.g:24
      indexFour := Filtered(normals, N -> Index(P, N) = 4);
                                                ^
  Syntax warning: Unbound global variable in Agents/Kourovka/problems/20.21/runs\
  /2026-08-16-r1-proof/scratch/search-equivariant-p.g:26
        N -> IdGroup(FactorGroup(P, N)) = [4, 1]);
                                 ^
  Syntax warning: Unbound global variable in Agents/Kourovka/problems/20.21/runs\
  /2026-08-16-r1-proof/scratch/search-equivariant-p.g:28
        N -> IdGroup(FactorGroup(P, N)) = [4, 2]);
                                 ^
  ORDER_START 16 groups=14
  ORDER_DONE 16 cumulative_groups=14 cumulative_filtered_pairs=
  16 cumulative_aut_builds=16 cumulative_witnesses=0 runtime_ms=569
  ORDER_START 32 groups=51
  ORDER_DONE 32 cumulative_groups=65 cumulative_filtered_pairs=
  234 cumulative_aut_builds=234 cumulative_witnesses=0 runtime_ms=7927
  ORDER_START 64 groups=267
  ORDER_DONE 64 cumulative_groups=332 cumulative_filtered_pairs=
  1887 cumulative_aut_builds=1887 cumulative_witnesses=0 runtime_ms=110835
  FINAL groups=332 filtered_pairs=1887 aut_builds=1887 witnesses=0 runtime_ms=
  110835
  ```

### Exact coverage and meaning

- Coverage: every GAP SmallGroups-library group of each exact order 16, 32, and 64 (14, 51, and 267 groups; 332 total).
- Software/library identification: GAP 4.12.1; SmallGrp 1.5.3 (installed `PackageInfo.g` date 16 May 2023).
- Discovery-script SHA-256 measured after the successful run (the script was not edited after that run): `f476dab18c9ffa5f139e183f5bac831f6ab7efc96f64372e74940ca97bc25c1c`.
- For each group, the script enumerated every normal subgroup of index four; selected every ordered pair \((K,L)\) with quotients \(C_4,V_4\) and exact `IdGroup` equality of the two kernels; stabilized the ordered pair in the full automorphism group; and tested order-three elements in a Sylow 3-subgroup for identity action modulo \(K\) and nonidentity action modulo \(L\).
- There were 1,887 filtered ordered pairs. None passed the automorphism-action criterion.
- Why one Sylow 3-subgroup suffices for each pair stabilizer: every order-three element is conjugate within that stabilizer into the chosen Sylow subgroup, and the properties “identity modulo \(K\)” and “nonidentity modulo \(L\)” are preserved under conjugation by automorphisms stabilizing both \(K\) and \(L\).
- **Bounded conclusion:** no equivariant index-four-kernel construction of the stated form exists with \(|P|\in\{16,32,64\}\). This says nothing about \(|P|\ge128\), about non-2-groups \(P\), about nonequivariant constructions, or about the original Kourovka scope outside this sufficient template.
- The syntax warnings are lexical warnings about top-level loop variables captured in filter closures; all completed-order markers and the final line were observed. No runtime error occurred.
- **Kill criterion met:** the bounded SmallGroups strategy stops here. It will not be enlarged to order 128. Representation-changing pivot: class-two presentation/cocycle analysis.
- Slot 2 released immediately by `REPORT` to Lead.
- 2026-08-16T12:27:30Z — cumulative active minutes: approximately 75.

## Class-two/cocycle pivot: structural obstruction

The following argument concerns the sufficient equivariant 2-group template, not every possible solution of the original problem.

Let
\[
K=\ker f,\qquad L=\ker h,\qquad N=K\cap L.
\]
Both \(K\) and \(L\) are \(\sigma\)-invariant. The image \(h(K)\) is invariant under the irreducible order-three action \(\tau\) on \(V_4\), hence is either \(0\) or \(V_4\). It cannot be zero: then \(K\le L\), and equal indices give \(K=L\), contradicting the nonisomorphic quotient types. Consequently
\[
h(K)=V_4,\qquad K/N\cong V_4.
\]
Because \(|K|=|L|\), also \([L:N]=4\). The restriction \(f|_L\) has kernel \(N\), so
\[
L/N\cong C_4,
\]
and \(P=KL\).

### Lemma: the two kernels cannot be abelian

Assume that \(K\) is abelian and choose an abstract isomorphism \(\theta:K\to L\). Put \(J=\theta^{-1}(N)\). Then
\[
J\cong N,\qquad K/J\cong L/N\cong C_4.
\]
On the other hand, \(\alpha=\sigma|_K\) stabilizes \(N\) and induces the irreducible order-three automorphism on \(K/N\cong V_4\).

Let \(2^t\) annihilate \(K\), choose \(u\) with \(3u\equiv1\pmod{2^t}\), and use the coprime-action idempotent
\[
e=u(1+\alpha+\alpha^2).
\]
It splits \(K=K_0\oplus K_1\), where \(\alpha=1\) on \(K_0\), while \(\alpha^2+\alpha+1=0\) on \(K_1\). The irreducible quotient kills \(K_0\) and is an epimorphic module map
\[
K_1\twoheadrightarrow R/(2),
\qquad R=(\mathbb Z/2^t\mathbb Z)[\omega]/(\omega^2+\omega+1).
\]
The finite \(R\)-module \(K_1\) is a direct sum of modules \(R/(2^{e_i})\). Smith reduction of the epimorphism to \(R/(2)\) replaces one summand \(R/(2^e)\) by \(R/(2^{e-1})\). Since the underlying abelian group of \(R/(2^e)\) is \(C_{2^e}\times C_{2^e}\), the invariant factors of \(N\) are obtained from those of \(K\) by lowering two equal factors \(C_{2^e}\) to \(C_{2^{e-1}}\).

For a finite abelian 2-group \(X\), let \(r_s(X)\) be the number of cyclic invariant factors whose order is at least \(2^s\). The preceding paragraph gives, for some \(e\),
\[
r_e(K)-r_e(N)=2. \tag{1}
\]

But dualizing \(0\to J\to K\to C_4\to0\) gives
\[
0\to C_4\to \widehat K\to \widehat J\to0.
\]
Finite abelian groups have the same invariant-factor type as their character duals, so \(J\) has the type of a quotient of \(K\) by one cyclic subgroup. Quotienting by a cyclic subgroup can decrease every \(r_s\) by at most one: on the elementary layer \(2^{s-1}K/2^sK\), the kernel introduced by one cyclic subgroup has dimension at most one. Hence
\[
r_s(K)-r_s(J)\le1 \quad\text{for every }s. \tag{2}
\]
Since \(J\cong N\), (1) and (2) contradict each other. Therefore \(K\), and hence \(L\), is nonabelian.

### Consequences and limits

- The equivariant template cannot use an abelian \(P\) or abelian target kernels.
- If \(|P|=32\), then \(|K|=8\). The nonabelian possibilities are \(D_8\), whose automorphism group has no element of order three, and \(Q_8\); the latter's unique order-two subgroup has quotient \(V_4\), never the required \(C_4\) under the transported intersection. Thus hand analysis already forces \(|P|\ge64\).
- The completed bounded computation strengthens this only **inside the template** to \(|P|\ge128\).
- None of these statements rules out a witness in the full-product Goursat branch, a fibre-product witness not arising from a 2-group complement as above, or a larger equivariant \(P\).

This lemma is being sent to Validator as a partial mathematical subclaim; until independently checked it remains `status/conjectured` reasoning, not certified fact.

### Corollary: central intersection is impossible

In the template, \(K/N\cong V_4\) and \(L/N\cong C_4\). If \(N\le Z(P)\), then \(N\le Z(L)\). Since \(L/N\) is cyclic, \(L/Z(L)\) is cyclic, which forces \(L\) to be abelian. Then \(K\cong L\) is abelian, contradicting the preceding lemma. Hence
\[
N=K\cap L\not\le Z(P).
\]
Thus a central-product or central-cocycle construction cannot realize this template.

### Proposition: split elementary-abelian intersection is impossible

Let \(N\cong C_2^d\), and suppose the two preimages split as
\[
K=N\rtimes V_4,\qquad L=N\rtimes C_4
\]
for arbitrary actions. Write \([N,Q]\) for the subspace generated by \(n^{-1}n^q\).

Because the complements are abelian,
\[
K'=[N,V_4],\qquad L'=[N,C_4].
\]
If \(K\cong L\), equality of derived-subgroup orders forces
\[
\dim [N,V_4]=\dim [N,C_4]. \tag{3}
\]
For a finite 2-group \(X\), the minimal generator number is \(d(X)=\dim_{\mathbb F_2}X/\Phi(X)\). Here
\[
\Phi(K)=[N,V_4],
\]
because \(N\) and the \(V_4\) complement have exponent two, whereas
\[
\Phi(L)=[N,C_4]\langle t^2\rangle
\]
for a complement generator \(t\) of order four. Consequently
\[
d(K)=\dim N/[N,V_4]+2,
\qquad
d(L)=\dim N/[N,C_4]+1.
\]
Equation (3) makes the two coinvariant dimensions equal, so \(d(K)=d(L)+1\), contradicting \(K\cong L\). Therefore no split elementary-abelian-module construction works, regardless of module dimension or chosen actions.

This kills the natural linear semidirect family \(P=N\rtimes(C_4\times A_4)\). A live class-two/cocycle strategy must now use a nonsplit extension and a noncentral, non-elementary (or nonabelian) intersection; simply increasing a matrix dimension cannot succeed.

## Control correction

- Lead correction received at 2026-08-16T12:38:00Z: no further internal or unrostered delegates may be spawned, consulted, or retained.
- Action: all such delegation stopped. The two helper computations remain quarantined non-evidence; no helper output is used in the bounded result, structural proofs, or subsequent reasoning. Further outside perspectives are requested only through the auditable file bus.
- No GAP, Sage, solver, or enumeration will run without a fresh exact Lead lease.

### Quarantine addendum

- The section `### Lemma: the two kernels cannot be abelian`, its order consequence, and `### Corollary: central intersection is impossible` were prompted by an unrostered helper's hand argument before Lead's correction. Even though the text was checked and expanded locally, Lead's instruction is controlling: **those sections are quarantined non-evidence and must not support any outcome or future inference in this run**.
- The corresponding Validator requests dated `2026-08-16T122731Z` and the central-intersection portion of `2026-08-16T123056Z` are withdrawn by a correction message.
- The split elementary-abelian proposition was derived separately from the Frattini and derived-subgroup formulas. To keep provenance clean, it is restated from scratch in `scratch/split-elementary-obstruction.md`; only that standalone note is eligible for review.
- The Goursat reduction, sufficient semidirect template, and separately leased 332-group screen predate and do not use either helper output; they remain eligible evidence.

## Personal cocycle derivation after the control correction

- Starting only from the eligible equivariant identities, a fresh Goursat argument is written in `scratch/equivariant-goursat-reduction.md`.
- It shows that the combined map \((f,h):P\to C_4\times V_4\) must be onto: the only proper subdirect possibility is a fibre product over \(C_2\), but its order-two kernel in \(V_4\) cannot be invariant under the 3-cycle \(\tau\).
- Hence a targeted constructor must build an extension of \(C_4\times V_4\) with an order-three lift of \(1\times\tau\) and isomorphic coordinate preimages.
- Together with the standalone split elementary-abelian obstruction, this says the next parameter family must be genuinely nonsplit (or use non-elementary kernel data), not merely a larger linear semidirect product.

### Scope-wide Goursat reduction

- A standalone proof applying to every hypothetical target triple is in `scratch/original-goursat-reduction.md`.
- With \(N=K\cap L\), exactly two combined quotients can occur: \(G/N\cong C_{12}\times A_4\), with \(K/N\cong A_4\), \(L/N\cong C_{12}\); or \(G/N\cong C_4\times A_4\), with \(K/N\cong V_4\), \(L/N\cong C_4\).
- This is a necessary two-branch extension reduction for the original scope, not merely for the sufficient semidirect template.

## Live post-partial strategy

- Named approach: nonsplit \(C_2^3\)-by-\((C_4\times V_4)\) factor-set search with an order-three lift.
- Specific next step: enumerate the finite action/cohomology/lift data at exact order 128 described in `scratch/nonsplit-order-128-family.md`, filter the two coordinate preimages by exact invariants, and construct an explicit isomorphism only for survivors.
- Reason for expected information: order 128 is the first unscreened order in the template, the common kernel then has exact order eight, and \(C_2^3\) makes all nonsplit factor-set equations finite linear algebra while escaping the proved split obstruction.
- Abandonment condition: exhaust every compatible action and cohomology class for \(N=C_2^3\) with exact coverage and no invariant-matched isomorphic pair. A negative outcome applies only to this declared family.
- No computation was launched; any implementation requires a fresh exact Lead lease.

### Action-layer reduction

- Personally derived after the control correction: for \(N=C_2^3\), the action and order-three lift combine to a homomorphism \(C_4\times A_4\to GL(3,2)\).
- The \(A_4\)-image is \(1\), \(C_3\), or faithful \(A_4\). In the two nontrivial cases its centralizer in \(GL(3,2)\) has odd order (respectively 3 or 1), forcing the commuting \(C_4\)-action to be trivial.
- When the \(A_4\)-image is trivial, the \(C_4\)-image has order 1, 2, or 4. Thus only a small finite action list reaches the second-cohomology stage.
- Full hand argument and limitations: `scratch/order-128-action-layer.md`.

## Math Expert response

- Current-inbox report received at 2026-08-16T12:44:48Z: Math Expert's fresh computation-free audit found no hidden problem in the equivariant semidirect template and agreed that equivariance forces the combined \(C_4\times V_4\) quotient.
- Strategy advice: parametrize remaining objects with genuinely noncentral/nonabelian extension data rather than repeating central or split elementary families.
- Clean-context handling: only the current inbox summary was read. Its linked `ideas/` note was not opened. This report is used as portfolio advice, not as certification or as revival of quarantined helper-derived material.

### Portfolio adjustment from the audited advice

- Priority next family is now \(N\cong Q_8\) at exact \(|P|=128\), described in `scratch/nonsplit-q8-order-128-family.md`; the elementary-abelian family remains a secondary bounded option.
- Personal outer-action reduction: since \(Out(Q_8)\cong S_3\), a homomorphism \(C_4\times A_4\to Out(Q_8)\) has only three types: \(A_4\to C_3\) with trivial \(C_4\), or trivial \(A_4\) with \(C_4\to1\) or \(C_2\).
- This leaves a finite nonabelian factor-set/obstruction problem with center \(Z(Q_8)=C_2\), followed by exact comparison of the two coordinate preimages.
- Since \(H^2(C_4\times C_2\times C_2,C_2)\) has dimension six, each unobstructed outer action contributes 64 cohomology classes, at most 192 before compatible-automorphism and order-three-lift filtering.
- The quotient 3-cycle has a two-dimensional fixed subspace on this \(H^2\): it fixes the \(C_4\) degree-two class and the line \(\langle y^2+yz+z^2\rangle\), with no fixed mixed class. Thus each affine extension torsor has zero or at most four invariant classes, at most 12 across the three outer-action types before the cube-one lift and kernel-isomorphism tests.

### Q8 family exhausted by centers

- A complete hand exclusion of the exact \(|P|=128\), \(N\cong Q_8\) family is in `scratch/q8-order128-exclusion.md`.
- The \(V_4\)-preimage is either \(Q_8\times V_4\), with center \(C_2^3\), or \(Q_8\circ Q_8\), with center \(C_2\).
- For outer-trivial \(C_4\), the other preimage is \(Q_8\times C_4\), with center \(C_2\times C_4\), or \(Q_8\circ C_8\), with center \(C_8\). For nontrivial outer \(C_4\)-action its center has order four. No center types match.
- Therefore no class in any of the three outer-action families can have isomorphic coordinate preimages. No computation was used.

### D8 family exhausted by the same invariant

- A complete hand exclusion of the exact \(|P|=128\), \(N\cong D_8\) family is in `scratch/d8-order128-exclusion.md`.
- Here \(Out(D_8)\cong C_2\), so \(A_4\) acts outer-trivially and \(C_4\) acts outer-trivially or through \(C_2\).
- The \(V_4\)-preimage has center \(C_2^3\) or \(C_2\). The \(C_4\)-preimage has center \(C_2\times C_4\), \(C_8\), \(C_2^2\), or \(C_4\). Again no center types match.
- Thus both nonabelian groups of order eight are excluded as the common kernel at the first unscreened order.

## Lead decision completed

- Decision received at 2026-08-16T12:50:23Z: finish a hand-checkable parametrization of all three \(Q_8\) outer-action types and their order-three-invariant factor sets, ending in a bounded command request or structural obstruction.
- Completed by structural obstruction, with no computation: `scratch/nonsplit-q8-order-128-family.md` gives the three outer actions and cohomology bound; `scratch/q8-order128-exclusion.md` shows every restriction pair has incompatible centers.
- The same independently written center analysis also excludes the \(D_8\) common-kernel family. A result report was sent to Lead.

## Presentation correction and cycle closeout

- 2026-08-16T12:55:07Z — Lead correction received: Validator passed the necessary two-branch Goursat reduction, with one presentation-only repair requested.
- Replaced the malformed string `le` by the intended relation `\\le` in the first subdirect-product display of `scratch/original-goursat-reduction.md`. Every mathematical claim and limitation is unchanged. The correction message is marked `done`.
- The quaternion- and dihedral-kernel exclusions remain tagged `status/conjectured` pending independent Validator review. No positive witness was found, so no scope constraint is claimed to pass and no claim-check JSON is appropriate.
- 2026-08-16T12:57:51Z — work stop; cumulative active minutes approximately 105, including the 43 minutes brought forward in the assignment. Approximately 32 allotted active minutes remain unused. The cycle closes early because the Lead-directed \(Q_8\) family reached a structural kill criterion and the next disjoint family would require a new bounded implementation and compute lease.
- Exactly one cycle outcome: `PARTIAL_RESULT`. Final report sent to Lead at `Agents/Kourovka/bus/inbox/Lead/2026-08-16T125751Z__Problem-20.21__REPORT__PARTIAL_RESULT-clean-constructive-cycle.md`.
