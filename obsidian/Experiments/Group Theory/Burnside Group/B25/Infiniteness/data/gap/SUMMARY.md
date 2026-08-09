# B(2,5)-infiniteness GAP session — SUMMARY

Date: 2026-07-31. GAP 4.15.1 (`/opt/homebrew/bin/gap`), run non-interactively as `gap -q -b <file.g>`.
All scripts/logs in this directory. Every claim below is backed by literal GAP output (pasted verbatim; long lines in `.out` files carry GAP's `\`-continuation, unwrapped copies in `04_candidates_unwrapped.out` / `candidates.txt`).

## 1. Package availability (`01_packages.g` -> `01_packages.out`)

```
PKG anupq : true
PKG nq : true
PKG lpres : true
PKG ace : true
PKG kbmag : true
GAP version: 4.15.1
```

All five relevant packages load. anupq used for everything below.

## 2. R(2,5) (`02_r25.g` -> `02_r25.out`)

`Q := Pq(FreeGroup(2) : Prime := 5, Exponent := 5)` — instantaneous (9 ms).

```
Size(Q) = 582076609134674072265625
Size = 5^34
NilpotencyClass = 12
LCS length (num subgroups) = 13
LCS layer 1 : order 5^2
LCS layer 2 : order 5^1
LCS layer 3 : order 5^2
LCS layer 4 : order 5^3
LCS layer 5 : order 5^2
LCS layer 6 : order 5^4
LCS layer 7 : order 5^4
LCS layer 8 : order 5^4
LCS layer 9 : order 5^6
LCS layer 10 : order 5^3
LCS layer 11 : order 5^2
LCS layer 12 : order 5^1
```

- **Order 5^34 CONFIRMED** (582076609134674072265625).
- LCS layer ranks: **2,1,2,3,2,4,4,4,6,3,2,1** (sum = 34).
- p-central series (p=5) is layer-for-layer identical to the LCS (expected: in an exponent-5 group all 5th powers vanish, so the lower 5-central series collapses onto the LCS). Literal output in `02_r25.out`.
- Cross-check with prior project results (GAP-verified 2026-06-26): dim(gamma5/gamma6)=2 and first 6-dim layer at weight 9 — both match.

### DISCREPANCY vs. task premise: nilpotency class is 12, not 13

The task brief said "nilpotency class 13". GAP says **class 12**, verified three independent ways (`03_phi_sanity.out`):

1. `NilpotencyClass = 12`, `Length(lcs) = 13` with `last term trivial: true` (i.e. gamma_13 = 1).
2. Exhaustive scan of ALL 2^13 = 8192 left-normed commutators [x1,...,x13], xi in {a,b}:
```
weight 12: #left-normed = 4096, #nontrivial = 252
weight 13: #left-normed = 8192, #nontrivial = 0
```
Since left-normed generator commutators of weight 13 generate gamma_13 mod gamma_14, all-trivial => gamma_13 = 1.
3. Direct subgroup computation:
```
Size(gamma_12) = 5^1
Size([gamma_12, Q]) = 1 (1 means class 12 exactly)
```

Consequence: **the first layer R(2,5) cannot see is weight 13**, not 14. Candidate lists below include both weight-13 words (already invisible to R(2,5), and shorter) and weight-14 words (safe under either class convention, as requested).

## 3. Epimorphism and word evaluator (`03_phi_sanity.g` -> `03_phi_sanity.out`)

`phi := PqEpimorphism(F : Prime := 5, Exponent := 5)`, image size 5^34. Word->R(2,5) evaluator `EvalWord` over alphabet a,b,A,B (A=a^-1, B=b^-1). Sanity:

```
[a,b] nontrivial in R(2,5): true
EvalWord ABab ([a,b]) nontrivial: true
EvalWord a^5 trivial: true
```

## 4. Kernel-candidate search (`04_candidates.g` -> `04_candidates.out`, re-verified by `06_verify_candidates.g` -> `06_verify_candidates.out`)

Family used: near-balanced commutator trees over leaves {a,b,a^-1,b^-1} of total LCS-weight 13 and 14. Any such word lies in gamma_w(F) with w >= 13 > class(R(2,5)) = 12, hence is trivial in R(2,5); it is NOT visibly a product of 5th powers (it is an iterated commutator). 6000 random trees per weight, freely reduced, deduped up to inversion, ranked by reduced length.

Balanced trees are what makes these short: a left-normed weight-14 commutator is ~24,574 letters; the balanced-tree optimum is ~208 letters pre-cancellation, and free cancellation across bracket junctions brings the best found to **110 (weight 14)** and **96 (weight 13)**.

Verification per word (all literal in the .out files): free-reduced length; abelianization = [0,0]; image under phi trivial in R(2,5). Example line:

```
W14-1 len=110 abel=[ 0, 0 ] trivial_in_R=true
```

End-to-end re-check of the exact unwrapped strings in `candidates.txt` (independent GAP run, letter-by-letter evaluator):

```
candidates.txt verification: 20 OK, 0 BAD
```

### Ranked list — 20 words trivial in R(2,5) (candidates for ker(B(2,5) -> R(2,5)))

Weight 14 (as requested, prioritized):

| id | len | word |
|----|-----|------|
| W14-1 | 110 | aBAbabABBabAbbaBABabABaBAbbaBABabAbabABBBabAbaBBAbabABaBAbbaBABabbAbaBABaBAbabABBabAbaBAbabABaBABabbABaBAbbaBA |
| W14-2 | 110 | aBAbabABBabAbaBAbaBABabbABaBAbbABAbaBaBabAbaBAAbABabaBaBAbabABabABaBAbbaBABabABabAbaBAbABAbaBaabABaBAbAbABabaB |
| W14-3 | 112 | ABabaBAAbaBabAABaabABAbaaBAbABabbABaBAbbaBBAbabABBabAbaBBabAABabaBAAbaaBAbABaabABAbabABaBAbbaBABabbABBabAbaBBAba |
| W14-4 | 112 | aBAbABaabABAbabABaBAbbaBABabaBAbabABABabAbaBBAbabABabaBABabAABabaBAAbaabABAbaBABabbABaBAbabaBABabABAbabABBabAbaB |
| W14-5 | 114 | BabAbaBBAbabABaBAbbaBABabbAABabaBAAbaBabABabABAbaaBAbABabaBBAbabABBabAbaBABabbABaBAbAbaBabAABabaBAbaBAbABaabABAbaB |
| W14-6 | 118 | aBAbABaabABAbabaBAABabaBAAbaBabbAABaBAbaBABabbAbaBABaBAbabbaBBAbABaabABAbaabABABabaBAAbaBabABABabAbabABaBBAbabABabAbaB |
| W14-7 | 120 | aBAAbaBabABabABAbaaBAbABabABabbABabaBAAbaBabABabABAbaaBAbABaBAbaBAbaBabAABabaBAbaBAbABaabAAbaBabAABabaBAbaBAbABaabABAbaB |
| W14-8 | 120 | BabABAbaBabAABaabABAbaaBAbABabaBAbaBAbbaBABabABabAbaBBAbabABabABBabABAbaBabAABabaBAAbaaBAbABabbaBAbaBABabbABaBAbaBAbabAB |
| W14-9 | 122 | BAbabABBabbaBAbABaBAbbaBABababABAbaBabAABabaBAbaBAbABaabABAbaaBABAbabABBabAbaBabABBAbbaBABabbABabABabaBAAbaBabABabABAbaaBA |
| W14-10 | 122 | AbaBabAABabaBABAbabABaabABAbaaBABabAABaabABAbaaBAbABabaBAAbaabAABabaBAAbaBABababABAbaaBAbABaBabABAbaBabAABabaBAAbaaBAbABab |
| W14-11 | 122 | BAbabABBabAbaBaBAbbABaBAbbaBABaabbABAbaBabAABabaBAAbaaBAbABaaBAAbabABBabAbaBBabAbABaBAbbaBABabAbaBabAABaabABAbaaBAbABabaBA |
| W14-12 | 122 | AbaBABabbABaBAbaBAbabABBabAbaaBAbABaBAbaabABaBAbABabAbaBBabAbABaBAbbaBABabABabAbaBBAbabABaaBAbbABaBAbaBabAbaBAABabAbaBabAB |

Weight 13 (already invisible to R(2,5) since class = 12; shorter witnesses):

| id | len | word |
|----|-----|------|
| W13-1 | 96 | AbaaBAbABabABabaBAAbaBabABabABabABAbaaBAbABabaBAAbaBabAABabaBAbaBAbABaabABAbaBabABAbaBabAABabaBA |
| W13-2 | 100 | BAbABababABaBAAbaBabbABabAbaBBABabAbabABaBBAbaBAbABaabAbaBABAbaBabbABabAbaBABaBAbabbABaBAbaBABabAbaB |
| W13-3 | 100 | ABabAbaBBAbabABaabABAbaaBAbABBabAbaBBAbaabAABabaBAAbaBABabbABaBAbaabABAbaaBAABabbABaBAbbaBabAABabaBA |
| W13-4 | 100 | BAbaBabAABabaBAbaBAbABaabABAbabABAbaBabAABabaBAbaBABabaBAAbaBabABabABAbaaBAbABabbABabABAbaaBAbABabaB |
| W13-5 | 100 | AbaBABabbABaBAbaBAbabABBaBAbabABabAbaBBABabAbabABaBAbbaBABabABabAbaBBAbabABBaBAbabbABaBAbaBABabbAbaB |
| W13-6 | 100 | BabaBAbbABaBAbaBabAAbaBBABabbABaBAbabABBabAbaBBAbbabABaaBAbABabAbaBBabABABabbABaBAbbaBABabAbaBBAbabA |
| W13-7 | 102 | ABabABAbaaBAbABababABaBAAbaBabAABabbaBabABAbaaBAbABabABBAbaaBAbABaabAbaBABAbaBabAABabaBAbbaBabAABabaBA |
| W13-8 | 104 | BAbaBabAABabaBAAbaaBAbABaabAbaBAbABaBAbaBabAAbaBabABaBAbABabaBAAbaBabAABaabABAbabaBAbABaaBAbABabAbaBabAB |

Machine-readable copy: `candidates.txt` (tag TAB length TAB word).

Caveats (honest limits of what was verified):
- Each word is verified nontrivial in the FREE group (nonempty free reduction) and structurally lies in gamma_w(F); its nonzero component in gamma_w/gamma_{w+1} of the free group mod 5 was NOT verified (the free class-14 5-quotient has order ~5^2538 — out of scope here). A word could conceivably sit even deeper in the LCS; that only makes it a better-hidden kernel candidate, not a wrong one.
- Whether any of these is nontrivial in B(2,5) is exactly the open infiniteness question — later stages' job, per brief.
- "Commutators of 5th-power conjugates" family was deliberately dropped: any word in the normal closure of 5th powers is trivial in B(2,5) itself, hence useless as a kernel witness.

## 5. Sanity cross-checks (`03_phi_sanity.out`, `04_candidates.out`)

- `[a,b] nontrivial in R(2,5): true`
- Task asked to exhibit a surviving weight-13 commutator (premised on class 13). **Not possible: all 8192 weight-13 left-normed commutators are trivial** (literal output above). Instead the top nontrivial layer is exhibited at weight 12:
```
weight 12: #left-normed = 4096, #nontrivial = 252
surviving weight-12 left-normed commutator [abaababaabbb] (letters = entry sequence) is NONTRIVIAL in R(2,5)
```
(i.e. the left-normed commutator [a,b,a,a,b,a,b,a,a,b,b,b] != 1 in R(2,5); gamma_12 has rank 1.)
- Negative control for the candidate pipeline — a same-shape balanced weight-12 tree that does NOT die in R(2,5) (proves the generator is not trivially collapsing everything):
```
CONTROL weight-12 balanced commutator NONTRIVIAL in R(2,5): len=146
BabABaBAbbabABBBabAbaBAbbaBAbaBABabaBAbabABABAbaBabbaBABabABAbabABaBAbABababABBabABaBAbbbaBABBabAbaBAAbaBabAbaBABabaBAbabABBAbABababaBABabABAbabAB
```

## 6. Calibration (`05_calibration.g` -> `05_calibration.out`)

```
B(2,3): order = 27 = 3^3, class = 2
B(2,4): order = 4096 = 2^12, class = 5
B(2,4) order = 4096: true
```

Both match the known values |B(2,3)| = 27 (the brief's uncertainty resolved: yes, 27, class 2) and |B(2,4)| = 2^12 = 4096 (class 5). Pipeline calibrated.

## File index

| file | role |
|------|------|
| 01_packages.g/.out | package detection |
| 02_r25.g/.out | R(2,5) order + LCS/p-central layers |
| 03_phi_sanity.g/.out | epimorphism, evaluator, class-12 proof, weight-12 survivor |
| 04_candidates.g/.out | candidate generation + verification + control |
| 04_candidates_unwrapped.out | same, GAP line-continuations removed |
| 05_calibration.g/.out | B(2,3), B(2,4) |
| 06_verify_candidates.g/.out | independent re-verification of candidates.txt strings |
| candidates.txt | 20 ranked kernel-candidate words (machine-readable) |
