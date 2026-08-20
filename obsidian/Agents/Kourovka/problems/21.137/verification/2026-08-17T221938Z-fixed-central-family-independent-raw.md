---
title: "Independent fixed central-family checker — complete raw output"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/compute-lease, project/kourovka, status/replicated]
---

# Frozen invocation

The two approved hashes matched immediately before the single invocation:

```text
04f8b72d3735b459326560ede404eb689ddfa257ccfac7c16b2c7a8d0b564efe  Agents/Kourovka/problems/21.137/verification/scratch/validate_fixed_central_family.py
dce2b28b8e27b0ccc33fb3b2c193c9510567c57b5661213e853a2a7174d2a830  Agents/Kourovka/problems/21.137/verification/scratch/validate-fixed-central-family-manifest.md
```

Exact leased command:

```text
timeout 600s python3 -u Agents/Kourovka/problems/21.137/verification/scratch/validate_fixed_central_family.py
```

Execution session `45525`; exit code `0`; no standard-error output, patch, or
rerun.

# Complete stdout

```text
frozen lift reconstruction: PASS
six action-relator inner labels: ((0, 0, 0, 1), (0, 1, 0, 0), (0, 0, 0, 0), (2, 0, 2, 1), (0, 2, 0, 2), (0, 1, 0, 1))
V defect/associativity checks: 729 19683 78732
central variables/equations/rank/dimension: 2028 59049 1951 77
relator affine rank/dimension/feasible rows: 8 8 6561
complete affine relator equations:
  ((1, 1), 0)
  ((2, 1), 0)
  ((4, 1), 0)
  ((5, 1), 0)
  ((6, 1), (11, 2), (13, 2), 0)
  ((7, 1), 0)
  ((8, 1), 0)
  ((11, 1), (13, 2), (16, 2), 0)
  ((14, 1), 2)
  ((17, 1), 2)
C1/coboundary/Z1 dimensions: 78 74 4
gauge rank/image size: 5 243
exact-row kernel equality: 69 69
quotient dimensions: 3 3
gauge matrix rows:
  002000000
  000000000
  000000000
  000001000
  000000000
  000000000
  000000000
  000000000
  000000000
  020020200
  002001020
  000000002
  002000021
  000000001
  000000000
  000002012
  000000001
  000000000
derived orbit count/coverage: 27 6561
CLASS 0 000000000000002002 factor fa61212431a7a7c66dd407f7a6d821eed5fcee8e0fbf967a3f42bd9d67f2f9bf factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 1, 0, 0, 0, 0, 0, 0, 1)
CLASS 1 000000000000002102 factor dc612620b1c3b802afe783e120863823fdc1ac4c8be0ad1bbc623c4e488de0fe factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 1, 0, 0, 0, 0, 0, 0, 1)
CLASS 2 000000000000002202 factor aa6b37ea3337fe55f42c231677553cdd23b9fd839e23de6a25c79602ac610301 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 1, 0, 0, 0, 0, 0, 0, 1)
CLASS 3 000000000000102002 factor 5d068b73f37430efd05229650a5244136e1aa4e509e0d158331a3bb3c3d1c8d7 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 1, 0, 0, 0, 0, 0, 0, 1)
CLASS 4 000000000000102102 factor d4c566183dd1925518f62e92ade30d1f4e4bfe41276bc977eae1da6b4816f850 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 1, 0, 0, 0, 0, 0, 0, 1)
CLASS 5 000000000000102202 factor 95a4c890c27065b4c6bb84334b47b8b7769de72233935338ccc144955f394a3e factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 1, 0, 0, 0, 0, 0, 0, 1)
CLASS 6 000000000000202002 factor dc211ea477e06fd7f417b61218851b4b9ef92d52d4c42ccc80dc707de997979a factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 1, 0, 0, 0, 0, 0, 0, 1)
CLASS 7 000000000000202102 factor 50420c19099b642df9ef6e97b20dc2cd9eeb50d0c367bbbacfc4c929f8d77771 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 1, 0, 0, 0, 0, 0, 0, 1)
CLASS 8 000000000000202202 factor 26edf7748c5baa864dbb1cf8ae07534fd1b4145aa253f39e9f3f664851794683 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 1, 0, 0, 0, 0, 0, 0, 1)
CLASS 9 000000100000012022 factor 9dcd63adf678fa4325503db6ccd8b665a3a86ae808c9afc1b825edade4495a13 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 10 000000100000012122 factor 95e3f6f489b2777a4b25c00004b0b15f7e175407dbe73a526e9aa5e52b346fc7 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 11 000000100000012222 factor 1b7f5874068d5a1f39979adfd7d5903a155d5d6cea9a6d2f1f20f16da11e0ce2 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 12 000000100000112022 factor 893cae76543f8833f5c0084722474aa8a40158a53a8c7af81cda83db305e7e8a factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 13 000000100000112122 factor 53b02ba52040f172cbae5d3dddad43cf90798b388a4180ac8e20df58fd74750d factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 14 000000100000112222 factor b30fae30c72e2534505852973a094697fcff31572b4d7e10db2f6f72517fd4cf factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 15 000000100000212022 factor 17aa86f2952bbcebd541664d183d1980de4c2a84c0940e86ebc7e0abca3fb5e5 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 16 000000100000212122 factor 793f7d2ef0fbd71bd2f49b0093faab7f9898c1d70e88efba4e53e3b76c07701c factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 17 000000100000212222 factor f0c84ccb9268ae7847555198130c8a98f0f129f9a5aa9740ad1f7c9be1abc641 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 18 000000200000022012 factor 13a1928118f6898f78c4b606048ed8c307cd98441739a9ca8d6104961dbeb920 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 19 000000200000022112 factor f63689b58479600c60c1622a5fa9dfe36918032d5fe8551a4354635c715f83d4 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 20 000000200000022212 factor 5c719800fea72f03b46d2add1b7000d7a8501fe915d5a2fb3fb030720e0e9b03 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 21 000000200000122012 factor 5dbc4c9e0547be6ce9c57e52988398e529b5b86dbeb903997e283c02fc935777 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 22 000000200000122112 factor be7bf38f71f65b8d84f8d3c19d93582cde2b39e392eb41e0bf595bfe6a2957c2 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 23 000000200000122212 factor d1e65a19ee9bce62a03848abf7f453f0e70900169c4b15da82b69bb0c7f4f83a factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 24 000000200000222012 factor 731a4fbb4369cf1b431adcc8543b2f401d657beb8cb7badb5119879b177089d4 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 25 000000200000222112 factor ce782a2c507361eb57143b4dfd913efd77293e3fd44679c1afa8e89f6431c82d factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
CLASS 26 000000200000222212 factor 9ede372654a586cae4f4174721c274d6d262b6e06371563599c6365c76464051 factor_triples 19683 order/kernel/quotient 59049 2187 27 exp9 True literal_cube_size 135 literal_closed False generated_closure_size 729
 CLOSURE_OUTSIDE (2, 1, 0, 2, 2, 0, 1, 0, 0, 0) progression [1, 3, 9, 27, 81, 243, 729]
 ORDER9_WITNESS (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
ALL 27 CLASSES: PASS
literal image sizes: [135]
generated comparator sizes: [729]
TARGET-EQUAL CLASS INDICES: []
BOUNDARY: exactly one frozen p=3 action/lift family; active_assignment_answered:no
```
