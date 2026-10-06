---
title: "Random van Kampen diagrams and algorithmic problems in groups"
authors: Alexei G. Myasnikov (Miasnikov), Alexander Ushakov
year: 2011
venue: "Groups Complexity Cryptology 3(1) (2011) 121–185"
url: https://doi.org/10.1515/gcc.2011.006
url_translated:
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: 11
citation_count_date: 2026-10-05
key_concepts:
  - "[[Concepts/certified-instance-generation]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[kapovich-2003-generic-case-complexity]]"
cited_by: []
quality_notes: "ABSTRACT-ONLY INGEST: full text NOT read. The paper is closed access (Unpaywall/OpenAlex: oa_status closed; no arXiv version; ResearchGate 403; De Gruyter page blocked automated fetch; the Stevens ACC publication list gives only the DOI). The abstract is verbatim from the Stevens research portal. Everything else in this note comes from SECONDARY sources, each attributed in the text: (i) Myasnikov's talk abstract, McGill GGT seminar, 2 Feb 2005; (ii) Morar–Ushakov, 'Search problems in groups and branching processes', arXiv:1407.1685, §1.4 and §3.1, which restates the depth definition and cites the solver bound as Theorem 16.4.3 of the Miasnikov–Shpilrain–Ushakov book 'Non-commutative cryptography and complexity of group-theoretic problems' (AMS Surveys 177, 2011), NOT of this paper; (iii) 'Knapsack problems in groups', arXiv:1302.5671, Proposition 5.1, which attributes the hyperbolic log-depth bound to this paper. No internal section, theorem or lemma numbers of the GCC paper are available, so none are given. Citation counts: Semantic Scholar 11, OpenAlex 7 (both 2026-10-05). Ushakov's PhD thesis 'Fundamental search problems in groups' (CUNY Graduate Center, 2005) seems to contain the underlying work and was also not accessible."
author: asetlearning
project: challenge-gen
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/word-problem
  - topic/trivial-words
  - topic/average-case-hardness
  - topic/hard-instance-generation
  - topic/proof-certificates
  - project/challenge-gen
  - paper
  - status/draft
---

# Random van Kampen diagrams and algorithmic problems in groups

> **Source caveat.** This note was written from the abstract and secondary sources only. The full text was not accessible (see `quality_notes`). Statements marked *(secondary)* restate this paper's results as later papers by the same group report them. They are not quoted from the paper.

## Abstract

"In this paper we study the structure of random van Kampen diagrams over finitely presented groups. Such diagrams have many remarkable properties. In particular, we show that a random van Kampen diagram over a given group is hyperbolic, even though the group itself may not be hyperbolic. This allows one to design new fast algorithms for the Word Problem in groups. We introduce and study a new filling function, the depth of van Kampen diagrams, - a crucial algorithmic characteristic of null-homotopic words in the group."

## TL;DR

Fix a finite presentation. Build trivial words by randomly inserting relators, which gives random van Kampen diagrams. Such diagrams are generically "hyperbolic", meaning shallow: their **depth** (the largest dual-graph distance from any cell to the outside) is small. A relator-closure solver whose cost is exponential in depth therefore solves the word *search* problem on these inputs in generic polynomial time. The paper's filling function is **depth, not area**. It treats random diagrams over a *fixed* group, not random groups.

## Problem

How hard is the word search problem (find a witness that $w =_G 1$) in a finitely presented group on *typical* inputs, as opposed to worst-case inputs? The motivation is cryptographic. The Wagner–Magyarik public-key scheme hides a message by randomly rewriting a word with relators, so its security depends on such random words being hard. Morar–Ushakov §1.3 (secondary) records this framing and describes [this paper] as the analysis of those random-rewriting "challengers". A second aim is to find the geometric parameter of a null-homotopic word that controls algorithmic cost. The paper's answer is depth.

## Approach

*(secondary + abstract; the details of the proof are not available)*

- **Random object.** The objects are random van Kampen diagrams over a fixed finite presentation $(X;R)$, equivalently the trivial words produced by randomly inserting relators (and free cancellations $xx^{-1}$) into a word. Morar–Ushakov §1.4 says the generators in [this paper] and in Ushakov's thesis "generate words in $(X^{\pm})^*$, i.e., nonreduced words." Their own 2014 follow-up moves to freely reduced outputs and uses Crump–Mode–Jagers branching processes. It is a reasonable guess that the 2011 paper also uses random-tree / branching analysis, but this is **unverified**.
- **Geometry.** The paper shows that a random diagram is "hyperbolic", meaning thin or shallow, "even though the group itself may not be hyperbolic" (Abstract).
- **Algorithm.** Algorithm A (secondary: Morar–Ushakov §3, citing the MSU book) repeatedly attaches all relator loops at every vertex of the graph Γ(w) ("R-completion") and then performs Stallings folding. It stops when the endpoints of the path w are identified. The number of rounds is bounded by depth.

## Key result

**(R1) Random diagrams are hyperbolic.** Abstract: "a random van Kampen diagram over a given group is hyperbolic, even though the group itself may not be hyperbolic."

**(R2) Generic polynomial time for the word search problem** (talk abstract, McGill GGT seminar, 2 Feb 2005; secondary): "we will show that the generic case time complexity of the search word problem in finitely presented groups is polynomial." The exact theorem statement, the measure, and the exponent are **not available**.

**(R3) Depth: the filling function introduced here.** Verbatim restatement in Morar–Ushakov §3.1, which says depth was "introduced in [the MSU book]". The GCC abstract also says "We introduce and study a new filling function, the depth":
- Dual graph $D^*$: the vertices are the cells of $D$ plus the outer cell $c_{out}$. Two cells are adjacent if their boundaries intersect: $E^* = \{(c_1,c_2) \mid \partial c_1 \cap \partial c_2 \ne \emptyset\}$.
- $\delta(D) = \max_{c \in C(D)} d^*(c, c_{out})$.
- $\delta(w) = \min\{\delta(D) \mid \mu(D) = w,\ D$ a van Kampen diagram$\}$ if $w =_G \varepsilon$, and $\infty$ otherwise.
- Note: adjacency is *sharing at least one vertex*, not only an edge. "Knapsack problems in groups" §5 uses the same convention.

**(R4) Solver cost is exponential in depth.** This is attributed to the MSU book, Theorem 16.4.3, not to this paper. Quoted by Morar–Ushakov as Theorem 3.3: "Algorithm $A_{WP}$ stops on the input $(X;R), w$ if and only if $w =_G \varepsilon$. Furthermore, it terminates in at most $\delta(w)$ iterations and the time complexity of Algorithm $A_{WP}$ is bounded above by: $\tilde O\big(|w|\,L(R)^{\delta(w)}\big)$", where $L(R) = \sum_{r\in R}|r|$. So **depth $O(\log |w|)$ ⇒ polynomial time**, and depth linear in $|w|$ ⇒ exponential time.

**(R5) Hyperbolic groups have logarithmic depth.** "Knapsack problems in groups" (arXiv:1302.5671), Proposition 5.1, attributed to this paper: "Let G be a hyperbolic group given by a finite presentation G = ⟨X | R⟩. Then for any word w = w(X) with w =_G 1 one has δ(w) = O(log₂ |w|)." The proof of Lemma 5.4 there uses it as "O(log |v|)", so log₂ means base 2, not log squared.

**(R6) Follow-up, for context only.** Morar–Ushakov 2014, Theorem A: for any finite presentation, $A_{WP}$ solves the word search problem on words from their reduced-word random generator "generically in polynomial time $\tilde O(n^{1+e^2 \ln L(R)})$". They call this "a significant improvement over" [this paper], whose generators produce nonreduced words.

**What the paper does NOT (as far as can be determined) prove:**
- **(a) Area.** No secondary source reports an area or Dehn-function bound for random diagrams. The filling function studied is depth. Area is bounded *above* by a function of depth and boundary length. Bounded-degree growth gives roughly $|w| \cdot c^{\delta}$, which is our inference and not a quoted result. Low depth therefore does *not* mean small area relative to $|w|$, and small area does not follow from what is available.
- **(b) Depth.** Covered above in R3–R5.
- **(c) What "random" means.** Random **diagrams/words over a fixed finitely presented group**, generated by random relator insertion. It is **not** a random finitely presented group (Gromov density / few-relator model). The group is arbitrary and fixed. Only the boundary word or diagram is random.
- **(d) Burnside / torsion / non-finitely-presented groups.** Nothing reported. All results assume a **finite** presentation, and $L(R)$ appears in every bound.

## Assumptions

- $G = \langle X \mid R \rangle$ is **finitely presented**, with $R$ finite and symmetrized.
- The distribution comes from a random rewriting / relator-insertion process over that fixed presentation. The outputs are non-reduced words (per Morar–Ushakov §1.4).
- "Generic" is in the generic-case complexity sense: the solver succeeds within the time bound on a set of inputs whose measure tends to 1 (definition restated in Morar–Ushakov §1.4).

## Limitations / scope

- Full text not read. Section, theorem and constant-level details are missing.
- Says nothing about the free Burnside group B(2,5). B(2,5) is not finitely presented (its natural presentation $\{w^5\}$ is infinite), so $L(R)$ is infinite and the solver bound does not apply as stated. The *definition* of depth still makes sense for any diagram over any presentation, including a finite set of B(2,5) relators actually used in a certificate.
- The genericity result concerns a specific generating process. A different generator, such as PatternBoost's learned distribution, gets no guarantee from it.
- The results are about *existence* of shallow diagrams (δ(w) is a minimum over diagrams). They say nothing about the depth of the particular diagram that a given certificate encodes.

## Replication evidence

Partial. The same group extended the framework to reduced-word generators and to the conjugacy and membership search problems (Morar–Ushakov, arXiv:1407.1685). They reused the log-depth bound for hyperbolic groups (Knapsack problems in groups, arXiv:1302.5671) and used conjugacy depth for Andrews–Curtis search (Panteleev–Ushakov, arXiv:1609.00325). No independent replication outside the Stevens group is known.

## Why this paper matters

This paper introduced **depth**, a filling function aimed at algorithms: it measures how many "relator-closure rounds" a null-homotopic word needs. It also showed that random relator-insertion produces shallow diagrams, so search on such inputs is generically easy. This fits the generic-case programme of [[kapovich-2003-generic-case-complexity]]: average or generic inputs are easy even when worst-case inputs are not. It also explains why random-rewriting cryptosystems (Wagner–Magyarik) are weak. Later surveys cite it for the "dual" question of finding "non-cooperative" words that drive worst-case complexity, which they relate to Dehn functions (see the survey arXiv:2401.09218 §1).

**Relevance to challenge-gen:** The paper directly addresses our baseline. According to [[project-challenge-gen]], the initial sample is "random products of conjugates of relators", which is the random relator-insertion process this paper analyses. Its message is that such samples are **generic, shallow (low-depth) and polynomially solvable** by a relator-closure + folding solver. That justifies *not* treating baseline random trivial words as hard. It also justifies the idea that hard challenges must be **non-generic** in some filling-function sense. The paper does **not** justify our specific metric $D(w) = \#\text{factors}/|w|$:
1. D(w) is an **upper bound on area**. The paper's hardness parameter is **depth**, and solver cost is $\tilde O(|w| L(R)^{\delta(w)})$, which is exponential in depth and insensitive to area. A certificate with many factors can still be a shallow "fan" diagram with all cells near the boundary, which $A_{WP}$ solves in a few rounds. High D(w) is therefore not shown to imply hardness for this solver.
2. D(w) bounds the area of *one* diagram from above. Hardness depends on the *minimal* depth over all diagrams, and a minimised certificate can still overstate it.
3. B(2,5) is outside the paper's finitely-presented scope.

Honest use: cite the paper as the theoretical anchor for "random relator-product words are easy, so hard instances must be atypical". Then add a **depth-type** statistic computed from the certificate's diagram alongside D(w), instead of claiming that D(w) is justified by the paper. See [[challenge-gen-success-metrics]].

## Quotes

1. > "a random van Kampen diagram over a given group is hyperbolic, even though the group itself may not be hyperbolic" — Abstract
2. > "the depth of van Kampen diagrams, - a crucial algorithmic characteristic of null-homotopic words" — Abstract

## Open questions surfaced

- **Certificate depth.** Each FactoredWord certificate $w = \prod_i c_i r_i^{\pm1} c_i^{-1}$ defines a van Kampen diagram (a bouquet of lollipops, then folded). Can we compute (an upper bound on) its depth after folding? Does depth correlate with solver failure (beam search, PatternBoost local search) better than D(w) does? This is a concrete experiment.
- **Depth of baseline samples.** Measure the depth distribution of the C++ initial-sample generator's outputs over a finite set of B(2,5) relators. The paper predicts $O(\log |w|)$-like behaviour. Confirm or refute it empirically.
- **Area vs depth for B(2,5) certificates.** Do the high-D(w) words that PatternBoost finds also have large depth, or are they "wide but shallow"?
- **Finite truncations.** Over a finite truncation $R_k$ of the B(2,5) relators, does the $L(R_k)^{\delta}$ bound give a usable hardness estimate? It grows with $k$.
- **Full text.** Obtain the paper and check: the exact distribution, the exact genericity statement, and whether any area statement is made. Upgrade this note from abstract-only.

## Related material in vault

- Parent overview: [[word-problem-overview]]
- MOC: [[_moc-word-problem]]
- Contrast filling function (area, not proved here): [[dehn-function]]
- Generic-case framework: [[kapovich-2003-generic-case-complexity]]
- Sibling, random trivial words with a different distribution (Metropolis sampling of reduced trivial words): [[elder-2015-random-trivial-words]]
- Hard-instance synthesis: [[_synthesis-hard-instance-generation]]
- Concept: [[Concepts/certified-instance-generation]]
- Project: [[project-challenge-gen]], metric note [[challenge-gen-success-metrics]]
- Extends / Contradicts / Replicates: none in vault
- Cites (in vault): [[kapovich-2003-generic-case-complexity]] (generic-case complexity framework; inferred, reference list not seen)
- Cited by (in this vault): none yet
