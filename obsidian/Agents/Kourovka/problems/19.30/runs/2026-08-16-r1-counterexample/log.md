---
title: "Problem 19.30 clean counterexample run r1"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/characters
  - project/kourovka
  - status/draft
---

# Run metadata

- Scope: `19.30/vanishing-order-simple-recognition`
- Assignment revision: 1
- Direction: counterexample
- Active budget: 162 minutes total; 18 minutes already used at assignment handoff
- Clean-context run directory: `Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample`
- Discovery blind: yes
- Independent scope audit: **passed**, recorded in the canonical scope record by Validator before this run (`status: passed`; revision 1).

## Active-time ledger

- 2026-08-16T11:55:31Z — work started; cumulative active minutes at handoff: 18.

## Staleness check

### Source and corpus gates

- Read `_meta/agents/Kourovka/_common-kourovka.md` in full, then the canonical scope record, then the clean `SAFE_CONTEXT_BRIEF`, in the prescribed order.
- The current inbox `Agents/Kourovka/bus/inbox/Problem-19.30/` contained no messages.
- Sourced `_meta/agents/Kourovka/paths.env`; observed `pdf_resolves=yes` and `author_set=yes`.
- Read PDF page 134 with
  `pdftotext -f 134 -l 134 -layout "$KOUROVKA_PDF" -`.
- Rendered that same page at 160 dpi with `pdftoppm` into a temporary directory and visually inspected the PNG. This visual inspection, rather than the text extraction alone, is the basis of the transcription check below.
- The corpus JSONL actually present in this vault is `kourovka-20-corpus.jsonl` (the protocol's named `kourovka-21-corpus.jsonl` path was absent). Its exact 19.30 record reports:
  `answered: false`, `has_editor_comment: false`, `has_later_comment: false`.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
- Open-web search was not used, as required by `DISCOVERY_BLIND: yes`.

### Corrected source transcription

> **19.30.** An element \(g\) of a finite group \(G\) is said to be vanishing if \(\chi(g)=0\) for some irreducible complex character \(\chi\in\operatorname{Irr}(G)\). Must a finite group and a finite simple group be isomorphic if they have equal orders and the same set of orders of vanishing elements?

Proposers rendered immediately below: M. Foroudi Ghasemabadi, A. Iranmanesh.

`source_transcription_checked: yes`

### Clause matrix

| source clause | equivalent formulation | in active scope? | literature status in this blind run |
|---|---|---:|---|
| An element \(g\in G\) is vanishing if \(\chi(g)=0\) for some \(\chi\in\operatorname{Irr}(G)\). | For any finite group \(H\), the vanishing elements are the union of the zero sets of its irreducible complex characters. | yes (`c-definition`) | external search deferred; no source comment |
| Must a finite group and a finite simple group be isomorphic if they have equal orders and the same set of orders of vanishing elements? | For every finite \(G\) and finite simple \(S\), \(|G|=|S|\) and \(V(G)=V(S)\) imply \(G\cong S\), where \(V(H)=\{|x|:x\in H,\ \exists\chi\in\operatorname{Irr}(H),\chi(x)=0\}\). | yes (`c-question`) | external search deferred; corpus flags all negative |

`active_scope_checked: yes`

### Admissibility checklist reconciled to the rendered source

| constraint_id | rendered-source requirement | counterexample obligation | reconciliation |
|---|---|---|---|
| `19.30-forall-GS` | Universal question over qualifying pairs | One qualifying pair refutes the universal implication | exact match |
| `19.30-G-finite` | First group is finite | Exhibit finite \(G\) | exact match |
| `19.30-S-finite-simple` | Second group is finite simple | Exhibit and certify finite simple \(S\) | exact match |
| `19.30-vanishing-definition` | Zero of at least one irreducible complex character | Compute zeros across all irreducible complex characters, class by class | exact match |
| `19.30-equal-orders` | The two groups have equal orders | Certify \(|G|=|S|\) exactly | exact match |
| `19.30-equal-vanishing-order-sets` | Sets of orders of vanishing elements agree | Compare sets only, with no multiplicities | exact match |
| `19.30-isomorphic` | Question asks whether they must be isomorphic | Certify \(G\not\cong S\) | exact match |

All quantifiers, object classes, equality hypotheses, the precise character-theoretic definition, the absence of multiplicities, and the target conclusion agree with the canonical record. No mismatch or ambiguity was found.

## Strategy portfolio

Ranked by expected information per active hour:

1. **Structured-construction mode — exceptional rank-one order matching.** Choose the Suzuki simple family \({}^2B_2(q)=\operatorname{Sz}(q)\), beginning with \(q=8\), and design nonsimple groups of the same order from its visible factorization \(q^2(q^2+1)(q-1)\). Use direct/semidirect products whose character tables are reconstructible from factor tables or orbit data. Kill criterion: no order-matched construction whose vanishing-order support can even plausibly equal the simple table after testing a finite named menu of decompositions/actions.
2. **Catalogue/small-case mode — exact table-library screen for the same named family.** Determine every installed character table whose group order equals each installed Suzuki table in an explicitly bounded parameter list; compute \(V(H)\) from every irreducible row and every conjugacy class. A negative result proves only that no collision occurs among those installed tables at those exact orders. Kill criterion: the order buckets contain only the simple table or no nonsimple table with matching \(V\).
3. **Theoretical mode — direct-product support obstruction.** Derive \(V(A\times B)\) exactly from class orders and the rule that an irreducible tensor character vanishes iff one tensor factor does. Use it to eliminate entire order factorizations without scanning isomorphism types. Kill criterion: the formula gives no restriction sharper than direct computation for the selected factors.
4. **Alternative representation-changing mode — Frobenius/action parameterization.** Encode an order-matched nonsimple group as a Frobenius or semidirect product \(N\rtimes H\); derive vanishing classes from induced characters and action orbits. This is the first pivot if catalogue tables are uninformative. Kill criterion: arithmetic prevents a compatible faithful action, or induced zeros force an order absent from \(V(S)\).

### Certificate plan

For any candidate pair: give explicit reconstructible presentations or standard library identifiers; list group orders; certify simplicity of \(S\) and nonisomorphism (preferably nonsimplicity) of \(G\); save the full class-order vectors and irreducible character matrices; compute each vanishing-order set with a short transparent script; and ask Validator to reproduce the character tables independently. A catalogue negative will instead include the exact installed table names, version, complete order buckets, algorithm, and raw output, while explicitly limiting coverage to that named catalogue.

## 30-active-minute self-check

- 2026-08-16T12:09:05Z — cumulative active minutes: approximately 32 (18 handed off + 14 in this segment).
- Target remains exactly revision 1 of `19.30/vanishing-order-simple-recognition`; no excluded full-spectrum or character-table-equality target has been substituted.
- Current hypothesis: there is no collision at the two installed Suzuki orders. This is a family-level exclusion hypothesis, not an answer to the universal active target.
- Evidence now in hand: exact ordinary-table scans for `Sz(8)` and `Sz(32)`; exact CTblLib size buckets at their two orders; a direct-product obstruction; a normal-cyclic-Hall structural obstruction; and a prospective all-groups recognition reduction using a normal-prime lemma plus the classification of nonabelian simple groups of order prime to 3.
- Representation check: the catalogue screen met its kill criterion (its two exact order buckets contain no comparison table). I therefore pivoted from table-name enumeration to the composition-factor/normal-Sylow representation. That pivot is producing checkable lemmas and remains productive.
- Admissibility: there is no candidate pair. Accordingly no counterexample constraint matrix is asserted. Every object screened does have the exact target order and a finite simple Suzuki member, but no nonsimple object passes the equal-vanishing-set row.

## Exact Suzuki-table computation

Environment observed before the scan:

```text
/usr/bin/gap
GAP_VERSION=4.12.1
CTblLib_loaded=true
SmallGrp_loaded=true
```

The reproducible script is
`Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/suzuki_exact_screen.g`.
Command:

```bash
gap -q 'Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/suzuki_exact_screen.g'
```

It terminated with exit code 0 in 1.80 seconds. Decisive observed output (the script also prints every zero-character index by class):

```text
GAP_VERSION=4.12.1
CTBLLIB_VERSION=1.3.7
IDENTIFIER=Sz(8)
IS_ORDINARY_TABLE=true
IS_SIMPLE=true
SIZE=29120
SIZE_FACTORS=[ 2, 2, 2, 2, 2, 2, 5, 7, 13 ]
NCLASSES=11
NIRR=11
CHARACTER_DEGREES=[ 1, 14, 14, 35, 35, 35, 64, 65, 65, 65, 91 ]
CLASS_ORDERS=[ 1, 2, 4, 4, 5, 7, 7, 7, 13, 13, 13 ]
CLASS_SIZES=[ 1, 455, 1820, 1820, 5824, 4160, 4160, 4160, 2240, 2240, 2240 ]
VANISHING_CLASS_INDICES=[ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]
FIRST_ZERO_CHARACTER_BY_VANISHING_CLASS=[ 7, 7, 7, 4, 2, 2, 2, 8, 8, 8 ]
NONVANISHING_CLASS_INDICES=[ 1 ]
VANISHING_ORDER_SET=[ 2, 4, 5, 7, 13 ]
NONVANISHING_ORDER_SET=[ 1 ]
CHECK_SUM_CLASS_SIZES=29120
CHECK_SUM_DEGREE_SQUARES=29120
IDENTIFIER=Sz(32)
IS_ORDINARY_TABLE=true
IS_SIMPLE=true
SIZE=32537600
SIZE_FACTORS=[ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 31, 41 ]
NCLASSES=35
NIRR=35
CHARACTER_DEGREES=[ 1, 124, 124, 775, 775, 775, 775, 775, 775, 775, 775, 775,
  775, 1024, 1025, 1025, 1025, 1025, 1025, 1025, 1025, 1025, 1025, 1025,
  1025, 1025, 1025, 1025, 1025, 1271, 1271, 1271, 1271, 1271, 1271 ]
CLASS_ORDERS=[ 1, 2, 4, 4, 5, 25, 25, 25, 25, 25, 31, 31, 31, 31, 31, 31, 31,
  31, 31, 31, 31, 31, 31, 31, 31, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41 ]
VANISHING_CLASS_INDICES=[ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
  17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35 ]
FIRST_ZERO_CHARACTER_BY_VANISHING_CLASS=[ 14, 14, 14, 4, 4, 4, 4, 4, 4, 2, 2,
  2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 15, 15, 15, 15, 15, 15, 15, 15, 15,
  15 ]
NONVANISHING_CLASS_INDICES=[ 1 ]
VANISHING_ORDER_SET=[ 2, 4, 5, 25, 31, 41 ]
NONVANISHING_ORDER_SET=[ 1 ]
CHECK_SUM_CLASS_SIZES=32537600
CHECK_SUM_DEGREE_SQUARES=32537600
```

Thus the exact installed ordinary tables give

\[
V(\operatorname{Sz}(8))=\{2,4,5,7,13\},\qquad
V(\operatorname{Sz}(32))=\{2,4,5,25,31,41\}.
\]

Every nonidentity class in each table is vanishing. This does **not** say that any same-order \(G\) must have the same full element-order spectrum, nor that all elements of an order belonging to \(V(G)\) vanish.

## Exact installed-catalogue coverage

The script
`Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/suzuki_catalogue_bucket.sh`
compares `AllCharacterTableNames()` with CTblLib's shipped precomputed `Size` index. It exited 0 in 1.77 seconds. Observed output:

```text
CTBLLIB_SIZE_INDEX=/usr/share/gap/pkg/CtblLib/data/attr_size.json.gz
SIZE_INDEX_RECORDS=2613
TARGET_ORDER_RECORDS
2461:["Sz(32)",32537600],
2463:["Sz(8)",29120],
ALL_CHARACTER_TABLE_NAMES_COUNT=2613
POSITION_SZ8=115
POSITION_SZ32=113
SUZUKI_SUBSTRING_NAMES=[ "2.Sz(8)", "2^2.Sz(8)", "2^2.Sz(8).3", "Sz(32)",
  "Sz(32).5", "Sz(8)", "Sz(8).3", "(2^2xSz(8)):3", "2.(2^2xSz(8)):3",
  "2^12:Sz(8)" ]
```

Exact coverage statement: among all 2,613 ordinary character tables named in installed CTblLib 1.3.7, the order-29,120 bucket is exactly `{"Sz(8)"}` and the order-32,537,600 bucket is exactly `{"Sz(32)"}`. Therefore that installed catalogue contains no nonsimple collision at either order. It does **not** enumerate, or say anything universal about, groups whose ordinary character tables are absent from CTblLib.

The direct GAP query `AllCharacterTableNames(Size,29120)` was also attempted under a 55-second cap before using the precomputed index. Because the optional `Browse` package is absent, it produced no result before the cap; no coverage claim is based on that timed-out query. Observed package message:

```text
#I  browse package is not available. Check that the name is correct
#I  and it is present in one of the GAP root directories (see '??RootPaths')
browse=fail
ctbllib=true
```

## Natural order-matched Borel-product family

For \(q=8,32\), let \(B_q\) denote the standard Suzuki Borel subgroup represented by the installed tables `2^(3+3):7` and `2^(5+5):31`. Then
\(|B_q|=q^2(q-1)\), so \(G_q=B_q\times C_{q^2+1}\) is nonsimple and has exactly \(|\operatorname{Sz}(q)|\).

For finite \(A,B\), irreducible characters of \(A\times B\) are tensors and therefore

\[
V(A\times B)=
\{\operatorname{lcm}(v,n):v\in V(A),\ n\in\omega(B)\}
\cup
\{\operatorname{lcm}(m,w):m\in\omega(A),\ w\in V(B)\}.
\]

Since a cyclic group has no vanishing elements, the second set is empty here. Script:
`Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/suzuki_borel_product.g`.
Observed output (exit 0, 1.81 seconds):

```text
Q=8 BOREL_TABLE=2^(3+3):7 BOREL_ORDER=448 CYCLIC_FACTOR_ORDER=
65 PRODUCT_ORDER=29120
BOREL_SPECTRUM=[ 1, 2, 4, 7 ]
BOREL_VANISHING_ORDERS=[ 7 ]
PRODUCT_VANISHING_ORDERS=[ 7, 35, 91, 455 ]
Q=32 BOREL_TABLE=2^(5+5):31 BOREL_ORDER=31744 CYCLIC_FACTOR_ORDER=
1025 PRODUCT_ORDER=32537600
BOREL_SPECTRUM=[ 1, 2, 4, 31 ]
BOREL_VANISHING_ORDERS=[ 31 ]
PRODUCT_VANISHING_ORDERS=[ 31, 155, 775, 1271, 6355, 31775 ]
```

Both exact-order candidates fail the equality-of-vanishing-order-sets row. They are `OUT_OF_SCOPE_EXAMPLE`s, not counterexamples. The result also illustrates why a direct product is structurally hostile: a vanishing order in one factor combines with every element order of the other factor.

More generally, any matching \(G\) at either Suzuki order has trivial centre and is directly indecomposable. For the centre assertion, if a central prime-order element \(z\) has order \(p\), select a required vanishing element \(x\) of a different prime order \(r\). Schur's lemma gives \(\chi(zx)=\lambda\chi(x)=0\), while \(|zx|=pr\), a forbidden mixed vanishing order. The direct-product formula then excludes every nontrivial decomposition because the four distinct prime orders required in \(V(G)\) cannot all be supplied without producing a mixed vanishing order.

## Structural pivot: a normal-prime obstruction

### Lemma A — normal Sylow prime in a solvable group

Let \(M=p\prod_i r_i^{a_i}\), with \(p\) occurring to exponent one. Suppose
\(p\nmid |\operatorname{GL}_d(r_i)|\) for every \(i\) and every \(1\le d\le a_i\).
Then every solvable group whose order divides \(M\) and is divisible by \(p\) has a normal Sylow \(p\)-subgroup.

Proof under review: induct on the group order. A minimal normal subgroup \(N\) is elementary abelian \(r^d\). If \(r=p\), it is the desired Sylow subgroup. Otherwise the quotient has, inductively, a normal Sylow \(p\)-subgroup. Its preimage \(K\) satisfies \(K/N\cong C_p\). By Schur–Zassenhaus, \(K=N\rtimes P\) for \(P\cong C_p\). The general-linear hypothesis makes the conjugation action of \(P\) on \(N\) trivial, so \(K=N\times P\). Thus \(P\) is the unique Sylow \(p\)-subgroup of \(K\), characteristic in \(K\), and normal in the original group.

### Lemma B — a normal Sylow of prime order is zero-free

If \(P=C_p\triangleleft G\), then no nonidentity element of \(P\) is vanishing. Indeed, Clifford theory gives, for every \(\chi\in\operatorname{Irr}(G)\),
\(\chi_P=e(\lambda_1+\cdots+\lambda_t)\) with the \(\lambda_i\) a single orbit of distinct linear characters of \(P\). At \(x\in P\setminus\{1\}\), this is \(e\) times a sum of \(t\) distinct \(p\)-th roots of unity. A zero sum would give a nonzero \(0/1\)-coefficient polynomial of degree at most \(p-1\) divisible by \(\Phi_p=1+X+\cdots+X^{p-1}\), forcing the orbit to contain all \(p\) roots. But a conjugation orbit on \(\operatorname{Irr}(P)\) cannot mix the trivial character with nontrivial ones; hence this is impossible. Therefore \(\chi(x)\ne0\) for every irreducible \(\chi\).

### Arithmetic instances

The script
`Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/normal_prime_arithmetic.g`
exited 0 and printed:

```text
ORDER_MOD_13_OF_2=12
ORDER_MOD_41_OF_2=20
ORDER_MOD_41_OF_5=20
41_DIVIDES_GL1_31=false
```

- At order \(29120=2^6\cdot5\cdot7\cdot13\), take \(p=13\). The only relevant dimensions are \(d\le6\) over \(\mathbb F_2\), and \(d=1\) over \(\mathbb F_5,\mathbb F_7\). Thus Lemma A makes \(C_{13}\) normal in every solvable group of this order, and Lemma B gives \(13\notin V(G)\).
- At order \(32537600=2^{10}\cdot5^2\cdot31\cdot41\), take \(p=41\). The relevant dimensions are \(d\le10\) over \(\mathbb F_2\), \(d\le2\) over \(\mathbb F_5\), and \(d=1\) over \(\mathbb F_{31}\). Thus Lemma A makes \(C_{41}\) normal in every solvable group of this order, and Lemma B gives \(41\notin V(G)\).

The exact simple tables instead give \(13\in V(\operatorname{Sz}(8))\) and \(41\in V(\operatorname{Sz}(32))\). Hence no solvable same-order group can collide with either simple group.

### Remaining composition-factor dependency

The standard classification consequence needed to turn the preceding solvable exclusion into an all-groups recognition theorem is:

> Every nonabelian finite simple group whose order is not divisible by 3 is a Suzuki group \({}^2B_2(2^{2m+1})\), \(m\ge1\).

Both target orders are prime to 3. At order 29,120, a nonabelian composition factor can only be `Sz(8)`; at order 32,537,600, `Sz(8)` does not divide the order (its primes 7 and 13 are absent), `Sz(32)` has the full order, and larger Suzuki groups are too large. Consequently a nonsimple group of either target order would have only abelian composition factors and hence be solvable. Combined with Lemmas A and B, this would prove recognition for `Sz(8)` and `Sz(32)`.

This final composition-factor step is mathematically plausible and has survived an internal adversarial check, but it still needs Validator/MathExpert to confirm the theorem statement and supply a proper citation. It is therefore recorded as a **conjectured partial result**, not certified fact and not an answer to the universal active target.

As independent computational support for the `Sz(8)` composition-factor step, GAP's perfect-group catalogue was screened at every divisor of 29,120 using
`scratch/perfect_divisor_screen_29120.g`. Observed output:

```text
DIVISOR_COUNT=56
UNSUPPORTED_DIVISOR_ORDERS=[  ]
NONZERO_PERFECT_COUNTS=[ [ 1, 1 ], [ 29120, 1 ] ]
ORDER_29120_PERFECT_GROUP_1_STRUCTURE=Sz(8)
ORDER_29120_PERFECT_GROUP_1_IS_SIMPLE=true
```

This is exact coverage of the installed perfect-group catalogue at all 56 divisor orders, with no unsupported divisor query. It supports the reduction because the last nontrivial derived subgroup of a nonsolvable finite group is perfect. It is not substituted for a cited mathematical classification theorem. `NumberPerfectGroups(32537600)` returned `fail`, so no analogous database coverage is claimed for the `Sz(32)` order.

## Constructor family with normal Hall odd subgroup at order 29,120

Every group with a normal Hall odd subgroup has that subgroup isomorphic to `C455`: the order is square-free and no prime among 5, 7, 13 divides another minus one. Schur–Zassenhaus therefore writes the group as `C455 ⋊ P`, where `|P|=64` (there are 267 isomorphism types of such \(P\), though the argument is uniform in \(P\) and in the action).

If an action-image element acts nontrivially on one Sylow factor of `C455` but trivially on another factor `C_r`, choose a linear character of the kernel moved by that image and a nonidentity element of `C_r` fixed by it. Clifford induction then produces a zero on a commuting product of even and odd order, giving a forbidden mixed vanishing order. Avoiding that forces every nonidentity action-image element to act nontrivially on all three cyclic prime factors. Projection to the 2-part of `Aut(C7)\cong C6` is then injective, so the image has order at most two; its nonidentity element is simultaneous inversion. In either the trivial or inversion case, an irreducible restriction to `C455` is a multiple of either one linear character or `\lambda+\lambda^{-1}`. At an odd-order kernel element these values cannot be zero. Thus none of 5, 7, 13 belongs to the vanishing-order set, and no member of this entire action family can collide with `Sz(8)`.

The normal-prime Lemma B strictly subsumes the order-13 part of this constructor exclusion once solvability is known. This family remains useful as a direct, classification-free representation-changing check over every action and every complement of order 64.

An explicit representative `C455 : C64` with the cyclic generator acting by inversion was constructed successfully in GAP (`act_is_hom=true`, `size=29120`, `structure=C455 : C64`). Its generic character-table computation did not finish under the imposed 55-second unleased cap; the process was stopped by `timeout`, and no unobserved vanishing set is reported.

## Procedural compute correction

- 2026-08-16T12:10Z — Lead corrected the compute interpretation: every GAP, Sage, solver, catalogue, or enumeration command requires a lease, irrespective of observed runtime. I stopped all further such commands immediately.
- The earlier commands above were actually run and the quoted outputs were actually observed, but they are **procedurally provisional** because no slot was rostered. They must not be treated as lease-compliant evidence until independently rerun under a current lease.
- Lead received an acknowledgement and an exact bounded request for `timeout 120s bash Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/leased_evidence_rerun.sh` (one CPU, <512 MB, five-minute lease). No rerun will occur absent an explicit grant.
- The correction message was changed to `status: done`. The required move to `bus/archive` failed with the observed output `Read-only file system`; it remains in the current inbox without being reread or otherwise using excluded archive context.

## Explicit symbolic near miss (no computation)

Let
\[
A=C_{455},\qquad H=C_4\times C_2^4,
\]
choose a homomorphism \(\varepsilon:H\to C_2\) that is nonzero on a \(C_2\)-coordinate, and let \(H\) act on \(A\) by
\(a^h=a\) for \(h\in K=\ker\varepsilon\) and \(a^h=a^{-1}\) for \(h\notin K\). Set \(G=A\rtimes H\). Then \(|G|=455\cdot64=29120=|\operatorname{Sz}(8)|\), and \(G\) is nonsimple.

The irreducible characters are reconstructed without a black-box table:

1. The 64 characters inflated from \(G/A\cong H\) are linear and never zero.
2. For every inversion pair \(\{\lambda,\lambda^{-1}\}\) of nontrivial characters of \(A\), and every \(\mu\in\operatorname{Irr}(K)\), inducing the extension \(\lambda\otimes\mu\) from \(AK=A\times K\) gives an irreducible character of degree two.
3. These account for all characters because
   \(64+((455-1)/2)|K|\cdot2^2=64+227\cdot32\cdot4=29120\).
4. Every induced degree-two character is zero on \(A(H\setminus K)\). At \(ak\in AK\) it has value
   \(\mu(k)(\lambda(a)+\lambda(a)^{-1})\), which is nonzero: \(\lambda(a)\) has odd order, whereas \(z+z^{-1}=0\) would force \(z\) to have order four.

Thus the vanishing elements are exactly \(A(H\setminus K)\). For \(h\notin K\), inversion gives \((ah)^2=h^2\), so \(|ah|=|h|\in\{2,4\}\). Choosing \(\varepsilon\) nonzero on a \(C_2\)-coordinate ensures both orders occur (an outside element in that coordinate has order two, and multiplying it by a generator of the \(C_4\) factor gives order four). Therefore

\[
V(G)=\{2,4\}.
\]

This is an exact `OUT_OF_SCOPE_EXAMPLE`: it passes finiteness, equal order, finite simplicity of the comparison group, exact vanishing-definition calculation, and nonisomorphism, but fails `19.30-equal-vanishing-order-sets` because it misses 5, 7, and 13. It is useful as a designed near miss matching the complete even part of \(V(\operatorname{Sz}(8))\).

Variants: with \(H=C_2^6\), any nonzero \(\varepsilon\) gives \(V(G)=\{2\}\); with \(H=C_4\times C_2^4\) and \(\varepsilon\) supported only on the \(C_4\)-parity, every element outside \(K\) has order four and \(V(G)=\{4\}\).

## Conjectured arithmetic recognition criterion for prime-exponent Suzuki groups

This is a partial theorem under review, not the active universal claim.

Let \(n\ge3\) be an odd prime, \(q=2^n\), and
\[
S=\operatorname{Sz}(q),\qquad
M=|S|=q^2(q-1)(q^2+1).
\]
Assume there is a prime \(p\) such that:

1. \(p\mid q^2+1\), \(v_p(M)=1\), and \(\operatorname{ord}_p(2)=4n\);
2. for each other prime power \(r^a\parallel M\), one has
   \(p\nmid |\operatorname{GL}_d(r)|\) for every \(1\le d\le a\);
3. the standard Suzuki character formula supplies an irreducible character of degree \(q^2+1\).

Then every finite group \(G\) with \(|G|=|S|\) and \(V(G)=V(S)\) is isomorphic to \(S\).

### Why no smaller nonsolvable composition factor occurs

The order \(M\) is not divisible by 3. Under the standard classification consequence that every nonabelian finite simple group of order prime to 3 is a Suzuki group, a nonabelian composition factor of \(G\) must be \(\operatorname{Sz}(2^m)\) for odd \(m\ge3\).

Suppose \(m<n\). By Zsigmondy's theorem, \(2^m-1\) has a prime divisor \(r\) with \(\operatorname{ord}_r(2)=m\) (there is no exception for odd \(m\ge3\)). If \(|\operatorname{Sz}(2^m)|\) divided \(M\), then \(r\) would divide either \(2^n-1\) or \(2^{2n}+1\). The first forces \(m\mid n\). The second gives \(m\mid4n\), and since \(m\) is odd it again forces \(m\mid n\). Because \(n\) is prime and \(1<m<n\), both are impossible.

Thus the only possible nonabelian composition factor is \(S\) itself, whose order consumes all of \(|G|\). A nonsimple \(G\) is therefore solvable. Lemma A then makes its Sylow \(p\)-subgroup normal, and Lemma B gives \(p\notin V(G)\).

On the simple-group side, the assumed irreducible character degree \(q^2+1\) has \(p\)-part equal to \(|S|_p=p\), hence has \(p\)-defect zero. The standard defect-zero theorem makes it vanish on every \(p\)-singular element; Cauchy's theorem then gives \(p\in V(S)\). Therefore a nonsimple \(G\) cannot have \(V(G)=V(S)\), while a simple same-order \(G\) is forced to be the same Suzuki group.

### Concrete arithmetic instances checked by hand

The following checks use exact factorizations and modular arithmetic, not any post-correction computer run:

| \(n\) | \(q\) | exact order factorization | chosen \(p\) | primitive-order check | other-prime linear checks |
|---:|---:|---|---:|---|---|
| 3 | 8 | \(2^6\cdot5\cdot7\cdot13\) | 13 | \(\operatorname{ord}_{13}(2)=12\) | \(13\nmid4,6\) |
| 5 | 32 | \(2^{10}\cdot5^2\cdot31\cdot41\) | 41 | \(\operatorname{ord}_{41}(2)=20\) | \(\operatorname{ord}_{41}(5)=20>2\), \(41\nmid30\) |
| 7 | 128 | \(2^{14}\cdot5\cdot29\cdot113\cdot127\) | 113 | \(2^{14}\equiv-1\pmod{113}\), so order 28 | \(113\nmid4,28,126\) |
| 11 | 2048 | \(2^{22}\cdot5\cdot23\cdot89\cdot397\cdot2113\) | 397 | \(2^{11}\equiv63\), \(2^{22}\equiv-1\pmod{397}\), so order 44 | \(397\nmid4,22,88,2112\) |
| 13 | 8192 | \(2^{26}\cdot5\cdot53\cdot157\cdot1613\cdot8191\) | 53 | \(2^{13}\equiv30\), \(2^{26}\equiv-1\pmod{53}\), so order 52 | \(53\nmid4,156,1612,8190\) |

Factor checks used above:

\[
\begin{aligned}
128^2+1&=16385=5\cdot29\cdot113,\\
2048-1&=2047=23\cdot89,\\
2048^2+1&=4194305=5\cdot397\cdot2113,\\
8192^2+1&=67108865=5\cdot53\cdot157\cdot1613.
\end{aligned}
\]

Accordingly, subject to the two external theorem inputs being cited and checked, the criterion recognizes
\(\operatorname{Sz}(8)\), \(\operatorname{Sz}(32)\), \(\operatorname{Sz}(128)\), \(\operatorname{Sz}(2048)\), and \(\operatorname{Sz}(8192)\).

Exact **catalogue** coverage remains only what was actually screened: the two installed CTblLib order buckets for `Sz(8)` and `Sz(32)`. The three larger cases are theoretical arithmetic instances; no claim is made that their character tables or all same-order groups were catalogued locally.

Dependencies and possible failure points:

- The classification statement for nonabelian simple groups of order not divisible by 3 needs an exact citation.
- The family-wide existence of an irreducible Suzuki character of degree \(q^2+1\) needs an exact character-table citation or derivation.
- The defect-zero vanishing theorem is standard but should be cited in the verification note.
- The concrete factorizations/primality statements, especially 8191, should be independently arithmetic-checked by Validator before certification.
- The criterion does not establish recognition for composite exponent \(n\), where proper subfield Suzuki composition factors can occur, nor for prime \(n\) when no prime \(p\) satisfies the stated exponent-one and linear-group conditions.

## Lease-compliant evidence rerun

- Lead granted slot 3 for exactly one run of the pre-inspected wrapper.
- Exact command run once:
  `timeout 120s bash Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/leased_evidence_rerun.sh`.
- Observed exit code: 0.
- Observed wall time: 7.354707486 seconds.
- Complete stdout (including every class's zero-character indices) is saved verbatim at
  `Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/leased_evidence_rerun.out`.
- A `REPORT` asking Lead to release slot 3 was sent immediately. No other compute command was launched under the lease.
- The rerun reproduces the earlier table sets, exact two order buckets, Borel-product outputs, 56-divisor perfect-group screen, and modular-order checks. Those fixed finite outputs are now lease-compliant evidence; they are not mathematical certification and do not broaden the stated catalogue coverage.

## Live theoretical extension candidate: composite exponent \(q=512\)

This is cheap hand analysis while reviewer decisions are pending; it is not yet promoted into the partial-result note.

For \(q=512=2^9\),
\[
|\operatorname{Sz}(512)|
=2^{18}(512-1)(512^2+1)
=2^{18}\cdot5\cdot7\cdot13\cdot37\cdot73\cdot109.
\]
Indeed \(511=7\cdot73\) and
\(262145=5\cdot13\cdot37\cdot109\). The prime \(p=109\) occurs once and
\(2^{18}\equiv-1\pmod{109}\). Since \(2^4\not\equiv1\) and
\(2^{12}\equiv63\not\equiv1\pmod{109}\), its order is 36. Thus it clears the \(2^{18}\) linear-group bound; all other odd primes occur once and none is 1 modulo 109.

Composite exponent 9 permits the proper subfield composition factor `Sz(8)`, so the solvable-only lemma is insufficient. A representation-changing generalization appears to handle it:

> If \(v_p(M)=1\), no proper simple divisor of \(M\) contains \(p\), and \(p\) divides neither the automorphism group of any possible nonabelian minimal normal subgroup nor the relevant general linear groups for abelian minimal normal subgroups, then every **nonsimple** group of order \(M\) has normal Sylow \(C_p\).

The same strong-induction proof works. For a minimal normal \(N\), the quotient has a normal Sylow \(p\)-subgroup by induction (a proper simple quotient containing \(p\) is excluded). Its preimage is \(NP\); the automorphism-group hypotheses force \([P,N]=1\), so \(P\) is characteristic in that preimage and normal in the whole group.

For the \(q=512\) order, Zsigmondy's argument forces a proper Suzuki factor exponent to divide 9; the only possibility is `Sz(8)`. It occurs with multiplicity at most one because the ambient primes 5, 7, and 13 have exponent one, and \(109\nmid|\operatorname{Aut}(\operatorname{Sz}(8))|=3|\operatorname{Sz}(8)|\). Thus the generalized induction would make \(C_{109}\) normal in every nonsimple same-order group, hence 109 nonvanishing there. The standard degree-\(q^2+1\) Suzuki character would be 109-defect zero, making 109 vanishing in the simple group.

This is a concrete next-hour experiment: formalize the generalized minimal-normal lemma and have reviewers check its use of the `3'`-simple-group classification and `Aut(Sz(8))`. Kill criterion: any possible proper nonabelian minimal normal subgroup has automorphism group divisible by 109, or the strong induction fails when the quotient is simple.

## One-hour checkpoint

- 2026-08-16T12:36:02Z — cumulative active minutes: approximately 59 (18 handed off + 41 in this segment).
- **Active scope/revision:** `19.30/vanishing-order-simple-recognition`, revision 1, counterexample direction.
- **New facts:** the independent source audit is passed; the rendered source and all seven constraints match; lease-reproduced exact tables give
  \(V(\operatorname{Sz}(8))=\{2,4,5,7,13\}\) and
  \(V(\operatorname{Sz}(32))=\{2,4,5,25,31,41\}\); the exact installed CTblLib buckets at both orders contain only the simple table; every solvable same-order group is excluded by a normal-prime/Clifford argument; every normal-Hall-455 construction and every nontrivial direct product is excluded; and an explicit same-order near miss has exactly \(V=\{2,4\}\).
- **Current strategy:** primitive-prime minimal-normal obstruction. Replace group-by-group search by proving that a strategically chosen Sylow \(C_p\) is normal in every nonsimple same-order group and hence entirely nonvanishing.
- **Firmly ruled out:** all installed ordinary character tables at the two exact target orders; the natural Borel-times-cyclic construction at both orders; all groups with nontrivial centre; all nontrivial direct products; every order-29,120 group with normal Hall-455 subgroup; and, most importantly, every solvable comparison group at both exact orders.
- **Bottleneck:** a full Suzuki recognition theorem uses external standard inputs not checked inside this discovery-blind run: classification of nonabelian simple groups of order prime to 3, the Suzuki outer automorphism formula, and the irreducible degree \(q^2+1\). Validator/MathExpert review is pending.
- **Alternative A (theorem/citation route):** certify the conjectured odd-exponent arithmetic criterion, currently instantiated at \(q=8,32,128,512,2048,8192\).
- **Alternative B (constructor route):** for composite exponent \(q=512\), parameterize extensions with a proper `Sz(8)` composition factor and solvable radical, then try to defeat the normal-109 obstruction. This is qualitatively different from catalogue and direct-product search.
- **Recommended next 60-minute experiment:** finish the generalized minimal-normal lemma for \(q=512,p=109\), obtain MathExpert/Validator review, and treat any surviving extension class as the next constructor space. This is hand work; no unleased compute is planned.
- **Kill criterion:** abandon the generalized route if a proper nonabelian minimal normal subgroup has automorphism group divisible by 109, a proper nonabelian simple quotient containing 109 exists, or the standard degree-\(q^2+1\) character input is false/unavailable. A hostile audit has so far found none of these failures after repairing the induction domain and the harmless \(C_p\) base case.
- **Admissibility status:** no candidate passes every row. The explicit pair
  \((C_{455}\rtimes(C_4\times C_2^4),\operatorname{Sz}(8))\) is an
  `OUT_OF_SCOPE_EXAMPLE`: it passes finiteness, finite simplicity of \(S\), equal order, exact character reconstruction, and nonisomorphism, but fails `19.30-equal-vanishing-order-sets` because \(\{2,4\}\ne\{2,4,5,7,13\}\).

Correction to the earlier prime-exponent limitation: the refined criterion can cover composite odd exponents as well. It covers only instances satisfying its exponent-one primitive-prime and cross-linear-group hypotheses; it is not a theorem for every Suzuki parameter.

## Lead decision: return to counterexample direction

- 2026-08-16T12:36Z — Lead bound the generalized Suzuki criterion to reviewer work and directed this agent to name one residual simple-group order with a structurally plausible order-matched nonsimple candidate.
- Chosen residual target: \(S=\operatorname{PSL}_2(7)\), \(|S|=168\).
- Chosen candidate: \(G=A\Gamma L(1,8)=\mathbb F_8^+\rtimes(\mathbb F_8^\times\rtimes\operatorname{Gal}(\mathbb F_8/\mathbb F_2))\), also of order \(8\cdot7\cdot3=168\), with normal translation subgroup \(C_2^3\). Hence \(G\) is nonsimple and not isomorphic to \(S\).
- Named strategy: **affine-semilinear collision at order 168**. Certificate plan: reconstruct both irreducible character sets by hand from the standard `PSL(2,7)` table and Clifford theory for the affine group; determine the two vanishing-order sets exactly. Kill criterion: any vanishing order in \(G\) outside \(\{2,3,4,7\}\), or failure of either 2 or 4 to occur as a vanishing order in \(G\).

## Exact hand test: \(\operatorname{PSL}_2(7)\) versus \(A\Gamma L(1,8)\)

### Simple side

The standard ordinary character table of \(S=\operatorname{PSL}_2(7)\) has class orders
\[
1,2,3,4,7,7
\]
and irreducible degrees \(1,3,3,6,7,8\). The needed zero pattern can be displayed without the two conjugate cyclotomic 7-class values:

| degree | order 2 | order 3 | order 4 | order 7 classes |
|---:|---:|---:|---:|---:|
| 3 (two characters) | \(-1\) | \(0\) | \(1\) | nonzero |
| 6 | \(2\) | \(0\) | \(0\) | \(-1\) |
| 7 | \(-1\) | \(1\) | \(-1\) | \(0\) |
| 8 | \(0\) | \(-1\) | \(0\) | \(1\) |

Thus every nonidentity element order in \(S\) is represented by a vanishing class and
\[
V(S)=\{2,3,4,7\}.
\]

### Affine-semilinear side

Write \(V=\mathbb F_8^+\cong C_2^3\) and
\(H=\mathbb F_8^\times\rtimes\operatorname{Gal}(\mathbb F_8/\mathbb F_2)\cong C_7\rtimes C_3\), so \(G=V\rtimes H\).

The irreducible characters of \(G\) are complete as follows.

1. Inflate the irreducibles of the Frobenius group \(H\): three linear characters and two degree-three characters induced from nontrivial characters of \(C_7\).
2. The Singer subgroup \(C_7\) is transitive on the seven nontrivial characters of \(V\). The inertia quotient of one such character has order three. Its three extensions induce three irreducible characters of degree seven.
3. The degree-square check is
   \[
   3\cdot1^2+2\cdot3^2+3\cdot7^2=3+18+147=168,
   \]
   so no irreducibles are missing.

Now determine zeros and orders.

- The degree-three characters inflated from \(H\) vanish whenever the \(H\)-component lies outside \(C_7\), in particular on every coset with order-three component.
- Every order-three linear transformation on the 3-dimensional \(\mathbb F_2\)-space \(V\) fixes a nonzero vector \(u\): its nontrivial irreducible \(\mathbb F_2C_3\)-module has dimension two, leaving a 1-dimensional fixed summand. For an order-three \(h\in H\), the commuting affine element \(uh\) has order six. An inflated degree-three character is zero on it. Hence \(6\in V(G)\).
- Every involution of \(G\) lies in \(V\), since \(G/V\) has odd order. Inflated characters take their positive degree there. Each degree-seven character restricts to the sum of all seven nontrivial linear characters of \(V\), whose value at \(1\ne v\in V\) is \(-1\). Thus no involution is vanishing and \(2\notin V(G)\).
- Elements with order-seven component are outside every conjugate of an inertia subgroup of order \(24\), so the induced degree-seven characters vanish on them; hence \(7\in V(G)\).
- The degree-three inflated characters also give vanishing order three. The affine group has no element order four: the kernel has exponent two, an order-seven component is fixed-point-free, and an order-three component yields order three or six.

Therefore the exact candidate invariant is
\[
V(A\Gamma L(1,8))=\{3,6,7\}.
\]

Comparison:
\[
\{3,6,7\}\ne\{2,3,4,7\}.
\]
The candidate meets the kill criterion twice: it has forbidden vanishing order 6 and lacks required vanishing orders 2 and 4. It is an `OUT_OF_SCOPE_EXAMPLE`, not a counterexample.

### Exact affine-family coverage

The argument covers every faithful affine group \(C_2^3\rtimes H\) with \(|H|=21\): a faithful order-21 subgroup of \(\operatorname{GL}_3(2)\) contains a Singer \(C_7\), acts transitively on \(V\setminus\{0\}\), and its order-three element necessarily fixes a nonzero vector. Consequently the same missing-order-2 and extra-order-6 obstruction applies independently of coordinates.

Constraint matrix for the affine candidate:

| constraint_id | role | required condition | candidate value / proof use | result |
|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | one qualifying pair refutes the universal assertion | pair tested against every row | pass as test setup |
| `19.30-G-finite` | admissibility | finite \(G\) | explicit affine semidirect product, order 168 | pass |
| `19.30-S-finite-simple` | admissibility | finite simple \(S\) | \(S=\operatorname{PSL}_2(7)\) | pass |
| `19.30-vanishing-definition` | admissibility | zeros of irreducible complex characters | complete degree count and Clifford zero loci for \(G\); standard table zero loci for \(S\) | pass |
| `19.30-equal-orders` | admissibility | \(|G|=|S|\) | \(8\cdot21=168\) | pass |
| `19.30-equal-vanishing-order-sets` | admissibility | \(V(G)=V(S)\) | \(\{3,6,7\}\ne\{2,3,4,7\}\) | **fail** |
| `19.30-isomorphic` | target conclusion | violate isomorphism | \(C_2^3\triangleleft G\), while \(S\) is simple | violated, but irrelevant after admissibility failure |

## Counterexample branch B: nonsolvable radical extensions at \(|\operatorname{Sz}(512)|\)

- 2026-08-16T12:43Z — Lead selected the exact residual family with a proper `Sz(8)` composition factor and forbade catalogue/computational expansion.

Let
\[
S=\operatorname{Sz}(512),\qquad
|S|=2^{18}\cdot5\cdot7\cdot13\cdot37\cdot73\cdot109.
\]
Assume a nonsimple comparison group \(G\) has `Sz(8)` as its nonabelian composition factor, and let \(R=\operatorname{Rad}(G)\). The 3-prime simple-group classification makes every nonabelian factor Suzuki. At this exact order, Zsigmondy's divisor argument permits only the proper exponent \(3\), hence only `Sz(8)`; it occurs once because the ambient 5-, 7-, and 13-parts each occur once. Since
\(|\operatorname{Out}(\operatorname{Sz}(8))|=3\) and \(3\nmid|G|\), the semisimple quotient has no outer layer. Therefore the entire residual family has the exact form
\[
1\longrightarrow R\longrightarrow G\longrightarrow\operatorname{Sz}(8)
\longrightarrow1,
\qquad
|R|=2^{12}\cdot37\cdot73\cdot109,
\]
where \(R\) is solvable. This parameterizes every action and every extension class; no split assumption is made.

### Uniform 109 kill criterion

Apply the solvable normal-prime lemma inside \(R\), with \(p=109\). The exact checks are
\[
\operatorname{ord}_{109}(2)=36>12,
\qquad
109\nmid |\operatorname{GL}_1(37)|=36,
\qquad
109\nmid |\operatorname{GL}_1(73)|=72.
\]
Thus the Sylow subgroup \(P\cong C_{109}\) is normal in \(R\). It is the unique Sylow 109-subgroup of \(R\), hence characteristic in \(R\); because \(R\triangleleft G\), this gives
\[
C_{109}=P\triangleleft G.
\]

The Clifford/cyclotomic lemma does not require \(G\) to be solvable: if \(C_p\triangleleft G\), every nonidentity element of it is nonvanishing. Consequently
\[
109\notin V(G)
\]
for every extension in the displayed family, independently of its action or cocycle.

On the target side, the standard Suzuki irreducible of degree
\[
512^2+1=262145=5\cdot13\cdot37\cdot109
\]
has 109-defect zero, so it vanishes on 109-elements and
\(109\in V(\operatorname{Sz}(512))\). Hence no member of the entire radical-extension family can have the target vanishing-order set.

**Family kill:** every nonsolvable order-matched extension with proper `Sz(8)` composition factor fails `19.30-equal-vanishing-order-sets` at the single order 109. No counterexample survives this branch.

### What was and was not used

- This is a uniform hand exclusion over all solvable radicals \(R\) of the exact displayed order, all actions of `Sz(8)` on \(R\), and all extension classes.
- It uses the review-bound standard facts about 3-prime simple groups, `Out(Sz(8))`, and the Suzuki degree \(q^2+1\); it does not broaden their proof here.
- No catalogue, enumeration, GAP, Sage, or solver command was run for this branch.

## New structural target: affine lift at \(|\operatorname{PSL}_2(8)|=504\)

The `Sz(512)` radical family met its uniform kill criterion, so the next counterexample target is
\[
S=\operatorname{PSL}_2(8),\qquad |S|=8(8^2-1)=504.
\]
Its element orders are \(1,2,3,7,9\); in particular it has no elements of order 6 or 18. Its involutions are vanishing (for example, the characteristic-2 Steinberg character vanishes on nonidentity unipotent elements), so
\[
2\in V(S).
\]

### Exact candidate

Let \(V=\mathbb F_8^+\cong C_2^3\). Define
\[
H=C_7\rtimes C_9
=\langle a,b\mid a^7=b^9=1,\ bab^{-1}=a^2\rangle,
\]
where the action of \(b\) on \(C_7\) has order three. Let \(H\) act on \(V\) through its quotient \(C_7\rtimes C_3\): \(a\) acts as multiplication by a primitive element of \(\mathbb F_8\), and \(b\) acts as the Frobenius map \(x\mapsto x^2\). Set
\[
G=V\rtimes H.
\]
Then \(|G|=8\cdot63=504=|S|\), while \(V\triangleleft G\), so \(G\not\cong S\).

The choice of \(C_9\) is intentional: unlike a direct product, this lift supplies order-nine elements, which occur in the simple target.

### Complete irreducible reconstruction

The group \(H\) has nine linear characters inflated from \(H/C_7\cong C_9\). Its six remaining irreducibles have degree three: the six nontrivial characters of \(C_7\) form two orbits of size three, the inertia quotient contributes three extensions for each orbit, and induction gives \(2\cdot3=6\) characters. Thus
\[
9\cdot1^2+6\cdot3^2=63.
\]

The image of \(H\) on \(V\) contains the Singer \(C_7\) and is transitive on the seven nontrivial characters of \(V\). A nontrivial character of \(V\) has inertia quotient of order nine, yielding nine extensions and nine induced degree-seven irreducibles of \(G\). Together with the inflated characters of \(H\),
\[
9\cdot1^2+6\cdot3^2+9\cdot7^2=63+441=504,
\]
so the list is complete.

### Uniform kill

- Every involution of \(G\) lies in \(V\), since \(G/V\) has odd order. Inflated characters take their nonzero degree on \(V\). Each degree-seven character restricts to the sum of all seven nontrivial linear characters of \(V\), which equals \(-1\) at every \(1\ne v\in V\). Hence
  \[
  2\notin V(G).
  \]
- A degree-three character induced from a nontrivial character of \(C_7\) vanishes on elements outside its inertia group, including a generator \(b\) of \(C_9\). The Frobenius image of \(b\) fixes the nonzero vector \(u=1\in\mathbb F_8\); hence \(u\) commutes with \(b\) and \(|ub|=18\). Inflating the degree-three character to \(G\) gives zero at \(ub\), so
  \[
  18\in V(G).
  \]

The target has vanishing order 2 and no element order 18. Therefore
\[
V(G)\ne V(\operatorname{PSL}_2(8)).
\]
This exact pair is another `OUT_OF_SCOPE_EXAMPLE`, failing `19.30-equal-vanishing-order-sets` in both directions.

The same two mechanisms also exclude the explicit split-kernel variant with complement
\((C_7\rtimes C_3)\times C_3\): transitivity makes all involutions nonvanishing, while the order-three field automorphism fixes a nonzero vector and produces a vanishing element of order 6. No claim is made here about every possible order-504 affine extension.

## Second order-504 family: central extensions of \(\operatorname{PSL}_2(7)\)

A nonsolvable nonsimple group \(G\) of order 504 can have the proper nonabelian composition factor
\(T=\operatorname{PSL}_2(7)\) of order 168, leaving a solvable radical of order three. In that exact branch,
\[
1\longrightarrow C_3\longrightarrow G\longrightarrow
\operatorname{PSL}_2(7)\longrightarrow1.
\]
The conjugation action on \(C_3\) is trivial: it would otherwise give a nontrivial homomorphism from the simple perfect quotient to
\(\operatorname{Aut}(C_3)\cong C_2\). Hence the extension is central. For
\(Q=\operatorname{PSL}_2(7)\), perfectness gives \(Q_{\mathrm{ab}}=0\), while its Schur multiplier is \(M(Q)\cong C_2\). The universal-coefficient sequence for the trivial \(Q\)-module \(C_3\) therefore gives
\[
H^2(Q,C_3)\cong\operatorname{Hom}(M(Q),C_3)=0.
\]
Thus the extension splits; centrality makes it the direct product
\[
G\cong\operatorname{PSL}_2(7)\times C_3.
\]

Using the already reconstructed set
\(V(\operatorname{PSL}_2(7))=\{2,3,4,7\}\), the direct-product formula gives
\[
V(G)=\{2,3,4,6,7,12,21\}.
\]
The target \(\operatorname{PSL}_2(8)\) has element orders only
\(1,2,3,7,9\), so in particular 6, 12, and 21 cannot belong to its vanishing-order set. Thus every nonsolvable order-504 group in this central-extension family fails the invariant equality.

This is a representation-changing pivot from affine modules to Schur-multiplier/central-extension data. Its exact coverage is groups fitting the displayed exact sequence with normal kernel \(C_3\) and quotient \(\operatorname{PSL}_2(7)\); it does not cover every nonsimple group of order 504 or the reverse extension orientation.

Terminology correction for the preceding `Sz(512)` section: every occurrence of “3-prime simple-group classification” means the classification of nonabelian simple groups whose orders are **prime to 3**.

## Inbox processing after the order-504 checkpoint

- 2026-08-16T12:48:37Z — read MathExpert's `REPORT` dated 12:44:50Z. It found no gap in the normal-Hall action partition after the inertia-group conjugacy detail is made explicit, and judged the all-odd Suzuki criterion coherent conditional on its four named standard inputs. No action was requested; the report remains review evidence rather than an externally sourced theorem citation.
- Read Lead's 12:47:00Z `KILL`, which ordered the older order-168 branch stopped and directed attention to the already-issued `Sz(512)` radical-extension decision. That instruction had already been followed: the order-168 branch was not resumed, the `Sz(512)` branch was uniformly killed at order 109, and the later order-504 work followed only after that kill. No computation was run.
- Cumulative active time: approximately 71 minutes (18 minutes at handoff plus 53 minutes in this run). Cheap packaging and inbox processing continue while the later 12:47Z checkpoint decision is pending.

## Hostile audit of the order-504 branches

- 2026-08-16T12:52Z — two independent hand audits found one real consistency error in the affine presentation: for multiplication \(a:x\mapsto\alpha x\) and Frobenius \(b:x\mapsto x^2\), one has \(b^{-1}ab=a^4\), equivalently \(bab^{-1}=a^2\). The displayed presentation above has been corrected to the latter relation. The abstract complement still has order 63; all character counts and the fixed-vector order-18 witness are unchanged.
- The audits independently reconstructed the nine linear and six degree-three characters of the complement, the nine degree-seven characters above the unique nontrivial orbit of \(\operatorname{Irr}(C_2^3)\), and the degree-square total 504. They confirmed \(2\notin V(G)\) and \(18\in V(G)\).
- The central-extension audit confirmed splitting only after making the perfectness argument explicit: \(H^2(\operatorname{PSL}_2(7),C_3)=0\) follows from the universal-coefficient sequence, trivial abelianization, and multiplier \(C_2\). The family boundary has been narrowed explicitly to the displayed extension orientation.
- No computation or external search was used in either audit.

## Cycle outcome: `PARTIAL_RESULT`

- 2026-08-16T12:55:31Z — Lead directed packaging of the reproducible counterexample-family exclusions and conditional theorem dependencies, recommendation of a proof-direction switch, and immediate stop without opening another family.
- Final package: `partial-result.md` in this run directory. It records exact installed-catalogue coverage, the uniform normal-Hall-455 exclusion, explicit symbolic near misses, centre/direct-product obstructions, the all-solvable `Sz(8)`/`Sz(32)` exclusion, the conditional `Sz(512)` radical-family exclusion, and the two precisely bounded order-504 branches.
- No candidate passes `19.30-equal-vanishing-order-sets`; hence there is no counterexample, no `CLAIM`, and no claim-check JSON.
- The active universal scope remains unanswered. The broader Suzuki statement remains conditional on the exact external inputs listed in `partial-result.md` and is not labelled proven.
- Recommended next scheduling action: switch to the proof direction after independent review.
- Work stopped at 2026-08-16T12:55:31Z. Cumulative active time: approximately 76 minutes (18 minutes handed off plus 58 minutes in this run); reviewer-wait time excluded.
