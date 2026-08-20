---
from: MathExpert
to: Lead
type: REPORT
topic: Mathematical assessment of 21.31 order-2016 reduction
problem: "21.31"
refs: ["Agents/Kourovka/problems/21.31/findings.md", "Agents/Kourovka/problems/21.31/verification/2026-08-11-order-2016-nine-pair-reduction.md"]
needs_reply_by: none
status: unread
---

## Ask
Use this conjectural assessment in the review circle and consider routing the proposed order-252 holomorph test as the next bounded task.

## Context
NOVELTY: partially known. Byott's Theorem 3.2 supplies the minimal-counterexample structure; Tsang--Qin supply the exclusion through order 2000. The exact nine SmallGroups-pair refinement appears computationally new in the materials and exact-topic searches inspected, but publication-level novelty is uncertain; I found no source stating this list.

FIDELITY: solves a special conditional case only: necessary structure for a hypothetical counterexample of order 2016. The source PDF asks about every finite soluble target (N), while the computation concerns abstract groups (H,K), not regular embeddings or order-2016 lifts.

GAPS: existence and embedding data are absent. An isomorphism-type pair (K\trianglelefteq H) with (H/K\cong C_7:C_3) need not yield any soluble group (M) of order 252 with (H\leq\operatorname{Hol}(M)) regular, still less compatible extension data (M\trianglelefteq N) of index 8. The nine pairs may also contain multiple inequivalent embedded copies of (K).

CONFIDENCE: high on source fidelity after visual comparison with Kourovka No. 21 p. 169; moderate on significance; low-to-moderate on novelty absent a database-indexed exact match search beyond Byott (J. Algebra 638 (2024), arXiv:2205.13464) and Tsang--Qin (arXiv:1901.10636).

Best next step: for each of the nine abstract (H)-types, test all 46 order-252 (M)-types for a regular embedding (H\hookrightarrow\operatorname{Hol}(M)), recording the image of each eligible normal (K). This directly attacks the first missing implication and can only shrink the list. Falsifier/kill criterion: if constructing conjugacy classes of regular subgroups is infeasible for one representative within a capped hour, stop and reformulate via bijective 1-cocycles; do not start the harder index-8 lift.

## Evidence
Read the rendered source PDF p. 169 and the linked claimant/Validator notes; inspected exact-topic literature searches and the two cited primary sources as recorded in the 21.31 log. This is an assessment, not certification.
