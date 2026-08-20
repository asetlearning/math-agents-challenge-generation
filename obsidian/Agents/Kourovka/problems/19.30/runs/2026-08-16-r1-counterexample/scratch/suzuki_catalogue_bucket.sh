#!/usr/bin/env bash
set -eu

SIZE_INDEX=$(dpkg -L gap-character-tables | rg '/attr_size\.json\.gz$' | head -1)

printf 'CTBLLIB_SIZE_INDEX=%s\n' "$SIZE_INDEX"
printf 'SIZE_INDEX_RECORDS='
gzip -dc "$SIZE_INDEX" | rg -c '^\['
printf 'TARGET_ORDER_RECORDS\n'
gzip -dc "$SIZE_INDEX" | rg -n ',(29120|32537600)\],?$'

timeout 20s gap -q <<'GAP'
LoadPackage("ctbllib");;
names := AllCharacterTableNames();;
Print("ALL_CHARACTER_TABLE_NAMES_COUNT=", Length(names), "\n");
Print("POSITION_SZ8=", Position(names, "Sz(8)"), "\n");
Print("POSITION_SZ32=", Position(names, "Sz(32)"), "\n");
Print("SUZUKI_SUBSTRING_NAMES=",
      Filtered(names, x -> PositionSublist(x, "Sz(") <> fail), "\n");
QUIT;
GAP

