# Full-complex-dual existence screen for the valid normal-Lagrangian branch.
# For each non-elementary abelian L of order 16, enumerate regular affine
# subgroups of Hol(L^*) (abstractly Hol(L)) isomorphic to the two exact-SMP
# quotient types SmallGroup(16,11) and SmallGroup(16,12).

Print("GAP_VERSION=",GAPInfo.Version,"\n");
if not IsBound(lidtargets) then lidtargets:=[1..NumberSmallGroups(16)]; fi;
for lid in lidtargets do
  L:=SmallGroup(16,lid);
  if IsAbelian(L) and not IsElementaryAbelian(L) then
    elts:=Elements(L);
    Trans:=Action(L,elts,OnRight);
    AutL:=AutomorphismGroup(L);
    AutPerm:=Action(AutL,elts,function(x,a) return Image(a,x); end);
    Hol:=Group(Concatenation(GeneratorsOfGroup(Trans),
                             GeneratorsOfGroup(AutPerm)));
    Syl:=SylowSubgroup(Hol,2);
    classes:=ConjugacyClassesSubgroups(Syl);
    targetcounts:=[0,0]; regularcount:=0;
    for cc in classes do
      U:=Representative(cc);
      if Size(U)=16 and IsTransitive(U,[1..16]) then
        regularcount:=regularcount+1;
        uid:=IdGroup(U)[2];
        if uid in [11,12] then
          p:=Position([11,12],uid);
          targetcounts[p]:=targetcounts[p]+1;
        fi;
      fi;
    od;
    Print("L_ID=",lid," L_STRUCTURE=",StructureDescription(L),
          " AUT_ORDER=",Size(AutL)," HOL_ORDER=",Size(Hol),
          " SYLOW_ORDER=",Size(Syl),
          " SYLOW_SUBGROUP_CLASSES=",Length(classes),
          " REGULAR_ORDER16_CLASSES=",regularcount,
          " TARGET_REGULAR_COUNTS_ID11_ID12=",targetcounts,"\n");
  fi;
od;
QUIT;
