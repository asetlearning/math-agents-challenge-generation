# Calibration: B(2,3) and B(2,4) are finite, computable the same way.
LoadPackage("anupq");;
F := FreeGroup("a","b");;

B23 := Pq(F : Prime := 3, Exponent := 3);;
Print("B(2,3): order = ", Size(B23), " = 3^", LogInt(Size(B23),3),
      ", class = ", NilpotencyClassOfGroup(B23), "\n");

B24 := Pq(F : Prime := 2, Exponent := 4);;
Print("B(2,4): order = ", Size(B24), " = 2^", LogInt(Size(B24),2),
      ", class = ", NilpotencyClassOfGroup(B24), "\n");
Print("B(2,4) order = 4096: ", Size(B24) = 4096, "\n");
QUIT;
