Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("NUMBER_SMALL_GROUPS_12=", NumberSmallGroups(12), "\n");
for i in [1..NumberSmallGroups(12)] do
  R := SmallGroup(12,i);
  a := Size(AutomorphismGroup(R));
  inn := Size(R)/Size(Centre(R));
  Print("id=", IdGroup(R),
        " structure=", StructureDescription(R),
        " center=", Size(Centre(R)),
        " aut=", a,
        " inn=", inn,
        " out=", a/inn,
        " out_divisible_by_168=", IsInt((a/inn)/168), "\n");
od;
QUIT;
