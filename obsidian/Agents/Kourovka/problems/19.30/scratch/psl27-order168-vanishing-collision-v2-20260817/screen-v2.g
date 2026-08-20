# Frozen corrected-coverage exact screen for Kourovka 19.30, target PSL(2,7).
# The value 57 is taken only from the persistent sanctioned v1 guard output.

AssertOrQuit := function(condition, message)
  if not condition then
    Print("FATAL\t", message, "\n");
    QUIT_GAP(2);
  fi;
end;

VanishingData := function(group)
  local table, irreducibles, classOrders, classSizes, degrees,
        zeroWitnesses, vanishingClassIndices, vanishingOrders;

  table := CharacterTable(group);
  irreducibles := Irr(table);
  classOrders := OrdersClassRepresentatives(table);
  classSizes := SizesConjugacyClasses(table);
  degrees := List(irreducibles, chi -> chi[1]);
  zeroWitnesses := List(
    [1..Length(classOrders)],
    classIndex -> Filtered(
      [1..Length(irreducibles)],
      characterIndex -> irreducibles[characterIndex][classIndex] = 0
    )
  );
  vanishingClassIndices := Filtered(
    [1..Length(classOrders)],
    classIndex -> Length(zeroWitnesses[classIndex]) > 0
  );
  vanishingOrders := Set(List(
    vanishingClassIndices,
    classIndex -> classOrders[classIndex]
  ));

  AssertOrQuit(
    Length(irreducibles) = Length(classOrders),
    "number of irreducibles differs from number of conjugacy classes"
  );
  AssertOrQuit(
    Length(classSizes) = Length(classOrders),
    "class-size and class-order lists have different lengths"
  );
  AssertOrQuit(
    Sum(classSizes) = Size(group),
    "conjugacy-class sizes do not sum to the group order"
  );
  AssertOrQuit(
    Sum(degrees, degree -> degree^2) = Size(group),
    "squared irreducible degrees do not sum to the group order"
  );

  return rec(
    irreducibles := irreducibles,
    classOrders := classOrders,
    classSizes := classSizes,
    degrees := degrees,
    zeroWitnesses := zeroWitnesses,
    vanishingClassIndices := vanishingClassIndices,
    vanishingOrders := vanishingOrders
  );
end;

PrintExactTableData := function(label, libraryIndex, data)
  local characterIndex;

  Print("TABLE\t", label, "\t", libraryIndex,
        "\tCLASS_ORDERS\t", data.classOrders, "\n");
  Print("TABLE\t", label, "\t", libraryIndex,
        "\tCLASS_SIZES\t", data.classSizes, "\n");
  Print("TABLE\t", label, "\t", libraryIndex,
        "\tIRREDUCIBLE_DEGREES\t", data.degrees, "\n");
  Print("TABLE\t", label, "\t", libraryIndex,
        "\tZERO_WITNESSES_BY_CLASS\t", data.zeroWitnesses, "\n");
  Print("TABLE\t", label, "\t", libraryIndex,
        "\tVANISHING_CLASS_INDICES\t", data.vanishingClassIndices, "\n");
  Print("TABLE\t", label, "\t", libraryIndex,
        "\tVANISHING_ORDER_SET\t", data.vanishingOrders, "\n");

  for characterIndex in [1..Length(data.irreducibles)] do
    Print("IRR_VALUES\t", label, "\t", libraryIndex, "\t",
          characterIndex, "\t",
          List(
            [1..Length(data.classOrders)],
            classIndex -> data.irreducibles[characterIndex][classIndex]
          ),
          "\n");
  od;
end;

expectedOrder := 168;
expectedCoverage := 57;

Print("RUN\tPSL27-ORDER168-VANISHING-COLLISION-V2\n");
Print("GAP_VERSION\t", GAPInfo.Version, "\n");
Print("INVARIANT\tset of element orders attained by classes on which at least one ordinary irreducible complex character is exactly zero; multiplicities discarded\n");

actualCoverage := NumberSmallGroups(expectedOrder);
Print("COVERAGE\tNumberSmallGroups(168)\tEXPECTED\t",
      expectedCoverage, "\tACTUAL\t", actualCoverage, "\n");
AssertOrQuit(
  actualCoverage = expectedCoverage,
  "SmallGroups-library coverage count for order 168 is not the frozen value 57"
);

target := PSL(2, 7);
AssertOrQuit(Size(target) = expectedOrder, "PSL(2,7) does not have order 168");
AssertOrQuit(IsSimpleGroup(target), "PSL(2,7) did not pass IsSimpleGroup");
targetId := IdGroup(target);
AssertOrQuit(
  targetId[1] = expectedOrder,
  "IdGroup(PSL(2,7)) has the wrong order component"
);
AssertOrQuit(
  targetId[2] >= 1 and targetId[2] <= actualCoverage,
  "IdGroup(PSL(2,7)) has an index outside the complete order-168 coverage"
);
Print("TARGET\tPSL(2,7)\tSIZE\t", Size(target),
      "\tIS_SIMPLE\t", IsSimpleGroup(target),
      "\tID_GROUP\t", targetId, "\n");

targetLibraryGroup := SmallGroup(targetId[1], targetId[2]);
AssertOrQuit(
  IsomorphismGroups(target, targetLibraryGroup) <> fail,
  "the PSL(2,7) construction is not isomorphic to its IdGroup representative"
);
targetData := VanishingData(target);
targetLibraryData := VanishingData(targetLibraryGroup);
AssertOrQuit(
  targetData.vanishingOrders = targetLibraryData.vanishingOrders,
  "PSL(2,7) and its SmallGroup representative have different vanishing-order sets"
);
PrintExactTableData("TARGET_PSL27", targetId[2], targetData);
PrintExactTableData("TARGET_SMALLGROUP", targetId[2], targetLibraryData);

completed := 0;
collisionIndices := [];

for libraryIndex in [1..actualCoverage] do
  group := SmallGroup(expectedOrder, libraryIndex);
  groupId := IdGroup(group);
  AssertOrQuit(
    groupId = [expectedOrder, libraryIndex],
    Concatenation("IdGroup mismatch at library index ", String(libraryIndex))
  );
  data := VanishingData(group);
  completed := completed + 1;

  Print("GROUP\t", libraryIndex,
        "\tID_GROUP\t", groupId,
        "\tSTRUCTURE\t", StructureDescription(group),
        "\tNUMBER_OF_CLASSES\t", Length(data.classOrders),
        "\tVANISHING_ORDER_SET\t", data.vanishingOrders,
        "\tEQUALS_TARGET_SET\t",
        data.vanishingOrders = targetData.vanishingOrders,
        "\n");
  PrintExactTableData("SMALLGROUP_168", libraryIndex, data);

  if data.vanishingOrders = targetData.vanishingOrders
     and libraryIndex <> targetId[2] then
    candidateIsomorphism := IsomorphismGroups(group, target);
    AssertOrQuit(
      candidateIsomorphism = fail,
      Concatenation("distinct SmallGroup ID unexpectedly isomorphic at index ",
                    String(libraryIndex))
    );

    permutationIsomorphism := IsomorphismPermGroup(group);
    permutationGroup := Image(permutationIsomorphism);
    AssertOrQuit(
      Size(permutationGroup) = expectedOrder,
      "materialized permutation group has the wrong order"
    );
    AssertOrQuit(
      IdGroup(permutationGroup) = groupId,
      "materialized permutation group has the wrong IdGroup"
    );
    AssertOrQuit(
      IsomorphismGroups(permutationGroup, target) = fail,
      "materialized permutation group is unexpectedly isomorphic to PSL(2,7)"
    );
    permutationData := VanishingData(permutationGroup);
    AssertOrQuit(
      permutationData.vanishingOrders = targetData.vanishingOrders,
      "materialized permutation group does not reproduce the collision"
    );

    Add(collisionIndices, libraryIndex);
    Print("COLLISION\tSMALLGROUP_ID\t", groupId,
          "\tSTRUCTURE\t", StructureDescription(group),
          "\tPERMUTATION_GENERATORS\t", GeneratorsOfGroup(permutationGroup),
          "\tVANISHING_ORDER_SET\t", permutationData.vanishingOrders,
          "\tNONISOMORPHIC_TO_PSL27\ttrue\n");
    PrintExactTableData(
      "COLLISION_PERMUTATION_MATERIALIZATION",
      libraryIndex,
      permutationData
    );
  fi;
od;

AssertOrQuit(completed = actualCoverage, "enumeration did not complete every row");
Print("SUMMARY\tEXPECTED_COVERAGE\t", expectedCoverage,
      "\tACTUAL_COVERAGE\t", actualCoverage,
      "\tCOMPLETED\t", completed,
      "\tTARGET_ID\t", targetId,
      "\tTARGET_VANISHING_ORDER_SET\t", targetData.vanishingOrders,
      "\tNONISOMORPHIC_COLLISION_COUNT\t", Length(collisionIndices),
      "\tCOLLISION_INDICES\t", collisionIndices,
      "\n");

QUIT_GAP(0);
