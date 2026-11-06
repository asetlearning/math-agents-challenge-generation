---
type: validation
date: 2026-11-04
author: Validator (asetlearning)
project: "[[project-b25-solver]]"
subject: "E2-whitehead-solvers: break certificates for C1|16|3 and C3|4|17"
status: verified
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, project/b25-solver, status/verified]
---
# E2 Whitehead breaks: replay

Triage: [[2026-11-04-b25-solver-e2-whitehead-breaks-check-triage]]. Own code (pure Python free-group reduction, run with `-I`, script outside the data directories); inputs: the two certificates under `runs/b25-solver/E2-whitehead-solvers/`, the registry rev 3 in `data/b25_challenge_candidates.json`, the sidecar and the R-step files of the run. No word strings here.

## Verdict: both CONFIRMED (L0 certificates)

| id | cells | registry word length | cores literal 5th powers (reduced) | periods | free reduction of prod conj^-1 core conj == registry word | g |
|---|---|---|---|---|---|---|
| C1\|16\|3 | 88 | 562 | 88 / 88 | 1..52 | **yes** | empty |
| C3\|4\|17 | 40 | 220 | 40 / 40 | 1..23 | **yes** | empty |

- The certificate ids match, the counts match the claim, and the sidecar's registry word equals the rev-3 registry word (both freely reduced).
- A free-group identity of this form is a proof of triviality in B(2,5) by definition (L0-cert). Both certificates contain cells of period above 7 (up to 52 and 23); that is allowed for an L0 certificate and is not a G_7 statement.

## Route math (all checked on the actual data)

1. **phi** is a Whitehead (elementary) automorphism: a -> a, b -> a^-1 b for C1|16|3, and b -> a^-2 b for C3|4|17. phi and the recorded phi_inverse compose to the identity on a and b in both orders.
2. **Minimal word.** phi(w) is conjugate to the recorded minimal word (equal to conjugator^-1 phi(w) conjugator; conjugator empty for C1|16|3, aa for C3|4|17), and is a cyclic rotation of its cyclic reduction (188 of 192 letters for C3|4|17).
3. **R step.** In both fix files the R step has in_word = minimal and out_word empty; the product of its 88 / 40 trace cells equals the minimal word as a free-group identity (rotation r and its inverse cancel around the empty result), and every trace core is a literal fifth power.
4. **Pullback.** For a cell g v^5 g^-1, phi^-1 gives phi^-1(g) phi^-1(v)^5 phi^-1(g)^-1, which is again a conjugate of a literal fifth power (of the word phi^-1(v)), because phi^-1 is a homomorphism. Replayed: the product of the phi^-1-images of the trace cells reduces to phi^-1(minimal), and phi^-1(minimal) equals the registry word (C1|16|3) or the registry word conjugated by phi^-1(conjugator) (C3|4|17, as the conjugator is aa). The published certificates are this pullback, and they check directly (table above).

## Scope
Exact free-group identities only; nothing rests on kbmag or a finite quotient. Not checked: that these two words were not already broken by an earlier solver (a registry question), and the other 205 words.
