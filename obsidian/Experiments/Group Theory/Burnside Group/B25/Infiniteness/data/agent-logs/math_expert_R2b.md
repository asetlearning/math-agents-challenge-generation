• Searched the web for https://arxiv.org/pdf/1311.0855

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

• Short Answer
  Quantitative NO for literal ball-radius-128 injectivity. Before theorem choice: if any length-4 root w has w^5 != 1 in G_3, then w^5 has word length at most 20 in G_3 and maps to 1 in G_4. So G_3 -> G_4 cannot be
  injective on the ordinary Cayley ball of radius 128. The viable target is E7-specific nontrivial image, not full ball injection.

  I added this to /Users/maumayma/Desktop/reps/algo_mixing/infinite_b25/avenues/math_expert_R2_full.md.

  Theorem Sanity

  - AGM / relatively hyperbolic Dehn filling: AGM Theorem 2.1 gives: for finite protected set F, there is a slope-length bound B so long fillings inject on F and preserve relative hyperbolicity. See Theorem 2.1,
    especially injectivity on F via Cor. 9.7 lines 189-206. But it is torsion-free as stated, and for cyclic peripheral P=<w>, filling by <w^5> has slope length 5. To use it for radius 128, one would need B <= 5,
    which is not plausible and not numerically supplied by AGM. Source: AGM PDF lines 181-206. (arxiv.org (https://arxiv.org/pdf/1311.0855))

  - DGO rotating families: DGO has a qualitative ball-injectivity theorem for relatively hyperbolic fillings: Theorem 7.9 says for each radius R there is a finite forbidden set S; fillings avoiding S inject on
    B_R(G). But again this is not a usable published numeric certificate for <w^5>, and literal ball injection is already impossible if any new w^5 is nontrivial. Source: DGO Theorem 7.9 lines 6207-6212. (arxiv.org
    (https://arxiv.org/pdf/1111.7048))

  - DGO computable constants are catastrophically too large: their rotating-family route requires huge injectivity radius. Proposition 6.23 requires inj_X(R) >= A0 δ, with A0 = inj_c(r0)/δ_c; Proposition 5.41 has
    inj_c = 4 r0 L(r0), and the universal cone radius satisfies r_U > 5 * 10^12. Sources: constants at lines 3992-3997, inj_c at lines 4158-4162, and A0 at lines 5111-5120. (arxiv.org
    (https://arxiv.org/pdf/1111.7048)) (arxiv.org (https://arxiv.org/pdf/1111.7048)) (arxiv.org (https://arxiv.org/pdf/1111.7048)) For a length-4 root, inj(<w^5>) <= |w^5| <= 20, so this route is off by astronomical
    orders of magnitude.

  - Coulon partial periodic quotients: formal NO for exponent 5. Coulon’s Proposition 6.1/Theorem 6.9/Theorem 6.15 require an odd exponent n > n1, where the construction first chooses n0 > 100, then n1 > n0; see
    lines 3203-3213 and Theorem 6.15 lines 3767-3775. (arxiv.org (https://arxiv.org/pdf/1311.0855)) (arxiv.org (https://arxiv.org/pdf/1311.0855)) Thus n=5 cannot satisfy the published theorem, independent of G_3
    constants.

  Recommendation
  Do not spend compute trying to certify ordinary B_128 injectivity. First check which length-4 fifth powers are nontrivial in G_3; one such receipt kills ball injectivity immediately. Then reformulate the theorem
  target as: protect the single element E7 under the quotient, or produce a DGO/Osin-style finite-forbidden-set test for {E7} only.

─ Worked for 10m 19s ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

 
› Use /skills to list available skills
 
  gpt-5.5 xhigh · ~/Documents/Obsidian/Math/obsidian/Agents/maumayma/MathExpert/.maestri/roles/4fc00b87-17b8-4a9c-9c3d-576bf1a2c0f9
