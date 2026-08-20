# Exact raw H^2(Q,C8) screen for the full-dual A=C8, Q=[32,43] branch.
# C8 is represented coefficient-safely as a quotient of an integral
# permutation lattice.  All 32 H^2 classes are converted to finite pc
# extensions with distinguished cyclic kernel and checked individually.

if LoadPackage("polycyclic")<>true then Error("Polycyclic unavailable"); fi;

UnitOnC8 := function(aut,g)
  local u;
  for u in [1,3,5,7] do
    if Image(aut,g)=g^u then return u; fi;
  od;
  Error("automorphism is not a C8 unit");
end;

InverseUnitMod8 := function(u)
  local v;
  for v in [1,3,5,7] do
    if (u*v) mod 8=1 then return v; fi;
  od;
  Error("unit has no inverse modulo 8");
end;

C8PermutationMatrix := function(u)
  local M,j;
  M:=NullMat(8,8);
  for j in [0..7] do M[j+1][(u*j mod 8)+1]:=1; od;
  return M;
end;

TailVectorModC8 := function(v,nslots)
  local out,i,j,s;
  out:=[];
  for i in [1..nslots] do
    s:=0;
    for j in [1..8] do s:=s+(j-1)*v[(i-1)*8+j]; od;
    Add(out,s mod 8);
  od;
  return out;
end;

ExtensionC8CR := function(C,c,units)
  local n,coll,rels,i,e,r,o,x,H;
  n:=Length(C.mats);
  if Length(c)<>Length(C.enumrels) then Error("wrong C8 tail length"); fi;
  coll:=FromTheLeftCollector(n+1);
  rels:=RelativeOrdersOfPcp(C.factor);
  for i in [1..Length(C.enumrels)] do
    e:=C.enumrels[i];
    r:=VectorOfWordCR(C.relators[e[1]][e[2]],n);
    Add(r,c[i] mod 8);
    o:=ObjByExponents(coll,r);
    if e[1]=e[2] then
      SetRelativeOrder(coll,e[1],rels[e[1]]);
      SetPower(coll,e[1],o);
    elif e[1]>e[2] then
      SetConjugate(coll,e[1],e[2],o);
    else
      SetConjugate(coll,e[1],-e[2]+e[1],o);
    fi;
  od;
  SetRelativeOrder(coll,n+1,8);
  for i in [1..n] do
    x:=Concatenation(List([1..n],j->0),[units[i]]);
    SetConjugate(coll,n+1,i,ObjByExponents(coll,x));
  od;
  UpdatePolycyclicCollector(coll);
  H:=PcpGroupByCollectorNC(coll);
  H!.module:=Subgroup(H,[Igs(H)[n+1]]);
  return H;
end;

HasSMPCharacterC8 := function(G)
  local irr,seen,i,j,sig;
  irr:=Irr(G); seen:=[];
  for i in [1..NrConjugacyClasses(G)] do
    sig:=[];
    for j in [1..Length(irr)] do Add(sig,irr[j][i]=irr[j][1]); od;
    if sig in seen then return false; fi;
    Add(seen,sig);
  od;
  return true;
end;

PassesRationalC8 := function(G)
  local cc,x,ox;
  for cc in ConjugacyClasses(G) do
    x:=Representative(cc); ox:=Order(x);
    if not IsConjugate(G,x,x^-1) then return false; fi;
    if ox>=8 and not IsConjugate(G,x,x^3) then return false; fi;
  od;
  return true;
end;

HasDeMeyerWitnessC8 := function(G,D,d)
  local normals,B,b,qinv;
  normals:=NormalSubgroups(G);
  for B in normals do
    if IsSubgroup(D,B) and IsSubgroup(Centre(D),B) then
      b:=LogInt(Size(B),2);
      if b<=d and (d-b) mod 2=0 then
        qinv:=AbelianInvariants(FactorGroup(D,B));
        if Length(qinv)>0 and Length(qinv) mod 2=0 and
           ForAll(qinv,n->n=2) then return [Position(normals,B),b,Length(qinv)]; fi;
      fi;
    fi;
  od;
  return fail;
end;

# Recover the exact dual affine group and its projection to Aut(C8).
A:=CyclicGroup(IsPcGroup,8); ag:=GeneratorsOfGroup(A)[1];
AutA:=AutomorphismGroup(A); autgens:=GeneratorsOfGroup(AutA);
V:=CyclicGroup(IsPcGroup,8); vg:=GeneratorsOfGroup(V)[1];
dualauts:=List(autgens,aut->GroupHomomorphismByImages(
  V,V,[vg],[vg^InverseUnitMod8(UnitOnC8(aut,ag))]));
DualAut:=Group(dualauts);
acthom:=GroupHomomorphismByImages(AutA,DualAut,autgens,dualauts);
P:=SemidirectProduct(AutA,acthom,V);
proj:=Projection(P); embV:=Embedding(P,2);
piso:=IsomorphismPcpGroup(P); U:=Image(piso); upcp:=Pcp(U); ugens:=Igs(U);

actionunits:=[]; mats:=[];
for ug in ugens do
  pre:=PreImagesRepresentative(piso,ug);
  unit:=UnitOnC8(Image(proj,pre),ag);
  Add(actionunits,unit); Add(mats,C8PermutationMatrix(unit));
od;
lat:=IdentityMat(8); lat[2]:=8*lat[2];
for j in [3..8] do lat[j][2]:=-(j-1); od;
C:=CRRecordByMats(U,mats);
coh:=TwoCohomologyModCR(C,lat);
coeffs:=ExponentsByRels(coh.factor.rels);

Print("GAP_VERSION=",GAPInfo.Version,
      " POLYCYCLIC_VERSION=",PackageInfo("polycyclic")[1].Version,
      " A=C8 Q_ID=",IdGroup(P),
      " TRANSLATION_KERNEL_ORDER=",Size(Image(embV,V)),"\n");
Print("ACTION_UNITS_MOD8=",actionunits,
      " LATTICE_DETERMINANT=",AbsInt(DeterminantMat(lat)),
      " H2_INVARIANTS=",coh.factor.rels,
      " RAW_CLASSES=",Length(coeffs),"\n");

structural:=0; rational:=0; exactsmp:=0; demeyer:=0;
parentids:=[]; pairdata:=[];
for idx in [1..Length(coeffs)] do
  tailfree:=IntVector(coeffs[idx]*coh.factor.prei);
  tail8:=TailVectorModC8(tailfree,Length(C.enumrels));
  H:=ExtensionC8CR(C,tail8,actionunits); N:=H!.module;
  qhom:=NaturalHomomorphismByNormalSubgroup(H,N);
  valid:=Size(H)=256 and Size(N)=8 and IsCyclic(N) and IsNormal(H,N) and
         IdGroup(Image(qhom))=[32,43] and
         ForAll([1..Length(actionunits)],i->
           Igs(N)[1]^Igs(H)[i]=Igs(N)[1]^actionunits[i]);
  if not valid then Error("constructed extension failed validation at class ",idx); fi;
  hid:=IdGroup(H)[2];
  D:=DerivedSubgroup(H); abinv:=AbelianInvariants(H/D); d:=Length(abinv);
  isstructural:=IsAbelian(D) and d in [3,4,5] and ForAll(abinv,n->n=2) and
    Size(D)=2^(8-d) and Exponent(D)<=8 and NilpotencyClassOfGroup(H)>=3 and
    Exponent(H)<=16 and Exponent(Centre(H))=2;
  if isstructural then
    structural:=structural+1;
    isrational:=PassesRationalC8(H);
    if isrational then
      rational:=rational+1; issmp:=HasSMPCharacterC8(H);
      if issmp then
        exactsmp:=exactsmp+1; dem:=HasDeMeyerWitnessC8(H,D,d);
        if dem<>fail then demeyer:=demeyer+1; AddSet(parentids,hid); fi;
      else dem:=fail;
      fi;
    else issmp:=false; dem:=fail;
    fi;
  else isrational:=false; issmp:=false; dem:=fail;
  fi;
  Add(pairdata,rec(H:=H,N:=N,hid:=hid,class:=coeffs[idx]));
  Print("CLASS=",coeffs[idx]," H_ID=",hid,
        " STRUCTURAL=",isstructural," RATIONAL=",isrational,
        " EXACT_SMP=",issmp," DEMEYER=",dem,"\n");
od;
Print("RAW_EXTENSION_SUMMARY TOTAL=",Length(coeffs),
      " STRUCTURAL=",structural," RATIONAL=",rational,
      " EXACT_SMP=",exactsmp," DEMEYER=",demeyer,
      " PARENT_IDS=",parentids,"\n");

# Exact compatible-pair orbits.  Two H^2 classes are in the same compatible-
# pair orbit iff their extensions are isomorphic by an isomorphism carrying
# the distinguished C8 kernel to the distinguished C8 kernel.  Map each pair
# to its canonical SmallGroup and take Aut(H)-orbits of the marked kernels.
SubgroupImageActionC8 := function(S,a) return Image(a,S); end;
paircache:=[]; pairorbitcount:=0;
for dat in pairdata do
  cache:=First(paircache,r->r.hid=dat.hid);
  if cache=fail then
    K:=SmallGroup(256,dat.hid);
    cache:=rec(hid:=dat.hid,K:=K,aut:=AutomorphismGroup(K),orbreps:=[]);
    Add(paircache,cache);
  fi;
  hiso:=IsomorphismGroups(dat.H,cache.K);
  if hiso=fail then Error("failed canonical isomorphism for ID ",dat.hid); fi;
  kernimg:=Image(hiso,dat.N);
  orbitpos:=First([1..Length(cache.orbreps)],i->
    RepresentativeAction(cache.aut,cache.orbreps[i],kernimg,
      SubgroupImageActionC8)<>fail);
  if orbitpos=fail then
    Add(cache.orbreps,kernimg); orbitpos:=Length(cache.orbreps);
    pairorbitcount:=pairorbitcount+1;
  fi;
  Print("PAIR_ORBIT_CLASS=",dat.class," H_ID=",dat.hid,
        " KERNEL_AUT_ORBIT=",orbitpos,"\n");
od;
Print("COMPATIBLE_PAIR_ORBIT_SUMMARY RAW_CLASSES=",Length(pairdata),
      " MARKED_PAIR_ORBITS=",pairorbitcount,
      " ABSTRACT_GROUP_IDS=",Set(List(pairdata,r->r.hid)),"\n");
QUIT;
