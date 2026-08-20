#!/usr/bin/env python3
"""Leased exact comparison of the PSL(2,8) 2/3 and full colour groups.

This program verifies the frozen product-scheme hash, builds two vertex-coloured
incidence graphs, and asks GAP/GRAPE (nauty 2.8.8 backend) for their automorphism
groups.  The action is restricted to the original 63 vertices.  If the two-colour
group is strictly larger, one explicit permutation is exhaustively certified on
every 2-edge and 3-edge and one changed 7/9-edge is emitted.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


EXPECTED_SCHEME_SHA256 = "54bb450db146199b72e51b2e18b4b2b507075d50725cc0556f5293291a5f2e90"
VERTEX_COUNT = 63


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gap_list(value: object) -> str:
    """Python integer/list data use syntax accepted verbatim by GAP."""
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        return "[" + ",".join(gap_list(x) for x in value) + "]"
    raise TypeError(type(value))


def build_gap_program(scheme: dict[str, object]) -> str:
    data = scheme["scheme"]
    assert isinstance(data, dict)
    matrix = data["product_order_matrix"]
    edges = data["edges_i_j_order"]
    assert isinstance(matrix, list) and len(matrix) == VERTEX_COUNT
    assert isinstance(edges, list) and len(edges) == 1953
    # GAP vertices are 1-based. Incidence edges need only endpoint pairs.
    by_colour: dict[int, list[list[int]]] = {2: [], 3: [], 7: [], 9: []}
    for row in edges:
        assert isinstance(row, list) and len(row) == 3
        i, j, t = row
        assert isinstance(i, int) and isinstance(j, int) and isinstance(t, int)
        assert t in by_colour
        by_colour[t].append([i + 1, j + 1])
    assert {t: len(v) for t, v in by_colour.items()} == {2: 189, 3: 252, 7: 756, 9: 756}

    # Replace the diagonal zero convention by the stored diagonal 1; only i<j is used.
    gap_matrix = gap_list(matrix)
    gap_edges = {t: gap_list(by_colour[t]) for t in (2, 3, 7, 9)}
    return f'''LoadPackage("GRAPE");;
SizeScreen([1000000,1000000]);;
NOriginal := {VERTEX_COUNT};;
M := {gap_matrix};;
Edges2 := {gap_edges[2]};;
Edges3 := {gap_edges[3]};;
Edges7 := {gap_edges[7]};;
Edges9 := {gap_edges[9]};;

BuildIncidence := function(edgeClasses)
  local total, gamma, adjacency, cells, next, cls, cell, e, i;
  total := NOriginal + Sum(List(edgeClasses, Length));
  gamma := NullGraph(Group(()), total);
  adjacency := List([1..total], x -> []);
  cells := [[1..NOriginal]];
  next := NOriginal;
  for cls in edgeClasses do
    cell := [];
    for e in cls do
      next := next + 1;
      Add(cell, next);
      Add(adjacency[e[1]], next);
      Add(adjacency[e[2]], next);
      Add(adjacency[next], e[1]);
      Add(adjacency[next], e[2]);
    od;
    Add(cells, cell);
  od;
  for i in [1..total] do
    Sort(adjacency[i]);
    gamma.adjacencies[i] := Immutable(adjacency[i]);
  od;
  return rec(graph := gamma, colourClasses := cells);
end;;

ImagesList := p -> List([1..NOriginal], i -> i^p);;

CountRelationEdges := function(t)
  local count, i, j;
  count := 0;
  for i in [1..NOriginal-1] do
    for j in [i+1..NOriginal] do
      if M[i][j] = t then count := count + 1; fi;
    od;
  od;
  return count;
end;;

PreservesRelation := function(p, t)
  local count, i, j;
  count := 0;
  for i in [1..NOriginal-1] do
    for j in [i+1..NOriginal] do
      if M[i][j] = t then
        count := count + 1;
        if M[i^p][j^p] <> t then return [false, count, i, j, i^p, j^p]; fi;
      fi;
    od;
  od;
  return [true, count];
end;;

PreservesAllColours := function(p)
  local i, j;
  for i in [1..NOriginal-1] do
    for j in [i+1..NOriginal] do
      if M[i][j] <> M[i^p][j^p] then return false; fi;
    od;
  od;
  return true;
end;;

TwoGraph := BuildIncidence([Edges2, Edges3]);;
FullGraph := BuildIncidence([Edges2, Edges3, Edges7, Edges9]);;
TwoIncidenceGroup := AutGroupGraph(TwoGraph);;
FullIncidenceGroup := AutGroupGraph(FullGraph);;
TwoGroup := Action(TwoIncidenceGroup, [1..NOriginal], OnPoints);;
FullGroup := Action(FullIncidenceGroup, [1..NOriginal], OnPoints);;

if not ForAll(GeneratorsOfGroup(TwoGroup), p -> PreservesRelation(p,2)[1] and PreservesRelation(p,3)[1]) then
  Error("a generator returned for the two-colour group fails a defining relation");
fi;
if not ForAll(GeneratorsOfGroup(FullGroup), PreservesAllColours) then
  Error("a generator returned for the full group fails a product-order relation");
fi;
if not IsSubgroup(TwoGroup, FullGroup) then
  Error("the computed full group is not a subgroup of the computed two-colour group");
fi;

IsEqual := TwoGroup = FullGroup;;
Candidate := fail;;
Candidate2Check := [true, CountRelationEdges(2)];;
Candidate3Check := [true, CountRelationEdges(3)];;
ChangedEdge := [];;
if not IsEqual then
  Candidate := First(GeneratorsOfGroup(TwoGroup), p -> not p in FullGroup);
  if Candidate = fail then Error("strict containment but no generator outside full group"); fi;
  Candidate2Check := PreservesRelation(Candidate,2);
  Candidate3Check := PreservesRelation(Candidate,3);
  if not Candidate2Check[1] or Candidate2Check[2] <> 189 then Error("candidate 2-edge certificate failed"); fi;
  if not Candidate3Check[1] or Candidate3Check[2] <> 252 then Error("candidate 3-edge certificate failed"); fi;
  for i in [1..NOriginal-1] do
    for j in [i+1..NOriginal] do
      if ChangedEdge = [] and M[i][j] <> M[i^Candidate][j^Candidate] then
        ChangedEdge := [i,j,M[i][j],i^Candidate,j^Candidate,M[i^Candidate][j^Candidate]];
      fi;
    od;
  od;
  if ChangedEdge = [] then Error("candidate outside full group has no changed colour edge"); fi;
  if ChangedEdge[3] in [2,3] then Error("candidate changed a defining 2/3 edge"); fi;
fi;

Print("@@TWO_INCIDENCE_VERTICES=", TwoGraph.graph.order, "\\n");
Print("@@FULL_INCIDENCE_VERTICES=", FullGraph.graph.order, "\\n");
Print("@@EDGE_COUNTS=[", CountRelationEdges(2), ",", CountRelationEdges(3), ",", CountRelationEdges(7), ",", CountRelationEdges(9), "]\\n");
Print("@@TWO_ORDER=", Size(TwoGroup), "\\n");
Print("@@FULL_ORDER=", Size(FullGroup), "\\n");
Print("@@FULL_SUBGROUP_OF_TWO=", IsSubgroup(TwoGroup, FullGroup), "\\n");
Print("@@EQUAL=", IsEqual, "\\n");
Print("@@TWO_GENERATORS=", List(GeneratorsOfGroup(TwoGroup), ImagesList), "\\n");
Print("@@FULL_GENERATORS=", List(GeneratorsOfGroup(FullGroup), ImagesList), "\\n");
if Candidate = fail then
  Print("@@CANDIDATE=[]\\n");
else
  Print("@@CANDIDATE=", ImagesList(Candidate), "\\n");
fi;
Print("@@CANDIDATE_2_CHECK=", Candidate2Check, "\\n");
Print("@@CANDIDATE_3_CHECK=", Candidate3Check, "\\n");
Print("@@CHANGED_EDGE=", ChangedEdge, "\\n");
QUIT;
'''


def parse_tagged(stdout: str) -> dict[str, object]:
    parsed: dict[str, object] = {}
    for line in stdout.splitlines():
        if not line.startswith("@@"):
            continue
        key, value = line[2:].split("=", 1)
        parsed[key.lower()] = json.loads(value)
    required = {
        "two_incidence_vertices", "full_incidence_vertices", "edge_counts",
        "two_order", "full_order", "full_subgroup_of_two", "equal",
        "two_generators", "full_generators", "candidate",
        "candidate_2_check", "candidate_3_check", "changed_edge",
    }
    missing = sorted(required - parsed.keys())
    if missing:
        raise RuntimeError(f"missing tagged GAP output: {missing}")
    return parsed


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: compare_colour_groups.py SCHEME.json OUTPUT_PREFIX")
    scheme_path = Path(sys.argv[1])
    prefix = Path(sys.argv[2])
    generated_gap = prefix.with_suffix(".generated.g")
    raw_path = prefix.with_suffix(".raw.txt")
    summary_path = prefix.with_suffix(".summary.json")
    for path in (generated_gap, raw_path, summary_path):
        if path.exists():
            raise SystemExit(f"refusing to overwrite existing output: {path}")

    actual_scheme_hash = sha256(scheme_path)
    if actual_scheme_hash != EXPECTED_SCHEME_SHA256:
        raise SystemExit(f"scheme hash mismatch: {actual_scheme_hash}")
    scheme = json.loads(scheme_path.read_text(encoding="utf-8"))
    assert scheme["group"]["order"] == 504
    assert scheme["group"]["second_smallest_distinct_prime"] == 3
    assert scheme["class"]["size"] == VERTEX_COUNT
    assert scheme["scheme"]["occurring_product_orders"] == [2, 3, 7, 9]

    generated_gap.write_text(build_gap_program(scheme), encoding="utf-8")
    completed = subprocess.run(
        ["gap", "-q", str(generated_gap)],
        text=True,
        capture_output=True,
        timeout=270,
        check=False,
    )
    raw = (
        f"returncode={completed.returncode}\n"
        "--- stdout ---\n" + completed.stdout +
        "--- stderr ---\n" + completed.stderr
    )
    raw_path.write_text(raw, encoding="utf-8")
    if completed.returncode != 0:
        raise SystemExit(f"GAP failed with return code {completed.returncode}; see {raw_path}")

    parsed = parse_tagged(completed.stdout)
    candidate = parsed["candidate"]
    changed = parsed["changed_edge"]
    vertices = scheme["class"]["vertices"]
    enriched: dict[str, object] = {
        "schema": "psl28-two-vs-full-colour-groups-v1",
        "input_scheme": str(scheme_path),
        "input_scheme_sha256": actual_scheme_hash,
        "wrapper_sha256": sha256(Path(__file__)),
        "generated_gap_sha256": sha256(generated_gap),
        "raw_output_sha256": sha256(raw_path),
        "software": {
            "gap": "4.12.1",
            "grape": "4.9.0",
            "nauty_backend": "2.8.8+ds-5",
        },
        **parsed,
    }
    if candidate:
        assert isinstance(candidate, list) and sorted(candidate) == list(range(1, VERTEX_COUNT + 1))
        enriched["candidate_zero_based"] = [x - 1 for x in candidate]
    if changed:
        assert isinstance(changed, list) and len(changed) == 6
        i, j, old, ii, jj, new = changed
        enriched["changed_edge_matrices"] = {
            "source_indices_one_based": [i, j],
            "source_matrices": [vertices[i - 1], vertices[j - 1]],
            "source_product_order": old,
            "image_indices_one_based": [ii, jj],
            "image_matrices": [vertices[ii - 1], vertices[jj - 1]],
            "image_product_order": new,
        }
    summary_path.write_text(json.dumps(enriched, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "two_order": parsed["two_order"],
        "full_order": parsed["full_order"],
        "equal": parsed["equal"],
        "candidate_present": bool(candidate),
        "candidate_2_check": parsed["candidate_2_check"],
        "candidate_3_check": parsed["candidate_3_check"],
        "changed_edge": changed,
        "summary": str(summary_path),
        "raw": str(raw_path),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
