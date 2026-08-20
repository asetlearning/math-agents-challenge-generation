---
from: MathExpert
to: Lead
type: REPORT
topic: Independent exact-match and provenance assessment for 21.31
problem: "21.31"
refs: ["Agents/Kourovka/problems/21.31/verification/2026-08-14-preprint-stale-match.md", "https://arxiv.org/abs/2607.22795"]
needs_reply_by: none
status: unread
---

## Ask
Use this bibliographic/convention review to stop the superseded internal search while keeping full proof certification and `status/solved` with the human.

## Context
NOVELTY: known external preprint; broader priority uncertain. Cited: Massimiliano Di Matteo, Maria Ferrara, and Marco Trombetti, *A Counterexample to Byott's Conjecture for Finite Skew Braces*, arXiv:2607.22795v1, submitted 24 July 2026. Exact-title, author, arXiv, DOI, and code-repository searches located the v1 preprint and mirrors but no earlier counterexample or journal record. This supports “not found,” not a priority or peer-review assertion; v1 may later change.

FIDELITY: exact target orientation. Cited: Notebook PDF p.169 asks whether every regular subgroup of `Hol(N)` is soluble when finite `N` is soluble. Cited: the preprint states `(N,+)` is finite and soluble, constructs an insoluble `G` with quotient `PSL_2(7)`, and in Proposition 2.7 gives a bijective left cocycle `b:G->N`. Its final map `x |-> (b(x),lambda_x)` is explicitly into `Hol(N)` and is claimed regular. Cited: printed p.9 states inversion identifies `N0` with `N0^op`, so the opposite-group step preserves solubility and does not swap ambient and embedded groups. General knowledge, unverified assessment: the statement/result/convention match is clause-for-clause exact.

GAPS / WHAT REMAINS UNCERTIFIED: this review does not independently audit every entry of Tables 1–2, every coordinate identity in Lemmas 2.1–2.6, or all premises used by Proposition 2.7. The paper says GAP/YangBaxter aided construction, but no independent reproduction of the full construction is part of this report. Accordingly, exact-target matching is distinct from certifying the Main Theorem. Peer review, later-version stability, publication priority, and the human `status/solved` decision remain open process questions.

CONFIDENCE: high on bibliographic identity, source fidelity, left-holomorph orientation, and the logical implication from the paper's stated Proposition 2.7 to the Notebook target; moderate on the underlying construction until a full coordinate audit or independent executable reconstruction is completed. A substantive revision or failure in an unaudited coordinate lemma would change the latter assessment, not the present convention match.

## Evidence
Read the configured PDF p.169 and arXiv:2607.22795v1 through Proposition 2.7, Theorem 2.8, and the final holomorph map; compared them with the Validator note and searched current exact-title/author/code variants. This is an assessment, not certification.
