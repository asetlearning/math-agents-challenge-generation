---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/arithmetic
  - project/kourovka
  - status/draft
problem_id: "21.89"
cycle: 1
---

# Problem 21.89 working log

## Active-time ledger

- 2026-08-11T15:49:47Z — work started; cumulative active minutes: 0.
- 2026-08-11T15:56:00Z — source and initial staleness gates completed; cumulative active minutes: 6.

## Staleness check

### Source gate

- Configured source PDF resolved through `_meta/agents/Kourovka/paths.env`.
- Inspected PDF p. 177 both with `pdftotext -layout` and visually from a 160-dpi rendering at `scratch/source-page-177.png`.
- Corrected, source-faithful transcription: **For \(n>39\), is it true that the number of conjugacy classes in the symmetric group \(S_n\) of degree \(n\) is never a divisor of the order of \(S_n\)? In other words, is it true that, for \(n>39\), the number \(p(n)\) of integer partitions of \(n\) is never a divisor of \(n!\)?** (D. MacHale.)
- The problem is unstarred on the rendered current page. It has no editor comment and no later comment in the printed statement.
- `source_transcription_checked: yes`.
- Corpus caveat: the protocol names a No. 21 JSONL corpus, but this vault contains only `kourovka-20-corpus.jsonl`; hence the requested No. 21 `answered`, `has_editor_comment`, and `has_later_comment` machine flags are unavailable. The current rendered No. 21 source itself shows an unstarred problem and no comments. The synthesis records the same status.

### Literature and current-edition search

- Searched the web for exact phrases `"Kourovka" "21.89"` and `"Problem 21.89" "Kourovka Notebook"`; found the current No. 21 statement, but no solution.
- Searched for `"D. MacHale" partition p(n) divides n!` and `partition number p(n) divisor of n! MacHale`.
- Searched arXiv for `"p(n) divides n!" partition` and `partition function factorial divisibility p(n) n!`; found no paper solving the conjecture.
- Checked current Kourovka No. 21, p. 177: problem 21.89 remains unstarred and has no appended answer/comment.
- Found Robert Heffernan and Des MacHale, “The genesis of a conjecture in number theory,” *Irish Math. Soc. Bulletin* 93 (Summer 2024), 39–41, DOI 10.33232/BIMS.0093.39.41. It states the exact conjecture and explicitly says the authors have no proof; it reports exhaustive computation through \(n=2{,}000{,}000\).
- Checked OEIS A046668 (live page, modified 2026-08-10): it lists only \(1,2,3,7,9,10,11,12,14,15,16,17,18,19,20,21,24,28,32,33,39\), reports no later term through \(2{,}000{,}000\), and contains no solution citation.
- Checked OEIS A192885 (live page, modified 2026-08-11): it records the stronger sufficient obstruction “largest prime factor of \(p(n)\) exceeds \(n\)” as observed through \(n=2500\), but not proved generally. Its cited Cilleruelo–Luca result gives only a much weaker almost-all lower bound.
- Conclusion: no evidence that the exact problem is already solved. The problem is current as of this check.

## Statement in my own words

For every integer \(n\ge 40\), decide whether the exact integer \(p(n)\), the coefficient of \(q^n\) in \(\prod_{m\ge1}(1-q^m)^{-1}\), fails to divide \(n!\). Equivalently, for each \(n\ge40\), one must exhibit a prime \(q\) with \(v_q(p(n))>v_q(n!)\). A particularly cheap sufficient obstruction is a prime divisor \(q>n\) of \(p(n)\), but that condition is not necessary.

## Computational reconnaissance

### Commands and observed outputs

- Attempted `python3 Agents/Kourovka/problems/21.89/scratch/check_partition_divisibility.py 1000 | tee Agents/Kourovka/problems/21.89/scratch/check-1000.out`. Observed output: `ModuleNotFoundError: No module named 'sympy'`. I did not install or reimplement a factorization package; GAP 4.12.1 was already available, so I switched to it.
- Sanity check: `gap -q -c 'Print(GAPInfo.Version,"\n"); Print(NrPartitions(40),"\n"); Print(FactorsInt(NrPartitions(40)),"\n"); QUIT;'`. Observed output was GAP `4.12.1`, `37338`, and `[ 2, 3, 7, 7, 127 ]`.
- Two initial GAP runs hung because `FactorsInt(1)` yields the unit factor `1`, and my factorial-valuation loop divided by 1 forever. A diagnostic bounded command printed every index 1 through 100 and `DONE`, isolating the bug to my valuation code rather than GAP factorization. I corrected the script to ignore the unit explicitly. The empty artifacts `check-10000.out` and `check-10000.time` are retained as evidence of the failed run.
- Successful exact run:

  ` /usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' gap -q -c 'limit:=1000;; Read("Agents/Kourovka/problems/21.89/scratch/check_partition_divisibility.g"); QUIT;' > Agents/Kourovka/problems/21.89/scratch/check-1000.out 2> Agents/Kourovka/problems/21.89/scratch/check-1000.time`

  Observed summary: GAP 4.12.1; limit 1000; the complete divisor list was `[1,2,3,7,9,10,11,12,14,15,16,17,18,19,20,21,24,28,32,33,39]`; all 961 integers from 40 through 1000 were obstructed by a prime factor of `p(n)` larger than `n`; zero required a valuation-only obstruction. Elapsed 9.61 s, maximum RSS 142208 KB. Full output is in `scratch/check-1000.out`; exact script is `scratch/check_partition_divisibility.g`.

### What the computation establishes

The exact GAP objects were the integers `NrPartitions(n)` for every integer `1<=n<=1000`, factored with `FactorsInt`, and compared prime-by-prime with Legendre's exact valuation of `n!`. Thus it establishes the target assertion for `40<=n<=1000` and independently reproduces the listed solutions through 39 in that finite interval.

It does **not** establish any case above 1000, any general theorem, or that the stronger property `P^+(p(n))>n` must continue. The published/OEIS coverage through 2,000,000 is external evidence rather than output reproduced in this run.

## Reduction and bottleneck

Let `P^+(m)` be the largest prime factor of `m`. If `P^+(p(n))>n`, then that prime does not divide `n!`, so `p(n)∤n!`. Hence the conjecture `P^+(p(n))>n` for all `n>39` is a clean sufficient reduction. It is strictly stronger than the target: target failure of divisibility may instead arise from `v_q(p(n))>v_q(n!)` for some `q<=n`.

The strongest directly relevant theorem located, Cilleruelo–Luca (2012), says only `P^+(p(n))>log log n` for a density-one set of `n`. This is far below `n` and does not discharge even an almost-all version of the required valuation obstruction. Current computation suggests the stronger route, but the literature explicitly treats much weaker largest-prime-factor growth as difficult. This is the main theoretical bottleneck.

- 2026-08-11T15:54:50Z — sent an early `QUESTION` to MathExpert asking for a theorem or viable route beyond the largest-prime-factor conjecture; cumulative active minutes: 10.

## Analytic necessary condition for any obstruction

I derived the following elementary reduction. Put `c = pi*sqrt(2/3)`. For every `n>=1`, if `p(n)∤n!`, then there is a prime `q|p(n)` such that

`q/log(q) > sqrt(n)/c = sqrt(3n/2)/pi`.

Proof check:

1. For `t>0`, coefficient positivity in Euler's product gives
   `p(n)e^(-tn) <= product_{m>=1}(1-e^(-tm))^(-1)`.
2. Taking logs and expanding gives
   `log(product) = sum_{r>=1} 1/(r(e^(tr)-1)) < (1/t) sum_{r>=1}1/r^2 = pi^2/(6t)`.
3. Optimizing `tn+pi^2/(6t)` at `t=pi/sqrt(6n)` yields the strict bound `log p(n) < c sqrt(n)`.
4. If `p(n)∤n!`, choose a prime `q` with `a=v_q(p(n))>v_q(n!)`. Since `v_q(n!)>=floor(n/q)`, integrality gives `a>=floor(n/q)+1>n/q`. Hence `log p(n)>=a log q>(n/q)log q`. Combining with step 3 gives the displayed inequality.

This is a genuine narrowing of where a valuation witness can occur, but it does not prove that such a witness exists. Asymptotically it demands a prime factor on the rough scale `sqrt(n) log n`, whereas Cilleruelo–Luca only prove a `log log n` lower bound for almost all `n`. Thus even this necessary consequence of the Kourovka assertion is well beyond the theorem found in the literature.

## Additional near-miss check

- Ran `gap -q -c 'for n in [40..70] do f:=FactorsInt(NrPartitions(n)); Print(n," ",Maximum(f)," ",Float(Maximum(f))/n,"\\n"); od; QUIT;'`. The complete observed table was printed in the terminal; the closest case in that interval was `n=52`, largest prime factor `53`, ratio `1.019230769230769`.
- Extended `scratch/check_partition_divisibility.g` to retain the minimum ratio `P^+(p(n))/n` over its exact range, then reran the exact `1<=n<=1000` computation. Observed final output: `CLOSEST_LARGEST_PRIME_RATIO=rec( n := 52, q := 53 )`; elapsed 9.40 s, maximum RSS 142208 KB. Full output is `scratch/check-1000-rerun.out`.
- This near miss did not suggest a uniform congruence or valuation mechanism. It instead reinforces that the computational phenomenon being observed is the stronger largest-prime-factor conjecture.

## REPORT: DEAD

### Tried and why it failed

1. **Staleness/literature route.** Located the exact 2024 origin article, current OEIS records, current No. 21 statement, and the relevant Cilleruelo–Luca theorem. Nothing located closes the problem. The strongest theorem is quantitatively far too weak.
2. **Counterexample search.** Exact GAP factorization and valuation comparison found no counterexample through 1000. Published external computation already reaches 2,000,000, so extending this light local range is not a meaningful live line.
3. **Largest-prime-factor reduction.** `P^+(p(n))>n` suffices and matches every locally checked `n>=40`, but this is a stronger open-looking assertion; known theory proves only `P^+(p(n))>log log n` on a density-one set.
4. **Size-plus-valuation argument.** The Euler-product bound yields the rigorous necessary witness condition `q/log q > sqrt(3n/2)/pi`. This narrows the obstruction to relatively large primes but supplies no reason such a prime divides `p(n)`.
5. **Partition congruences.** Fixed-modulus Ramanujan-type congruences force divisibility by small fixed primes; for large `n`, `n!` contains far more copies of each such prime than the size of `p(n)` can require. They point in the wrong direction for producing a valuation obstruction.

### Ruled out, and firmness

- Firmly ruled out: any counterexample with `40<=n<=1000`, by exact complete computation.
- Firmly ruled out as a sufficient proof: the located Cilleruelo–Luca theorem, because `log log n < n` and it says nothing about excess valuation in `n!`.
- Strongly disfavored: more bounded brute force, because the existing exact external coverage to 2,000,000 already dominates what a one-hour local run could add.
- Not ruled out: a new modular-form theorem controlling large prime factors or prime-adic valuations of individual partition values.

### What progress would require

A genuinely new theorem on the prime factors of individual values `p(n)`—on at least the rough `sqrt(n) log n` scale forced by the logged lemma—or a different argument producing an excess `q`-adic valuation. This looks like specialist analytic/modular-form work, not a GAP search.

### Honest priority read

Low priority for another general-purpose computational cycle. The finite evidence is already exceptionally deep, while the evident theoretical bottleneck is far beyond the best directly relevant published bound located. Worth revisiting only with a partition-theory/modular-forms specialist who can name a theorem stronger than Cilleruelo–Luca or exploit the factorial valuation structure directly.

- 2026-08-11T16:00:00Z — work stopped and early `REPORT: DEAD` prepared; cumulative active minutes: 11. This is explicitly an early dead-end report, not a representation that the 180-minute budget was consumed. Lead may void or resume the cycle under the timing contract.
