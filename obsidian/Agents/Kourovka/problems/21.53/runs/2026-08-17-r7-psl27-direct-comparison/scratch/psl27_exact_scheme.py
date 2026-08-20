#!/usr/bin/env python3
"""Exact PSL(2,7) group/class/product-order certificate.

Elements are determinant-one 2x2 matrices over F_7 modulo the central pair
{I,-I}.  Each projective element is represented by the lexicographically smaller
of A and -A.  The program uses only integer arithmetic and exhaustive finite loops.
"""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from itertools import product
from pathlib import Path


P = 7
HERE = Path(__file__).resolve().parent


def neg(a: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return tuple((-x) % P for x in a)  # type: ignore[return-value]


def canon(a: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    b = neg(a)
    return min(a, b)


def det(a: tuple[int, int, int, int]) -> int:
    x, y, z, w = a
    return (x * w - y * z) % P


def mul(
    a: tuple[int, int, int, int], b: tuple[int, int, int, int]
) -> tuple[int, int, int, int]:
    x, y, z, w = a
    r, s, t, u = b
    return canon(
        (
            (x * r + y * t) % P,
            (x * s + y * u) % P,
            (z * r + w * t) % P,
            (z * s + w * u) % P,
        )
    )


def inv(a: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    x, y, z, w = a
    return canon((w, (-y) % P, (-z) % P, x))


IDENTITY = canon((1, 0, 0, 1))


def order(a: tuple[int, int, int, int]) -> int:
    x = IDENTITY
    for n in range(1, 169):
        x = mul(x, a)
        if x == IDENTITY:
            return n
    raise AssertionError("Lagrange bound failed")


sl2 = [
    a
    for a in product(range(P), repeat=4)
    if det(a) == 1
]
elements = sorted({canon(a) for a in sl2})
assert len(sl2) == 336
assert len(elements) == 168
element_set = set(elements)
assert IDENTITY in element_set
assert all(mul(a, b) in element_set for a in elements for b in elements)
assert all(mul(a, inv(a)) == IDENTITY for a in elements)

orders = {a: order(a) for a in elements}
order_counts = Counter(orders.values())


# Exact conjugacy-class partition.
unseen = set(elements)
classes: list[list[tuple[int, int, int, int]]] = []
while unseen:
    x = min(unseen)
    cl = sorted({mul(mul(inv(g), x), g) for g in elements})
    assert set(cl) <= unseen
    classes.append(cl)
    unseen -= set(cl)
classes.sort(key=lambda cl: (orders[cl[0]], len(cl), cl[0]))
assert sum(map(len, classes)) == 168
assert all(len({orders[x] for x in cl}) == 1 for cl in classes)


# Simplicity certificate: every normal subgroup is a union of conjugacy classes.
identity_class_index = next(i for i, cl in enumerate(classes) if IDENTITY in cl)
other_class_indices = [i for i in range(len(classes)) if i != identity_class_index]
normal_subgroup_sizes: list[int] = []
normal_union_masks_tested = 0
for bits in range(1 << len(other_class_indices)):
    selected = {identity_class_index}
    for j, class_index in enumerate(other_class_indices):
        if bits & (1 << j):
            selected.add(class_index)
    candidate = {x for i in selected for x in classes[i]}
    normal_union_masks_tested += 1
    if not all(inv(x) in candidate for x in candidate):
        continue
    if not all(mul(x, y) in candidate for x in candidate for y in candidate):
        continue
    normal_subgroup_sizes.append(len(candidate))
assert normal_subgroup_sizes == [1, 168]


# A displayed noncommuting pair.
noncommuting_pair = next(
    (a, b) for a in elements for b in elements if mul(a, b) != mul(b, a)
)


involutions = sorted(a for a in elements if orders[a] == 2)
involution_classes = [cl for cl in classes if orders[cl[0]] == 2]
assert len(involutions) == 21
assert len(involution_classes) == 1
assert involutions == involution_classes[0]


# Complete 21 x 21 product-order matrix and all 210 unordered edges.
n = len(involutions)
matrix = [[order(mul(involutions[i], involutions[j])) for j in range(n)] for i in range(n)]
assert all(matrix[i][i] == 1 for i in range(n))
assert all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n))
edges = [
    {"i": i + 1, "j": j + 1, "order": matrix[i][j]}
    for i in range(n)
    for j in range(i + 1, n)
]
edge_colour_counts = Counter(e["order"] for e in edges)
colour_valencies = {
    colour: [sum(matrix[i][j] == colour for j in range(n) if j != i) for i in range(n)]
    for colour in sorted(edge_colour_counts)
}
assert sum(edge_colour_counts.values()) == 210
assert all(len(set(vals)) == 1 for vals in colour_valencies.values())


def digest(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(raw).hexdigest()


vertex_records = [
    {"vertex": i + 1, "matrix_mod_7_up_to_sign": list(a)}
    for i, a in enumerate(involutions)
]
class_records = [
    {
        "order": orders[cl[0]],
        "size": len(cl),
        "representative": list(cl[0]),
    }
    for cl in classes
]

certificate = {
    "model": "PSL(2,7)=SL(2,7)/{+I,-I}",
    "canonical_representative": "lexicographically smaller of A and -A mod 7",
    "sl2_matrix_count": len(sl2),
    "projective_group_order": len(elements),
    "prime_factorization": {"2": 3, "3": 1, "7": 1},
    "second_smallest_distinct_prime": 3,
    "nonabelian_witness": {
        "a": list(noncommuting_pair[0]),
        "b": list(noncommuting_pair[1]),
        "ab": list(mul(*noncommuting_pair)),
        "ba": list(mul(noncommuting_pair[1], noncommuting_pair[0])),
    },
    "element_order_counts": {str(k): order_counts[k] for k in sorted(order_counts)},
    "conjugacy_classes": class_records,
    "normal_class_unions_tested": normal_union_masks_tested,
    "normal_subgroup_sizes": normal_subgroup_sizes,
    "involution_count": len(involutions),
    "involution_class_count": len(involution_classes),
    "involution_vertices": vertex_records,
    "product_order_matrix": matrix,
    "unordered_edges": edges,
    "occurring_edge_colours": sorted(edge_colour_counts),
    "edge_colour_counts": {str(k): edge_colour_counts[k] for k in sorted(edge_colour_counts)},
    "colour_valencies_by_vertex": {
        str(k): colour_valencies[k] for k in sorted(colour_valencies)
    },
    "digests": {
        "projective_elements_sha256": digest([list(a) for a in elements]),
        "involution_vertices_sha256": digest(vertex_records),
        "product_order_matrix_sha256": digest(matrix),
        "unordered_edges_sha256": digest(edges),
    },
}

certificate_path = HERE / "psl27_exact_scheme_certificate.json"
matrix_path = HERE / "psl27_product_order_matrix.csv"
certificate_path.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
with matrix_path.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["vertex"] + list(range(1, n + 1)))
    for i, row in enumerate(matrix, start=1):
        writer.writerow([i] + row)

print("MODEL=PSL(2,7)=SL(2,7)/{+I,-I}")
print(f"SL2_MATRIX_COUNT={len(sl2)}")
print(f"GROUP_ORDER={len(elements)}")
print(f"ELEMENT_ORDER_COUNTS={dict(sorted(order_counts.items()))}")
print(f"CONJUGACY_CLASS_ORDER_SIZE={[(orders[cl[0]], len(cl)) for cl in classes]}")
print(f"NORMAL_CLASS_UNIONS_TESTED={normal_union_masks_tested}")
print(f"NORMAL_SUBGROUP_SIZES={normal_subgroup_sizes}")
print(f"NONABELIAN_WITNESS={certificate['nonabelian_witness']}")
print(f"INVOLUTION_COUNT={len(involutions)}")
print(f"INVOLUTION_CLASS_COUNT={len(involution_classes)}")
print(f"EDGE_COLOURS={sorted(edge_colour_counts)}")
print(f"EDGE_COLOUR_COUNTS={dict(sorted(edge_colour_counts.items()))}")
print(f"COLOUR_VALENCIES={{k: v[0] for k, v in colour_valencies.items()}}")
print(f"COLOUR_VALENCIES={{{', '.join(f'{k}: {v[0]}' for k, v in sorted(colour_valencies.items()))}}}")
print(f"DIGESTS={certificate['digests']}")
print(f"CERTIFICATE={certificate_path.name}")
print(f"MATRIX_CSV={matrix_path.name}")
