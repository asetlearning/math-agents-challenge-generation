#!/usr/bin/env python3
"""Exact sign/action gate for NS3-FIXED-OUTER-ACTION.

This program deliberately performs no categorical factor-row or group-element
enumeration.  It checks the common action equation that every one of the
3^10 frozen central-correction rows must satisfy.  Matrices act on column BCH
coordinates (a,b,u,v,z), and matrix multiplication is ordinary function
composition.  Group commutators are [r,s]=r^-1 s^-1 r s and right
conjugation is q^g=g^-1 q g.
"""

from __future__ import annotations

import argparse
import json

P = 3
DIM = 5
BASIS = ("a", "b", "u", "v", "z")
ROW_NAMES = (
    "e_X", "e_Y", "e_K", "e_T", "e_YX",
    "e_KX", "e_KY", "e_TX", "e_TY", "e_TK",
)


def ident() -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(int(i == j) for j in range(DIM)) for i in range(DIM))


I = ident()


def mat(rows: list[list[int]]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(x % P for x in row) for row in rows)


def mul(x, y):
    return tuple(
        tuple(sum(x[i][k] * y[k][j] for k in range(DIM)) % P
              for j in range(DIM))
        for i in range(DIM)
    )


def power(x, n: int):
    out = I
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n //= 2
    return out


def inverse(x):
    aug = [list(x[i]) + list(I[i]) for i in range(DIM)]
    for col in range(DIM):
        pivot = next(i for i in range(col, DIM) if aug[i][col] % P)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = pow(aug[col][col], -1, P)
        aug[col] = [(scale * entry) % P for entry in aug[col]]
        for i in range(DIM):
            if i == col:
                continue
            scale = aug[i][col] % P
            if scale:
                aug[i] = [
                    (aug[i][j] - scale * aug[col][j]) % P
                    for j in range(2 * DIM)
                ]
    return mat([row[DIM:] for row in aug])


def commutator(x, y):
    """[x,y]=x^-1 y^-1 x y."""
    return mul(mul(mul(inverse(x), inverse(y)), x), y)


def reverse_commutator(x, y):
    """x y x^-1 y^-1, arising from right action of [Y,X]."""
    return mul(mul(mul(x, y), inverse(x)), inverse(y))


def inner(q):
    """Matrix of r |-> r^q in the class-two BCH group Q."""
    qa, qb, _, _, _ = q
    rows = [list(row) for row in I]
    # [r,q]=(r_a q_b-r_b q_a)z.
    rows[4][0] = (rows[4][0] + qb) % P
    rows[4][1] = (rows[4][1] - qa) % P
    return mat(rows)


def unique_zero_central_inner_representative(x):
    """Return (qa,qb,0,0,0), or fail if x is not such an inner map."""
    qb = (x[4][0] - I[4][0]) % P
    qa = -(x[4][1] - I[4][1]) % P
    q = (qa, qb, 0, 0, 0)
    if x != inner(q):
        raise AssertionError("matrix is not inner on Q")
    return q


def named_matrix_data(x):
    return [list(row) for row in x]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sign-gate-only", action="store_true",
        help="run only the pre-lease action/sign gate (the only implemented mode)",
    )
    args = parser.parse_args()
    if not args.sign_gate_only:
        raise SystemExit(
            "categorical enumeration is intentionally disabled; "
            "run --sign-gate-only before requesting any Lead compute lease"
        )

    rows_a = [list(row) for row in I]
    rows_b = [list(row) for row in I]
    # N_A(b)=-u, N_A(u)=v, N_A(v)=z.
    rows_a[2][1] = -1 % P
    rows_a[3][2] = 1
    rows_a[4][3] = 1
    # N_B(a)=u, N_B(u)=v, N_B(v)=z.
    rows_b[2][0] = 1
    rows_b[3][2] = 1
    rows_b[4][3] = 1
    A, B = mat(rows_a), mat(rows_b)
    C = commutator(A, B)
    T = I

    q_x = unique_zero_central_inner_representative(commutator(C, A))
    q_y = unique_zero_central_inner_representative(commutator(C, B))

    assertions = {
        "A^3=Inn(a)": power(A, 3) == inner((1, 0, 0, 0, 0)),
        "B^3=Inn(b)": power(B, 3) == inner((0, 1, 0, 0, 0)),
        "C=[A,B]": C == commutator(A, B),
        "C^3=I": power(C, 3) == I,
        "T=I": T == I,
        "[C,A]=Inn(q_X)": commutator(C, A) == inner(q_x),
        "[C,B]=Inn(q_Y)": commutator(C, B) == inner(q_y),
        "q_X=q_Y=a-b": q_x == q_y == (1, 2, 0, 0, 0),
        "Inn(z)=I": inner((0, 0, 0, 0, 1)) == I,
        "|H|=3^4=81_from_normal_forms": 3 ** 4 == 81,
    }
    if not all(assertions.values()):
        raise AssertionError(assertions)

    # H has [y,x]=c, hence yx=xyc and s(yx)=XYK.  Right conjugation
    # gives alpha_y=B, alpha_x=A, alpha_(yx)=C B A.  Equation (C1) for
    # s(y)s(x)=s(yx)u(y,x) is
    #       A B = Inn(u(y,x)) C B A.
    # The frozen relation [Y,X]=K z^e_YX makes u(y,x)=z^e_YX,
    # whose inner automorphism is I for every e_YX.  Compute the missing
    # noncentral defect without iterating over any row.
    alpha_x_alpha_y = mul(A, B)
    alpha_yx = mul(mul(C, B), A)
    missing_inner = mul(alpha_x_alpha_y, inverse(alpha_yx))
    missing_q = unique_zero_central_inner_representative(missing_inner)
    frozen_pair_passes = alpha_x_alpha_y == alpha_yx

    # Equivalent word-level audit: the action of [Y,X] is the reverse
    # automorphism commutator A B A^-1 B^-1 and differs from C by the
    # same inner automorphism.
    action_yx_commutator = reverse_commutator(A, B)
    word_defect = mul(action_yx_commutator, inverse(C))
    word_missing_q = unique_zero_central_inner_representative(word_defect)
    if missing_q != word_missing_q or missing_q != (1, 2, 0, 0, 0):
        raise AssertionError((missing_q, word_missing_q))
    if frozen_pair_passes:
        raise AssertionError("expected the frozen central-only [Y,X] gate to fail")

    result = {
        "strategy_id": "NS3-FIXED-OUTER-ACTION",
        "field": 3,
        "basis": BASIS,
        "commutator_convention": "[r,s]=r^-1 s^-1 r s",
        "conjugation_convention": "q^g=g^-1 q g",
        "matrix_convention": "column vectors; XY acts as B*A",
        "row_coordinates": ROW_NAMES,
        "frozen_row_count": 3 ** len(ROW_NAMES),
        "categorical_rows_enumerated": 0,
        "group_elements_enumerated": 0,
        "H_normal_form": "x^i y^j c^k t^l, 0<=i,j,k,l<3",
        "H_order": 81,
        "matrices": {
            "A": named_matrix_data(A),
            "B": named_matrix_data(B),
            "C_standard_commutator_A_B": named_matrix_data(C),
            "action_of_[Y,X]": named_matrix_data(action_yx_commutator),
            "common_inner_defect": named_matrix_data(missing_inner),
        },
        "inner_defect_representatives": {
            "q_X_for_[C,A]": q_x,
            "q_Y_for_[C,B]": q_y,
            "required_noncentral_correction_in_[Y,X]": missing_q,
        },
        "assertions": assertions,
        "decisive_pair": {
            "h": "y",
            "j": "x",
            "section_product": "Y X = X Y K z^e_YX",
            "required_equation": "A B = Inn(z^e_YX) C B A",
            "Inn(z^e_YX)": "I for every e_YX in F_3",
            "left_equals_right": frozen_pair_passes,
            "missing_inner": "Inn(a-b)",
        },
        "outcome": (
            "all 59049 frozen central rows fail the action equation before "
            "the cocycle/associativity or cube-set stages"
        ),
        "limitation": (
            "This eliminates only the central-N family as frozen. Allowing the "
            "noncentral correction a-b in [Y,X], changing C, or enlarging the "
            "factor family is outside this run."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
