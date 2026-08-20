# Frozen exact checker for Kourovka 21.53, fixed M11 counterexample lane.
# Canonical constraints explicitly checked or implemented:
# 21.53-forall-L-D
# 21.53-L-finite-nonabelian-simple
# 21.53-D-single-involution-class
# 21.53-Gamma-product-order-colouring
# 21.53-Aut-t-definition
# 21.53-two-minimal-primes
# 21.53-full-colour-group-definition
# 21.53-two-colours-determine-all

M11Assert := function(condition, message)
  if not condition then
    Error(Concatenation("ASSERTION_FAILED: ", message));
  fi;
end;

M11Assert(LoadPackage("grape") = true, "GRAPE package failed to load");

M11RestrictToClass := function(rawGroup, n)
  local restrictedGenerators, g, images;
  restrictedGenerators := [];
  for g in GeneratorsOfGroup(rawGroup) do
    images := List([1..n], i -> i^g);
    M11Assert(Set(images) = [1..n],
      "incidence automorphism does not preserve the class-vertex cell");
    Add(restrictedGenerators, PermList(images));
  od;
  if Length(restrictedGenerators) = 0 then
    return Group(());
  fi;
  return Group(restrictedGenerators);
end;

M11BuildIncidenceGraph := function(n, pairRecords, wantedColours)
  local directedEdges, colourCells, nextVertex, colour, records,
        record, incidenceVertex, graph;
  directedEdges := [];
  colourCells := [[1..n]];
  nextVertex := n;
  for colour in wantedColours do
    records := Filtered(pairRecords, record -> record[3] = colour);
    if Length(records) > 0 then
      Add(colourCells,
        [nextVertex + 1..nextVertex + Length(records)]);
      for record in records do
        nextVertex := nextVertex + 1;
        incidenceVertex := nextVertex;
        Add(directedEdges, [record[1], incidenceVertex]);
        Add(directedEdges, [incidenceVertex, record[1]]);
        Add(directedEdges, [record[2], incidenceVertex]);
        Add(directedEdges, [incidenceVertex, record[2]]);
      od;
    fi;
  od;
  graph := EdgeOrbitsGraph(Group(()), directedEdges, nextVertex);
  M11Assert(IsSimpleGraph(graph), "incidence graph is not simple");
  M11Assert(Union(colourCells) = [1..nextVertex],
    "vertex-colour cells do not partition the incidence graph");
  return rec(
    graph := graph,
    colourCells := colourCells,
    order := nextVertex,
    undirectedEdgeCount := Length(directedEdges) / 2
  );
end;

M11AuditRelationGroup := function(group, matrix, wantedColours)
  local n, failures, g, i, j;
  n := Length(matrix);
  failures := 0;
  for g in GeneratorsOfGroup(group) do
    for i in [1..n-1] do
      for j in [i+1..n] do
        if matrix[i][j] in wantedColours and
           matrix[i^g][j^g] <> matrix[i][j] then
          failures := failures + 1;
        fi;
      od;
    od;
  od;
  return failures;
end;

M11FindChangedEdge := function(permutation, matrix)
  local n, i, j;
  n := Length(matrix);
  for i in [1..n-1] do
    for j in [i+1..n] do
      if matrix[i][j] <> matrix[i^permutation][j^permutation] then
        return [i, j, matrix[i][j], i^permutation, j^permutation,
                matrix[i^permutation][j^permutation]];
      fi;
    od;
  od;
  return fail;
end;

Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("GRAPE_VERSION=", PackageInfo("grape")[1].Version, "\n");

# Define the standard degree-11 permutation model directly by its two generators.
L := Group(
  (1,2,3,4,5,6,7,8,9,10,11),
  (3,7,11,8)(4,10,5,6)
);
M11Assert(IsFinite(L), "the explicit permutation group is not finite");
M11Assert(not IsAbelian(L), "the explicit permutation group is abelian");
M11Assert(Size(L) = 7920, "the explicit group order is not 7920");
M11Assert(IsSimpleGroup(L), "the explicit group is not simple");
M11Assert(MovedPoints(L) = [1..11], "the natural moved-point domain is not 1..11");
sharpFourOrbit := Orbit(L, [1,2,3,4], OnTuples);
M11Assert(Length(sharpFourOrbit) = 11*10*9*8,
  "the degree-11 action is not sharply 4-transitive");
simpleType := IsomorphismTypeInfoFiniteSimpleGroup(L);
M11Assert(simpleType <> fail and simpleType.shortname = "M11",
  "finite-simple-group identification is not M11");
M11Assert(Size(Center(L)) = 1, "M11 centre is not trivial");

Print("GROUP_GENERATORS=", GeneratorsOfGroup(L), "\n");
Print("GROUP_ORDER=", Size(L), "\n");
Print("GROUP_IS_FINITE=", IsFinite(L), "\n");
Print("GROUP_IS_ABELIAN=", IsAbelian(L), "\n");
Print("GROUP_IS_SIMPLE=", IsSimpleGroup(L), "\n");
Print("GROUP_SIMPLE_TYPE=", simpleType, "\n");
Print("NATURAL_DEGREE=", Length(MovedPoints(L)), "\n");
Print("ORDERED_4_TUPLE_ORBIT_SIZE=", Length(sharpFourOrbit), "\n");

primeDivisors := Set(FactorsInt(Size(L)));
M11Assert(Length(primeDivisors) >= 2 and primeDivisors[1] = 2,
  "group order does not have two distinct prime divisors beginning with 2");
p := primeDivisors[2];
M11Assert(p = 3, "the second-smallest distinct prime divisor is not 3");
Print("PRIME_DIVISORS=", primeDivisors, "\n");
Print("SECOND_SMALLEST_PRIME=", p, "\n");

allClasses := ConjugacyClasses(L);
involutionClasses := Filtered(allClasses,
  class -> Order(Representative(class)) = 2);
M11Assert(Length(involutionClasses) = 1,
  "M11 does not have exactly one involution conjugacy class");
D := ShallowCopy(AsList(involutionClasses[1]));
Sort(D);
allInvolutions := Filtered(Elements(L), element -> Order(element) = 2);
M11Assert(Set(D) = Set(allInvolutions),
  "selected class is not the complete set of nonidentity involutions");
M11Assert(ForAll(D, element -> Order(element) = 2),
  "selected class contains a non-involution");
M11Assert(Set(Orbit(L, D[1], OnPoints)) = Set(D),
  "selected set is not one full conjugacy orbit");
M11Assert(Length(D) = 165, "selected involution class does not have size 165");
M11Assert(Size(Centralizer(L, D[1])) = 48,
  "selected involution centralizer does not have order 48");
n := Length(D);
Print("TOTAL_CONJUGACY_CLASSES=", Length(allClasses), "\n");
Print("INVOLUTION_CLASS_COUNT=", Length(involutionClasses), "\n");
Print("INVOLUTION_CLASS_REPRESENTATIVE=", D[1], "\n");
Print("INVOLUTION_CLASS_SIZE=", n, "\n");
Print("INVOLUTION_CENTRALIZER_ORDER=", Size(Centralizer(L,D[1])), "\n");
for i in [1..n] do
  Print("VERTEX_", i, "=", D[i], "\n");
od;

# Complete exact product-order colouring on all unordered distinct pairs.
matrix := List([1..n], i -> ListWithIdenticalEntries(n, 1));
pairRecords := [];
for i in [1..n-1] do
  for j in [i+1..n] do
    productOrder := Order(D[i] * D[j]);
    matrix[i][j] := productOrder;
    matrix[j][i] := productOrder;
    Add(pairRecords, [i, j, productOrder]);
  od;
od;
M11Assert(Length(pairRecords) = n*(n-1)/2,
  "complete unordered-pair enumeration has the wrong size");
colours := Set(List(pairRecords, record -> record[3]));
edgeCounts := List(colours,
  colour -> Number(pairRecords, record -> record[3] = colour));
valencies := List(colours,
  colour -> Number([2..n], j -> matrix[1][j] = colour));
for colour in colours do
  expectedValency := Number([2..n], j -> matrix[1][j] = colour);
  M11Assert(ForAll([1..n], i ->
    Number(Filtered([1..n], j -> j <> i),
      j -> matrix[i][j] = colour) = expectedValency),
    Concatenation("colour relation is not regular for colour ", String(colour)));
od;
M11Assert(Sum(edgeCounts) = n*(n-1)/2,
  "colour edge counts do not cover the complete graph");
Print("UNORDERED_PAIR_COUNT=", Length(pairRecords), "\n");
Print("PRODUCT_ORDER_COLOURS=", colours, "\n");
Print("PRODUCT_ORDER_EDGE_COUNTS=", edgeCounts, "\n");
Print("PRODUCT_ORDER_VALENCIES=", valencies, "\n");
for i in [1..n] do
  Print("MATRIX_ROW_", i, "=",
    JoinStringsWithSeparator(List(matrix[i], String), ","), "\n");
od;

otherColours := Difference(colours, [2,p]);
if Length(otherColours) = 0 then
  Print("TAUTOLOGY_GATE=STOP_ONLY_MINIMAL_PRIME_COLOURS_OCCUR\n");
  Print("COMPARISON=TAUTOLOGICAL_EQUALITY\n");
else
  Print("TAUTOLOGY_GATE=PASS_OTHER_COLOURS_OCCUR\n");
  Print("OTHER_OCCURRING_COLOURS=", otherColours, "\n");

  twoData := M11BuildIncidenceGraph(n, pairRecords, [2,p]);
  Print("TWO_COLOUR_INCIDENCE_ORDER=", twoData.order, "\n");
  Print("TWO_COLOUR_INCIDENCE_EDGES=", twoData.undirectedEdgeCount, "\n");
  twoRaw := AutGroupGraph(twoData.graph, twoData.colourCells);
  twoGroup := M11RestrictToClass(twoRaw, n);
  M11Assert(Size(twoRaw) = Size(twoGroup),
    "two-colour incidence action is not faithful on the class vertices");
  twoAuditFailures := M11AuditRelationGroup(twoGroup, matrix, [2,p]);
  M11Assert(twoAuditFailures = 0,
    "a returned two-colour generator fails an exact selected relation");

  fullData := M11BuildIncidenceGraph(n, pairRecords, colours);
  Print("FULL_COLOUR_INCIDENCE_ORDER=", fullData.order, "\n");
  Print("FULL_COLOUR_INCIDENCE_EDGES=", fullData.undirectedEdgeCount, "\n");
  fullRaw := AutGroupGraph(fullData.graph, fullData.colourCells);
  fullGroup := M11RestrictToClass(fullRaw, n);
  M11Assert(Size(fullRaw) = Size(fullGroup),
    "full-colour incidence action is not faithful on the class vertices");
  fullAuditFailures := M11AuditRelationGroup(fullGroup, matrix, colours);
  M11Assert(fullAuditFailures = 0,
    "a returned full-colour generator changes an exact colour");

  naturalConjugationGroup := Action(L, D, OnPoints);
  M11Assert(Size(naturalConjugationGroup) = Size(L),
    "natural conjugation action is not faithful");
  naturalInFull := IsSubgroup(fullGroup, naturalConjugationGroup);
  M11Assert(naturalInFull,
    "natural M11 conjugation action is not contained in the full colour group");

  fullInTwo := IsSubgroup(twoGroup, fullGroup);
  M11Assert(fullInTwo,
    "the computed full-colour group is not contained in the two-colour group");
  twoInFull := IsSubgroup(fullGroup, twoGroup);

  Print("TWO_COLOUR_RAW_ORDER=", Size(twoRaw), "\n");
  Print("TWO_COLOUR_RESTRICTED_ORDER=", Size(twoGroup), "\n");
  Print("TWO_COLOUR_GENERATOR_COUNT=", Length(GeneratorsOfGroup(twoGroup)), "\n");
  Print("TWO_COLOUR_AUDIT_FAILURES=", twoAuditFailures, "\n");
  Print("FULL_COLOUR_RAW_ORDER=", Size(fullRaw), "\n");
  Print("FULL_COLOUR_RESTRICTED_ORDER=", Size(fullGroup), "\n");
  Print("FULL_COLOUR_GENERATOR_COUNT=", Length(GeneratorsOfGroup(fullGroup)), "\n");
  Print("FULL_COLOUR_AUDIT_FAILURES=", fullAuditFailures, "\n");
  Print("NATURAL_CONJUGATION_GROUP_ORDER=", Size(naturalConjugationGroup), "\n");
  Print("NATURAL_GROUP_IN_FULL=", naturalInFull, "\n");
  Print("FULL_GROUP_IN_TWO_COLOUR_GROUP=", fullInTwo, "\n");
  Print("TWO_COLOUR_GROUP_IN_FULL_GROUP=", twoInFull, "\n");

  if twoInFull then
    M11Assert(Size(twoGroup) = Size(fullGroup),
      "mutual containment did not produce equal group orders");
    M11Assert(M11AuditRelationGroup(twoGroup, matrix, colours) = 0,
      "equal two-colour group has a generator changing another colour");
    Print("COMPARISON=EQUALITY\n");
  else
    M11Assert(Size(twoGroup) > Size(fullGroup),
      "strict containment did not produce a larger two-colour group");
    separator := First(GeneratorsOfGroup(twoGroup),
      generator -> not generator in fullGroup);
    M11Assert(separator <> fail,
      "strict containment has no displayed generator outside the full group");
    M11Assert(M11AuditRelationGroup(Group(separator), matrix, [2,p]) = 0,
      "displayed separator changes a minimal-prime relation");
    changedEdge := M11FindChangedEdge(separator, matrix);
    M11Assert(changedEdge <> fail,
      "displayed separator does not change any exact product-order colour");
    M11Assert(not (changedEdge[3] in [2,p]),
      "displayed changed edge has a minimal-prime source colour");
    Print("SEPARATOR_CYCLES=", separator, "\n");
    Print("SEPARATOR_IMAGE_LIST=", List([1..n], i -> i^separator), "\n");
    Print("SEPARATOR_SELECTED_RELATION_FAILURES=0\n");
    Print("SEPARATOR_CHANGED_EDGE=", changedEdge, "\n");
    Print("COMPARISON=STRICT\n");
  fi;
fi;

Print("FINAL_SUCCESS_SENTINEL=M11_TWO_COLOUR_CHECK_V2_PASS\n");

