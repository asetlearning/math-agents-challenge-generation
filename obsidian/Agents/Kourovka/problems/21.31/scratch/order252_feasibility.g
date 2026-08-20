Print("GAP_VERSION=", GAPInfo.Version, "\n");
for i in [1..NumberSmallGroups(252)] do
  M := SmallGroup(252,i);
  A := AutomorphismGroup(M);
  Print("M_ID=", IdGroup(M), " AUT_ORDER=", Size(A),
        " AUT_GENERATORS=", Length(GeneratorsOfGroup(A)), "\n");
od;
QUIT;
