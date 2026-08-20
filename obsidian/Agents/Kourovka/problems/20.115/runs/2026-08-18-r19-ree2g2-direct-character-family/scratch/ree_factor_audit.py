#!/usr/bin/env python3
"""Exact arithmetic checks for the proposed ^2G_2(q) family reduction.

This is not a character-table constructor.  It checks the displayed generic
degree inventory, its sum-of-squares checksum modulo r^2=3q, and the finite
factor-support matrix used in the hand proof.
"""

from fractions import Fraction as Q


def norm(poly):
    out = {}
    for (qe, re), coefficient in poly.items():
        qe += re // 2
        coefficient *= 3 ** (re // 2)
        re %= 2
        out[qe, re] = out.get((qe, re), Q(0)) + coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, Q(0)) + coefficient
    return norm(out)


def scale(coefficient, poly):
    return {monomial: Q(coefficient) * value for monomial, value in poly.items()}


def multiply(left, right):
    out = {}
    for (lq, lr), lc in left.items():
        for (rq, rr), rc in right.items():
            monomial = (lq + rq, lr + rr)
            out[monomial] = out.get(monomial, Q(0)) + lc * rc
    return norm(out)


def power(poly, exponent):
    out = {(0, 0): Q(1)}
    for _ in range(exponent):
        out = multiply(out, poly)
    return out


one = {(0, 0): Q(1)}
q = {(1, 0): Q(1)}
r = {(0, 1): Q(1)}
sub = lambda left, right: add(left, scale(-1, right))
qm = sub(q, one)
qp = add(q, one)
nm = add(q, scale(-1, r), one)
np = add(q, r, one)
d_cyclo = multiply(nm, np)

# (multiplicity, degree), including the two exceptional characters in each of
# the three degree pairs.
inventory = [
    (one, one),
    (one, d_cyclo),
    (scale(2, one), scale(Q(1, 6), multiply(multiply(r, qm), nm))),
    (scale(2, one), scale(Q(1, 6), multiply(multiply(r, qm), np))),
    (scale(2, one), scale(Q(1, 3), multiply(r, multiply(qm, qp)))),
    (scale(Q(1, 6), add(q, r)), multiply(multiply(qm, qp), nm)),
    (scale(Q(1, 6), add(q, scale(-3, one))), multiply(qm, d_cyclo)),
    (one, multiply(q, d_cyclo)),
    (one, power(q, 3)),
    (scale(Q(1, 2), add(q, scale(-3, one))), multiply(qp, d_cyclo)),
    (scale(Q(1, 6), add(q, scale(-1, r))), multiply(multiply(qm, qp), np)),
]

sum_squares = {}
for multiplicity, degree in inventory:
    sum_squares = add(sum_squares, multiply(multiplicity, power(degree, 2)))
group_order = multiply(power(q, 3), multiply(multiply(qm, qp), d_cyclo))
print("sum_square_remainder_mod_r2_minus_3q=", sub(sum_squares, group_order))

# Prime-coordinate support.  For m>=1, 2, 3, u=(q-1)/2,
# a=(q+1)/4, b=q-r+1, c=q+r+1 are pairwise coprime, with u,a,b,c
# odd.  Presence means the codegree contains the entire coordinate; the 2 and
# 3 exponents are separately large enough for the listed element types.
coordinates = frozenset({"2", "3", "u", "a", "b", "c"})
codegree_support = {
    "1": coordinates,
    "D": frozenset({"2", "3", "u", "a"}),
    "E_b": frozenset({"2", "3", "a", "c"}),
    "E_c": frozenset({"2", "3", "a", "b"}),
    "F": frozenset({"3", "b", "c"}),
    "A_b": frozenset({"3", "c"}),
    "B": frozenset({"2", "3", "a"}),
    "qD": frozenset({"2", "3", "u", "a"}),
    "St": frozenset({"2", "u", "a", "b", "c"}),
    "C": frozenset({"2", "3", "u"}),
    "A_c": frozenset({"3", "b"}),
}
element_support = {
    "3-or-9": frozenset({"3"}),
    "involution-2": frozenset({"2"}),
    "mixed-6": frozenset({"2", "3"}),
    # Identity and the involution have already been separated.  Thus every
    # remaining split/A1 class has a nontrivial odd u/a coordinate; a factor
    # 2 may additionally occur but never creates an uncovered cell.
    "split-noncentral": frozenset({"u"}),
    "A1-noncentral": frozenset({"a"}),
    "A2-divisor-b": frozenset({"b"}),
    "A3-divisor-c": frozenset({"c"}),
}
for character, support in codegree_support.items():
    full_defect = coordinates - support
    cells = []
    for element_type, needed in element_support.items():
        missing = needed - support
        result = "SAFE" if not missing else "ZERO_BY_DEFECT:" + ",".join(sorted(missing))
        assert missing <= full_defect
        cells.append(element_type + "=" + result)
    print(character + " | " + " | ".join(cells))

for m in range(1, 5):
    q_value = 3 ** (2 * m + 1)
    r_value = 3 ** (m + 1)
    multiplicities = [
        1, 1, 2, 2, 2,
        (q_value + r_value) // 6,
        (q_value - 3) // 6,
        1, 1,
        (q_value - 3) // 2,
        (q_value - r_value) // 6,
    ]
    print("q=", q_value, "character_count=", sum(multiplicities), "expected=", q_value + 8)
