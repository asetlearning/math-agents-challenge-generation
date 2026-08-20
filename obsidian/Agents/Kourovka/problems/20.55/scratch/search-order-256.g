LoadPackage("smallgrp");
LoadPackage("ctbllib");
Print("GAP_VERSION=", GAPInfo.Version, " SMALLGRP_VERSION=",
      InstalledPackageVersion("smallgrp"), " CTBLLIB_VERSION=",
      InstalledPackageVersion("ctbllib"), "\n");
ids2 := IdsOfAllSmallGroups(Size, 256, DerivedLength, 2);
ids4 := IdsOfAllSmallGroups(Size, 256, DerivedLength, 4);
Print("ORDER=256 DL2=", Length(ids2), " DL4=", Length(ids4), "\n");
entries2 := List(ids2, id -> rec(id := id, table := CharacterTable(SmallGroup(id))));
exacttests := 0;
matches := [];
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
Print("SUMMARY EXACT_TESTS=", exacttests, " MATCH_COUNT=", Length(matches),
      " MATCHES=", matches, "\n");
QUIT;
