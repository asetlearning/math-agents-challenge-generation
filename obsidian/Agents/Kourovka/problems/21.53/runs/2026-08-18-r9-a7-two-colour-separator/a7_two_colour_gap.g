LoadPackage("grape");

if not IsBound(AutGroupGraph) then
  Error("GRAPE/AutGroupGraph is unavailable");
fi;

G := AlternatingGroup(7);
S := SymmetricGroup(7);
rep := (1,2)(3,4);
D := ShallowCopy(AsList(ConjugacyClass(G, rep)));
Sort(D);
n := Length(D);

if Size(G) <> 2520 then Error("wrong A7 order"); fi;
if not IsSimpleGroup(G) then Error("A7 simplicity check failed"); fi;
if n <> 105 then Error("wrong double-transposition class size"); fi;
if not ForAll(D, x -> Order(x) = 2) then Error("class contains non-involution"); fi;

allinvolutions := Filtered(Elements(G), x -> x <> One(G) and Order(x) = 2);
if Set(allinvolutions) <> Set(D) then
  Error("double transpositions are not the unique involution class");
fi;

matrix := List([1..n], i -> List([1..n], j -> 0));
edgesByOrder := List([1..20], t -> []);
for i in [1..n] do
  matrix[i][i] := 1;
od;
for i in [1..n-1] do
  for j in [i+1..n] do
    t := Order(D[i] * D[j]);
    if t > Length(edgesByOrder) then Error("unexpected product order"); fi;
    matrix[i][j] := t;
    matrix[j][i] := t;
    Add(edgesByOrder[t], [i,j]);
  od;
od;
colours := Filtered([1..Length(edgesByOrder)], t -> Length(edgesByOrder[t]) > 0);

MakeIncidenceGadget := function(edgeSets)
  local total, gamma, classes, offset, edges, nodes, k, node, e, u, v;
  total := n + Sum(edgeSets, Length);
  gamma := NullGraph(Group(()), total);
  classes := [[1..n]];
  offset := n;
  for edges in edgeSets do
    nodes := [offset+1..offset+Length(edges)];
    Add(classes, nodes);
    for k in [1..Length(edges)] do
      node := offset + k;
      e := edges[k];
      u := e[1];
      v := e[2];
      Add(gamma.adjacencies[u], node);
      Add(gamma.adjacencies[v], node);
      gamma.adjacencies[node] := [u,v];
    od;
    offset := offset + Length(edges);
  od;
  return rec(graph := gamma, colourClasses := classes);
end;

CheckRelation := function(g, t)
  local checked, failures, i, j;
  checked := 0;
  failures := 0;
  for i in [1..n-1] do
    for j in [i+1..n] do
      if matrix[i][j] = t then
        checked := checked + 1;
        if matrix[i^g][j^g] <> t then
          failures := failures + 1;
        fi;
      fi;
    od;
  od;
  return [checked, failures];
end;

PreservesAllColours := function(g)
  local i, j;
  for i in [1..n-1] do
    for j in [i+1..n] do
      if matrix[i][j] <> matrix[i^g][j^g] then
        return false;
      fi;
    od;
  od;
  return true;
end;

FirstChangedEdge := function(g)
  local i, j;
  for i in [1..n-1] do
    for j in [i+1..n] do
      if matrix[i][j] <> matrix[i^g][j^g] then
        return [i,j,i^g,j^g,matrix[i][j],matrix[i^g][j^g]];
      fi;
    od;
  od;
  return fail;
end;

NaturalActionGenerator := function(g)
  local images, x, pos;
  images := [];
  for x in D do
    pos := Position(D, x^g);
    if pos = fail then Error("S7 failed to normalize D"); fi;
    Add(images, pos);
  od;
  return PermList(images);
end;

Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("GRAPE_VERSION=", InstalledPackageVersion("grape"), "\n");
Print("GROUP=A7 natural degree 7\n");
Print("GROUP_ORDER=", Size(G), "\n");
Print("GROUP_ORDER_FACTORS=", FactorsInt(Size(G)), "\n");
Print("IS_SIMPLE=", IsSimpleGroup(G), "\n");
Print("INVOLUTION_CLASS_REP=", rep, "\n");
Print("INVOLUTION_CLASS_SIZE=", n, "\n");
Print("ALL_NONIDENTITY_INVOLUTIONS_SIZE=", Length(allinvolutions), "\n");
Print("UNIQUE_INVOLUTION_CLASS_CHECK=PASS\n");
Print("SECOND_SMALLEST_DISTINCT_PRIME=3\n");
Print("COLOURS=", colours, "\n");
Print("COLOUR_EDGE_COUNTS=", List(colours, t -> [t,Length(edgesByOrder[t])]), "\n");

twoGadget := MakeIncidenceGadget([edgesByOrder[2], edgesByOrder[3]]);
Print("TWO_GADGET_ORDER=", twoGadget.graph.order, "\n");
twoBig := AutGroupGraph(twoGadget.graph, twoGadget.colourClasses);
twoSmall := Action(twoBig, [1..n], OnPoints);
Print("TWO_BIG_ORDER=", Size(twoBig), "\n");
Print("TWO_COLOUR_GROUP_ORDER=", Size(twoSmall), "\n");
Print("TWO_RESTRICTION_KERNEL_TRIVIAL=", Size(twoBig)=Size(twoSmall), "\n");

fullGadget := MakeIncidenceGadget(List(colours, t -> edgesByOrder[t]));
Print("FULL_GADGET_ORDER=", fullGadget.graph.order, "\n");
fullBig := AutGroupGraph(fullGadget.graph, fullGadget.colourClasses);
fullSmall := Action(fullBig, [1..n], OnPoints);
Print("FULL_BIG_ORDER=", Size(fullBig), "\n");
Print("FULL_COLOUR_GROUP_ORDER=", Size(fullSmall), "\n");
Print("FULL_RESTRICTION_KERNEL_TRIVIAL=", Size(fullBig)=Size(fullSmall), "\n");
Print("FULL_SUBGROUP_OF_TWO=", IsSubgroup(twoSmall, fullSmall), "\n");

naturalGenerators := List(GeneratorsOfGroup(S), NaturalActionGenerator);
naturalS7 := Group(naturalGenerators);
Print("NATURAL_S7_ACTION_ORDER=", Size(naturalS7), "\n");
Print("NATURAL_S7_SUBGROUP_OF_FULL=", IsSubgroup(fullSmall, naturalS7), "\n");

twoGeneratorAudit := List(GeneratorsOfGroup(twoSmall),
                          g -> [CheckRelation(g,2), CheckRelation(g,3)]);
fullGeneratorAudit := List(GeneratorsOfGroup(fullSmall), PreservesAllColours);
Print("TWO_GENERATOR_RELATION_AUDIT=", twoGeneratorAudit, "\n");
Print("FULL_GENERATOR_ALL_COLOURS_AUDIT=", fullGeneratorAudit, "\n");

if Size(twoSmall) = Size(fullSmall) and IsSubgroup(twoSmall, fullSmall) then
  Print("COMPARISON=EQUALITY\n");
else
  separator := First(GeneratorsOfGroup(twoSmall), g -> not g in fullSmall);
  if separator = fail then Error("strict orders but no separator generator"); fi;
  changed := FirstChangedEdge(separator);
  if changed = fail then Error("separator has no changed colour"); fi;
  Print("COMPARISON=STRICT\n");
  Print("SEPARATOR_CYCLES=", separator, "\n");
  Print("SEPARATOR_IMAGES=", List([1..n], i -> i^separator), "\n");
  Print("SEPARATOR_R2_AUDIT=", CheckRelation(separator,2), "\n");
  Print("SEPARATOR_R3_AUDIT=", CheckRelation(separator,3), "\n");
  Print("CHANGED_EDGE=", changed, "\n");
  Print("CHANGED_EDGE_OBJECTS=", [D[changed[1]],D[changed[2]],
                                   D[changed[3]],D[changed[4]]], "\n");
fi;

Print("VERTEX_TABLE_BEGIN\n");
for i in [1..n] do
  Print(i, ":", D[i], "\n");
od;
Print("VERTEX_TABLE_END\n");
Print("CHECKER_STATUS=PASS\n");
Print("FINAL_SUCCESS_SENTINEL=A7_TWO_COLOUR_CHECK_V4_PASS\n");
QUIT_GAP(0);
