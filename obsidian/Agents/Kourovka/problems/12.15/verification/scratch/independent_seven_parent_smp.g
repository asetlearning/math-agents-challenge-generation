HasSMPByClasses := function(G)
  local reps, closures, i, j;
  reps := List(ConjugacyClasses(G),Representative);
  closures := List(reps,x -> NormalClosure(G,Subgroup(G,[x])));
  for i in [1..Length(reps)] do
    for j in [i+1..Length(reps)] do
      if closures[i]=closures[j] then return false; fi;
    od;
  od;
  return true;
end;

Print("GAP_VERSION=",GAPInfo.Version,"\n");
for id in [53342,53343,53355,53356,53357,53358,53359] do
  H := SmallGroup(256,id);
  p := Pcgs(H);
  f8 := p[Length(p)];
  Print("BASE=[256,",id,"] EXACT_SMP=",HasSMPByClasses(H),
        " F8=",f8,
        " F8_PC_EXPONENTS=",ExponentsOfPcElement(p,f8),
        " F8_CENTRAL=",f8 in Centre(H),"\n");
od;
Print("RUN_COMPLETE=true\n");
QUIT;
