# Frozen exact checker for the fixed PSL(3,3) instance of Kourovka 21.52.
#
# Model: L is a faithful permutation image of SL(3,3)=PSL(3,3).
# The full edge-coloured complete graph on one involution class is encoded as a
# vertex-coloured subdivision/incidence graph.  Its original vertices are one
# colour class; its edge-vertices are partitioned by the exact order of ab.

if LoadPackage("grape") <> true then
  Error("GRAPE is required");
fi;

Require := function(condition, message)
  if not condition then
    Error(message);
  fi;
end;

S := SL(3, 3);
Require(Size(S) = 5616, "unexpected order for SL(3,3)");
Require(Size(Centre(S)) = 1, "SL(3,3) has unexpected centre");
standardPSL := PSL(3, 3);
Require(Size(standardPSL) = 5616, "unexpected order for PSL(3,3)");
slToPSL := IsomorphismGroups(S, standardPSL);
Require(slToPSL <> fail, "SL(3,3) is not isomorphic to PSL(3,3)");

permIso := IsomorphismPermGroup(S);
Require(permIso <> fail, "no faithful permutation image for SL(3,3)");
L := Image(permIso);
Require(Size(L) = 5616, "unexpected permutation-image order");
Require(not IsAbelian(L), "L is abelian");
Require(IsSimpleGroup(L), "L is not simple");

allClasses := ConjugacyClasses(L);
involutionClasses := Filtered(allClasses,
  C -> Order(Representative(C)) = 2);
involutionClassSizes := List(involutionClasses, Size);
Require(Length(involutionClasses) = 1,
        "expected exactly one involution conjugacy class");
D := AsSSortedList(involutionClasses[1]);
n := Length(D);
Require(n = 117, "unexpected involution class size");
Require(ForAll(D, x -> Order(x) = 2),
        "selected class contains a non-involution");

# Complete exact product-order matrix and all unordered edges.
productOrderMatrix := List([1..n],
  i -> List([1..n], j -> Order(D[i] * D[j])));
edgeRecords := [];
edgeOrders := [];
edgeVertex := n;
incidenceArcs := [];
for i in [1..n-1] do
  for j in [i+1..n] do
    edgeVertex := edgeVertex + 1;
    colour := productOrderMatrix[i][j];
    Add(edgeRecords, [i, j, edgeVertex, colour]);
    Add(edgeOrders, colour);
    Add(incidenceArcs, [i, edgeVertex]);
    Add(incidenceArcs, [edgeVertex, i]);
    Add(incidenceArcs, [j, edgeVertex]);
    Add(incidenceArcs, [edgeVertex, j]);
  od;
od;
Require(Length(edgeRecords) = n * (n - 1) / 2,
        "unordered edge list is incomplete");
colourValues := Set(edgeOrders);
edgeColourClasses := List(colourValues,
  c -> List(Filtered(edgeRecords, e -> e[4] = c), e -> e[3]));
edgeColourCounts := List(edgeColourClasses, Length);
Require(Sum(edgeColourCounts) = Length(edgeRecords),
        "edge colour classes are incomplete");

# Exact full colour group.  An automorphism of this vertex-coloured incidence
# graph restricts faithfully to D because every edge-vertex is uniquely
# determined by its two original endpoints.
incidenceGraph := EdgeOrbitsGraph(Group(()), incidenceArcs, edgeVertex);
vertexColourClasses := Concatenation([[1..n]], edgeColourClasses);
incidenceAut := AutGroupGraph(incidenceGraph,
                              ShallowCopy(vertexColourClasses));
colourAction := Action(incidenceAut, [1..n], OnPoints);
Require(Size(colourAction) = Size(incidenceAut),
        "incidence automorphism has a nontrivial kernel on D");
Require(ForAll(GeneratorsOfGroup(colourAction), p ->
  ForAll([1..n-1], i -> ForAll([i+1..n], j ->
    productOrderMatrix[i][j] =
    productOrderMatrix[i^p][j^p]))),
  "a colour-group generator failed the exhaustive direct colour check");

# Compute Aut(L), its setwise stabilizer of the unique involution class, and
# its exact restriction image.  Uniqueness makes the stabilizer all of Aut(L).
autL := AutomorphismGroup(L);
autLGens := GeneratorsOfGroup(autL);
Require(ForAll(autLGens, a ->
  Set(List(D, x -> Image(a, x))) = Set(D)),
  "an Aut(L) generator does not stabilize D");
autPermGens := List(autLGens, a ->
  PermList(List(D, x -> PositionSorted(D, Image(a, x)))));
Require(not (fail in autPermGens),
        "failed to construct an Aut(L) restriction generator");
autAction := Group(autPermGens);
Require(Size(autAction) = Size(autL),
        "Aut(L) restriction has a nontrivial kernel on D");
Require(ForAll(GeneratorsOfGroup(autAction), p ->
  ForAll([1..n-1], i -> ForAll([i+1..n], j ->
    productOrderMatrix[i][j] =
    productOrderMatrix[i^p][j^p]))),
  "an Aut(L) restriction generator failed the exhaustive colour check");

autContainedInColour := IsSubgroup(colourAction, autAction);
colourContainedInAut := IsSubgroup(autAction, colourAction);
groupsEqual := autContainedInColour and colourContainedInAut;
separator := fail;
separatorPassesAllEdges := false;
if autContainedInColour and not colourContainedInAut then
  separator := First(GeneratorsOfGroup(colourAction), g -> not g in autAction);
  Require(separator <> fail, "strict containment has no separating generator");
  separatorPassesAllEdges := ForAll([1..n-1], i ->
    ForAll([i+1..n], j ->
      productOrderMatrix[i][j] =
      productOrderMatrix[i^separator][j^separator]));
  Require(separatorPassesAllEdges,
          "separating permutation failed exhaustive colour check");
fi;

Print("PSL33_FULL_COLOUR_CERTIFICATE_V1\n");
Print("gap_version=", GAPInfo.Version, "\n");
Print("grape_version=", PackageInfo("grape")[1].Version, "\n");
Print("sl_order=", Size(S), "\n");
Print("sl_centre_order=", Size(Centre(S)), "\n");
Print("psl_order=", Size(standardPSL), "\n");
Print("sl_isomorphic_to_psl=", slToPSL <> fail, "\n");
Print("L_order=", Size(L), "\n");
Print("L_nonabelian=", not IsAbelian(L), "\n");
Print("L_simple=", IsSimpleGroup(L), "\n");
Print("involution_class_count=", Length(involutionClasses), "\n");
Print("involution_class_sizes=", involutionClassSizes, "\n");
Print("selected_class_size=", n, "\n");
Print("unordered_edge_count=", Length(edgeRecords), "\n");
Print("colour_values=", colourValues, "\n");
Print("edge_colour_counts=", edgeColourCounts, "\n");
Print("product_order_matrix=", productOrderMatrix, "\n");
Print("incidence_graph_order=", incidenceGraph.order, "\n");
Print("incidence_aut_order=", Size(incidenceAut), "\n");
Print("colour_action_order=", Size(colourAction), "\n");
Print("colour_action_generators=", GeneratorsOfGroup(colourAction), "\n");
Print("autL_order=", Size(autL), "\n");
Print("setwise_stabilizer_order=", Size(autL), "\n");
Print("aut_action_order=", Size(autAction), "\n");
Print("aut_action_generators=", GeneratorsOfGroup(autAction), "\n");
Print("aut_contained_in_colour=", autContainedInColour, "\n");
Print("colour_contained_in_aut=", colourContainedInAut, "\n");
Print("groups_equal=", groupsEqual, "\n");
Print("separator=", separator, "\n");
Print("separator_passes_all_edges=", separatorPassesAllEdges, "\n");

QUIT_GAP(0);
