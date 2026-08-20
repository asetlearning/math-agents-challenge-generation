# Exact finite CTblLib screen for the target L3(9).
# Scope: every nonduplicate ordinary character table named by the installed
# GAP Character Table Library, not every abstract group of order |L3(9)|.

VanishingOrdersTable := function(tbl)
  local irr, classOrders, pos;
  irr := Irr(tbl);
  classOrders := OrdersClassRepresentatives(tbl);
  pos := Filtered([1..Length(classOrders)],
                  j -> ForAny(irr, chi -> chi[j] = 0));
  return Set(classOrders{pos});
end;

targetName := "L3(9)";;
target := CharacterTable(targetName);;
targetOrder := Size(target);;
targetVo := VanishingOrdersTable(target);;

names := AllCharacterTableNames();;
matches := [];;
sameOrderNames := [];;
loaded := 0;;
for name in names do
  tbl := CharacterTable(name);
  loaded := loaded + 1;
  if not IsDuplicateTable(tbl) and Size(tbl) = targetOrder then
    Add(sameOrderNames, name);
    if name <> targetName and not IsSimple(tbl)
       and VanishingOrdersTable(tbl) = targetVo then
      Add(matches, name);
    fi;
  fi;
od;

Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("CTBLLIB_VERSION=", InstalledPackageVersion("ctbllib"), "\n");
Print("TARGET=", targetName, " ORDER=", targetOrder,
      " FACTORS=", FactorsInt(targetOrder), " VO=", targetVo, "\n");
Print("ALL_NAMES_COUNT=", Length(names), " LOADED_COUNT=", loaded, "\n");
Print("NONDUPLICATE_SAME_ORDER_TABLES=", sameOrderNames, "\n");
Print("NONSIMPLE_EQUAL_VO_MATCHES=", matches, "\n");
QUIT;
