# Independent bounded checker for the fixed PSL(2,7) instance of Kourovka 21.52.
#
# This checker deliberately does not implement the claimant's edge-exposure
# backtracking.  It converts the edge-coloured complete graph into a
# vertex-coloured incidence graph and asks GRAPE/nauty for the full automorphism
# group of that incidence graph.  The restriction to the 21 original vertices is
# faithful because each edge-vertex is uniquely determined by its two endpoints.

if LoadPackage("grape") <> true then
  Error("GRAPE is required");
fi;

Require := function(condition, message)
  if not condition then
    Error(message);
  fi;
end;

# Reconstruct SL(2,7)/Z(SL(2,7)) and then take a faithful permutation image.
S := SL(2, 7);
Z := Centre(S);
Require(Size(S) = 336, "unexpected order for SL(2,7)");
Require(Size(Z) = 2, "unexpected centre for SL(2,7)");
quotientMap := NaturalHomomorphismByNormalSubgroup(S, Z);
Q := Image(quotientMap);
permIso := IsomorphismPermGroup(Q);
Require(permIso <> fail, "no permutation isomorphism for the quotient");
L := Image(permIso);
Require(Size(L) = 168, "unexpected quotient order");
Require(not IsAbelian(L), "quotient is abelian");
Require(IsSimpleGroup(L), "quotient is not simple");
standardPSL := PSL(2, 7);
quotientToStandard := IsomorphismGroups(L, standardPSL);
Require(quotientToStandard <> fail,
        "explicit quotient is not isomorphic to GAP's PSL(2,7)");

# Reconstruct all involution classes, and require the unique class in this group.
involutionClasses := Filtered(ConjugacyClasses(L),
  C -> Order(Representative(C)) = 2);
Require(Length(involutionClasses) = 1,
        "expected exactly one involution conjugacy class");
D := AsSSortedList(involutionClasses[1]);
n := Length(D);
Require(n = 21, "unexpected involution class size");
Require(ForAll(D, x -> Order(x) = 2),
        "selected class contains a non-involution");

# Compute the complete product-order matrix and all 210 unordered edge records.
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
Require(Length(edgeRecords) = 210, "did not construct all 210 edges");
colourValues := Set(edgeOrders);
edgeColourClasses := List(colourValues,
  c -> List(Filtered(edgeRecords, e -> e[4] = c), e -> e[3]));
edgeColourCounts := List(edgeColourClasses, Length);
Require(Sum(edgeColourCounts) = 210, "edge colour classes are incomplete");

# Full colour group by a coloured-incidence-graph automorphism oracle.
# Vertex colour class 1 is D; subsequent classes are edge-vertices partitioned
# by their exact product order.  This is structurally different from extending a
# partial permutation of D by edge compatibility.
incidenceGraph := EdgeOrbitsGraph(Group(()), incidenceArcs, edgeVertex);
vertexColourClasses := Concatenation([[1..n]], edgeColourClasses);
incidenceAut := AutGroupGraph(incidenceGraph,
                              ShallowCopy(vertexColourClasses));
colourRestrictions := Set(Elements(incidenceAut),
  g -> List([1..n], i -> i^g));
Require(Length(colourRestrictions) = Size(incidenceAut),
        "incidence automorphism has a nontrivial kernel on D");
Require(ForAll(colourRestrictions, p ->
  ForAll([1..n-1], i -> ForAll([i+1..n], j ->
    productOrderMatrix[i][j] = productOrderMatrix[p[i]][p[j]]))),
  "incidence restriction failed a direct colour check");

# Independently compute every abstract automorphism and its restriction to D.
autL := AutomorphismGroup(L);
autLElements := Elements(autL);
setwiseStabilizer := Filtered(autLElements, a ->
  Set(List(D, x -> Image(a, x))) = Set(D));
autRestrictions := Set(setwiseStabilizer, a ->
  List(D, x -> Position(D, Image(a, x))));
Require(not (fail in Flat(autRestrictions)),
        "an automorphism image left the indexed involution class");
Require(ForAll(autRestrictions, p ->
  ForAll([1..n-1], i -> ForAll([i+1..n], j ->
    productOrderMatrix[i][j] = productOrderMatrix[p[i]][p[j]]))),
  "an automorphism restriction failed the colour check");

groupsEqual := colourRestrictions = autRestrictions;
colourOnly := Difference(colourRestrictions, autRestrictions);
autOnly := Difference(autRestrictions, colourRestrictions);

# Full finite transcript: the matrix and both complete, canonically sorted sets
# make equality auditable rather than inferred from equal orders.
Print("VALIDATOR_PSL27_INDEPENDENT_V1\n");
Print("gap_version=", GAPInfo.Version, "\n");
Print("grape_version=", PackageInfo("grape")[1].Version, "\n");
Print("sl_order=", Size(S), "\n");
Print("centre_order=", Size(Z), "\n");
Print("quotient_order=", Size(L), "\n");
Print("quotient_nonabelian=", not IsAbelian(L), "\n");
Print("quotient_simple=", IsSimpleGroup(L), "\n");
Print("quotient_isomorphic_to_PSL_2_7=", quotientToStandard <> fail, "\n");
Print("involution_class_count=", Length(involutionClasses), "\n");
Print("involution_class_size=", n, "\n");
Print("unordered_edge_count=", Length(edgeRecords), "\n");
Print("colour_values=", colourValues, "\n");
Print("edge_colour_counts=", edgeColourCounts, "\n");
Print("product_order_matrix=", productOrderMatrix, "\n");
Print("incidence_graph_order=", incidenceGraph.order, "\n");
Print("incidence_aut_order=", Size(incidenceAut), "\n");
Print("colour_restriction_count=", Length(colourRestrictions), "\n");
Print("autL_order=", Size(autL), "\n");
Print("setwise_stabilizer_count=", Length(setwiseStabilizer), "\n");
Print("aut_restriction_count=", Length(autRestrictions), "\n");
Print("colour_restrictions=", colourRestrictions, "\n");
Print("aut_restrictions=", autRestrictions, "\n");
Print("groups_equal_as_permutation_sets=", groupsEqual, "\n");
Print("colour_only=", colourOnly, "\n");
Print("aut_only=", autOnly, "\n");

Require(groupsEqual, "the two restriction sets are not equal");
QUIT_GAP(0);
