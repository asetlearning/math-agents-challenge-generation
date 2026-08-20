# Exact raw-class, marked-pair orbit, and parent-property screen for the
# surviving A=C4xC2, Q=[32,27], dual-intersection-order-4 affine action.

Read("Agents/Kourovka/problems/12.15/scratch/pilot_c4c2_q27_intersection4_action_cohomology.g");

TailVectorC4C2I4 := function(v,nslots,elts,a4,a2)
  local coords,out,i,j,s4,s2;
  coords:=List(elts,x->CoordC4C2I4(x,a4,a2)); out:=[];
  for i in [1..nslots] do
    s4:=0; s2:=0;
    for j in [1..Length(elts)] do
      s4:=s4+coords[j][1]*v[(i-1)*Length(elts)+j];
      s2:=s2+coords[j][2]*v[(i-1)*Length(elts)+j];
    od;
    Add(out,[s4 mod 4,s2 mod 2]);
  od;
  return out;
end;

ExtensionC4C2I4 := function(C,tails,actcoords)
  local n,coll,rels,i,e,r,o,x,extgrp;
  n:=Length(C.mats);
  if Length(tails)<>Length(C.enumrels) then Error("wrong C4xC2 tail length"); fi;
  coll:=FromTheLeftCollector(n+2); rels:=RelativeOrdersOfPcp(C.factor);
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
  SetRelativeOrder(coll,n+1,4); SetRelativeOrder(coll,n+2,2);
  for i in [1..n] do
    x:=Concatenation(List([1..n],j->0),actcoords[i][1]);
    SetConjugate(coll,n+1,i,ObjByExponents(coll,x));
    x:=Concatenation(List([1..n],j->0),actcoords[i][2]);
    SetConjugate(coll,n+2,i,ObjByExponents(coll,x));
  od;
  UpdatePolycyclicCollector(coll); extgrp:=PcpGroupByCollectorNC(coll);
  extgrp!.markedmoduleI4:=Subgroup(extgrp,Igs(extgrp){[n+1,n+2]});
  return extgrp;
end;

PowerRationalExactI4 := function(G)
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

SMPNormalClosuresExactI4 := function(G)
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

DeMeyerWitnessesI4 := function(G,D,d)
  local normals,out,B,b,qinv;
  normals:=NormalSubgroups(G); out:=[];
  for B in normals do
    if IsSubgroup(D,B) and IsSubgroup(Centre(D),B) then
      b:=LogInt(Size(B),2);
      if b<=d and (d-b) mod 2=0 then
        qinv:=AbelianInvariants(FactorGroup(D,B));
        if Length(qinv)>0 and Length(qinv) mod 2=0 and
           ForAll(qinv,n->n=2) then
          Add(out,[Position(normals,B),Size(B),b,qinv]);
        fi;
      fi;
    fi;
  od;
  return out;
end;

SubgroupImageActionI4 := function(S,a) return Image(a,S); end;

coeffs4:=ExponentsByRels(coh4.factor.rels);
if not IsBound(classstart4) then classstart4:=1; fi;
if not IsBound(classlimit4) then classlimit4:=Length(coeffs4)-classstart4+1; fi;
if not IsBound(dopairorbits4) then dopairorbits4:=true; fi;
classend4:=Minimum(Length(coeffs4),classstart4+classlimit4-1);

Print("C4C2_I4_EXTENSION_SCREEN TOTAL_RAW_CLASSES=",Length(coeffs4),
      " CLASS_START=",classstart4," CLASS_END=",classend4,
      " DO_PAIR_ORBITS=",dopairorbits4,"\n");

structural4:=0; rational4:=0; exactsmp4:=0; demeyer4:=0;
parentids4:=[]; paircache4:=[]; propcache4:=[]; pairorbitcount4:=0; idset4:=[];
for idx4 in [classstart4..classend4] do
  tailfree4:=IntVector(coeffs4[idx4]*coh4.factor.prei);
  tails4:=TailVectorC4C2I4(tailfree4,Length(C4rec.enumrels),aelts4,a4i4,a2i4);
  ext4:=ExtensionC4C2I4(C4rec,tails4,actioncoords4); ker4:=ext4!.markedmoduleI4;
  hgens4:=Igs(ext4); nfac4:=Length(actioncoords4);
  qhom4:=NaturalHomomorphismByNormalSubgroup(ext4,ker4);
  valid4:=Size(ext4)=256 and Size(ker4)=8 and IsAbelian(ker4) and
    AbelianInvariants(ker4)=[2,4] and IsNormal(ext4,ker4) and
    IdGroup(Image(qhom4))=[32,27];
  if valid4 then
    for i4 in [1..nfac4] do
      if hgens4[nfac4+1]^hgens4[i4]<>
           hgens4[nfac4+1]^actioncoords4[i4][1][1]*
           hgens4[nfac4+2]^actioncoords4[i4][1][2] or
         hgens4[nfac4+2]^hgens4[i4]<>
           hgens4[nfac4+1]^actioncoords4[i4][2][1]*
           hgens4[nfac4+2]^actioncoords4[i4][2][2] then
        valid4:=false; break;
      fi;
    od;
  fi;
  if not valid4 then Error("constructed extension failed validation at class ",idx4); fi;

  hid4:=IdGroup(ext4)[2]; AddSet(idset4,hid4);
  prop4:=First(propcache4,r4->r4.hid=hid4);
  if prop4=fail then
    D4:=DerivedSubgroup(ext4); abinv4:=AbelianInvariants(ext4/D4);
    d4:=Length(abinv4);
    isstructural4:=IsAbelian(D4) and d4 in [3,4,5] and
      ForAll(abinv4,n4->n4=2) and Size(D4)=2^(8-d4) and
      Exponent(D4)<=8 and NilpotencyClassOfGroup(ext4)>=3 and
      Exponent(ext4)<=16 and Exponent(Centre(ext4))=2;
    powrat4:=[false,fail,fail]; charrat4:=false;
    smp4:=[false,fail,fail]; demw4:=[];
    if isstructural4 then
      powrat4:=PowerRationalExactI4(ext4);
      irr4:=Irr(ext4); charrat4:=ForAll(irr4,chi4->ForAll(chi4,v4->IsRat(v4)));
      if powrat4[1] and charrat4 then
        smp4:=SMPNormalClosuresExactI4(ext4);
        if smp4[1] then demw4:=DeMeyerWitnessesI4(ext4,D4,d4); fi;
      fi;
    fi;
    prop4:=rec(hid:=hid4,structural:=isstructural4,powrat:=powrat4,
      charrat:=charrat4,smp:=smp4,demw:=demw4,d:=d4,
      dinv:=AbelianInvariants(D4),abinv:=abinv4,
      class:=NilpotencyClassOfGroup(ext4));
    Add(propcache4,prop4);
  fi;

  if prop4.structural then structural4:=structural4+1; fi;
  if prop4.powrat[1] and prop4.charrat then rational4:=rational4+1; fi;
  if prop4.smp[1] then exactsmp4:=exactsmp4+1; fi;
  if Length(prop4.demw)>0 then demeyer4:=demeyer4+1; AddSet(parentids4,hid4); fi;

  if dopairorbits4 then
    pairdat4:=First(paircache4,r4->r4.hid=hid4);
    if pairdat4=fail then
      can4:=SmallGroup(256,hid4);
      pairdat4:=rec(hid:=hid4,can:=can4,aut:=AutomorphismGroup(can4),orbreps:=[]);
      Add(paircache4,pairdat4);
    fi;
    hiso4:=IsomorphismGroups(ext4,pairdat4.can);
    if hiso4=fail then Error("failed canonical isomorphism for ID ",hid4); fi;
    kernimg4:=Image(hiso4,ker4);
    orbitpos4:=fail;
    if Length(pairdat4.orbreps)>0 then
      orbitpos4:=First([1..Length(pairdat4.orbreps)],j4->
        RepresentativeAction(pairdat4.aut,pairdat4.orbreps[j4],kernimg4,
          SubgroupImageActionI4)<>fail);
    fi;
    if orbitpos4=fail then
      Add(pairdat4.orbreps,kernimg4); orbitpos4:=Length(pairdat4.orbreps);
      pairorbitcount4:=pairorbitcount4+1;
    fi;
  else orbitpos4:=fail;
  fi;

  Print("CLASS_INDEX=",idx4," CLASS=",coeffs4[idx4]," H_ID=",hid4,
        " MARKED_ORBIT_IN_ID=",orbitpos4,
        " STRUCTURAL=",prop4.structural,
        " POWER_RATIONAL=",prop4.powrat[1]," CHAR_RATIONAL=",prop4.charrat,
        " EXACT_SMP=",prop4.smp[1]," DEMEYER_COUNT=",Length(prop4.demw),"\n");
  if (idx4-classstart4+1) mod 32=0 then
    Print("CHECKPOINT_COVERED=",idx4-classstart4+1,
          " PAIR_ORBITS=",pairorbitcount4," DISTINCT_IDS=",Length(idset4),
          " STRUCTURAL=",structural4," RATIONAL=",rational4,
          " EXACT_SMP=",exactsmp4," DEMEYER=",demeyer4,
          " PARENT_IDS=",parentids4,"\n");
  fi;
od;

Print("C4C2_I4_EXTENSION_SUMMARY TOTAL_RAW_CLASSES=",Length(coeffs4),
      " COVERED_CLASSES=",classend4-classstart4+1,
      " MARKED_PAIR_ORBITS=",pairorbitcount4,
      " DISTINCT_IDS=",Length(idset4),
      " STRUCTURAL=",structural4," RATIONAL=",rational4,
      " EXACT_SMP=",exactsmp4," DEMEYER=",demeyer4,
      " PARENT_IDS=",parentids4,"\n");
