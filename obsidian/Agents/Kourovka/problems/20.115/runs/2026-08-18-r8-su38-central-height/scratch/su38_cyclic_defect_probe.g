SetUserPreference("UseColor", false);
L := SU(3,8);
Cen := Center(L);
one := One(GF(8^2));
zero := Zero(GF(8^2));
lambda := Z(8^2)^7;
x := [ [lambda,zero,zero], [zero,lambda,zero],
       [zero,zero,lambda^(-2)] ];
D2 := Group([x]);
Print("LAMBDA_ORDER=", Order(lambda), "\n");
Print("X_IN_SU38=", x in L, " X_ORDER=", Order(x), "\n");
Print("X_CUBE_CENTRAL=", x^3 in Cen,
      " X_CUBE_NONTRIVIAL=", x^3 <> One(L), "\n");
Print("D2_ORDER=", Size(D2), " CENTER_INCLUDED=", IsSubgroup(D2,Cen), "\n");
Print("CENTRALIZER_X_ORDER=", Size(Centralizer(L,x)), "\n");
Q2 := FactorGroup(D2,Cen);
Print("D2_MOD_CENTER_ORDER=", Size(Q2),
      " D2_MOD_CENTER_EXPONENT=", Exponent(Q2), "\n");
Print("X_MATRIX=", x, "\n");
Print("END_SU38_CYCLIC_DEFECT_PROBE\n");
