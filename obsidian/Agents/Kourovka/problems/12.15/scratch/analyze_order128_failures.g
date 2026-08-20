ord := 128;
Print("GAP_VERSION=", GAPInfo.Version, " ORDER=", ord, "\n");
for id in [1..NumberSmallGroups(ord)] do
  G := SmallGroup(ord,id);
  D := DerivedSubgroup(G);
  if not IsAbelian(D) then
    reps := List(ConjugacyClasses(G), Representative);
    closures := List(reps, x -> NormalClosure(G, Subgroup(G,[x])));
    found := false;
    for i in [1..Length(reps)] do
      for j in [i+1..Length(reps)] do
        if not found and closures[i] = closures[j] then
          Print("ID=",id," DESC=",StructureDescription(G),
                " CLASS=",NilpotencyClassOfGroup(G),
                " D_ORDER=",Size(D)," D_DESC=",StructureDescription(D),
                " WITNESS_CLASS_INDEX=",i,",",j,
                " WITNESS_ORDERS=",Order(reps[i]),",",Order(reps[j]),
                " CLOSURE_ORDER=",Size(closures[i]),"\n");
          found := true;
        fi;
      od;
    od;
  fi;
od;
QUIT;
