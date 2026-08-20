# Exact bounded screen of selected first uncovered non-type-A rank >= 4 tables.
names := [ "S8(2)", "O8+(2)", "O8-(2)", "U5(2)", "U5(3)", "S8(3)" ];
Print("GAP version: ", GAPInfo.Version, "\n");
Print("CTblLib version: ", InstalledPackageVersion("ctbllib"), "\n");
Print("table,nclasses,tested_ordered_nonidentity_pairs,single_class_products\n");
for name in names do
  tbl := CharacterTable(name); n := NrConjugacyClasses(tbl); hits := [];
  for i in [2..n] do
    for j in [2..n] do
      support := Filtered([1..n], k -> ClassMultiplicationCoefficient(tbl,i,j,k) <> 0);
      if Length(support)=1 then Add(hits,[i,j,support[1]]); fi;
    od;
  od;
  Print(name, ",", n, ",", (n-1)^2, ",", hits, "\n");
od;
QUIT;
