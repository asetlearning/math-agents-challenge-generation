Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("NUMBER_SMALL_GROUPS_12=", NumberSmallGroups(12), "\n");
for i in [1..NumberSmallGroups(12)] do
  K := SmallGroup(12,i);
  A := AutomorphismGroup(K);
  I := InnerAutomorphismsAutomorphismGroup(A);
  Print("K_ID=", IdGroup(K),
        " CENTER_ORDER=", Size(Centre(K)),
        " AUT_ORDER=", Size(A),
        " INNER_ORDER=", Size(I),
        " OUT_ORDER=", Index(A,I), "\n");
od;
QUIT;
