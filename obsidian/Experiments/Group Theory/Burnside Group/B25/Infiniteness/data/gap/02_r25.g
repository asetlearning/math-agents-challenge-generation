LoadPackage("anupq");;
F := FreeGroup("a","b");;
t0 := Runtime();;
Q := Pq(F : Prime := 5, Exponent := 5);;
Print("Pq time ms: ", Runtime()-t0, "\n");
Print("Size(Q) = ", Size(Q), "\n");
Print("Size = 5^", LogInt(Size(Q),5), "\n");
Print("NilpotencyClass = ", NilpotencyClassOfGroup(Q), "\n");
lcs := LowerCentralSeries(Q);;
Print("LCS length (num subgroups) = ", Length(lcs), "\n");
for i in [1..Length(lcs)-1] do
  Print("LCS layer ", i, " : order 5^", LogInt(Size(lcs[i])/Size(lcs[i+1]),5),
        "  rank(elem-ab layer) = ", LogInt(Size(lcs[i])/Size(lcs[i+1]),5), "\n");
od;
pcs := PCentralSeries(Q, 5);;
Print("p-central series length = ", Length(pcs), "\n");
for i in [1..Length(pcs)-1] do
  Print("pC layer ", i, " : 5^", LogInt(Size(pcs[i])/Size(pcs[i+1]),5), "\n");
od;
QUIT;
