LoadPackage("smallgrp");
LoadPackage("ctbllib");
if not IsBound(lowOrder) then lowOrder := 257; fi;
if not IsBound(highOrder) then highOrder := 383; fi;
Print("GAP_VERSION=", GAPInfo.Version, " SMALLGRP_VERSION=",
      InstalledPackageVersion("smallgrp"), " CTBLLIB_VERSION=",
      InstalledPackageVersion("ctbllib"), "\n");
orders := [];
total2 := 0;
total4 := 0;
exacttests := 0;
matches := [];
for n in [lowOrder..highOrder] do
  ids4 := IdsOfAllSmallGroups(Size, n, IsSolvableGroup, true, DerivedLength, 4);
  if Length(ids4) > 0 then
    ids2 := IdsOfAllSmallGroups(Size, n, IsSolvableGroup, true, DerivedLength, 2);
    Add(orders, n);
    total2 := total2 + Length(ids2);
    total4 := total4 + Length(ids4);
    Print("ORDER=", n, " DL2=", Length(ids2), " DL4=", Length(ids4), "\n");
    entries2 := List(ids2, id -> rec(id := id, table := CharacterTable(SmallGroup(id))));
    for id4 in ids4 do
      t4 := CharacterTable(SmallGroup(id4));
      for e2 in entries2 do
        if NrConjugacyClasses(e2.table) = NrConjugacyClasses(t4) then
          exacttests := exacttests + 1;
          trans := TransformingPermutationsCharacterTables(e2.table, t4);
          if trans <> fail then
            Add(matches, [e2.id, id4]);
            Print("MATCH=", e2.id, ",", id4, " TRANSFORM=", trans, "\n");
          fi;
        fi;
      od;
    od;
  fi;
od;
Print("SUMMARY_ORDERS=", orders, " TOTAL_DL2=", total2,
      " TOTAL_DL4=", total4, " EXACT_TESTS=", exacttests,
      " MATCH_COUNT=", Length(matches), " MATCHES=", matches, "\n");
QUIT;
