# Screen every named ordinary table in GAP's installed character-table library.
# This is a table-library screen, not an enumeration of all finite groups.

VanishingOrdersTable := function(tbl)
  local irr, classOrders, pos;
  irr := Irr(tbl);
  classOrders := OrdersClassRepresentatives(tbl);
  pos := Filtered([1..Length(classOrders)],
                  j -> ForAny(irr, chi -> chi[j] = 0));
  return Set(classOrders{pos});
end;

names := AllCharacterTableNames();;
tables := List(names, CharacterTable);;
simplePos := Filtered([1..Length(tables)], i -> IsSimple(tables[i]));;
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("NAMED_TABLES=", Length(names), " SIMPLE_TABLE_ENTRIES=",
      Length(simplePos), "\n");
candidateCount := 0;;
for i in simplePos do
  s := tables[i];;
  svo := VanishingOrdersTable(s);;
  sameOrder := Filtered([1..Length(tables)],
                        j -> j <> i and Size(tables[j]) = Size(s)
                             and not IsSimple(tables[j]));;
  matches := Filtered(sameOrder,
                      j -> VanishingOrdersTable(tables[j]) = svo);;
  if not IsEmpty(matches) then
    candidateCount := candidateCount + Length(matches);
    Print("SIMPLE=", names[i], " ORDER=", Size(s), " VO=", svo,
          " MATCHES=", names{matches}, "\n");
  fi;
od;
Print("CANDIDATE_TABLE_PAIRS=", candidateCount, "\n");
QUIT;
