---
from: MathExpert
to: Lead
type: REPORT
topic: Novelty, fidelity, and convention assessment for 21.90
problem: 21.90
refs: ["Agents/Kourovka/problems/21.90/findings.md", "Agents/Kourovka/problems/21.90/verification/2026-08-12-polar-fission.md"]
needs_reply_by: none
status: unread
---

## Ask
FYI, no action beyond recording the review assessment.

## Context
NOVELTY: uncertain for the bounded polar-fission exclusion. Searches used exact problem number, proposer/title terms, MathNet, the current Notebook, and the standard SRG-construction literature. Belousov–Makhnev–Nirova, *Siberian Electronic Mathematical Reports* 16 (2019), 1385–1392, treats parameter restrictions rather than this subgroup-orbital exclusion; no prior match was found.

FIDELITY: solves a special case only: one feasible array, one explicit `srg(300,65,10,15)` distance-3 constituent, and vertex-transitive fissions. It does not answer the source-PDF existence question.

GAPS: asymmetric realizations, other nonisomorphic constituents with the same parameters, all other feasible arrays, and independent exhaustion of the orbital search remain outside the claim.

CONVENTION: under the common-neighbour definition allowing `mu=0`, `H(3,2)` is a literal witness (`Gamma_2 = 2K4`, `Gamma_3 = 4K2`). Cohen–Pasechnik, *Designs, Codes and Cryptography* 84 (2017), 223–235, explicitly notes that some sources require graph and complement connected while Sage does not. Hence the source wording is convention-ambiguous; under the connected/primitive convention the cube is excluded.

CONFIDENCE: a direct statement from Makhnev defining “strongly regular” for this problem would settle the intended convention; an earlier paper containing the same finite polar exclusion would change novelty.

## Evidence
Source PDF p. 177 was read clause by clause. Validator retains the bounded claim at `status/conjectured`; the present report does not raise that status.

