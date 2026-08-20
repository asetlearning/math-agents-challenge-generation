"""Exact F_3 check for a local root-action triple.

This checks only automorphisms of P = H_3(3) x C_3^2 and the necessary
root/action equations.  It does not construct an ambient exponent-nine group.
"""

P = 3
N = 4


def eye():
    return [[int(i == j) for j in range(N)] for i in range(N)]


def mm(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(N)) % P for j in range(N)]
        for i in range(N)
    ]


def mv(a, v):
    return [sum(a[i][j] * v[j] for j in range(N)) % P for i in range(N)]


def vm(v, a):
    return [sum(v[i] * a[i][j] for i in range(N)) % P for j in range(N)]


def madd(*matrices):
    return [
        [sum(a[i][j] for a in matrices) % P for j in range(N)]
        for i in range(N)
    ]


def transpose(a):
    return [list(row) for row in zip(*a)]


def dot(v, w):
    return sum(v[i] * w[i] for i in range(len(v))) % P


identity = eye()

# V has basis A,B,r1,r2.  Only beta(A,B)=1 is nonzero; r1,r2 span
# the radical.  P is the class-two exponent-three BCH group V x F_3 z.
omega = [[0] * N for _ in range(N)]
omega[0][1] = 1
omega[1][0] = -1 % P

# T(B)=B+r1, T(r1)=r1+r2; S(A)=A-r1, S(r1)=r1+r2.
T = eye()
T[2][1] = 1
T[3][2] = 1
S = eye()
S[2][0] = -1 % P
S[3][2] = 1

# alpha(v,t)=(Tv,t+lambda(v)), beta(v,t)=(Sv,t+mu(v)).
lam = [0, 0, 0, 2]
mu = [0, 0, 2, 2]

# Right conjugation by xy applies alpha and then beta, hence as ordinary
# functions gamma=beta o alpha: U=S*T and nu=lambda+mu*T.
U = mm(S, T)
nu = [(lam[j] + vm(mu, T)[j]) % P for j in range(N)]


def cube_sum(a):
    return madd(identity, a, mm(a, a))


def preserves_beta(a):
    return mm(mm(transpose(a), omega), a) == omega


def beta(v, w):
    return dot(v, mv(omega, w))


def label_functional(v):
    # The row u |-> beta(u,v).
    return vm(v, transpose(omega))


A = [1, 0, 0, 0]
B = [0, 1, 0, 0]
C = [1, 1, 1, 0]

phi_a = vm(lam, cube_sum(T))
phi_b = vm(mu, cube_sum(S))
phi_c = vm(nu, cube_sum(U))

assert preserves_beta(T) and preserves_beta(S) and preserves_beta(U)
assert mm(mm(T, T), T) == identity
assert mm(mm(S, S), S) == identity
assert mm(mm(U, U), U) == identity
assert phi_a == label_functional(A)
assert phi_b == label_functional(B)
assert phi_c == label_functional(C)
assert mv(T, A) == A and dot(lam, A) == 0
assert mv(S, B) == B and dot(mu, B) == 0
assert mv(U, C) == C and dot(nu, C) == 0

delta = beta(A, B)
epsilon = beta(B, C)
zeta = beta(C, A)
frequency = [epsilon, zeta, delta]
tx = [0, -delta % P, zeta]
ty = [delta, 0, -epsilon % P]
tw = [-zeta % P, epsilon, 0]
assert delta and epsilon and zeta
assert dot(frequency, tx) == dot(frequency, ty) == dot(frequency, tw) == 0

assert mv(T, B) != B and mv(S, A) != A and mv(U, A) != A

print("formal_object=local_actions_on_H3(3)xC3^2_not_an_ambient_group")
print("alpha_beta_product_cube_labels=A,B,C")
print("pairings_delta_epsilon_zeta=%d,%d,%d" % (delta, epsilon, zeta))
print("root_values_fixed_by_respective_actions=pass")
print("linear_parts_and_product_have_order_three=pass")
print("cube_actions_equal_inner_A_inner_B_inner_C=pass")
print("three_action_monodromy_pairings=0,0,0")
print("nontrivial_quotient_orbits_for_X_Y_XY=pass")
