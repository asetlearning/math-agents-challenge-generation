---
agent: Problem-20.49-Proof
problem: "20.49"
scope_id: 20.49/two-generated-same-exponent
scope_record: Agents/Kourovka/scopes/20.49-two-generated-same-exponent.json
assignment_revision: 1
direction: proof
session_id: collaboration:/root/p2049_base_preimage
parent_session_id: collaboration:/root/p2049_subdirect_proof
runtime: codex-collaboration
reasoning_effort: ultra
spawned_utc: 2026-08-17T14:11:00Z
cycle: 3
budget_hours: 3
active_budget_minutes: 45
active_minutes_used: 74
extensions_granted: 0
safety_stop_utc: 2026-08-17T15:11:00Z
compute_slot: none
compute_pid: none
compute_started_utc: none
compute_expires_utc: none
selection_status: approved
truth_likelihood: 0.68
alternate_direction: proof
run_dir: Agents/Kourovka/problems/20.49/runs/2026-08-17-r3-base-preimage
state: parked
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/exponent, project/kourovka, status/draft]
---

The exact revision-1 scope and independent source-fidelity audit both pass. The
target is universal over finite groups, uses equality of group exponents, and
asks for an at-most-two-generated subgroup; the known soluble theorem and weaker
three-generator theorem are context only.

## 2026-08-17T11:44:30Z — initial counterexample reconnaissance

Use `NONSOLUBLE-SMALLGROUP-PAIR-ORBIT-RECON`. First formalize the exact failure
predicate `exp(<x,y>) < exp(G)` for every ordered pair `(x,y)` and record why
solvable and two-generated ambient groups cannot be counterexamples. Identify one
precise, complete bounded nonsoluble catalogue layer from installed static
metadata. Before any GAP call, freeze the complete script, output path, hash,
timeout, CPU/RAM estimate, and request a Lead lease. A hit needs a reconstructible
group and an all-pairs or automorphism-orbit certificate; a bounded negative cannot
prove the universal statement. Report a first checkpoint at roughly 60 active
minutes and do not self-abort on strategy exhaustion—return to Lead or MathExpert
for a pivot.

## 2026-08-17T11:53:52Z — SG255 exhaustive pair lease

Lead independently matches the frozen 117-line script at SHA-256
`63c90b1de2144002ce001900880a23616f9ee90e850c0300fc4ece8c7d9a55bd`.
Compute slot 2 is leased through `2026-08-17T12:23:52Z` for exactly one run of
the requested 20-minute capped command, one CPU, and at most 1 GiB RAM. The
authorized layer is every nonsoluble SmallGroups representative of order at most
255 with all ordered pairs. No rerun, higher order, or catalogue extension is
authorized. Release the slot immediately on exit and preserve the complete output.

## 2026-08-17T12:18:20Z — corrected witness-first SG255 pass

The first leased command exited `124` at 20 minutes and released slot 2. Its
intended output file is empty; the manually preserved partial is operational
diagnostic material only and is not certification-grade evidence. Do not promote
its claimed bounded coverage.

Continue the same bounded layer with `SG255-WITNESS-FIRST`. For every nonsoluble
SmallGroups representative through order 255, stop that group's pair loop at the
first exact equality `exp(<x,y>)=exp(G)` and persist the group ID, ambient
exponent, pair coordinates, element orders, and subgroup order immediately. Only
a group with no witness must exhaust all ordered pairs; record its exact pair
count as a candidate certificate. Use a robust raw output path that survives
timeout, preferably shell redirection plus immediate stdout rows or verified
`AppendTo`. Freeze the complete script/command, hash and resource estimate and
request a new lease. Do not run, enlarge the order bound, or begin the structural
construction without Lead approval.

## 2026-08-17T12:23:52Z — witness-first slot-2 lease

Lead independently matches the frozen 132-line script at SHA-256
`50351b6a13abfc7f44e46cd7854e92d81fe0a0b5bc86749b3b2fa0afa9f9b756`,
4,334 bytes. Grant slot 2 through `2026-08-17T12:38:52Z` for exactly one run
of the requested 10-minute capped command, one CPU and at most 1 GiB RAM. Standard
output and error must remain in the two frozen persistent paths. No rerun, higher
order, histogram pass over negative rows, or structural-search follow-on is
authorized. Release immediately on exit and report exact coverage and hashes.

## 2026-08-17T12:43:53Z — monolithic-socle structural pivot

The corrected run exited 0 and released slot 2. It persistently covers all 7,012
SmallGroups representatives through order 255: 6,998 are soluble, and each of the
14 nonsoluble groups has an explicit full-exponent two-generator witness. Preserve
this only as a bounded candidate exclusion pending fresh validation; do not enlarge
the catalogue.

Continue by hand for at most 30 active minutes on `MONOLITHIC-SOCLE-GATE`. Starting
from a least-order counterexample and the submitted exponent-critical reductions,
determine whether its proper-subgroup/proper-quotient conditions force a unique
minimal normal subgroup. If so, split abelian and nonabelian socles and derive the
strongest exact exponent constraint on the action/extension. If direct
indecomposability does not imply monolithicity, freeze the first explicit obstruction
and stop the method at 30 minutes. No computation or catalogue enlargement is
authorized. Report the outcome and await Lead; do not self-park.

## 2026-08-17T12:51:55Z — three-pair prime-power defect pivot

The monolithic gate met its hard kill after three active minutes. The order-30
dihedral group with rotation order 15 is directly indecomposable and exponent-
critical in all proper subgroups and nontrivial proper quotients, yet has distinct
minimal normal order-3 and order-5 rotation subgroups. It refutes only the proposed
unique-minimal-normal inference and is not a target counterexample.

Continue by hand for at most 25 active minutes on
`THREE-PAIR-DEFECT-HYPERGRAPH`. In a least counterexample, use the known
three-generator theorem to choose an irredundant full-exponent triple
`(x1,x2,x3)`. For each omitted-generator pair, record every maximal prime power
present in `exp(G)` but absent from that pair subgroup. Determine whether minimality
forces three distinct localized prime-power defects or a reusable chief-factor
constraint. Stop early if defect membership cannot be made invariant under changing
the full-exponent triple, and freeze that exact obstruction. No computation; report
and await Lead rather than self-parking.

## 2026-08-17T13:00:01Z — exactly-three-prime abelian-chief norm gate

The defect-hypergraph route used six active minutes. It derives candidate exact
subcases: any counterexample has at least three exponent primes; with exactly
three, maximal pure prime-power elements generate the least counterexample and the
three pair defects are the three distinct omitted primes; an abelian minimal normal
`p`-layer lowers the quotient's maximal `p` exponent by exactly one, with a nonzero
norm condition in a split extension. General defect labels are not invariant under
Nielsen changes, so do not continue unrestricted coloring. These subclaims await
fresh validation.

Use at most 30 active minutes on `THREE-PRIME-ABELIAN-CHIEF-NORM`. Restrict
explicitly to the exactly-three-exponent-prime residual and one minimal abelian
normal `p`-layer. In the split case, write the norm map for lifts of the two
complementary prime-power elements and determine whether some mixed element, paired
with the pure `p`-element, necessarily realizes all three maximal prime powers. A
success eliminates this chief-layer case; a failure must be an explicit compatible
module/action pattern, not a vague loss of control. Stop and report at 30 minutes;
no computation or self-park.

## 2026-08-17T13:10:28Z — route the bounded/structural package to Validator

The abelian-chief norm gate used seven active minutes. It proposes a full-Jordan-
block constraint when an elementary abelian `p`-layer raises the maximal `p`
exponent by one level, but an explicit soluble split action of exponent 900 meets
the local rows while its order-9 element has no single partner carrying both
complementary maximal powers. This is a method obstruction, not a target
counterexample.

Pause research at 56 active minutes. Route the complete package to a fresh
Validator: the SG255 zero-candidate run and witness rows; least-counterexample
reductions; the order-30 monolithicity control; at-least-three-prime and
exactly-three defect claims; abelian-chief quotient/norm/Jordan rows; Nielsen
non-invariance control; and the exponent-900 no-partner control. The universal
scope is unanswered, and no claim may be reused before verdict.

## 2026-08-17T13:29:54Z — reviewed package and proof-direction switch

Validator upholds the SG255 transcript as an internally complete bounded
zero-candidate result at `status/conjectured`, and independently reconstructs the
least-counterexample, three-prime, abelian-chief exponent-drop, split norm/Jordan,
and explicit control claims. One generic sentence in the exponent-900 control
needed its stated direct-product structure, which supplies the repair.
`active_assignment_answered:no`.

Switch to a fresh ultra-effort proof session for at most 45 active minutes on
`TWO-MINIMAL-NORMAL-SUBDIRECT-PAIRING`. Let `M,N` be distinct minimal normal
subgroups of a hypothetical least counterexample. Since `M cap N=1`, use the
canonical subdirect embedding `G -> G/M x G/N`; minimality supplies two-generator
full-exponent subgroups in each proper quotient. Determine whether their generator
pairs can be chosen compatibly in the subdirect product so that two lifts recover
`exp(G)`, forcing monolithicity under the full nonsoluble and `d(G)=3` hypotheses.
Success must be a complete simultaneous-lift lemma; failure must identify the exact
Goursat/fibre-product obstruction and its exponent effect. Kill at 30 minutes if
compatibility remains an unsupported choice; absolute stop 45. No computation.

## 2026-08-17T13:45:50Z — route exact subdirect lift profile to Validator

The subdirect-pairing pass used nine active minutes, bringing the centralized
ledger to 65. It did not prove monolithicity. It proposes the exact replacement:
write `G=(G/M) x_(G/MN) (G/N)` and group compatible two-generator lifts by their
common Nielsen orbit in `Hom(F_2,G/MN)`. A full-exponent two-generator subgroup
exists exactly when one common orbit has attainable projected exponents whose
lcm is `exp(G)`. Minimality supplies separate nonempty full-factor witness-orbit
sets but does not force them to intersect.

Pause research and request fresh independent reconstruction of the fibre-product
identity, the orbitwise iff criterion, and the stated limitation. This is a
candidate structural partial only; the universal scope remains unanswered.

## 2026-08-17T14:11:00Z — validated profile and base-preimage continuation

Validator independently upholds the fibre-product description, both exponent-lcm
identities, compatible arbitrary `F_2` maps, precomposition-orbit alignment, and
the exact attainable-profile iff. The wording repair is important: a common orbit
carrying both full factor exponents is sufficient but not necessary; the exact
obstruction ranges over all complementary exponent profiles. Only the common map
to `C=G/MN` may be required epimorphic in a successful least-counterexample
profile, not the maps to `A` or `B`.

Resume in a fresh ultra proof context for at most 45 active minutes on
`BASE-PREIMAGE-PRIME-COVER`. Use minimality in the proper quotient `C` to choose
a two-generated subgroup `D<=C` with `exp(D)=exp(C)`. Analyze its inverse images
in `A`, `B`, and `G`, and record exactly which maximal prime powers can be lost
when those preimages are proper. Success must force one compatible epimorphic base
profile whose projected exponent lcm is `exp(G)`; failure must be a complete
primewise defect configuration, not another unsupported orbit-intersection claim.
Kill at 30 minutes without a new invariant; absolute stop 45. No computation.

## 2026-08-17T14:31:30Z — route the prime-cover reduction to Validator

The base-preimage pass used nine active minutes, bringing the centralized ledger
to 74. It submits a candidate conditional package: every proper two-generated
full-exponent base subgroup has a nonempty fixed defect set of extension-created
maximal prime powers; exact top-lift support sets detect those defects; every
choice of one support element per defect prime generates the common quotient
together with the base subgroup; and the residual splits into a rank-three base
obstruction or cross-intersecting loss profiles over epimorphic Nielsen orbits.

Pause research and ask a fresh Validator to reconstruct every divisibility and
quantifier, especially the arbitrary-support-transversal generation lemma and the
claim that a top-order lift may be chosen as a p-element. The universal target is
unanswered; this package is not reusable before verdict.

## 2026-08-17T14:49:16Z — accept reviewed prime-cover partial and compare pivots

Validator independently upholds the fixed-`D` exponent identities, nonempty
extension-created defect, support equivalence, universal support-transversal
generation, primary-carrier existence, and the `d(C)=3`/`d(C)<=2` dichotomy.
Apply its four wording repairs: use literal quotient kernels; allow primary-part
replacement to move the base support element; state only forward closure under
coprime powers; and retain the dependence `S(D)` on fixed `D`.

Before more research, ask a fresh MathExpert to compare three target-facing
routes: maximal-subgroup/core consequences in the rank-three branch, primewise
Nielsen-profile patching in the rank-at-most-two branch, and a Frattini/chief-
factor representation change. The universal target remains open at 74 active
minutes, with 106 minutes available.

## 2026-08-17T15:01:51Z — park at the reviewed compatibility frontier

Accept MathExpert's `PARK_RECOMMENDED`. In the `d(C)=3` branch, maximal-overgroup
avoidance yields only a primitive-action `p`-derangement/index label. In the
`d(C)<=2` branch, attainable loss profiles still have unconstrained orientations
across epimorphic Nielsen orbits. Repeating either encoding or the earlier naive
abelian-chief norm implication is not a new target-facing experiment.

Preserve 106 active minutes. Restart only after a source-checked chief/crown
theorem passes Validator review and turns a nonsoluble three-generator exponent-
critical group into a monolithic primitive/crown quotient while retaining every
top-prime loss, together with either explicit two-generator lift equations or a
finite bound on crown multiplicity. Kill any restart immediately if it controls
only generator number and loses exponent/lift data. The universal scope is open.
