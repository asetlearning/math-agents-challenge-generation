# Exact SMP catalogue through order 128, restricted in output to class >= 3.
# This is new coverage: the earlier order-128 screen tested only groups with
# nonabelian derived subgroup.

HasSMPExactSmall := function(G)
  local closures, cc, x, N;
  closures := [];
  for cc in ConjugacyClasses(G) do
    x := Representative(cc);
    N := NormalClosure(G,Subgroup(G,[x]));
    if N in closures then return false; fi;
    Add(closures,N);
  od;
  return true;
end;

PassesRationalSmall := function(G)
  local cc,x,ox;
  for cc in ConjugacyClasses(G) do
    x:=Representative(cc); ox:=Order(x);
    if not IsConjugate(G,x,x^-1) then return false; fi;
    if ox>=8 and not IsConjugate(G,x,x^3) then return false; fi;
  od;
  return true;
end;

Print("GAP_VERSION=",GAPInfo.Version,"\n");
for ordsmall in [1,2,4,8,16,32,64,128] do
  smpcount:=0; highclass:=[];
  for idsmall in [1..NumberSmallGroups(ordsmall)] do
    smallg:=SmallGroup(ordsmall,idsmall);
    if PassesRationalSmall(smallg) and HasSMPExactSmall(smallg) then
      smpcount:=smpcount+1;
      if NilpotencyClassOfGroup(smallg)>=3 then
        Add(highclass,idsmall);
        Print("ORDER=",ordsmall," SMP_CLASS_GE3_ID=",idsmall,
              " CLASS=",NilpotencyClassOfGroup(smallg),
              " ABINV=",AbelianInvariants(smallg/DerivedSubgroup(smallg)),
              " DERIVED_INV=",AbelianInvariants(DerivedSubgroup(smallg)),
              " CENTER_INV=",AbelianInvariants(Centre(smallg)),"\n");
      fi;
    fi;
  od;
  Print("ORDER=",ordsmall," SMP_COUNT=",smpcount,
        " CLASS_GE3_COUNT=",Length(highclass),
        " CLASS_GE3_IDS=",highclass,"\n");
od;
QUIT;
