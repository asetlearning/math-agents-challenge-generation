# Independent elementwise verifier for the 14 nonmetabelian groups of order
# 128.  Unlike search_smallgroups.g, this checks every element pair rather
# than only conjugacy-class representatives.

ord := 128;
nonmetaids := [];
Print("GAP_VERSION=", GAPInfo.Version, " ORDER=", ord, "\n");
for id in [1..NumberSmallGroups(ord)] do
  G := SmallGroup(ord, id);
  if not IsAbelian(DerivedSubgroup(G)) then
    Add(nonmetaids, id);
    els := Elements(G);
    closures := List(els, x -> NormalClosure(G, Subgroup(G, [x])));
    found := false;
    for i in [1..Length(els)-1] do
      for j in [i+1..Length(els)] do
        if not found and closures[i] = closures[j]
           and not IsConjugate(G, els[i], els[j]) then
          Print("REJECT_ID=", id, " ELEMENT_POSITIONS=", i, ",", j,
                " ORDERS=", Order(els[i]), ",", Order(els[j]),
                " CLOSURE_ORDER=", Size(closures[i]), "\n");
          found := true;
        fi;
      od;
    od;
    if not found then
      Print("UNREJECTED_NONMETABELIAN_ID=", id, "\n");
    fi;
  fi;
od;
Print("NONMETABELIAN_IDS=", nonmetaids, "\n");
QUIT;
