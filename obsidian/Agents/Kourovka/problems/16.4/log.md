---
title: "Problem-16.4 cycle 1 log"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/conjugacy-classes
  - project/kourovka
  - status/draft
problem_id: "16.4"
cycle: 1
active_budget_minutes: 180
started_utc: 2026-08-12T00:56:37Z
safety_stop_utc: 2026-08-12T03:56:37Z
source_transcription_checked: yes
---

# Working log

## 2026-08-12T03:15:43Z — work start

Cumulative active minutes at start: 0. Inbox was empty.

## Staleness check

Corpus record: `kourovka-20-corpus.jsonl`, id 16.4, issue 16 (2006), recorded printed page 93; `answered: false`, `has_editor_comment: false`, `has_later_comment: false`. In the configured current PDF the statement is on PDF/printed page 95 (pagination differs from the old corpus record).

Visually inspected the rendered page 95 at 170 dpi, not merely `pdftotext`. Correct transcription:

> **16.4.** Let \(G\) be a finite group with \(C,D\) two nontrivial conjugacy classes such that \(CD\) is also a conjugacy class. Can \(G\) be a non-abelian simple group? — Z. Arad

The typography confirms that \(CD\) is the setwise product of the two classes and that “nontrivial” modifies both \(C\) and \(D\). There are no extra quantifiers, parts, comments, or formula decorations.

`source_transcription_checked: yes`.

Literature searches performed before mathematics:

- exact statement fragments (`"Let G be a finite group" "CD is also a conjugacy class" simple group`);
- `"product of two conjugacy classes" "non-abelian simple" Arad`;
- `Kourovka 16.4 Z. Arad conjugacy classes product`;
- arXiv/current-web searches for `Arad-Herzog conjecture`, including 2023–2026;
- checked the configured current Kourovka PDF directly: 16.4 is still printed without an answer/comment;
- checked the March 2026 update search result; no update to 16.4 was located.

Negative staleness conclusion: no solution was found. The problem is the Arad–Herzog conjecture and remains described as open in a 2022 paper and in a recent Bourbaki survey available in search results. Relevant partial results:

- R. M. Guralnick, G. Malle, P. H. Tiep, *Products of conjugacy classes in finite and algebraic simple groups*, arXiv:1202.2627 / Trans. AMS 365 (2013): proves the conjecture for various families; in Lie type, excludes the case where both classes are semisimple or both unipotent. <https://arxiv.org/abs/1202.2627>
- J. Moori, H. P. Tong-Viet, *Products of conjugacy classes in simple groups*, Quaest. Math. 34 (2011), 433–439, DOI 10.2989/16073606.2011.640452: verifies several families. <https://doi.org/10.2989/16073606.2011.640452>
- A. Beltrán, M. J. Felipe, C. Melchor, *An Arad and Fisman’s Theorem on Products of Conjugacy Classes Revisited*, Mediterr. J. Math. 19 (2022), article 257: explicitly calls the general statement long-standing and treats related special hypotheses. <https://doi.org/10.1007/s00009-022-02171-7>

Thus this is not stale; bounded computation must be reported only as bounded evidence.

## 2026-08-12T03:17:19Z — computational setup and exact criterion

GAP is installed: command `gap -q -c 'Print(GAPInfo.Version,"\\n");QUIT;'` printed `4.12.1`. CTblLib later reported version `1.3.7`.

For conjugacy classes \(K_i,K_j\), the character-table class multiplication coefficient \(n_{ijk}\) is the number of pairs \((x,y)\in K_i\times K_j\) with \(xy=z\), for a fixed \(z\in K_k\). It is constant on \(K_k\). Hence

\[
K_iK_j=K_k\quad\Longleftrightarrow\quad
n_{ijk}>0\ \text{and}\ n_{ij\ell}=0\text{ for every }\ell\ne k.
\]

Equivalently, the support of the class-algebra product has exactly one class. This is an exact decision from an ordinary character table, not a sampling heuristic. The standard character formula is

\[
n_{ijk}=\frac{|K_i||K_j|}{|G|}
\sum_{\chi\in\operatorname{Irr}(G)}
\frac{\chi(g_i)\chi(g_j)\overline{\chi(g_k)}}{\chi(1)}.
\]

Cheap consequences useful for checks: if \(K_iK_j=K_k\), then counting all pairs gives \(|K_i||K_j|=n_{ijk}|K_k|\); also fixing one factor gives \(|K_i|,|K_j|\le |K_k|\). These are necessary, not sufficient.

## 2026-08-12T03:18Z — bounded character-table screen

Created `scratch/screen_tables.g` and ran exactly:

```text
timeout 55s gap -q Agents/Kourovka/problems/16.4/scratch/screen_tables.g | tee Agents/Kourovka/problems/16.4/scratch/screen_tables.out
```

It terminated normally in about 2.2 wall seconds. For every ordered pair of nonidentity classes, the script computed all class multiplication coefficients and selected supports of size one. Exact output is in `scratch/screen_tables.out`.

Tables tested (number of ordered nonidentity pairs in parentheses): A5 (16), L2(7) (25), A6 (36), L2(8) (64), L2(11) (49), A7 (64), L2(13) (64), L2(17) (100), A8 (169), L3(3) (121), U3(3) (169), M11 (81), L2(19) (121), L2(23) (169), M12 (196), J1 (196), L2(25) (196), L2(27) (225), Sz(8) (100), L3(4) (81).

Observed result: every table printed `[]`; no ordered pair of nontrivial classes in any of these 20 named simple-group character tables has a single-class product.

What this establishes: exact exclusion for the particular ordinary character tables named above, assuming CTblLib's tables. What it does not establish: the conjecture for all finite simple groups, a classification-free argument, or even exhaustive coverage of all simple tables available in CTblLib. An attempted call `AllCharacterTableNames(IsSimple,true)` was capped at 20 seconds and produced no output before timeout, so no coverage claim is made from it.

## 2026-08-12T03:20Z — process-cap blocker

Sent `BLOCKER` to Lead: the session became active at 03:15Z with cumulative active time 0 but the supplied safety stop is 03:56:37Z, so the 180-minute cycle cannot be completed in this process. Requested a resumed cycle/new safety cap. Continued bounded work pending reply.

## 2026-08-12T03:22Z — literature reduction sharpened

Read the theorem statements in Guralnick–Malle–Tiep rather than relying only on the abstract. Their results give:

1. alternating simple groups are excluded;
2. every simple \(\operatorname{PSL}_d(q)\) is excluded (arbitrary rank and field size);
3. simple groups of Lie type of rank less than 4 are excluded;
4. if \(a^Gb^G=c^G\) in a finite simple group of Lie type, then \(c\) is neither semisimple nor unipotent; moreover \(a,b\) cannot both be semisimple and cannot both be unipotent.

Source: R. M. Guralnick, G. Malle, P. H. Tiep, arXiv:1202.2627, Theorems 1.5, 1.6, 1.8 and Corollary 1.7. The recent Bourbaki survey restates the surviving general conjecture and the coverage as alternating groups, \(\operatorname{PSL}_n(q)\), and Lie type of rank below 4.

Consequently the genuinely uncovered locus is much narrower than “all simple groups”: apart from already-computational sporadics, it lies among non-type-A finite simple groups of Lie rank at least 4, with any hypothetical output class mixed (nontrivial semisimple and unipotent Jordan parts), and with input classes not both semisimple or both unipotent. A useful resumed computation should target mixed-class products in the first uncovered families (for example symplectic/unitary/orthogonal rank 4), rather than repeat alternating or PSL cases.

Also extracted the stronger necessary character identity (GMT Lemma 2.2): if \(CD\) is one conjugacy class, then for every \(\chi\in\operatorname{Irr}(G)\) and every \(x\in C,y\in D\),

\[
\chi(x)\chi(y)=\chi(1)\chi(xy).
\]

This supplies a cheap disproof certificate: one irreducible character and one pair \((x,y)\) violating the identity excludes that class pair. It is stronger operationally than first constructing every structure constant.

## 2026-08-12T03:21Z — selected rank-4 table screen

Created `scratch/screen_rank4.g` to target six non-type-A groups at the edge of the literature reduction and ran:

```text
timeout 55s gap -q Agents/Kourovka/problems/16.4/scratch/screen_rank4.g | tee Agents/Kourovka/problems/16.4/scratch/screen_rank4.out
```

The explicit cap fired before the last two tables. Completed exact results:

- `S8(2)`: 81 classes, all 6,400 ordered nonidentity class pairs tested, no hit;
- `O8+(2)`: 53 classes, all 2,704 pairs tested, no hit;
- `O8-(2)`: 39 classes, all 1,444 pairs tested, no hit;
- `U5(2)`: 47 classes, all 2,116 pairs tested, no hit.

`U5(3)` and `S8(3)` were named in the script but did not print a result before timeout, so **no result is claimed for them**. Exact observed output is in `scratch/screen_rank4.out`. The four completed exclusions are table-specific bounded evidence, not a general rank-4 theorem.

A subsequent separately capped 30-second `U5(3)` run printed only the setup line (`150` classes and `22,201` ordered nonidentity pairs) before timeout, not a final hit list. Its partial output is `scratch/screen_U5_3.out`; it establishes no exclusion and is retained only to size a future optimized computation.

Sent a file-bus question to Validator asking what independent check is needed to certify the bounded table exclusions, and a question to MathExpert asking for the sharpest uncovered-family target.

## 2026-08-12T03:22:56Z — work stop (blocked on process cap)

Cumulative active minutes: 7. No waiting time charged. The source/staleness gate is complete, literature reduction and reproducible bounded screens are recorded, but the 180-active-minute cycle is not complete. Parked pending Lead's decision on a resumed process with a usable safety cap; no `CLAIM`, `REPORT: PROMISING`, or `REPORT: DEAD` is issued because doing so after seven active minutes would violate the timing contract.

## 2026-08-12T17:00:48Z — work resumed

Cumulative active minutes at resume: 7/180. New safety stop: `2026-08-12T18:48:03Z`. Read and processed Lead's reactivation dispatch. Task: inspect standing-agent replies, sharpen the uncovered-family computation, then request a heavy-compute lease if warranted.

## 2026-08-12T17:03Z — sharpened uncovered-family task

No standing-agent reply was present; the earlier MathExpert and Validator questions remain unread in their queues.

The first concrete target is `U5(3)`, a non-type-A rank-4 simple-group character table with 150 conjugacy classes and 22,201 ordered nonidentity class pairs. This sits outside the broad alternating/PSL/rank-below-4 exclusions recorded above. Created `scratch/screen_early_exit.g`: for each ordered class pair it tests class multiplication coefficients and stops once two nonzero output classes are found, which exactly disproves singleton support for that pair. It prioritizes possible singleton classes satisfying the necessary size/divisibility constraints, but still examines all classes when needed, so the optimization does not weaken the conclusion.

Sent Lead a heavy-compute lease request for a one-core, under-1-GB, 1,200-second-capped U5(3) run. No heavy computation started pending approval.

## 2026-08-12T17:04Z — optimization validation and structural consequences

Validated `screen_early_exit.g` on `A5`: all 16 ordered nonidentity pairs were excluded after 38 coefficient calls, reproducing the earlier result. Then benchmarked it on `S8(2)` under a 55-second cap: all 6,400 pairs were excluded after 15,976 coefficient calls and the command completed in 1.6 wall seconds, reproducing the earlier full-support result. Output: `scratch/screen_early_exit_S8_2.out`. This checks that early exit does not create false singleton hits on two previously completed tables and suggests the leased U5(3) task is feasible.

Further exact consequences of a hypothetical \(A=a^G,B=b^G,C=c^G\) with \(AB=C\), useful for both proof and computation:

- Since \(aB\subseteq C\) and \(Ab\subseteq C\), \(|A|,|B|\le |C|\), equivalently \(|C_G(a)|,|C_G(b)|\ge |C_G(c)|\).
- Uniform fiber counting gives an integer \(m\ge1\) with \(|A||B|=m|C|\), hence
  \[
  m=\frac{|G|\,|C_G(c)|}{|C_G(a)|\,|C_G(b)|}.
  \]
- GMT Lemma 2.2 implies the character-column identity
  \(\chi(c)=\chi(a)\chi(b)/\chi(1)\) for every irreducible \(\chi\). Thus every irreducible character vanishing on \(a\) or \(b\) must vanish on \(c\), and column orthogonality yields
  \[
  |C_G(c)|=\sum_{\chi\in\operatorname{Irr}(G)}
  \frac{|\chi(a)|^2|\chi(b)|^2}{\chi(1)^2}.
  \]

These are necessary conditions only. The open status shows they cannot presently be treated as a general contradiction, but they define cheap filters and potential family-specific certificates.

## 2026-08-12T17:05Z — U5(3) counts (subsequently found already covered)

Using `OrdersClassRepresentatives(CharacterTable("U5(3)"))` in defining characteristic 3 gave 149 nonidentity classes split as: 80 semisimple (order prime to 3), 6 unipotent (nonidentity 3-power order), and 63 mixed (order divisible by 3 and by another prime). The distinct mixed orders observed are 6, 12, 18, 21, 24, 36, 42, 84.

Combining only GMT Corollary 1.7/Theorem 1.8, the same-type exclusions would leave 15,765 ordered input pairs and force output among the 63 mixed classes. **Correction at 17:12Z:** this is not a genuinely residual literature case, because GMT Proposition 3.1 proves the full conjecture for `U_n(q)` for `3 <= n <= 6`. The counts are retained as observed data, but the earlier “uncovered” characterization is withdrawn.

## 2026-08-12T17:08Z — refreshed-cap blocker

Sent Lead a blocker noting that 173 remaining active minutes cannot fit between the 17:00:48Z resume and 18:48:03Z safety stop (about 107 wall minutes). Work continues within this window, but another resume will be required unless Lead explicitly terminates the cycle earlier on its mathematical outcome.

## 2026-08-12T17:12Z — literature correction and actual first uncovered target

Search inspection of the full GMT Section 3 statements found:

- Proposition 3.1: the conjecture holds for `U_n(q)` with `3 <= n <= 6` (apart from the nonsimple `(3,2)` exception);
- Proposition 3.2: it holds for `S4(q)`, `S6(q)`, `O8+(q)`, and `O8-(q)`;
- Proposition 3.3 covers the listed low-rank exceptional families.

Therefore U5(3), U5(4), O8±(3), and the earlier O8±(2) computations do not extend published family coverage. The first uncovered classical series suggested by these propositions is `S8(q)=PSp8(q)` (type C4). The completed `S8(2)` computation is thus relevant table-specific evidence. The next target `S8(3)` has 278 classes: 44 nonidentity semisimple, 31 nonidentity unipotent, and 202 mixed classes in characteristic 3. GMT's same-type theorems leave 73,832 residual ordered input pairs and require any hypothetical output to be mixed.

Withdrew the U5(3) lease request before launch and sent a corrected 20-minute capped lease request for S8(3). This correction illustrates why a table's rank alone was insufficient: GMT's unitary proposition reaches Lie rank 5, while its symplectic proposition stops below C4.

CTblLib metadata check: `CharacterTable("S8(2)")` has identifier `S8(2)`, size 47,377,612,800, and `IsSimple=true`; `CharacterTable("S8(3)")` has identifier `S8(3)`, size 65,784,756,654,489,600, and `IsSimple=true`. Thus both tables represent the intended finite simple targets rather than covers or automorphism groups.

## 2026-08-12T17:15Z — MathExpert response processed

MathExpert independently ranked `S8(3)=PSp8(3)` as the first one-hour residual target, subject to Lead's lease. Suggested order: strict centralizer/class-size filters, then GMT character-column identities, and full structure constants only for survivors; desired output is a cheap witness character per rejected pair. Kill criterion: abandon the one-hour computation if an initial five-minute pilot cannot certify 10,000 residual pairs or if column-compatible survivors lack a bounded full-support plan. Read the linked idea note and archived the processed inbox message.

The current `screen_early_exit.g` instead uses the exact weak size/divisibility filter and structure constants with early exit. This is robust and already benchmarked. A witness-character implementation could make the certificate more compact, but is not required for exact exclusion; it remains a possible optimization if the leased pilot is slow.

## 2026-08-12T17:16Z — character-column implementation

Implemented MathExpert's suggested order in `scratch/screen_character_columns.g`. For each ordered nonidentity pair \((i,j)\), it first retains only output classes satisfying the necessary size/divisibility constraints, then tests the exact GMT identity \(\chi_i\chi_j=\chi(1)\chi_k\) for every irreducible table row. Pairs with no compatible output are rigorously excluded without structure coefficients. Any survivors are resolved by exact class multiplication coefficients, stopping at two nonzero output classes.

Validated on A5: all 16 ordered pairs were rejected by the column identities alone, with zero coefficient calls, agreeing with both earlier screens. Updated the pending S8(3) lease request to use this implementation. The script records all column-compatible survivors and a final exact hit list, so a timeout still leaves auditable row progress.

## 2026-08-12T17:18Z — 2026 partial-result check

Found a relevant post-PDF paper, but not a solution of 16.4: C. Parker and J. Saunders, *Expansion of normal subsets of odd-order elements in finite groups*, J. London Math. Soc. 113 (2026), e70534, DOI `10.1112/jlms.70534`, arXiv:2507.07529. Its Theorem A says: if a normal subset \(K\) consists of odd-order elements and \(K^2\subseteq \mathbf D_K\), its rational closure, then \(\langle K\rangle\) is soluble. Corollary 1.3 says that if \(K,D\) are conjugacy classes, elements of \(K\) have odd order, and \(K^n=D\cup D^{-1}\) for \(n\ge2\), then \(\langle K\rangle\) is soluble.

Consequences for a nonabelian simple hypothetical counterexample (special cases only):

- If \(A=B\) consists of odd-order elements and \(A^2=C\subseteq\mathbf D_A\), impossible, since \(\langle A\rangle=G\) would be soluble.
- If \(A=B\) consists of odd-order elements and the singleton output class \(C\) is real, then \(A^2=C=C\cup C^{-1}\), so Corollary 1.3 excludes it.

This does **not** handle unequal input classes, even-order inputs, or nonreal output outside the rational closure, so it does not make the Kourovka problem stale. It is an additional theoretically excluded slice that a family computation can label rather than rediscover.

## 2026-08-12T17:19Z — Validator responses processed

Validator checked the strict-size lemma line by line and judged it valid as a hand-checked reduction, not a solution. The required implicit fact is satisfied: in a nonabelian simple group, each nonidentity conjugacy class has more than one element. Updated the S8(3) character-column screen to use the strict candidate condition \(|K_k|>\max(|K_i|,|K_j|)\), while retaining the divisibility condition.

For replication of bounded CTblLib exclusions, Validator requires a second independently written computation that recomputes coefficients directly from the irreducible-character formula, records GAP/CTblLib versions and table identifiers, and compares the complete coefficient matrix (or a collision-resistant digest plus exceptions). Merely rerunning either existing script is insufficient. Direct multiplication in an explicit manageable representation would be stronger. Any replication would still certify only the named tables, not a family theorem.

Unit-tested the direct character formula independently on A5 classes `(2,2)`. For output classes `k=1..5`, the directly evaluated exact cyclotomic sums gave coefficients `15,2,3,5,5`, respectively, identical to `ClassMultiplicationCoefficient`: observed lines were `1:15:builtin=15` through `5:5:builtin=5`. This validates the formula implementation on one row only; it is **not** the complete independent recomputation Validator requires.

Both Validator messages were marked done and archived. An independent formula implementation is a secondary target after the primary S8(3) lease; it should not consume the lease unless the first screen completes with sufficient time.

## 2026-08-12T17:21Z — multiplicity-one reduction via Szep's theorem

Let \(m\) be the uniform number of factorizations \(c=ab\) with \((a,b)\in A\times B\), assuming \(AB=C\). In a nonabelian simple group, \(m\ne1\), hence \(m\ge2\).

Argument: if the fiber over fixed \(c=ab\) is the singleton \((a,b)\), conjugation by \(C_G(c)\) preserves that fiber, so every element of \(C_G(c)\) centralizes both \(a\) and \(b\). Thus
\[
C_G(c)=C_G(a)\cap C_G(b).
\]
The equality \(|A||B|=|C|\) for \(m=1\) becomes
\[
|G|\,|C_G(c)|=|C_G(a)|\,|C_G(b)|.
\]
Consequently
\[
|C_G(a)C_G(b)|=
\frac{|C_G(a)|\,|C_G(b)|}{|C_G(a)\cap C_G(b)|}=|G|,
\]
so \(G=C_G(a)C_G(b)\). This contradicts the proved Szep conjecture (Fisman–Arad): a finite nonabelian simple group is not the product of centralizers of two nonidentity elements. Citation checked: E. Fisman and Z. Arad, *A proof of Szep's conjecture on nonsimplicity of certain finite groups*, J. Algebra 108 (1987), no. 2, 340–354, DOI `10.1016/0021-8693(87)90107-4`.

Therefore a hypothetical singleton output must satisfy the strengthened counting filter
\[
|A||B|=m|C|\quad\text{with integer }m\ge2.
\]
Added this to `screen_character_columns.g` as `sizes[i]*sizes[j] >= 2*sizes[k]` after divisibility. This remains only a candidate filter, not a general contradiction.

## 2026-08-12T17:25:56Z — work stop pending Lead lease

Cumulative active minutes: 27/180 (20 active minutes in this resumed segment; polling/waiting not charged). The Lead dispatch has been fulfilled through the pre-compute stage: standing replies were processed, the initially mistaken covered target U5(3) was withdrawn, the sharp residual target was corrected to `S8(3)=PSp8(3)`, and an exact character-column/structure-coefficient screen was implemented and unit-tested. MathExpert independently endorsed the target; Validator checked the strict-size lemma and specified replication requirements.

No heavy job was launched because Lead has not yet granted a compute lease. Parked with the S8(3) lease request and the safety-window blocker unread in Lead's inbox. This is not a cycle outcome and no `CLAIM`, `PROMISING`, or `DEAD` report is issued at 27 active minutes.

## 2026-08-12T17:10Z — elementary strict-size reduction

Derived the following lemma for a hypothetical counterexample in a nonabelian simple group:

> If nontrivial conjugacy classes \(A,B\) satisfy \(AB=C\), where \(C\) is a conjugacy class, then \(|A|<|C|\) and \(|B|<|C|\).

Proof for the first inequality. The easy inclusion \(Ab\subseteq C\) gives \(|A|\le|C|\). Suppose equality. Then \(Ab=C\) for every \(b\in B\). A nontrivial conjugacy class in a centreless simple group has at least two elements, so choose distinct \(b_1,b_2\in B\). From \(Ab_1=Ab_2\) follows \(A(b_1b_2^{-1})=A\). The right setwise stabilizer
\[
H=\{h\in G:Ah=A\}
\]
is a subgroup. It is normal because \(A\) is conjugacy-invariant: conjugating \(Ah=A\) by any \(g\) gives \(A(ghg^{-1})=A\). Thus \(H\) contains the nonidentity element \(b_1b_2^{-1}\), so simplicity gives \(H=G\). But then \(A\) is invariant under all right translations, forcing nonempty \(A=G\), impossible because a nontrivial conjugacy class omits the identity. Hence \(|A|<|C|\). The second inequality follows symmetrically using the left stabilizer (or applying the first argument after reversing factors).

Equivalent centralizer filter:
\[
|C_G(a)|>|C_G(c)|\quad\text{and}\quad |C_G(b)|>|C_G(c)|.
\]

This is a genuine elementary reduction but not a solution: many class triples satisfy the strict size inequalities. Sent Validator a proof-check question before relying on it in reported coverage.

## 2026-08-13T11:21:00Z — work resumed under replacement slot-2 lease

Cumulative active minutes at resume: 27/180, from the audited prior stop entry. Safety stop: `2026-08-13T14:15:00Z`. Read the inbox oldest-first. The 09:45:33Z slot-2 lease had expired before delivery and is void; marked it done without action. Processed Lead's replacement lease expiring at 12:30Z, authorizing exactly the recorded one-core, under-1-GB, 1,200-second-capped `S8(3)` character-column screen. Starting that command now and applying the recorded five-minute/10,000-pair kill criterion.

## 2026-08-13T11:21:43Z — slot-2 computation completed and released

Ran exactly the Lead-authorized command:

```text
timeout 1200s gap -q -c 'name:="S8(3)"; Read("Agents/Kourovka/problems/16.4/scratch/screen_character_columns.g");' > Agents/Kourovka/problems/16.4/scratch/screen_character_columns_S8_3.out 2>&1
```

Observed process result: exit code 0; about 13 wall seconds, far inside both the five-minute kill checkpoint and the 1,200-second cap. Slot 2 is released immediately.

Exact recorded coverage:

- GAP 4.12.1; CTblLib 1.3.7; table identifier `S8(3)`;
- 278 conjugacy classes, hence all \(277^2=76,729\) ordered pairs of nonidentity classes tested;
- all 76,729 pairs rejected by the strict class-size, multiplicity/divisibility, and GMT irreducible-character column conditions;
- zero column-compatible pairs, zero structure-coefficient fallback calls, zero singleton class products;
- output file has 560 lines and SHA-256 `736df30f8c99e223f587ab54390f31ca8b22f8a8519cc7f0b581f3940a49f1fb`.

Final observed lines:

```text
COLUMN_COMPATIBLE_PAIRS=[  ]
FINAL table=S8(3) tested=76729 columnRejected=76729 compatiblePairs=
0 coeffCalls=0 singleClassProducts=[  ]
```

What this establishes: conditional on the checked strict-size lemma and the multiplicity-one/Szep reduction recorded above, the ordinary character table exactly excludes a singleton product for every ordered pair of nonidentity conjugacy classes of the specific finite simple group `S8(3)=PSp8(3)`. It does not prove the Arad–Herzog conjecture for the family `PSp8(q)` or all finite simple groups, and it is not independently replicated.

Cumulative active minutes: 28/180 (rounded up from this sub-minute resumed computation and inspection). Waiting time was not charged.

## 2026-08-13T11:22Z — work stop after lease report

Cumulative active minutes: 28/180. Slot 2 release and exact coverage were reported to Lead through the file bus. Stopped as dispatched; no cycle-level `CLAIM`, `PROMISING`, or `DEAD` outcome is issued because the active-time budget is not exhausted and the result is a bounded exclusion for one group only.
