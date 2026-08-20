# Full-complex-character affine pairing screen for every abelian A of order 8.
# This correctly permits order-4 and order-8 scalar characters.  For each
# exact-SMP order-32 subgroup embedding left by the holomorph screen, find a
# nonidentity a in A that is alpha-regular, or record that the embedding passes
# this necessary nondegeneracy-on-A test.

targetids:=[27,43,49];
Print("GAP_VERSION=",GAPInfo.Version,"\n");
for aid in [1..NumberSmallGroups(8)] do
  A:=SmallGroup(8,aid);
  if IsAbelian(A) then
    ccs:=ConjugacyClasses(A); reps:=List(ccs,Representative);
    chars:=Irr(A); charvals:=List(chars,chi->List(chi)); n:=Length(chars);
    transperms:=[];
    for k in [1..n] do
      imgs:=[];
      for i in [1..n] do
        vals:=List([1..n],j->charvals[i][j]*charvals[k][j]);
        Add(imgs,Position(charvals,vals));
      od;
      Add(transperms,PermList(imgs));
    od;
    Trans:=Group(transperms);
    AutA:=AutomorphismGroup(A); autperms:=[];
    for aut in GeneratorsOfGroup(AutA) do
      imgs:=[]; autinv:=InverseGeneralMapping(aut);
      for i in [1..n] do
        vals:=List(reps,a->charvals[i][Position(reps,Image(autinv,a))]);
        Add(imgs,Position(charvals,vals));
      od;
      Add(autperms,PermList(imgs));
    od;
    Hol:=Group(Concatenation(GeneratorsOfGroup(Trans),autperms));
    casecount:=0;
    for cc in ConjugacyClassesSubgroups(Hol) do
      S:=Representative(cc);
      if Size(S)=32 and IdGroup(S)[2] in targetids then
        casecount:=casecount+1; regularwitness:=fail;
        for aidx in [2..n] do
          isregular:=true;
          for s in Elements(S) do
            lambdaidx:=1^s;
            lin:=s*transperms[lambdaidx]^-1;
            fixes:=ForAll([1..n],i->
              charvals[i^lin][aidx]=charvals[i][aidx]);
            if fixes and charvals[lambdaidx][aidx]<>1 then
              isregular:=false; break;
            fi;
          od;
          if isregular then regularwitness:=reps[aidx]; break; fi;
        od;
        Print("A_ID=",aid," A_STRUCTURE=",StructureDescription(A),
              " CASE=",casecount," Q_ID=",IdGroup(S)[2],
              " INTERSECTION_FULL_DUAL_ORDER=",Size(Intersection(S,Trans)),
              " ALPHA_REGULAR_A_REP=",regularwitness,
              " PASSES_A_NONDEGENERACY=",regularwitness=fail,"\n");
      fi;
    od;
    Print("A_ID=",aid," HOL_ORDER=",Size(Hol),
          " TARGET_EMBEDDING_CLASSES=",casecount,"\n");
  fi;
od;
QUIT;
