# Exhaustive extension screen for the surviving A=C2^3 non-Lagrangian
# affine embeddings whose H^2(Q,A) dimensions are at most 8.  This covers
# 256+64 extension classes; the dimension-14 class is deliberately excluded.

HasSMPCharacterExc := function(G)
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

PassesRationalExc := function(G)
  local cc,x,ox;
  for cc in ConjugacyClasses(G) do
    x:=Representative(cc); ox:=Order(x);
    if not IsConjugate(G,x,x^-1) then return false; fi;
    if ox>=8 and not IsConjugate(G,x,x^3) then return false; fi;
  od;
  return true;
end;

HasDeMeyerWitnessExc := function(G,D,d)
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
embAut:=Embedding(P,1); embV:=Embedding(P,2); proj:=Projection(P);

Print("GAP_VERSION=",GAPInfo.Version," AFFINE_DUAL_ORDER=",Size(P),"\n");
embeddingcase:=0; coveredclasses:=0;
for cc in ConjugacyClassesSubgroups(P) do
  S:=Representative(cc);
  if Size(S)=32 and IdGroup(S)[2] in [27,49] then
    embeddingcase:=embeddingcase+1;
    regularwitness:=fail;
    for a in Elements(A) do
      if not IsOne(a) then
        avec:=ExponentsOfPcElement(abasis,a); isregular:=true;
        for s in Elements(S) do
          saut:=Image(proj,s);
          if Image(saut,a)=a then
            residual:=PreImagesRepresentative(embV,Image(embAut,saut)^-1*s);
            vvec:=ExponentsOfPcElement(vbasis,residual);
            if Sum([1..3],i->avec[i]*vvec[i]) mod 2=1 then
              isregular:=false; break;
            fi;
          fi;
        od;
        if isregular then regularwitness:=avec; break; fi;
      fi;
    od;
    if regularwitness=fail then
      siso:=IsomorphismPcGroup(S); Spc:=Image(siso); smats:=[];
      for spcg in GeneratorsOfGroup(Spc) do
        sg:=PreImagesRepresentative(siso,spcg); saut:=Image(proj,sg);
        Add(smats,List(abasis,a->
          ExponentsOfPcElement(abasis,Image(saut,a))*One(GF(2))));
      od;
      smodule:=GModuleByMats(smats,GF(2));
      scoh:=TwoCohomology(Spc,smodule);
      classspace:=Image(scoh.cohom);
      classbasis:=BasisVectors(Basis(classspace));
      h2dim:=Length(classbasis);
      Print("SURVIVING_EMBEDDING_CASE=",embeddingcase,
            " Q_ID=",IdGroup(S)[2],
            " INTERSECTION_V_ORDER=",Size(Intersection(S,Image(embV,V))),
            " H2_DIM=",h2dim,"\n");
      if h2dim<=8 then
        structural:=0; rational:=0; exactsmp:=0; parentids:=[];
        for idx in [0..2^h2dim-1] do
          coeff:=CoefficientsMultiadic(List([1..h2dim],j->2),idx)*One(GF(2));
          classv:=Zero(classspace);
          for j in [1..h2dim] do classv:=classv+coeff[j]*classbasis[j]; od;
          cocycle:=PreImagesRepresentative(scoh.cohom,classv);
          H:=ExtensionSQ(scoh.collector,Spc,smodule,cocycle);
          D:=DerivedSubgroup(H);
          abinv:=AbelianInvariants(H/D); d:=Length(abinv);
          if IsAbelian(D) and d in [3,4,5] and ForAll(abinv,n->n=2) and
             Size(D)=2^(8-d) and Exponent(D)<=8 and
             NilpotencyClassOfGroup(H)>=3 and Exponent(H)<=16 and
             Exponent(Centre(H))=2 then
            structural:=structural+1;
            if PassesRationalExc(H) then
              rational:=rational+1;
              if HasSMPCharacterExc(H) then
                exactsmp:=exactsmp+1;
                dem:=HasDeMeyerWitnessExc(H,D,d);
                if dem<>fail then
                  hid:=IdGroup(H)[2]; AddSet(parentids,hid);
                  Print("PARENT_EXTENSION_CLASS=",idx,
                        " H_ID=",hid," D=",d," DEMEYER=",dem,"\n");
                fi;
              fi;
            fi;
          fi;
          if (idx+1) mod 32=0 then
            Print("EXTENSION_CHECKPOINT_CASE=",embeddingcase,
                  " COMPLETED_CLASSES=",idx+1,
                  " STRUCTURAL=",structural," RATIONAL=",rational,
                  " EXACT_SMP=",exactsmp," PARENT_IDS=",parentids,"\n");
          fi;
        od;
        coveredclasses:=coveredclasses+2^h2dim;
        Print("EXTENSION_SUMMARY_CASE=",embeddingcase,
              " TOTAL_CLASSES=",2^h2dim,
              " STRUCTURAL=",structural," RATIONAL=",rational,
              " EXACT_SMP=",exactsmp," PARENT_IDS=",parentids,"\n");
      else
        Print("LEASE_SIZED_CASE_SKIPPED=",embeddingcase,
              " TOTAL_CLASSES=",2^h2dim,"\n");
      fi;
    fi;
  fi;
od;
Print("TOTAL_EXHAUSTIVELY_COVERED_EXTENSION_CLASSES=",coveredclasses,"\n");
QUIT;
