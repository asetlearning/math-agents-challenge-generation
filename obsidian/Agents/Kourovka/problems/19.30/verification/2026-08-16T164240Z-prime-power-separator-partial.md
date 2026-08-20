---
title: "Verification — Kourovka 19.30 — prime-power separator partial theorem"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
scope_record: Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json
assignment_revision: 1
claim: "If a finite simple group S and a prime p satisfy Target-vanishing, CS-p, Aut-p, and Simple-order uniqueness as stated in Theorem 4, then every finite same-order group G with V_o(G)=V_o(S) is isomorphic to S."
claimant: Problem-19.30
target_statement: "For every finite group G and finite simple group S, if |G|=|S| and G and S have the same set of orders of vanishing elements, then G is isomorphic to S."
excluded_scopes: ["Equality of character tables without equality of vanishing-order sets", "Equality of spectra of all elements rather than only vanishing elements", "Pairs in which neither group is finite simple"]
target_object: "Every pair (G,S) in the canonical universal scope: G finite, S finite simple, |G|=|S|, and V_o(G)=V_o(S)."
witness_object: "Only the restricted pairs (G,S) whose simple member admits a prime satisfying Target-vanishing, CS-p, Aut-p, and Simple-order uniqueness, checked by a line-by-line hand proof with no computational model."
witness_equals_target: false
citation: "Internal hand derivation in this verification note; no external citation used."
verification_method: line-by-line hand proof
tools_used: ["No mathematical computation; filesystem and SHA-256 inspection only"]
scope_answered: ["Restricted sufficient subclass: finite simple S for which at least one prime p satisfies Target-vanishing, CS-p, Aut-p, and Simple-order uniqueness exactly as in Theorem 4"]
scope_not_answered: ["19.30/vanishing-order-simple-recognition universal scope", "Conditional Suzuki specialization", "Any unconditional nonabelian simple family not separately shown to satisfy the four hypotheses"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/conjectured]
---

# Verification — Kourovka 19.30

## The claim

Lemmas 1–3 and Theorem 4 form a valid computation-free sufficient-condition theorem: for precisely the restricted class in `scope_answered`, equality of order and vanishing-element-order sets forces isomorphism.

The line-by-line audit assessment attaches only to Lemmas 1–3 and Theorem 4. The formal status remains `status/conjectured`; neither the conditional Suzuki subsection nor the canonical universal target is promoted.

## Scope, revision, and clause matrix

Canonical scope: `19.30/vanishing-order-simple-recognition`, assignment revision 1. The linked canonical source-fidelity audit passed. The report and proof draft also name revision 1, so there is no revision collision.

| source clause | active? | what the audited theorem answers | what remains open |
|---|---:|---|---|
| `c-definition`: vanishing means zero of some irreducible complex character | yes | Used exactly in Lemmas 1–2 and Theorem 4 | none within the restricted theorem |
| `c-question`: universal same-order/equal-`V_o` recognition of finite simple groups | yes | Only pairs whose simple member admits a prime satisfying the four added hypotheses | all other admissible pairs; therefore the universal source clause |

`active_assignment_answered: no` because the active universal row is not proved. The exact surviving subclass is

\[
 \left\{S\text{ finite simple}:\ \exists p\mid |S|\text{ satisfying Target-vanishing, CS-p, Aut-p, and Simple-order uniqueness}\right\}.
\]

No linked artifact proves that this subclass contains any particular nonabelian simple family. The abstract theorem is therefore a reusable reduction, not a concrete family classification.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | audited use | result |
|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | every admissible pair `(G,S)` | restricted by four additional sufficient hypotheses | **not established universally** |
| `19.30-G-finite` | admissibility | `G` finite | minimal normal subgroups, Sylow theory, and Clifford theory | proved for covered subclass |
| `19.30-S-finite-simple` | admissibility | `S` finite simple | assumed in Theorem 4 | proved for covered subclass |
| `19.30-vanishing-definition` | admissibility | a zero of some `Irr` character | used to separate membership of `p^a` in the two sets | exact |
| `19.30-equal-orders` | admissibility | `|G|=|S|=m` | transfers the full `p`-part and all order-divisor hypotheses | exact |
| `19.30-equal-vanishing-order-sets` | admissibility | equality of sets, not multisets | contradicted by presence versus absence of the single integer `p^a` | exact |
| `19.30-isomorphic` | target conclusion | `G \cong S` | follows in the restricted subclass after proving `G` simple and invoking Simple-order uniqueness | proved only for covered subclass |

## Target vs witness

There is no finite computational witness. The canonical target is the universal scope, whereas the proof vehicle covers only the explicitly restricted abstract subclass. Therefore `witness_equals_target: false`. Within that restricted theorem the hand proof reasons in exactly its quantified groups, so there is no additional quotient/model mismatch and no object constructed from the desired conclusion. The universal scope remains open, as recorded by `active_assignment_answered: no`.

## Subclaims and what each method proves

1. Clifford restriction proves the homogeneous orbit-sum formula in Lemmas 1 and 2. It does not itself prove Sylow normality.
2. Cyclotomic divisibility proves noncancellation at a generator of a cyclic normal Sylow `p`-subgroup. It does not say that arbitrary root sums or arbitrary `p`-elements are nonvanishing.
3. Strong induction plus the two added divisor/automorphism hypotheses proves normality of the full Sylow `p`-subgroup in every nonsimple same-order group. It does not establish those hypotheses for a named family.
4. Comparing the single order `p^a` and applying Simple-order uniqueness proves Theorem 4. It does not cover simple order-twins when uniqueness is absent.

## Evidence

### Artifact identity and tool boundary

The submitted proof file has the reported hash:

```text
$ sha256sum Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/scratch/minimal-normal-prime-separator.md
c0a0d6d72ab23072868a70189550420b50c300e479f80e6e0b5b381b31f038fc  Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/scratch/minimal-normal-prime-separator.md
```

The prescribed probe found GAP (package `gap-core` version `4.12.1-2build2`), Python 3.12.3, and `pdftotext` 24.02.0; Sage and Magma were not found. None was used for mathematics. No web search, historical solution, delegated reasoning, or computation entered this audit.

### Lemma 1

For `chi in Irr(X)`, Clifford restriction has the form

\[
 \chi_N=e\sum_{\lambda\in\mathcal O}\lambda
\]

for one nonempty `X`-orbit in `Irr(N)`. Since the trivial character is fixed by every automorphism, the orbit is either the singleton trivial character or consists entirely of nontrivial characters. At any `1 != x in N`, the group `N` has prime order, so `x` generates it. In the nontrivial-orbit case, a hypothetical zero is `f(zeta)=0` for a nonzero `0/1` polynomial of degree at most `p-1` and zero constant coefficient. Its divisibility by `Phi_p` is impossible below degree `p-1`; at degree `p-1`, equality of leading coefficients would force `f=Phi_p`, contradicting the constant coefficient. The trivial-orbit case has value `e != 0`. The coverage qualification in the consequence is therefore necessary and sufficient for the argument made. The `C_2 x S_3` warning example is also correct and is not used in later deductions.

### Lemma 2: orbit length and cyclotomic noncancellation

If the normal Sylow group `P` is noncyclic, no element can have order `|P|=p^a`; such an element would generate `P`. If `P` is cyclic and `x` is a generator, Clifford restriction again yields one orbit `O`. Conjugation by `P` on `P` is trivial, hence `P` lies in every character stabilizer and

\[
 |\mathcal O|=[X:I_X(\lambda)]\mid [X:P].
\]

Thus `p` does not divide the orbit length. Evaluation at `x` distinguishes all characters of the cyclic group, so a hypothetical zero gives a `0/1` polynomial `f` with `f(zeta)=0` and `f(1)=|O|`. Because `Phi_{p^a}` is monic in `Z[T]`, ordinary monic polynomial division (equivalently Gauss's lemma) shows that `f=Phi_{p^a}q` with `q in Z[T]`, not merely `Q[T]`. Evaluation at `1` then gives

\[
 |\mathcal O|=f(1)=\Phi_{p^a}(1)q(1)=p q(1),
\]

contradicting the prime-to-`p` orbit length. This closes both specifically requested points: the orbit length is a divisor of `[X:P]`, and no hidden rational denominator invalidates evaluation at `1`.

Every element of order `p^a` is a `p`-element, hence lies in the unique Sylow group `P`; in the cyclic case it is a generator. Lemma 2 follows.

### Lemma 3: both minimal-normal lifting cases

The strengthened induction is legitimate: among groups whose orders are divisors `d` of `m` with `p|d`, it asks for every group at `d<m` and for nonsimple groups at `d=m`. A least-order counterexample has a nontrivial minimal normal subgroup `N`, which is characteristically simple.

- If `p| |N|`, then abelian `N` is elementary abelian of `p`-power order. When the quotient is `p'`, `N` is already a normal Sylow subgroup. Otherwise the inverse image of the quotient's inductively normal Sylow subgroup is an extension of a `p`-group by a `p`-group and has the full `p`-part of `|X|`, so it is a normal Sylow subgroup. If `N` is nonabelian, then `|N|<m` (including the separate top-order and proper-divisor possibilities), contradicting CS-p.
- If `p` does not divide `|N|`, induction gives a normal Sylow subgroup `Pbar` of `X/N`; let `M` be its inverse image and take `P in Syl_p(M)`. Since `N` is a normal `p'`-group and `M/N=Pbar`, orders give `M=NP` and `P` maps isomorphically onto `Pbar`. Aut-p makes the conjugation homomorphism `P -> Aut(N)` trivial, so `[P,N]=1`. Consequently `P` is normal, hence the unique Sylow subgroup of `M` and characteristic in `M`; normality of `M` in `X` then gives `P normal X`. Finally, because `N` is `p'` and `Pbar` has the full `p`-part of `|X/N|`, `|P|=|X|_p`; thus `P` really is a Sylow subgroup of `X`, the small order equality implicit in the draft's last sentence.

No complement theorem is assumed in either case; the displayed order calculation supplies `M=NP`.

### Theorem 4

For nonsimple `G`, Lemma 3 gives a normal Sylow subgroup of order `p^a`, and Lemma 2 excludes `p^a` from `V_o(G)`. Target-vanishing puts that same integer in `V_o(S)`, contradicting equality of sets. Hence `G` is simple. Same order plus Simple-order uniqueness gives `G isomorphic S`. No converse or necessity claim is used.

## Verdict

**`status/conjectured`.** The mathematical hand audit finds that Lemmas 1–3 and Theorem 4 survive as the explicitly restricted reusable partial theorem, but the full review circle and human-visibility gate required for `status/proven` have not completed. The two focal risks—the prime-to-`p` Clifford orbit length and integral cyclotomic quotient—close exactly as stated. Both minimal-normal cases lift a full Sylow subgroup, with only one routine `p`-part equality left implicit in the draft.

**`active_assignment_answered: no`.** The canonical universal scope is explicitly open and receives no status promotion from this partial audit.

## Why this verdict

Each deduction in the four abstract statements follows from the hypotheses stated there; no external classification, computation, or unlisted character-table input is needed. The proof works in the groups it quantifies over and does not test a quotient or a property built into a witness. The additional hypotheses are materially stronger than the Kourovka assumptions, so exact scope accounting remains essential.

## What is NOT established

- The universal target `19.30/vanishing-order-simple-recognition` is not answered.
- No unconditional Suzuki specialization is certified. Inputs (E0)–(E7), the arithmetic conditions (P1)–(P2), and the assertion that they hold for any or infinitely many parameters were outside this audit and remain conditional.
- No particular nonabelian finite simple group or family is shown by the linked artifacts to lie in the surviving subclass.
- Simple groups having an order-twin, groups lacking a full-Sylow-order vanishing element, or orders violating CS-p or Aut-p are not covered.
- The four conditions are sufficient only; necessity is not claimed.

## What would upgrade it

To obtain a concrete family-level partial result, independently prove all four hypotheses for a named family and parameter range. To upgrade the active assignment, cover every finite simple `S` (including simple order-twins) or provide a fully admissible counterexample. The Suzuki branch requires independent grounding of every named external input and the relevant parameter condition before any promotion.
