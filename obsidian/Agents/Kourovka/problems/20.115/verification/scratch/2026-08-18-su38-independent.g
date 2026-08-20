SetUserPreference("UseColor", false);
LogTo("Agents/Kourovka/problems/20.115/verification/scratch/2026-08-18-su38-independent.out");

Print("BEGIN_INDEPENDENT_SU38_VALIDATION\n");
Print("GAP_VERSION=", GAPInfo.Version, "\n");

AssertEqual := function(actual, expected, label)
  if actual <> expected then
    Print("ASSERTION_FAILED=", label, " ACTUAL=", actual,
          " EXPECTED=", expected, "\n");
    LogTo();
    QUIT_GAP(2);
  fi;
end;

ThreePartValuation := function(integer)
  local valuation, remaining;
  valuation := 0;
  remaining := integer;
  while remaining mod 3 = 0 do
    remaining := remaining / 3;
    valuation := valuation + 1;
  od;
  return valuation;
end;

AssertEqual(LoadPackage("ctbllib"), true, "CTblLib unavailable");
Print("CTBLLIB_VERSION=", InstalledPackageVersion("ctbllib"), "\n");

table := CharacterTable("3.U3(8)");
characters := Irr(table);
degrees := List(characters, character -> character[1]);
groupOrder := Size(table);
orderValuation := ThreePartValuation(groupOrder);

AssertEqual(Identifier(table), "3.U3(8)", "table identifier");
AssertEqual(groupOrder, 16547328, "table order");
AssertEqual(Length(characters), 82, "number of ordinary characters");
AssertEqual(Sum(List(degrees, degree -> degree^2)), groupOrder,
            "ordinary degree-square sum");
AssertEqual(orderValuation, 5, "3-part of group order");
AssertEqual(Length(Positions(SizesConjugacyClasses(table), 1)), 3,
            "number of central conjugacy classes");

matrixGroup := SU(3,8);
centralSubgroup := Center(matrixGroup);
sylowSubgroup := SylowSubgroup(matrixGroup,3);
AssertEqual(Size(matrixGroup), 8^3*(8^3+1)*(8^2-1),
            "unitary order formula");
AssertEqual(Size(matrixGroup), groupOrder, "matrix/table order comparison");
AssertEqual(Size(centralSubgroup), 3, "matrix-group center order");
AssertEqual(IsSubgroup(sylowSubgroup,centralSubgroup), true,
            "central subgroup lies in Sylow subgroup");
AssertEqual(Size(sylowSubgroup), 243, "Sylow 3-subgroup order");
principalQuotient := FactorGroup(sylowSubgroup,centralSubgroup);
AssertEqual(Size(principalQuotient), 81, "principal quotient order");
AssertEqual(Exponent(principalQuotient), 9, "principal quotient exponent");

blocks := PrimeBlocks(table,3);
AssertEqual(blocks.defect, [5,2,2,2,1,1,1,1,1,1],
            "ordinary 3-block defects");
blockRows := List([1..10], block -> Positions(blocks.block,block));
AssertEqual(List(blockRows,Length), [37,9,9,9,3,3,3,3,3,3],
            "ordinary 3-block row counts");

# For every block, the central 3-subgroup lies in each defect group.
# Hence defects 2 and 1 force quotient orders 3 and 1, independently of
# the submitted cyclic-representative/support calculation.
quotientOrders := [81,3,3,3,1,1,1,1,1,1];
quotientExponents := [9,3,3,3,1,1,1,1,1,1];
thresholds := List([1..10], block ->
  quotientOrders[block]/quotientExponents[block]);
AssertEqual(thresholds, [9,1,1,1,1,1,1,1,1,1],
            "central-height thresholds");

failures := [];
passes := 0;
for row in [1..82] do
  block := blocks.block[row];
  defect := blocks.defect[block];
  height := ThreePartValuation(degrees[row])-(orderValuation-defect);
  AssertEqual(height, blocks.height[row],
              Concatenation("stored/derived height at row ",String(row)));
  comparisonPasses := 3^height <= thresholds[block];
  if comparisonPasses then
    passes := passes + 1;
  else
    Add(failures,row);
  fi;
  Print("ROW=", row, " BLOCK=", block, " DEGREE=", degrees[row],
        " DEFECT=", defect, " HEIGHT=", height,
        " HEIGHT_POWER=", 3^height,
        " QUOTIENT_ORDER=", quotientOrders[block],
        " QUOTIENT_EXPONENT=", quotientExponents[block],
        " THRESHOLD=", thresholds[block],
        " PASS=", comparisonPasses, "\n");
od;

AssertEqual(failures, [35,36,37,38,39,40], "exact failure rows");
AssertEqual(Set(List(failures,row -> degrees[row])), [189],
            "failure degrees");
AssertEqual(Set(List(failures,row -> blocks.block[row])), [1],
            "failure block");
AssertEqual(Set(List(failures,row -> blocks.height[row])), [3],
            "failure heights");
AssertEqual(passes, 76, "number of passing rows");

Print("TABLE_ID=", Identifier(table),
      " TABLE_ORDER=", groupOrder,
      " MATRIX_GROUP_ORDER=", Size(matrixGroup),
      " CENTER_ORDER=", Size(centralSubgroup),
      " SIMPLE_QUOTIENT_ORDER=", Size(matrixGroup)/Size(centralSubgroup), "\n");
Print("BLOCK_DEFECTS=", blocks.defect,
      " BLOCK_ROW_COUNTS=", List(blockRows,Length), "\n");
Print("PRINCIPAL_QUOTIENT_ORDER=", Size(principalQuotient),
      " PRINCIPAL_QUOTIENT_EXPONENT=", Exponent(principalQuotient), "\n");
Print("FAILURE_ROWS=", failures,
      " PASS_COUNT=", passes,
      " FAILURE_COUNT=", Length(failures), "\n");
Print("END_INDEPENDENT_SU38_VALIDATION\n");
LogTo();
QUIT_GAP(0);
