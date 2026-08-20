# Independent Validator reconstruction for Kourovka 19.30, fixed target A6.
#
# The submitted computation used OrdersClassRepresentatives(CharacterTable(H))
# directly.  This checker instead takes the actual conjugacy classes stored on
# the character table constructed from each concrete group, takes actual class
# representatives, obtains their element orders with Order, and aligns those
# classes with the exact ordinary characters returned by Irr(group).

SizeScreen([ 4096, 24 ]);

Require := function(condition, message)
  if condition <> true then
    Error(message);
  fi;
end;

BoolWord := function(value)
  if value = true then
    return "true";
  fi;
  return "false";
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

ActualVanishingData := function(group)
  local table, classes, representatives, actualClassOrders, tableClassOrders,
        actualClassSizes, tableClassSizes, irreducibles, valueRows, degrees,
        zeroCounts, classPosition, vanishingClassPositions,
        vanishingOrderSet;

  table := CharacterTable(group);
  Require(UnderlyingCharacteristic(table) = 0,
          "character table is not ordinary (characteristic zero)");
  Require(HasUnderlyingGroup(table),
          "character table has no stored underlying group");
  Require(UnderlyingGroup(table) = group,
          "character table's underlying group is not the candidate group");

  classes := ConjugacyClasses(table);
  representatives := List(classes, Representative);
  actualClassOrders := List(representatives, Order);
  tableClassOrders := OrdersClassRepresentatives(table);
  Require(actualClassOrders = tableClassOrders,
          "actual representative orders disagree with table class orders");

  actualClassSizes := List(classes, Size);
  tableClassSizes := SizesConjugacyClasses(table);
  Require(actualClassSizes = tableClassSizes,
          "actual conjugacy-class sizes disagree with table class sizes");
  Require(Sum(actualClassSizes) = Size(group),
          "actual conjugacy-class sizes do not sum to the group order");

  irreducibles := Irr(group);
  Require(Length(irreducibles) = Length(classes),
          "number of ordinary irreducibles differs from number of classes");
  Require(ForAll(irreducibles,
                 character -> UnderlyingCharacteristic(character) = 0),
          "a returned irreducible is not an ordinary character");
  Require(ForAll(irreducibles,
                 character -> UnderlyingCharacterTable(character) = table),
          "irreducible character uses a different class ordering");

  valueRows := List(irreducibles, ValuesOfClassFunction);
  Require(ForAll(valueRows,
                 row -> Length(row) = Length(actualClassOrders)),
          "irreducible-character value row has the wrong length");
  degrees := List(valueRows, row -> row[1]);
  Require(Sum(degrees, degree -> degree^2) = Size(group),
          "squares of ordinary irreducible degrees do not sum to group order");

  zeroCounts := [];
  for classPosition in [1 .. Length(classes)] do
    zeroCounts[classPosition] := Number(
      valueRows,
      row -> row[classPosition] = 0
    );
  od;

  vanishingClassPositions := Filtered(
    [1 .. Length(classes)],
    classPosition -> zeroCounts[classPosition] > 0
  );
  vanishingOrderSet := Set(List(
    vanishingClassPositions,
    classPosition -> actualClassOrders[classPosition]
  ));

  return rec(
    classOrders := actualClassOrders,
    classSizes := actualClassSizes,
    degrees := degrees,
    zeroCounts := zeroCounts,
    vanishingClassPositions := vanishingClassPositions,
    vanishingOrderSet := vanishingOrderSet
  );
end;

Require(LoadPackage("smallgrp") = true,
        "SmallGrp package could not be loaded");
Require(LoadPackage("ctbllib") = true,
        "CTblLib package could not be loaded");
Require(SmallGroupsAvailable(360) = true,
        "SmallGroups catalogue is unavailable at order 360");

Print("RUN\tVALIDATOR-INDEPENDENT-A6-ORDER360\n");
Print("GAP_VERSION\t", GAPInfo.Version, "\n");
Print("SMALLGRP_VERSION\t", PackageVersionOrUnknown("smallgrp"), "\n");
Print("CTBLLIB_VERSION\t", PackageVersionOrUnknown("ctbllib"), "\n");
Print("DEFINITION\torders of actual class representatives whose aligned ordinary Irr(group) column has at least one exact zero\n");

catalogueCount := NumberSmallGroups(360);
Require(catalogueCount = 162,
        "NumberSmallGroups(360) is not the submitted coverage count 162");
Print("CATALOGUE_COUNT\t", catalogueCount, "\n");

target := AlternatingGroup(6);
Require(Size(target) = 360, "AlternatingGroup(6) does not have order 360");
Require(IsSimpleGroup(target) = true,
        "AlternatingGroup(6) is not reported simple");
targetId := IdGroup(target);
Require(targetId = [ 360, 118 ],
        "AlternatingGroup(6) does not have IdGroup [360,118]");
targetIndex := targetId[2];
targetData := ActualVanishingData(target);
Require(targetData.vanishingOrderSet = [ 2, 3, 4, 5 ],
        "A6 vanishing-order set differs from [2,3,4,5]");

Print("TARGET\tSIZE\t", Size(target),
      "\tIS_SIMPLE\t", BoolWord(IsSimpleGroup(target)),
      "\tID_GROUP\t", targetId, "\n");
Print("TARGET_CLASS_ORDERS\t", targetData.classOrders, "\n");
Print("TARGET_ZERO_COUNTS\t", targetData.zeroCounts, "\n");
Print("TARGET_VANISHING_CLASS_POSITIONS\t",
      targetData.vanishingClassPositions, "\n");
Print("TARGET_VANISHING_ORDER_SET\t", targetData.vanishingOrderSet, "\n");

seenIndices := [];
equalSetIndices := [];
nonisomorphicCollisionIndices := [];
catalogueTargetSet := fail;

for groupIndex in [1 .. catalogueCount] do
  candidate := SmallGroup(360, groupIndex);
  Require(Size(candidate) = 360,
          "a SmallGroups order-360 candidate has the wrong size");
  candidateId := IdGroup(candidate);
  Require(candidateId = [ 360, groupIndex ],
          "a candidate IdGroup does not match its catalogue index");

  candidateData := ActualVanishingData(candidate);
  hasEqualSet := candidateData.vanishingOrderSet =
                 targetData.vanishingOrderSet;
  Add(seenIndices, groupIndex);

  if hasEqualSet then
    Add(equalSetIndices, groupIndex);
    candidateIsomorphism := IsomorphismGroups(candidate, target);
    if candidateIsomorphism = fail then
      Add(nonisomorphicCollisionIndices, groupIndex);
    fi;
  fi;

  if groupIndex = targetIndex then
    catalogueTargetSet := candidateData.vanishingOrderSet;
  fi;

  Print("GROUP\t", groupIndex,
        "\tSIZE\t", Size(candidate),
        "\tID_GROUP\t", candidateId,
        "\tNUMBER_OF_CLASSES\t", Length(candidateData.classOrders), "\n");
  Print("GROUP_CLASS_ORDERS\t", groupIndex,
        "\t", candidateData.classOrders, "\n");
  Print("GROUP_ZERO_COUNTS\t", groupIndex,
        "\t", candidateData.zeroCounts, "\n");
  Print("GROUP_VANISHING_CLASS_POSITIONS\t", groupIndex,
        "\t", candidateData.vanishingClassPositions, "\n");
  Print("GROUP_VANISHING_ORDER_SET\t", groupIndex,
        "\t", candidateData.vanishingOrderSet,
        "\tEQUALS_TARGET_SET\t", BoolWord(hasEqualSet), "\n");
od;

Require(seenIndices = [1 .. catalogueCount],
        "catalogue indices were not visited exactly once in order");
Require(catalogueTargetSet <> fail,
        "the target catalogue row was not visited");
Require(catalogueTargetSet = targetData.vanishingOrderSet,
        "constructed A6 and catalogue target row have different invariants");
Require(IsomorphismGroups(SmallGroup(360, targetIndex), target) <> fail,
        "SmallGroup(360,118) is not isomorphic to constructed A6");
Require(equalSetIndices = [ targetIndex ],
        "equal-set indices are not the singleton target index");
Require(nonisomorphicCollisionIndices = [],
        "a nonisomorphic equal-set collision exists");

Print("SUMMARY\tCATALOGUE_COUNT\t", catalogueCount,
      "\tTARGET_INDEX\t", targetIndex,
      "\tEQUAL_SET_INDICES\t", equalSetIndices,
      "\tCOLLISION_INDICES\t", nonisomorphicCollisionIndices, "\n");
Print("VALIDATION_COMPLETE\ttrue\n");

QUIT_GAP(0);
