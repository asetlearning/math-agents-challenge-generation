---
title: "Kourovka 21.137 — revision-2 odd-prime counterexample cycle log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
cycle: 1
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/draft
---

# Cycle log

Fresh counterexample-direction run. The prior proof direction consumed 64 active
minutes; this run has at most 116 active minutes from the shared 180-minute cycle
budget. I am treating the assignment block itself as the current safe-context
brief and will not inspect the ordinary synthesis, historical logs/findings,
transcripts, archived messages, unlisted verification notes, or solution-bearing
scratch artifacts.

## Active-time ledger

| UTC start | UTC stop | active minutes this interval | cumulative scope active minutes | activity |
|---|---|---:|---:|---|
| 2026-08-16T13:16:16Z | 2026-08-16T13:41:56Z | 26 | 90 | source/scope gates, reviewed handoff, construction research |
| 2026-08-16T13:42:00Z | 2026-08-16T13:46:24Z | 4 | 94 | scope correction and filtered-algebra hand check (30 s bus wait excluded) |
| 2026-08-16T13:46:24Z | 2026-08-16T13:47:58Z | 2 | 96 | package PARTIAL_RESULT and audit requests |

## Staleness check

Recorded 2026-08-16T13:18:32Z.

- Source resolved through `_meta/agents/Kourovka/paths.env`; no absolute PDF path
  was guessed or recorded.
- Inspected PDF page 184 both by `pdftotext -layout` and visually from the rendered
  page. The page header is *New Problems (21st issue, 2026)*.
- Corrected source transcription: “21.137. If the \(p\)-th powers in a finite
  \(p\)-group form a subgroup, must that subgroup be powerful? That is, for
  \(p\ne2\), if the \(p\)-th powers in a \(p\)-group of exponent \(p^2\) form a
  subgroup, must that subgroup be abelian? For a 2-group of exponent 8, if the
  squares form a subgroup, must that subgroup be abelian?” (L. Wilson.)
- `source_transcription_checked: yes`.
- The vault has no issue-21 corpus JSONL/readable record, so the requested corpus
  fields `answered`, `has_editor_comment`, and `has_later_comment` are unavailable.
  On the rendered page, problem 21.137 has no answer asterisk, editor comment, or
  later comment attached to it. I do not promote that visual negative into absent
  corpus metadata.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
  Per the assignment boundary, I did not browse, search arXiv, inspect later
  editions, or inspect local solution-bearing artifacts.

### Clause matrix

| source clause | equivalent formulation | active scope? | literature/staleness disposition |
|---|---|---:|---|
| If actual \(p\)-th powers in a finite \(p\)-group form a subgroup, is it powerful? | opening broader powerfulness question | no | not searched in discovery-blind run |
| For \(p\ne2\), in exponent \(p^2\), does subgroup closure of the actual \(p\)-power value set force it abelian? | exactly the odd-prime target below | yes | external check deferred; no source answer annotation |
| For a 2-group of exponent 8, do subgroup-forming squares commute? | separate \(p=2\) clause | no | explicitly excluded; not searched |

`active_scope_checked: yes`.

### Admissibility checklist

| constraint_id | source requirement | active target interpretation | reconciled? |
|---|---|---|---:|
| 21.137-odd-forall-p-G | universal question over qualifying \(p,G\) | one qualifying witness refutes it | yes |
| 21.137-odd-p-not-2 | \(p\ne2\), with \(p\) prime | construction begins at \(p=3\) | yes |
| 21.137-odd-finite-p-group | finite \(p\)-group (inherited from opening sentence) | finite 3-group | yes |
| 21.137-odd-exponent-p2 | exponent \(p^2\) | exponent exactly 9, not merely dividing 9 | yes |
| 21.137-odd-power-set-definition | all actual values \(P=\{g^p:g\in G\}\) | equality with a named set must be proved | yes |
| 21.137-odd-power-set-subgroup | that actual value set is a subgroup | closure/equality certificate required | yes |
| 21.137-odd-P-abelian | target says \(P\) is abelian | witness must exhibit two actual cubes with nontrivial commutator | yes |

No mismatch was found between the rendered source and canonical revision-2 scope.

## Reviewed handoff used

Only the five verification notes named in the assignment were read. They give the
following necessary conditions for a quotient-minimal counterexample, not a
solution: nilpotency class at least \(p+1\); \(Q=P\) has class 2 and exponent \(p\),
with \(Q'=C\cong C_p\); \(\dim Q\ge p+2\); \(\dim Z(Q)\ge p\); the sharpened
order bound \(|G|\ge p^{2p+3}\); and the stated cyclic-isotropic-cover index bound.
Thus for \(p=3\), any quotient-minimal model must have class at least 4,
\(|Q|\ge3^5\), \(\dim Z(Q)\ge3\), and \(|G|\ge3^9\). (The \(3^9\) value comes
from the latest reviewed \(p^{2p+3}\) bound.)

## Strategy portfolio

Ranked by expected certifiable information per active hour:

1. **Structured construction — minimal \(p=3\) power/commutator extension.** Start
   with the least quotient-minimal dimensions allowed by the reviewed conditions:
   a class-2 exponent-3 nonabelian candidate \(Q=P\) of dimension 5, with
   \(\dim Z(Q)=3\), and an index at least \(3^4\) extension \(G/Q\). Derive a
   class-at-least-4 exponent-9 pc/Lie-style relation system backwards from two
   desired cube values whose commutator generates \(Q'\). Kill this ansatz if no
   complete consistent power/conjugation system or exact actual-cube-set
   certificate emerges by the 30-minute checkpoint.
2. **Catalogue/small-case probe.** The reviewed bound excludes orders below
   \(3^9=19683\) for a quotient-minimal witness. A bounded catalogue check at the
   first admissible order could only establish finite coverage of available
   catalogued groups and near-miss data; it could not settle the general scope.
   No catalogue run will occur without a fresh Lead compute lease.
3. **Representation-changing structured pivot.** If direct pc relations become
   opaque, represent \(G\) as an extension of a class-2 exponent-3 group \(Q\) by
   an exponent-3 quotient \(R\), with lifts encoded by unipotent automorphisms and
   a factor set. Express cube values as a norm-plus-cocycle map and solve the
   surjectivity/closure requirements exactly at the coefficient level. This is
   distinct from reopening the exhausted affine-cover proof manipulation: its
   purpose is construction and full multiplication, not another covering bound.
4. **Theoretical obstruction.** Derive Hall–Petrescu consistency identities for a
   minimal class-4 exponent-9 presentation and test whether closure of the actual
   cube set forces the commutator of two cube values to vanish. A firm exclusion
   of the minimal tuple would be a reusable partial result.

### Certificate plan

A successful construction must provide: a finite normal form with an associative
multiplication rule (or a confluent pc presentation); an exact order; direct
verification that every element has ninth power 1 and some element has order 9;
an exact formula for every cube showing its image equals the named subgroup \(Q\),
not merely generates it; subgroup closure; and an explicit nontrivial commutator
of two cube values. Validator should be able to reconstruct these checks by hand
from the normal form independently of any bespoke script.

## 2026-08-16T13:24:30Z — early review questions and context incident

- Sent a bounded framework question to MathExpert and a certificate-design question
  to Validator through the file bus; work continues asynchronously.
- During a filename-only inventory used to isolate the fresh run, I inadvertently
  saw the historical filename
  `verification/scratch/independent_wreath_counterexample.g`. I did not open it and
  will not use its contents or treat the filename as evidence. This is recorded as
  `possible_prior_context_exposure: filename_only`; any construction must be
  derived and checked from the active statement and current-run work.

## 2026-08-16T13:34:45Z — minimal tuple and first construction tests

### Least quotient-minimal tuple allowed by the reviewed conditions

For (p=3), take the least possible nonabelian class-2 exponent-3 power subgroup

\[
Q=\langle a,b,u,v,z\mid [a,b]=z,\ z,u,v\in Z(Q),\ Q^3=1\rangle
  \cong H_3(3)\times C_3^2.
\]

It has (|Q|=3^5), (Q'=\langle z\rangle), and
(Z(Q)=\langle z,u,v\rangle) of dimension 3, attaining all reviewed lower
endpoints. The affine bound then forces a quotient-minimal extension index at least
(3^{5-\lfloor4/3\rfloor}=3^4), so the least complete tuple is

\[
(p,\dim Q,\dim Z(Q),\dim Q/Q', [G:Q], |G|)=(3,5,3,4,3^4,3^9).
\]

### Root-action relations that are individually consistent

Use BCH coordinates on the class-2 Lie algebra of (Q) (valid because
(2^{-1}\in\mathbf F_3)). Let (T:u\mapsto v\mapsto z\mapsto0). A prospective
root (x^3=a) can act by (A=I+N_a), with

\[
N_a(b)=-u,\quad N_a(u)=v,\quad N_a(v)=z,
\]

and a prospective root (y^3=b) by (B=I+N_b), with

\[
N_b(a)=u,\quad N_b(u)=v,\quad N_b(v)=z.
\]

Both maps fix the other listed basis vectors. They preserve the sole bracket
([a,b]=z), fix their own proposed cube, and satisfy
(A^3=\operatorname{Inn}(a)), (B^3=\operatorname{Inn}(b)), up to the fixed
conjugation convention. Thus each one-generator cyclic extension is consistent.
Their joint coherence is the issue.

### Exact matrix checks (commands and observed outputs)

The first command attempted to use NumPy and failed; no result was inferred:

```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

A pure-Python (5\times5) calculation over (mathbf F_3) then gave:

```text
A^3-I
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 2 0 0 0
B^3-I
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 0 0 0 0
C=[A,B]
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
1 1 0 1 0
1 1 0 0 1
C-I
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 0 0 0
1 1 0 0 0
[C,A]-I
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
2 2 0 0 0
[C,B]-I
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
2 2 0 0 0
C^3-I
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```

What this establishes: these two selected root actions generate a class-2 outer
pattern—(C=[A,B]) is not inner, while its commutators with (A,B) are inner.
What it does not establish: existence of a group extension realizing all these
automorphisms with the prescribed cubes, a normal form, power-set closure, or a
counterexample.

### Split-holomorph kill

Trying (E=Q\rtimes\langle A,B\rangle) avoids the extension-coherence problem but
cannot work. Every generated automorphism acts trivially on (Q/Z(Q)). For
((q,s)\in E), the base component of ((q,s)^3) is therefore central, while the
automorphism component (s^3) is inner. Since (Q) has class 2, its inner
automorphism group is abelian and acts trivially on (Z(Q)). Hence all cubes in
this split ansatz lie in the abelian subgroup
(Z(Q)\times\operatorname{Inn}(Q)). This is a firm exclusion of this split
realization, not of nonsplit extensions.

### Representation-changing cyclic-coordinate test

To permit noncentral norm values, replace (Q) by three Heisenberg coordinates and
let an order-3 automorphism cyclically permute them. I also allowed the maximal
linear space of central shears satisfying the exact order-3 norm equation. The
exact linear-algebra command formed the 18-variable condition

\[
\tau^2f+\tau f\tau+f\tau^2=0
\]

and computed the image of the central term in a cube. Its observed output was:

```text
dim ker(K)= 12
rank central norm im(I+tau+tau^2)=1
w=e1, u=(1,0,0;0,0,0) rank H= 3 rank(H+diag)= 3 Nu= [1, 0]
w=0, u=(1,-1,0;0,0,0) rank H= 1 rank(H+diag)= 1 Nu= [0, 0]
w=0, u=(1,-1,0;1,-1,0) rank H= 1 rank(H+diag)= 1 Nu= [0, 0]
w=0, u=(1,-1,0;0,1,-1) rank H= 1 rank(H+diag)= 1 Nu= [0, 0]
```

Thus the shears fill every central coordinate above a nonzero diagonal
noncentral value, but over zero they supply only the diagonal central line. A hand
check shows the BCH bracket correction is also diagonal when the three
noncentral coordinates sum to zero: writing (u_0+u_1+u_2=0), each correction
coordinate is (-\tfrac12\omega(u_0,u_1)). Therefore this enlarged semidirect
family still has an exact zero-fibre defect and its cube-value set is not a
subgroup.

### Exact wreath-family near miss

The preceding defect has a group-theoretic formulation. If (H) is any nonabelian
group of exponent 3 and (W=H\wr C_3=H^3\rtimes\langle t\rangle) with (t)
cycling the coordinates, then

\[
\{w^3:w\in W\}=\{1\}\cup
\{(h,h^r,h^s):h,r,s\in H\}.
\]

Indeed the three coordinate products of ((h_1,h_2,h_3)t)^3 are cyclic
permutations of (h_1h_2h_3), and conversely the two conjugators can be prescribed
independently. Choose (h,r) with (h^r\ne h). Both
((h,h^r,h)) and ((h^{-1},h^{-1},h^{-1})) are actual cubes, but their product
((1,h^rh^{-1},1)) is not: three coordinates of any displayed cube are conjugate,
and an element conjugate to 1 is 1. So this actual cube set is not closed.

For (H=H_3(3)), (W) is a finite 3-group of order (3^{10}) and exact exponent
9, but it is an `OUT_OF_SCOPE_EXAMPLE` because the actual cubes fail the subgroup
hypothesis.

#### Constraint-and-conclusion matrix for the near miss

| constraint_id | role | required condition | candidate value / proof use | evidence | result |
|---|---|---|---|---|---|
| 21.137-odd-forall-p-G | admissibility | one qualifying witness refutes universal assertion | proposed single group (W) | construction above | pass as witness form |
| 21.137-odd-p-not-2 | admissibility | odd prime | (p=3) | definition | pass |
| 21.137-odd-finite-p-group | admissibility | finite same-3 group | (|W|=3^{10}) | semidirect-product order | pass |
| 21.137-odd-exponent-p2 | admissibility | exact exponent 9 | every cube lies in exponent-3 base; a nontrivial norm gives order 9 | hand argument above | pass |
| 21.137-odd-power-set-definition | admissibility | actual cube set | exact conjugate-triple formula above | direct collection | pass |
| 21.137-odd-power-set-subgroup | admissibility | actual cubes closed | explicit product leaves the set | hand witness above | **fail** |
| 21.137-odd-P-abelian | target conclusion | target predicts abelian | not evaluated after failed hypothesis | scope gate | not applicable |

This is not a counterexample and cannot trigger a claim.

## 2026-08-16T13:41:56Z — counterexample-direction 30-minute self-check

- **Target/revision:** `21.137/odd-prime-exponent-p2`, revision 2,
  counterexample direction.
- **Current hypothesis:** a counterexample, if accessible constructively, should be
  an exponent-9 extension whose quotient action realizes enough length-three norm
  images to cover a nonabelian class-2 cube subgroup.
- **New checkable facts:** the least quotient-minimal tuple is
  ((3,5,3,4,3^4,3^9)); the displayed individual root actions satisfy their cube
  identities; their split holomorph realization has only abelian cubes; and the
  entire regular-wreath family (H\wr C_3) with nonabelian exponent-3 (H) fails
  actual-cube closure by an explicit two-cube product.
- **Candidate admissibility:** no current candidate passes every row. The exact
  (H_3(3)\wr C_3) near miss passes (p=3), finiteness, exact exponent 9, and the
  actual-set identification, but fails
  `21.137-odd-power-set-subgroup`; it is an `OUT_OF_SCOPE_EXAMPLE`.
- **Productivity decision:** the assigned minimal direct pc/Lie ansatz has met its
  kill criterion. There is no complete jointly consistent power/conjugation
  presentation and no exact closed actual-cube certificate. I will not keep adding
  relations to it ad hoc.
- **Representation-changing pivot:** yes—from direct minimal pc relations to an
  exact norm/cocycle coefficient model for a cyclic action on a class-2
  exponent-3 Lie base.

### Decision checkpoint

**Bottleneck.** Individual root automorphisms are easy; global extension coherence
and the zero fibre of the actual cube map are not. Filling noncentral fibres while
missing central cancellation values is the recurring closure defect.

**Alternative A (recommended).** *Equivariant-bracket norm construction.* Test the
prepared 45-coefficient linear family in which a cyclic order-3 action on two
regular modules has exact norm image (W\oplus Z_0). A complete multiplication
law follows immediately from any surviving alternating bracket. This has a
specific next step under one second, a reason to produce either an explicit
candidate or an exact family exclusion, and a hand-readable linear certificate.
Kill it if the constrained solution space forces ([W,W]=0), or if the (t^2)
cube image differs from the same subgroup. A fresh Lead lease is pending.

**Alternative B.** *Central cocycle over products of (C_3\wr C_3).* Start from a
class-3 exponent-9 group whose actual cubes form a central elementary-abelian
subgroup, then classify only central 2-cocycles capable of making two lifted cube
values fail to commute while preserving exponent 9 and exact cube-set closure.
Kill it if the Hall weight-4 identities force the induced alternating pairing on
the cube subgroup to vanish.

**Recommended next experiment:** Alternative A, bounded to one hour including a
hand reconstruction. While Lead decides, only symbolic derivation and inbox
polling will continue.

## 2026-08-16T13:43:05Z — pre-compute scope correction

The prepared cyclic-bracket test targets an exact cube subgroup
(P=W\oplus Z_0) of dimension (2+1=3). If it were nonabelian, then every quotient
in which its image remains nonabelian would retain the full order-(3^3) image,
because (3^3) is already the smallest possible order of a nonabelian 3-group.
But the reviewed quotient-minimal reduction forces (|P|\ge3^{p+2}=3^5) at
(p=3). Hence this coefficient family cannot yield an active-scope
counterexample; a positive algebraic output would necessarily conceal a failed
group/exponent/power-set premise. The compute request is withdrawn before launch.

This is a scope-driven kill, not an observed solver result. The script was prepared
but never run.

## 2026-08-16T13:46:24Z — a second exact near miss: noncommuting actual cubes

Let (J\) be the 15-dimensional associative (mathbf F_3)-algebra embedded in
strictly upper-triangular (7\times7) matrices and generated by

\[
x=e_{12}+e_{23}+e_{34},\qquad
y=e_{45}+e_{56}+e_{67}.
\]

Equivalently, its basis is the nonconstant monomials (x^iy^j) with
(0\le i,j\le3), subject to (x^4=y^4=yx=0). Distinct displayed monomials have
distinct matrix support, so they are independent. Put (G_J=1+J).

- (|G_J|=3^{15}).
- (J^7=0), so ((1+a)^9=1+a^9=1) for every (a\in J). Since
  ((1+x)^3=1+x^3\ne1), the exponent is exactly 9.
- In characteristic 3, every actual cube is exactly (1+a^3).
- The two actual cubes (1+x^3=1+e_{14}) and (1+y^3=1+e_{47}) do not commute,
  because (x^3y^3=e_{17}\ne0) while (y^3x^3=0).
- Nevertheless their product is not an actual cube. Filter (J) by word degree.
  If (a=a_1+a_{\ge2}) with (a_1=\alpha x+\beta y), then the degree-3 part of
  (a^3) is

  \[
  \alpha x^3+\alpha^2\beta x^2y+\alpha\beta^2xy^2+\beta y^3.
  \]

  The degree-3 part of
  ((1+x^3)(1+y^3)-1=x^3+y^3+x^3y^3) is (x^3+y^3). Monomial independence
  forces (alpha=\beta=1), but then both mixed degree-3 coefficients equal 1,
  a contradiction.

Thus this group has exact exponent 9 and explicitly noncommuting actual cubes, but
the actual cube-value set is not a subgroup. It is another
`OUT_OF_SCOPE_EXAMPLE`, now showing that noncommutativity itself is easy and the
closure row is the sharp obstruction.

### Constraint-and-conclusion matrix for (G_J)

| constraint_id | role | required condition | candidate value / proof use | evidence | result |
|---|---|---|---|---|---|
| 21.137-odd-forall-p-G | admissibility | one qualifying witness refutes universal assertion | proposed single algebra group | construction above | pass as witness form |
| 21.137-odd-p-not-2 | admissibility | odd prime | (p=3) | base field | pass |
| 21.137-odd-finite-p-group | admissibility | finite same-3 group | (|G_J|=3^{15}) | 15-dimensional algebra normal form | pass |
| 21.137-odd-exponent-p2 | admissibility | exact exponent 9 | (J^7=0), (x^3\ne0) | binomial calculation | pass |
| 21.137-odd-power-set-definition | admissibility | actual cubes | exactly ({1+a^3:a\in J}) | characteristic-3 identity | pass |
| 21.137-odd-power-set-subgroup | admissibility | actual cubes closed | product of (1+x^3), (1+y^3) is not a cube | degree-filtration proof | **fail** |
| 21.137-odd-P-abelian | target conclusion | target predicts abelian | two actual cubes do not commute, but hypothesis failed first | direct matrix products | violated only out of scope |

No catalogue, GAP, Sage, solver, or enumeration was used for this example.

## Cycle outcome — 2026-08-16T13:47:58Z

`PARTIAL_RESULT`. The active scope remains unanswered. The exact covered families,
failed admissibility rows, and uncovered scope are packaged in `findings.md` and
routed to Validator. The assigned minimal pc/Lie construction strategy is stopped;
no further computation or construction will run in this cycle without a new Lead
decision.
