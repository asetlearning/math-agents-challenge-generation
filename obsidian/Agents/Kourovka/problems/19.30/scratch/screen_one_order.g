VanishingOrders := function(g)
  local tbl, irr, classOrders, pos;
  tbl := CharacterTable(g);
  irr := Irr(tbl);
  classOrders := OrdersClassRepresentatives(tbl);
  pos := Filtered([1..Length(classOrders)],
                  j -> ForAny(irr, chi -> chi[j] = 0));
  return Set(classOrders{pos});
end;

if not IsBound(n) or not IsBound(lo) or not IsBound(hi) then
  Error("set n, lo, hi with gap -c before reading this file");
fi;
nr := NrSmallGroups(n);;
simpleIds := Filtered([1..nr], i -> IsSimpleGroup(SmallGroup(n,i)));;
Print("GAP_VERSION=", GAPInfo.Version, " ORDER=", n, " NR_GROUPS=", nr,
      " RANGE=", [lo..hi], " SIMPLE_IDS=", simpleIds, "\n");
for sid in simpleIds do
  s := SmallGroup(n,sid);;
  svo := VanishingOrders(s);;
  Print("TARGET_ID=", IdGroup(s), " TARGET_STRUCTURE=", StructureDescription(s),
        " TARGET_VO=", svo, "\n");
  matches := [];
  for i in [lo..hi] do
    if i <> sid and VanishingOrders(SmallGroup(n,i)) = svo then
      Add(matches, i);
    fi;
  od;
  Print("MATCH_IDS_IN_RANGE=", matches, "\n");
od;
QUIT;
