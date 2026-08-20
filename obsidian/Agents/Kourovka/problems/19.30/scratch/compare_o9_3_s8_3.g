# Exact comparison for the nonisomorphic same-order simple groups O9(3), S8(3).
VanishingOrdersTable := function(tbl)
  local irr, classOrders, pos;
  irr := Irr(tbl);
  classOrders := OrdersClassRepresentatives(tbl);
  pos := Filtered([1..Length(classOrders)],
                  j -> ForAny(irr, chi -> chi[j] = 0));
  return Set(classOrders{pos});
end;

a := CharacterTable("O9(3)");;
b := CharacterTable("S8(3)");;
avo := VanishingOrdersTable(a);;
bvo := VanishingOrdersTable(b);;
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("CTBLLIB_VERSION=", InstalledPackageVersion("ctbllib"), "\n");
Print("A=", Identifier(a), " ORDER=", Size(a), " SIMPLE=", IsSimple(a),
      " CLASSES=", NrConjugacyClasses(a), " VO=", avo, "\n");
Print("B=", Identifier(b), " ORDER=", Size(b), " SIMPLE=", IsSimple(b),
      " CLASSES=", NrConjugacyClasses(b), " VO=", bvo, "\n");
Print("EQUAL_ORDER=", Size(a)=Size(b), " EQUAL_VO=", avo=bvo, "\n");
Print("A_MINUS_B=", Difference(avo,bvo),
      " B_MINUS_A=", Difference(bvo,avo), "\n");
QUIT;
