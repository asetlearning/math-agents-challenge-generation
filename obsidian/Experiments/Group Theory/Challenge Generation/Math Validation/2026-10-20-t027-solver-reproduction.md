---
type: validation-verdict
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-027: independent reproduction of the owner's solver chain (R, D) on the 12 T-024 confirmed words; soundness of the chain; B0(2,5) and kbmag checks"
verdict: "REPRODUCED. All 12 length chains equal the owner's, step for step. 8 words go to the empty word. ds94 and ds764 end at the identical string T024_R1 (exact, not just up to rotation). ds665 ends at T024_R2 exactly, and ds519 L3 at the owner's 251-letter word exactly; the 251 -> 249 step at 1e9/rml 9 was not run. Every one of the 16 D shortenings is an equality in G_3 = <a,b | v^5, |v| <= 3>, thrown at the end of relator stage 3 below the coset bound. R steps are conjugacies, not equalities, so the owner's 'each step preserves equality' is wrong for R, though 'residual trivial iff original trivial' holds. B0: all 43 words trivial (necessary only). NEW: both existing kbmag systems (rec, slx; they regenerate identically from b25_full) reduce all 12 originals, all 16 D-step loops, all 36 intermediates and all 4 residuals (R1, R2, R3 249, and the 251-letter word) to IdWord, which proves them trivial in B(2,5). Total under 1 s; 0/13 negative controls reduce."
---
# T-027: reproduction of the owner's solver test

This is a Lead request (2026-10-20). Triage: [[2026-10-20-t027-solver-reproduction-triage]].

**Private data.** The owner's materials (`shared/t-024-challenge-test/`) were read in place and not copied. The 12 words are private, so this note gives lengths and hashes only. Every intermediate word, the per-step records, the B0 and kbmag CSVs, and my two scripts are in `Agents/asetlearning/Validator/t027/`, which is gitignored. The chain JSON is `t027-chain-2026-10-20.json`, sha256 prefix `ae5e929e…`.

**Terms.**
- **R** = `greedy_reduce_cyclic_exhaustive2_5`.
- **D(bound, rml)** = `attempt_to_decide_if_trivial(word, coset_bound, relator_max_length)`.
- **G_k** = ⟨a, b | v⁵, v cyclically reduced, 1 ≤ |v| ≤ k⟩. Every G_k maps onto B(2,5).
- **Stage k of D** = the k-th call of `completeWith`. It sews the cumulative relator set of G_k.

## Setup

- **Code.** b25 main `d1b5d0f`, with the tcgraph pin `63564c3`. Both were exported clean (`git archive`) into my scratchpad, and only `tcgraph_ext` was built: Release, under capjob with 2 GB / 2 CPUs.
- **Owner's code.** The owner used tcgraph `26f4f5a`, an ancestor of `63564c3`.
  - Between the two, `include/tc_graph.h` is unchanged.
  - `src/word_problem.cpp` only moves the relator builder into `buildStandardRelators`. It now uses `(v^5).cyclicallyReduce()` instead of `.reduce()`, which is the same word for cyclically reduced v.
  - `greedy_reduction.cpp` changed (T-026 consolidation), and so did `word.cpp` / `word.h` (121 lines added). `src/tc_graph.cpp` and `enumerate_words.h` are unchanged.
  - So D's call path is unchanged. The outputs reproduce exactly, and that is the real evidence.
- **Driver.** My own `chain.py`, which follows the owner's logic:
  - R on the original;
  - then D(20M, 5) → R, until the empty word, a verdict, or 50 rounds;
  - D(20M, 7) once on each residual (the owner's step 6).
- **What the driver checks and records.**
  - It parses the shortened word from the binding's `… | word: <ints>` text, and asserts that the word is non-empty or legitimately empty, freely reduced, and strictly shorter.
  - For each D output it finds the **stage**: the smallest rml at which D throws the same word. D is deterministic and runs its stages in sequence, so D(rml = k) is exactly the first k stages of D(rml = 5).
- **Run.** capjob 2 GB / 2 CPUs, 4 min 32 s wall, 1.1 GB peak RSS. Python was run with `-I -S` from a clean directory, never from `shared/`.

## 1. Chain results

| check | result |
|---|---|
| input file (sha256 `cd1ae09d…1c17be`): certificate replay (owner's method: product of c⁻¹·rel·c, freely reduced) = stored word | 12/12 |
| the 12 words = the T-017 staged words that I verified earlier (`words11` and `l3word`) | 12/12, letter for letter |
| abelianization trivial, freely reduced | 12/12 |
| length chain = the owner's (original → D → R → …) | **12/12** (ds519 to 251, see below) |
| 8 words reach the empty word (ds125, ds145, ds160, ds368, ds512, ds547, ds566, ds781), each after one D and one R | **confirmed** |
| ds94 → T024_R1 and ds764 → T024_R1 | **exact equality** of the two residuals, and both equal the owner's R1 string exactly |
| ds665 → T024_R2 | exact |
| ds519 L3 at D(20M, 5) | 1548 → 1301 → 370 → 355 → 258 → 253 → **251**, exactly the owner's `t024_iterate.json` final word |
| D(20M, 7) on the 4 residual lineages | undecided, no change (as the owner found) |
| T024_R3 (249) | **not reproduced.** It needs D(1e9, 9), which does not fit the local cap. As cyclic words, R3 and my 251-letter word are not related by rotation or inversion |

**Length chains** (all equal to the owner's):

| word | chain | D stages |
|---|---|---|
| ds125 | 163 → 136 → 0 | 3 |
| ds368 | 211 → 192 → 0 | 3 |
| ds160 | 261 → 202 → 0 | 3 |
| ds566 | 320 → 254 → 0 | 3 |
| ds145 | 361 → 296 → 0 | 3 |
| ds512 | 378 → 321 → 0 | 3 |
| ds781 | 529 → 447 → 0 | 3 |
| ds547 | 699 → 588 → 0 | 3 |
| ds94 | 216 → 188 → 75 → 73 → 47 | 3, 3 |
| ds764 | 635 → 556 → 136 → 135 → 47 | 3, 3 |
| ds665 | 405 → 339 → 47 | 3 |
| ds519 L3 | 1548 → 1301 → 370 → 355 → 258 → 253 → 251 | 3, 3, 3 |

**Residual hashes** (sha256 prefix of the letter string):
- R1 = `5082fb21…`, from both ds94 and ds764;
- R2 = `a61d770b…`;
- the ds519 251-letter word = `c4826b7e…`;
- the owner's R3 (249) = `fdde2a7a…`.

**Small corrections to the owner's note.**
- "R on the originals: no change". This holds for **length**. For 5 of the 12 words (ds160, ds512, ds566, ds781 and ds519 L3), R returns a different word of the same length, and that word is not a rotation of the original. These are length-neutral rewrites: R allows the exponent p = 2.5. The owner's chains record lengths, so they are unaffected.
- "D raised ShorterLengthFound within 0.5 s". Confirmed: every shortening came after about 30 ms.
- "The 20M table fills during the |v| = 4 stage". This is true only of the **undecided** calls on the residuals. No shortening came from a full table (see §2).

## 2. Soundness of the chain (from the source at tcgraph `63564c3`)

**D.** `attemptToDecideIfTrivial_in_B_2_5` (`src/word_problem.cpp`) works as follows.
- It builds a fresh `TCGraph<2>` and lays a path labelled w from the root. There are **no subgroup generators**, so this is coset enumeration over the trivial subgroup.
- Stage i (i = 1 … rml) calls `completeWith` with `buildStandardRelators(i)`: all v⁵ for cyclically reduced v with 1 ≤ |v| ≤ i. The set is cumulative.
- The graph changes only in two ways, so the label of any path from the root to a vertex is the same element of G_k at stage k:
  - `addCycleAt`, which sews a relator cycle at a vertex;
  - `identifyVertices`, which folds edges that are forced.
- `track_word_length` → `get_min_word` traces w from the root (folding maps paths to paths, so the trace completes) and takes a BFS geodesic u from the root to the end vertex. If |u| < |w|, it throws `ShorterLengthFound(u)`.

**Guarantee.** ShorterLengthFound(u) certifies **u = w as elements of G_k**, where k is the stage being run when it was thrown, and hence u = w in B(2,5). This is **equality**, not conjugacy.

**When the check runs.** `completeWith` calls `track_word_length`:
- at the end of every stage;
- when the table reaches `coset_bound`;
- every `len_log_step` (10⁸) iterations.

So the check is not made only at the bound. In this run, **all 16 D shortenings were thrown at the end of stage 3**, below the bound. None follows a "Max coset reached" log line, and each was reproduced at rml = 3 and not at rml = 2. So every D step here is an equality in **G_3**.

**D's other outputs.**
- `true` means w = 1 in G_k.
- `false` (a full pass made no change, so the graph is finite and closed) proves w ≠ 1 in **G_k only**. It does not prove w ≠ 1 in B(2,5). No `false` occurred.

**R.** `greedyReduceCyclic` (`greedy_reduction.h`) applies `greedyReduce` to cyclic permutations of the word and keeps the shortest result. The rewrite is u^p → u^{-(5-p)} for 2.5 ≤ p < 5, where u is the minimal period of a square in the word, of any length. So:
- each R step returns a word **conjugate** to its input in G_m, where m is the longest period used, and therefore conjugate in B(2,5);
- the rewrite part is an equality in G_m, but m is not bounded by 7.

**What the dataset can say.**
- Each residual is conjugate in B(2,5) to its original, so the residual is trivial iff the original is.
- The owner's "each step preserves equality in B(2,5)" is wrong for R: R gives conjugacy.
- Since the 12 originals have verified certificates, **every intermediate word and every residual is trivial in B(2,5)**. "Undecided" measures D's strength, not the word's status.

## 3. B0(2,5)

- **Method.** The existing `b0_challenge_triviality.g` (copied unchanged), with anupq `PqEpimorphism` at class 12. The checks came out as expected:
  - order 5^34, class 12, generated by the images, exponent 5 on the pcgs;
  - p-central sizes as in the 2026-10-07 run;
  - the 5 controls behave correctly: a⁵ and (ab)⁵ trivial; [a,b], a and a⁴ not.
- **Words: 43 in total:**
  - the 4 originals (ds94, ds764, ds665, ds519 L3);
  - every stored intermediate of all 12 chains (36 words);
  - the owner's R1, R2 and R3.
- **Result: all 43 are trivial in B0(2,5).** capjob 2 GB / 1 CPU, 2.7 s.
- **Necessary condition only.** It is the expected outcome, because all these words are trivial in B(2,5) (§2). A NONTRIVIAL result would have exposed a bug.

## 4. kbmag

- **Method.** `kb_reduce_words.py` with `wordreduce -kbprog`, using the kb-verify-20261007 systems:
  - `rec` (recursive ordering, 97,484 rules) and `slx` (shortlex, 99,948 rules);
  - `b25_full`: sha256 `b1d511fe…`, generators `[a, A, b, B]`.
- **Validity.** Every kbprog rule is a consequence of b25_full's relators v^{5k}, |v| ≤ 7, so the rules hold in G_7 whether or not the system is confluent. Reduction to IdWord therefore **proves w = 1 in G_7**, and hence in B(2,5).

| words | rec | slx |
|---|---|---|
| the 3 residuals, plus the 251-letter ds519 word | **4/4 IdWord** | **4/4 IdWord** |
| the 12 originals | **12/12 IdWord** | **12/12 IdWord** |
| the 36 chain intermediates | 36/36 | 36/36 |
| negative controls: each residual with one letter inverted, plus a, ab, abAB, aabAB, ababABAB, plus each residual with its last 2 letters deleted | 0/13 | 0/13 |

- **Reproducible from the presentation alone.** I regenerated both systems with `kbprog -me 100000` on copies of `rec` and `slx` (b25_full, `b1d511fe…`). This took 10.2 s and 1.9 s and halted at 97,483 and 99,947 equations, as in the provenance.
  - The regenerated `.kbprog` files are byte-identical to the stored ones once the `maxeqns := 2000000` line is added. The stored files carry that line so that `wordreduce` can load them; without it, loading fails with 'Too many equations'.
- **D steps proved independently.** All 16 D-step loops w_i · u_i⁻¹ (148–2,849 letters) reduce to IdWord under both rec and slx. So every D step is an independently proved equality in G_7, not only an equality read off the source.
- **Cost.** All 12 originals take 0.44 s (rec) and 0.27 s (slx), including the rule load, at under 50 MB RSS.
- **Consequence for T-027.** The existing kbmag systems break every T-024 word, original or residual, in well under a second. The residuals, including the 249- and 251-letter ds519 words, are **trivial in G_7**. So the T-024 words are not resilient to kbmag (Math Expert's B8).
- This agrees with Math Expert's §0.4: the tiles are kbprog rule words. I did not test whether that is the mechanism.

## Scope

- **Reproduced:** the owner's chain up to D(20M, 5/7) on the current main.
- **Not reproduced:** D(200M, 5) and D(1e9, 9), so neither T024_R3 nor the owner's 1e9 timings.
- B0 is a necessary condition only.
- The kbmag results are proofs of triviality in G_7. They are not statements about the cost or resilience of any other breaker.
