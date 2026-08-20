#!/usr/bin/env python3
"""Exact subgroup computation in a small truncated F_2-algebra.

Let J have basis the words of lengths 1, 2, 3 on {a,b,c,d} with no
adjacent repeated letter, with concatenation, x_i^2=0, and J^4=0.
This computes H=<1+a,1+b,1+c,1+d> <= 1+J without enumerating H: it
enumerates H/(H intersect (1+J^3)), then obtains the central kernel from
Schreier edge cycles as an F_2-vector space.
"""

from collections import deque
from itertools import product

LETTERS = "abcd"
WORDS = []
for length in (1, 2, 3):
    for word in product(range(4), repeat=length):
        if all(word[i] != word[i + 1] for i in range(length - 1)):
            WORDS.append(word)

INDEX = {word: i for i, word in enumerate(WORDS)}
DEGREE3_MASK = sum(1 << i for i, word in enumerate(WORDS) if len(word) == 3)
LOW_MASK = ((1 << len(WORDS)) - 1) ^ DEGREE3_MASK


def set_bits(bits):
    while bits:
        low = bits & -bits
        yield low.bit_length() - 1
        bits ^= low


def algebra_product(left, right):
    out = 0
    for i in set_bits(left):
        u = WORDS[i]
        for j in set_bits(right):
            v = WORDS[j]
            if len(u) + len(v) >= 4 or u[-1] == v[0]:
                continue
            out ^= 1 << INDEX[u + v]
    return out


def group_product(left, right):
    # (1+left)(1+right) = 1 + left + right + left*right in characteristic 2.
    return left ^ right ^ algebra_product(left, right)


def group_inverse(value):
    square = algebra_product(value, value)
    cube = algebra_product(square, value)
    return value ^ square ^ cube


def add_to_basis(value, basis):
    original = value
    while value:
        pivot = value.bit_length() - 1
        if pivot in basis:
            value ^= basis[pivot]
        else:
            # Keep a reduced pivot dictionary for deterministic output.
            for old_pivot, old_value in list(basis.items()):
                if (old_value >> pivot) & 1:
                    basis[old_pivot] = old_value ^ value
            basis[pivot] = value
            return True, original
    return False, original


def format_vector(value):
    return "+".join("".join(LETTERS[k] for k in WORDS[i]) for i in set_bits(value)) or "0"


def main():
    generators = [1 << INDEX[(i,)] for i in range(4)]
    reps = {0: 0}
    queue = deque([0])
    kernel_basis = {}
    cycle_count = 0

    while queue:
        quotient_value = queue.popleft()
        representative = reps[quotient_value]
        for generator in generators:
            candidate = group_product(representative, generator)
            candidate_quotient = candidate & LOW_MASK
            if candidate_quotient not in reps:
                reps[candidate_quotient] = candidate
                queue.append(candidate_quotient)
            else:
                cycle_count += 1
                difference = group_product(group_inverse(reps[candidate_quotient]), candidate)
                assert difference & LOW_MASK == 0
                add_to_basis(difference, kernel_basis)

    # Direct generator and centrality checks used by the construction.
    assert all(group_product(g, g) == 0 for g in generators)
    for value in kernel_basis.values():
        assert value & LOW_MASK == 0
        assert all(group_product(value, g) == group_product(g, value) for g in generators)

    kernel_vectors = sorted(kernel_basis.values(), key=lambda x: x.bit_length())
    exponent = (len(reps).bit_length() - 1) + len(kernel_vectors)
    assert len(reps) == 1 << (len(reps).bit_length() - 1)

    print(f"algebra_dimension={len(WORDS)}")
    print(f"degree_dimensions=4,12,36")
    print(f"quotient_states={len(reps)}")
    print(f"schreier_edges_checked={cycle_count}")
    print(f"central_kernel_rank={len(kernel_vectors)}")
    print(f"subgroup_order=2^{exponent}")
    print("central_kernel_basis:")
    for value in kernel_vectors:
        print(format_vector(value))


if __name__ == "__main__":
    main()
