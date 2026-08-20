# Independent Validator reconstruction for Kourovka 19.30, fixed target PSL(2,7).
# Frozen before any Validator GAP probe or mathematical enumeration.
# This implementation was written from the source definition and the validation
# request; the claimant's screen-v3.g was not opened or reused.

SizeScreen([ 4096, 24 ]);

Require := function(condition, message)
  if condition <> true then
    Error(message);
  fi;
end;

PackageVersionOrUnknown := function(packageName)
  local info;
  info := PackageInfo(packageName);
  if Length(info) = 0 then
    return "unavailable";
  fi;
  if IsBound(info[1].Version) then
    return info[1].Version;
  fi;
  return "unknown";
end;

VanishingOrderData := function(group)
  local table, classOrders, classSizes, irreducibles, valueRows,
        zeroRowsByClass, classPosition, characterPosition,
        vanishingClassPositions, vanishingOrderSet, degrees;

  table := CharacterTable(group);
  classOrders := OrdersClassRepresentatives(table);
  classSizes := SizesConjugacyClasses(table);
  irreducibles := Irr(table);
  valueRows := List(irreducibles, character -> ValuesOfClassFunction(character));

  Require(Length(classOrders) = Length(classSizes),
          "class-order and class-size vectors have different lengths");
  Require(ForAll(valueRows, row -> Length(row) = Length(classOrders)),
          "an irreducible-character row has the wrong number of classes");
  Require(Sum(classSizes) = Size(group),
          "conjugacy-class sizes do not sum to the group order");

  degrees := List(valueRows, row -> row[1]);
  Require(Sum(degrees, degree -> degree^2) = Size(group),
          "squares of irreducible degrees do not sum to the group order");

  zeroRowsByClass := [];
  for classPosition in [1 .. Length(classOrders)] do
    zeroRowsByClass[classPosition] := [];
    for characterPosition in [1 .. Length(valueRows)] do
      if valueRows[characterPosition][classPosition] = 0 then
        Add(zeroRowsByClass[classPosition], characterPosition);
      fi;
    od;
  od;

  vanishingClassPositions := Filtered(
    [1 .. Length(classOrders)],
    classPosition -> Length(zeroRowsByClass[classPosition]) > 0
  );
  vanishingOrderSet := Set(List(
    vanishingClassPositions,
    classPosition -> classOrders[classPosition]
  ));

  return rec(
    classOrders := classOrders,
    classSizes := classSizes,
    degrees := degrees,
    zeroRowsByClass := zeroRowsByClass,
    vanishingClassPositions := vanishingClassPositions,
    vanishingOrderSet := vanishingOrderSet
  );
end;

Require(LoadPackage("smallgrp") = true,
        "the SmallGrp package could not be loaded");
Require(LoadPackage("ctbllib") = true,
        "the CTblLib package could not be loaded");

Print("RUN\tVALIDATOR-INDEPENDENT-PSL27-ORDER168\n");
Print("GAP_VERSION\t", GAPInfo.Version, "\n");
Print("SMALLGRP_VERSION\t", PackageVersionOrUnknown("smallgrp"), "\n");
Print("CTBLLIB_VERSION\t", PackageVersionOrUnknown("ctbllib"), "\n");
Print("DEFINITION\texact set of class-representative orders for columns with at least one zero in Irr(CharacterTable(group))\n");

catalogueCount := NumberSmallGroups(168);
Require(catalogueCount = 57,
        "NumberSmallGroups(168) is not the claimed complete coverage 57");
Print("CATALOGUE_COUNT\t", catalogueCount, "\n");

target := PSL(2, 7);
Require(Size(target) = 168, "PSL(2,7) does not have order 168");
Require(IsSimpleGroup(target) = true, "PSL(2,7) is not reported simple");
targetId := IdGroup(target);
Require(targetId = [ 168, 42 ],
        "the independently constructed target does not have IdGroup [168,42]");
targetIndex := targetId[2];
targetData := VanishingOrderData(target);

Print("TARGET\tSIZE\t", Size(target),
      "\tIS_SIMPLE\t", IsSimpleGroup(target),
      "\tID_GROUP\t", targetId, "\n");
Print("TARGET_CLASS_ORDERS\t", targetData.classOrders, "\n");
Print("TARGET_CLASS_SIZES\t", targetData.classSizes, "\n");
Print("TARGET_IRREDUCIBLE_DEGREES\t", targetData.degrees, "\n");
Print("TARGET_ZERO_ROWS_BY_CLASS\t", targetData.zeroRowsByClass, "\n");
Print("TARGET_VANISHING_CLASS_POSITIONS\t",
      targetData.vanishingClassPositions, "\n");
Print("TARGET_VANISHING_ORDER_SET\t", targetData.vanishingOrderSet, "\n");

Require(targetData.vanishingOrderSet = [ 2, 3, 4, 7 ],
        "target vanishing-order set differs from [2,3,4,7]");

equalSetIndices := [];
nonisomorphicEqualSetIndices := [];
catalogueTargetData := fail;

for groupIndex in [1 .. catalogueCount] do
  candidate := SmallGroup(168, groupIndex);
  Require(Size(candidate) = 168, "a catalogue candidate has the wrong order");
  candidateId := IdGroup(candidate);
  Require(candidateId = [ 168, groupIndex ],
          "a catalogue candidate's identifier does not match its index");

  candidateData := VanishingOrderData(candidate);
  hasEqualSet := candidateData.vanishingOrderSet = targetData.vanishingOrderSet;

  if hasEqualSet then
    Add(equalSetIndices, groupIndex);
    candidateIsomorphism := IsomorphismGroups(candidate, target);
    if candidateIsomorphism = fail then
      Add(nonisomorphicEqualSetIndices, groupIndex);
    fi;
  fi;

  if groupIndex = targetIndex then
    catalogueTargetData := candidateData;
  fi;

  Print("GROUP\t", groupIndex,
        "\tID_GROUP\t", candidateId,
        "\tSTRUCTURE\t", StructureDescription(candidate),
        "\tNUMBER_OF_CLASSES\t", Length(candidateData.classOrders),
        "\tCLASS_ORDERS\t", candidateData.classOrders,
        "\tCLASS_SIZES\t", candidateData.classSizes,
        "\tIRREDUCIBLE_DEGREES\t", candidateData.degrees,
        "\tZERO_ROWS_BY_CLASS\t", candidateData.zeroRowsByClass,
        "\tVANISHING_CLASS_POSITIONS\t",
        candidateData.vanishingClassPositions,
        "\tVANISHING_ORDER_SET\t", candidateData.vanishingOrderSet,
        "\tEQUALS_TARGET_SET\t", hasEqualSet, "\n");
od;

Require(catalogueTargetData <> fail,
        "the target catalogue row was not encountered");
Require(catalogueTargetData.vanishingOrderSet = targetData.vanishingOrderSet,
        "constructed target and catalogue target have different invariants");
Require(IsomorphismGroups(SmallGroup(168, targetIndex), target) <> fail,
        "catalogue target row is not isomorphic to constructed PSL(2,7)");
Require(equalSetIndices = [ targetIndex ],
        "the exact set-equality indices are not the singleton target index");
Require(Length(nonisomorphicEqualSetIndices) = 0,
        "a nonisomorphic equal-set collision was found");

Print("SUMMARY\tEXPECTED_COVERAGE\t57",
      "\tACTUAL_COVERAGE\t", catalogueCount,
      "\tTARGET_ID\t", targetId,
      "\tTARGET_VANISHING_ORDER_SET\t", targetData.vanishingOrderSet,
      "\tEQUAL_SET_INDICES\t", equalSetIndices,
      "\tNONISOMORPHIC_COLLISION_COUNT\t",
      Length(nonisomorphicEqualSetIndices),
      "\tNONISOMORPHIC_COLLISION_INDICES\t",
      nonisomorphicEqualSetIndices, "\n");
Print("VALIDATION_COMPLETE\ttrue\n");

QUIT_GAP(0);
