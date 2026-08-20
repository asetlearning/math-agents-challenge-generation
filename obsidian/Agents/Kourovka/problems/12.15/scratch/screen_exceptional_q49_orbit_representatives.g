# Lease-sized exhaustive screen of one surviving non-Lagrangian subcase.
# Here A=C2^3 and Q=H/A=SmallGroup(32,49), in its unique surviving affine
# embedding with full character-translation subgroup.  CompatiblePairs and
# ExtensionRepresentatives reduce H^2(Q,A) (dimension 14) to exact orbits.

HasSMPCharacterQ49 := function(G)
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

PassesRationalQ49 := function(G)
  local cc,x,ox;
  for cc in ConjugacyClasses(G) do
    x:=Representative(cc); ox:=Order(x);
    if not IsConjugate(G,x,x^-1) then return false; fi;
    if ox>=8 and not IsConjugate(G,x,x^3) then return false; fi;
  od;
  return true;
end;

HasDeMeyerWitnessQ49 := function(G,D,d)
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

# Build the exact dual affine group Hom(A,C2) semidirect Aut(A).
A:=ElementaryAbelianGroup(8); abasis:=Pcgs(A);
AutA:=AutomorphismGroup(A); autgens:=GeneratorsOfGroup(AutA);
V:=ElementaryAbelianGroup(8); vbasis:=Pcgs(V); dualauts:=[];
for aut in autgens do
  M:=List(abasis,a->ExponentsOfPcElement(abasis,Image(aut,a))*One(GF(2)));
  N:=TransposedMat(M^-1);
  imgs:=List(N,row->PcElementByExponents(vbasis,List(row,IntFFE)));
  Add(dualauts,GroupHomomorphismByImages(V,V,vbasis,imgs));
od;
DualAut:=Group(dualauts);
acthom:=GroupHomomorphismByImages(AutA,DualAut,autgens,dualauts);
P:=SemidirectProduct(AutA,acthom,V);
embV:=Embedding(P,2); proj:=Projection(P);

q49classes:=Filtered(ConjugacyClassesSubgroups(P),cc->
  Size(Representative(cc))=32 and IdGroup(Representative(cc))[2]=49 and
  Size(Intersection(Representative(cc),Image(embV,V)))=8);
if Length(q49classes)<>1 then Error("expected unique full-translation Q49 class"); fi;
S:=Representative(q49classes[1]);
siso:=IsomorphismPcGroup(S); Spc:=Image(siso); smats:=[];
for spcg in GeneratorsOfGroup(Spc) do
  sg:=PreImagesRepresentative(siso,spcg); saut:=Image(proj,sg);
  Add(smats,List(abasis,a->
    ExponentsOfPcElement(abasis,Image(saut,a))*One(GF(2))));
od;
smodule:=GModuleByMats(smats,GF(2));
scoh:=TwoCohomology(Spc,smodule);
Print("GAP_VERSION=",GAPInfo.Version,
      " Q_ID=49 INTERSECTION_V_ORDER=8 H2_DIM=",
      Dimension(Image(scoh.cohom))," RAW_CLASSES=",Size(Image(scoh.cohom)),"\n");

Print("COMPATIBLE_PAIRS_START\n");
CP:=CompatiblePairs(Spc,smodule);
Print("COMPATIBLE_PAIRS_ORDER=",Size(CP),"\n");
exts:=ExtensionRepresentatives(Spc,smodule,CP);
Print("EXTENSION_ORBIT_REPRESENTATIVES=",Length(exts),"\n");

structural:=0; rational:=0; exactsmp:=0; parentids:=[]; pos:=0;
for H in exts do
  pos:=pos+1; D:=DerivedSubgroup(H);
  abinv:=AbelianInvariants(H/D); d:=Length(abinv);
  if IsAbelian(D) and d in [3,4,5] and ForAll(abinv,n->n=2) and
     Size(D)=2^(8-d) and Exponent(D)<=8 and
     NilpotencyClassOfGroup(H)>=3 and Exponent(H)<=16 and
     Exponent(Centre(H))=2 then
    structural:=structural+1;
    if PassesRationalQ49(H) then
      rational:=rational+1;
      if HasSMPCharacterQ49(H) then
        exactsmp:=exactsmp+1;
        dem:=HasDeMeyerWitnessQ49(H,D,d);
        if dem<>fail then
          hid:=IdGroup(H)[2]; AddSet(parentids,hid);
          Print("PARENT_ORBIT_REP=",pos," H_ID=",hid,
                " D=",d," DEMEYER=",dem,"\n");
        fi;
      fi;
    fi;
  fi;
  if pos mod 50=0 then
    Print("ORBIT_REP_CHECKPOINT=",pos,
          " STRUCTURAL=",structural," RATIONAL=",rational,
          " EXACT_SMP=",exactsmp," PARENT_IDS=",parentids,"\n");
  fi;
od;
Print("Q49_EXTENSION_SUMMARY TOTAL_ORBIT_REPS=",Length(exts),
      " STRUCTURAL=",structural," RATIONAL=",rational,
      " EXACT_SMP=",exactsmp," PARENT_IDS=",parentids,"\n");

# Every parent is finally subjected to the complete H^2(H,C2)
# nondegeneracy and derived-restriction screen used elsewhere in this cycle.
noquit:=true; requirederived:=true; stopafterfirst:=true;
for hid in parentids do
  ordtarget:=256; idtarget:=hid;
  Read("Agents/Kourovka/problems/12.15/scratch/screen_nondegenerate_c2_cocycles.g");
od;
