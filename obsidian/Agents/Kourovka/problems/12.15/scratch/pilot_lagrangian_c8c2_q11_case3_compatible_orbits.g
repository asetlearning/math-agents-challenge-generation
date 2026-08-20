# Exact compatible-pair action on H^2(Q,L)=C2^9 for the unique
# restricted-SMP-surviving C8xC2/[16,11] regular affine action.

lagcasetargets:=[3];
Read("Agents/Kourovka/problems/12.15/scratch/pilot_lagrangian_c8c2_q11_actions_cohomology.g");
lagrec:=lagrecords[1];

TailVectorLagComp := function(v)
  local coords,out,i,j,s8,s2;
  coords:=List(leltslag,x->CoordC8C2Lag(x,l8lag,l2lag)); out:=[];
  for i in [1..Length(lagrec.Crec.enumrels)] do
    s8:=0; s2:=0;
    for j in [1..Length(leltslag)] do
      s8:=s8+coords[j][1]*v[(i-1)*Length(leltslag)+j];
      s2:=s2+coords[j][2]*v[(i-1)*Length(leltslag)+j];
    od;
    Add(out,[s8 mod 8,s2 mod 2]);
  od;
  return out;
end;

ExtensionLagComp := function(C,tails,actcoords)
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

ModuleCoordsLagComp := function(x,m8,m2)
  local i,j;
  for i in [0..7] do
    for j in [0..1] do if x=m8^i*m2^j then return [i,j]; fi; od;
  od;
  Error("tail escaped marked C8xC2 module");
end;

CocycleToFactorLagComp := function(coc)
  local elm,i;
  elm:=PcpSolutionIntMat(lagrec.coh.gcc,coc);
  if elm=fail then Error("transformed tail is not in cocycle lattice"); fi;
  elm:=elm*lagrec.coh.factor.imgs;
  for i in [1..Length(elm)] do
    elm[i]:=elm[i] mod lagrec.coh.factor.rels[i];
  od;
  return elm;
end;

PairImageOfCocycleLagComp := function(coc,alpha,beta)
  local tails,E,egs,n,base,m8,m2,ainv,newlifts,invlifts,rels,
        out,e,i,j,lhs,rhs,t,tc,ta,ac,slot;
  tails:=TailVectorLagComp(coc);
  E:=ExtensionLagComp(lagrec.Crec,tails,lagrec.actioncoords);
  egs:=Igs(E); n:=Length(lagrec.ugens); base:=egs{[1..n]};
  m8:=egs[n+1]; m2:=egs[n+2]; ainv:=InverseGeneralMapping(alpha);
  newlifts:=List(lagrec.ugens,q->
    MappedVector(ExponentsByPcp(lagrec.upcp,Image(ainv,q)),base));
  invlifts:=List(newlifts,x->x^-1);
  rels:=RelativeOrdersOfPcp(lagrec.Crec.factor); out:=[];
  for e in lagrec.Crec.enumrels do
    i:=e[1]; j:=e[2];
    rhs:=MappedWordCR(lagrec.Crec.relators[i][j],newlifts,invlifts);
    if i=j then
      lhs:=newlifts[i]^rels[i];
    elif j<i then
      lhs:=newlifts[i]^newlifts[j];
    else
      lhs:=newlifts[i]^(newlifts[j-i]^-1);
    fi;
    t:=rhs^-1*lhs;
    if not t in E!.markedLagrangian then Error("relation tail escaped module"); fi;
    tc:=ModuleCoordsLagComp(t,m8,m2);
    ta:=Image(beta,l8lag^tc[1]*l2lag^tc[2]);
    ac:=CoordC8C2Lag(ta,l8lag,l2lag);
    slot:=List(leltslag,x->0); slot[pos8lag]:=ac[1]; slot[pos2lag]:=ac[2];
    Append(out,slot);
  od;
  return CocycleToFactorLagComp(out);
end;

ApplyFactorMapLagComp := function(v,rows)
  local out,i,j;
  out:=List(lagrec.coh.factor.rels,x->0);
  for i in [1..Length(v)] do
    for j in [1..Length(out)] do out[j]:=out[j]+v[i]*rows[i][j]; od;
  od;
  for j in [1..Length(out)] do
    out[j]:=out[j] mod lagrec.coh.factor.rels[j];
  od;
  return out;
end;

MixedIndexLagComp := function(v,rels)
  local z,i;
  z:=0; for i in [1..Length(v)] do z:=z*rels[i]+v[i]; od;
  return z+1;
end;

rhoimglag:=Group(lagrec.actionauts);
rholag:=GroupHomomorphismByImages(lagrec.Q,rhoimglag,
  lagrec.ugens,lagrec.actionauts);
if not IsGroupHomomorphism(rholag) then Error("action homomorphism failed"); fi;
AutQlag:=AutomorphismGroup(lagrec.Q); autqeltslag:=Elements(AutQlag);
AutLlag:=AutomorphismGroup(Llag); autaeltslag:=Elements(AutLlag);
compatiblelag:=[]; pairpermslag:=[];
qeltslag:=Elements(lagrec.Q);
for alphalag in autqeltslag do
  for betalag in autaeltslag do
    compatlag:=true;
    for qglag in lagrec.ugens do
      for alag in [l8lag,l2lag] do
        if Image(betalag,Image(Image(rholag,qglag),alag))<>
           Image(Image(rholag,Image(alphalag,qglag)),Image(betalag,alag)) then
          compatlag:=false; break;
        fi;
      od;
      if not compatlag then break; fi;
    od;
    if compatlag then
      Add(compatiblelag,[alphalag,betalag]);
      pimgslag:=Concatenation(
        List(qeltslag,q->Position(qeltslag,Image(alphalag,q))),
        List(leltslag,a->Length(qeltslag)+Position(leltslag,Image(betalag,a))));
      Add(pairpermslag,PermList(pimgslag));
    fi;
  od;
od;
CPpermlag:=Group(pairpermslag); cppermgenslag:=SmallGeneratingSet(CPpermlag);
cppairslag:=List(cppermgenslag,p->compatiblelag[Position(pairpermslag,p)]);

idrowslag:=List(lagrec.coh.factor.prei,c->
  PairImageOfCocycleLagComp(c,One(AutQlag),One(AutLlag)));
identityoklag:=idrowslag=IdentityMat(Length(lagrec.coh.factor.rels));
actionrowslag:=[];
for pairlag in cppairslag do
  Add(actionrowslag,List(lagrec.coh.factor.prei,c->
    PairImageOfCocycleLagComp(c,pairlag[1],pairlag[2])));
od;
coeffslag:=ExponentsByRels(lagrec.coh.factor.rels);
bijectivelag:=ForAll(actionrowslag,rows->
  Length(Set(List(coeffslag,v->ApplyFactorMapLagComp(v,rows))))=Length(coeffslag));

seenlag:=BlistList([1..Length(coeffslag)],[]); orbitrepslag:=[]; orbitsizeslag:=[];
for vlag in coeffslag do
  keylag:=MixedIndexLagComp(vlag,lagrec.coh.factor.rels);
  if not seenlag[keylag] then
    Add(orbitrepslag,vlag); queuelag:=[vlag]; seenlag[keylag]:=true; headlag:=1;
    while headlag<=Length(queuelag) do
      wlag:=queuelag[headlag]; headlag:=headlag+1;
      for rowslag in actionrowslag do
        imlag:=ApplyFactorMapLagComp(wlag,rowslag);
        ikeylag:=MixedIndexLagComp(imlag,lagrec.coh.factor.rels);
        if not seenlag[ikeylag] then
          seenlag[ikeylag]:=true; Add(queuelag,imlag);
        fi;
      od;
    od;
    Add(orbitsizeslag,Length(queuelag));
  fi;
od;

Print("AUT_Q_ORDER=",Size(AutQlag)," AUT_L_ORDER=",Size(AutLlag),
      " COMPATIBLE_PAIRS_ENUMERATED=",Length(compatiblelag),
      " COMPATIBLE_PAIR_GROUP_ORDER=",Size(CPpermlag),
      " COMPATIBLE_PAIR_GENERATORS=",Length(cppairslag),"\n");
Print("IDENTITY_ACTION_RECONSTRUCTION_OK=",identityoklag,
      " GENERATOR_ACTIONS_BIJECTIVE=",bijectivelag,
      " H2_CLASSES=",Length(coeffslag),
      " COMPATIBLE_PAIR_ORBITS=",Length(orbitrepslag),
      " ORBIT_SIZE_DISTRIBUTION=",Collected(orbitsizeslag),"\n");
# No QUIT: orbit parent screens reuse orbitrepslag.
