#!/usr/bin/env bash
set -euo pipefail
export LC_ALL=C

p20115_script='Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.g'
p20115_stdout='Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.stdout'
p20115_stderr='Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.stderr'
p20115_resource='Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.resource'
p20115_tsv='Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.tsv'
p20115_script_sha='68d94b828032836644f8863ab02bee3e243401155ac5d3ea2c0b199ce76758b6'
p20115_sentinel=$'TERMINAL_SENTINEL\tKOUROVKA_20_115_6A7_AUDIT_COMPLETE_EXACTLY_ONCE'

p20115_die() {
  printf 'RUNNER_REJECTED: %s\n' "$1" >&2
  exit 1
}

printf '%s  %s\n' "$p20115_script_sha" "$p20115_script" \
  | sha256sum -c --status - \
  || p20115_die 'frozen GAP checker hash mismatch'

for p20115_path in "$p20115_stdout" "$p20115_stderr" "$p20115_resource" "$p20115_tsv"; do
  [[ ! -e "$p20115_path" ]] || p20115_die "pre-existing output: $p20115_path"
done

set +e
/usr/bin/time -v -o "$p20115_resource" \
  timeout 45s gap --quitonbreak -q "$p20115_script" \
  >"$p20115_stdout" 2>"$p20115_stderr"
p20115_rc=$?
set -e

[[ "$p20115_rc" -eq 0 ]] || p20115_die "GAP invocation exit status $p20115_rc"
[[ -s "$p20115_stdout" ]] || p20115_die 'stdout is absent or empty'
[[ -e "$p20115_stderr" ]] || p20115_die 'stderr path was not created'
[[ ! -s "$p20115_stderr" ]] || p20115_die 'stderr is nonempty'
[[ -s "$p20115_resource" ]] || p20115_die 'resource report is absent or empty'
[[ -s "$p20115_tsv" ]] || p20115_die 'TSV certificate is absent or empty'

if grep -Eq 'Error,|Error:|Syntax error|Syntax warning|brk>|^#E' "$p20115_stdout"; then
  p20115_die 'GAP error or diagnostic marker in stdout'
fi
if grep -Eq $'_GATE\tfalse$|^ALL_ROWS_IRREDUCIBLE\tfalse$|^FULL_ROW_ORTHOGONALITY\tfalse$' "$p20115_stdout"; then
  p20115_die 'explicit failed acceptance gate'
fi

p20115_require_once() {
  local p20115_line="$1"
  local p20115_count
  p20115_count=$(grep -Fxc "$p20115_line" "$p20115_stdout" || true)
  [[ "$p20115_count" -eq 1 ]] || p20115_die "expected exactly once: $p20115_line"
}

p20115_require_once $'TABLE_REQUEST\t6.A7'
p20115_require_once $'TABLE_IDENTIFIER\t6.A7'
p20115_require_once $'IS_LIBRARY_TABLE\ttrue'
p20115_require_once $'IS_ORDINARY_TABLE\ttrue'
p20115_require_once $'UNDERLYING_CHARACTERISTIC\t0'
p20115_require_once $'GROUP_ORDER\t15120'
p20115_require_once $'IS_PERFECT_TABLE\ttrue'
p20115_require_once $'IS_QUASISIMPLE_TABLE\ttrue'
p20115_require_once $'QUOTIENT_TABLE_IDENTIFIER\tA7'
p20115_require_once $'QUOTIENT_ORDER\t2520'
p20115_require_once $'CENTRAL_ORDER_RATIO\t6'
p20115_require_once $'QUOTIENT_KERNEL_ORDER\t6'
p20115_require_once $'IDENTITY_GATE\ttrue'
p20115_require_once $'SHAPE_GATE\ttrue'
p20115_require_once $'ALL_ROWS_IRREDUCIBLE\ttrue'
p20115_require_once $'FULL_ROW_ORTHOGONALITY\ttrue'
p20115_require_once $'COVERAGE_GATE\ttrue'
p20115_require_once "$p20115_sentinel"

p20115_final_count=$(grep -Ec $'^FINAL_STATUS\t(ZERO_HIT|HIT)$' "$p20115_stdout" || true)
[[ "$p20115_final_count" -eq 1 ]] || p20115_die 'final status is not unique'
[[ "$(tail -n 1 "$p20115_stdout")" = "$p20115_sentinel" ]] \
  || p20115_die 'terminal sentinel is not the final stdout line'

p20115_total=$(awk -F '\t' '$1 == "TOTAL_CELLS" { print $2 }' "$p20115_stdout")
p20115_nonzero=$(awk -F '\t' '$1 == "EXACT_NONZERO_CELLS" { print $2 }' "$p20115_stdout")
p20115_zeros=$(awk -F '\t' '$1 == "ZERO_CELLS" { print $2 }' "$p20115_stdout")
p20115_violations=$(awk -F '\t' '$1 == "VIOLATION_COUNT" { print $2 }' "$p20115_stdout")
p20115_nrows=$(awk -F '\t' '$1 == "IRREDUCIBLE_ROW_COUNT" { print $2 }' "$p20115_stdout")
p20115_nclasses=$(awk -F '\t' '$1 == "CLASS_COUNT" { print $2 }' "$p20115_stdout")

for p20115_integer in "$p20115_total" "$p20115_nonzero" "$p20115_zeros" \
  "$p20115_violations" "$p20115_nrows" "$p20115_nclasses"; do
  [[ "$p20115_integer" =~ ^[0-9]+$ ]] || p20115_die 'missing or noninteger summary count'
done
[[ "$p20115_total" -eq $(( p20115_nrows * p20115_nclasses )) ]] \
  || p20115_die 'summary grid size mismatch'
[[ "$p20115_total" -eq $(( p20115_nonzero + p20115_zeros )) ]] \
  || p20115_die 'summary zero/nonzero count mismatch'
[[ "$(wc -l < "$p20115_tsv")" -eq $(( p20115_total + 1 )) ]] \
  || p20115_die 'TSV line count mismatch'
[[ "$(head -n 1 "$p20115_tsv")" = $'row\tdegree\tclass\tclass_name\tclass_order\tvalue\texact_nonzero\tproduct\tgroup_order\tremainder\tdivides' ]] \
  || p20115_die 'TSV header mismatch'

awk -F '\t' \
  -v total="$p20115_total" \
  -v expected_nonzero="$p20115_nonzero" \
  -v expected_zeros="$p20115_zeros" \
  -v expected_violations="$p20115_violations" \
  -v nrows="$p20115_nrows" \
  -v nclasses="$p20115_nclasses" '
  NR == 1 { next }
  {
    if (NF != 11) exit 10;
    if ($1 !~ /^[0-9]+$/ || $3 !~ /^[0-9]+$/) exit 11;
    if ($1 < 1 || $1 > nrows || $3 < 1 || $3 > nclasses) exit 12;
    key = $1 SUBSEP $3;
    if (seen[key]++) exit 13;
    if ($7 == "true") nz++;
    else if ($7 == "false") z++;
    else exit 14;
    if ($11 != "true" && $11 != "false") exit 15;
    if ($7 == "true" && $11 == "false") bad++;
  }
  END {
    if (NR - 1 != total || nz != expected_nonzero || z != expected_zeros || bad != expected_violations) exit 16;
    for (i = 1; i <= nrows; i++)
      for (j = 1; j <= nclasses; j++)
        if (!((i SUBSEP j) in seen)) exit 17;
  }
' "$p20115_tsv" || p20115_die 'TSV Cartesian-grid or summary audit failed'

p20115_final=$(awk -F '\t' '$1 == "FINAL_STATUS" { print $2 }' "$p20115_stdout")
p20115_violation_lines=$(grep -c $'^VIOLATION\t' "$p20115_stdout" || true)
if [[ "$p20115_final" = 'ZERO_HIT' ]]; then
  [[ "$p20115_violations" -eq 0 && "$p20115_violation_lines" -eq 0 ]] \
    || p20115_die 'ZERO_HIT conflicts with violations'
elif [[ "$p20115_final" = 'HIT' ]]; then
  [[ "$p20115_violations" -gt 0 && "$p20115_violation_lines" -eq "$p20115_violations" ]] \
    || p20115_die 'HIT lacks one exact certificate per violation'
else
  p20115_die 'unrecognized final status'
fi

printf 'RUNNER_ACCEPTED\t%s\tCELLS\t%s\tNONZERO\t%s\tVIOLATIONS\t%s\n' \
  "$p20115_final" "$p20115_total" "$p20115_nonzero" "$p20115_violations"
