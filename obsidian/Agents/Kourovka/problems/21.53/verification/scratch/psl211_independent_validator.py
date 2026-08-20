#!/usr/bin/env python3
"""Independent bounded certificate checker for the fixed PSL(2,11) report.

This script deliberately does not import or execute claimant code.  It constructs
SL(2,11)/{+-I} from four-tuples, proves simplicity by normal closures of all
nonidentity conjugacy classes, reconstructs all involution-pair product orders,
checks the claimant's immutable data artifacts byte-for-byte, and emits two
vertex-coloured incidence graphs for an independent dreadnaut computation.
"""

from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
import json
from pathlib import Path
import re
import sys


Q = 11
Mat = tuple[int, int, int, int]
IDENTITY: Mat = (1, 0, 0, 1)
NEG_IDENTITY: Mat = (10, 0, 0, 10)

VAULT = Path.cwd()
CLAIM_DIR = VAULT / "Agents/Kourovka/problems/21.53/runs/2026-08-17-r3-psl211-two-colour-separation/scratch"
OUT_DIR = VAULT / "Agents/Kourovka/problems/21.53/verification/scratch/psl211"


def mmul(x: Mat, y: Mat) -> Mat:
    a, b, c, d = x
    e, f, g, h = y
    return (
        (a * e + b * g) % Q,
        (a * f + b * h) % Q,
        (c * e + d * g) % Q,
        (c * f + d * h) % Q,
    )


def mneg(x: Mat) -> Mat:
    return tuple((-a) % Q for a in x)  # type: ignore[return-value]


def canon(x: Mat) -> Mat:
    y = mneg(x)
    return x if x < y else y


def qmul(x: Mat, y: Mat) -> Mat:
    return canon(mmul(x, y))


def qinv(x: Mat) -> Mat:
    a, b, c, d = x
    return canon((d, (-b) % Q, (-c) % Q, a))


def digest(data: bytes) -> str:
    return sha256(data).hexdigest()


def generated_subgroup(generators: set[Mat]) -> set[Mat]:
    steps = sorted(generators | {qinv(g) for g in generators})
    seen = {IDENTITY}
    queue: deque[Mat] = deque([IDENTITY])
    while queue:
        x = queue.popleft()
        for g in steps:
            y = qmul(x, g)
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen


def element_order(x: Mat) -> int:
    y = IDENTITY
    for n in range(1, 661):
        y = qmul(y, x)
        if y == IDENTITY:
            return n
    raise AssertionError(f"order exceeded group order for {x}")


def dreadnaut_incidence(edge_lists: list[list[tuple[int, int]]]) -> tuple[str, int, int]:
    """Encode labelled binary relations as a vertex-coloured incidence graph.

    Original points are 0..54.  Each relation gets its own partition cell of
    degree-two vertices, one for each unordered pair.  Therefore restriction to
    the original cell identifies the incidence automorphism group exactly with
    the common relation automorphism group.
    """

    next_vertex = 55
    cells = ["0:54"]
    graph_lines = ["As", "n=0 g"]  # n is replaced after all cells are counted.
    incidence_edges = 0
    for relation in edge_lists:
        first = next_vertex
        for i, j in relation:
            graph_lines.append(f"{next_vertex}: {i} {j};")
            next_vertex += 1
            incidence_edges += 2
        last = next_vertex - 1
        assert last >= first
        cells.append(str(first) if first == last else f"{first}:{last}")
    graph_lines[1] = f"n={next_vertex} g"
    graph_lines.extend([".", "f=[" + "|".join(cells) + "]", "x", "q", ""])
    return "\n".join(graph_lines), next_vertex, incidence_edges


def main() -> None:
    assert Q == 11 and all(Q % p for p in range(2, 4))

    sl2 = sorted(
        (a, b, c, d)
        for a in range(Q)
        for b in range(Q)
        for c in range(Q)
        for d in range(Q)
        if (a * d - b * c) % Q == 1
    )
    sl2_set = set(sl2)
    assert len(sl2) == 1320
    assert IDENTITY in sl2_set and NEG_IDENTITY in sl2_set

    # Direct centre computation in SL(2,11), with no group-library naming step.
    centre = [x for x in sl2 if all(mmul(x, y) == mmul(y, x) for y in sl2)]
    assert centre == [IDENTITY, NEG_IDENTITY]

    group = sorted({canon(x) for x in sl2})
    group_set = set(group)
    assert len(group) == 660
    assert all(qmul(x, IDENTITY) == x == qmul(IDENTITY, x) for x in group)
    assert all(qmul(x, qinv(x)) == IDENTITY == qmul(qinv(x), x) for x in group)
    closure_pairs = 0
    for x in group:
        for y in group:
            assert qmul(x, y) in group_set
            closure_pairs += 1
    assert closure_pairs == 660 * 660

    s = canon((0, 1, 10, 0))
    u = canon((1, 1, 0, 1))
    generated = generated_subgroup({s, u})
    assert len(generated) == 660
    generators_noncommute = qmul(s, u) != qmul(u, s)
    assert generators_noncommute

    order_of = {x: element_order(x) for x in group}
    unseen = set(group)
    classes: list[list[Mat]] = []
    while unseen:
        representative = min(unseen)
        conjugates = sorted({qmul(qmul(g, representative), qinv(g)) for g in group})
        assert representative in conjugates
        assert set(conjugates) <= unseen
        classes.append(conjugates)
        unseen.difference_update(conjugates)
    class_data = [
        {
            "representative": list(cls[0]),
            "element_order": order_of[cls[0]],
            "class_size": len(cls),
            "normal_closure_size": len(generated_subgroup(set(cls))),
        }
        for cls in classes
    ]
    class_data.sort(key=lambda row: (row["element_order"], row["representative"]))
    assert len(classes) == 8
    assert sorted(row["normal_closure_size"] for row in class_data) == [1] + [660] * 7
    assert sum(len(cls) for cls in classes) == 660

    involution_classes = [cls for cls in classes if order_of[cls[0]] == 2]
    involutions = sorted(x for x in group if order_of[x] == 2)
    assert len(involution_classes) == 1
    assert len(involutions) == 55
    assert involutions == involution_classes[0]
    involution_centralizer = [g for g in group if qmul(g, involutions[0]) == qmul(involutions[0], g)]
    assert len(involution_centralizer) == 12

    edges: list[tuple[int, int, int]] = []
    matrix = [[1 if i == j else 0 for j in range(55)] for i in range(55)]
    valencies = [Counter() for _ in range(55)]
    by_colour: dict[int, list[tuple[int, int]]] = {}
    for i in range(55):
        for j in range(i + 1, 55):
            colour = order_of[qmul(involutions[i], involutions[j])]
            edges.append((i + 1, j + 1, colour))
            matrix[i][j] = matrix[j][i] = colour
            valencies[i][colour] += 1
            valencies[j][colour] += 1
            by_colour.setdefault(colour, []).append((i, j))
    assert len(edges) == 1485
    colours = sorted(by_colour)
    assert colours == [2, 3, 5, 6]
    edge_counts = {c: len(by_colour[c]) for c in colours}
    assert edge_counts == {2: 165, 3: 330, 5: 660, 6: 330}
    expected_valency = {2: 6, 3: 12, 5: 24, 6: 12}
    assert all(dict(v) == expected_valency for v in valencies)
    assert sum(edge_counts.values()) == 1485
    assert all(matrix[i][j] == matrix[j][i] for i in range(55) for j in range(55))
    assert all(matrix[i][i] == 1 for i in range(55))

    vertex_text = "index\ta00\ta01\ta10\ta11\n" + "".join(
        f"{i}\t{a}\t{b}\t{c}\t{d}\n"
        for i, (a, b, c, d) in enumerate(involutions, start=1)
    )
    edge_text = "i\tj\tproduct_order\n" + "".join(
        f"{i}\t{j}\t{colour}\n" for i, j, colour in edges
    )
    matrix_text = "vertex," + ",".join(str(i) for i in range(1, 56)) + "\n" + "".join(
        str(i + 1) + "," + ",".join(str(x) for x in row) + "\n"
        for i, row in enumerate(matrix)
    )
    regenerated = {
        "vertices.tsv": vertex_text.encode(),
        "unordered_edges.tsv": edge_text.encode(),
        "product_order_matrix.csv": matrix_text.encode(),
    }

    artifact_checks: dict[str, dict[str, object]] = {}
    for filename, expected_bytes in regenerated.items():
        actual_bytes = (CLAIM_DIR / filename).read_bytes()
        artifact_checks[filename] = {
            "byte_identical": actual_bytes == expected_bytes,
            "independent_sha256": digest(expected_bytes),
            "claimant_sha256": digest(actual_bytes),
        }
        assert actual_bytes == expected_bytes

    claimant_summary = json.loads((CLAIM_DIR / "summary.json").read_text())
    summary_expectations = {
        "field_order": 11,
        "sl2_order": 1320,
        "quotient_order": 660,
        "generated_subgroup_order": 660,
        "generators_noncommute": True,
        "involution_count": 55,
        "involution_class_count": 1,
        "involution_class_sizes": [55],
        "involution_centralizer_order": 12,
        "distinct_prime_divisors": [2, 3, 5, 11],
        "second_smallest_distinct_prime": 3,
        "unordered_pair_count": 1485,
        "occurring_edge_colours": [2, 3, 5, 6],
        "edge_count_by_colour": {"2": 165, "3": 330, "5": 660, "6": 330},
        "valency_by_colour": {"2": 6, "3": 12, "5": 24, "6": 12},
        "matrix_diagonal": 1,
        "vertex_order": "lexicographic canonical matrix tuple",
    }
    summary_fields_match = all(claimant_summary.get(k) == v for k, v in summary_expectations.items())
    assert summary_fields_match
    assert claimant_summary["conjugacy_classes"] == class_data

    frozen_manifest = (CLAIM_DIR / "frozen-manifest.md").read_text()
    frozen_hashes = dict(re.findall(r"\| `([^`]+)` \| `([0-9a-f]{64})` \|", frozen_manifest))
    assert len(frozen_hashes) == 7
    frozen_hash_checks = {
        name: {
            "manifest_sha256": recorded,
            "actual_sha256": digest((CLAIM_DIR / name).read_bytes()),
            "match": digest((CLAIM_DIR / name).read_bytes()) == recorded,
        }
        for name, recorded in frozen_hashes.items()
    }
    assert all(row["match"] for row in frozen_hash_checks.values())

    two_dre, two_vertices, two_incidence_edges = dreadnaut_incidence(
        [by_colour[2], by_colour[3]]
    )
    full_dre, full_vertices, full_incidence_edges = dreadnaut_incidence(
        [by_colour[2], by_colour[3], by_colour[5], by_colour[6]]
    )
    assert (two_vertices, two_incidence_edges) == (550, 990)
    assert (full_vertices, full_incidence_edges) == (1540, 2970)

    independent_summary = {
        "python": sys.version.split()[0],
        "construction": "direct SL(2,11)/{+-I} tuple arithmetic",
        "sl2_order": len(sl2),
        "sl2_centre": [list(x) for x in centre],
        "quotient_order": len(group),
        "closure_pairs_checked": closure_pairs,
        "generator_subgroup_order": len(generated),
        "generators_noncommute": generators_noncommute,
        "conjugacy_classes": class_data,
        "simple_by_all_nonidentity_class_normal_closures": True,
        "involution_count": len(involutions),
        "involution_class_count": len(involution_classes),
        "involution_centralizer_order": len(involution_centralizer),
        "prime_factorization": {"2": 2, "3": 1, "5": 1, "11": 1},
        "second_smallest_distinct_prime": 3,
        "unordered_pairs_checked": len(edges),
        "colours": colours,
        "edge_counts": edge_counts,
        "valencies": expected_valency,
        "aut_t_vacuity": "for every positive t outside {2,3,5,6}, Aut_t=S_55",
        "indexing": "1-based lexicographic canonical matrix tuples; pairs i<j lexicographically",
        "artifact_checks": artifact_checks,
        "claimant_summary_fields_match": summary_fields_match,
        "frozen_hash_checks": frozen_hash_checks,
        "two_incidence_graph": {
            "vertices": two_vertices,
            "incidence_edges": two_incidence_edges,
            "partition_cells": [55, 165, 330],
            "sha256": digest(two_dre.encode()),
        },
        "full_incidence_graph": {
            "vertices": full_vertices,
            "incidence_edges": full_incidence_edges,
            "partition_cells": [55, 165, 330, 660, 330],
            "sha256": digest(full_dre.encode()),
        },
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "validator_vertices.tsv").write_bytes(regenerated["vertices.tsv"])
    (OUT_DIR / "validator_unordered_edges.tsv").write_bytes(regenerated["unordered_edges.tsv"])
    (OUT_DIR / "validator_product_order_matrix.csv").write_bytes(regenerated["product_order_matrix.csv"])
    (OUT_DIR / "two_relations.dre").write_text(two_dre)
    (OUT_DIR / "full_colours.dre").write_text(full_dre)
    (OUT_DIR / "independent_summary.json").write_text(
        json.dumps(independent_summary, indent=2, sort_keys=True) + "\n"
    )

    print("PSL211_INDEPENDENT_MODEL_OK")
    print(f"PYTHON={sys.version.split()[0]}")
    print(f"SL2_ORDER={len(sl2)}")
    print(f"SL2_CENTRE={centre}")
    print(f"QUOTIENT_ORDER={len(group)}")
    print(f"CLOSURE_PAIRS_CHECKED={closure_pairs}")
    print(f"GENERATOR_SUBGROUP_ORDER={len(generated)}")
    print(f"GENERATORS_NONCOMMUTE={str(generators_noncommute).lower()}")
    print("CLASS_ORDER_SIZE_NORMAL_CLOSURE=" + str([
        (row["element_order"], row["class_size"], row["normal_closure_size"])
        for row in class_data
    ]))
    print("SIMPLE_BY_NORMAL_CLOSURES=true")
    print(f"INVOLUTION_COUNT={len(involutions)}")
    print(f"INVOLUTION_CLASS_COUNT={len(involution_classes)}")
    print(f"INVOLUTION_CENTRALIZER_ORDER={len(involution_centralizer)}")
    print("PRIME_FACTORIZATION=2^2*3*5*11")
    print("SECOND_SMALLEST_DISTINCT_PRIME=3")
    print(f"UNORDERED_PAIRS_CHECKED={len(edges)}")
    print(f"COLOURS={colours}")
    print(f"EDGE_COUNTS={edge_counts}")
    print(f"VALENCIES={expected_valency}")
    print("AUT_T_VACUITY=all absent positive labels impose no restriction, hence S_55")
    for filename, row in artifact_checks.items():
        print(
            f"ARTIFACT_BYTE_IDENTICAL[{filename}]={str(row['byte_identical']).lower()} "
            f"SHA256={row['independent_sha256']}"
        )
    print(f"CLAIMANT_SUMMARY_FIELDS_MATCH={str(summary_fields_match).lower()}")
    print(f"FROZEN_HASHES_ALL_MATCH={str(all(row['match'] for row in frozen_hash_checks.values())).lower()}")
    print(f"TWO_INCIDENCE_VERTICES={two_vertices}")
    print(f"TWO_INCIDENCE_EDGES={two_incidence_edges}")
    print(f"TWO_DREADNAUT_SHA256={digest(two_dre.encode())}")
    print(f"FULL_INCIDENCE_VERTICES={full_vertices}")
    print(f"FULL_INCIDENCE_EDGES={full_incidence_edges}")
    print(f"FULL_DREADNAUT_SHA256={digest(full_dre.encode())}")


if __name__ == "__main__":
    main()
