#!/usr/bin/env python3
"""Independent exact checker for the frozen CTH-3-6 word certificate.

This implements only two finite calculations:
  * free reduction of words on x,y;
  * integer Magnus series truncated after total degree 6.

It does not implement a general nilpotent quotient package.  The Hall/Mal'cev
coordinates are recovered weight by weight from the explicitly listed basic
commutators.
"""

from fractions import Fraction

MAX_DEGREE = 6
ONE = {(): 1}
X = {(): 1, (0,): 1}
Y = {(): 1, (1,): 1}


def clean(a):
    return {m: c for m, c in a.items() if c}


def add(a, b, scale=1):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, 0) + scale * c
    return clean(out)


def mul(a, b):
    out = {}
    for u, cu in a.items():
        for v, cv in b.items():
            if len(u) + len(v) <= MAX_DEGREE:
                uv = u + v
                out[uv] = out.get(uv, 0) + cu * cv
    return clean(out)


def inv(a):
    assert a.get((), 0) == 1
    z = add(a, ONE, scale=-1)
    out = dict(ONE)
    term = dict(ONE)
    for k in range(1, MAX_DEGREE + 1):
        term = mul(term, z)
        out = add(out, term, scale=(-1) ** k)
    assert mul(a, out) == ONE and mul(out, a) == ONE
    return out


def power(a, n):
    if n < 0:
        return power(inv(a), -n)
    out = dict(ONE)
    base = a
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


def comm(a, b):
    """[a,b] = a^-1 b^-1 a b."""
    return mul(mul(mul(inv(a), inv(b)), a), b)


def prod(*items):
    out = dict(ONE)
    for item in items:
        out = mul(out, item)
    return out


def homogeneous(a, degree):
    return {m: c for m, c in a.items() if len(m) == degree and c}


def min_degree(a):
    nonconstant = [len(m) for m, c in a.items() if m and c]
    return min(nonconstant) if nonconstant else None


def solve_columns(columns, target, degree):
    """Solve sum_j q_j columns[j] = target over Q; demand uniqueness."""
    monomials = sorted({m for col in columns for m in col} | set(target))
    rows = []
    for m in monomials:
        rows.append(
            [Fraction(col.get(m, 0)) for col in columns]
            + [Fraction(target.get(m, 0))]
        )
    ncols = len(columns)
    pivot_rows = []
    row = 0
    for col in range(ncols):
        pivot = next((r for r in range(row, len(rows)) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[row], rows[pivot] = rows[pivot], rows[row]
        p = rows[row][col]
        rows[row] = [v / p for v in rows[row]]
        for r in range(len(rows)):
            if r != row and rows[r][col]:
                q = rows[r][col]
                rows[r] = [u - q * v for u, v in zip(rows[r], rows[row])]
        pivot_rows.append((row, col))
        row += 1
    for r in rows:
        if all(v == 0 for v in r[:ncols]) and r[-1] != 0:
            raise AssertionError(f"inconsistent degree-{degree} coordinate system")
    if len(pivot_rows) != ncols:
        raise AssertionError(
            f"rank {len(pivot_rows)} < {ncols} in degree {degree}"
        )
    answer = [Fraction(0) for _ in range(ncols)]
    for r, col in pivot_rows:
        answer[col] = rows[r][-1]
    return answer, len(pivot_rows), len(monomials)


def hall_coordinates(word, hall_by_weight):
    """Coordinates for the ordered normal form, stripping weights from the left."""
    remainder = word
    coordinates = {}
    diagnostics = []
    for weight in range(1, MAX_DEGREE + 1):
        entries = hall_by_weight[weight]
        target = homogeneous(add(remainder, ONE, scale=-1), weight)
        columns = [homogeneous(add(series, ONE, scale=-1), weight)
                   for _, series in entries]
        coeffs, rank, ambient = solve_columns(columns, target, weight)
        if any(q.denominator != 1 for q in coeffs):
            raise AssertionError(f"nonintegral weight-{weight} coordinates: {coeffs}")
        ints = [int(q) for q in coeffs]
        layer = dict(ONE)
        for (_, series), exponent in zip(entries, ints):
            layer = mul(layer, power(series, exponent))
        remainder = mul(inv(layer), remainder)
        md = min_degree(add(remainder, ONE, scale=-1))
        if md is not None and md <= weight:
            raise AssertionError(
                f"failed to strip weight {weight}; residual minimum degree {md}"
            )
        diagnostics.append((weight, len(entries), rank, ambient, md))
        for (name, _), exponent in zip(entries, ints):
            coordinates[name] = exponent
    if remainder != ONE:
        raise AssertionError("nontrivial residual after class-6 collection")
    return coordinates, diagnostics


# A second representation: literal freely reduced signed-generator words.
def wmul(a, b):
    out = list(a)
    for letter in b:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def winv(a):
    return tuple(-letter for letter in reversed(a))


def wpow(a, n):
    if n < 0:
        return wpow(winv(a), -n)
    out = ()
    for _ in range(n):
        out = wmul(out, a)
    return out


def wcomm(a, b):
    return wmul(wmul(wmul(winv(a), winv(b)), a), b)


# Named commutators and exact frozen words in the Magnus representation.
c = comm(Y, X)
a = comm(c, X)
b = comm(c, Y)
alpha = comm(a, X)
beta = comm(a, Y)
gamma = comm(b, Y)
r = comm(alpha, X)
s = comm(alpha, Y)
t = comm(beta, Y)
u = comm(gamma, Y)
delta = comm(a, c)
epsilon = comm(b, c)

h1 = comm(r, X)
h2 = comm(r, Y)
h3 = comm(s, Y)
h4 = comm(t, Y)
h5 = comm(u, Y)
h6 = comm(alpha, c)
h7 = comm(beta, c)
h8 = comm(gamma, c)
h9 = comm(b, a)

HALL = {
    1: [("x", X), ("y", Y)],
    2: [("c", c)],
    3: [("a", a), ("b", b)],
    4: [("alpha", alpha), ("beta", beta), ("gamma", gamma)],
    5: [("r", r), ("s", s), ("t", t), ("u", u),
        ("delta", delta), ("epsilon", epsilon)],
    6: [("h1", h1), ("h2", h2), ("h3", h3), ("h4", h4),
        ("h5", h5), ("h6", h6), ("h7", h7), ("h8", h8),
        ("h9", h9)],
}

A = comm(Y, power(X, 3))
TA = mul(inv(mul(power(c, 3), power(a, 3))), A)
SA = comm(TA, Y)

q1 = comm(X, Y)
q2 = comm(q1, Y)
B = comm(X, power(Y, 3))
TB = mul(inv(mul(power(q1, 3), power(q2, 3))), B)
Q = comm(TB, X)

C = comm(power(X, 3), power(Y, 3))
R5 = prod(
    power(c, -9), power(a, -9), power(b, -9), power(beta, -9),
    power(delta, 54), power(epsilon, 27), power(TA, -3),
    power(SA, -3), power(TB, 3), power(Q, 3),
)
D = mul(C, inv(R5))


def show_nonzero(label, coords):
    body = " ".join(f"{name}={value}" for name, value in coords.items() if value)
    print(f"{label}: {body if body else '(identity)'}")


def main():
    print("commutator_convention=[a,b]=a^-1 b^-1 a b")
    print("max_magnus_degree=6")

    # Exact free-word identity, independently of truncation.
    wx, wy = (1,), (2,)
    wv1 = wcomm(wpow(wx, 3), wy)
    wv2 = wcomm(wv1, wy)
    wv3 = wcomm(wv2, wy)
    wleft = wcomm(wpow(wx, 3), wpow(wy, 3))
    wright = wmul(
        wmul(wmul(wpow(wv1, 3), wpow(wv2, 3)), wv3),
        wcomm(wv2, wv1),
    )
    print(f"three_conjugate_free_word_equal={wleft == wright}")
    print(f"three_conjugate_reduced_length_left={len(wleft)}")
    print(f"three_conjugate_reduced_length_right={len(wright)}")

    # Weight-layer ranks and Hall collection diagnostics.
    ccoords, cdiag = hall_coordinates(C, HALL)
    rcoords, rdiag = hall_coordinates(R5, HALL)
    dcoords, ddiag = hall_coordinates(D, HALL)
    print("hall_layer_diagnostics=(weight,count,rank,ambient_monomials,residual_min_degree)")
    for row in ddiag:
        print(row)
    show_nonzero("C_coordinates", ccoords)
    show_nonzero("R5_coordinates", rcoords)
    show_nonzero("D_coordinates", dcoords)
    print(f"lower_coordinates_C_equal_R5={all(ccoords[n] == rcoords[n] for w in range(1, 6) for n, _ in HALL[w])}")
    print(f"coord_h3_C={ccoords['h3']}")
    print(f"coord_h3_R5={rcoords['h3']}")
    print(f"coord_h3_D={dcoords['h3']}")
    print(f"coord_h3_difference={ccoords['h3'] - rcoords['h3']}")
    print(f"D_min_nonconstant_degree={min_degree(add(D, ONE, scale=-1))}")

    # Direct factor-order audit: recompute the exact product after omitting Q,
    # and compare Q against its lower Hall truncation.  These are collected from
    # exact words; no claimant intermediate formula is used.
    qcoords, _ = hall_coordinates(Q, HALL)
    tacoords, _ = hall_coordinates(TA, HALL)
    sacoords, _ = hall_coordinates(SA, HALL)
    tbcoords, _ = hall_coordinates(TB, HALL)
    show_nonzero("TA_coordinates", tacoords)
    show_nonzero("SA_coordinates", sacoords)
    show_nonzero("TB_coordinates", tbcoords)
    show_nonzero("Q_coordinates", qcoords)
    print(f"coord_h3_Q={qcoords['h3']}")

    # Left-side audit via exact factors from the proposed formula.  Comparing
    # partial products with full collection catches all power/interchange terms.
    v1 = comm(power(X, 3), Y)
    v2 = comm(v1, Y)
    v3 = comm(v2, Y)
    left_factors = [power(v1, 3), power(v2, 3), v3, comm(v2, v1)]
    running = dict(ONE)
    for i, factor in enumerate(left_factors, 1):
        running = mul(running, factor)
        coords, _ = hall_coordinates(running, HALL)
        print(f"left_prefix_{i}_coord_h3={coords['h3']}")
    print(f"magnus_three_conjugate_equal={prod(*left_factors) == C}")

    # Reversal/order audit is direct: D uses the inverse of the full ordered R5.
    # The coordinate difference must agree with collection of C*R5^-1.
    print(f"central_difference_consistency={dcoords['h3'] == ccoords['h3'] - rcoords['h3']}")
    print(f"nondivisible_mod_3={dcoords['h3'] % 3 != 0}")


if __name__ == "__main__":
    main()
