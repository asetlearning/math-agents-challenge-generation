# Frozen bounded checker for Kourovka 21.52, fixed pair PSU(3,3), unique involution class.
# Run only under an external wall-clock timeout and a Lead compute lease.

outputPath := "Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33-full-colour-output.txt";
matrixPath := "Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33-colour-matrix.g";
certificatePath := "Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33-full-colour-certificate.g";

LogTo(outputPath);
Print("BEGIN_PSU33_FULL_COLOUR_CHECKER\n");
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("ATLASREP_LOADED=", LoadPackage("AtlasRep"), "\n");
Print("GRAPE_LOADED=", LoadPackage("GRAPE"), "\n");

Require := function(name, condition)
  if condition then
    Print("CHECK ", name, "=PASS\n");
  else
    Print("CHECK ", name, "=FAIL\n");
    Error(Concatenation("CHECK_FAILED:", name));
  fi;
end;

PreservesAllColours := function(p, matrix, d)
  local i, j;
  for i in [1..d-1] do
    for j in [i+1..d] do
      if matrix[i][j] <> matrix[i^p][j^p] then
        return false;
      fi;
    od;
  od;
  return true;
end;

# GAP's primitive-group library identifies PrimitiveGroup(28,4) as PSU(3,3).
# The separate projective-unitary constructor and an exact isomorphism test guard
# against a library-index or notation mismatch.
L := PrimitiveGroup(28,4);
P := PSU(3,3);
isoLP := IsomorphismGroups(L,P);
Print("L_LIBRARY_ID=PrimitiveGroup(28,4)\n");
Print("L_SIZE=", Size(L), "\n");
Print("L_DEGREE=", LargestMovedPoint(L), "\n");
Print("L_STRUCTURE=", StructureDescription(L), "\n");
Print("PSU_CONSTRUCTOR_SIZE=", Size(P), "\n");
Print("PSU_CONSTRUCTOR_STRUCTURE=", StructureDescription(P), "\n");
Require("L_IS_FINITE", IsFinite(L));
Require("L_IS_NONABELIAN", not IsAbelian(L));
Require("L_IS_SIMPLE", IsSimple(L));
Require("L_CENTRE_TRIVIAL", Size(Centre(L)) = 1);
Require("L_ORDER_6048", Size(L) = 6048);
Require("L_ISOMORPHIC_TO_PSU_3_3_CONSTRUCTOR", isoLP <> fail);

# Inventory every conjugacy class before selecting an involution class.
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
if Length(involutionClasses) <> 1 then
  Print("STOP_NONUNIQUE_INVOLUTION_CLASSES\n");
  LogTo();
  QUIT_GAP(3);
fi;
Require("UNIQUE_INVOLUTION_CLASS", Length(involutionClasses) = 1);

D := Set(Elements(involutionClasses[1]));
d := Length(D);
Require("D_SIZE_63", d = 63);
Require("EVERY_D_ELEMENT_ORDER_2", ForAll(D,x -> Order(x) = 2));
Require("D_IS_SINGLE_FULL_CLASS", Set(D) = Set(Elements(involutionClasses[1])));

# Complete product-order matrix, including diagonal value 1 for convenience.
colourMatrix := List([1..d], i -> List([1..d], j -> Order(D[i]*D[j])));
Require("MATRIX_DIMENSION_63", Length(colourMatrix) = d and
  ForAll(colourMatrix,row -> Length(row) = d));
Require("MATRIX_SYMMETRIC", ForAll([1..d], i ->
  ForAll([1..d], j -> colourMatrix[i][j] = colourMatrix[j][i])));
Require("MATRIX_DIAGONAL_1", ForAll([1..d], i -> colourMatrix[i][i] = 1));

colourOrders := Set(Concatenation(List([1..d-1], i ->
  colourMatrix[i]{[i+1..d]})));
edgeCountByOrder := List(colourOrders, o ->
  Sum([1..d-1], i -> Number([i+1..d], j -> colourMatrix[i][j] = o)));
Print("D_SIZE=", d, "\n");
Print("EDGE_COUNT=", Binomial(d,2), "\n");
Print("PRODUCT_ORDER_COLOURS=", colourOrders, "\n");
Print("EDGE_COUNTS_BY_ORDER=", List([1..Length(colourOrders)],
  k -> [colourOrders[k],edgeCountByOrder[k]]), "\n");
Require("ALL_COMPLETE_GRAPH_EDGES_COLOURED",
  Sum(edgeCountByOrder) = Binomial(d,2));
PrintTo(matrixPath, colourMatrix, ";\n");

# Exact coloured-incidence encoding. Original D-vertices are 1..d. Each
# unordered pair gets one new degree-2 vertex, partitioned by exact |ab|.
pairRecords := [];
nextNode := d;
for i in [1..d-1] do
  for j in [i+1..d] do
    nextNode := nextNode + 1;
    Add(pairRecords,[i,j,colourMatrix[i][j],nextNode]);
  od;
od;
totalNodes := nextNode;
Require("PAIR_RECORD_COUNT", Length(pairRecords) = Binomial(d,2));
Require("INCIDENCE_NODE_COUNT_2016", totalNodes = d + Binomial(d,2));

incidence := NullGraph(Group(()),totalNodes);
for r in pairRecords do
  AddEdgeOrbit(incidence,[r[1],r[4]]);
  AddEdgeOrbit(incidence,[r[4],r[1]]);
  AddEdgeOrbit(incidence,[r[2],r[4]]);
  AddEdgeOrbit(incidence,[r[4],r[2]]);
od;
Require("INCIDENCE_GRAPH_SIMPLE", IsSimpleGraph(incidence));
Require("INCIDENCE_UNDIRECTED_EDGE_COUNT",
  Length(UndirectedEdges(incidence)) = 2*Binomial(d,2));

colourClasses := Concatenation([[1..d]],
  List(colourOrders, o -> Set(List(Filtered(pairRecords,r -> r[3] = o),
    r -> r[4]))));
CheckColourClasses(incidence,colourClasses);
Require("INCIDENCE_VERTEX_PARTITION_COMPLETE",
  Union(colourClasses) = [1..totalNodes] and
  Sum(List(colourClasses,Length)) = totalNodes);

Print("NAUTY_INCIDENCE_AUTOMORPHISM_START\n");
incidenceAut := AutGroupGraph(incidence,colourClasses);
Print("NAUTY_INCIDENCE_AUTOMORPHISM_DONE\n");
Require("INCIDENCE_AUT_PRESERVES_D",
  ForAll(GeneratorsOfGroup(incidenceAut),g -> OnSets([1..d],g) = [1..d]));
incidenceAction := ActionHomomorphism(incidenceAut,[1..d],OnPoints);
Require("INCIDENCE_ACTION_KERNEL_TRIVIAL",
  Size(Kernel(incidenceAction)) = 1);
colourGroup := Image(incidenceAction);
Print("INCIDENCE_AUT_ORDER=", Size(incidenceAut), "\n");
Print("COLOUR_GROUP_ORDER=", Size(colourGroup), "\n");
Print("COLOUR_GROUP_GENERATORS=", GeneratorsOfGroup(colourGroup), "\n");
Require("COLOUR_GROUP_GENERATORS_EXHAUSTIVE_EDGE_CHECK",
  ForAll(GeneratorsOfGroup(colourGroup),
    g -> PreservesAllColours(g,colourMatrix,d)));

# Full exact automorphism group of L and its induced action on the unique class D.
Print("AUTOMORPHISM_GROUP_L_START\n");
autL := AutomorphismGroup(L);
Print("AUTOMORPHISM_GROUP_L_DONE\n");
Print("AUT_L_ORDER=", Size(autL), "\n");
autLGens := GeneratorsOfGroup(autL);
Require("AUT_L_GENERATORS_MAP_D_SETWISE",
  ForAll(autLGens,a -> Set(List(D,x -> Image(a,x))) = D));
inducedGens := List(autLGens, a -> PermList(List([1..d],
  i -> Position(D,Image(a,D[i])))));
autImage := Group(inducedGens,());
Print("AUT_L_RESTRICTION_IMAGE_ORDER=", Size(autImage), "\n");
Print("AUT_L_RESTRICTION_GENERATORS=", GeneratorsOfGroup(autImage), "\n");
Require("AUT_IMAGE_GENERATORS_EXHAUSTIVE_EDGE_CHECK",
  ForAll(GeneratorsOfGroup(autImage),
    g -> PreservesAllColours(g,colourMatrix,d)));
Require("AUT_IMAGE_SUBGROUP_OF_COLOUR_GROUP",
  ForAll(GeneratorsOfGroup(autImage),g -> g in colourGroup));

strictContainment := Size(colourGroup) > Size(autImage);
equalGroups := Size(colourGroup) = Size(autImage) and
  ForAll(GeneratorsOfGroup(colourGroup),g -> g in autImage) and
  ForAll(GeneratorsOfGroup(autImage),g -> g in colourGroup);
Print("STRICT_CONTAINMENT=", strictContainment, "\n");
Print("GROUPS_EQUAL=", equalGroups, "\n");

separator := fail;
if strictContainment then
  separator := First(GeneratorsOfGroup(colourGroup),g -> not g in autImage);
  Require("EXPLICIT_SEPARATOR_FOUND", separator <> fail);
  Print("SEPARATING_PERMUTATION=", separator, "\n");
  Require("SEPARATOR_NOT_IN_AUT_IMAGE", not separator in autImage);
  Require("SEPARATOR_EXHAUSTIVE_ALL_EDGE_COLOUR_CHECK",
    PreservesAllColours(separator,colourMatrix,d));
else
  Require("BOUNDED_GROUP_EQUALITY", equalGroups);
  Print("NO_SEPARATOR_BECAUSE_GROUPS_EQUAL\n");
fi;

# A reconstructible GAP record containing the finite certificate metadata.
PrintTo(certificatePath,
  "PSU33FullColourCertificate := rec(\n",
  "  groupLibraryId := \"PrimitiveGroup(28,4)\",\n",
  "  groupStructure := \"", StructureDescription(L), "\",\n",
  "  groupOrder := ", Size(L), ",\n",
  "  involutionClassCount := ", Length(involutionClasses), ",\n",
  "  involutionClassSize := ", d, ",\n",
  "  productOrderColours := ", colourOrders, ",\n",
  "  edgeCountsByOrder := ", List([1..Length(colourOrders)],
    k -> [colourOrders[k],edgeCountByOrder[k]]), ",\n",
  "  colourGroupOrder := ", Size(colourGroup), ",\n",
  "  colourGroupGenerators := ", GeneratorsOfGroup(colourGroup), ",\n",
  "  autLOrder := ", Size(autL), ",\n",
  "  autRestrictionImageOrder := ", Size(autImage), ",\n",
  "  autRestrictionGenerators := ", GeneratorsOfGroup(autImage), ",\n",
  "  strictContainment := ", strictContainment, ",\n",
  "  groupsEqual := ", equalGroups, ",\n",
  "  separator := ", separator, "\n",
  ");\n");

Print("MATRIX_PATH=", matrixPath, "\n");
Print("CERTIFICATE_PATH=", certificatePath, "\n");
Print("PSU33_FULL_COLOUR_CHECKER_SUCCESS\n");
LogTo();
QUIT;
