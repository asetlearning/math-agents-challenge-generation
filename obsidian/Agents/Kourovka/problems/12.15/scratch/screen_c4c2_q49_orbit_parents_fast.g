# Exact parent-property screen on compatible-pair orbit representatives for
# the surviving full-dual C4xC2/[32,49] action.  This version applies the exact
# power-rationality filter first, since it is necessary and cheaply rejects
# almost every validated marked extension.  Later counts are sequential.

Read("Agents/Kourovka/problems/12.15/scratch/pilot_c4c2_q49_compatible_orbits.g");

PowerRationalExactFastQ49 := function(G)
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

SMPNormalClosuresExactFastQ49 := function(G)
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

DeMeyerWitnessesFastQ49 := function(G,D,d)
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
Print("Q49_FAST_PARENT_SCREEN ORBIT_REPRESENTATIVES=",Length(orbitreps49),
      " ORBIT_START=",orbitstart49," ORBIT_END=",orbitend49,"\n");

rationalorbits49:=0; rationalraw49:=0; structuralorbits49:=0;
structuralraw49:=0; smporbits49:=0; smpraw49:=0;
allfilterorbits49:=0; allfilterraw49:=0; propcacheq49:=[];
rationalids49:=[]; survivorids49:=[]; survivororbits49:=[];
failurewitnesses49:=[]; powcacheq49:=[];
abprefilterorbits49:=0; abprefilterraw49:=0;
for opos49 in [orbitstart49..orbitend49] do
  coeff49:=orbitreps49[opos49]; coc49:=IntVector(coeff49*coh49.factor.prei);
  tails49:=TailVectorModQ49(coc49);
  parent49:=ExtensionC4C2Q49(C49rec,tails49,actioncoords49);
  ker49:=parent49!.markedmoduleQ49; pgens49:=Igs(parent49);
  valid49:=Size(parent49)=256 and Size(ker49)=8 and IsAbelian(ker49) and
    AbelianInvariants(ker49)=[2,4] and IsNormal(parent49,ker49);
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

  # Lossless cheap parent prefilter from the minimal-counterexample reduction:
  # H/H' must be elementary abelian of rank 3, 4, or 5.  Only then pay for
  # catalogue identification and conjugacy calculations.
  abquick49:=AbelianInvariants(parent49);
  if Length(abquick49) in [3,4,5] and ForAll(abquick49,n49->n49=2) then
    abprefilterorbits49:=abprefilterorbits49+1;
    abprefilterraw49:=abprefilterraw49+orbitsizes49[opos49];
    hid49:=IdGroup(parent49)[2];
    powrec49:=First(powcacheq49,r49->r49.hid=hid49);
    if powrec49=fail then
      canparent49:=SmallGroup(256,hid49);
      pow49:=PowerRationalExactFastQ49(canparent49);
      powrec49:=rec(hid:=hid49,pow:=pow49);
      Add(powcacheq49,powrec49);
    else
      pow49:=powrec49.pow;
    fi;
  else
    pow49:=[false,fail,fail];
  fi;
  if IsBound(hid49) and pow49[1] then
    rationalorbits49:=rationalorbits49+1;
    rationalraw49:=rationalraw49+orbitsizes49[opos49];
    # The collector construction is over the fixed Q49 presentation.  Confirm
    # its quotient explicitly on every case that can survive rationality.
    qhom49:=NaturalHomomorphismByNormalSubgroup(parent49,ker49);
    if IdGroup(Image(qhom49))<>[32,49] then
      Error("rational marked extension has wrong quotient at orbit ",opos49);
    fi;
    AddSet(rationalids49,hid49);
    prop49:=First(propcacheq49,r49->r49.hid=hid49);
    if prop49=fail then
      canparent49:=SmallGroup(256,hid49); Dcan49:=DerivedSubgroup(canparent49);
      abcan49:=AbelianInvariants(canparent49/Dcan49); dcan49:=Length(abcan49);
      irr49:=Irr(canparent49);
      charrat49:=ForAll(irr49,chi49->ForAll(chi49,v49->IsRat(v49)));
      isstructural49:=IsAbelian(Dcan49) and dcan49 in [3,4,5] and
        ForAll(abcan49,n49->n49=2) and Size(Dcan49)=2^(8-dcan49) and
        Exponent(Dcan49)<=8 and NilpotencyClassOfGroup(canparent49)>=3 and
        Exponent(canparent49)<=16 and Exponent(Centre(canparent49))=2;
      smp49:=[false,fail,fail]; demw49:=[];
      if charrat49 and isstructural49 then
        smp49:=SMPNormalClosuresExactFastQ49(canparent49);
        if smp49[1] then
          demw49:=DeMeyerWitnessesFastQ49(canparent49,Dcan49,dcan49);
        fi;
      fi;
      prop49:=rec(hid:=hid49,charrat:=charrat49,
        structural:=isstructural49,smp:=smp49,demw:=demw49,
        structure:=StructureDescription(canparent49),
        dinv:=AbelianInvariants(Dcan49),abinv:=abcan49,d:=dcan49,
        class:=NilpotencyClassOfGroup(canparent49));
      Add(propcacheq49,prop49);
    fi;
    if not prop49.charrat then Error("power/character rationality mismatch"); fi;
    if prop49.structural then
      structuralorbits49:=structuralorbits49+1;
      structuralraw49:=structuralraw49+orbitsizes49[opos49];
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
    Print("RATIONAL_ORBIT=",opos49," COEFF=",coeff49,
          " ORBIT_SIZE=",orbitsizes49[opos49]," H_ID=",hid49,
          " CHAR_RATIONAL=",prop49.charrat,
          " STRUCTURAL=",prop49.structural,
          " EXACT_SMP=",prop49.smp[1],
          " DEMEYER_WITNESS_COUNT=",Length(prop49.demw),"\n");
  elif IsBound(hid49) then
    Add(failurewitnesses49,[pow49[2],pow49[3]]);
  fi;
  if IsBound(hid49) then Unbind(hid49); fi;
  if (opos49-orbitstart49+1) mod 100=0 then
    Print("FAST_PARENT_CHECKPOINT=",opos49-orbitstart49+1,
          " ABELIAN_PREFILTER_ORBITS=",abprefilterorbits49,
          " RATIONAL_ORBITS=",rationalorbits49,
          " STRUCTURAL_AFTER_RATIONAL=",structuralorbits49,
          " EXACT_SMP_ORBITS=",smporbits49,
          " ALL_FILTER_ORBITS=",allfilterorbits49,
          " SURVIVOR_IDS=",survivorids49,"\n");
  fi;
od;

Print("Q49_FAST_PARENT_SUMMARY TOTAL_H2_CLASSES=",Length(coeffs49),
      " TOTAL_COMPATIBLE_ORBITS=",Length(orbitreps49),
      " COVERED_ORBITS=",orbitend49-orbitstart49+1,
      " ABELIAN_PREFILTER_ORBITS=",abprefilterorbits49,
      " RATIONAL_ORBITS=",rationalorbits49,
      " STRUCTURAL_AFTER_RATIONAL=",structuralorbits49,
      " EXACT_SMP_ORBITS=",smporbits49,
      " ALL_FILTER_ORBITS=",allfilterorbits49,
      " ABELIAN_PREFILTER_RAW_CLASSES=",abprefilterraw49,
      " RATIONAL_RAW_CLASSES=",rationalraw49,
      " STRUCTURAL_AFTER_RATIONAL_RAW_CLASSES=",structuralraw49,
      " EXACT_SMP_RAW_CLASSES=",smpraw49,
      " ALL_FILTER_RAW_CLASSES=",allfilterraw49,
      " RATIONAL_IDS=",rationalids49,
      " SURVIVOR_IDS=",survivorids49,
      " SURVIVOR_ORBITS=",survivororbits49,
      " DISTINCT_ABSTRACT_IDS=",Length(powcacheq49),
      " POWER_FAILURE_DISTINCT_WITNESSES=",Length(Set(failurewitnesses49)),
      " POWER_FAILURE_K_DISTRIBUTION=",
        Collected(List(failurewitnesses49,x49->x49[2])),
      "\n");
