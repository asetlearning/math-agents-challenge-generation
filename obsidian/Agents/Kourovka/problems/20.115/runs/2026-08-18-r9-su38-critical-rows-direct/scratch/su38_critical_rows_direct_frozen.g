#############################################################################
## Frozen one-shot checker for Kourovka 20.115, strategy R9.
## Authorized domain: exactly Irr rows 35..40 of CharacterTable("3.U3(8)"),
## against every conjugacy-class column.  All value and arithmetic tests are
## exact.  Do not edit after the pre-run SHA-256 is recorded and leased.
#############################################################################

SetUserPreference("UseColor", false);
SizeScreen([ 100000, 100000 ]);

outputPath := "Agents/Kourovka/problems/20.115/runs/2026-08-18-r9-su38-critical-rows-direct/scratch/su38_critical_rows_direct_frozen.out";
LogTo(outputPath);

AssertEqual := function(actual, expected, label)
  if actual <> expected then
    Print("ASSERTION_FAILED\t", label,
          "\tactual=", actual, "\texpected=", expected, "\n");
    LogTo();
    QUIT_GAP(2);
  fi;
end;

Print("BEGIN_SU38_CRITICAL_ROWS_DIRECT\n");
Print("META\tGAP_VERSION\t", GAPInfo.Version, "\n");

AssertEqual(LoadPackage("ctbllib"), true, "CTblLib available");
Print("META\tCTBLLIB_VERSION\t", InstalledPackageVersion("ctbllib"), "\n");

table := CharacterTable("3.U3(8)");
if table = fail then
  Print("ASSERTION_FAILED\ttable unavailable\n");
  LogTo();
  QUIT_GAP(2);
fi;

characters := Irr(table);
degrees := List(characters, chi -> chi[1]);
groupOrder := Size(table);
numberRows := Length(characters);
numberClasses := NrConjugacyClasses(table);
classOrders := OrdersClassRepresentatives(table);
classSizes := SizesConjugacyClasses(table);
classLabels := AtlasClassNames(table);
centrePositions := ClassPositionsOfCentre(table);
authorizedRows := [ 35, 36, 37, 38, 39, 40 ];
expectedDegrees := [ 189, 189, 189, 189, 189, 189 ];
reviewedDirectTables := [ "L4(3)", "2.L4(3).2_2",
                          "2.L4(3).2_3", "3.U3(5)" ];

## Identity, ordinary-row, and class-order gates precede predicate evaluation.
AssertEqual(Identifier(table), "3.U3(8)", "exact table identifier");
AssertEqual(IsOrdinaryTable(table), true, "ordinary complex table");
AssertEqual(IsPerfect(table), true, "perfect table");
AssertEqual(IsQuasisimple(table), true, "quasisimple table");
AssertEqual(groupOrder, 16547328, "exact group order");
AssertEqual(groupOrder, 8^3 * (8^3 + 1) * (8^2 - 1),
            "SU3(8) order formula");
AssertEqual(numberRows, 82, "ordinary row count");
AssertEqual(numberClasses, 82, "conjugacy-class count");
AssertEqual(Length(classOrders), numberClasses, "class-order count");
AssertEqual(Length(classSizes), numberClasses, "class-size count");
AssertEqual(Length(classLabels), numberClasses, "class-label count");
AssertEqual(Sum(classSizes), groupOrder, "class-size sum");
AssertEqual(Sum(degrees, degree -> degree^2), groupOrder,
            "ordinary degree-square sum");
AssertEqual(Length(centrePositions), 3, "central class count");
AssertEqual(Sum(classSizes{centrePositions}), 3, "centre order");
AssertEqual(ForAll(classOrders,
                   order -> IsPosInt(order) and groupOrder mod order = 0),
            true, "every exact class order is a positive divisor of |G|");
AssertEqual(authorizedRows, [ 35 .. 40 ], "authorized row indices");
AssertEqual(List(authorizedRows, row -> degrees[row]), expectedDegrees,
            "exact authorized row degrees");
AssertEqual(Identifier(table) in reviewedDirectTables, false,
            "target absent from reviewed direct-scan table identifiers");
AssertEqual(ForAll(authorizedRows,
                   row -> ForAll(characters[row], value -> IsCyc(value))),
            true, "all authorized values are exact cyclotomics");

Print("META\tIDENTIFIER\t", Identifier(table), "\n");
Print("META\tINFO_TEXT\t",
      ReplacedString(InfoText(table), "\n", " | "), "\n");
Print("META\tORDINARY\t", IsOrdinaryTable(table), "\n");
Print("META\tPERFECT\t", IsPerfect(table), "\n");
Print("META\tQUASISIMPLE\t", IsQuasisimple(table), "\n");
Print("META\tGROUP_ORDER\t", groupOrder, "\n");
Print("META\tNUMBER_ROWS\t", numberRows, "\n");
Print("META\tNUMBER_CLASSES\t", numberClasses, "\n");
Print("META\tCENTRE_POSITIONS\t", centrePositions, "\n");
Print("META\tCENTRE_ORDER\t", Sum(classSizes{centrePositions}), "\n");
Print("META\tAUTHORIZED_ROWS\t", authorizedRows, "\n");
Print("META\tAUTHORIZED_DEGREES\t",
      List(authorizedRows, row -> degrees[row]), "\n");
Print("META\tCLASS_ORDERS\t", classOrders, "\n");
Print("META\tREVIEWED_DIRECT_SCAN_TABLES\t", reviewedDirectTables, "\n");
Print("META\tTARGET_PREVIOUSLY_DIRECT_SCANNED\t",
      Identifier(table) in reviewedDirectTables, "\n");

for class in [ 1 .. numberClasses ] do
  Print("CLASS\tindex=", class,
        "\tlabel=", classLabels[class],
        "\torder=", classOrders[class],
        "\tsize=", classSizes[class],
        "\tcentral=", class in centrePositions, "\n");
od;

for row in authorizedRows do
  Print("ROW\tindex=", row, "\tdegree=", degrees[row], "\n");
od;

cellCount := 0;
nonzeroCount := 0;
zeroCount := 0;
hitCount := 0;
hits := [];

for row in authorizedRows do
  for class in [ 1 .. numberClasses ] do
    cellCount := cellCount + 1;
    value := characters[row][class];
    zeroByEquality := value = 0;
    AssertEqual(zeroByEquality, IsZero(value),
                Concatenation("exact zero-test agreement row ", String(row),
                              " class ", String(class)));
    isNonzero := not zeroByEquality;
    product := degrees[row] * classOrders[class];
    remainder := groupOrder mod product;
    divides := remainder = 0;
    if isNonzero then
      nonzeroCount := nonzeroCount + 1;
    else
      zeroCount := zeroCount + 1;
    fi;
    if isNonzero and not divides then
      hitCount := hitCount + 1;
      Add(hits, [ row, class, classLabels[class], degrees[row],
                  classOrders[class], value, groupOrder, product, remainder ]);
      Print("HIT\trow=", row,
            "\tclass=", class,
            "\tlabel=", classLabels[class],
            "\tdegree=", degrees[row],
            "\tclass_order=", classOrders[class],
            "\texact_value=", String(value),
            "\tgroup_order=", groupOrder,
            "\tproduct=", product,
            "\tremainder=", remainder,
            "\tdivides=", divides, "\n");
    fi;
    Print("CELL\trow=", row,
          "\tclass=", class,
          "\tlabel=", classLabels[class],
          "\tdegree=", degrees[row],
          "\tclass_order=", classOrders[class],
          "\texact_value=", String(value),
          "\tnonzero=", isNonzero,
          "\tgroup_order=", groupOrder,
          "\tproduct=", product,
          "\tremainder=", remainder,
          "\tdivides=", divides, "\n");
  od;
od;

AssertEqual(cellCount, 6 * 82, "exact bounded cell coverage");
AssertEqual(nonzeroCount + zeroCount, cellCount, "zero/nonzero partition");
AssertEqual(hitCount, Length(hits), "hit count");

Print("SUMMARY\tCELLS\t", cellCount, "\n");
Print("SUMMARY\tNONZERO\t", nonzeroCount, "\n");
Print("SUMMARY\tZERO\t", zeroCount, "\n");
Print("SUMMARY\tHITS\t", hitCount, "\n");
Print("SUMMARY\tHIT_RECORDS\t", hits, "\n");
Print("END_SU38_CRITICAL_ROWS_DIRECT\n");

LogTo();
QUIT_GAP(0);
