LogTo("Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33-inventory-output.txt");
Print("BEGIN_PSU33_INVENTORY\n");
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("ATLASREP_LOADED=", LoadPackage("AtlasRep"), "\n");

L := AtlasGroup("U3(3)", NrMovedPoints, 28);
Print("ATLAS_GROUP_FAIL=", L = fail, "\n");
if L = fail then
  Print("FALLBACK_NR_PRIMITIVE_28=", NrPrimitiveGroups(28), "\n");
  candidates := Filtered([1..NrPrimitiveGroups(28)],
    i -> Size(PrimitiveGroup(28,i)) = 6048);
  Print("FALLBACK_PRIMITIVE_IDS_SIZE_6048=", candidates, "\n");
  if Length(candidates) = 1 then
    L := PrimitiveGroup(28,candidates[1]);
  fi;
fi;

if L <> fail then
  Print("L_SIZE=", Size(L), "\n");
  Print("L_DEGREE=", LargestMovedPoint(L), "\n");
  Print("L_IS_FINITE=", IsFinite(L), "\n");
  Print("L_IS_ABELIAN=", IsAbelian(L), "\n");
  Print("L_IS_SIMPLE=", IsSimple(L), "\n");
  Print("L_CENTRE_SIZE=", Size(Centre(L)), "\n");
  Print("L_STRUCTURE=", StructureDescription(L), "\n");
  Print("PSU_CONSTRUCTOR_BOUND=", IsBoundGlobal("PSU"), "\n");
  if IsBoundGlobal("PSU") then
    P := PSU(3,3);
    Print("PSU_SIZE=", Size(P), "\n");
    Print("PSU_IS_SIMPLE=", IsSimple(P), "\n");
    Print("PSU_STRUCTURE=", StructureDescription(P), "\n");
    iso := IsomorphismGroups(L,P);
    Print("ATLAS_ISOMORPHIC_TO_PSU33=", iso <> fail, "\n");
  fi;

  classes := ConjugacyClasses(L);
  Print("CLASS_COUNT=", Length(classes), "\n");
  Print("CLASS_INVENTORY_BEGIN\n");
  for i in [1..Length(classes)] do
    Print(i, ":order=", Order(Representative(classes[i])),
      ":size=", Size(classes[i]),
      ":centralizer=", Size(Centralizer(L,Representative(classes[i]))), "\n");
  od;
  Print("CLASS_INVENTORY_END\n");
  involutionClasses := Filtered(classes,
    c -> Order(Representative(c)) = 2);
  Print("INVOLUTION_CLASS_COUNT=", Length(involutionClasses), "\n");
  Print("INVOLUTION_CLASS_SIZES=", List(involutionClasses,Size), "\n");
fi;
Print("END_PSU33_INVENTORY\n");
LogTo();
QUIT;
