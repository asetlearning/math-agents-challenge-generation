#!/usr/bin/env bash
set -euo pipefail

scratch_dir='Agents/Kourovka/problems/21.53/runs/2026-08-17-r1-a6-two-colour-separation/scratch'
output_dir="$scratch_dir/output"
mkdir -p "$output_dir"

python3 "$scratch_dir/build_a6_instance.py" \
  --params "$scratch_dir/a6-parameters.json" \
  --out "$output_dir" \
  > "$output_dir/a6_build_stdout.json"

sha256sum \
  "$scratch_dir/build_a6_instance.py" \
  "$scratch_dir/a6-parameters.json" \
  "$output_dir/a6_two_colour.dre" \
  "$output_dir/a6_full_colour.dre" \
  > "$output_dir/pre-nauty-sha256.txt"

timeout 25s dreadnaut \
  < "$output_dir/a6_two_colour.dre" \
  > "$output_dir/a6_two_colour.nauty.out" \
  2> "$output_dir/a6_two_colour.nauty.err"

timeout 25s dreadnaut \
  < "$output_dir/a6_full_colour.dre" \
  > "$output_dir/a6_full_colour.nauty.out" \
  2> "$output_dir/a6_full_colour.nauty.err"

sha256sum "$output_dir"/* > "$output_dir/all-output-sha256.txt"
