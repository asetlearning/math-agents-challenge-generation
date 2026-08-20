#!/usr/bin/env python3
"""Independent transcript checker for the frozen MIN9 action-family run.

This does not invoke GAP or trust the claimant's aggregate prose.  It hashes the
two frozen artifacts, parses every multiline candidate record, recomputes the
closed histogram flow, and checks all advertised partitions and terminal gates.
"""

from __future__ import annotations

from collections import Counter
import hashlib
from pathlib import Path
import re


ROOT = Path("Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch")
SCRIPT = ROOT / "min9_central_module_action.g"
OUTPUT = ROOT / "min9_profile_before_fusion.out"

EXPECTED = {
    "script_sha256": "ba0b74b5f3d3e0ba6604c8d4399f925cd9decbd2fc8f3803753fb78b62241cdd",
    "script_lines": 508,
    "script_bytes": 18475,
    "output_sha256": "b1b187eb3add7ef6154ff3aa1b32eda390c1e1c50877bb23043a26eee01b17ab",
    "output_lines": 22408,
    "output_bytes": 1504811,
}


def digest_and_size(path: Path) -> tuple[str, int, int]:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest(), data.count(b"\n"), len(data)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def one(pattern: str, text: str, label: str) -> re.Match[str]:
    matches = list(re.finditer(pattern, text))
    require(len(matches) == 1, f"{label}: expected one match, found {len(matches)}")
    return matches[0]


script_sha, script_lines, script_bytes = digest_and_size(SCRIPT)
output_sha, output_lines, output_bytes = digest_and_size(OUTPUT)
require(script_sha == EXPECTED["script_sha256"], "script SHA-256 mismatch")
require(script_lines == EXPECTED["script_lines"], "script line count mismatch")
require(script_bytes == EXPECTED["script_bytes"], "script byte count mismatch")
require(output_sha == EXPECTED["output_sha256"], "output SHA-256 mismatch")
require(output_lines == EXPECTED["output_lines"], "output line count mismatch")
require(output_bytes == EXPECTED["output_bytes"], "output byte count mismatch")

raw = OUTPUT.read_text(encoding="utf-8")
# GAP uses backslash-newline for a few display wraps.  Removing those and then
# collapsing whitespace makes each printed logical record parseable as one line.
flat = re.sub(r"\s+", " ", raw.replace("\\\n", "")).strip()

coord = one(
    r"COORDINATE_CHECK bracket_generators=(true|false) aut_order=\s*(\d+) "
    r"inner_order=\s*(\d+) inner_normal=(true|false)",
    flat,
    "coordinate check",
)
require(coord.groups() == ("true", "15116544", "9", "true"), "coordinate totals mismatch")

outer = one(
    r"OUTER_CHECK outer_order=(\d+) expected=(\d+) sylow3_order=\s*(\d+) "
    r"expected_sylow3=(\d+) kernel_order=(\d+)",
    flat,
    "outer check",
)
require(
    tuple(map(int, outer.groups())) == (1679616, 1679616, 6561, 6561, 9),
    "outer/Sylow totals mismatch",
)

subgroups = one(r"SUBGROUP_ENUM_COMPLETE s_class_count=(\d+)", flat, "subgroup enumeration")
require(int(subgroups.group(1)) == 17409, "Sylow subgroup-class count mismatch")

part_a = one(
    r"PREFUSION_PARTITION quotient=C3\^4 target_sclasses=(\d+) "
    r"target_subgroups_sum=\s*(\d+) central_pass_sclasses=(\d+) "
    r"central_pass_subgroups_sum=(\d+)",
    flat,
    "C3^4 partition",
)
require(tuple(map(int, part_a.groups())) == (8797, 96163, 500, 11892), "C3^4 partition mismatch")

part_n = one(
    r"PREFUSION_PARTITION quotient=H3xC3 target_sclasses=(\d+) "
    r"target_subgroups_sum=\s*(\d+) central_pass_sclasses=(\d+) "
    r"central_pass_subgroups_sum=(\d+)",
    flat,
    "H3xC3 partition",
)
require(tuple(map(int, part_n.groups())) == (12258, 133410, 2366, 36738), "H3xC3 partition mismatch")

setup = one(r"PROFILE_BEFORE_FUSION_SETUP retained_sclasses=(\d+)", flat, "profile setup")
require(int(setup.group(1)) == 2398, "retained union count mismatch")
require(500 + 2366 - 2398 == 468, "overlap arithmetic mismatch")

starts = list(re.finditer(r"PREFUSION_LIFT_PROFILE candidate=(\d+)", flat))
require(len(starts) == 2398, f"expected 2398 candidate records, found {len(starts)}")
end_marker = flat.index("PREFUSION_LIFT_PROFILE_COMPLETE")

record_pattern = re.compile(
    r"PREFUSION_LIFT_PROFILE candidate=(\d+) sclass_index=(\d+) image_order=\s*(\d+) "
    r"central_branch=([A-Z0-9_x]+) kernel_size=(\d+) label_histogram=\s*"
    r"\[\s*([0-9, ]*?)\s*\] max_flow=(\d+) min_cut=(\d+).*?survives=(true|false)$"
)

rows: list[dict[str, object]] = []
for i, start in enumerate(starts):
    stop = starts[i + 1].start() if i + 1 < len(starts) else end_marker
    chunk = flat[start.start() : stop].strip()
    match = record_pattern.fullmatch(chunk)
    require(match is not None, f"candidate record {i + 1} did not parse")
    candidate, sindex, order, branch, kernel, hist_text, flow, cut, survives = match.groups()
    hist = [int(x.strip()) for x in hist_text.split(",") if x.strip()]
    row = {
        "candidate": int(candidate),
        "sindex": int(sindex),
        "order": int(order),
        "branch": branch,
        "kernel": int(kernel),
        "hist": hist,
        "flow": int(flow),
        "cut": int(cut),
        "survives": survives,
    }
    rows.append(row)

require([row["candidate"] for row in rows] == list(range(1, 2399)), "candidate IDs have a gap or duplicate")
sindices = [int(row["sindex"]) for row in rows]
require(sindices == sorted(sindices), "Sylow-class indices are not monotone")
require(len(set(sindices)) == 2398, "duplicate Sylow-class index in retained union")
require(min(sindices) >= 1 and max(sindices) <= 17409, "Sylow-class index outside enumerated range")

allowed_branches = {
    "CYCLIC_REGULAR_C3",
    "ELEMENTARY_C3xC3_CENTRALIZER",
    "FULL_UT3_3",
}
flow_counts: Counter[int] = Counter()
order_counts: Counter[int] = Counter()
branch_counts: Counter[str] = Counter()
order_flow_counts: Counter[tuple[int, int]] = Counter()

for row in rows:
    order = int(row["order"])
    kernel = int(row["kernel"])
    branch = str(row["branch"])
    hist = list(row["hist"])
    flow = int(row["flow"])
    cut = int(row["cut"])
    require(order in {3, 9, 27, 81}, f"unexpected image order in candidate {row['candidate']}")
    require(order * kernel == 81, f"bad k=81/|U| in candidate {row['candidate']}")
    require(branch in allowed_branches, f"unexpected central branch in candidate {row['candidate']}")
    require(len(hist) == 8, f"label histogram does not have eight entries in candidate {row['candidate']}")
    require(hist == sorted(hist), f"label histogram is not sorted in candidate {row['candidate']}")
    require(all(0 <= value <= order for value in hist), f"histogram entry out of range in candidate {row['candidate']}")
    if branch in {"CYCLIC_REGULAR_C3", "ELEMENTARY_C3xC3_CENTRALIZER"}:
        regular_upper = 2 * order // 3
    else:
        require(order >= 27, f"full UT3 branch below order 27 in candidate {row['candidate']}")
        regular_upper = 4 * order // 9
    require(sum(hist) <= regular_upper, f"too many admitted regular elements in candidate {row['candidate']}")
    recomputed = sum(min(27, 9 * kernel * multiplicity) for multiplicity in hist)
    require(recomputed == flow, f"histogram flow mismatch in candidate {row['candidate']}")
    require(flow == cut, f"max-flow/min-cut mismatch in candidate {row['candidate']}")
    require(row["survives"] == "false", f"unexpected survivor in candidate {row['candidate']}")
    flow_counts[flow] += 1
    order_counts[order] += 1
    branch_counts[branch] += 1
    order_flow_counts[(order, flow)] += 1

require(flow_counts == Counter({0: 158, 54: 1736, 108: 336, 162: 168}), "flow distribution mismatch")
require(sum(flow_counts.values()) == 2398, "flow distribution does not cover every row")
require(max(flow_counts) < 216, "a printed row reaches terminal demand 216")

complete = one(
    r"PREFUSION_LIFT_PROFILE_COMPLETE survivors=\s*(\d+) "
    r"survivor_C3\^4_sclasses=\s*(\d+) survivor_H3xC3_sclasses=(\d+)",
    flat,
    "prefusion completion",
)
require(tuple(map(int, complete.groups())) == (0, 0, 0), "prefusion terminal counts mismatch")

fusion = one(
    r"FULL_OUTER_FUSION_COMPLETE prefusion_survivors=(\d+) full_outer_classes=(\d+)",
    flat,
    "fusion completion",
)
require(tuple(map(int, fusion.groups())) == (0, 0), "fusion terminal counts mismatch")

survivor_counts = one(
    r"SURVIVOR_COUNTS quotient_C3\^4_outer_orbits=\s*(\d+) "
    r"quotient_H3xC3_epimorphism_orbits=(\d+)",
    flat,
    "survivor counts",
)
require(tuple(map(int, survivor_counts.groups())) == (0, 0), "quotient survivor counts mismatch")

status = one(
    r"STATUS=MIN9_CENTRAL_MODULE_ACTION_COMPLETE active_assignment_answered=no "
    r"factor_systems_opened=0 cocycles_opened=0",
    flat,
    "normal status",
)
require("STATUS=HARD_KILL" not in flat and "Error," not in flat, "failure marker present")
require(raw.count("Syntax warning:") == 1, "unexpected number of lexical warnings")

print(f"SCRIPT sha256={script_sha} lines={script_lines} bytes={script_bytes}")
print(f"OUTPUT sha256={output_sha} lines={output_lines} bytes={output_bytes}")
print("COORDINATES aut=15116544 inn=9 out=1679616 sylow3=6561")
print("SUBGROUPS sylow_conjugacy_classes=17409")
print("PARTITION C3^4=8797/500 H3xC3=12258/2366 union=2398 overlap=468")
print("CANDIDATES ids=1..2398 unique_sclasses=2398 all_rows_parsed=yes")
print("ORDER_COUNTS " + " ".join(f"{key}:{order_counts[key]}" for key in sorted(order_counts)))
print("BRANCH_COUNTS " + " ".join(f"{key}:{branch_counts[key]}" for key in sorted(branch_counts)))
print("FLOW_COUNTS " + " ".join(f"{key}:{flow_counts[key]}" for key in sorted(flow_counts)))
print(
    "ORDER_FLOW_COUNTS "
    + " ".join(f"{order}/{flow}:{count}" for (order, flow), count in sorted(order_flow_counts.items()))
)
print("ROW_CHECKS kernel=yes hist8=yes regular_upper=yes formula=yes maxflow_eq_mincut=yes survivors=0")
print("TERMINAL prefusion=0 fusion=0 quotient_survivors=0 normal_status=yes warnings=1")
