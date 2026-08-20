Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("NUMBER_SMALL_GROUPS_252=", NumberSmallGroups(252), "\n");
wanted := IdGroup(SmallGroup(21,1));
pairs := [];
for i in [1..NumberSmallGroups(252)] do
  H := SmallGroup(252,i);
  candidates := Filtered(NormalSubgroups(H), N -> Size(N)=12);
  for K in candidates do
    Q := FactorGroup(H,K);
    if IdGroup(Q)=wanted then
      Add(pairs, [IdGroup(H), IdGroup(K)]);
      Print("PAIR=", [IdGroup(H), IdGroup(K)],
            " QUOTIENT_ID=", IdGroup(Q), "\n");
    fi;
  od;
od;
Print("PAIR_COUNT=", Length(pairs), "\n");
Print("DISTINCT_PAIR_COUNT=", Length(Set(pairs)), "\n");
Print("PAIRS=", pairs, "\n");
QUIT;
