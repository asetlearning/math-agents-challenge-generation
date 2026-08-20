Print("GAP_VERSION=", GAPInfo.Version, "\n");

HasSMPElementwise := function(G)
  local elts, closures, i, j;
  elts := Elements(G);
  closures := List(elts, x -> NormalClosure(G, Group([x], One(G))));
  for i in [1..Length(elts)] do
    for j in [i+1..Length(elts)] do
      if closures[i] = closures[j] and not IsConjugate(G, elts[i], elts[j]) then
        return false;
      fi;
    od;
  od;
  return true;
end;

for ord in [2,4,8,16,32,64,128] do
  total := NumberSmallGroups(ord);
  nonmeta := 0;
  passing := [];
  for id in [1..total] do
    G := SmallGroup(ord,id);
    if not IsAbelian(DerivedSubgroup(G)) then
      nonmeta := nonmeta + 1;
      if HasSMPElementwise(G) then Add(passing,id); fi;
    fi;
  od;
  Print("ORDER=",ord,
        " NUMBER_SMALL_GROUPS=",total,
        " NONMETABELIAN=",nonmeta,
        " COUNTEREXAMPLE_IDS=",passing,"\n");
od;
Print("RUN_COMPLETE=true\n");
QUIT;
