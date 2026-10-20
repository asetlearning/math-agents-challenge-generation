---
type: validation-triage
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: review of Math Expert's generation-strategy proposal (2026-10-20-t028-generation-strategy-long-peaks, incl. §6 and §6b), with the Researcher's literature findings"
verdict: "Sound in its main lines, with issues to fix before pre-registration. CONFIRMED: substitution (C, C', C'-r) preserves triviality and maps certificates cell by cell; the e_U >= 1 lemma for strictly power-free words; the U1 upper bound; the finiteness caveat; conjugacy composition along distillation. ISSUES: (1) C's certificate lives over U_{7m} (cores of u^5, |u| <= 7m, any u), not R7, so L0 tooling and the depth metrics need a new table; (2) the half-exposure lemma in §6 has the wrong sign (gluing one cell never SHORTENS; it lengthens or keeps the length), though the multi-cell conclusion still holds for another reason; (3) C' 'no 2-generated subgroup contains W' is false as stated (F itself is 2-generated); (4) the Hall–Petresco c_5 certificate is about 6 U-cells, not about 3; (5) the 'onion is a monotone R_KB path, e = 0' is argued, not shown; (6) the in-loop compression statistic is the first stage of the held-out recovery attack (overfitting risk); (7) the falsifiers need denominators, a definition of 'broken', time units and a growth test; (8) the cost is underestimated, and coset bounds 2^26-2^27 do not fit the local cap. Probe: random-substitution W is rarely 2.5-reduced (0-10%) but keeps rho >= 0.5 in 70-97%."
---
# T-028 generation strategy: review (triage)

This is a Lead request (2026-10-20). It reviews `Agents/asetlearning/MathExpert/proposals/2026-10-20-t028-generation-strategy-long-peaks.md`, §1–§5, the §6 addendum and §6b, together with Lead's three FYIs: the Researcher's synthesis [[_synthesis-t028-literature-2026-10-20]], plus [[havas-ramsay-2000]], [[gersten-riley-2002]] and [[olshanskii-2011-space-functions]].

**Method.** I reviewed the logic of each claim. I ran one small probe on scheme C (§2 below), with scratch scripts in my session scratchpad. Nothing else was run.

**Terms.**
- **U** = {u⁵ : u any word}. **U_L** = the cyclic cores of u⁵ (and of u^{5k}), |u| ≤ L.
- **FFL_P** = free filling length over the move set P, and **e_P** = FFL_P − |w| is its excess (§6b).
- **Strictly power-free**: no window with exponent ≥ 2.5.
- **2.5-reduced**: no window with exponent > 2.5.

## 1. Definitions and §1 claims

| claim | verdict |
|---|---|
| Peak, filling length, excess | **Sound once named as FFL_P (§6b)**: cyclic words, free insertion and deletion, and x → y where x y⁻¹ is a rotation of r^{±1}. I agree with the correction: Gromov's FL and Olshanskii's FFFL are different functions, and the three can differ hugely in one group (Bridson–Riley, per Researcher). |
| "R is monotone over U" | **Correct.** Each R rewrite u^p → u^{−(5−p)} with p ≥ 2.5 is a U-move with |y| ≤ |x|, rotations are free on cyclic words, and free reduction only deletes. **Only one direction holds:** R succeeding implies e_U = 0, but e_U = 0 does not imply that greedy R succeeds. |
| "kbmag-slx is monotone over R_KB" | **Correct.** A shortlex rule l → r has |r| ≤ |l|, and inverse-pair rules are free deletions. Again one-directional: slx reaching IdWord implies e_{R_KB} = 0, not the converse. Rec is bounded-up, as stated. |
| "D works in a tube of radius ~log N" | **Heuristic only.** The table is grown by sewing relator cycles at all vertices, not as a ball around the root. §6b already withdraws "all three fail by construction" for D, and the Researcher found no source tying FL to coset-table size. D's coset bound should stay its own axis (§6), so the tube sentence should be marked conjectured or dropped. |
| "The onion read backwards is a monotone path over V ⊂ R_KB, so e = 0" | **Argued, not shown, and too strong.** Three gaps: (i) a level step with junction cancellation s, read backwards, needs a free insertion of length 2|s| before the V-move (the loop is a conjugate s t^{±1} s⁻¹ of the tile, not a rotation), so the shown bound is e_V ≤ 2·max junction cancellation, not e = 0; (ii) the parent dataset word must also be reduced, and many reduce only under rec, which is not monotone; (iii) "V ⊂ R_KB" needs kbprog to have kept every R7 equation and tile as a rule, which it may not after tidying. Also, a monotone path existing does not explain why kbmag *finds* one. As an explanation it is plausible and consistent with my data (kbmag also breaks the D/R residuals, which are not onion-built). It is not a derivation. |
| U1 (certificate prefix peak) | **Valid upper bound on FFL**: insert c c⁻¹ freely, insert the relator, free-reduce; the peak is ≤ \|P_j\| + 2\|c_j\| + \|r_j\| at each step. |
| U2 (shelling peak) | **Unproven.** It is only a bound once each layer peel is realised as moves within \|B_k\| + \|B_{k+1}\| + max\|r\|. This can fail for diagrams with cut vertices or non-annular layers. Do not report it as an upper bound until it is proved. |
| U3 (construction peak) | **Valid only when every generator step is a move sequence.** D jumps are not moves: a D step's diagram can have a high peak. So for distilled words, U3 needs the D steps replaced by explicit paths (e.g. kbmag paths). Also, the climb ratio κ is a construction statistic, not evidence about FFL. "Its known path has peak ≥ \|W\|" bounds nothing from below. |
| Finiteness caveat | **Correct.** If B(2,5) is finite, it has a finite Dehn presentation (every trivial word of length ≤ M, for M fixed by the hyperbolicity constant). Each such relator has a U-filling of bounded excess, so e_U ≤ K. |
| **§6: strictly power-free trivial w ⇒ e_U ≥ 1** | **CONFIRMED** for cyclically reduced w under the FFL move set. The argument: free deletion is impossible and free insertion lengthens. A U-move x → y with \|y\| ≤ \|x\| has \|x\| ≥ 2.5\|v\|, where v is the cyclic core of u, because x y⁻¹ is a rotation of u⁵. A non-reduced u only adds the conjugating part, which x cannot contain because x is reduced. So x is a v-periodic window of exponent ≥ 2.5 (higher if v is a proper power), and strict power-freeness forbids it. So the first move lengthens, and the peak is ≥ \|w\| + 1. Exact halves (2.5-reduced but not strictly power-free) allow a length-neutral flip first, as Math Expert notes. **Scope:** this holds for P = U only. The T-024 words were strictly power-free (the gate actually used), so they had e_U ≥ 1, yet kbmag broke them over R_KB. |

## 2. Scheme C (substitution)

- **Soundness: CONFIRMED.**
  - F⁵ (the verbal subgroup generated by all fifth powers) is fully invariant: φ(g⁵) = φ(g)⁵ for any endomorphism φ of F. So t ∈ F⁵ implies φ(t) ∈ F⁵, with no need for any further property of relatively free groups.
  - The certificate maps exactly: if ∏ c_i⁻¹ r_i c_i freely reduces to t, then ∏ φ(c_i)⁻¹ φ(r_i) φ(c_i) freely reduces to φ(t). Here r_i = (v′)^{5k}, where v′ is a rotation of v, so φ(r_i) = (φ(v′)^k)⁵.
  - Cyclically reducing φ(t) to W is a conjugation by some g, which must be applied to every conjugator.
  - Composed substitutions (C′-r) work the same way, through φ₂∘φ₁.
  - C′'s inverted factors need inverted cells. U contains (u⁻¹)⁵, so that is fine.
- **What table the certificate lives over.**
  - φ(v′) need not be cyclically reduced or primitive.
  - Its cell is a conjugate of z^{5j}, where z is the primitive root of the cyclic core of φ(v′). Write it either as the relator z^{5j} or as j cells z⁵.
  - So the table is **U_{7m}** (with |u| ≤ 35m only if v^{35} is kept as one relator), **not R7**.
  - L0-cert holds under the success-metrics rule ("standard relators v⁵, |v| ≤ L, qualify automatically") **with L = 7m stated**.
  - The current L0 tooling, the R7-keyed RelatorMap, and the S2 / flip depth measures on R7 do not apply as they are. They need a table built per word from the certificate.
- **Injectivity.** The pilot's no-cancellation junction rule makes every reduced word in x, y map to a reduced word of exactly m times its length. So φ is injective, |W| = m|t|, and W is cyclically reduced whenever t is.
  - That rule does **not** make φ(v′) primitive. If x is a proper power, x⁵ = z^{10}, and the certificate must then use U-relators with non-primitive roots. That is harmless, but the table must allow it.
  - **Without the junction rule (C′),** injectivity and non-triviality of W must be checked, for example by Stallings folding.
- **Is W still capable of passing L1-r25? Yes, but it is rarely 2.5-reduced as generated.**
  - **Probe.** t = 20 dataset words of 50–80 letters (2.5-reduced). x and y are uniform random of length m, with the pilot's junction rule. 3 pairs per t, 60 words per m. R = greedy then cyclic exhaustive 2.5, as in the L1 definition.

    | m | W 2.5-reduced | median ρ(W) | ρ ≥ 0.5 | ρ = 0 (R empties W) |
    |---|---|---|---|---|
    | 4 | 2/60 | 0.80 | 42/60 | 15/60 |
    | 8 | 6/60 | 0.87 | 55/60 | 4/60 |
    | 16 | 0/60 | 0.84 | 58/60 | 1/60 |

  - So the powers inside x and y and at the junctions are seen by R almost always. **The in-loop R rewrites W**, so the distilled word is not φ(t) and the certificate needs R-step fragments (U-cells).
  - At m = 4, R empties a quarter of the W.
  - I stopped a variant with x and y filtered for 2.5-reducedness to put the registry vetting first. It can be re-run if wanted.
- **Recovery breaks C completely** (Researcher; §6). I agree. Once x and y are known, every kbmag rule transfers as φ(l) → φ(r). Demoting C to the recovery control is right.
- **C′ "K ≥ 3 different pairs, so no 2-generated subgroup contains W"** is **false as stated**: F = ⟨a, b⟩ is itself 2-generated, and ⟨W⟩ is cyclic.
  - What is meant is: no decomposition W = φ(t) with φ recoverable and t KB-solvable.
  - Two attacks remain. A segmentation attack can solve each conjugated block c_j⁻¹ t_j(x_j, y_j) c_j separately, since each block is trivial on its own, if the junction cancellation does not hide the boundaries. And K = 3 blocks of one recovered key would still be solved block-wise.
  - The pre-registration should state the claim as a falsifiable property of the attack, not of the subgroup.
- **C12 (t = the T-024 originals).** 8 of the 12 are private. Words built from them, and their certificates (which reveal t once recovered), cannot go to public data/ without the owner's approval.

## 3. Scheme A (distillation)

- **The residual is an in-loop fixpoint:** true by construction when the chain stops at a fixpoint and not at a cap. The record must say which.
- **Certificate composition along the descent: CONFIRMED.** If w′ = c⁻¹ w c · E, then cert(w′) = [cert(w) with each conjugator multiplied by c] ++ fragment(E), as in v2 §4, which I checked.
  - R steps: one cell each, over U.
  - KB steps: kbcert. It did produce R7 certificates for R1, R2 and R3 (199 / 325 / 2,364 cells, L0-checked in the registry vetting).
- **D steps are the gap.** A D step has only a reproduction record unless its loop is certified. Then the residual is **not L0-cert**, and under the success metrics it cannot be a candidate.
  - Recommendation: accept an in-loop D step only if kbcert certifies its loop w_i u_i⁻¹. Otherwise skip the step, or reject the word.
  - In the T-027 data, kbmag reduced all 16 D-step loops, so certification may often be possible.
- §6's point stands: distillation adds nothing when the in-loop solvers cannot act on W. The probe shows that R **does** act on random-substitution W (median ρ 0.8–0.87), which partly scrambles the blocks. That interacts with the recovery attack and should be measured.

## 4. Pilot: arms, falsifiers and held-out list

**Arms (§6b revised).** C′ with K ∈ {1, 3, 5}, × rounds ∈ {1, 2} at matched |W|, plus the B feasibility probe. The CTRL arm is unchanged. Still to pin:
- the t-source per arm: kbcert-certified dataset words, or laws;
- how m and rounds map to matched |W|;
- seeds, the number of (x, y) pairs per t, and the conjugator sampling (best of K, by which score);
- whether W must be 2.5-reduced before distillation.

**Falsifiers: well defined in intent, but each needs pinning.**
- **F1** ("the in-loop chain empties ≥ 90 % at every m ≥ 8"): per arm or pooled? Is a word that stopped at a cap counted as emptied?
- **F2** ("held-out solvers break ≥ 90 % of the S2-chain residuals in < 1 s"):
  - define "break" (TRUE only, or also SHORTER);
  - set a minimum denominator, since F2 is undefined if few residuals reach S2-chain;
  - state the time as CPU-s on a named machine.
- **F3** ("no solver's minimum budget grows across m"): give a test. For example, the median minimum budget is non-decreasing over the ladder and strictly larger at the top value of m than at the bottom, with censoring at the cap. The §3 success criterion ("polynomial of degree ≥ 2 or exponential") cannot be decided from 4 values of m. Pre-register a fit rule, or drop the model claim.
- **F4** (the iterated recovery attack): define success. For example: the attack outputs (φ′, t′) with φ′(t′) = W verified, and t′ is then solved by kbmag. Recovering the exact x and y is not required, since any Nielsen-equivalent pair works.
- **B probe** (drop B if the yield is < 1 %): define the patch sampler and the denominator.
- **CTRL:** make it a theorem-backed control by checking C′(1/6) per instance. Pieces between different cells must be < 5|u|/6. Under C′(1/6), Greendlinger's lemma guarantees that R empties every such word, so anything below 100 % flags a harness bug.

**In-loop and held-out lists.**
- The two lists are disjoint as procedures, but they overlap in substance:
  - held-out D at rml 7–9 runs the same stages 1–3 as in-loop D(20M, ≤ 3);
  - the S_std gate (KB in certify mode, D1, DR) is used for **selection**, so S_std is effectively in-loop and must not count as held-out evidence;
  - DV over R_KB uses the in-loop KB vocabulary.
- **Overfitting risk.** The in-loop selection statistic for C′ is the grammar-compression ratio, and the held-out recovery attack starts with compression-based segmentation. Selecting on compression directly targets the attack's first stage, which is against the spirit of "no statistic used for selection may be the output of a held-out solver". Either hold out a different segmentation method, or report the attack with and without that stage.
- **Tuned solvers (6b.4)** are correct to add. Note that tcgraph has no HLT or randomised-rotation strategy; tuned TC needs ACE or GAP's ACE package, or new code. That cost is not in the estimate.

**Cost: underestimated.**
- K = 5 × m = 32 × |t| ≈ 65 gives |W| ≈ 10⁴ letters before cancellation. R scales roughly as n³ (seconds at 10³ letters), so it takes hours per word at 10⁴ letters. My probe took about 3 s per word on average over m ≤ 16 (|W| up to about 1.3·10³). Cap |W| or budget for this.
- The D ladder "2^20–2^27 locally" does not fit the 2 GB cap. D at 20M used 1.1 GB, so 2^25 ≈ 33.5M is the local limit, and 2^26–2^27 need an rjob plan.
- kbcert on long KB steps is the stated cost risk.
- The tuned-TC implementation is not costed.

## 5. Other points

- **§6, B: the half-exposure lemma has the wrong sign.** Gluing a u⁵ cell along a shared arc of length s changes the length by 5|u| − 2s. On a 2.5-reduced boundary s ≤ 2.5|u|, so this is **≥ 0**: gluing never *shortens*.
  - The real constraint is different. The new boundary exposes 5|u| − s ≥ 2.5|u| of u⁵, which is a window of exponent ≥ 2.5, so R undoes the step unless further cells cover the exposure.
  - So "growth needs multi-cell patches" holds, for that reason.
  - "Removing a patch must pass through a lengthening first cell" needs strict power-freeness; with exact halves, the first cell can be length-neutral.
- **The Hall–Petresco certificate.** From x⁵y⁵ = (xy)⁵ c₂^{10} c₃^{10} c₄^{5} c₅, with the c_i taken as explicit words making this hold in F, c₅ is a product of **6** fifth-power cells: x⁵, y⁵, (xy)⁵, (c₂²)⁵, (c₃²)⁵, c₄⁵. "About 3 U-cells" is too low. The Researcher should confirm the explicit c_i.
- **Olshanskii's caveat** (6b.2) is correctly folded in. Long peaks target rewriting solvers only, and hardness against D or tuned TC stays empirical.

## Recommendation

1. Return the proposal to Math Expert for these fixes:
   - name the U_{7m} table and the L0 tooling change for C, C′ and C′-r;
   - correct the half-exposure sign and restate the patch constraint;
   - restate the C′ claim as an attack property;
   - change the Hall–Petresco count to 6 cells (Researcher to confirm);
   - weaken the onion e = 0 claim to "e_V ≤ 2·junction cancellation, argued";
   - remove U2 as a bound until it is proved;
   - mark the D tube claim as conjectured;
   - pin the falsifiers, arms and seeds;
   - re-estimate the cost, and move coset bounds above 2^25 to rjob.
2. The lemma e_U ≥ 1 and the C-family soundness need no further math check before a pilot.
3. Not checked:
   - the B patch feasibility;
   - the literature claims themselves (Researcher);
   - the pool and code of any implementation (none exists yet).
