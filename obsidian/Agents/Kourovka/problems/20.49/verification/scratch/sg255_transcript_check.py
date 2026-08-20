#!/usr/bin/env python3
"""Parse and cross-check the frozen SG255 witness-first transcript."""

from pathlib import Path
import re


PATH = Path(
    "Agents/Kourovka/problems/20.49/runs/"
    "2026-08-17-r1-nonsoluble-pair-orbits/scratch/sg255_witness_first.out"
)
lines = PATH.read_text().splitlines()
start_re = re.compile(r"^ORDER_START order=(\d+) catalogue_count=(\d+)$")
done_re = re.compile(
    r"^ORDER_DONE order=(\d+) catalogue_count=(\d+) "
    r"soluble_count=(\d+) nonsoluble_count=(\d+)$"
)
group_re = re.compile(
    r"^GROUP id=\[\s*(\d+),\s*(\d+)\s*\] status=([A-Z_]+) "
    r"ambient_exponent=(\d+) tested_pairs_until_witness=(\d+) "
    r"witness=\[i,j,ord_i,ord_j,subgroup_size,subgroup_exponent\]="
    r"\[\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+)\s*\] "
    r"runtime_ms=(\d+)$"
)
summary_re = re.compile(
    r"^SUMMARY total_catalogue_groups=(\d+) soluble_groups=(\d+) "
    r"nonsoluble_groups=(\d+) pairs_tested=(\d+) "
    r"candidate_groups=(\d+) runtime_ms=(\d+)$"
)
headers = {
    "KOUROVKA_20_49_SG255_WITNESS_FIRST_V1",
    "gap_version=4.12.1",
    "smallgrp_static_version=1.5.3",
    "bound=255",
    "catalogue_iteration=all_indices",
    "candidate_rule=exhaust_all_ordered_pairs_without_exponent_equality",
}
starts = []
dones = []
groups = []
summaries = []
unknown = []
for line_number, line in enumerate(lines, 1):
    if match := start_re.match(line):
        starts.append(tuple(map(int, match.groups())))
    elif match := done_re.match(line):
        dones.append(tuple(map(int, match.groups())))
    elif match := group_re.match(line):
        values = match.groups()
        groups.append(
            (line_number,)
            + tuple(value if index == 2 else int(value) for index, value in enumerate(values))
        )
    elif match := summary_re.match(line):
        summaries.append(tuple(map(int, match.groups())))
    elif line not in headers:
        unknown.append((line_number, line))

assert lines[:6] == [
    "KOUROVKA_20_49_SG255_WITNESS_FIRST_V1",
    "gap_version=4.12.1",
    "smallgrp_static_version=1.5.3",
    "bound=255",
    "catalogue_iteration=all_indices",
    "candidate_rule=exhaust_all_ordered_pairs_without_exponent_equality",
]
assert [n for n, _ in starts] == list(range(1, 256))
assert [n for n, *_ in dones] == list(range(1, 256))
starts_by_order = dict(starts)
dones_by_order = {n: (count, soluble, nonsoluble) for n, count, soluble, nonsoluble in dones}
assert all(
    starts_by_order[n] == dones_by_order[n][0]
    and dones_by_order[n][1] + dones_by_order[n][2] == starts_by_order[n]
    for n in starts_by_order
)
assert len(summaries) == 1 and lines[-1].startswith("SUMMARY ")
total, soluble, nonsoluble, pair_count, candidates, runtime = summaries[0]
assert (
    sum(starts_by_order.values()),
    sum(row[1] for row in dones_by_order.values()),
    sum(row[2] for row in dones_by_order.values()),
) == (total, soluble, nonsoluble) == (7012, 6998, 14)
assert len(groups) == nonsoluble == 14

by_order = {}
ids = []
pair_sum = 0
for row in groups:
    (
        line_number,
        order,
        index,
        status,
        ambient_exponent,
        tested,
        i,
        j,
        order_i,
        order_j,
        subgroup_size,
        subgroup_exponent,
        runtime_ms,
    ) = row
    assert status == "HAS_FULL_EXPONENT_PAIR"
    assert 1 <= index <= starts_by_order[order]
    assert 1 <= i <= order and 1 <= j <= order
    assert tested == (i - 1) * order + j
    assert subgroup_exponent == ambient_exponent
    assert order % subgroup_size == 0
    ids.append((order, index))
    pair_sum += tested
    by_order[order] = by_order.get(order, 0) + 1

assert len(set(ids)) == 14
assert all(by_order.get(n, 0) == dones_by_order[n][2] for n in dones_by_order)
assert pair_sum == pair_count == 5932 and candidates == 0
assert not unknown
assert not any("FATAL" in line or "COUNTEREXAMPLE_CANDIDATE" in line for line in lines)

print("PARSE_PASS")
print(
    f"lines={len(lines)} starts={len(starts)} dones={len(dones)} "
    f"group_rows={len(groups)} summaries={len(summaries)} unknown={len(unknown)}"
)
print(
    f"sums catalogue={sum(starts_by_order.values())} "
    f"soluble={sum(row[1] for row in dones_by_order.values())} "
    f"nonsoluble={sum(row[2] for row in dones_by_order.values())} "
    f"tested_pairs={pair_sum} candidates={candidates}"
)
print("nonsoluble_by_order=" + ",".join(f"{n}:{by_order[n]}" for n in sorted(by_order)))
print(
    "all_ids_unique=yes all_indices_in_range=yes "
    "all_tested_pair_positions_consistent=yes "
    "all_subgroup_exponents_equal_ambient=yes "
    "all_subgroup_sizes_divide_order=yes"
)
print("fatal_rows=0 candidate_rows=0 terminal_summary=yes")
for row in groups:
    (
        line_number,
        order,
        index,
        status,
        ambient_exponent,
        tested,
        i,
        j,
        order_i,
        order_j,
        subgroup_size,
        subgroup_exponent,
        runtime_ms,
    ) = row
    print(
        f"id=[{order},{index}] pair=[{i},{j}] orders=[{order_i},{order_j}] "
        f"subgroup_size={subgroup_size} exponent={subgroup_exponent} tested={tested}"
    )
