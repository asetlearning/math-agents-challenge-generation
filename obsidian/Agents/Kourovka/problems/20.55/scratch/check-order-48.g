LoadPackage("smallgrp");
LoadPackage("ctbllib");
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
Print("CTBLLIB_VERSION=", InstalledPackageVersion("ctbllib"), "\n");
ids2 := IdsOfAllSmallGroups(Size, 48, IsSolvableGroup, true, DerivedLength, 2);
ids4 := IdsOfAllSmallGroups(Size, 48, IsSolvableGroup, true, DerivedLength, 4);
Print("DL2_COUNT=", Length(ids2), " IDS=", ids2, "\n");
Print("DL4_COUNT=", Length(ids4), " IDS=", ids4, "\n");
matches := [];
for id4 in ids4 do
  g4 := SmallGroup(id4);
  t4 := CharacterTable(g4);
  Print("DL4_GROUP=", id4, " STRUCTURE=", StructureDescription(g4),
        " NCLASSES=", NrConjugacyClasses(t4), "\n");
  for id2 in ids2 do
    g2 := SmallGroup(id2);
    t2 := CharacterTable(g2);
    trans := TransformingPermutationsCharacterTables(t2, t4);
    if trans <> fail then
      Add(matches, [id2, id4]);
      Print("MATCH=", id2, ",", id4, " TRANSFORM=", trans, "\n");
    fi;
  od;
od;
Print("MATCH_COUNT=", Length(matches), " MATCHES=", matches, "\n");
QUIT;
