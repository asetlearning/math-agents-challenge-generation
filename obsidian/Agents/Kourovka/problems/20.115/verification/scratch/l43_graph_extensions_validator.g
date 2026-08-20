# Independent bounded certificate checker for Kourovka 20.115.
# Scope: exactly the ordinary CTblLib tables 2.L4(3).2_2 and 2.L4(3).2_3.
# This script was written without reading or importing the claimant's GAP code.

SizeScreen([ 100000, 100000 ]);;

pkgok := LoadPackage("ctbllib");;
if pkgok <> true then
  Error("CTblLib is unavailable");
fi;

Demand := function(condition, label)
  if condition <> true then
    Error(Concatenation("FAILED: ", label));
  fi;
  Print("PASS|", label, "\n");
end;

PreimagePositions := function(map, imagepoint)
  local ans, i;
  ans := [];
  for i in [ 1 .. Length(map) ] do
    if map[i] = imagepoint then
      Add(ans, i);
    fi;
  od;
  return ans;
end;

CenterPositionsFromSizes := function(tbl)
  local ans, sizes, i;
  ans := [];
  sizes := SizesConjugacyClasses(tbl);
  for i in [ 1 .. Length(sizes) ] do
    if sizes[i] = 1 then
      Add(ans, i);
    fi;
  od;
  return ans;
end;

KernelPositionsFromValues := function(chi)
  local ans, i, degree;
  ans := [];
  degree := chi[1];
  for i in [ 1 .. Length(chi) ] do
    if chi[i] = degree then
      Add(ans, i);
    fi;
  od;
  return ans;
end;

DerivedPositionsFromLinearRows := function(tbl)
  local ans, c, chi, good, linear;
  linear := Filtered(Irr(tbl), chi -> chi[1] = 1);
  ans := [];
  for c in [ 1 .. NrConjugacyClasses(tbl) ] do
    good := true;
    for chi in linear do
      if chi[c] <> 1 then
        good := false;
      fi;
    od;
    if good then
      Add(ans, c);
    fi;
  od;
  return ans;
end;

SubgroupFusionSizesAreExact := function(source, target, fusion)
  local imagepoint, preimage, sourceSizes, targetSizes;
  sourceSizes := SizesConjugacyClasses(source);
  targetSizes := SizesConjugacyClasses(target);
  for imagepoint in Set(fusion) do
    preimage := PreimagePositions(fusion, imagepoint);
    if Sum(sourceSizes{preimage}) <> targetSizes[imagepoint] then
      return false;
    fi;
  od;
  return true;
end;

CentralQuotientFusionSizesAreExact := function(source, quotient, fusion, kernelOrder)
  local imagepoint, preimage, sourceSizes, quotientSizes;
  sourceSizes := SizesConjugacyClasses(source);
  quotientSizes := SizesConjugacyClasses(quotient);
  for imagepoint in [ 1 .. NrConjugacyClasses(quotient) ] do
    preimage := PreimagePositions(fusion, imagepoint);
    if Sum(sourceSizes{preimage}) <> kernelOrder * quotientSizes[imagepoint] then
      return false;
    fi;
  od;
  return true;
end;

Print("SOFTWARE|GAP|", GAPInfo.Version, "\n");
Print("SOFTWARE|CTblLib|", PackageInfo("ctbllib")[1].Version, "\n");

base := CharacterTable("2.L4(3)");;
simple := CharacterTable("L4(3)");;
baseIrr := Irr(base);;
baseCenter := CenterPositionsFromSizes(base);;
baseDerived := DerivedPositionsFromLinearRows(base);;
baseToSimple := GetFusionMap(base, simple);;

Demand(IsOrdinaryTable(base), "base table is ordinary");
Demand(Identifier(base) = "2.L4(3)", "base identifier is exact");
Demand(Size(base) = 12130560, "base order is 12130560");
Demand(Sum(List(baseIrr, chi -> chi[1]^2)) = Size(base),
       "base irreducible degrees square-sum to the order");
Demand(baseDerived = [ 1 .. NrConjugacyClasses(base) ],
       "base is perfect, reconstructed from all linear rows");
Demand(baseDerived = ClassPositionsOfDerivedSubgroup(base),
       "base reconstructed derived positions equal GAP attribute");
Demand(baseCenter = [ 1, 2 ],
       "base center positions reconstructed from singleton classes are [1,2]");
Demand(baseCenter = ClassPositionsOfCenter(base),
       "base reconstructed center positions equal GAP attribute");
Demand(Sum(SizesConjugacyClasses(base){baseCenter}) = 2,
       "base center has order two");
Demand(IsOrdinaryTable(simple) and Identifier(simple) = "L4(3)",
       "central quotient target is the ordinary L4(3) table");
Demand(Size(simple) = 6065280, "L4(3) quotient order is 6065280");
Demand(ClassPositionsOfNormalSubgroups(simple) =
       [ [ 1 ], [ 1 .. NrConjugacyClasses(simple) ] ],
       "L4(3) table has only trivial and whole normal-subgroup class sets");
Demand(baseToSimple <> fail, "stored 2.L4(3) to L4(3) fusion exists");
Demand(PreimagePositions(baseToSimple, 1) = baseCenter,
       "stored base-to-simple fusion has kernel equal to the center");
Demand(Set(baseToSimple) = [ 1 .. NrConjugacyClasses(simple) ],
       "stored base-to-simple fusion is onto all quotient classes");
Demand(TransformingPermutationsCharacterTables(
         CharacterTableFactorGroup(base, baseCenter), simple) <> fail,
       "factor table 2.L4(3)/Z is permutation-equivalent to L4(3)");

Print("BASE|identifier=", Identifier(base), "|order=", Size(base),
      "|classes=", NrConjugacyClasses(base),
      "|derived=", baseDerived, "|center=", baseCenter, "\n");
Print("BASE_TO_SIMPLE_FUSION|", baseToSimple, "\n");
Print("SIMPLE_NORMAL_CLASS_SETS|", ClassPositionsOfNormalSubgroups(simple), "\n");

diagonal := CharacterTable("L4(3).2_1");;
graph := CharacterTable("L4(3).2_2");;
diagonalGraph := CharacterTable("L4(3).2_3");;
outerTables := [ diagonal, graph, diagonalGraph ];
outerClassCounts := List(outerTables, NrConjugacyClasses);

Demand(List(outerTables, Size) = [ 12130560, 12130560, 12130560 ],
       "all three quotient outer extensions have index two over L4(3)");
Demand(outerClassCounts = [ 43, 49, 34 ],
       "three quotient outer-extension tables have distinct class counts 43,49,34");
Demand(PositionSublist(InfoText(diagonal), "PGL(4,3)") <> fail,
       "CTblLib identifies L4(3).2_1 with PGL(4,3)");
Demand(PositionSublist(InfoText(graph), "transpose-inverse") <> fail,
       "CTblLib identifies L4(3).2_2 with the transpose-inverse extension");
Demand(PositionSublist(InfoText(graph), "PGO(+1,6,3)") <> fail,
       "CTblLib also identifies L4(3).2_2 with PGO(+1,6,3)");

for quotient in outerTables do
  simpleToOuter := GetFusionMap(simple, quotient);;
  reconstructedOuterDerived := DerivedPositionsFromLinearRows(quotient);;
  Demand(simpleToOuter <> fail,
         Concatenation("stored L4(3) fusion exists for ", Identifier(quotient)));
  Demand(Set(simpleToOuter) = reconstructedOuterDerived,
         Concatenation("fusion image is reconstructed derived subgroup for ",
                       Identifier(quotient)));
  Demand(Sum(SizesConjugacyClasses(quotient){reconstructedOuterDerived}) =
         Size(simple),
         Concatenation("derived subgroup has order |L4(3)| in ",
                       Identifier(quotient)));
  Print("OUTER_QUOTIENT|identifier=", Identifier(quotient),
        "|classes=", NrConjugacyClasses(quotient),
        "|derived=", reconstructedOuterDerived,
        "|info=", InfoText(quotient), "\n");
od;

targetIds := [ "2.L4(3).2_2", "2.L4(3).2_3" ];
quotientIds := [ "L4(3).2_2", "L4(3).2_3" ];
grandPairs := 0;
grandNonzero := 0;
grandViolations := 0;

Print("PAIR_HEADER|table|row|row_name|degree|class|class_name|class_order|exact_value|nonzero|product|remainder\n");

for targetIndex in [ 1, 2 ] do
  target := CharacterTable(targetIds[targetIndex]);;
  quotient := CharacterTable(quotientIds[targetIndex]);;
  chars := Irr(target);;
  classOrders := OrdersClassRepresentatives(target);;
  classSizes := SizesConjugacyClasses(target);;
  classNames := AtlasClassNames(target);;
  rowNames := CharacterNames(target);;

  reconstructedDerived := DerivedPositionsFromLinearRows(target);;
  storedDerived := ClassPositionsOfDerivedSubgroup(target);;
  reconstructedCenter := CenterPositionsFromSizes(target);;
  storedCenter := ClassPositionsOfCenter(target);;
  outerPositions := Difference([ 1 .. NrConjugacyClasses(target) ],
                               reconstructedDerived);;
  faithfulRows := [];
  for row in [ 1 .. Length(chars) ] do
    reconstructedKernel := KernelPositionsFromValues(chars[row]);;
    Demand(reconstructedKernel = ClassPositionsOfKernel(chars[row]),
           Concatenation("reconstructed kernel agrees for ", Identifier(target),
                         " row ", String(row)));
    if reconstructedKernel = [ 1 ] then
      Add(faithfulRows, row);
    fi;
  od;

  baseFusion := GetFusionMap(base, target);;
  quotientFusion := GetFusionMap(target, quotient);;

  Demand(IsOrdinaryTable(target),
         Concatenation(Identifier(target), " is an ordinary table"));
  Demand(Identifier(target) = targetIds[targetIndex],
         Concatenation("exact target identifier ", targetIds[targetIndex]));
  Demand(Size(target) = 24261120,
         Concatenation(Identifier(target), " has order 24261120"));
  Demand(Sum(List(chars, chi -> chi[1]^2)) = Size(target),
         Concatenation(Identifier(target),
                       " irreducible degrees square-sum to the order"));
  Demand(baseFusion <> fail,
         Concatenation("stored base fusion exists for ", Identifier(target)));
  Demand(Set(baseFusion) = reconstructedDerived,
         Concatenation("base fusion image equals independently reconstructed derived positions for ",
                       Identifier(target)));
  Demand(reconstructedDerived = storedDerived,
         Concatenation("reconstructed and stored derived positions agree for ",
                       Identifier(target)));
  Demand(SubgroupFusionSizesAreExact(base, target, baseFusion),
         Concatenation("base fusion aggregates every derived class size exactly for ",
                       Identifier(target)));
  Demand(Sum(classSizes{reconstructedDerived}) = Size(base),
         Concatenation("derived class sizes sum to 12130560 for ",
                       Identifier(target)));
  Demand(Size(target) / Sum(classSizes{reconstructedDerived}) = 2,
         Concatenation("derived subgroup has index two in ", Identifier(target)));
  Demand(reconstructedCenter = [ 1, 2 ] and reconstructedCenter = storedCenter,
         Concatenation("center positions are exactly [1,2] for ",
                       Identifier(target)));
  Demand(Set(baseFusion{baseCenter}) = reconstructedCenter,
         Concatenation("base center fuses onto target center for ",
                       Identifier(target)));
  Demand(quotientFusion <> fail,
         Concatenation("stored central quotient fusion exists for ",
                       Identifier(target)));
  Demand(PreimagePositions(quotientFusion, 1) = reconstructedCenter,
         Concatenation("central quotient fusion kernel is [1,2] for ",
                       Identifier(target)));
  Demand(Set(quotientFusion) = [ 1 .. NrConjugacyClasses(quotient) ],
         Concatenation("central quotient fusion is onto ",
                       Identifier(quotient)));
  Demand(CentralQuotientFusionSizesAreExact(target, quotient,
                                            quotientFusion, 2),
         Concatenation("central quotient fusion class sizes are exact for ",
                       Identifier(target)));
  factorTable := CharacterTableFactorGroup(target, reconstructedCenter);;
  Demand(TransformingPermutationsCharacterTables(factorTable, quotient) <> fail,
         Concatenation("factor by center is permutation-equivalent to ",
                       Identifier(quotient)));

  Print("TARGET|identifier=", Identifier(target),
        "|order=", Size(target),
        "|classes=", NrConjugacyClasses(target),
        "|derived=", reconstructedDerived,
        "|outer=", outerPositions,
        "|center=", reconstructedCenter, "\n");
  Print("BASE_FUSION|table=", Identifier(target), "|map=", baseFusion, "\n");
  Print("CENTRAL_QUOTIENT_FUSION|table=", Identifier(target),
        "|quotient=", Identifier(quotient), "|map=", quotientFusion, "\n");
  Print("FAITHFUL_ROWS|table=", Identifier(target), "|rows=", faithfulRows, "\n");

  pairCount := 0;
  nonzeroCount := 0;
  violationCount := 0;
  for row in faithfulRows do
    degree := chars[row][1];
    for class in outerPositions do
      value := chars[row][class];
      nonzero := value <> 0;
      product := degree * classOrders[class];
      remainder := RemInt(Size(target), product);
      pairCount := pairCount + 1;
      if nonzero then
        nonzeroCount := nonzeroCount + 1;
        if remainder <> 0 then
          violationCount := violationCount + 1;
        fi;
      fi;
      Print("PAIR|", Identifier(target), "|", row, "|", rowNames[row],
            "|", degree, "|", class, "|", classNames[class],
            "|", classOrders[class], "|", value, "|", nonzero,
            "|", product, "|", remainder, "\n");
    od;
  od;

  Demand(pairCount = Length(faithfulRows) * Length(outerPositions),
         Concatenation("complete Cartesian grid counted for ", Identifier(target)));
  Demand(violationCount = 0,
         Concatenation("zero nonzero-value divisibility violations for ",
                       Identifier(target)));

  Print("SUMMARY|table=", Identifier(target),
        "|faithful_rows=", Length(faithfulRows),
        "|outer_classes=", Length(outerPositions),
        "|pairs=", pairCount,
        "|nonzero=", nonzeroCount,
        "|violations=", violationCount, "\n");

  grandPairs := grandPairs + pairCount;
  grandNonzero := grandNonzero + nonzeroCount;
  grandViolations := grandViolations + violationCount;
od;

Demand(grandPairs = 869, "combined grid has exactly 869 pairs");
Demand(grandNonzero = 120, "combined grid has exactly 120 nonzero values");
Demand(grandViolations = 0, "combined grid has zero divisibility violations");
Print("TOTAL|pairs=", grandPairs, "|nonzero=", grandNonzero,
      "|violations=", grandViolations, "\n");
Print("FINAL|PASS\n");

QUIT;
