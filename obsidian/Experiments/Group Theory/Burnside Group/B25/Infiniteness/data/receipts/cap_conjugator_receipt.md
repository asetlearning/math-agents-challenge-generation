# Cap-conjugator finite check — receipt (Lead, 2026-08-02)

**Statement checked (exhaustively):** for each of the 5 periods p ∈ {AABB, AAbb, ABAb, ABaB, ABab},
each rotation k ∈ {1,2,3}, and EVERY freely-reduced word c with |c| ≤ 3 (53 candidates incl. ε):
does c·rot_k(p)·c⁻¹ = p hold in G₃? (Decided via wordreduce -diff2 g3, verified automatic
structure.)

**Result:** 34 solutions total; **every solution lies in the coset u_k·⟨rot_k(p)⟩** where
u_k = p[:k] is the trivial rotation conjugator (p = u_k v ⟹ u_k·(v u_k)·u_k⁻¹ = p).
30/34 verified at the free-group level (c freely equals u_k·rot_k(p)^m, m ∈ [-6,6]);
the remaining 4 (aaa, BBB for AABB k=2; aaa, bbb for AAbb k=2) are G₃-power-identity duplicates:
NF(aaa) = A² = NF(AA), NF(BBB) = b² = NF(bb) (wordreduce receipts in session log).

**Zero exotic conjugators.** Combined with E(p_i) = ⟨p_i⟩ (annulus closure, B_ann = 24,
Validator-corroborated), this gives: the transporter set {c : |c| ≤ 3, c·rot_k(p)·c⁻¹ =_{G₃} p}
is exactly the single coset u_k·⟨rot_k(p)⟩ restricted to length ≤ 3.

**Intended use (unified band-reduction lemma):** any end-cap of a phase-offset same-period band
that "eats the conjugation" must be the trivial rotation conjugator up to axis powers; hence a
phase-offset band untwists into an aligned band of the same period (with the cap absorbed into
the rotation), reducing the phase-offset case to the aligned case handled by Lemma 2.1/BR2.
The lemma-level argument (that a band's caps must satisfy exactly this transporter equation)
is Math-expert's to write; this receipt supplies the finite input.

Replay: python block in Lead session log (5×3×53 wordreduce calls + coset classification);
periods/rotations/caps enumerated exhaustively, no sampling.
