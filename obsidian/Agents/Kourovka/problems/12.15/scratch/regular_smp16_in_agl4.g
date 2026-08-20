# Existence screen forced by a C2-valued normal Lagrangian L=C2^4.
# Any bijective cocycle Q -> L is a regular affine embedding of the order-16
# SMP quotient Q in AGL(4,2).  Every 2-subgroup is conjugate into a fixed
# Sylow 2-subgroup, so its full subgroup lattice suffices for existence.

Lin:=GL(4,2);
Aff:=AffineActionByMatrixGroup(Lin);
Syl:=SylowSubgroup(Aff,2);
T:=Socle(Aff); tpcgs:=Pcgs(T); V4:=GF(2)^4;
Print("GAP_VERSION=",GAPInfo.Version,
      " AGL_ORDER=",Size(Aff)," SYLOW_ORDER=",Size(Syl),
      " TRANSLATION_SOCLE_ORDER=",Size(T),
      " DEGREE=",LargestMovedPoint(Aff),"\n");
allclasses:=ConjugacyClassesSubgroups(Syl);
ord16classes:=0; regularclasses:=0; regularids:=[];
targetcounts:=[0,0]; targetmodulepasses:=[0,0];
for cc in allclasses do
  U:=Representative(cc);
  if Size(U)=16 then
    ord16classes:=ord16classes+1;
    if IsTransitive(U,[1..16]) then
      regularclasses:=regularclasses+1;
      AddSet(regularids,IdGroup(U)[2]);
      if IdGroup(U)[2] in [11,12] then
        targetpos:=Position([11,12],IdGroup(U)[2]);
        targetcounts[targetpos]:=targetcounts[targetpos]+1;
        dualmats:=[];
        for u in GeneratorsOfGroup(U) do
          M:=List(tpcgs,t->ExponentsOfPcElement(tpcgs,t^u)*One(GF(2)));
          Add(dualmats,TransposedMat(M^-1));
        od;
        DualAct:=Group(dualmats);
        seenreps:=[]; seenmodules:=[]; modulesmp:=true;
        for v in Elements(V4) do
          if ForAll(seenreps,r->not v in Orbit(DualAct,r,
                function(x,g) return x*g; end)) then
            vorb:=Orbit(DualAct,v,function(x,g) return x*g; end);
            vmod:=VectorSpace(GF(2),vorb);
            if vmod in seenmodules then modulesmp:=false; break; fi;
            Add(seenreps,v); Add(seenmodules,vmod);
          fi;
        od;
        if modulesmp then
          targetmodulepasses[targetpos]:=targetmodulepasses[targetpos]+1;
        fi;
      fi;
    fi;
  fi;
od;
Print("ALL_SUBGROUP_CLASSES_IN_SYLOW=",Length(allclasses),
      " ORDER16_CLASSES=",ord16classes,
      " REGULAR_ORDER16_CLASSES=",regularclasses,
      " REGULAR_ORDER16_IDS=",regularids,
      " SMP_TARGET_IDS_PRESENT=",Intersection(regularids,[11,12]),"\n");
Print("TARGET_REGULAR_COUNTS_ID11_ID12=",targetcounts,
      " TARGET_RESTRICTED_SMP_PASSES_ID11_ID12=",targetmodulepasses,"\n");
QUIT;
