---
title: "Verification — Kourovka 20.21 — minimum-witness reductions"
problem: "20.21"
scope_id: 20.21/two-index-twelve-kernels
scope_record: Agents/Kourovka/scopes/20.21-two-index-twelve-kernels.json
assignment_revision: 1
claim: "If an active-scope witness exists, a minimum-order witness lies in the common-C3 branch and has even, odd-core-free intersection N, nonabelian coordinate kernels, and N not contained in Z(L)."
claimant: Problem-20.21
target_statement: "There exist a finite group G and normal subgroups K,L normal in G such that [G:K]=[G:L]=12, K is isomorphic to L, G/K is isomorphic to C_12, and G/L is isomorphic to A_4."
excluded_scopes:
  - Pairs of nonnormal subgroups
  - Pairs with only one index equal to 12
  - Pairs with the two quotient isomorphism types swapped unless K and L are correspondingly relabelled
target_object: "A finite triple (G,K,L) satisfying every active-scope row"
witness_object: "None submitted; the claim concerns arbitrary hypothetical witnesses and smaller triples descended from them"
witness_equals_target: unknown
citation: none
verification_method: computation-free line-by-line hand proof within the Lead-imposed three-artifact boundary
tools_used: [none]
scope_answered:
  - "Necessary minimum-witness reductions inside 20.21/two-index-twelve-kernels"
scope_not_answered:
  - 20.21/two-index-twelve-kernels
  - "Existence or nonexistence of a surviving common-C3 witness"
active_assignment_answered: no
partial_result_certifiable: yes
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/group-extensions, project/kourovka, status/conjectured]
---

# Verification — Kourovka 20.21

## The claim

Conditionally on the existence of an active-scope witness, choose one of minimum ambient-group order and put (N=K\cap L).  The candidate reduction says that this minimum witness satisfies

\[
K/N\cong V_4,\qquad L/N\cong C_4,
\]


\[
2\mid |N|,\qquad O_{2'}(N)=1,
\]

and (K\cong L) is nonabelian, with (N\not\le Z(L)).

Validator verdict: **PASS as a necessary `PARTIAL_RESULT`**.  Each of the four candidate restrictions survives hostile reconstruction.  The result is conditional and does not answer whether a witness exists.

## Scope, revision, and clause matrix

Locked scope: `20.21/two-index-twelve-kernels`, assignment revision 1.

| source clause | active | what the claim establishes | what remains |
|---|---:|---|---|
| c1: existence of one finite triple satisfying every structural row | yes | Restrictions that any minimum-order witness must satisfy | The complete existence/nonexistence question |

No excluded scope is used or answered.  In particular, the descended triple retains the ordered quotients (C_{12}) at the first kernel and (A_4) at the second kernel; no unannounced relabelling is used.

`active_assignment_answered: no`.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / proof use | evidence | result |
|---|---|---|---|---|---|
| 20.21-exists-GKL | admissibility | One triple satisfies all remaining rows | No concrete triple; existence is assumed only conditionally | Every argument begins with a hypothetical witness | not established |
| 20.21-G-finite | admissibility | (G) finite | Used to select a least order and in Sylow/torsion arguments; every quotient/subgroup constructed is finite | Sections 1, 2, and 4 | preserved conditionally, not witnessed |
| 20.21-KL-normal | admissibility | (K,L\triangleleft G) | Gives (N\triangleleft G), makes both descended kernels normal in their new ambient group, and gives the conjugation equivariance | Sections 1 and 4 | preserved conditionally, not witnessed |
| 20.21-both-index-12 | admissibility | Both indices exactly 12 | In the strict descent, both new indices are computed from (L/N\cong C_{12}) and (K/N\cong A_4) | Section 1 | preserved conditionally, not witnessed |
| 20.21-kernels-isomorphic | admissibility | (K\cong L) | Supplies (	heta); its restriction identifies the descended kernels and later identifies the torsion profiles of (N) and (M) | Sections 1, 2, 3, and 4 | preserved conditionally, not witnessed |
| 20.21-quotient-K-C12 | admissibility | (G/K\cong C_{12}) | The first new kernel is chosen as (	heta^{-1}(N)), so the first descended quotient is (L/N\cong C_{12}) | Section 1 | preserved with correct orientation, not witnessed |
| 20.21-quotient-L-A4 | admissibility | (G/L\cong A_4) | The second new kernel is (N), so the second descended quotient is (K/N\cong A_4); its common-C3 image supplies the order-three action | Sections 1 and 4 | preserved with correct orientation, not witnessed |
| 20.21-existence-conclusion | target_conclusion | At least one such triple exists | No candidate value | The note expressly remains conditional | unproved |

There is no candidate object to label an out-of-scope example.  Rather, this is a proof of necessary conditions whose existence row remains open.

## Target versus witness

The target is the finite triple in the canonical scope record.  The submission contains no concrete witness and therefore provides no `witness = target` identification.  For the reduction actually claimed, the relevant fidelity test is instead whether each smaller triple is again an active-scope triple.  Section 1 checks this directly, including normality, index (12), kernel isomorphism, strict decrease, and the quotient orientation.

The mathematical-resource boundary was exactly the three artifacts named by Lead: the revision-1 scope record, the prior scope-wide Goursat audit, and the standalone reduction note.  The contaminated root log and unrostered-helper material were not used.  The prior audit is the locked input for the two Goursat branches and their orientation.

## Subclaims and what each method proves

| subclaim | method | a pass proves | a pass does not prove |
|---|---|---|---|
| Existence of a minimum conditional on existence | Well-ordering of finite group orders | A least-order witness can be selected | That the set of witnesses is nonempty |
| Full-product descent | Isomorphism theorem plus explicit normality and order checks | No minimum witness lies in the full-product branch | That no larger full-product witness exists |
| Evenness of (N) | Sylow 2-subgroup comparison | Every common-C3 witness has even (|N|) | Any classification of even (N) |
| Odd-core removal | Characteristic-radical equality and quotient correspondence | A minimum witness has (O_{2'}(N)=1) | That (N) is a 2-group |
| Abelian-kernel exclusion | Equivariant (2)-power torsion filtration in a finite abelian group | A common-C3 witness has nonabelian (K\cong L) | Exclusion of any nonabelian kernel |
| Centrality corollary | Cyclic central quotient lemma | (N\not\le Z(L)) | (N\not\le Z(K)), or any stronger placement claim |

## Evidence

### 1. Full-product descent: normality, orientation, and strictness

Assume the reviewed full-product branch

\[
K/N\cong A_4,\qquad L/N\cong C_{12}.
\]

Since (K,L\triangleleft G), their intersection (N) is normal in (G), hence normal in both (K) and (L).  Fix an abstract isomorphism (	heta:K\to L), set (Q=K), and define

\[
K_1=\theta^{-1}(N),\qquad L_1=N.
\]

The normality point is genuine and does not require either subgroup to be characteristic: (N\triangleleft L) implies (	heta^{-1}(N)\triangleleft K=Q), while (N\triangleleft K=Q) directly.  Moreover, restriction gives

\[
\theta|_{K_1}:K_1\xrightarrow{\sim}N=L_1.
\]

The quotient orientation is

\[
Q/K_1\cong L/N\cong C_{12},\qquad
Q/L_1=K/N\cong A_4.
\]

Thus ([Q:K_1]=[Q:L_1]=12), and ((Q,K_1,L_1)) is a witness to exactly the ordered active target, not its swapped variant.  Finally,

\[
|Q|=|K|=|G|/12<|G|.
\]

If any finite witness exists, the positive integers (|G|) occurring among witnesses have a least element.  The strict descent contradicts minimality in the full-product branch.  Therefore every minimum-order witness is in the common-(C_3) branch.

### 2. The intersection has even order

Now use

\[
K/N\cong V_4,qquad L/N\cong C_4.
\]

Suppose that (|N|) is odd.  Then the 2-part of both (|K|=4|N|) and (|L|=4|N|) is (4).  If (P\in\operatorname{Syl}_2(K)), then (|P|=4), (P\cap N=1), and the quotient map embeds (P) in the order-four group (K/N).  Its image has order four, so

\[
P\cong K/N\cong V_4.
\]

The identical argument for every (S\in\operatorname{Syl}_2(L)) gives

\[
S\cong L/N\cong C_4.
\]

An isomorphism (K\to L) maps a Sylow 2-subgroup of (K) onto a Sylow 2-subgroup of (L).  It cannot map (V_4) isomorphically to (C_4).  Hence (|N|) is even.  This argument applies to every common-(C_3) witness, not only a minimum one.

### 3. Equality of odd cores and quotient descent

Use the following elementary lemma.  If (N\triangleleft H) and (H/N) is a 2-group, then

\[
O_{2'}(H)=O_{2'}(N)
\]

as actual subgroups of (H).  Indeed, (O_{2'}(H)) has trivial image in the 2-group (H/N), so it lies in (N); being normal in (N), it lies in (O_{2'}(N)).  Conversely, (O_{2'}(N)) is characteristic in (N), hence normal in (H), so it lies in (O_{2'}(H)).

Apply the lemma to (H=K) and (H=L).  Since both (K/N\cong V_4) and (L/N\cong C_4) are 2-groups,

\[
O_{2'}(K)=O_{2'}(N)=O_{2'}(L)=:O.
\]

This is equality of the same subgroup (O\le N), not merely equality of orders or abstract isomorphism types.  Also (O=O_{2'}(K)) is characteristic in (K), so (O\triangleleft G) because (K\triangleleft G).  For any isomorphism (	heta:K\to L), characteristic-radical functoriality gives

\[
\theta(O_{2'}(K))=O_{2'}(L),
\]

and the displayed actual equality therefore says (	heta(O)=O).  Hence (	heta) induces (K/O\cong L/O).

If (O\ne1), then (K/O,L/O\triangleleft G/O), and

\[
(G/O)/(K/O)\cong G/K\cong C_{12},
\]

\[
(G/O)/(L/O)\cong G/L\cong A_4.
\]

Both indices remain (12), while (|G/O|<|G|).  Thus ((G/O,K/O,L/O)) is a strictly smaller active-scope witness.  A minimum-order witness consequently has

\[
O_{2'}(N)=1.
\]

This does not imply that (N) is a 2-group; it only removes normal odd-order subgroups.

### 4. The torsion filtration: equivariance and equal image sizes

Continue in the common-(C_3) branch.  Put (Q=K), choose (	heta:K\to L), and put

\[
M=\theta^{-1}(N).
\]

Then (M\triangleleft Q), restriction of (	heta) gives (M\cong N), and there are quotient maps

\[
f_N:Q\twoheadrightarrow Q/N\cong V_4,
\qquad
f_M:Q\twoheadrightarrow Q/M\cong C_4.
\]

Assume for contradiction that (Q) is abelian.  Let (eta:G\twoheadrightarrow G/L\cong A_4), and choose (g\in G) for which (eta(g)) is a 3-cycle.  The common-(C_3) orientation identifies

\[
\beta(K)=K/(K\cap L)=K/N\cong V_4
\]

with the normal Klein four subgroup of (A_4).  Conjugation by a 3-cycle cycles its three nonidentity elements.

Both (Q=K) and (N) are normal in (G), so conjugation by (g) preserves them and (f_N) is equivariant for this action.  For (j\ge1), define

\[
Q[2^j]=\{q\in Q:q^{2^j}=1\}.
\]

Because (Q) is abelian, (Q[2^j]) is a characteristic subgroup of (Q), hence is preserved by conjugation by (g).  Therefore (f_N(Q[2^j])) is invariant under the 3-cycle action on (V_4).  That action has no subgroup of order two invariant under it, so

\[
|f_N(Q[2^j])|\in\{1,4\}. \tag{1}
\]

The kernels of the two restricted maps are exactly

\[
Q[2^j]\cap N=N[2^j],\qquad
Q[2^j]\cap M=M[2^j].
\]

Consequently,

\[
|f_N(Q[2^j])|=\frac{|Q[2^j]|}{|N[2^j]|},
\qquad
|f_M(Q[2^j])|=\frac{|Q[2^j]|}{|M[2^j]|}. \tag{2}
\]

The abstract isomorphism (M\cong N) preserves element orders, hence

\[
|M[2^j]|=|N[2^j]|
\]

for every (j).  Equation (2) therefore gives the required equality

\[
|f_M(Q[2^j])|=|f_N(Q[2^j])|. \tag{3}
\]

It remains to force an intermediate image of order two on the (C_4) side.  Since (f_M) is onto, take (x\in Q) mapping to a generator of (C_4).  Write (|x|=2^a m) with (m) odd.  Then (x^m) has 2-power order and (f_M(x^m)=f_M(x)^m) is still a generator.  Hence there is a least (j\ge2) such that

\[
f_M(Q[2^j])=C_4.
\]

Choose (y\in Q[2^j]) mapping to a generator.  Then (y^2\in Q[2^{j-1}]) maps to the unique involution of (C_4).  By minimality, (f_M(Q[2^{j-1}])\ne C_4); since it contains that involution, it is exactly the subgroup of order two.  This contradicts (1) and (3).

Thus (Q=K) is nonabelian.  Since (K\cong L), (L) is nonabelian as well.

Finally, if (N\le Z(L)), then (L/Z(L)) is a quotient of the cyclic group (L/N\cong C_4), so (L/Z(L)) is cyclic.  A group with cyclic quotient by its center is abelian: if (L/Z(L)=\langle tZ(L)\rangle), all elements have the form (t^i z) and commute.  This contradicts the established nonabelianity of (L).  Therefore

\[
N\not\le Z(L).
\]

No parallel conclusion (N\not\le Z(K)) follows from this argument, because (K/N\cong V_4) is not cyclic.

No mathematical computation, web search, historical solution, root-log material, or delegated work was used.

## Verdict

`status/conjectured` under the certification ladder, with the mathematical verdict **PASS as a scoped necessary `PARTIAL_RESULT`**.  The full-product descent has the correct normality and quotient orientation; the odd-core equality is equality of actual characteristic subgroups and its quotient descent is valid; the (Q[2^j]) argument is equivariant and its equal-image-size step follows from the exact kernel formula; and the stated centrality conclusion follows on the (L/N\cong C_4) side.

The tag remains `status/conjectured` because the protocol's human-seen gate for `status/proven` has not been met.  This does not weaken the explicit Validator judgement on the partial reduction.

## Why this verdict

Each subclaim is supported by a complete hand argument and survives the named hostile checks.  Crucially, all descended objects are shown to remain in the exact active scope.  Equally crucially, no conditional restriction is mistaken for the active existence conclusion.

## What is NOT established

- No active-scope witness is constructed.
- Nonexistence is not proved.
- A larger full-product witness is not ruled out; only a minimum witness is forced out of that branch.
- The common-(C_3) branch remains open for nonabelian (K\cong L) with even (N), (O_{2'}(N)=1), and (N\not\le Z(L)).
- Trivial odd core does not make (N) a 2-group.
- No claim is established about (N\le Z(K)).
- No earlier bounded family exclusion is generalized.

Thus `active_assignment_answered: no`.

## What would upgrade it

To answer the active assignment, one must either construct an explicit surviving triple and prove all eight constraint/conclusion rows, or prove that no finite triple in the surviving common-(C_3) class exists.  Separately, the protocol requires the human to see this proof before the partial lemma's note can carry `status/proven`.
