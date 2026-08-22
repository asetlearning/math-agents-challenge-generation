---
title: "Bicategories, Biequivalence, and Bi-Interpretability"
authors: Anthony D'Arienzo, Vinny Pagano, Ian M.J. McInnis
year: 2020
venue: arxiv
url: https://arxiv.org/abs/2011.14056v2
url_translated:
language: en
domain: math-logic
status: draft
methodology_type: theoretical
citation_count:
citation_count_date: 2026-08-21
key_concepts:
  - "[[Concepts/bi-interpretability]]"
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "arXiv preprint (math.LO primary, math.CT secondary), v1 submitted 2020-11-28, v2 major rewrite 2023-07-09 (60 pages, reformulated using the bicategorical framework — this summary covers v2). Citation count not verified at ingest; no Semantic Scholar/Google Scholar entry surfaced via web search at ingest time. Third `#domain/math-logic` paper in the vault. Substantively overlaps with `[[daniyarova-myasnikov-2026]]` — both give a categorical criterion for (a strong form of) bi-interpretability via equivalence of derived categories — but the two use unrelated formalisms (exact completions of syntactic categories here vs. projective logical geometry there) developed independently; no citation link between them has been found in either direction."
author: brett-b
tags:
  - agent/research
  - user/brett-b
  - domain/math-logic
  - topic/bi-interpretability
  - topic/category-theory
  - topic/coherent-logic
  - topic/morita-equivalence
  - topic/model-theory
  - topic/interpretability-theory
  - topic/elimination-of-imaginaries
  - topic/definability
  - paper
  - status/draft
---

# Bicategories, Biequivalence, and Bi-Interpretability

## Abstract

> "We make explicit the correspondence between syntax and syntactic categories for coherent first-order logic, providing a categorical characterization of bi-interpretability. This is done by creating a biequivalence between a bicategory of coherent theories and the (strict) bicategory of coherent categories. While the biequivalence concerns the stronger equality-preserving bi-interpretability, we use it to obtain a necessary and sufficient condition for two theories to be bi-interpretable in general, by relating the exact completions of their syntactic categories. These results extend analogously to familiar fragments of first-order logic, thereby clarifying the long-intuited relation between logical syntax and syntactic categories."

*(Verbatim abstract, arXiv:2011.14056v2.)*

## TL;DR

A 60-page categorical-logic paper that builds a full bicategory of coherent first-order theories (theories as objects, "translations" as 1-cells, "t-maps" as 2-cells) and proves it is *biequivalent* to the 2-category of coherent categories — making precise, for the first time with a full coherence proof, an intuition Makkai and Reyes only sketched in 1977. The headline consequence is a proof of **Harnik's conjecture**: two coherent theories are bi-interpretable if and only if the *exact completions* of their syntactic categories are equivalent as categories. This resolves an open reconciliation problem between three competing notions of theory-equivalence in the recent literature (bi-interpretability, Morita equivalence, and classifying-pretopos equivalence) by pinning down exactly which categorical construction each one corresponds to.

## Problem

The paper poses and answers three questions (§1): (1) what categorical structure do coherent predicate theories form; (2) how does bi-interpretability (and other equivalence notions) fit into that structure; (3) how does that structure interact with Makkai–Reyes's syntactic-category and internal-logic operations. The technical target underlying all three is **Harnik's conjecture** (Harnik 2011): for theories in finite languages, the most general notion of interpretation is a logical functor 𝒞(T) → 𝒞(T′^eq) (T′^eq being Shelah's elimination-of-imaginaries extension), so T and T′ should be bi-interpretable iff 𝒞(T^eq) and 𝒞(T′^eq) are equivalent categories. Prior work had left this unsettled: Tsementzis (2017) characterized *Morita equivalence* via classifying pretopoi, but McEldowney/Tran-Hoang (2020/2023) showed Morita equivalence is strictly coarser than bi-interpretability in general (they coincide only when "coproduct Morita extensions" can be eliminated), so classifying pretopoi cannot be the right invariant for bi-interpretability itself — a smaller "classifying" category is needed, and reconciling this with Harnik's proper-theories result (𝒞(T^eq) ≃ the classifying pretopos of T, for *proper* T only) was the open puzzle.

## Approach

Built from first principles across five sections:

1. **Bicategory theory** (§2): reviews bicategories, pseudofunctors, biequivalence, and the "homotopy category" hC of a bicategory (1-cells identified up to iso in the hom-category), used later because bi-interpretability turns out to be exactly isomorphism in a homotopy category.
2. **Bicategories of theories** (§3): defines *translations* (many-sorted, Hodges-style reconstruals between signatures that preserve provability; a translation is *equality-preserving*, e.p., if it sends the language's equality relation to actual equality) and *t-maps* (2-cells between translations, generalizing natural transformations syntactically). Proves the collection of small coherent theories **CTh₀** is a genuine bicategory (translations as 1-cells, t-maps as 2-cells, with nontrivial unitors but trivial associators), and identifies **CThEq** as its full sub-bicategory of e.p. translations. Bi-interpretability is *defined* as homotopy equivalence (weak equivalence in the bicategorical sense) in CTh₀ (Definition 3.35).
3. **Biequivalence** (§4): extends Makkai–Reyes's syntactic-category functor 𝒞 and internal-logic functor 𝒯 to a pair of pseudofunctors 𝒞 : CThEq → **Coh** (2-category of coherent categories) and 𝒯 : Coh → CThEq, and proves they form a biequivalence.
4. **Bi-interpretability in general** (§5): defines a "categorification of exact completion" functor 𝒳 : hCTh₀ → hExactCoh (sending a theory to the *exact completion* of its syntactic category, 𝒞(T)^ex) and proves it is an equivalence of homotopy categories — extending the biequivalence of §4 from e.p. translations to arbitrary translations.
5. **Extensions and consequences** (§6): ports the same construction to classical logic (biequivalence with **Bool**, Boolean coherent categories), sketches the analogous statement for intuitionistic and κ-coherent logic, recovers Morleyization as a pseudofunctor (conjecturally part of a bi-adjunction), and relates the results to Morita equivalence.

## Key result

- **Theorem 3.32**: The collection of small coherent theories, with translations as 1-cells and t-maps as 2-cells, forms a bicategory **CTh₀**.
- **Theorem 4.27**: The syntactic-category and internal-logic operations extend to a biequivalence 𝒞 : CThEq ⇄ Coh : 𝒯. **Corollary 4.28**: two coherent theories T₁, T₂ are *e.p.* bi-interpretable iff 𝒞(T₁) and 𝒞(T₂) are equivalent categories.
- **Theorem 5.1 / Theorem 5.19** (the paper's headline result): two small coherent theories T₁ and T₂ are bi-interpretable **if and only if** the exact completions 𝒞(T₁)^ex and 𝒞(T₂)^ex are equivalent categories. Proved by showing the functor 𝒳 : hCTh₀ → hExactCoh is fully faithful and essentially surjective.
- **Corollary 6.8 / discussion following Prop. 6.7**: this recovers **Harnik's conjecture** exactly, since 𝒞(T^eq) is shown to coincide with the exact completion 𝒞(T)^ex (not merely the classifying pretopos, which it equals only when T is *proper* — Proposition 6.7: "A consistent coherent (or classical) theory T is proper if and only if 𝒞(T)^ex is a pretopos").
- **Theorem 6.1**: CThEq has weak (bicategorical) colimits, ported from an analogous result for Coh via the biequivalence.
- **Theorem 6.3**: the classical-logic analogue — ThEq (e.p. classical translations) is biequivalent to **Bool** (Boolean coherent categories), and this restricts 𝒳 to an equivalence hTh₀ ≃ hExactBool.
- **Theorem 6.4 / Corollary**: a classical theory's Morleyization T′ is e.p. bi-interpretable with 𝒯ι𝒞^Bool(T); Morleyization extends to a pseudofunctor ℳ : ThEq → CThEq, and T₁, T₂ are e.p. bi-interpretable iff their Morleyizations are.

## Assumptions

- Standard coherent first-order logic with equality (formulae built from ∃, ∧, ∨, ⊤, ⊥); no negation in the base setting (added separately for the classical-logic extension in §6.1 via Rule 6.2 and axiom schema IL12).
- All theories and categories are *small* (a set of objects, small hom-categories) — needed for the bicategory/2-category machinery to be well-behaved.
- Assumes and builds directly on the Makkai–Reyes (1977) syntactic-category/internal-logic apparatus and on Johnstone's *Sketches of an Elephant* coherent-category formalism; assumes familiarity with 2-category/bicategory theory (pseudofunctors, pseudonatural transformations, Gray's formalism).
- Associators are trivial throughout but unitors are not (a deliberate consequence of translations sending function symbols to substitution classes rather than to actual functions) — this is exactly why the paper needs bicategories rather than strict 2-categories (Remark 4.30: a *strict* biequivalence is provably impossible).

## Limitations / scope

- Purely theoretical/proof-theoretic: no computational, algorithmic, or complexity content, and no connection to Burnside groups, Knuth–Bendix rewriting, or this vault's B(2,5) program.
- The core biequivalence (Theorem 4.27) only directly characterizes the *stronger*, equality-preserving notion of bi-interpretability; general bi-interpretability requires the separate exact-completion argument of §5 (Theorem 5.1), which is considerably more technical (most of the paper's longest proofs, e.g. Theorem 5.19, live here).
- The generalized-Morleyization bi-adjunction (§6.2, Proposition 6.5 and its "if the above equivalence... satisfies the appropriate coherence conditions" caveat) is presented as a proof sketch with an explicit open question (Question 6.6) about which sub-bicategories of Coh admit the relevant left adjoint — not a fully proved result.
- Restricted to coherent logic and its familiar extensions (classical, intuitionistic, κ-coherent); the authors state the intuitionistic case needs additional reconstrual rules for ∀, ⟹, ¬ that are only briefly indicated (referencing IL11 in the appendix), not spelled out with the same rigor as the coherent case.

## Replication evidence

N/A — a pure proof-theoretic/category-theoretic paper (theorems with full proofs, largely relegated to a 17-page appendix); not an empirical or computational result subject to replication.

## Why this paper matters

This paper settles a specific, named open conjecture (Harnik's) that had been sitting unresolved at the intersection of model theory and categorical logic for over a decade, and does so by finally supplying rigorous 2-categorical/bicategorical foundations (translations, t-maps, coherence-law verification) that earlier related work (Visser's `INT^iso`, Kamsma's `CohTheory`) either restricted to purely relational signatures or left unverified. The result reorganizes how three competing notions of theory-equivalence relate to each other: Morita equivalence corresponds to equivalence of *classifying pretopoi* (Tsementzis), while bi-interpretability corresponds to equivalence of *exact completions* of syntactic categories — a strictly finer invariant that agrees with the pretopos-completion picture exactly on *proper* theories (Proposition 6.7 gives a clean, checkable criterion for properness in terms of the exact completion being a pretopos). For a vault already tracking the Daniyarova–Myasnikov "Theory of Interpretations" series, this paper is a directly relevant precedent: it proves a structurally similar theorem (a strong equivalence notion between structures ⟺ equivalence of an associated category built from each structure) via an entirely independent route — exact completions of Makkai–Reyes syntactic categories, rather than Daniyarova–Myasnikov's projective logical sets built on Plotkin's logical-geometry program. Neither series appears to cite the other; a reader who wants the sharpest available toolkit for turning bi-interpretability arguments into category-equivalence arguments now has two independently-developed, differently-flavored routes to compare.

## Quotes

1. > "We make explicit the correspondence between syntax and syntactic categories for coherent first-order logic, providing a categorical characterization of bi-interpretability." — Abstract
2. > "Proving some form of Harnik's conjecture would yield a categorical characterization of bi-interpretability, similar to Tsementzis' characterization of Morita equivalence." — §1

## Open questions surfaced

- **Question 6.6** (verbatim, §6.2): "Let D be a sub-bicategory of Coh closed under equivalence of categories... Under what conditions on D_∼ does d admit a (weak) left-adjoint?" — posed as the general form of the Morleyization adjunction, with only two examples (Pretopos, ExactCoh) currently known to satisfy it.
- Whether the sketched bi-adjunction ℒ ⊣ ℳ between coherent and classical theories (Proposition 6.5) actually satisfies the full 2-categorical coherence conditions for a genuine bi-adjunction — the authors give only a proof sketch and flag this as conditional ("if the above equivalence of categories satisfies the appropriate coherence conditions...").
- Not addressed by either paper: whether this paper's exact-completion characterization of bi-interpretability (Theorem 5.1) and `[[daniyarova-myasnikov-2026]]`'s projective-logical-sets characterization of *strong* bi-interpretability (Theorem 13 there) are two presentations of the same underlying invariant, or genuinely different constructions that happen to answer structurally analogous questions — a natural cross-formalism question for whoever reads both papers closely.

## Related material in vault

- Extends: (none in vault)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: `[[Concepts/bi-interpretability]]` — this paper is the third in the vault to substantively engage with bi-interpretability, alongside `[[daniyarova-myasnikov-2025]]` and `[[daniyarova-myasnikov-2026]]`; concept hub updated to reflect this paper's independent categorical route (exact completions of syntactic categories) alongside the projective-logical-sets route of Paper II.
- Cites: (none confirmed in vault; no direct citation relationship established with the Daniyarova–Myasnikov series despite substantial topical overlap — see `quality_notes`)
- Cited by (in vault): (none)
- Sibling math-logic notes: `[[daniyarova-myasnikov-2025]]` and `[[daniyarova-myasnikov-2026]]` — both engage with bi-interpretability and give categorical characterizations of a strong bi-interpretability variant, but via an unrelated formalism (projective logical geometry rather than exact completions of syntactic categories); `[[pakhomov-solda-2025-generalized-higman]]` — the vault's other non-series math-logic paper, connected only at the field level (order theory/reverse mathematics vs. model theory/categorical logic here).

---

## Notation conventions

Sequent and category-theoretic notation in this note (turnstiles, functor arrows, superscripts like `T^eq`) is rendered in plain Unicode/prose rather than LaTeX double-bracket forms; no `[[...]]`-style commutator or bracket expressions requiring backtick-escaping appear, per `[[paper-summary]]` § Notation conventions.
