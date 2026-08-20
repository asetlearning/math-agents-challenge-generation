---
title: "Outcome r36 — DEFECT-ROOT-FIBRE-CONJUGACY"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: DEFECT-ROOT-FIBRE-CONJUGACY
outcome: PARTIAL_RESULT
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

# Outcome r36 — DEFECT-ROOT-FIBRE-CONJUGACY

## Exact active scope

`p` is an odd prime `p>2`; `G` is a finite same-`p` group; `exp(G)=` exactly `p^2`; `P={g^p:g in G}` is the literal actual `p`th-power value set, not merely the generated subgroup; `P` itself is assumed a subgroup; ask whether `P` is abelian. The separate `p=2`/exponent-`8` clause is excluded.

Scope `21.137/odd-prime-exponent-p2`, revision `2`.

## Outcome

`PARTIAL_RESULT`; `status/conjectured`; `active_assignment_answered: no`.

Corrected ledger: new decision read and charged work started at `2026-08-18T01:08:43Z`, official cumulative minute `757`; live audit stopped at the already elapsed timestamp `2026-08-18T01:17:26Z`, after eight complete newly active minutes, official cumulative minute `765`. No future-dated time is claimed.

The Hall defect in a hypothetical reviewed minimum counterexample forces a complete conjugacy filling and root-fibre divisibility theorem, but no contradiction. The surviving freedom is an arbitrary finite `C_p`-set of root `V`-cosets under the return monodromy.

## Derived conditional lemma

Retain `P'=N=<n_0><=Z(G)`, `[a,b]=n_0`, `g^p=b`, `h=ag`, `Delta=b^(-1)h^p`, and `[h,Delta]=n_0^(-1)`. Then:

1. `Delta^(h^k)=Delta n_0^k`, so `Delta^<h>=Delta N` and the entire central fibre consists of literal actual pth powers obtained from one root by conjugacy.
2. With `V=<Delta,N>` and `R_k={x:x^p=Delta n_0^k}`, one has `|V|=p^2`, `R_k subseteq C_G(V)`, and every `R_k` is a union of free `V`-cosets of elements of order exactly `p^2`. Hence `p^2` divides `|R_k|`, all `|R_k|` are equal, and `p^3` divides the number of roots above `Delta N`.
3. Conjugation by `h` cycles the fibres. After one circuit, conjugation by `h^p=b Delta` acts on every root exactly as conjugation by `b`; also `[b,Delta]=1`.
4. On `X=R_0/V`, the return map is an arbitrary permutation of order dividing `p`. Its lift to each free `V`-torsor may also include an arbitrary V-translation subject only to the order-`p` cycle-sum equation. A root has `<h>`-orbit length `p` exactly when both its quotient torsor and the root itself are return-fixed; otherwise its orbit has length `p^2`.
5. For a root `x`, the displacement `s_x=x^(-1)x^b` lies in `P intersect C_G(V)`. Its cyclic norm condition is automatic in the class-two exponent-`p` group `P`, because for `[s_x,b]=m in N`,

   `product_(i=0)^(p-1) s_x^(b^i)=s_x^p m^(p(p-1)/2)=1`.

Thus neither orbit arithmetic nor odd-prime norm collection forces a fixed root or another commutator to vanish.

## Exact formal freedom

At the level of all derived identities, choose any nonempty finite `C_p`-set `X`. Take `p` root layers, each a free `V`-set indexed by `X`. Let `h` carry each layer to the next while acting on `V` by `Delta -> Delta n_0`, `n_0 -> n_0`; on returning from the last layer, apply the chosen `C_p`-permutation of `X` and a V-translation on each torsor. The translations need only have zero sum around each quotient cycle; at a fixed quotient point every translation is allowed because `pV=0`. This realizes every required value orbit, fibre divisibility row, and return-monodromy row.

This is only a formal incidence model, not a group or witness. It demonstrates exactly why the present conjugacy identities do not contradict the hypothetical minimum-counterexample reduction: the quotient root set `R_0/V`, its return permutation, and the V-torsor translations remain uncontrolled.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | use / result | evidence | result |
|---|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every admissible `p,G` | derivation is conditional on a hypothetical reviewed minimum counterexample | r36 setup | partial only |
| `21.137-odd-p-not-2` | admissibility | prime `p>2` | oddness is used in `p(p-1)/2` being divisible by `p` | cyclic norm audit | conditional-pass |
| `21.137-odd-finite-p-group` | admissibility | finite same-`p` group | finite cyclic orbit lengths and root cardinalities are used | conjugacy/root orbit audit | conditional-pass |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | gives root orders at most `p^2` and `exp(P)=p` | reviewed reduction and r36 identities | conditional-pass |
| `21.137-odd-power-set-definition` | admissibility | literal actual pth-power set | each fibre `R_k` consists of actual roots and conjugation is applied elementwise | definitions of `R_k`, (C3), (C7) in log | conditional-pass |
| `21.137-odd-power-set-subgroup` | admissibility | literal `P` is a subgroup | makes `Delta` an actual value in `P` and gives the reviewed class-two reduction | frozen reviewed setup | conditional-pass |
| `21.137-odd-P-abelian` | target conclusion | `P` abelian | assumed false in the conditional minimum counterexample; no contradiction follows | arbitrary return `C_p`-set survives | unresolved |

## What this does not establish

- It does not construct a group realizing the formal incidence data.
- It does not force a common choice of roots across fibres.
- It does not constrain the return `C_p`-set `R_0/V` enough to force a contradiction.
- It does not prove the universal active conclusion or answer any excluded clause.

## Evidence boundaries

Hand identities only. No computation, web, solution lookup, remembered citation, unreviewed historical run, `p=2` example, or common root-section assumption was used.

The named strategy is exhausted at the uncontrolled V-torsor return data. This is not a scope park.
