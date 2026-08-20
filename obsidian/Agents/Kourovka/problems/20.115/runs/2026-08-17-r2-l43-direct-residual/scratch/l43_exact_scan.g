# Deterministic exact ordinary-character scan for CTblLib table L4(3).
# Scope: every Irr row and every conjugacy class of this one table only.

if LoadPackage("ctbllib") <> true then
  Error("CTblLib is unavailable");
fi;

tableRequest := "L4(3)";
tbl := CharacterTable(tableRequest);
if tbl = fail then
  Error("CharacterTable(\"L4(3)\") returned fail");
fi;

irr := Irr(tbl);
classOrders := OrdersClassRepresentatives(tbl);
classNames := AtlasClassNames(tbl);
classSizes := SizesConjugacyClasses(tbl);
groupOrder := Size(tbl);
expectedPSL43Order := (3^6 * (3^2 - 1) * (3^3 - 1) * (3^4 - 1)) / Gcd(4, 3 - 1);
centerPositions := ClassPositionsOfCenter(tbl);

Print("SCHEMA_VERSION\t1\n");
Print("SOFTWARE\tGAP\t", GAPInfo.Version, "\n");
Print("SOFTWARE\tCTblLib\t", InstalledPackageVersion("ctbllib"), "\n");
Print("TABLE_REQUEST\t", tableRequest, "\n");
Print("TABLE_IDENTIFIER\t", Identifier(tbl), "\n");
Print("TABLE_IS_ORDINARY\t", IsOrdinaryTable(tbl), "\n");
Print("TABLE_IS_SIMPLE_CHARACTER_TABLE\t", IsSimpleCharacterTable(tbl), "\n");
Print("TABLE_ORDER\t", groupOrder, "\n");
Print("EXPECTED_PSL4_3_ORDER\t", expectedPSL43Order, "\n");
Print("ORDER_MATCH\t", groupOrder = expectedPSL43Order, "\n");
Print("CENTER_CLASS_POSITIONS\t", centerPositions, "\n");
Print("CENTER_ORDER\t", Length(centerPositions), "\n");
Print("ROW_COUNT\t", Length(irr), "\n");
Print("CLASS_COUNT\t", Length(classOrders), "\n");
Print("IRR_ORTHONORMAL\t",
      ForAll(irr, chi -> ScalarProduct(tbl, chi, chi) = 1), "\n");
Print("CLASS_NAMES\t", classNames, "\n");
Print("CLASS_ORDERS\t", classOrders, "\n");
Print("CLASS_SIZES\t", classSizes, "\n");
Print("PAIR_COLUMNS\tpair_index\trow\tclass\tclass_name\tdegree\tclass_order\texact_value\tnonzero\torder_times_degree\tdivides_group_order\tviolation\n");

pairIndex := 0;
nonzeroCount := 0;
violationCount := 0;
for i in [1 .. Length(irr)] do
  chi := irr[i];
  degree := chi[1];
  for j in [1 .. Length(classOrders)] do
    pairIndex := pairIndex + 1;
    value := chi[j];
    nonzero := value <> 0;
    orderTimesDegree := classOrders[j] * degree;
    divides := groupOrder mod orderTimesDegree = 0;
    violation := nonzero and not divides;
    if nonzero then
      nonzeroCount := nonzeroCount + 1;
    fi;
    if violation then
      violationCount := violationCount + 1;
    fi;
    Print("PAIR\t", pairIndex,
          "\t", i,
          "\t", j,
          "\t", classNames[j],
          "\t", degree,
          "\t", classOrders[j],
          "\t", value,
          "\t", nonzero,
          "\t", orderTimesDegree,
          "\t", divides,
          "\t", violation,
          "\n");
  od;
od;

Print("SUMMARY\tpairs\t", pairIndex,
      "\tnonzero_pairs\t", nonzeroCount,
      "\tviolations\t", violationCount,
      "\n");

if pairIndex <> Length(irr) * Length(classOrders) then
  Error("pair coverage mismatch");
fi;

QUIT;
