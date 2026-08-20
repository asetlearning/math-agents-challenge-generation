#!/usr/bin/env bash
set -euo pipefail
export LC_ALL=C

p20115_stdout='Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.stdout'
p20115_stderr='Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.stderr'
p20115_resource='Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.resource'
p20115_tsv='Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.tsv'

p20115_die() {
  printf 'POSTHOC_REJECTED: %s\n' "$1" >&2
  exit 1
}

printf '%s  %s\n' \
  'b8ee32b2473278bb98dc1bbc23908ee4ea605d2c66730f339e788a0e1e8cdbcd' "$p20115_stdout" \
  'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' "$p20115_stderr" \
  '9099971d0629d0d6ae1de027f789219b12cd313b4f4ad66ff78c67844c5e8598' "$p20115_resource" \
  'd592aee3277c3b870daec04c5d10ef49b98b39a555bd8736fed0019111284d31' "$p20115_tsv" \
  | sha256sum -c --status - \
  || p20115_die 'immutable output hash mismatch'

[[ ! -s "$p20115_stderr" ]] || p20115_die 'stderr is nonempty'
[[ "$(tail -n 1 "$p20115_stdout")" = $'TERMINAL_SENTINEL\tKOUROVKA_20_115_6A7_AUDIT_COMPLETE_EXACTLY_ONCE' ]] \
  || p20115_die 'stdout terminal sentinel mismatch'

p20115_header=$(sed -n '1,2p' "$p20115_tsv" | sed ':a;N;$!ba;s/\\\n//g')
[[ "$p20115_header" = $'row\tdegree\tclass\tclass_name\tclass_order\tvalue\texact_nonzero\tproduct\tgroup_order\tremainder\tdivides' ]] \
  || p20115_die 'the two physical header lines do not reconstruct the frozen header'

awk -F '\t' '
  BEGIN { nonzero = 0; zeros = 0; violations = 0 }
  NR <= 2 { next }
  {
    if (NF != 11) exit 10;
    if ($1 !~ /^[0-9]+$/ || $2 !~ /^[0-9]+$/ || $3 !~ /^[0-9]+$/ ||
        $5 !~ /^[0-9]+$/ || $8 !~ /^[0-9]+$/ || $9 !~ /^[0-9]+$/ ||
        $10 !~ /^[0-9]+$/) exit 11;
    if ($1 < 1 || $1 > 40 || $3 < 1 || $3 > 40) exit 12;
    key = $1 SUBSEP $3;
    if (seen[key]++) exit 13;
    if ($7 != "true" && $7 != "false") exit 14;
    if ($11 != "true" && $11 != "false") exit 15;
    if ((($6 != "0") ? "true" : "false") != $7) exit 16;
    if ($8 != $2 * $5 || $9 != 15120 || $10 != 15120 % $8) exit 17;
    if ((($10 == 0) ? "true" : "false") != $11) exit 18;
    if (($1 in rowdegree) && rowdegree[$1] != $2) exit 19;
    rowdegree[$1] = $2;
    if (($3 in classname) && classname[$3] != $4) exit 20;
    classname[$3] = $4;
    if (($3 in classorder) && classorder[$3] != $5) exit 21;
    classorder[$3] = $5;
    if ($7 == "true") {
      nonzero++;
      if ($11 == "false") violations++;
    } else {
      zeros++;
    }
  }
  END {
    if (NR - 2 != 1600 || nonzero != 1044 || zeros != 556 || violations != 0) exit 22;
    for (i = 1; i <= 40; i++)
      for (j = 1; j <= 40; j++)
        if (!((i SUBSEP j) in seen)) exit 23;
    print "POSTHOC_DATA_ROWS\t" NR - 2;
    print "POSTHOC_EXACT_NONZERO\t" nonzero;
    print "POSTHOC_ZEROS\t" zeros;
    print "POSTHOC_VIOLATIONS\t" violations;
  }
' "$p20115_tsv" || p20115_die 'data-row Cartesian, value, or arithmetic audit failed'

printf 'POSTHOC_ACCEPTED\tHEADER_WRAP_ONLY\tIMMUTABLE_HASHES_PINNED\n'
