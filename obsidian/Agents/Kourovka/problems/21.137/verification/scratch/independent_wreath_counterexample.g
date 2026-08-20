Print("GAP_VERSION=", GAPInfo.Version, "\n");

D := DihedralGroup(IsPermGroup, 8);
C := CyclicGroup(IsPermGroup, 2);
W := WreathProduct(D, C);

elts := Elements(W);
sqs := Set(elts, x -> x^2);
mulClosed := ForAll(sqs, x -> ForAll(sqs, y -> x*y in sqs));
invClosed := ForAll(sqs, x -> x^-1 in sqs);
identityIn := One(W) in sqs;
S := Group(sqs);

a := First(elts, x -> ForAny(elts, y -> x^2*y^2 <> y^2*x^2));
b := First(elts, y -> a^2*y^2 <> y^2*a^2);

Print("D_SIZE=", Size(D), " C_SIZE=", Size(C), " W_SIZE=", Size(W), "\n");
Print("W_EXPONENT=", Exponent(W),
      " IS_2_GROUP=", IsPGroup(W) and PrimePGroup(W)=2,
      " PRIME_P=", PrimePGroup(W), "\n");
Print("W_ID=", IdGroup(W), "\n");
Print("SQUARE_SET_SIZE=", Length(sqs),
      " IDENTITY_IN=", identityIn,
      " MUL_CLOSED=", mulClosed,
      " INV_CLOSED=", invClosed, "\n");
Print("SQUARE_GENERATED_GROUP_SIZE=", Size(S),
      " SQUARE_SUBGROUP_NONABELIAN=", not IsAbelian(S),
      " S_EQUALS_SQUARE_SET=", Size(S)=Length(sqs), "\n");
Print("S_ID=", IdGroup(S), " S_STRUCTURE=", StructureDescription(S), "\n");
Print("NONCOMMUTING_PAIR_FOUND=", a <> fail and b <> fail, "\n");
Print("A_SQUARED=", a^2, "\n");
Print("B_SQUARED=", b^2, "\n");
Print("AB_SQUARES_COMMUTE=", a^2*b^2 = b^2*a^2, "\n");
Print("RUN_COMPLETE=true\n");
QUIT;
