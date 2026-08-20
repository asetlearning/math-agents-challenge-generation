# Sharpen Proposition 3.2 for a C2-valued cocycle.  Scalar twists arising
# from lift commutators lie in Hom(A,C2), dual to A/Phi(A), rather than in
# the full complex character group.  A faithful exceptional quotient H/A
# must embed in Hom(A,C2) semidirect Aut(A).

smpids := [27,34,35,43,44,46,47,49,50,51];
Print("GAP_VERSION=",GAPInfo.Version," SMP32_IDS=",smpids,"\n");
for aid in [1..NumberSmallGroups(8)] do
  A := SmallGroup(8,aid);
  if IsAbelian(A) then
    AutA := AutomorphismGroup(A);
    epi := NaturalHomomorphismByNormalSubgroup(A,FrattiniSubgroup(A));
    V := Image(epi,A);
    autgens := GeneratorsOfGroup(AutA);
    indgens := List(autgens,a->InducedAutomorphism(epi,a));
    IndAut := Group(indgens);
    acthom := GroupHomomorphismByImages(AutA,IndAut,autgens,indgens);
    P := SemidirectProduct(AutA,acthom,V);
    subids := [];
    for cc in ConjugacyClassesSubgroups(P) do
      S := Representative(cc);
      if Size(S)=32 then AddSet(subids,IdGroup(S)[2]); fi;
    od;
    Print("A_ID=",aid," A_STRUCTURE=",StructureDescription(A),
          " HOM_A_C2_ORDER=",Size(V),
          " AUT_ORDER=",Size(AutA),
          " C2_TWIST_ACTION_GROUP_ORDER=",Size(P),
          " ORDER32_SUBGROUP_IDS=",subids,
          " SMP32_EMBEDDABLE_IDS=",Intersection(subids,smpids),"\n");
  fi;
od;
QUIT;
