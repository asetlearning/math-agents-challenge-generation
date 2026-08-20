#!/usr/bin/env python3
"""Exact full two-point product-order arrays for rank-two involutions in GL(4,2).

This is a deliberately small, dependency-free finite model for Kourovka 21.52.
Matrices are 16-bit integers in row-major order; all arithmetic is over F_2.
The script writes one deterministic JSON certificate and performs internal checks.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


DIM = 4
FIELD_VECTOR_COUNT = 1 << DIM
MATRIX_COUNT = 1 << (DIM * DIM)
GL4_ORDER = 20160
IDENTITY = sum(1 << (r * DIM + r) for r in range(DIM))


def row(matrix: int, r: int) -> int:
    return (matrix >> (r * DIM)) & (FIELD_VECTOR_COUNT - 1)


def multiply(a: int, b: int) -> int:
    """Return a*b over F_2."""
    out = 0
    for r in range(DIM):
        arow = row(a, r)
        product_row = 0
        for k in range(DIM):
            if (arow >> k) & 1:
                product_row ^= row(b, k)
        out |= product_row << (r * DIM)
    return out


def apply(matrix: int, vector: int) -> int:
    out = 0
    for r in range(DIM):
        out |= ((row(matrix, r) & vector).bit_count() & 1) << r
    return out


def rank(matrix: int) -> int:
    rows = [row(matrix, r) for r in range(DIM)]
    pivot_row = 0
    for column in range(DIM):
        pivot = next(
            (r for r in range(pivot_row, DIM) if (rows[r] >> column) & 1),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        for r in range(DIM):
            if r != pivot_row and ((rows[r] >> column) & 1):
                rows[r] ^= rows[pivot_row]
        pivot_row += 1
    return pivot_row


def subspace_mask(vectors: set[int]) -> int:
    return sum(1 << v for v in vectors)


def flag(matrix: int) -> tuple[int, int]:
    image = {apply(matrix, v) for v in range(FIELD_VECTOR_COUNT)}
    kernel = {v for v in range(FIELD_VECTOR_COUNT) if apply(matrix, v) == 0}
    return subspace_mask(image), subspace_mask(kernel)


def matrix_order(matrix: int) -> int:
    if matrix == IDENTITY:
        return 1
    power = matrix
    exponent = 1
    while power != IDENTITY:
        power = multiply(power, matrix)
        exponent += 1
        if exponent > GL4_ORDER:
            raise AssertionError("matrix order exceeded |GL(4,2)|")
    if GL4_ORDER % exponent != 0:
        raise AssertionError("matrix order does not divide |GL(4,2)|")
    return exponent


def product_order(p: int, q: int) -> int:
    return matrix_order(multiply(IDENTITY ^ p, IDENTITY ^ q))


def transpose_array(signature: tuple[int, ...], size: int) -> tuple[int, ...]:
    return tuple(signature[j * size + i] for i in range(size) for j in range(size))


def canonical_array(signature: tuple[int, ...], size: int) -> tuple[int, ...]:
    return min(signature, transpose_array(signature, size))


def nonzero_cells(
    signature: tuple[int, ...], palette: list[int]
) -> list[dict[str, int]]:
    size = len(palette)
    cells: list[dict[str, int]] = []
    for i, left_colour in enumerate(palette):
        for j, right_colour in enumerate(palette):
            count = signature[i * size + j]
            if count:
                cells.append({"i": left_colour, "j": right_colour, "count": count})
    return cells


def matrix_record(matrix: int) -> dict[str, object]:
    image, kernel = flag(matrix)
    return {
        "hex": f"0x{matrix:04x}",
        "rows_binary": [f"{row(matrix, r):04b}" for r in range(DIM)],
        "image_vector_mask_hex": f"0x{image:04x}",
        "kernel_vector_mask_hex": f"0x{kernel:04x}",
    }


def histogram_records(
    histogram: Counter[tuple[int, ...]], palette: list[int]
) -> list[dict[str, object]]:
    return [
        {
            "multiplicity": histogram[signature],
            "nonzero_cells": nonzero_cells(signature, palette),
        }
        for signature in sorted(histogram)
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    vertices = [
        matrix
        for matrix in range(MATRIX_COUNT)
        if multiply(matrix, matrix) == 0 and rank(matrix) == 2
    ]
    assert len(vertices) == 210
    assert len(set(vertices)) == 210

    flags = [flag(matrix) for matrix in vertices]
    fibres: dict[tuple[int, int], list[int]] = defaultdict(list)
    for index, vertex_flag in enumerate(flags):
        fibres[vertex_flag].append(index)
    assert len(fibres) == 35
    assert sorted(map(len, fibres.values())) == [6] * 35
    assert all(image == kernel for image, kernel in flags)

    vertex_count = len(vertices)
    colours = [bytearray(vertex_count) for _ in range(vertex_count)]
    for p in range(vertex_count):
        colours[p][p] = 1
        for q in range(p + 1, vertex_count):
            colour = product_order(vertices[p], vertices[q])
            assert GL4_ORDER % colour == 0
            colours[p][q] = colour
            colours[q][p] = colour

    palette = sorted({colour for colour_row in colours for colour in colour_row})
    palette_index = {colour: index for index, colour in enumerate(palette)}
    palette_size = len(palette)

    same_histogram: Counter[tuple[int, ...]] = Counter()
    cross_histogram: Counter[tuple[int, ...]] = Counter()
    same_excluded_histogram: Counter[tuple[int, ...]] = Counter()
    cross_excluded_histogram: Counter[tuple[int, ...]] = Counter()
    first_witness: dict[
        str, dict[tuple[int, ...], tuple[int, int, tuple[int, ...]]]
    ] = {"same": {}, "cross": {}}
    colour_two_pair_count = 0
    same_pair_count = 0
    cross_pair_count = 0

    for p in range(vertex_count):
        for q in range(p + 1, vertex_count):
            if colours[p][q] != 2:
                continue
            colour_two_pair_count += 1
            is_same = flags[p] == flags[q]
            if is_same:
                same_pair_count += 1
            else:
                cross_pair_count += 1

            counts = [0] * (palette_size * palette_size)
            excluded_counts = [0] * (palette_size * palette_size)
            for t in range(vertex_count):
                cell = (
                    palette_index[colours[p][t]] * palette_size
                    + palette_index[colours[q][t]]
                )
                counts[cell] += 1
                if t != p and t != q:
                    excluded_counts[cell] += 1

            raw = tuple(counts)
            raw_excluded = tuple(excluded_counts)
            assert sum(raw) == 210
            assert sum(raw_excluded) == 208
            canonical = canonical_array(raw, palette_size)
            canonical_excluded = canonical_array(raw_excluded, palette_size)
            kind = "same" if is_same else "cross"
            histogram = same_histogram if is_same else cross_histogram
            excluded_histogram = (
                same_excluded_histogram if is_same else cross_excluded_histogram
            )
            histogram[canonical] += 1
            excluded_histogram[canonical_excluded] += 1
            first_witness[kind].setdefault(canonical, (p, q, raw))

    assert same_pair_count == 35 * 15
    assert colour_two_pair_count == same_pair_count + cross_pair_count
    assert all(
        colours[p][q] == 2
        for fibre in fibres.values()
        for offset, p in enumerate(fibre)
        for q in fibre[offset + 1 :]
    )

    intersection = set(same_histogram) & set(cross_histogram)
    excluded_intersection = set(same_excluded_histogram) & set(
        cross_excluded_histogram
    )
    # Including or excluding the two endpoints changes every colour-2 pair by the
    # same two cells (1,2) and (2,1), hence the gate result must agree.
    assert bool(intersection) == bool(excluded_intersection)

    certificate: dict[str, object] = {
        "model": "all rank-2 square-zero 4x4 matrices over F_2; I+N in GL(4,2)=PSL(4,2)",
        "matrix_encoding": "16-bit row-major, low nibble is row 0; vectors are 4-bit columns",
        "vertex_count": vertex_count,
        "bare_flag_fibre_count": len(fibres),
        "vertices_per_fibre": 6,
        "product_order_palette_including_diagonal": palette,
        "edge_product_order_palette": [colour for colour in palette if colour != 1],
        "colour_two_pair_count": colour_two_pair_count,
        "same_fibre_colour_two_pair_count": same_pair_count,
        "cross_fibre_colour_two_pair_count": cross_pair_count,
        "array_convention": (
            "S_ij counts all 210 T, including endpoints; signatures of unordered "
            "pairs are canonicalized up to transposition. Endpoint-excluded arrays "
            "were checked separately and give the same collision/separation gate."
        ),
        "same_signature_type_count": len(same_histogram),
        "cross_signature_type_count": len(cross_histogram),
        "shared_signature_type_count": len(intersection),
        "gate_result": "FULL_ARRAY_COLLISION" if intersection else "FIBRE_SEPARATION",
        "same_signature_histogram": histogram_records(same_histogram, palette),
        "cross_signature_histogram": histogram_records(cross_histogram, palette),
        "endpoint_excluded_gate_agrees": True,
    }

    if intersection:
        shared = min(intersection)
        same_p, same_q, same_raw = first_witness["same"][shared]
        cross_p, cross_q, cross_raw = first_witness["cross"][shared]

        # Orient both witnesses so their displayed arrays equal the shared
        # canonical array, swapping endpoints when transposition is needed.
        if same_raw != shared:
            assert transpose_array(same_raw, palette_size) == shared
            same_p, same_q = same_q, same_p
        if cross_raw != shared:
            assert transpose_array(cross_raw, palette_size) == shared
            cross_p, cross_q = cross_q, cross_p

        certificate["collision"] = {
            "full_array_nonzero_cells": nonzero_cells(shared, palette),
            "same_fibre_pair": {
                "P_index": same_p,
                "Q_index": same_q,
                "P": matrix_record(vertices[same_p]),
                "Q": matrix_record(vertices[same_q]),
                "edge_product_order": colours[same_p][same_q],
                "same_flag": flags[same_p] == flags[same_q],
            },
            "cross_fibre_pair": {
                "P_index": cross_p,
                "Q_index": cross_q,
                "P": matrix_record(vertices[cross_p]),
                "Q": matrix_record(vertices[cross_q]),
                "edge_product_order": colours[cross_p][cross_q],
                "same_flag": flags[cross_p] == flags[cross_q],
            },
        }

    output = Path(args.output)
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
