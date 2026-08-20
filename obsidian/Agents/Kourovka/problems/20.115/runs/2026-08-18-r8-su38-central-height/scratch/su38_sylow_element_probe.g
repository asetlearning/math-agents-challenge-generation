SetUserPreference("UseColor", false);
L := SU(3,8);
Cen := Center(L);
P := SylowSubgroup(L,3);
els9 := Filtered(Elements(P), y -> Order(y)=9);
Print("ORDER9_COUNT=", Length(els9), "\n");
Print("MINPOLY_DEGREE_COUNTS=",
      Collected(List(els9, y -> Degree(MinimalPolynomial(GF(8^2),y)))), "\n");
for i in [1..Length(els9)] do
  y := els9[i];
  if Degree(MinimalPolynomial(GF(8^2),y)) = 2 then
    Print("FIRST_REPEATED_EIGENVALUE_INDEX=", i, "\n");
    Print("Y_MATRIX=", y, "\n");
    Print("Y_CUBE_CENTRAL=", y^3 in Cen,
          " Y_CUBE_NONTRIVIAL=", y^3 <> One(L), "\n");
    D2 := Group([y]);
    Print("D2_ORDER=", Size(D2),
          " CENTER_INCLUDED=", IsSubgroup(D2,Cen), "\n");
    break;
  fi;
od;
Print("END_SU38_SYLOW_ELEMENT_PROBE\n");
