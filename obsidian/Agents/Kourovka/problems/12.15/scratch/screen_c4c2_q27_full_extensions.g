# Exact raw and compatible-pair orbit screen for the marked full-dual
# A=C4xC2, Q=[32,27], dual-intersection-order-8 action.

Read("Agents/Kourovka/problems/12.15/scratch/pilot_c4c2_q27_full_action_cohomology.g");

TailVectorModC4C2 := function(v,nslots,elts,a4,a2)
  local coords,out,i,j,s4,s2;
  coords:=List(elts,x->CoordC4C2(x,a4,a2)); out:=[];
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

ExtensionC4C2CR := function(C,tails,actcoords)
  local n,coll,rels,i,e,r,o,x,H;
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
  UpdatePolycyclicCollector(coll); H:=PcpGroupByCollectorNC(coll);
  H!.module:=Subgroup(H,Igs(H){[n+1,n+2]});
  return H;
end;

HasSMPCharacterC4C2 := function(G)
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

PassesRationalC4C2 := function(G)
  local cc,x,ox;
  for cc in ConjugacyClasses(G) do
    x:=Representative(cc); ox:=Order(x);
    if not IsConjugate(G,x,x^-1) then return false; fi;
    if ox>=8 and not IsConjugate(G,x,x^3) then return false; fi;
  od;
  return true;
end;

HasDeMeyerWitnessC4C2 := function(G,D,d)
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

SubgroupImageActionC4C2 := function(S,a) return Image(a,S); end;

coeffs:=ExponentsByRels(coh.factor.rels);
if not IsBound(classstart) then classstart:=1; fi;
if not IsBound(classlimit) then classlimit:=Length(coeffs)-classstart+1; fi;
if not IsBound(dopairorbits) then dopairorbits:=true; fi;
classend:=Minimum(Length(coeffs),classstart+classlimit-1);

Print("C4C2_EXTENSION_SCREEN TOTAL_RAW_CLASSES=",Length(coeffs),
      " CLASS_START=",classstart," CLASS_END=",classend,
      " DO_PAIR_ORBITS=",dopairorbits,"\n");

structural:=0; rational:=0; exactsmp:=0; demeyer:=0; parentids:=[];
paircache:=[]; pairorbitcount:=0; idset:=[];
for idx in [classstart..classend] do
  tailfree:=IntVector(coeffs[idx]*coh.factor.prei);
  tails:=TailVectorModC4C2(tailfree,Length(C.enumrels),elts,a4,a2);
  H:=ExtensionC4C2CR(C,tails,actioncoords); N:=H!.module;
  hgens:=Igs(H); nfac:=Length(actioncoords);
  qhom:=NaturalHomomorphismByNormalSubgroup(H,N);
  valid:=Size(H)=256 and Size(N)=8 and AbelianInvariants(N)=[2,4] and
    IsNormal(H,N) and IdGroup(Image(qhom))=[32,27];
  if valid then
    for i in [1..nfac] do
      if hgens[nfac+1]^hgens[i]<>
           hgens[nfac+1]^actioncoords[i][1][1]*
           hgens[nfac+2]^actioncoords[i][1][2] or
         hgens[nfac+2]^hgens[i]<>
           hgens[nfac+1]^actioncoords[i][2][1]*
           hgens[nfac+2]^actioncoords[i][2][2] then
        valid:=false; break;
      fi;
    od;
  fi;
  if not valid then Error("constructed extension failed validation at class ",idx); fi;

  hid:=IdGroup(H)[2]; AddSet(idset,hid);
  D:=DerivedSubgroup(H); abinv:=AbelianInvariants(H/D); d:=Length(abinv);
  isstructural:=IsAbelian(D) and d in [3,4,5] and ForAll(abinv,n->n=2) and
    Size(D)=2^(8-d) and Exponent(D)<=8 and NilpotencyClassOfGroup(H)>=3 and
    Exponent(H)<=16 and Exponent(Centre(H))=2;
  if isstructural then
    structural:=structural+1; isrational:=PassesRationalC4C2(H);
    if isrational then
      rational:=rational+1; issmp:=HasSMPCharacterC4C2(H);
      if issmp then
        exactsmp:=exactsmp+1; dem:=HasDeMeyerWitnessC4C2(H,D,d);
        if dem<>fail then demeyer:=demeyer+1; AddSet(parentids,hid); fi;
      else dem:=fail;
      fi;
    else issmp:=false; dem:=fail;
    fi;
  else isrational:=false; issmp:=false; dem:=fail;
  fi;

  if dopairorbits then
    cache:=First(paircache,r->r.hid=hid);
    if cache=fail then
      K:=SmallGroup(256,hid);
      cache:=rec(hid:=hid,K:=K,aut:=AutomorphismGroup(K),orbreps:=[]);
      Add(paircache,cache);
    fi;
    hiso:=IsomorphismGroups(H,cache.K);
    if hiso=fail then Error("failed canonical isomorphism for ID ",hid); fi;
    kernimg:=Image(hiso,N);
    orbitpos:=First([1..Length(cache.orbreps)],j->
      RepresentativeAction(cache.aut,cache.orbreps[j],kernimg,
        SubgroupImageActionC4C2)<>fail);
    if orbitpos=fail then
      Add(cache.orbreps,kernimg); orbitpos:=Length(cache.orbreps);
      pairorbitcount:=pairorbitcount+1;
    fi;
  else orbitpos:=fail;
  fi;

  Print("CLASS_INDEX=",idx," CLASS=",coeffs[idx]," H_ID=",hid,
        " MARKED_ORBIT_IN_ID=",orbitpos,
        " STRUCTURAL=",isstructural," RATIONAL=",isrational,
        " EXACT_SMP=",issmp," DEMEYER=",dem,"\n");
  if (idx-classstart+1) mod 50=0 then
    Print("CHECKPOINT_COVERED=",idx-classstart+1,
          " PAIR_ORBITS=",pairorbitcount," DISTINCT_IDS=",Length(idset),
          " STRUCTURAL=",structural," RATIONAL=",rational,
          " EXACT_SMP=",exactsmp," PARENT_IDS=",parentids,"\n");
  fi;
od;

Print("C4C2_EXTENSION_SUMMARY TOTAL_RAW_CLASSES=",Length(coeffs),
      " COVERED_CLASSES=",classend-classstart+1,
      " MARKED_PAIR_ORBITS=",pairorbitcount,
      " DISTINCT_IDS=",Length(idset),
      " STRUCTURAL=",structural," RATIONAL=",rational,
      " EXACT_SMP=",exactsmp," DEMEYER=",demeyer,
      " PARENT_IDS=",parentids,"\n");
# Direct GAP invocation exits at EOF; wrappers may inspect the retained data.
