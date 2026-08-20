#!/usr/bin/env python3
"""Independent bounded F_3 checks for the 21.137 extension-family audit."""

from itertools import product

P = 3


def add(A, B):
    return [[(A[i][j] + B[i][j]) % P for j in range(len(A[0]))]
            for i in range(len(A))]


def sub(A, B):
    return [[(A[i][j] - B[i][j]) % P for j in range(len(A[0]))]
            for i in range(len(A))]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % P
             for j in range(len(B[0]))] for i in range(len(A))]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def zero(m, n):
    return [[0] * n for _ in range(m)]


def col(*xs):
    return [[x % P] for x in xs]


def mat_from_cols(cols):
    return [[cols[j][i] % P for j in range(len(cols))]
            for i in range(len(cols[0]))]


def det2(A):
    return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % P


def rank(A):
    A = [row[:] for row in A]
    m, n = len(A), len(A[0])
    r = 0
    for j in range(n):
        piv = next((i for i in range(r, m) if A[i][j]), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][j], -1, P)
        A[r] = [(inv * x) % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][j]:
                c = A[i][j]
                A[i] = [(A[i][k] - c * A[r][k]) % P for k in range(n)]
        r += 1
    return r


def det(v, w):
    return (v[0] * w[1] - v[1] * w[0]) % P


def kmul(x, y):
    """K=H_3(3) x C_3^3, coordinates (v1,v2,c,d1,d2,d3)."""
    v, w = x[:2], y[:2]
    ans = [(x[i] + y[i]) % P for i in range(6)]
    ans[2] = (ans[2] + 2 * det(v, w)) % P
    return tuple(ans)


def kinv(x):
    return tuple((-a) % P for a in x)


def kcomm(x, y):
    return kmul(kmul(kmul(kinv(x), kinv(y)), x), y)


I2 = eye(2)
gl2 = []
for vals in product(range(P), repeat=4):
    A = [list(vals[:2]), list(vals[2:])]
    if det2(A):
        gl2.append(A)

order3 = [A for A in gl2 if mul(mul(A, A), A) == I2]
nontrivial_order3 = [A for A in order3 if A != I2]
fixed_ranks_nontrivial = []
norm_zero = True
for A in order3:
    N = sub(A, I2)
    if A != I2:
        fixed_ranks_nontrivial.append(2 - rank(N))
    norm_zero &= add(add(I2, A), mul(A, A)) == zero(2, 2)

print(f"GL2(3) size: {len(gl2)}")
print(f"elements with A^3=I: {len(order3)} (nonidentity {len(nontrivial_order3)})")
print(f"fixed-space dimensions for nonidentity A^3=I: {sorted(set(fixed_ranks_nontrivial))}")
print(f"I+A+A^2 vanishes for every A^3=I: {norm_zero}")

vectors2 = list(product(range(P), repeat=2))
assoc_v = True
inner_sign = True
comm_formula = True
for u, v, w in product(vectors2, repeat=3):
    xu = tuple(u) + (0, 0, 0, 0)
    xv = tuple(v) + (0, 0, 0, 0)
    xw = tuple(w) + (0, 0, 0, 0)
    assoc_v &= kmul(kmul(xu, xv), xw) == kmul(xu, kmul(xv, xw))
for a, v in product(vectors2, repeat=2):
    xa = tuple(a) + (0, 0, 0, 0)
    xv = tuple(v) + (0, 0, 0, 0)
    conjugate = kmul(kmul(xa, xv), kinv(xa))
    inner_sign &= conjugate == tuple(v) + (det(a, v), 0, 0, 0)
for v, w in product(vectors2, repeat=2):
    xv = tuple(v) + (0, 0, 0, 0)
    xw = tuple(w) + (0, 0, 0, 0)
    comm_formula &= kcomm(xv, xw) == (0, 0, det(v, w), 0, 0, 0)

lines = []
unused = set(vectors2) - {(0, 0)}
while unused:
    v = min(unused)
    line = {(0, 0), v, ((2*v[0]) % P, (2*v[1]) % P)}
    lines.append(line)
    unused -= line
line_commutation = all(det(v, w) == 0 for line in lines for v in line for w in line)
print(f"E0 associative on all V-coordinate triples: {assoc_v}")
print(f"inner conjugation has +det(a,v)c sign: {inner_sign}")
print(f"commutator is det(v,w)c for all V-coordinate pairs: {comm_formula}")
print(f"number of V-lines: {len(lines)}; all full central fibres over one line commute: {line_commutation}")

# Basis order is e1,e2,c,d, and matrices act on column vectors.
R = mat_from_cols([
    [0, 1, 0, 0],  # R e1 = e2
    [0, 0, 1, 0],  # R e2 = c
    [0, 0, 0, 0],  # R c = 0
    [0, 0, 0, 0],  # R d = 0
])

# Rank of the complete linear system XR=RX and Xc=0 on all 16 entries of X.
constraints = []
for i in range(4):
    for j in range(4):
        row = []
        for pos in range(16):
            E = zero(4, 4)
            E[pos // 4][pos % 4] = 1
            row.append(sub(mul(E, R), mul(R, E))[i][j])
        constraints.append(row)
for i in range(4):
    row = []
    for pos in range(16):
        E = zero(4, 4)
        E[pos // 4][pos % 4] = 1
        row.append(mul(E, col(0, 0, 1, 0))[i][0])
    constraints.append(row)
linear_solution_dimension = 16 - rank(constraints)

centralizing_fix_c = []
nilpotent_index_at_most_3 = []
normal_form_ok = True
r2_formula_ok = True
for a, b, gamma, delta, epsilon, zeta in product(range(P), repeat=6):
    Rp = mat_from_cols([
        [a, b, gamma, delta],
        [0, a, b, 0],
        [0, 0, a, 0],
        [0, 0, epsilon, zeta],
    ])
    if mul(R, Rp) != mul(Rp, R):
        raise AssertionError("derived centralizer parametrization failed")
    if mul(Rp, col(0, 0, 1, 0)) == col(0, 0, 0, 0):
        centralizing_fix_c.append((a, b, gamma, delta, epsilon, zeta, Rp))
        if mul(mul(Rp, Rp), Rp) == zero(4, 4):
            nilpotent_index_at_most_3.append((a, b, gamma, delta, epsilon, zeta, Rp))
            normal_form_ok &= (a == 0 and zeta == 0)
            actual = mul(mul(Rp, Rp), col(1, 0, 0, 0))
            expected = col(0, 0, (b*b + delta*epsilon) % P, 0)
            r2_formula_ok &= actual == expected
            for basis_col in (col(0, 1, 0, 0), col(0, 0, 1, 0), col(0, 0, 0, 1)):
                r2_formula_ok &= mul(mul(Rp, Rp), basis_col) == col(0, 0, 0, 0)

print(f"centralizer matrices fixing c: {len(centralizing_fix_c)}")
print(f"dimension of full linear solution space [R,X]=0, Xc=0: {linear_solution_dimension}")
print(f"among them R'^3=0: {len(nilpotent_index_at_most_3)}")
print(f"R'^3=0 forces exactly a=zeta=0: {normal_form_ok}")
print(f"R'^2 formula in the claimed normal form: {r2_formula_ok}")

# Exhaust the scalar implications arising after reducing RL'-R'L modulo kc.
# x is any nonzero functional on F_3^2; q and q' are represented by the
# corresponding determinant functionals, so dependence of functionals is enough.
functionals = [(a, b) for a, b in product(range(P), repeat=2) if (a, b) != (0, 0)]
outer_cases = 0
bad_cases = []
for x in functionals:
    for xp in functionals:
        for b, delta, epsilon in product(range(P), repeat=3):
            commutes_mod_c = all(
                (xp[i] - b*x[i]) % P == 0 and (delta*x[i]) % P == 0
                for i in range(2)
            )
            r2_equations_nonzero = any(
                ((b*b + delta*epsilon) * xp[i]) % P for i in range(2)
            )
            if commutes_mod_c and r2_equations_nonzero:
                outer_cases += 1
                qprime_functional = tuple(((b*b + delta*epsilon) * xp[i]) % P for i in range(2))
                if not any(all(qprime_functional[i] == lam*x[i] % P for i in range(2))
                           for lam in (1, 2)):
                    bad_cases.append((x, xp, b, delta, epsilon, qprime_functional))

print(f"nonzero-functional outer-commutation cases checked: {outer_cases}")
print(f"cases violating proportional-label conclusion: {len(bad_cases)}")
if bad_cases:
    print("first bad case:", bad_cases[0])
    raise SystemExit(1)
