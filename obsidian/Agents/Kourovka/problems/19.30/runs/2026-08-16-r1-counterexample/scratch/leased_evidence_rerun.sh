#!/usr/bin/env bash
set -eu

RUN_ROOT='Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample'

gap -q "$RUN_ROOT/scratch/suzuki_exact_screen.g"
bash "$RUN_ROOT/scratch/suzuki_catalogue_bucket.sh"
gap -q "$RUN_ROOT/scratch/suzuki_borel_product.g"
gap -q "$RUN_ROOT/scratch/perfect_divisor_screen_29120.g"
gap -q "$RUN_ROOT/scratch/normal_prime_arithmetic.g"

