---
title: "Verification — Kourovka 20.115 — Malle--Navarro--Tiep is partial stale"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
claim: "Malle--Navarro--Tiep, arXiv:2605.04513v1, states the exact active conjecture but does not prove its universal conclusion, so the result is PARTIAL_STALE and not STALE_MATCH."
claimant: Problem-20.115
target_statement: "For every finite group G, every ordinary irreducible complex character chi of G, and every x in G, chi(x) nonzero implies o(x)chi(1) divides |G|."
excluded_scopes:
  - Brauer or modular characters
  - reducible characters
  - rows with chi(x)=0
  - the already-known solvable-group restriction
  - the weaker contextual fourth-power/fifth-power bound
  - bounded character-table screens presented as universal proofs
target_object: "The universal ordinary-character implication in Kourovka 20.115."
witness_object: "The conjecture, reductions, and proved family/prime cases stated in arXiv:2605.04513v1, together with the official July 2026 edition status."
witness_equals_target: false
citation: "G. Malle, G. Navarro, P. H. Tiep, Zeros of characters and orders of elements in finite groups, arXiv:2605.04513v1 (6 May 2026)."
verification_method: "Independent rendered-source and primary-literature clause audit"
tools_used: ["Poppler 24.02.0", "MuPDF 1.23.10", "curl 8.5.0", "Python 3.12.3", "GAP 4.12.1 probe only"]
scope_answered: []
partial_coverage: ["Named proper subfamilies and prime cases", "Conditional reduction to all nearly-simple triples satisfying (*)"]
scope_not_answered: ["20.115/nonzero-character-order-divisibility"]
active_assignment_answered: no
staleness_classification: PARTIAL_STALE
source_transcription_checked: yes
current_edition_checked: "Official July 3, 2026 No. 21 main PDF and updates-only PDF"
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/conjectured]
---

# Verification — Kourovka 20.115

## Verdict

**PARTIAL_STALE is confirmed. STALE_MATCH is rejected.**

The paper's Conjecture A is the exact active Kourovka clause, row for row. The paper does not assert Conjecture A as a theorem: Theorem B reduces it conditionally to all nearly-simple triples satisfying its condition `(*)`, and later theorems establish many—but explicitly not all—of those primewise cases. Thus the external work is substantial, target-facing progress, but the active universal quantifier and target conclusion remain incomplete.

The official July 2026 No. 21 PDF independently still prints 20.115 unstarred, unchanged, and without a comment. Its updates-only PDF has no 20.115 entry. That edition evidence corroborates the classification, though absence of an editor comment alone would not prove worldwide openness.

`active_assignment_answered: no`.

## The claim under review

The request claimed only a staleness classification: arXiv:2605.04513v1 matches the exact active statement but is not a universal solution. This note audits scope coverage. It does **not** certify every proof in the paper, and it does not promote the unresolved conjecture above `status/conjectured`.

## Locked source, scope, and revision

- Canonical scope: `20.115/nonzero-character-order-divisibility`.
- Assignment revision: 1.
- Rendered source: configured Kourovka PDF, printed/PDF page 161.
- Exact active target: for arbitrary finite `G`, ordinary `chi in Irr(G)`, and `x in G`, the implication `chi(x) != 0 => o(x) | |G|/chi(1)`.
- Since `chi(1)` is a positive integer dividing `|G|`, the source conclusion is equivalent to `o(x)chi(1) | |G|`.

The source has exactly one active question clause and two contextual known-result clauses. The scope JSON records all three correctly. No canonical-scope edit is required or was made.

## Source/literature clause matrix

| source clause | active? | arXiv:2605.04513v1 | July 2026 No. 21 | audit result |
|---|---:|---|---|---|
| `c-question`: if `chi(x) != 0`, must `o(x)` divide `|G|/chi(1)`? | yes | Conjecture A states this exact implication. Theorem B is conditional, and the paper explicitly retains remaining nearly-simple prime cases. | Unstarred and unchanged; no answer/comment. | Exact-subject match, but not a complete answer: PARTIAL_STALE. |
| `c-solvable-context`: the assertion holds for solvable `G` | no | Used as prior input in the reduction; not presented as a new universal solution. | Repeated as known context. | Excluded contextual knowledge; cannot close the active scope. |
| `c-general-bound-context`: `(o(x)chi(1))^4` divides `|G|^5` for arbitrary `G` | no | The paper pursues the first-power conjecture via reductions and family cases; no weaker bound is substituted for the target conclusion. | Repeated as known context. | Excluded weaker conclusion; cannot close the active scope. |

## Constraint-and-conclusion matrix

This matrix was reconstructed from the rendered source before reading the claimant's log.

| constraint_id | role | source requirement | paper's Conjecture A | coverage by proved results | gate result |
|---|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | Universal implication over every admissible triple `(G,chi,x)` | Exact match | Only a conditional global reduction plus proper families/prime cases | **INCOMPLETE** |
| `20.115-G-finite` | admissibility | `G` is finite | Explicit exact match | All proved cases remain in the finite-group class, but do not cover every finite `G` | PASS for object class; not universal |
| `20.115-chi-complex-irreducible` | admissibility | `chi` is an ordinary irreducible complex character of `G` | `chi in Irr(G)`, the standard ordinary-character notation used throughout | Exact character class within covered cases | PASS |
| `20.115-x-in-G` | admissibility | `x in G`; `o(x)` is its exact order | `g in G`; exact `o(g)` | Exact element/order datum within covered cases | PASS |
| `20.115-character-value-nonzero` | admissibility | Exact `chi(x) != 0` | Exact `chi(g) != 0` | Exact hypothesis within covered cases | PASS |
| `20.115-order-degree-divisibility` | target conclusion | `o(x) | |G|/chi(1)`, equivalently `o(x)chi(1) | |G|` | Exact same desired conclusion | Established only in the paper's covered cases; explicitly not for all remaining nearly-simple cases | **NOT ESTABLISHED UNIVERSALLY** |

Every object, hypothesis, and conclusion row matches at the level of the conjecture's statement. The stale-match gate nevertheless fails mechanically on the universal-quantifier row and the target-conclusion row. Merely restating the exact target as a conjecture cannot be a `STALE_MATCH`.

## Target versus witness

- **Target:** one universal theorem (or one admissible counterexample) for all finite-group triples in scope.
- **Witness actually supplied by the paper:** an exact restatement as Conjecture A; a conditional reduction; and theorems for named proper families/prime cases.
- **Witness equals target:** false.

Theorem B says that if Condition (1.1) holds for **all** nearly-simple triples `(H,h,chi)` satisfying `(*)`, then Conjecture A follows. It does not establish that antecedent. The paper's abstract says cases remain, and the introduction identifies a residual family for primes greater than five. There is therefore no circular route from the reduction back to a universal theorem.

## What the paper actually establishes

The relevant statement hierarchy is:

1. **Conjecture A (p. 1):** the exact active Kourovka implication.
2. **Theorem B (pp. 1–2):** a sufficient reduction to Condition (1.1) for every nearly-simple triple satisfying `(*)`.
3. **Theorem 2.2 (pp. 4–7):** a stronger conditional reduction, still assuming the nearly-simple conjecture.
4. **Theorem C (p. 3):** the stronger block conditions `(double-dagger)` and `(double-dagger-star)` for listed quasi-simple families and prime ranges.
5. **Theorem D (p. 3):** Condition (1.1) for all nearly-simple groups associated to alternating, Suzuki, small Ree, or sporadic simple groups, plus the defining-characteristic prime for simple groups of Lie type.
6. Further propositions cover additional Lie-type cases, including `GL_n(epsilon q)` itself, but the paper never upgrades Conjecture A to a theorem for all finite groups.

The stronger block condition is sufficient, not necessary. In particular, Corollary 4.13's possible failures of `(double-dagger-star)` are **not** counterexamples to Wilde's conjecture; Proposition 4.16 directly proves Condition (1.1) in part of that difficult region. A strategy that searches only for failure of the block-exponent bound would therefore risk mistaking failure of a sufficient criterion for failure of the target.

## Exact residual cases stated by the paper

### Exhaustive statement only for primes greater than five

The paper gives a clean residual statement only at a prime `ell > 5`: the unproved nearly-simple cases satisfying `(*)` are special `ell`-block cases attached to decorated versions of `PSL_n(epsilon q)`. The relevant prime necessarily lies in the critical range `ell | gcd(n,q-epsilon)`; the other odd cross-characteristic cases are covered by Theorem 4.3.

Corollary 4.13 makes the possible obstructing blocks precise. Put

- `G = SL_n(epsilon q)`, `epsilon in {+1,-1}`, `n >= 3`;
- `2 < ell | gcd(n,q-epsilon)`;
- `B` an `ell`-block with `Irr(B)` contained in the Lusztig block union `E_ell(G,s)` for an `ell'`-element `s in G* = PGL_n(epsilon q)`.

Then `(double-dagger-star)` holds unless possibly the connected centralizer has one of these two forms:

1. `C^0_{G*}(s) ~= GL_r((epsilon q)^(n/r))/C_(q-epsilon)`, for an `ell`-power `r` dividing `n`; or
2. `C^0_{G*}(s) ~= (GL_(n1)(q^e1) x GL_(n2)(q^e2))/C_(q-epsilon)`, where `n1,n2 > 1` are `ell`-powers and `n = n1 e1 + n2 e2`.

These are possible residual proof cases, not asserted counterexamples.

### The part Proposition 4.16 already handles

For the first/Coxeter-torus type, Proposition 4.16 proves Condition (1.1) at `ell` when:

- the derived quasi-simple group is `SL_n(q)` (the linear, not unitary, case);
- the semisimple parameter has Coxeter-torus centralizer;
- `2 < ell | gcd(n,q-1)`; and
- the automorphism induced by `h` is also induced by some semilinear element `h1 in GammaL_n(q)`.

Repeating this subcase or a broad character-table sweep would duplicate the paper rather than attack the stated residual.

### The explicit reduction bottleneck

To extend Proposition 4.16 to extensions of `SL_n(q)` by arbitrary automorphisms and to the `SU_n(q)` analogue (thereby finishing the blocks isolated in Remark 4.14), the authors say one must:

1. extend their Curtis-type trace formula to disconnected reductive algebraic groups; and
2. relate constituents of Lusztig restrictions for the disconnected extension `G` to those for `[G,G]`.

They state that the first step can be done, while the second is the difficult missing ingredient. The abstract describes the same obstruction more broadly as unavailable information concerning extensions of irreducible characters.

The second two-factor centralizer family in Corollary 4.13 is not disposed of by the post-Proposition-4.16 paragraph. The paragraph expressly discusses finishing the blocks in Remark 4.14, which treats the first family. Accordingly, my reading is that Lead should treat the second family as a separately listed potential residual; this is an inference from the paper's statement structure, not a separate theorem declaring that family open.

### Important small-prime limitation

The phrase “only exceptions” in the introduction is expressly restricted to `p > 5`. The paper does **not** give one exhaustive complement of the proved results for `p = 2,3,5`. It proves many small-prime and family cases, but Lead must not infer that the two Corollary 4.13 shapes are the only unresolved cases at all primes.

## Current July 2026 edition status

The official editors' July 3, 2026 post links:

- the [No. 21 main PDF](https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/07/21tkt.pdf); and
- the [July updates-only PDF](https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/07/21upd.pdf).

The main PDF metadata has creation time 3 July 2026. On rendered printed page 161, problem 20.115 is unstarred, word-for-word unchanged from the source clause, and has no editor comment or citation. Text search of the updates-only PDF finds neither `20.115`, `Wilde`, nor `2605.04513`. The main PDF contains no `*20.115` marker.

The arXiv [abstract/version-history page](https://arxiv.org/abs/2605.04513) showed only v1, submitted 6 May 2026, when checked on 17 August 2026. A bounded search for a later arXiv paper claiming a universal proof or counterexample found none. This negative result is limited to the cited arXiv/version and official-edition checks; it is not an assertion that no unpublished work exists.

## Subclaims and what each method proves

| subclaim | independent method | what a pass proves | what it does not prove |
|---|---|---|---|
| exact active source | visually inspect rendered configured page 161 | correct quantifiers, character class, nonzero hypothesis, and divisibility typography | truth of the assertion |
| exact paper target | inspect v1 PDF, especially Conjecture A | the paper states the same active proposition | that the proposition is proved |
| incomplete universal coverage | inspect abstract, Theorem B, Theorems C/D, Corollary 4.13, Proposition 4.16, and its following paragraph | v1 retains explicit proof cases and a missing reduction ingredient | that every theorem proof in v1 is correct |
| current edition status | inspect official rendered page plus updates-only PDF | editors had not marked 20.115 answered in the July release | exhaustive worldwide literature status |
| staleness classification | apply the clause and constraint gates | PARTIAL_STALE, with `active_assignment_answered: no` | a solution or counterexample |

## Evidence

Primary sources:

- [Malle--Navarro--Tiep arXiv v1 PDF](https://arxiv.org/pdf/2605.04513v1), SHA-256 `a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f` for the file inspected.
- [Official July 2026 No. 21 PDF](https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/07/21tkt.pdf), SHA-256 `301b0cdcc53abc88b57cc0732cad73bf8fbe1c9ba0de5a0a794070398e3395fe` for the file inspected.
- [Official July 2026 updates-only PDF](https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/07/21upd.pdf), SHA-256 `ab208d727d4d46f53616c809b67a3f01221c91806a82e58806735c99134d640f` for the file inspected.

Relevant command/output transcript:

```text
$ pdftotext -layout /tmp/2605.04513v1.pdf - | rg -n -m 1 'arXiv:2605\.04513v1'
8:arXiv:2605.04513v1 [math.RT] 6 May 2026

$ pdftotext -layout /tmp/2605.04513v1.pdf - | rg -n -A 2 -m 1 '^\s*Conjecture A'
35:                                          Conjecture A (Wilde). Let G be a finite group and let χ ∈ Irr(G). If χ(g) ̸= 0 for
36-                                          some g ∈ G, then the order o(g) of g divides |G|/χ(1).
37-                                             Our first main result is the reduction of Conjecture A to a stronger version of the

$ rg -n -A 4 -m 1 '^20\.115\.' /tmp/kourovka-21-july-2026.txt
7696:20.115. Let χ be a complex irreducible character of a finite group G. If χ(x) ̸= 0 for
7697-some x ∈ G, must the order o(x) of x divide |G|/χ(1)?
7698-   This is known to be true if G is solvable, and it is known that (o(x)χ(1))4 divides
7699-   5
7700-|G| for arbitrary G.                                                         T. Wilde

$ rg -n '20\.115|Wilde|2605\.04513' /tmp/kourovka-21-july-2026-updates.txt
[no output]
rg_exit=1

$ rg -n '^\*20\.115\.' /tmp/kourovka-21-july-2026.txt
[no output]
rg_exit=1
```

The displayed superscripts in the last source formula were checked on the rendered page: the correct typography is `(o(x)chi(1))^4 | |G|^5`. Plain-text extraction was used only for navigation.

## Why this verdict

`STALE_MATCH` requires an external result that fully answers the active scope. Here, the paper's **statement** passes every object/hypothesis/conclusion fidelity row, but its **proved result** fails the universal-coverage gate. That is exactly the protocol definition of `PARTIAL_STALE`: external work answers substantial subfamilies and supplies a reduction without closing the active target.

## What is NOT established

- The universal divisibility conjecture is not established.
- No counterexample is supplied or independently found.
- This audit does not certify the proofs of Theorems B–D or the later propositions; it certifies only what their stated coverage does and does not claim.
- The Corollary 4.13 block-bound exceptions are not counterexamples to the active conjecture.
- The paper does not provide an exhaustive residual list for primes 2, 3, and 5.
- The July edition's lack of a comment is corroboration, not a logically exhaustive literature search.

## What would upgrade it

An upgrade to `STALE_MATCH` would require either a primary-source universal proof covering every remaining nearly-simple prime case after Theorem B, or one fully admissible finite-group counterexample with exact ordinary-character and element-order data. Neither appears in arXiv:2605.04513v1 or the official July 2026 edition.
