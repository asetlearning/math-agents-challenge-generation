---
title: "Validator advice — Kourovka 19.30 Suzuki exclusions"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
result: not-yet-certifiable
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

# Current assessment

The proposed package is certifiable in principle as two sharply limited partial results, but it is **not yet independently certifiable from the referenced log**. At the time of review, that log contains only the strategy and certificate plan; it does not yet contain the claimed CTblLib commands/raw outputs or the developing hand proof.

## Catalogue component

To certify the installed-table statement for `Sz(8)` and `Sz(32)`, add the exact GAP and CTblLib versions; the complete query enumerating every installed table name and filtering by exact order; raw order buckets; every class order; the complete zero mask or, for each vanishing class, a witnessing irreducible-row index; the resulting sets (V(H)); and an independent checker. The conclusion must remain: “among installed CTblLib tables at these two orders,” not “among all groups of these orders.” A bucket containing only the simple table is not a group census.

## Structural order-29120 component

The claimed reduction for groups with a normal Hall odd subgroup is sound only after these steps are supplied explicitly:

1. if (N\lhd G) is the Hall odd subgroup, then (|N|=455=5\cdot7\cdot13);
2. prove (N\cong C_{455}) (Schur–Zassenhaus does not supply cyclicity); an elementary Sylow/action proof is available because no prime among (5,7,13) divides the relevant smaller-prime automorphism orders;
3. invoke Schur–Zassenhaus to obtain (G\cong C_{455}\rtimes_\varphi P) with (|P|=64);
4. quantify over **every** group (P) of order 64 and every action (\varphi:P\to\operatorname{Aut}(C_{455})), including trivial and nonfaithful actions;
5. give an exhaustive case partition and a hand derivation showing (V(C_{455}\rtimes_\varphi P)\ne V(\operatorname{Sz}(8))) in every case, with all character-theoretic lemmas proved or precisely stated and all element-order claims checked.

Merely checking selected 2-groups, faithful actions, or CTblLib entries would not prove the family exclusion. Once the complete proof and outputs are appended, the family result can be audited line by line; it still answers neither the `Sz(32)` noncatalogue cases nor the universal active assignment.
