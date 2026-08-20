# Exact bounded parent screen for the sole restricted-SMP-surviving regular
# affine action in the normal-Lagrangian type L=C8xC2, Q=[16,11].
# It enumerates the full 512-class H^2(Q,L) superset unless classlimitlag is set.

if IsBound(lagusecompatible) and lagusecompatible=true then
  Read("Agents/Kourovka/problems/12.15/scratch/pilot_lagrangian_c8c2_q11_case3_compatible_orbits.g");
else
  lagcasetargets:=[3];
  Read("Agents/Kourovka/problems/12.15/scratch/pilot_lagrangian_c8c2_q11_actions_cohomology.g");
fi;
lagrec:=lagrecords[1];

TailVectorC8C2Lag := function(v,C)
  local coords,out,i,j,s8,s2;
  coords:=List(leltslag,x->CoordC8C2Lag(x,l8lag,l2lag)); out:=[];
  for i in [1..Length(C.enumrels)] do
    s8:=0; s2:=0;
    for j in [1..Length(leltslag)] do
      s8:=s8+coords[j][1]*v[(i-1)*Length(leltslag)+j];
      s2:=s2+coords[j][2]*v[(i-1)*Length(leltslag)+j];
    od;
    Add(out,[s8 mod 8,s2 mod 2]);
  od;
  return out;
end;

ExtensionC8C2Lag := function(C,tails,actcoords)
  local n,coll,rels,i,e,r,o,x,G;
  n:=Length(C.mats); coll:=FromTheLeftCollector(n+2);
  rels:=RelativeOrdersOfPcp(C.factor);
  for i in [1..Length(C.enumrels)] do
    e:=C.enumrels[i]; r:=VectorOfWordCR(C.relators[e[1]][e[2]],n);
    Append(r,tails[i]); o:=ObjByExponents(coll,r);
    if e[1]=e[2] then
      SetRelativeOrder(coll,e[1],rels[e[1]]); SetPower(coll,e[1],o);
    elif e[1]>e[2] then
      SetConjugate(coll,e[1],e[2],o);
    else
      SetConjugate(coll,e[1],-e[2]+e[1],o);
    fi;
  od;
  SetRelativeOrder(coll,n+1,8); SetRelativeOrder(coll,n+2,2);
  for i in [1..n] do
    x:=Concatenation(List([1..n],j->0),actcoords[i][1]);
    SetConjugate(coll,n+1,i,ObjByExponents(coll,x));
    x:=Concatenation(List([1..n],j->0),actcoords[i][2]);
    SetConjugate(coll,n+2,i,ObjByExponents(coll,x));
  od;
  UpdatePolycyclicCollector(coll); G:=PcpGroupByCollectorNC(coll);
  G!.markedLagrangian:=Subgroup(G,Igs(G){[n+1,n+2]});
  return G;
end;

PowerRationalExactLag := function(G)
  local cc,x,o,k;
  for cc in ConjugacyClasses(G) do
    x:=Representative(cc); o:=Order(x);
    for k in [1..o] do
      if GcdInt(k,o)=1 and not IsConjugate(G,x,x^k) then
        return [false,ExponentsOfPcElement(Pcgs(G),x),k];
      fi;
    od;
  od;
  return [true,fail,fail];
end;

SMPNormalClosuresExactLag := function(G)
  local reps,closures,i,j;
  reps:=List(ConjugacyClasses(G),Representative);
  closures:=List(reps,x->NormalClosure(G,Subgroup(G,[x])));
  for i in [1..Length(reps)] do
    for j in [1..i-1] do
      if closures[i]=closures[j] then return [false,i,j]; fi;
    od;
  od;
  return [true,Length(reps),Length(closures)];
end;

DeMeyerWitnessesLag := function(G,D,d)
  local out,B,b,qinv;
  out:=[];
  for B in NormalSubgroups(G) do
    if IsSubgroup(D,B) and IsSubgroup(Centre(D),B) then
      b:=LogInt(Size(B),2); qinv:=AbelianInvariants(FactorGroup(D,B));
      if b=6-d and Length(qinv)=2 and ForAll(qinv,n->n=2) then
        Add(out,[Size(B),b,qinv,
          List(Pcgs(B),z->ExponentsOfPcElement(Pcgs(G),z))]);
      fi;
    fi;
  od;
  return out;
end;

allcoeffslag:=ExponentsByRels(lagrec.coh.factor.rels);
if IsBound(lagusecompatible) and lagusecompatible=true then
  coeffslag:=orbitrepslag; weightslag:=orbitsizeslag;
else
  coeffslag:=allcoeffslag; weightslag:=List(coeffslag,x->1);
fi;
if not IsBound(classstartlag) then classstartlag:=1; fi;
if not IsBound(classlimitlag) then
  classlimitlag:=Length(coeffslag)-classstartlag+1;
fi;
classendlag:=Minimum(Length(coeffslag),classstartlag+classlimitlag-1);
Print("C8C2_Q11_CASE3_PARENT_SCREEN TOTAL_H2_CLASSES=",Length(allcoeffslag),
      " TOTAL_SCREEN_OBJECTS=",Length(coeffslag),
      " USE_COMPATIBLE_ORBITS=",
        IsBound(lagusecompatible) and lagusecompatible=true,
      " OBJECT_START=",classstartlag," OBJECT_END=",classendlag,"\n");

structurallag:=0; rationallag:=0; smplag:=0; demeyerlag:=0;
structuralrawlag:=0; rationalrawlag:=0; smprawlag:=0; demeyerrawlag:=0;
structuralidslag:=[]; survivoridslag:=[]; survivorclasseslag:=[];
propcachelag:=[];
for classidxlag in [classstartlag..classendlag] do
  coefflag:=coeffslag[classidxlag];
  coclag:=IntVector(coefflag*lagrec.coh.factor.prei);
  tailslag:=TailVectorC8C2Lag(coclag,lagrec.Crec);
  Hlag:=ExtensionC8C2Lag(lagrec.Crec,tailslag,lagrec.actioncoords);
  Lkerlag:=Hlag!.markedLagrangian; hgenslag:=Igs(Hlag);
  qhomlag:=NaturalHomomorphismByNormalSubgroup(Hlag,Lkerlag);
  validlag:=Size(Hlag)=256 and Size(Lkerlag)=16 and IsAbelian(Lkerlag) and
    AbelianInvariants(Lkerlag)=[2,8] and IsNormal(Hlag,Lkerlag) and
    IdGroup(Image(qhomlag))=[16,11];
  if validlag then
    for ilag in [1..Length(lagrec.actioncoords)] do
      if hgenslag[5]^hgenslag[ilag]<>
           hgenslag[5]^lagrec.actioncoords[ilag][1][1]*
           hgenslag[6]^lagrec.actioncoords[ilag][1][2] or
         hgenslag[6]^hgenslag[ilag]<>
           hgenslag[5]^lagrec.actioncoords[ilag][2][1]*
           hgenslag[6]^lagrec.actioncoords[ilag][2][2] then
        validlag:=false; break;
      fi;
    od;
  fi;
  if not validlag then Error("invalid marked extension class ",classidxlag); fi;

  Dlag:=DerivedSubgroup(Hlag); ablag:=AbelianInvariants(Hlag/Dlag);
  dlag:=Length(ablag);
  isstructlag:=IsAbelian(Dlag) and dlag in [3,4,5] and
    ForAll(ablag,n->n=2) and Size(Dlag)=2^(8-dlag) and
    Size(Intersection(Dlag,Lkerlag))=2^(7-dlag) and
    Exponent(Dlag)<=8 and NilpotencyClassOfGroup(Hlag)>=3 and
    Exponent(Hlag)<=16 and Exponent(Centre(Hlag))=2;
  if isstructlag then
    structurallag:=structurallag+1;
    structuralrawlag:=structuralrawlag+weightslag[classidxlag];
    hidlag:=IdGroup(Hlag)[2]; AddSet(structuralidslag,hidlag);
    proplag:=First(propcachelag,r->r.hid=hidlag);
    if proplag=fail then
      canlag:=SmallGroup(256,hidlag); Dcanlag:=DerivedSubgroup(canlag);
      abcanlag:=AbelianInvariants(canlag/Dcanlag); dcanlag:=Length(abcanlag);
      powlag:=PowerRationalExactLag(canlag); charlag:=false;
      if powlag[1] then
        irrLag:=Irr(canlag);
        charlag:=ForAll(irrLag,chi->ForAll(chi,v->IsRat(v)));
      fi;
      smptestlag:=[false,fail,fail]; demwlag:=[];
      if powlag[1] and charlag then
        smptestlag:=SMPNormalClosuresExactLag(canlag);
        if smptestlag[1] then
          demwlag:=DeMeyerWitnessesLag(canlag,Dcanlag,dcanlag);
        fi;
      fi;
      proplag:=rec(hid:=hidlag,pow:=powlag,char:=charlag,
        smp:=smptestlag,demw:=demwlag,
        structure:=StructureDescription(canlag),
        abinv:=abcanlag,dinv:=AbelianInvariants(Dcanlag),d:=dcanlag);
      Add(propcachelag,proplag);
    fi;
    if proplag.pow[1] and proplag.char then
      rationallag:=rationallag+1;
      rationalrawlag:=rationalrawlag+weightslag[classidxlag];
    fi;
    if proplag.smp[1] then
      smplag:=smplag+1; smprawlag:=smprawlag+weightslag[classidxlag];
    fi;
    if Length(proplag.demw)>0 then
      demeyerlag:=demeyerlag+1;
      demeyerrawlag:=demeyerrawlag+weightslag[classidxlag];
      AddSet(survivoridslag,hidlag);
      Add(survivorclasseslag,
        [classidxlag,coefflag,weightslag[classidxlag],hidlag]);
    fi;
    Print("STRUCTURAL_OBJECT=",classidxlag," COEFF=",coefflag,
          " WEIGHT=",weightslag[classidxlag]," H_ID=",hidlag,
          " POWER_RATIONAL=",proplag.pow[1],
          " POWER_RESULT=",proplag.pow,
          " CHAR_RATIONAL=",proplag.char," EXACT_SMP=",proplag.smp[1],
          " DEMEYER_WITNESS_COUNT=",Length(proplag.demw),"\n");
  fi;
  if (classidxlag-classstartlag+1) mod 32=0 then
    Print("LAGRANGIAN_PARENT_CHECKPOINT=",classidxlag-classstartlag+1,
          " STRUCTURAL=",structurallag," RATIONAL=",rationallag,
          " EXACT_SMP=",smplag," DEMEYER=",demeyerlag,
          " SURVIVOR_IDS=",survivoridslag,"\n");
  fi;
od;
Print("C8C2_Q11_CASE3_PARENT_SUMMARY TOTAL_H2_CLASSES=",Length(allcoeffslag),
      " TOTAL_SCREEN_OBJECTS=",Length(coeffslag),
      " COVERED_OBJECTS=",classendlag-classstartlag+1,
      " STRUCTURAL=",structurallag," RATIONAL=",rationallag,
      " EXACT_SMP=",smplag," DEMEYER=",demeyerlag,
      " STRUCTURAL_RAW_CLASSES=",structuralrawlag,
      " RATIONAL_RAW_CLASSES=",rationalrawlag,
      " EXACT_SMP_RAW_CLASSES=",smprawlag,
      " DEMEYER_RAW_CLASSES=",demeyerrawlag,
      " DISTINCT_STRUCTURAL_IDS=",structuralidslag,
      " SURVIVOR_IDS=",survivoridslag,
      " SURVIVOR_CLASSES=",survivorclasseslag,"\n");
