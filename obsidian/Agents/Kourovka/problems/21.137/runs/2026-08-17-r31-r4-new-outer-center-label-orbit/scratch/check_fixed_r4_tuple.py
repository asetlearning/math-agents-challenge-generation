#!/usr/bin/env python3
"""Exact F_3 action/support gate for the single R4 common-root datum.

This script checks only the frozen tuple documented in the sibling manifest.
It does not construct a factor system or a finite extension group.
"""

from itertools import product

P = 3


def mm(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) % P
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def ma(*matrices):
    return [
        [sum(m[i][j] for m in matrices) % P
         for j in range(len(matrices[0][0]))]
        for i in range(len(matrices[0]))
    ]


def sm(c, a):
    return [[c * x % P for x in row] for row in a]


def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def zero(r, c):
    return [[0 for _ in range(c)] for _ in range(r)]


def mpow(a, n):
    out = ident(len(a))
    base = a
    while n:
        if n & 1:
            out = mm(out, base)
        base = mm(base, base)
        n >>= 1
    return out


def minv(a):
    n = len(a)
    aug = [row[:] + ident(n)[i] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col] % P)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = pow(aug[col][col], -1, P)
        aug[col] = [scale * x % P for x in aug[col]]
        for i in range(n):
            if i != col and aug[i][col]:
                c = aug[i][col]
                aug[i] = [(x - c * y) % P
                          for x, y in zip(aug[i], aug[col])]
    return [row[n:] for row in aug]


def rank(a):
    if not a:
        return 0
    b = [row[:] for row in a]
    r = 0
    for col in range(len(b[0])):
        pivot = next((i for i in range(r, len(b)) if b[i][col]), None)
        if pivot is None:
            continue
        b[r], b[pivot] = b[pivot], b[r]
        z = pow(b[r][col], -1, P)
        b[r] = [z * x % P for x in b[r]]
        for i in range(len(b)):
            if i != r and b[i][col]:
                c = b[i][col]
                b[i] = [(x - c * y) % P for x, y in zip(b[i], b[r])]
        r += 1
        if r == len(b):
            break
    return r


def column_space_basis(a):
    columns = [[a[i][j] for i in range(len(a))]
               for j in range(len(a[0]))]
    basis = []
    for v in columns:
        if rank(basis + [v]) > rank(basis):
            basis.append(v)
    return basis


def vector_span_basis(vectors):
    basis = []
    for v in vectors:
        if rank(basis + [list(v)]) > rank(basis):
            basis.append(list(v))
    return basis


def compact(a):
    return "/".join("".join(str(x % P) for x in row) for row in a)


def vcompact(v):
    return "".join(str(x % P) for x in v)


def omega(v, w):
    return (v[0] * w[2] + v[1] * w[3]
            - v[2] * w[0] - v[3] * w[1]) % P


# A triple (M,T,L) acts as (v,z) |-> (Mv,Tz+Lv).
def tmul(g, h):
    mg, tg, lg = g
    mh, th, lh = h
    return (mm(mg, mh), mm(tg, th), ma(mm(lg, mh), mm(tg, lh)))


ONE = (ident(4), ident(3), zero(3, 4))


def tinv(g):
    m, t, l = g
    mi, ti = minv(m), minv(t)
    return (mi, ti, sm(-1, mm(mm(ti, l), mi)))


def tpow(g, n):
    out = ONE
    for _ in range(n):
        out = tmul(out, g)
    return out


def comm(g, h):
    return tmul(tmul(tmul(tinv(g), tinv(h)), g), h)


def inner_label(g):
    m, t, l = g
    assert m == ident(4), compact(m)
    assert t == ident(3), compact(t)
    assert l[1] == [0, 0, 0, 0] and l[2] == [0, 0, 0, 0], compact(l)
    r = l[0]
    # J_q(v)=omega(q,v)c has row (-q_f1,-q_f2,q_e1,q_e2).
    return (r[2] % P, r[3] % P, -r[0] % P, -r[1] % P)


def assert_inner(g):
    return inner_label(g)


# Frozen basis: V=<e1,e2,f1,f2>, Z=<c,s,t>.
I4, I3 = ident(4), ident(3)
M = [
    [1, 0, 2, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]  # tau_e1(v)=v+omega(v,e1)e1
T = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1],
]  # c->c, s->s+c, t->t+s
U = minv(T)

e2 = (0, 1, 0, 0)
f2 = (0, 0, 0, 1)
j_e2 = [0, 0, 0, 1]
j_f2 = [0, 2, 0, 0]
LX = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    j_e2,
]
LY = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    j_f2,
]

X = (M, T, LX)
Y = (M, U, LY)
Z = comm(X, Y)

# Exact action gate.
assert mpow(M, 3) == I4 and M != I4
assert mpow(T, 3) == I3 and mm(T, U) == I3 and mm(U, T) == I3
assert assert_inner(tpow(X, 3)) == e2
assert assert_inner(tpow(Y, 3)) == f2
assert tpow(Z, 3) == ONE
assert tmul(comm(X, Y), tinv(Z)) == ONE
label_xz = assert_inner(comm(X, Z))
label_yz = assert_inner(comm(Y, Z))

# Displayed orbit separator from the exhausted transverse row.
OLD_X = [
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 2, 1],
]
OLD_Y = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]
old_z = mm(mm(mm(minv(OLD_X), minv(OLD_Y)), OLD_X), OLD_Y)
new_z = mm(mm(mm(minv(M), minv(M)), M), M)
old_center_rank = rank(ma(old_z, sm(-1, I4)))
new_center_rank = rank(ma(new_z, sm(-1, I4)))
assert old_center_rank == 1 and new_center_rank == 0

print("field=3")
print(f"M={compact(M)}")
print(f"T={compact(T)}")
print(f"Tinv={compact(U)}")
print(f"LX={compact(LX)}")
print(f"LY={compact(LY)}")
print(f"X^3_label={vcompact(assert_inner(tpow(X, 3)))}")
print(f"Y^3_label={vcompact(assert_inner(tpow(Y, 3)))}")
print(f"omega_labels={omega(e2, f2)}")
print(f"Z_M={compact(Z[0])}")
print(f"Z_T={compact(Z[1])}")
print(f"Z_L={compact(Z[2])}")
print(f"Z^3_label={vcompact(assert_inner(tpow(Z, 3)))}")
print("[X,Y]Z^-1=identity")
print(f"[X,Z]_label={vcompact(label_xz)}")
print(f"[Y,Z]_label={vcompact(label_yz)}")
print(f"orbit_separator_rank_Mz_minus_I_new={new_center_rank}")
print(f"orbit_separator_rank_Mz_minus_I_exhausted={old_center_rank}")
print(f"exhausted_Mz={compact(old_z)}")

supports = []
rows = []
for a, b, d in product(range(3), repeat=3):
    h = tmul(tmul(tpow(X, a), tpow(Y, b)), tpow(Z, d))
    h3 = tpow(h, 3)
    label = assert_inner(h3)
    norm = ma(I4, h[0], mm(h[0], h[0]))
    w_basis = column_space_basis(norm)
    fibre = {
        tuple((label[i] + sum(c * basis[i] for c, basis in zip(coeffs, w_basis))) % P
              for i in range(4))
        for coeffs in product(range(3), repeat=len(w_basis))
    }
    supports.append(fibre)
    rows.append(((a, b, d), label, w_basis, fibre))

sigma = set().union(*supports)
span_basis = vector_span_basis(sorted(sigma))
gram = [[omega(v, w) for w in span_basis] for v in span_basis]
symplectic_rank = rank(gram)
is_subspace = len(sigma) == 3 ** len(span_basis) and (0, 0, 0, 0) in sigma
outsider = None
if not is_subspace:
    for x in sorted(sigma):
        for y in sorted(sigma):
            z = tuple((u + v) % P for u, v in zip(x, y))
            if z not in sigma:
                outsider = (x, y, z)
                break
        if outsider:
            break

print("support_table_begin")
for h, label, w_basis, fibre in rows:
    w_text = ",".join(vcompact(v) for v in w_basis) if w_basis else "0"
    f_text = ",".join(vcompact(v) for v in sorted(fibre))
    print(f"h={h[0]}{h[1]}{h[2]} lambda={vcompact(label)} W={w_text} F={f_text}")
print("support_table_end")
print("Sigma=" + ",".join(vcompact(v) for v in sorted(sigma)))
print(f"Sigma_size={len(sigma)}")
print("Sigma_span_basis=" + ",".join(vcompact(v) for v in span_basis))
print(f"Sigma_span_dimension={len(span_basis)}")
print(f"Sigma_is_subspace={str(is_subspace).lower()}")
print(f"Sigma_symplectic_rank={symplectic_rank}")
if outsider:
    print("additive_outsider=" + "+".join(vcompact(v) for v in outsider[:2])
          + "->" + vcompact(outsider[2]))

