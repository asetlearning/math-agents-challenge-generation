LoadPackage("ctbllib");;
SizeScreen([4096,1000]);;

BoolString := function(b)
  if b then
    return "true";
  fi;
  return "false";
end;;

gapVersion := GAPInfo.Version;;
ctblVersion := PackageInfo("ctbllib")[1].Version;;
irr := [];;
source := CharacterTable("2.L4(3)");;
simple := CharacterTable("L4(3)");;
sourceToSimple := GetFusionMap(source, simple);;
sourceCentre := ClassPositionsOfCenter(source);;
sourceDerived := ClassPositionsOfDerivedSubgroup(source);;

Print("RUN|strategy=L43-GRAPH-EXTENSIONS|gap=", gapVersion,
      "|ctbllib=", ctblVersion,
      "|tables=2.L4(3).2_2,2.L4(3).2_3\n");
Print("SOURCE|id=", Identifier(source),
      "|order=", Size(source),
      "|classes=", NrConjugacyClasses(source),
      "|centre_positions=", sourceCentre,
      "|centre_order=", Length(sourceCentre),
      "|derived_positions=", sourceDerived,
      "|perfect=", BoolString(sourceDerived = [1..NrConjugacyClasses(source)]),
      "|central_quotient_id=", Identifier(simple),
      "|central_quotient_order=", Size(simple),
      "|central_projection_kernel_positions=", Positions(sourceToSimple, 1),
      "|central_quotient_simple_table=", BoolString(IsSimpleCharacterTable(simple)),
      "\n");

for entry in [
    ["2.L4(3).2_2", "L4(3).2_2", "graph-via-D3=A3/PGO+"],
    ["2.L4(3).2_3", "L4(3).2_3", "diagonal-graph-by-exhaustion"]
  ] do
  id := entry[1];;
  quotientId := entry[2];;
  outerType := entry[3];;
  tbl := CharacterTable(id);;
  quotient := CharacterTable(quotientId);;
  irr := Irr(tbl);;
  classOrders := OrdersClassRepresentatives(tbl);;
  classSizes := SizesConjugacyClasses(tbl);;
  classNames := AtlasClassNames(tbl);;
  charNames := CharacterNames(tbl);;
  derivedPositions := ClassPositionsOfDerivedSubgroup(tbl);;
  centrePositions := ClassPositionsOfCenter(tbl);;
  sourceFusion := GetFusionMap(source, tbl);;
  quotientFusion := GetFusionMap(tbl, quotient);;
  simpleFusion := GetFusionMap(simple, quotient);;
  quotientDerivedPositions := ClassPositionsOfDerivedSubgroup(quotient);;
  quotientCentrePositions := ClassPositionsOfCenter(quotient);;
  outerPositions := Difference([1..NrConjugacyClasses(tbl)], derivedPositions);;
  faithfulRows := Filtered([1..Length(irr)],
      i -> ClassPositionsOfKernel(irr[i]) = [1]);;
  constructionInfo := ConstructionInfoCharacterTable(tbl);;
  degreeSquareSum := Sum(irr, chi -> chi[1]^2);;
  classSizeSum := Sum(classSizes);;
  derivedSizeFromClasses := Sum(classSizes{derivedPositions});;
  allValuesCyclotomic := ForAll(irr, chi -> ForAll(chi, IsCyc));;
  structuralPass :=
      IsOrdinaryTable(tbl) and UnderlyingCharacteristic(tbl) = 0 and
      Size(tbl) = 2 * Size(source) and
      Set(sourceFusion) = Set(derivedPositions) and
      derivedSizeFromClasses = Size(source) and
      centrePositions = Set(sourceFusion{sourceCentre}) and
      centrePositions = [1,2] and
      Positions(quotientFusion, 1) = centrePositions and
      Size(quotient) * Length(centrePositions) = Size(tbl) and
      Set(simpleFusion) = Set(quotientDerivedPositions) and
      quotientCentrePositions = [1] and
      degreeSquareSum = Size(tbl) and classSizeSum = Size(tbl) and
      allValuesCyclotomic;

  Print("TABLE|id=", Identifier(tbl),
        "|declared_outer_type=", outerType,
        "|ordinary=", BoolString(IsOrdinaryTable(tbl)),
        "|underlying_characteristic=", UnderlyingCharacteristic(tbl),
        "|info=", InfoText(tbl),
        "|order=", Size(tbl),
        "|rows=", Length(irr),
        "|classes=", NrConjugacyClasses(tbl),
        "|class_size_sum=", classSizeSum,
        "|degree_square_sum=", degreeSquareSum,
        "|all_values_cyclotomic=", BoolString(allValuesCyclotomic),
        "|construction_info=", constructionInfo,
        "\n");
  Print("STRUCTURE|id=", id,
        "|source_id=", Identifier(source),
        "|source_order=", Size(source),
        "|index=", Size(tbl)/Size(source),
        "|fusion_sources=", NamesOfFusionSources(tbl),
        "|source_fusion=", sourceFusion,
        "|source_fusion_image=", Set(sourceFusion),
        "|derived_positions=", derivedPositions,
        "|derived_size_from_classes=", derivedSizeFromClasses,
        "|centre_positions=", centrePositions,
        "|source_centre_image=", Set(sourceFusion{sourceCentre}),
        "|quotient_id=", Identifier(quotient),
        "|quotient_order=", Size(quotient),
        "|quotient_fusion=", quotientFusion,
        "|quotient_kernel_positions=", Positions(quotientFusion,1),
        "|quotient_centre_positions=", quotientCentrePositions,
        "|quotient_derived_positions=", quotientDerivedPositions,
        "|simple_fusion_image=", Set(simpleFusion),
        "|outer_positions=", outerPositions,
        "|structural_pass=", BoolString(structuralPass),
        "\n");

  for j in outerPositions do
    Print("OUTER_CLASS|table=", id,
          "|class=", j,
          "|label=", classNames[j],
          "|order=", classOrders[j],
          "|size=", classSizes[j],
          "|generates_mod_derived=true\n");
  od;

  for i in faithfulRows do
    Print("FAITHFUL_ROW|table=", id,
          "|row=", i,
          "|label=", charNames[i],
          "|degree=", irr[i][1],
          "|kernel_positions=", ClassPositionsOfKernel(irr[i]),
          "\n");
  od;

  pairCount := 0;;
  nonzeroCount := 0;;
  violationCount := 0;;
  for i in faithfulRows do
    for j in outerPositions do
      pairCount := pairCount + 1;;
      value := irr[i][j];;
      nonzero := not IsZero(value);;
      product := irr[i][1] * classOrders[j];;
      remainder := RemInt(Size(tbl), product);;
      divides := remainder = 0;;
      violation := nonzero and not divides;;
      if nonzero then
        nonzeroCount := nonzeroCount + 1;;
      fi;
      if violation then
        violationCount := violationCount + 1;;
      fi;
      Print("PAIR|table=", id,
            "|row=", i,
            "|row_label=", charNames[i],
            "|degree=", irr[i][1],
            "|kernel_positions=", ClassPositionsOfKernel(irr[i]),
            "|class=", j,
            "|class_label=", classNames[j],
            "|class_order=", classOrders[j],
            "|class_size=", classSizes[j],
            "|value=", value,
            "|nonzero=", BoolString(nonzero),
            "|product=", product,
            "|remainder=", remainder,
            "|divides=", BoolString(divides),
            "|violation=", BoolString(violation),
            "\n");
    od;
  od;
  Print("SUMMARY|table=", id,
        "|faithful_rows=", Length(faithfulRows),
        "|outer_classes=", Length(outerPositions),
        "|pairs=", pairCount,
        "|nonzero_pairs=", nonzeroCount,
        "|violations=", violationCount,
        "|structural_pass=", BoolString(structuralPass),
        "\n");
od;

QUIT;
