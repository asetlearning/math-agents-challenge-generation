---
title: "Verification — Kourovka 12.15 — order-128 reduction and central-lift specification"
problem: "12.15"
scope_id: 12.15/normal-closure-fibres
scope_record: Agents/Kourovka/scopes/12.15-normal-closure-fibres.json
assignment_revision: 1
claim: "The cycle-close deductions and action-plus-cocycle specification give a correct and exhaustive partial reduction at the first possible counterexample order."
claimant: Problem-12.15
target_statement: "Every qualifying finite 2-group has abelian derived subgroup."
target_object: "A hypothetical least counterexample, specialized after the lower bound to order 128"
witness_object: "No witness; symbolic reductions and an exact reconstruction specification"
verification_method: computation-free line-by-line hand proof
tools_used: ["none"]
scope_answered: ["order lower bound, order-128 regimes, and reconstruction/checking specification"]
scope_not_answered: ["12.15/normal-closure-fibres"]
active_assignment_answered: no
partial_result_certifiable: yes
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/conjectured]
---

# Verdict

**PASS as a `PARTIAL_RESULT`, with one minor organizational correction.** The lower bound |G|≥128, the three surviving order-128 regimes, and the action-plus-cocycle reconstruction/check rows are sound and exhaustive for the stated partial reduction. Row H5 should be moved from Layer 1 to Layer 2 (or explicitly marked deferred): (D_G(c)) depends on the completed extension (G), not on (H) alone. Its duplicate, G7, is correctly placed. This does not affect the mathematics or coverage.

# Order lower bound

Let \(z\) generate \(Z(G)=G''\cong C_2\), as in the already audited least-counterexample core. An irreducible character nontrivial on \(z\) is faithful, because every nontrivial normal kernel contains the unique minimal normal subgroup \(\langle z\rangle\). Hence \(z\) acts as \(-I\). Since every noncentral \(g\) is conjugate to \(gz\), \(\chi(g)=\chi(gz)=-\chi(g)\), so \(\chi\) vanishes off \(\{1,z\}\). Row orthogonality gives

\[
|G|=2\chi(1)^2=2^{2n+1}.
\]

Also |G:G'|≥4 and |G'|≥8, so |G|≥32. Order (32) is impossible without classification: then |G'|=8; with γ_i the lower central series, (1\ne G''=[\gamma_2,\gamma_2]\le\gamma_4), strict descent forces |γ₃|=4, |γ₄|=2, and γ₅=1. A two-generator group has cyclic (G'/\gamma_3), so (G'=\langle c\rangle\gamma_3). The group γ₃ is abelian of order (4), and ([c,\gamma_3]\le[\gamma_2,\gamma_3]\le\gamma_5=1); hence (G') would be abelian. The next possible value (2^{2n+1}) is (128).

# Exhaustion of order-128 regimes

Put (H=G'), (A=Z(H)), (V=H/A), and (E=G/H). Here (E) is elementary abelian of order at least (4), (H) is nonabelian, and the commutator form makes nonzero (V) symplectic. The order equation initially permits exactly

\[
(|E|,|H|,|A|,|V|)=(16,8,2,4),(8,16,4,4),(4,32,2,16),(4,32,8,4).
\]

In the two-generator case, writing the two commuting augmentation operators on (V) as (N=s-1), (M=t-1), the fibre condition forces (NM=0). Since (V) is cyclic as an \(\mathbf F_2E\)-module, \(\dim V\le3\); symplecticity makes its positive dimension even, hence \(\dim V=2\). This removes ((4,32,2,16)) and leaves exactly R1–R3 in the specification.

The associated action rows also check out. Clifford theory yields

\[
t=|A:\langle z\rangle|,  e^2=|E|/|A:\langle z\rangle|, 
|E:C_E(A)|=|A:\langle z\rangle|.
\]

Thus the action on \(A\) has image orders \(1,2,4\) in R1, R2, R3 respectively. The image on \(V\cong C_2^2\) has order at most \(2\); in R3 it is nontrivial, because a trivial action could not make the cyclic \(\mathbf F_2E\)-module \(V\) two-dimensional. The listed possibilities for \(A\), and \(H=D_8\) or \(Q_8\) in R1, are therefore complete. The deductions \(A^E=\langle z\rangle\), \(\exp(A)\le8\), and \(\exp(H)\le16\) are also valid.

# Reconstruction audit

1. **Layer 1 is exhaustive.** A normalized central cocycle η on (V=C_2^2) with values in (A) gives every central extension (1\to A\to H\to V\to1). The displayed cocycle identity, multiplication, square formula, and alternating-part formula are correct. Requiring the alternating part to have image ⟨z⟩ and be nondegenerate is precisely (H'=\langle z\rangle) and (Z(H)=A).
2. **Layer 2 is exhaustive.** With the specified section convention, the weak-action equation
   \(α_eα_f=\operatorname{Inn}(f(e,f))α_{e+f}\), the nonabelian cocycle equation, and the multiplication law are mutually consistent and parametrize every extension (1\to H\to G\to E\to1). G2–G4 enforce the characteristic layers and exact center. G5 is exactly the condition (G'=H); together with elementary-abelian (E), G6 then gives (H=\Phi(G)), the exact quotient, and order (128).
3. **The R3 cross-layer row is sound.** For a basic commutator (c), its defect subgroup has image a line in (V), has order (16), contains all of (A), and is abelian; its complementary coset is the conjugacy class of (c). This belongs with G7, not H5.
4. **Layer 3 is exact.** P1 and P2 are precisely the audited intrinsic form of the source hypothesis. P3 is a valid redundant least-counterexample consistency check. With G5, P4 is exactly (G''=H'=\langle z\rangle\ne1). Thus these rows neither omit a source condition nor silently assume the target conclusion. The warning that P1–P2 must be checked upstairs, not merely in the layer quotients, is essential and correct.

# Boundary

The specification is a complete certificate format for the order-128 branch, not an existence/nonexistence result. It does not establish (G''=1) and does not answer the active assignment. The earlier unleased wreath diagnostic is outside this audit and supplies no certified evidence here.
