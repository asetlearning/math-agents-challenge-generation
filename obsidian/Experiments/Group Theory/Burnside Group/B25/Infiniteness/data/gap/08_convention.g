# Convention receipt (Math-expert D1/K5.1): E7 in R(2,5) under BOTH commutator conventions.
LoadPackage("anupq");;
F := FreeGroup("a","b");;
phi := PqEpimorphism(F : Prime := 5, Exponent := 5);;
Q := Image(phi);;
ia := Image(phi, F.1);; ib := Image(phi, F.2);; one := One(Q);;
# Convention 1 (GAP Comm): [x,y] = x^-1 y^-1 x y
g := ia;;
for k in [1..6] do g := Comm(g, ib); od;
Print("Conv1 [x,y]=x^-1y^-1xy: E7 trivial in R(2,5): ", g = one, "\n");
# Convention 2: [x,y] = x y x^-1 y^-1
CommAlt := function(x,y) return x*y*x^-1*y^-1; end;;
g := ia;;
for k in [1..6] do g := CommAlt(g, ib); od;
Print("Conv2 [x,y]=xyx^-1y^-1:  E7 trivial in R(2,5): ", g = one, "\n");
# also 5-fold under conv2 (should be nontrivial, mirroring conv1)
g := ia;;
for k in [1..5] do g := CommAlt(g, ib); od;
Print("Conv2 [a,5b] trivial: ", g = one, " (expect false)\n");
QUIT;
