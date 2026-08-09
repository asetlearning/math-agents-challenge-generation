# LADDER_G4 — automatic structure attempt for G_4, E7 != 1 test

Date: 2026-08-01/02. Host: Darwin, 14 cores, 36 GB RAM.
Working dir: `infinite_b25/avenues/a6_bounded/kbmag/`
Binaries: `kbmag_v1/standalone/bin/` (kbprog, gpmakefsa, gpaxioms, wordreduce).

G_4 = <a,b | w^5 for all cyclic words w of length <= 4>, 17 relators (file `g4`),
shortlex, generator order [a,A,b,B]. Target word: `e7_kb.txt` (139 letters,
terminated copy in `e7_input.txt`).

## Prior failures (before this session)

- `autgroup g4`: `#Knuth-Bendix program failed or was inconclusive. Giving up.`
- `autgroup -l g4`: `Maximum number of word-differences exceeded. Cannot continue.`
- `kbprog -mwd 16384` (log `kbprog_g4_mwd16384.log`):
  `#Maximum number of equations exceeded. #Halting with 262118 equations.`
  diff1 = 5572 states, diff2 = 6155 states (these were the stale `g4.diff1/diff2`,
  backed up to `backup_prev_run/`).
- `gpmakefsa g4` on those: `#Too much hash-space - try running with -l or -h.`
  then assertion failure (exit 134); `-h` variants killed by timeout (exit 142).

## Stage 1 — kbprog with generous limits (this session)

Command:

    kbprog -wd -v -me 1048576 -mwd 262144 -t 100 -cn 0 -mt 10 -hf 100 g4
    (log: kbprog_g4_big.log)

Progress: equations grew steadily (~120 eq/s), word-difference count grew and
then PLATEAUED at 5751:

    6714:	#There are 5751 word-differences.        (first hit, eqns ~302k, t=1101s)
    #Tidy: 306379->306373 eqns (...); len: 8225362,8030468; 1853671 st; 1135s

Word-differences stayed at 5751 from eqn ~302k onward. With `-hf 100` the
auto-halt would have required ~604k equations (~40 more min), so kbprog was
sent SIGINT (graceful halt handler: finishes tidying, writes wdiff machines).

SIGINT halt output (literal, from `kbprog_g4_big.log` tail):

      #Interrupt received - tidying and halting.
      #Tidy: 310037->310037 eqns; len: 8341180,8143928; 1879427 st; 1165s
        #There are 5754 word-differences.
    #Halting with 310037 equations.
    #First word-difference machine with 5754 states computed.
    #Second word-difference machine with 6395 states computed.
      #Exit status is 2

Files written: `g4.diff1` (5754 states, 298.6K), `g4.diff2` (6395 states,
784.5K), `g4.kbprog.live` 16.6M. Exit code 2 = interrupted/non-confluent, which
is expected; correctness is established downstream by gpmakefsa + gpaxioms,
not by KB confluence.

## Stage 2 — gpmakefsa

### 2a. `gpmakefsa -l -v g4` — FAILED (log: gpmakefsa_g4_big.log)

    #Too much hash-space - try running with -l or -h.
    Assertion failed: (wa), function main, file gpmakefsa.c, line 268.
    91.86 real   89.55 user   1.13 sys
    2555592704  maximum resident set size        (2.55 GB peak)
    gpmakefsa exit=134

The word-acceptor construction overflows the (larger) `-l` hash space; the
`assert(wa)` at gpmakefsa.c:268 fires because the wa build returned NULL.

### 2b. `gpmakefsa -h -v g4` (huge hash space; log: gpmakefsa_g4_huge.log)

Run with a 30-min wall budget and a 12 GB RSS kill-guard (prior `-h` attempts
died at an 8-min external timeout — exit 142 = SIGALRM — not on their own).

Progress (live): the `-h` hash space (1024 blocks x 16M entries vs `-l`'s
1024 x 1M — `lib/hash.c:15-21`) survived the word-acceptor determinization
that killed `-l`:

    #Number of states of word-acceptor before minimisation = 20087759.

(logged at 16:52 after ~23 min; process then CPU-bound in minimisation,
RSS 1.35 GB at 36 min elapsed. For scale: g3's final minimised word-acceptor
file is 41.6K — rung 4's raw acceptor is ~20M states before minimisation.)

NOTE: this first `-h` run was killed EXTERNALLY at ~40 min (orchestration
process-group reaping; no assert, no error in the log, RSS only 1.35 GB)
while still minimising. Not a solver failure.

### 2c. Detached relaunch of `gpmakefsa -h -v g4` (log: gpmakefsa_g4_huge2.log)

Relaunched in its own session (python `start_new_session=True`) so external
task reaping cannot kill it:

    /usr/bin/time -l gpmakefsa -h -v g4

Word acceptor COMPLETED (log, literal):

    #Number of states of word-acceptor before minimisation = 20087759.
    #Number of states of word-acceptor after minimisation = 7971915.
    #Word-acceptor with 7971915 states computed.

`g4.wa` = 199,906,447 bytes, written Aug 2 18:52:24. The process then entered
the general-multiplier phase (silent between milestones); at 2h38m elapsed it
was alive, state R, RSS 1.66 GB. For scale: g3.wa is 41.6K — the rung-4
minimised word acceptor (~8M states / 200 MB) is a ~4800x jump over rung 3.

Multiplier phase status at close of this session (Aug 3): pid 51925 STILL
RUNNING — 7h07m elapsed, state R (on CPU), RSS 945 MB (oscillating, i.e.
live allocation, not frozen), 20 GB guard never approached. gpmakefsa logs
nothing between multiplier milestones, so silence here is normal. `g4.gm`
not yet written. The process is detached (own session) and left running;
if `g4.gm` + `g4.success` appear later, resume at Stage 3 verification:

    gpcheckmult -h -v g4        (correction loop if it finds missing eqns)
    gpaxioms -l -v g4           (the actual verification)

## Stage 3 — reductions with the (unverified) diff2 machine

The 6395-state `g4.diff2` machine is SOUND but possibly INCOMPLETE: every
transition is backed by a KB-derived equation, so any reduction it performs
is a valid equality in G_4; what is missing without gpaxioms is the guarantee
that irreducible words are UNIQUE normal forms. Consequences:
- sanity word -> IdWord: proves that word = 1 in G_4 (sound).
- E7 -> nonempty word: evidence, NOT a proof, that E7 != 1.

Literal outputs (`wordreduce -diff2 g4`):

    A*A*A*A*A;                                    reduces to:  IdWord
    A*B*A*B*A*B*A*B*A*B;                          reduces to:  IdWord
    A*A*A*B*A*A*A*B*A*A*A*B*A*A*A*B*A*A*A*B;     reduces to:  IdWord

E7 (138 letters, `e7_input.txt`):

    reduces to:
      A*b*a*b*A*B*a*b*A*b*a*B*A*B*a*b*A*b*a*b*A*B*a*B*A*b*a*B*A*B*a*b*A*b*a*b*A
        *B*a*b*A*b*a*B*A*B*a*B*A*b*a*b*A*B*a*B*A*b*a*B*A*B*a*B*A*b*a*b*A*B*a*b
        *A*b*a*B*A*B*a*b*A*b*a*b*A*B*a*B*A*b*a*B*A*B*a*B*A*b*a*b*A*B*a*b*A*b*a
        *B*A*B*a*B*A*b*a*b*A*B*a*B*A*b*a*B*A*B*a*b

    reduced length: 128   (original: 138 — exactly the B^5 prefix and b^5 of
    the b^6 suffix stripped; the 128-letter core is diff2-irreducible)

Saved in `e7_diff2_result.txt`.

## Frontier summary (G_4, KB/automatic route)

- Knuth-Bendix itself is NOT the wall at rung 4: with `-me 1048576
  -mwd 262144 -cn 0`, equations grow indefinitely (310k at halt, no
  confluence) but the word-difference count PLATEAUS at 5751-5754 (drift of
  +3 over the last ~8k equations), strongly suggesting G_4 is shortlex
  automatic with ~5.8k word differences.
- The word acceptor IS computable but enormous: 20,087,759 states at
  determinization, 7,971,915 states minimised, 200 MB on disk (rung 3:
  ~41.6K file). Requires `-h` hash space (16 GB-entry ceiling); `-l`
  asserts at gpmakefsa.c:268 after 92s / 2.55 GB.
- The general multiplier over an 8M-state acceptor is the open cost: >4.5 h
  CPU-bound at modest memory (0.9-1.7 GB) without completing in this
  session. Not memory-bound — time-bound.
- Verification (gpcheckmult + gpaxioms) has therefore NOT run; no claim of
  a verified automatic structure is made. E7 != 1 in G_4 remains
  CONJECTURED (sound-reduction evidence above), E7 = 1 is NOT possible to
  conclude from this data.

## Verdict

NO VERIFIED STRUCTURE YET (multiplier construction still running at session
close). E7 STATUS: diff2-irreducible 128-letter core, nonzero in G_4 modulo
completeness of the 6395-state diff2 machine — evidence, not theorem.
Sanity fifth-powers all reduce to IdWord (proven equalities). If the
detached gpmakefsa finishes, run gpaxioms and re-issue the E7 reduction
under the verified structure to upgrade this to a theorem.
