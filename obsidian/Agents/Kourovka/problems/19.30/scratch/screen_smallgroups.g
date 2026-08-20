# Exact bounded screen for Kourovka 19.30.
# For each completely available SmallGroups order, compute ordinary character
# tables and compare the sets of class-representative orders having a zero in
# at least one irreducible character row.

VanishingOrders := function(g)
  local tbl, irr, classOrders, pos;
  tbl := CharacterTable(g);
  irr := Irr(tbl);
  classOrders := OrdersClassRepresentatives(tbl);
  pos := Filtered([1..Length(classOrders)],
                  j -> ForAny(irr, chi -> chi[j] = 0));
  return Set(classOrders{pos});
end;

orders := [60, 168, 360, 504, 660];;
Print("GAP_VERSION=", GAPInfo.Version, "\n");

for n in orders do
  if not SmallGroupsAvailable(n) then
    Print("ORDER=", n, " AVAILABLE=false\n");
  else
    nr := NrSmallGroups(n);
    simpleIds := Filtered([1..nr], i -> IsSimpleGroup(SmallGroup(n,i)));
    Print("ORDER=", n, " AVAILABLE=true NR_GROUPS=", nr,
          " SIMPLE_IDS=", simpleIds, "\n");
    for sid in simpleIds do
      s := SmallGroup(n,sid);
      svo := VanishingOrders(s);
      Print("TARGET_ID=", IdGroup(s), " TARGET_STRUCTURE=",
            StructureDescription(s), " TARGET_VO=", svo, "\n");
      matches := [];
      for i in [1..nr] do
        if i <> sid then
          g := SmallGroup(n,i);
          if VanishingOrders(g) = svo then Add(matches, i); fi;
        fi;
      od;
      Print("NONTARGET_MATCH_IDS=", matches, "\n");
    od;
  fi;
od;

QUIT;
