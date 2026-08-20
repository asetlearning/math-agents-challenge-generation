# Direct canonical-SmallGroups witnesses for the two rational parent-filter
# candidates in the surviving intersection-order-4 affine branch.

PowerRationalWitnessI4V := function(G)
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

DeMeyerWitnessesI4V := function(G)
  local D,d,out,B,b,qinv;
  D:=DerivedSubgroup(G); d:=Length(AbelianInvariants(G/D)); out:=[];
  for B in NormalSubgroups(G) do
    if IsSubgroup(D,B) and IsSubgroup(Centre(D),B) then
      b:=LogInt(Size(B),2); qinv:=AbelianInvariants(FactorGroup(D,B));
      if b<=d and (d-b) mod 2=0 and Length(qinv)>0 and
         Length(qinv) mod 2=0 and ForAll(qinv,n->n=2) then
        Add(out,[Size(B),b,qinv,
          List(Pcgs(B),z->ExponentsOfPcElement(Pcgs(G),z))]);
      fi;
    fi;
  od;
  return out;
end;

for hidv in [25880,25886] do
  Gv:=SmallGroup(256,hidv); pgv:=Pcgs(Gv);
  ccsv:=ConjugacyClasses(Gv); repsv:=List(ccsv,Representative);
  closuresv:=List(repsv,xv->NormalClosure(Gv,Subgroup(Gv,[xv])));
  collisionsv:=[];
  for iv in [1..Length(repsv)] do
    for jv in [1..iv-1] do
      if closuresv[iv]=closuresv[jv] then Add(collisionsv,[iv,jv]); fi;
    od;
  od;
  firstv:=collisionsv[1]; xv:=repsv[firstv[1]]; yv:=repsv[firstv[2]];
  powv:=PowerRationalWitnessI4V(Gv); irrv:=Irr(Gv);
  demwv:=DeMeyerWitnessesI4V(Gv);
  firstdemv:=fail; if Length(demwv)>0 then firstdemv:=demwv[1]; fi;
  Print("PARENT_ID=",hidv," STRUCTURE=",StructureDescription(Gv),
        " CLASS=",NilpotencyClassOfGroup(Gv),
        " DERIVED_INVARIANTS=",AbelianInvariants(DerivedSubgroup(Gv)),
        " ABELIANIZATION=",AbelianInvariants(Gv/DerivedSubgroup(Gv)),"\n");
  Print("POWER_RATIONAL_EXACT=",powv[1],
        " CHARACTERS_RATIONAL_VALUED=",
        ForAll(irrv,chiv->ForAll(chiv,vv->IsRat(vv))),
        " CONJUGACY_CLASSES=",Length(ccsv),
        " NORMAL_CLOSURE_COLLISION_PAIRS=",Length(collisionsv),
        " DEMEYER_WITNESS_COUNT=",Length(demwv),
        " FIRST_DEMEYER_WITNESS=",firstdemv,"\n");
  Print("FIRST_COLLISION_CLASS_INDICES=",firstv,
        " X_EXPONENTS=",ExponentsOfPcElement(pgv,xv),
        " X_ORDER=",Order(xv)," X_CLASS_SIZE=",Size(ccsv[firstv[1]]),
        " Y_EXPONENTS=",ExponentsOfPcElement(pgv,yv),
        " Y_ORDER=",Order(yv)," Y_CLASS_SIZE=",Size(ccsv[firstv[2]]),
        " IS_CONJUGATE=",IsConjugate(Gv,xv,yv),
        " NORMAL_CLOSURES_EQUAL=",closuresv[firstv[1]]=closuresv[firstv[2]],
        " NORMAL_CLOSURE_ORDER=",Size(closuresv[firstv[1]]),"\n");
od;
