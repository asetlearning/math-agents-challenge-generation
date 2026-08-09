# Engel words [a, k*b] in R(2,5): which are trivial?
# Kourovka 11.48 (Kostrikin): E7 = [x,y,y,y,y,y,y] (k=6). If E7 is not a product of
# fifth powers in F2 (i.e. E7 <> 1 in B(2,5)), then B(2,5) is infinite.
# Witness logic requires E7 = 1 in R(2,5). Verify.
LoadPackage("anupq");;
F := FreeGroup("a","b");;
phi := PqEpimorphism(F : Prime := 5, Exponent := 5);;
Q := Image(phi);;
Print("size 5^", LogInt(Size(Q),5), " class ", NilpotencyClassOfGroup(Q), "\n");
ia := Image(phi, F.1);; ib := Image(phi, F.2);; one := One(Q);;
g := ia;;
for k in [1..8] do
  g := Comm(g, ib);
  Print("[a,", k, "*b] trivial in R(2,5): ", g = one, "\n");
od;
# also symmetric family [b, k*a]
g := ib;;
for k in [1..8] do
  g := Comm(g, ia);
  Print("[b,", k, "*a] trivial in R(2,5): ", g = one, "\n");
od;
# and Engel with arbitrary second entry: [x, k*y] for x,y ranging over short words
# spot-check: x=[a,b], y=ab
x := Comm(ia,ib);; y := ia*ib;;
g := x;;
for k in [1..8] do
  g := Comm(g, y);
  Print("[[a,b],", k, "*(ab)] trivial: ", g = one, "\n");
od;
QUIT;
