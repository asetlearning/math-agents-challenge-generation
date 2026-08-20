# Bounded screen for Problem 16.4. GAP 4.12.1 + CTblLib.
# A product of classes i,j is a single class iff precisely one class
# multiplication coefficient ClassMultiplicationCoefficient(tbl,i,j,k) is nonzero.

names := [ "A5", "L2(7)", "A6", "L2(8)", "L2(11)", "A7", "L2(13)",
  "L2(17)", "A8", "L3(3)", "U3(3)", "M11", "L2(19)", "L2(23)",
  "M12", "J1", "L2(25)", "L2(27)", "Sz(8)", "L3(4)" ];

Print("GAP version: ", GAPInfo.Version, "\n");
Print("CTblLib version: ", InstalledPackageVersion("ctbllib"), "\n");
Print("table,nclasses,tested_ordered_nonidentity_pairs,single_class_products\n");

for name in names do
  tbl := CharacterTable(name);
  n := NrConjugacyClasses(tbl);
  hits := [];
  for i in [2..n] do
    for j in [2..n] do
      support := Filtered([1..n], k ->
        ClassMultiplicationCoefficient(tbl,i,j,k) <> 0);
      if Length(support) = 1 then
        Add(hits,[i,j,support[1]]);
      fi;
    od;
  od;
  Print(name, ",", n, ",", (n-1)^2, ",", hits, "\n");
od;
QUIT;
