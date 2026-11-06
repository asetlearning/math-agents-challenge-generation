---
type: validation
date: 2026-11-04
author: Validator (asetlearning)
project: "[[project-b25-solver]]"
subject: "I1-invariant-review: H_6 charge chi_6 (M3), integral exponent sums (M4), mod-5 degree-5 Magnus layer (M5)"
status: verified
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, project/b25-solver, status/verified]
---
# I1 check: chi_6 charge and Magnus claims

Triage: [[2026-11-04-b25-solver-i1-charge-magnus-check-triage]]. Proposal under test: Math Expert, 2026-11-04 (M3, M4, M5). Own code (GAP 4.15.1 `PQuotient`, Python Z_5 Magnus), run under capjob 2G / 2 CPUs. Scope: what each claim says about the **finite quotients and Magnus coefficients named**. None of this is a free-group certificate and none is claimed to be.

## Verdicts

| Item | Verdict |
|---|---|
| M3 (chi_6 well defined, additive, conjugation-invariant, 0 on period <= 6) | **CONFIRMED**, 3 caveats below |
| M3 images (automorphisms and inversion act on K_6 by a unit) | **CONFIRMED**, stronger than stated: the 8 letter automorphisms act by **1**, inversion by **-1** |
| M4 (e = 5 sum +-l(v_i); #cells >= ||e||_1/(5k)) | **CONFIRMED** |
| M5 (degree-5 layer mod 5 = +-l(v)^5, conjugation-invariant) | **CONFIRMED** for degree 5 only; degree 6 is **not** conjugation-invariant |

**Usable for E1-charge-census: yes**, under the three caveats (C1-C3).

## 1. M3 (GAP, own presentations)

- G_k relators: one fifth power per cyclic class (up to rotation and inversion) of cyclically reduced words of length <= k. k=6: 117 relators; k=7: 275.
- H_6 = `PQuotient(G_6, 5)`: order **5^35**. H_7 = `PQuotient(G_7, 5)`: order **5^34**. Both match Phase 0 ([[2026-10-23-t028-phase0-ladder-review]]).
- The map H_6 -> H_7 on the generator images is well defined and surjective. Kernel **K_6 has order 5 and lies in the centre** of H_6. The centre of H_6 has order 5^2.
- H_7 = R(2,5): R(2,5) is a 2-generated 5-group satisfying all G_7 relators, so it is a quotient of H_7; its order 5^34 (published value, **GK**, not re-derived here) equals |H_7|, so H_7 = R(2,5). Supporting evidence: 300 random elements of H_7 all have x^5 = 1; all 434 registry words (word and W, below) land in K_6, as they must if H_7 is a quotient of B(2,5).
- Random cells g v^{+-5} g^-1 (v random reduced, conjugator length 0..12):
  - period <= 6: chi_6 != 0 in **0 / 240**;
  - period 7 / 8 / 9 / 10: chi_6 != 0 in 38 / 57 / 75 / 96 of 200 each; every cell image lies in K_6 (no exceptions);
  - **additivity**: 300 products of 2..7 cells (periods 7..10, conjugators 0..15 long, free-reduced as one word): chi_6(product) = sum of chi_6(cells) in **300 / 300**; 210 of the products have chi_6 != 0; each product is trivial in H_7 (300 / 300); conjugating the product by a random word leaves chi_6 unchanged (300 / 300).
- **Images.** Each of the 8 letter automorphisms (swap x signs): on 60 random cells each, chi_6(phi(c)) = 1 * chi_6(c), chi_6 = 0 preserved. Inversion: chi_6(c^-1) = -chi_6(c). On all 207 registry candidate words, none of the 8 automorphisms changes chi_6, and inversion negates it (0 exceptions). So **chi_6 != 0 is image-invariant over all 16 images**, and the "compute per image" cost in the proposal is not needed.

### Caveats on M3
- **C1: K_6 is not one pc generator.** In my presentation the generating element z of K_6 has non-zero exponents at pc positions 30 and 35 (of 35); the last pc generator is central but **not** in K_6. Use the kernel (log of the element in K_6, found via the map to H_7), not "the exponent of the last pc generator". For elements already known to lie in K_6 the exponent at one fixed pc position is proportional to chi_6, so a zero / non-zero census is presentation independent; the **value** of chi_6 depends on the choice of generator z (a unit multiple), so compare **zero versus non-zero** across implementations, not the values.
- **C2: chi_6 is a property of the exact word, not of its B-class.** Two B-equal words differ in chi_6 by the charge of whatever period >= 7 cells link them. On the registry, chi_6(word) != chi_6(W) for **55 of 227** records (word = the shortened challenge word, W = the construction word; the shortening steps used period >= 7 cells or G_7 equalities). Compute chi_6 on the word actually tested.
- **C3: necessary condition only**, as the proposal says: chi_6(w) != 0 proves every certificate of w contains a cell of period >= 7; chi_6(w) = 0 proves nothing.

### Reference numbers for E1-charge-census (registry rev 3, `word` field, 207 candidates)
chi_6 = 0: **68**; non-zero: **139** (counts 34, 38, 30, 37 for the four non-zero values in my normalization). Per-id values: `Agents/asetlearning/Validator/scratch/i1-chi6-registry-rev3.txt` (ids and numbers, gitignored). The 20 `tested` records are in the same file after the 207. The Experimenter's zero set must match mine exactly; the non-zero values match up to one unit.

## 2. M4 (Python)

- Exponent-sum vector of a free-reduced product of random cells (periods 2..12, conjugators 0..14, 1..8 cells): e = 5 * sum(sign_i * l(v_i)) exactly in **500 / 500**; e divisible by 5 and ||e||_1 <= 5 k #cells (k = max period) in **1000 / 1000**. Free and cyclic reduction preserve e, so the claim carries to q = cycred(w u^-1).
- Registry rev 3, 207 words: e divisible by 5 in 207 / 207; **e != 0 in 203 / 207**, so the degree-1 lower bound is informative on almost every target.
- The area / degree-2 remarks in M4 were not checked (not asked).

## 3. M5 (Python, Z_5 Magnus, degree 6, a -> 1+X, b -> 1+Y)

- 300 random cells (period 2..10, conjugator 0..14, random sign): the Magnus image is 1 in degrees 1-4; the degree-5 part equals sign * l(v)^5 (coefficient of a monomial with i X's: e_a^i e_b^(5-i) mod 5) in **300 / 300**; it is identical to that of the unconjugated cell in 300 / 300; 293 are non-zero (the rest have l(v) = 0 mod 5).
- Degree-5 part of a free-reduced product of 2..6 cells = sum of sign * l(v_i)^5: **100 / 100**.
- The span of the l^5 over F_5^2 has dimension 6 (matches the proposal).
- **Degree 6 is not conjugation-invariant** (differs from the unconjugated cell in 73 / 100). The proposal already says degrees 6..c are coarse; this confirms that only degree 5 is an invariant of the cell.
- Registry rev 3: Magnus degrees 1-4 vanish and the degree-5 part lies in the span of the l^5 for **207 / 207** words (necessary conditions of B-triviality, all hold).

## Not checked
H_k for k <= 5 (M6), the area terms of M4, and the Experimenter's chi_6 numbers (not yet delivered; compare against the reference above). Scratch code stays uncommitted in the Validator scratch area.
