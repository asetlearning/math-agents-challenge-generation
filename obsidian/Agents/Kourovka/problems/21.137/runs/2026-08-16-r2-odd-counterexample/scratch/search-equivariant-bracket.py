#!/usr/bin/env python3
"""Exact F_3 coefficient test for one cyclic-semidirct construction family.

No group catalogue is used.  An alternating central bracket beta on
U=(F_3[C_3])^2 with values in Z=F_3[C_3] is constrained to be equivariant.
For both nontrivial top cosets, the quadratic central term in the cube formula is
required to lie in Z0=im(1+tau+tau^2).  We then test whether the two-dimensional
noncentral norm image W can have nonzero bracket.
"""

P = 3
U_DIM = 6
Z_DIM = 3
PAIRS = [(i, j) for i in range(U_DIM) for j in range(i + 1, U_DIM)]
VAR = {(k, i, j): k * len(PAIRS) + PAIRS.index((i, j))
       for k in range(Z_DIM) for i, j in PAIRS}
NVAR = Z_DIM * len(PAIRS)


def invmod(a):
    return pow(a % P, -1, P)


def rref(rows):
    a = [[x % P for x in row] for row in rows]
    m = len(a)
    n = len(a[0]) if m else NVAR
    pivots = []
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = invmod(a[r][c])
        a[r] = [(scale * x) % P for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                scale = a[i][c]
                a[i] = [(a[i][j] - scale * a[r][j]) % P
                        for j in range(n)]
        pivots.append(c)
        r += 1
        if r == m:
            break
    return a, pivots


def nullspace(rows):
    reduced, pivots = rref(rows)
    free = [j for j in range(NVAR) if j not in pivots]
    basis = []
    for f in free:
        v = [0] * NVAR
        v[f] = 1
        for i, pivot in enumerate(pivots):
            v[pivot] = (-reduced[i][f]) % P
        basis.append(v)
    return basis, len(pivots)


def zero_row():
    return [0] * NVAR


def add_scaled(dst, src, scale=1):
    for i, x in enumerate(src):
        dst[i] = (dst[i] + scale * x) % P


def tau_u_index(i, power=1):
    base = 0 if i < 3 else 3
    return base + ((i - base + power) % 3)


def tau_z_index(k, power=1):
    return (k + power) % 3


def bracket_coordinate_row(k, x, y):
    """Coefficient row for the k-coordinate of beta(x,y)."""
    row = zero_row()
    for i, xi in enumerate(x):
        if not xi:
            continue
        for j, yj in enumerate(y):
            if not yj or i == j:
                continue
            if i < j:
                row[VAR[(k, i, j)]] = (row[VAR[(k, i, j)]] + xi * yj) % P
            else:
                row[VAR[(k, j, i)]] = (row[VAR[(k, j, i)]] - xi * yj) % P
    return row


def basis_vector(dim, i):
    v = [0] * dim
    v[i] = 1
    return v


def tau_u(v, power=1):
    out = [0] * U_DIM
    for i, value in enumerate(v):
        out[tau_u_index(i, power)] = value
    return out


def quadratic_cube_rows(u, top_power):
    """Rows for the three coordinates of the BCH bracket correction."""
    au = tau_u(u, top_power)
    a2u = tau_u(u, 2 * top_power)
    rows = []
    half = 2  # 1/2 in F_3
    for k in range(Z_DIM):
        row = zero_row()
        add_scaled(row, bracket_coordinate_row(k, u, au), half)
        add_scaled(row, bracket_coordinate_row(k, u, a2u), half)
        add_scaled(row, bracket_coordinate_row(k, au, a2u), half)
        rows.append(row)
    return rows


equations = []

# beta(tau e_i, tau e_j) = tau beta(e_i,e_j)
for i, j in PAIRS:
    ti, tj = tau_u_index(i), tau_u_index(j)
    for k in range(Z_DIM):
        left = bracket_coordinate_row(
            k, basis_vector(U_DIM, ti), basis_vector(U_DIM, tj))
        right_k = (k - 1) % 3  # (tau z)_k = z_{k-1}
        right = bracket_coordinate_row(
            right_k, basis_vector(U_DIM, i), basis_vector(U_DIM, j))
        add_scaled(left, right, -1)
        equations.append(left)

# A homogeneous quadratic map over F_3 vanishes iff it vanishes on e_i and
# e_i+e_j. Require coordinate 0=1=2 modulo the diagonal line, for tau and tau^2.
test_vectors = [basis_vector(U_DIM, i) for i in range(U_DIM)]
for i, j in PAIRS:
    v = basis_vector(U_DIM, i)
    v[j] = 1
    test_vectors.append(v)

for top_power in (1, 2):
    for u in test_vectors:
        rows = quadratic_cube_rows(u, top_power)
        eq01 = rows[0][:]
        add_scaled(eq01, rows[1], -1)
        equations.append(eq01)
        eq12 = rows[1][:]
        add_scaled(eq12, rows[2], -1)
        equations.append(eq12)

basis, rank = nullspace(equations)

# W is spanned by the two diagonal vectors in the regular U summands.
w1 = [1, 1, 1, 0, 0, 0]
w2 = [0, 0, 0, 1, 1, 1]
functional_rows = [bracket_coordinate_row(k, w1, w2) for k in range(Z_DIM)]

values = []
for vector in basis:
    values.append(tuple(sum(row[i] * vector[i] for i in range(NVAR)) % P
                        for row in functional_rows))
nonzero_index = next((i for i, value in enumerate(values) if value != (0, 0, 0)), None)

print(f"variables={NVAR}")
print(f"equation_rows={len(equations)}")
print(f"constraint_rank={rank}")
print(f"solution_nullity={len(basis)}")
print(f"nonabelian_W_possible={'yes' if nonzero_index is not None else 'no'}")
if nonzero_index is not None:
    candidate = basis[nonzero_index]
    print(f"beta(w1,w2)={values[nonzero_index]}")
    print("nonzero_brackets:")
    for i, j in PAIRS:
        value = tuple(candidate[VAR[(k, i, j)]] for k in range(Z_DIM))
        if value != (0, 0, 0):
            print(f"  [{i},{j}]={value}")
else:
    print("certificate: beta(W,W)=0 on the entire constrained solution space")
