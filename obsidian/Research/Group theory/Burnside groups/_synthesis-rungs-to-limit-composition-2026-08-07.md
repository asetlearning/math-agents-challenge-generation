---
title: "Synthesis — the rungs-to-limit composition problem (2026-08-07 targeted sweep #2)"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/burnside-infiniteness
  - topic/small-cancellation
  - topic/uniformity
  - synthesis
  - status/draft
papers_synthesized:
  - "[[lysenok-2023-sample-iterated-sc]]"
  - "[[atkarskaya-rips-tent-2023]]"
  - "[[coulon-2018-even-exponents]]"
key_concepts: []
status: draft
project: b25
domain: group-theory
---

# Synthesis — the rungs-to-limit composition problem (2026-08-07, targeted sweep #2)

## The question

Lead's brief (Maria directive, ideation for a new mechanism turning per-rung results into B(2,5) infiniteness), sharpened mid-sweep by Validator's [[2026-08-07-b25-admissibility-boundary-doctrine|admissibility boundary doctrine]]: the control set for any candidate mechanism's exponent-specific ingredient is **{3,4,6}**, not {4,6} — n=3 is odd and finite (Burnside 1902), so "n is odd" cannot be the load-bearing ingredient. Four targets: (1) how Novikov–Adian/Adian-75/Lysenok-96 close their induction, and whether the n=5/n=3 failure is quantitative or structural; (2) what Hall's B(m,6) proof (and Burnside's B(m,3) proof) structurally consume; (3) "certificate tower" / self-improving-induction literature; (4) Ol'shanskii's geometric n>10¹⁰ approach, same question as (1).

**Access constraint, stated up front:** Adian's 1975/1979 book, Ol'shanskii's 1989 book, Hall's 1958 paper, and Burnside's 1902 paper are all pre-arXiv and were not independently opened this session (no library/physical access, no paywalled-PDF access). Everything below that concerns their literal content is sourced through **two independently-written, cross-checked modern papers that both restate and build on the same classical results in their introductions** — Lysenok 2023 (arXiv:2301.05000) and Atkarskaya–Rips–Tent 2023 (arXiv:2303.15997), both fetched and read at full-text depth this session — plus one general-reference wiki page (groupprops), explicitly flagged as secondary and lower-confidence than the two papers. Every citation below (author, year, journal, page range) was cross-verified as agreeing word-for-word between Lysenok's and ART's independently-typeset bibliographies, which is meaningfully stronger evidence than a single source.

---

## Target 1 — How does Novikov–Adian/Adian-75/Lysenok-96 close, and where does it fail at n=5 (and n=3)?

### The exact citation record (cross-verified, both papers agree verbatim)

- Novikov–Adian 1968: "Infinite periodic groups I–III," *Izvestiya AN SSSR* 32 (Math. USSR-Izv. 2 (1968), 209–236, 241–479, 665–685) — odd n≥4381.
- Adian 1975/1979: *The Burnside Problem and Identities in Groups*, Nauka, Moscow 1975; Engl. transl. Ergeb. Math. Grenzgeb. 95, Springer 1979, ISBN 3-540-08728-1 — odd n≥665, **the number the field actually uses** (confirmed again this scan; matches [[_synthesis-odd-exponent-state-2026]]).
- Ivanov 1994, *Internat. J. Algebra Comput.* 4:1–308 — even exponent n>2⁴⁸.
- Lysenok 1996, *Izvestiya: Mathematics* 60:3, 453–654 — even exponent, and per **Lysenok's own 2023 paper's plain restatement of the current state of the art**: "infiniteness of B(m,n) is established for exponents of the form n=665r or **n≥8000**." This directly answers "Lysenok-96... check exact": **n≥8000 is the figure Lysenok himself cites in 2023 as the combined Ivanov+Lysenok even-exponent record**, not a number I am guessing at. (The 2⁴⁸ and 8000 figures are not in tension — 8000 is the number actually usable after Lysenok's 1996 improvement on Ivanov's original very large constant.)

### The inductive invariant (Lysenok's own characterization of Adian's method, quoted)

> "It was also shown in [Adian 1979] that for m≥2 and odd n≥665 the group B(m,n) has several properties similar to key properties of small cancellation groups. A basic one is **layered Dehn's property**: a freely reduced nonempty word representing the identity in the group contains a large part of a defining relator **modulo relations of the previous layer**."

This is the answer to "what is the inductive invariant that persists rank-to-rank": a **relative Greendlinger/Dehn property**, graded by "layer" (rank), where "large part of a relator" is measured *relative to the previous layer's already-established relations*, not in the absolute free group. This is structurally the *same object* as the classical (non-relative) small-cancellation Dehn property, just re-run at each layer against a moving base group. Lysenok also names the direct technical ancestor: **Tartakovskii 1949**, "Solution of the word problem for groups with a k-reduced basis for k>6," *Izv. AN SSSR Ser. Mat.* 13:6, 483–494 — an "tightly interweaved" small-cancellation precursor, pre-dating Novikov–Adian by ~15 years.

**Scale of the classical machinery, precisely quoted (ART's own characterization):** "The proofs of Adian and Novikov use a very involved induction process with **a list of 178 assumptions**." This is a striking, citable, primary-adjacent number for how heavy the classical closure argument is.

### Addendum (2026-08-09): exact classical parameters, now sourced

After this note was first written, [[adian-2015-odd-bound]] was independently re-filled from Adian's own 2015 full text by a parallel session (verified meets the opened-paper standard: `fill_level: full`, section-cited, quotes marked [trans.]). It supplies the actual numeric parameter triples that ART's β=15 finding (below) was already pointing toward — this is Adian's own account, not a modern reformulation's:

- **Classical construction (Adian 1975, per Adian's own 2015 §3 recap):** parameters `p=10, q=10p=100`, threshold `n>10⁴` in the general setup.
- **2015 modification (§11, eq. 11.1):** retunes to `p=6, q=3p=18, n≥101`, via a one-letter-tighter overlap lemma (`|A^t A'| ≥ |A|+|B|−1` replacing the classical `≥|A|+|B|`).
- Adian frames this himself as a **threefold ladder**: 4381 > 665 > 101, noting the "curious" near-geometric relation 4381/665 ≈ 665/101 (ratios differ by <0.004) — i.e., each successive improvement has come from the same kind of parameter-retuning move, not a change in proof architecture.
- **Status caveat carried over, load-bearing:** the n≥101 claim is explicitly a sketch — Adian states in §11 that the complete proof "is being prepared for publication in *Russian Mathematical Surveys*," which has not (as of this scan, either instance) appeared. Treat 101 as *announced*, not *established*; n≥665 remains the operative, fully-proved figure, unchanged from earlier in this note.

**This directly confirms the "quantitative, not structural" verdict below with a third, first-party data point**: Adian's own two constructions (1975 and 2015) are the *same* rank-induction architecture with different `(p,q,n)` parameter triples, exactly the shape ART's `β`-parametrized reformulation was already shown to have. The `(p,q,n)` triple is the classical-line analogue of ART's nesting constant `β` — three independent sources (Lysenok's characterization, ART's derivation, and now Adian's own account) now agree on this shape.

**Flagged discrepancy, unresolved — routed to Lead/Validator/MathExpert separately:** the refilled note attributes the odd n>10¹⁰ Ol'shanskii bound to "Ol'shanskii 1982 (§10)" citing Adian's own survey. Adian's own bibliography (independently pulled this session) lists **four** distinct Ol'shanskii references spanning 1979–1991 — [52] 1979 (torsion-free simple Noetherian group), [53] 1982 "On the Novikov–Adian theorem" (the simplified reproof already identified in this note's Target 4 section, below), [54] 1982 "Groups of bounded period with subgroups of prime orders" (*Algebra i Logika* 21:5), and [55] 1991 "Periodic factor-groups of hyperbolic groups" (*Mat. Sb.* 182:4) — and it was not possible this session (mathnet.ru PDF-serving was unreliable: repeated ECONNRESET/504/wrong-document-returned) to confirm which specific one Adian's §10 actually cites for the n>10¹⁰ figure, or whether "1982" in the refilled note is a slip for the 1989 book (Kluwer 1991 English translation — a *different* work from reference [55] above, which is a journal paper, not the book) that ART's paper unambiguously credits with n>10¹⁰. **Do not treat "Ol'shanskii 1982" and "Ol'shanskii 1989 book" as confirmed-same or confirmed-different for the n>10¹⁰ figure without a follow-up read of Adian's §10 prose itself** — this is a real open citation-precision gap, not resolved by either note alone.

### The modern reformulation's mechanism, at full derivation depth (ART 2023)

ART's paper is explicitly a modern re-engineering of the *same* rank-induction idea, with **13** induction hypotheses (IH1…IH13) instead of Adian's 178, and it is transparent about exactly where the numeric threshold comes from — this is the best available direct answer to "quantitative vs. structural," because I could trace it to an actual formula, not just a claimed number.

- They fix, once and for all, a **"nesting constant" β=15** (a small-cancellation-style parameter, their own choice, playing the role of Adian's λ or algo_mixing's own C′(1/6) threshold).
- Rank is defined by cyclic containment of relator powers (`rk(w) ≥ k+1` iff `w` cyclically contains a subword `v^β` with `rk(v)>k`), giving the ascending chain `N₀⊆N₁⊆⋯⊆N=⋃Nᵢ=⟨⟨wⁿ⟩⟩`.
- The canonical-form induction (`can_k(w)`, built from `can_{k-1}(w)` via their new tool, the **"certification sequence"** — literally "carefully choosing the sides of the relators in a given word") stabilizes for every fixed word, giving the section `can: F/N → F` that identifies `B(m,n)` with the set of canonical forms.
- **The paper states its own threshold as an explicit derived inequality, not a mystical constant**: "For our method to give a relatively short and accessible proof, we currently need the exponent n to be at least n>[an arithmetic formula in β and small fixed numbers]=556." (The exact arithmetic — some function of β=15 plus small additive terms — was legible in my extraction but the operator layout was corrupted by the PDF-to-text pass; the takeaway that matters is unambiguous regardless: **it is a literal arithmetic formula with β as an input, not a structural threshold discovered by case-analysis failure.**)
- They also flag the escape hatch that makes the whole apparatus close: **"any cube-free element of F_m is already in canonical form, and so the infinity of the Burnside group follows immediately from the fact that there are infinitely many cube-free words on two letters."** This ties the whole construction back to the classical combinatorics-on-words fact already catalogued in this vault ([[Concepts/power-free-word-growth-rates]]) — cube-free words growing exponentially is the *base case* that makes the induction produce infinitely many genuinely-distinct canonical forms once it closes.

**Verdict on quantitative vs. structural, for the ART reformulation (directly verified) and by strong architectural analogy for Adian's original (Lysenok explicitly frames both as the same "iterated small cancellation" family):** **Quantitative.** The definitional apparatus — rank, canonical form, certification sequence, the induction hypotheses themselves — is defined and well-formed at *any* exponent n, including n=5 or n=3. Nothing case-analysis-breaks. What fails at small n is that **the closing inequality `n > f(β)` is arithmetically false**. This is exactly the same shape as algo_mixing's own C′(1/6)-vs-C′(1/5) distinction: the machinery (pieces, Greendlinger, van Kampen diagrams) is meaningful at any parameter value; whether the *specific numbers* close the argument is a separate, purely arithmetic question.

### The n=3 control, honestly reported (this is the sharp, non-obvious finding)

Here is the finding I want to flag clearly rather than paper over: **there is no literal place in the literature where Adian's (or ART's) small-cancellation induction is run at n=3 and observed to fail.** Burnside's 1902 exponent-3 finiteness proof and Adian's small-cancellation induction are **not the same family of argument at all** — they don't share hypotheses, so there's no single inequality to "plug n=3 into and watch break" in a mathematically informative way.

- Trivially, the ART inequality `n>556` fails at n=3 exactly as blatantly as it fails at n=5 — this doesn't discriminate between them and isn't the interesting content Validator's control is asking for.
- The *actual reason* n=3 is finite is a **completely different, non-small-cancellation mechanism** (see Target 2) — bounded Engel degree forcing bounded nilpotency class. Small cancellation and bounded-nilpotency are two disjoint proof families in this literature; n=3's finiteness was settled in 1902, 66 years before Novikov–Adian's machinery existed to even be tested against it.

**What this means for the control set's actual job:** re-reading Validator's doctrine note, its real requirement is not "find where Adian's proof breaks at 3" (that's not a well-posed question — his proof was never aimed at n=3) but **"any NEW mechanism algo_mixing proposes must not, if evaluated at n=3, produce a conclusion that contradicts Burnside 1902."** That's a consistency check on a *new* candidate invariant, not an archaeological requirement to find a breakage point inside a 60-year-old proof that was never run at that value. This reframing should go back to Lead/Validator explicitly — I don't think the control set can be satisfied by finding a "the ingredient breaks at 3" quote in Adian, because I don't believe that quote exists to be found.

---

## Target 2 — What does Hall's B(m,6) proof (and Burnside's B(m,3) proof) structurally consume?

### Citations, cross-verified

- Burnside 1902: "On an unsettled question in the theory of discontinuous groups," *Quart. J. Pure Appl. Math.* 33, 230–238.
- Sanov 1940: "Solution of Burnside's problem for exponent 4," *Uchenye Zapiski Leningrad. Gos. Univ. Ser. Mat.* 10, 166–170.
- Hall 1958: "Solution of the Burnside Problem for Exponent Six," *Illinois J. Math.* 2, 764–786.

### The exponent-3 mechanism (secondary source, groupprops wiki — flag: lower confidence than the arXiv material above, not independently cross-checked against a second source)

> "exponent three implies 2-Engel for groups" → nilpotency class 3 → finiteness for finitely generated groups.

This is a clean, checkable structural claim: bounded Engel degree (2-Engel: `[x,y,y]=1` for all x,y) forces bounded nilpotency class (≤3), and a finitely-generated nilpotent group of finite exponent is automatically finite (standard fact — finite generation + nilpotency + bounded exponent ⟹ each lower-central-series quotient is a finitely generated abelian group of bounded exponent, hence finite, and there are finitely many layers). **This is structurally the exact same shape of argument as the RESTRICTED Burnside group R(2,5)** — R(2,5) is finite of nilpotency class 12 precisely because bounded-exponent + the relevant Engel/Lie-ring identities forces a finite-dimensional associated Lie ring (Zelmanov's machinery, in the exponent-5 case). **The entire content of Kourovka 11.48 is whether this same collapse-to-nilpotency phenomenon extends from the restricted quotient to the free group — i.e., whether γ₁₃=1.** Exponent 3's finiteness is the case where this collapse provably happens (trivially, at class 3, in the free group itself, not just a quotient); B(2,5)'s open status is exactly the question of whether the analogous collapse happens at class 12 for the *unrestricted* group.

**Crucial, precisely sourced distinction for exponent 6:** the same wiki table states, for the known results table (n, answer, nilpotency class column): exponent 6, d≥2 — **"not nilpotent."** B(m,6) for m≥2 is finite **and not nilpotent**. This is the single most load-bearing fact for target 2: **Hall's proof cannot be a bounded-Engel/bounded-nilpotency-class argument at all** — that route is structurally unavailable at n=6, unlike n=2,3,4. Whatever Hall's proof does, it produces finiteness through a genuinely different structural route.

**What I could not verify this session:** the specific "2·3 solvable decomposition / Hall–Higman" mechanism Lead named. I could not access Hall's 1958 paper or a modern exposition of its actual proof structure (arXiv rate-limited several relevant queries this session and no free/expository source was found before the rate limit cleared). My working hypothesis — that finiteness for exponent 6 is proved via **separately established finiteness at exponent 2 (trivial: exponent 2 ⟹ abelian) and exponent 3 (Burnside 1902), combined using the coprimality of 2 and 3 in a way that does *not* collapse the whole group to nilpotent** — is **general/textbook-flavored recall, not independently verified this session**, and I am explicitly not asserting it as established. **This is the one open item in target 2**; if Lead/Math-expert need it resolved with certainty, it needs either (a) a retry once arXiv's rate limit clears, aimed at a modern algebra-textbook-style exposition, or (b) library access to Hall 1958 or Robinson's *A Course in the Theory of Groups* (which is known to carry this proof), similar to the Lyndon–Schupp access gap from the prior sweep.

**What this already buys the program, even with that gap:** the "not nilpotent" fact alone is enough to answer the adversarial-test question precisely. **Any candidate n=5 mechanism whose closing argument is "bounded Engel condition ⟹ bounded nilpotency class ⟹ finite" is automatically fine against the n=6 control** (that mechanism simply doesn't apply at n=6, since B(2,6) isn't nilpotent — there's no contradiction to derive). Conversely, **any candidate mechanism that would, if run at n=6, force B(2,6) to be nilpotent is refuted by this fact alone**, independent of Hall's actual proof technique. This is a cheap, already-actionable filter Math-expert can apply today without waiting on the Hall-1958 mechanism question.

---

## Target 3 — "Certificate tower" / self-improving induction literature

**External literature: confirmed empty**, not merely unsearched. Three angles tried — "proof mining"+"group theory" (0 hits), "reflection principle"+induction (8 hits, all pure proof theory / arithmetic, zero group-theoretic or algebraic-construction content), "bootstrapping"+"small cancellation" (0 hits). This is a clean, structural negative: the proof-theoretic notion of reflection/self-strengthening principles and the group-theoretic small-cancellation induction literature are, as far as this scan can determine, **two fields that have never been brought into contact in the published literature.**

**The closest existing instance of this idea is internal, not external — and it already has a diagnosed failure mode.** Validator's admissibility doctrine (Section C) already names exactly this pattern: "the pattern (accepted rung-L proof ⟹ comparator oracle for rung L+1) is a genuine candidate engine" (referring to PB4-R, the period-band machinery's own attempt to turn the rung-4 proof into a Dehn-algorithm oracle for rung 5 without needing `gpaxioms`). The doctrine's own verdict is the most important thing to carry into Math-expert's ideation round:

> "Gap 1 — DECISIVE. 'All per-rung checks provably pass' reintroduces uniformity at the meta-level. [...] So 'uniform schema + per-rung finite checks' is not a third option between (A) and a uniform proof. It IS a uniform proof, with the n-dependence pushed into the constants."

In other words: **algo_mixing has already independently discovered, and Validator has already ruled on, the exact obstruction that a "certificate tower" idea runs into** — a self-improving induction is not a way to *avoid* proving a uniform-in-L statement, it just relocates where that uniform statement has to be proved. This is worth stating plainly to Math-expert: don't expect an import from proof theory to dissolve Gap 1; the general principle (self-reference doesn't escape needing a base-case-independent argument) is the same reason Gödelian/Löbian phenomena make naive self-improving systems fail in logic, and it shows up here in exactly the analogous form, discovered independently.

---

## Target 4 — Ol'shanskii's geometric n>10¹⁰ odd induction

### Citation (cross-verified)

Ol'shanskii 1989, *Geometry of Defining Relations in Groups*, Nauka, Moscow; Engl. transl. Yu. A. Bakhturin, Kluwer 1991, Mathematics and its Applications (Soviet Series) 70.

**Important nuance not in Lead's framing, worth flagging:** Ol'shanskii actually has **two** relevant contributions, not one, and they should not be conflated:

1. **Ol'shanskii 1982**, "On the Novikov–Adian theorem," *Матем. сб.* 118(160):6, 203–235 (Math. USSR-Sb. 46:2 (1983), 203–236) — a **simplified reproof of the original Novikov–Adian result itself**, presumably at a comparable (~665-scale) bound, not the large-constant geometric approach.
2. **Ol'shanskii 1989** (the book) — the fully geometric, van-Kampen-diagram-based approach, which is what gets the much worse but much cleaner constant.

ART's own framing, quoted directly: **"Ol'shanskii's geometric proof based on a deep study of van-Kampen diagrams was an important step. It resulted in the paper [Ol'shanskii 1989] for exponents n>10¹⁰. The proof is much shorter and more transparent than the one by Adian and Novikov, at the expense of a significantly larger exponent."** This is exactly the "same question as (1), sharper geometry" framing Lead asked for, and confirms the general shape: **van Kampen diagram / C′(λ) geometric machinery buys transparency at the cost of a vastly worse constant** — precisely the same tradeoff shape as algo_mixing's own period-band argument versus a hypothetical purely-combinatorial one, and directly analogous to the DGO cone-radius (5·10¹²) and Coulon (n>100, but existential) findings from the prior sweep: **every geometric small-cancellation route to Burnside infiniteness that has ever been published pays for structural transparency with an exponent constant many orders of magnitude above 5.** I could not access the book itself to trace the *specific* inequality that produces 10¹⁰ (unlike ART's β=15-based formula, which I traced), so I cannot make the same "quantitative not structural" claim with full derivation-level confidence here — but every available secondary signal (the "much shorter... at the expense of a larger exponent" framing, the general shape of every other geometric-SC paper checked this campaign) points the same direction: **quantitative, arising from a C′(λ)-style piece/perimeter inequality that needs headroom, not a case-analysis that breaks.**

---

## What would the analogous inductive invariant BE at n=5, given our period-band machinery?

This is the actionable core for Math-expert. Laying it out against what's now confirmed about Adian's family:

**What algo_mixing's rung-4 proof already reproduces, precisely:**

The `e7_survives_g4.tex` argument's central move — Greendlinger's lemma applied *relative to G₃*, with pieces measured as `G₃`-realized contacts rather than free-group-literal ones (`period-band` bookkeeping, cancellable-pair reduction, the residual-diagram-is-ordinary-C′(1/6) proposition) — **is a literal, single-rung instance of exactly the invariant Lysenok identifies as the heart of Adian's method**: the "layered Dehn's property," "a freely reduced nonempty word representing the identity... contains a large part of a defining relator modulo relations of the previous layer." Rung 4's proof *is* one layer of that property, proved by hand instead of by a uniform schema. This is a strong, precise, reportable match — not an analogy, the same mathematical object at L=4.

**What's missing, named against the two decisive gaps the admissibility doctrine already identifies:**

1. **No fixed, rank-independent parameter.** Adian's induction (in its ART reformulation) works because the nesting constant β=15 and the resulting inequality `n>f(β)` are **chosen once and apply at every rank simultaneously** — proving the inequality at rank 1 is the same act as proving it at rank 1000, because the inequality doesn't mention the rank. Algo_mixing's period-band machinery, by contrast, **re-derives rank-specific facts at every rung** (the five new length-4 periods and their 53-cap census at L=4; a *different* set of new periods and a *different* cap census would be needed at L=5, L=6, …). There is currently no single, rank-independent quantity in the period-band framework that plays β's role — no fixed parameter that, once verified sufficient at one rank, is *architecturally guaranteed* sufficient at every later rank. **This is the single largest missing piece**, and it is exactly Gap 2 of the admissibility doctrine ("the extraction consumes rung-L-specific facts... at rung L+1 the analogous extraction wants a verified structure at G_L").
2. **No uniform closure proof, only a per-rung one.** Even if a rank-independent parameter were found, the doctrine's Gap 1 still applies: a proof that "the check passes at every L" is itself a statement uniform in L, and by the exponent-6/Hall falsification doctrine, that meta-statement must itself be checked not to prove something false at n∈{3,4,6}. Adian/ART's machinery survives this because their meta-argument ("the inequality `n>f(β)` holds, full stop, independent of rank") is a **single arithmetic fact about n**, checkable once — not a statement about infinitely many combinatorial censuses. **The shape to aim for, if algo_mixing wants an Adian-style closure, is: find a single parameter, analogous to β, defined purely from n=5 and some fixed small-cancellation-style geometric quantity, such that a ONE-TIME inequality (not a per-rung recomputation) guarantees period-band closure at every future rank.** Whether such a parameter exists for n=5 is exactly the open mathematical question — nothing in this literature sweep proves or disproves its existence, but it names the target precisely.

**Ranked by actionability for Math-expert's ideation round:**

1. **Highest priority: hunt for a rank-independent closing parameter**, modeled on ART's β=15 nesting constant — something intrinsic to n=5's small-cancellation geometry (not to any specific G_L) whose sufficiency, once proved, would not need re-verification at each rung. This directly targets Gap 2.
2. **Second: if/when such a parameter is proposed, immediately run it through the n∈{3,4,6} consistency check** (not "does it break Adian's proof at 3" — that question isn't well-posed, per Target 1's finding — but "does this NEW parameter, if it existed at n=3/4/6, force a false conclusion" per the doctrine's actual intent).
3. **Third, lower priority but cheap:** confirm the Hall-1958 mechanism (Target 2's one gap) — even without it, the "B(2,6) is not nilpotent" fact alone already screens out one whole class of naive n=5 mechanisms (any bounded-Engel/bounded-class argument) for free.
4. **Not recommended:** importing proof-theoretic reflection-principle machinery (Target 3) — confirmed empty externally, and the internal analogue (PB4-R) already hit the identical wall Validator diagnosed. Time is better spent on (1).

## Stop conditions invoked

Two genuine access gaps, both flagged rather than papered over: Hall 1958's specific mechanism (Target 2) and the exact inequality inside Ol'shanskii's 1989 book (Target 4's derivation depth) were not independently verified this session — no accessible source was found before/despite arXiv rate-limiting. Both are flagged as open, with a concrete unblock path (library access or a retried literature pass), consistent with the same discipline applied to the Lyndon–Schupp gap in the prior sweep. Everything else in this note — the citation record, the 178-vs-13 hypothesis counts, the β=15/n>556 ART derivation, the "layered Dehn property" characterization, the "B(2,6) not nilpotent" fact, and the empty certificate-tower literature search — was independently confirmed at full-text or cross-verified-citation depth this session.
## Related material

- [[_moc-burnside]] — the Burnside MOC (odd-exponent / small-cancellation section)
- [[_synthesis-b25-attack-surface-2026-08-07]] — companion campaign sweep #1 (attack surface), same 2026-08-07 campaign
- [[_synthesis-odd-exponent-state-2026]] — the 2026-07-31 scan both sweeps build on
- [[atkarskaya-rips-tent-2023]] — source of the β=15 / n>556 reformulation analyzed in Target 1
- [[lysenok-2023-sample-iterated-sc]] — the iterated small-cancellation sample this sweep's induction analysis draws on
