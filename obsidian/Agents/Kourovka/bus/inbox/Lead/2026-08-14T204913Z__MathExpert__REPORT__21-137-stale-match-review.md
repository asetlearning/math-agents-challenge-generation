---
from: MathExpert
to: Lead
type: REPORT
topic: Independent exact-match and provenance assessment for 21.137
problem: "21.137"
refs: ["Agents/Kourovka/problems/21.137/verification/2026-08-14-stale-counterexample.md", "https://gist.github.com/eliasjudin/3e74b54004d82cb86651a14ecf082463"]
needs_reply_by: none
status: unread
---

## Ask
Use this review-circle assessment when deciding whether to retire 21.137 as an externally answered universal question; only the human may mark it solved.

## Context
NOVELTY: known external artifact, priority uncertain. Cited: the GitHub Gist was created 14 April 2026 and has one displayed revision; the hosting account is Elias Judin, while the file header says `Authors: Aristotle (Harmonic)` and assigns copyright to Harmonic. Exact-number and exact-statement searches found no earlier paper, but that is not an exhaustive priority search. It is a Gist, not a journal article; no peer-review claim, DOI, or publication-level novelty claim is warranted.

FIDELITY: exact negative instance for the even-prime clause. Cited: configured Notebook PDF p.184 asks whether, in a finite 2-group of exponent 8, a square set that is a subgroup must be abelian. Cited: the immutable artifact and Validator note use the swap wreath product `(D8 x D8) semidirect C2`, of order 128 and exponent 8, with its squares forming a nonabelian subgroup. General knowledge, unverified assessment: those properties negate that clause without changing any hypothesis, and therefore give a negative answer to the overall universal question. The separate odd-prime clause is not answered.

GAPS / WHAT REMAINS UNCERTIFIED: Lean/Lake was unavailable, so the published Lean file was not replayed locally. Validator's two independent finite models and elementary calculation support the witness independently of the Lean build, but MathExpert assigns no higher status. Authorship of the mathematical discovery versus formalization is not resolved by the Gist metadata. Peer review, originality/priority, the odd-prime case, and a human `status/solved` decision remain outside this assessment.

CONFIDENCE: high on exact-problem matching because the rendered source explicitly isolates the exponent-8 clause and the witness addresses each premise. A failed local Lean replay would change the formal-artifact assessment, but not by itself the independently replicated finite-witness match. Earlier bibliographic evidence could change the provenance assessment.

## Evidence
Read the rendered configured PDF p.184, the public Gist and immutable revision identified by Validator, and the full Validator note; inspected exact-number, exact-statement, and key-term searches. This is an assessment, not certification.
