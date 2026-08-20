# Necessary action test for extending the guaranteed normal isotropic subgroup
# A of order 8 to a normal Lagrangian.  If H/A acts faithfully on C[A], then
# H/A embeds in A^* semidirect Aut(A), abstractly Hol(A).

smpids := [27,34,35,43,44,46,47,49,50,51];
Print("GAP_VERSION=",GAPInfo.Version," SMP32_IDS=",smpids,"\n");
for aid in [1..NumberSmallGroups(8)] do
  A := SmallGroup(8,aid);
  if IsAbelian(A) then
    AutA := AutomorphismGroup(A);
    Hol := SemidirectProduct(AutA,A);
    subids := [];
    for cc in ConjugacyClassesSubgroups(Hol) do
      S := Representative(cc);
      if Size(S)=32 then AddSet(subids,IdGroup(S)[2]); fi;
    od;
    Print("A_ID=",aid," A_STRUCTURE=",StructureDescription(A),
          " HOL_ORDER=",Size(Hol),
          " ORDER32_SUBGROUP_IDS=",subids,
          " SMP32_EMBEDDABLE_IDS=",Intersection(subids,smpids),"\n");
  fi;
od;
QUIT;
