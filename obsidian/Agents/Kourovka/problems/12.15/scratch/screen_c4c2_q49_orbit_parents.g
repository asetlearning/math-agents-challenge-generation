# Exact parent-property screen on compatible-pair orbit representatives for
# the surviving full-dual C4xC2/[32,49] action.

Read("Agents/Kourovka/problems/12.15/scratch/pilot_c4c2_q49_compatible_orbits.g");

PowerRationalExactQ49 := function(G)
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

SMPNormalClosuresExactQ49 := function(G)
  local ccs,reps,closures,i,j;
  ccs:=ConjugacyClasses(G); reps:=List(ccs,Representative);
  closures:=List(reps,x->NormalClosure(G,Subgroup(G,[x])));
  for i in [1..Length(reps)] do
    for j in [1..i-1] do
      if closures[i]=closures[j] then return [false,i,j]; fi;
    od;
  od;
  return [true,Length(reps),Length(closures)];
end;

DeMeyerWitnessesQ49 := function(G,D,d)
  local out,B,b,qinv;
  out:=[];
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

if not IsBound(orbitstart49) then orbitstart49:=1; fi;
if not IsBound(orbitlimit49) then
  orbitlimit49:=Length(orbitreps49)-orbitstart49+1;
fi;
orbitend49:=Minimum(Length(orbitreps49),orbitstart49+orbitlimit49-1);
Print("Q49_PARENT_SCREEN ORBIT_REPRESENTATIVES=",Length(orbitreps49),
      " ORBIT_START=",orbitstart49," ORBIT_END=",orbitend49,"\n");

structuralorbits49:=0; rationalorbits49:=0; smporbits49:=0;
allfilterorbits49:=0; structuralraw49:=0; rationalraw49:=0;
smpraw49:=0; allfilterraw49:=0; propcacheq49:=[];
survivorids49:=[]; survivororbits49:=[]; structuralids49:=[];
for opos49 in [orbitstart49..orbitend49] do
  coeff49:=orbitreps49[opos49]; coc49:=IntVector(coeff49*coh49.factor.prei);
  tails49:=TailVectorModQ49(coc49);
  parent49:=ExtensionC4C2Q49(C49rec,tails49,actioncoords49);
  ker49:=parent49!.markedmoduleQ49; pgens49:=Igs(parent49);
  qhom49:=NaturalHomomorphismByNormalSubgroup(parent49,ker49);
  valid49:=Size(parent49)=256 and Size(ker49)=8 and IsAbelian(ker49) and
    AbelianInvariants(ker49)=[2,4] and IsNormal(parent49,ker49) and
    IdGroup(Image(qhom49))=[32,49];
  if valid49 then
    for i49 in [1..Length(actioncoords49)] do
      if pgens49[6]^pgens49[i49]<>
           pgens49[6]^actioncoords49[i49][1][1]*
           pgens49[7]^actioncoords49[i49][1][2] or
         pgens49[7]^pgens49[i49]<>
           pgens49[6]^actioncoords49[i49][2][1]*
           pgens49[7]^actioncoords49[i49][2][2] then
        valid49:=false; break;
      fi;
    od;
  fi;
  if not valid49 then Error("invalid marked extension at orbit ",opos49); fi;

  D49:=DerivedSubgroup(parent49); abinv49:=AbelianInvariants(parent49/D49);
  d49:=Length(abinv49);
  isstructural49:=IsAbelian(D49) and d49 in [3,4,5] and
    ForAll(abinv49,n49->n49=2) and Size(D49)=2^(8-d49) and
    Exponent(D49)<=8 and NilpotencyClassOfGroup(parent49)>=3 and
    Exponent(parent49)<=16 and Exponent(Centre(parent49))=2;
  if isstructural49 then
    structuralorbits49:=structuralorbits49+1;
    structuralraw49:=structuralraw49+orbitsizes49[opos49];
    hid49:=IdGroup(parent49)[2]; AddSet(structuralids49,hid49);
    prop49:=First(propcacheq49,r49->r49.hid=hid49);
    if prop49=fail then
      # Use the canonical SmallGroup for subgroup/character algorithms.  The
      # raw pc extension above remains the separately validated marked object.
      canparent49:=SmallGroup(256,hid49); Dcan49:=DerivedSubgroup(canparent49);
      abcan49:=AbelianInvariants(canparent49/Dcan49); dcan49:=Length(abcan49);
      pow49:=PowerRationalExactQ49(canparent49); irr49:=Irr(canparent49);
      charrat49:=ForAll(irr49,chi49->ForAll(chi49,v49->IsRat(v49)));
      smp49:=[false,fail,fail]; demw49:=[];
      if pow49[1] and charrat49 then
        smp49:=SMPNormalClosuresExactQ49(canparent49);
        if smp49[1] then
          demw49:=DeMeyerWitnessesQ49(canparent49,Dcan49,dcan49);
        fi;
      fi;
      prop49:=rec(hid:=hid49,pow:=pow49,charrat:=charrat49,
        smp:=smp49,demw:=demw49,structure:=StructureDescription(canparent49),
        dinv:=AbelianInvariants(Dcan49),abinv:=abcan49,d:=dcan49,
        class:=NilpotencyClassOfGroup(canparent49));
      Add(propcacheq49,prop49);
    fi;
    if prop49.pow[1] and prop49.charrat then
      rationalorbits49:=rationalorbits49+1;
      rationalraw49:=rationalraw49+orbitsizes49[opos49];
    fi;
    if prop49.smp[1] then
      smporbits49:=smporbits49+1; smpraw49:=smpraw49+orbitsizes49[opos49];
    fi;
    if Length(prop49.demw)>0 then
      allfilterorbits49:=allfilterorbits49+1;
      allfilterraw49:=allfilterraw49+orbitsizes49[opos49];
      AddSet(survivorids49,hid49);
      Add(survivororbits49,[opos49,coeff49,orbitsizes49[opos49],hid49]);
    fi;
    Print("STRUCTURAL_ORBIT=",opos49," COEFF=",coeff49,
          " ORBIT_SIZE=",orbitsizes49[opos49]," H_ID=",hid49,
          " POWER_RATIONAL=",prop49.pow[1]," CHAR_RATIONAL=",prop49.charrat,
          " EXACT_SMP=",prop49.smp[1],
          " DEMEYER_WITNESS_COUNT=",Length(prop49.demw),"\n");
  fi;
  if (opos49-orbitstart49+1) mod 100=0 then
    Print("PARENT_CHECKPOINT=",opos49-orbitstart49+1,
          " STRUCTURAL_ORBITS=",structuralorbits49,
          " RATIONAL_ORBITS=",rationalorbits49,
          " EXACT_SMP_ORBITS=",smporbits49,
          " ALL_FILTER_ORBITS=",allfilterorbits49,
          " SURVIVOR_IDS=",survivorids49,"\n");
  fi;
od;

Print("Q49_PARENT_SUMMARY TOTAL_H2_CLASSES=",Length(coeffs49),
      " TOTAL_COMPATIBLE_ORBITS=",Length(orbitreps49),
      " COVERED_ORBITS=",orbitend49-orbitstart49+1,
      " STRUCTURAL_ORBITS=",structuralorbits49,
      " RATIONAL_ORBITS=",rationalorbits49,
      " EXACT_SMP_ORBITS=",smporbits49,
      " ALL_FILTER_ORBITS=",allfilterorbits49,
      " STRUCTURAL_RAW_CLASSES=",structuralraw49,
      " RATIONAL_RAW_CLASSES=",rationalraw49,
      " EXACT_SMP_RAW_CLASSES=",smpraw49,
      " ALL_FILTER_RAW_CLASSES=",allfilterraw49,
      " STRUCTURAL_IDS=",structuralids49,
      " SURVIVOR_IDS=",survivorids49,
      " SURVIVOR_ORBITS=",survivororbits49,"\n");
