# Exact compatible-pair action on H^2(Q,C4xC2) for the surviving Q49 action.
# The installed finite-field helper does not cover this non-elementary module,
# so this reconstructs the same action from marked extension relators.

Read("Agents/Kourovka/problems/12.15/scratch/pilot_c4c2_q49_full_action_cohomology.g");

TailVectorModQ49 := function(v)
  local coords,out,i,j,s4,s2;
  coords:=List(aelts49,x->CoordC4C2Q49(x,a4q49,a2q49)); out:=[];
  for i in [1..Length(C49rec.enumrels)] do
    s4:=0; s2:=0;
    for j in [1..Length(aelts49)] do
      s4:=s4+coords[j][1]*v[(i-1)*Length(aelts49)+j];
      s2:=s2+coords[j][2]*v[(i-1)*Length(aelts49)+j];
    od;
    Add(out,[s4 mod 4,s2 mod 2]);
  od;
  return out;
end;

ExtensionC4C2Q49 := function(C,tails,actcoords)
  local n,coll,rels,i,e,r,o,x,extgrp;
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
  SetRelativeOrder(coll,n+1,4); SetRelativeOrder(coll,n+2,2);
  for i in [1..n] do
    x:=Concatenation(List([1..n],j->0),actcoords[i][1]);
    SetConjugate(coll,n+1,i,ObjByExponents(coll,x));
    x:=Concatenation(List([1..n],j->0),actcoords[i][2]);
    SetConjugate(coll,n+2,i,ObjByExponents(coll,x));
  od;
  UpdatePolycyclicCollector(coll); extgrp:=PcpGroupByCollectorNC(coll);
  extgrp!.markedmoduleQ49:=Subgroup(extgrp,Igs(extgrp){[n+1,n+2]});
  return extgrp;
end;

ModuleCoordsQ49 := function(x,m4,m2)
  local i,j;
  for i in [0..3] do
    for j in [0..1] do if x=m4^i*m2^j then return [i,j]; fi; od;
  od;
  Error("tail escaped marked C4xC2 module");
end;

CocycleToFactorQ49 := function(coc)
  local elm,i;
  elm:=PcpSolutionIntMat(coh49.gcc,coc);
  if elm=fail then Error("transformed tail is not in cocycle lattice"); fi;
  elm:=elm*coh49.factor.imgs;
  for i in [1..Length(elm)] do elm[i]:=elm[i] mod coh49.factor.rels[i]; od;
  return elm;
end;

PairImageOfCocycleQ49 := function(coc,alpha,beta)
  local tails,extgrp,egs,n,base,m4,m2,ainv,newlifts,invlifts,rels,
        out,e,i,j,lhs,rhs,t,tc,ta,ac,slot;
  tails:=TailVectorModQ49(coc);
  extgrp:=ExtensionC4C2Q49(C49rec,tails,actioncoords49);
  egs:=Igs(extgrp); n:=Length(ugens49); base:=egs{[1..n]};
  m4:=egs[n+1]; m2:=egs[n+2]; ainv:=InverseGeneralMapping(alpha);
  newlifts:=List(ugens49,q->
    MappedVector(ExponentsByPcp(upcp49,Image(ainv,q)),base));
  invlifts:=List(newlifts,x->x^-1);
  rels:=RelativeOrdersOfPcp(C49rec.factor); out:=[];
  for e in C49rec.enumrels do
    i:=e[1]; j:=e[2];
    rhs:=MappedWordCR(C49rec.relators[i][j],newlifts,invlifts);
    if i=j then
      lhs:=newlifts[i]^rels[i];
    elif j<i then
      lhs:=newlifts[i]^newlifts[j];
    else
      lhs:=newlifts[i]^(newlifts[j-i]^-1);
    fi;
    t:=rhs^-1*lhs;
    if not t in extgrp!.markedmoduleQ49 then Error("relation tail escaped module"); fi;
    tc:=ModuleCoordsQ49(t,m4,m2);
    ta:=Image(beta,a4q49^tc[1]*a2q49^tc[2]);
    ac:=CoordC4C2Q49(ta,a4q49,a2q49);
    slot:=List(aelts49,x->0); slot[pos4q49]:=ac[1]; slot[pos2q49]:=ac[2];
    Append(out,slot);
  od;
  return CocycleToFactorQ49(out);
end;

ApplyFactorMapQ49 := function(v,rows)
  local out,i,j;
  out:=List(coh49.factor.rels,x->0);
  for i in [1..Length(v)] do
    for j in [1..Length(out)] do out[j]:=out[j]+v[i]*rows[i][j]; od;
  od;
  for j in [1..Length(out)] do out[j]:=out[j] mod coh49.factor.rels[j]; od;
  return out;
end;

MixedIndexQ49 := function(v,rels)
  local z,i;
  z:=0; for i in [1..Length(v)] do z:=z*rels[i]+v[i]; od;
  return z+1;
end;

# Enumerate all compatible automorphism pairs exactly.
rhoimggrp49:=Group(actionauts49);
rhohom49:=GroupHomomorphismByImages(U49,rhoimggrp49,ugens49,actionauts49);
if not IsGroupHomomorphism(rhohom49) then Error("Q49 action homomorphism failed"); fi;
AutQ49:=AutomorphismGroup(U49); autqelts49:=Elements(AutQ49);
autaelts49:=Elements(AutA49); compatible49:=[]; pairperms49:=[];
qelts49:=Elements(U49);
for alpha49 in autqelts49 do
  for beta49 in autaelts49 do
    compatok49:=true;
    for qg49 in ugens49 do
      for aa49 in [a4q49,a2q49] do
        if Image(beta49,Image(Image(rhohom49,qg49),aa49))<>
           Image(Image(rhohom49,Image(alpha49,qg49)),Image(beta49,aa49)) then
          compatok49:=false; break;
        fi;
      od;
      if not compatok49 then break; fi;
    od;
    if compatok49 then
      Add(compatible49,[alpha49,beta49]);
      pimgs49:=Concatenation(
        List(qelts49,q49->Position(qelts49,Image(alpha49,q49))),
        List(aelts49,aa49->Length(qelts49)+Position(aelts49,Image(beta49,aa49))));
      Add(pairperms49,PermList(pimgs49));
    fi;
  od;
od;
CPperm49:=Group(pairperms49); cppermgens49:=SmallGeneratingSet(CPperm49);
cppairs49:=List(cppermgens49,p49->compatible49[Position(pairperms49,p49)]);

# Identity is a necessary reconstruction check before any orbit calculation.
idrows49:=List(coh49.factor.prei,c49->
  PairImageOfCocycleQ49(c49,One(AutQ49),One(AutA49)));
identityok49:=idrows49=IdentityMat(Length(coh49.factor.rels));

actionrows49:=[];
for pair49 in cppairs49 do
  Add(actionrows49,List(coh49.factor.prei,c49->
    PairImageOfCocycleQ49(c49,pair49[1],pair49[2])));
od;
coeffs49:=ExponentsByRels(coh49.factor.rels);
actionbijective49:=ForAll(actionrows49,rows49->
  Length(Set(List(coeffs49,v49->ApplyFactorMapQ49(v49,rows49))))=Length(coeffs49));

seen49:=BlistList([1..Length(coeffs49)],[]); orbitreps49:=[]; orbitsizes49:=[];
for v49 in coeffs49 do
  key49:=MixedIndexQ49(v49,coh49.factor.rels);
  if not seen49[key49] then
    Add(orbitreps49,v49); queue49:=[v49]; seen49[key49]:=true; head49:=1;
    while head49<=Length(queue49) do
      w49:=queue49[head49]; head49:=head49+1;
      for rows49 in actionrows49 do
        im49:=ApplyFactorMapQ49(w49,rows49);
        ikey49:=MixedIndexQ49(im49,coh49.factor.rels);
        if not seen49[ikey49] then seen49[ikey49]:=true; Add(queue49,im49); fi;
      od;
    od;
    Add(orbitsizes49,Length(queue49));
  fi;
od;

Print("AUT_Q_ORDER=",Size(AutQ49)," AUT_A_ORDER=",Size(AutA49),
      " COMPATIBLE_PAIRS_ENUMERATED=",Length(compatible49),
      " COMPATIBLE_PAIR_GROUP_ORDER=",Size(CPperm49),
      " COMPATIBLE_PAIR_GENERATORS=",Length(cppairs49),"\n");
Print("IDENTITY_ACTION_RECONSTRUCTION_OK=",identityok49,
      " GENERATOR_ACTIONS_BIJECTIVE=",actionbijective49,
      " H2_CLASSES=",Length(coeffs49),
      " COMPATIBLE_PAIR_ORBITS=",Length(orbitreps49),
      " ORBIT_SIZE_DISTRIBUTION=",Collected(orbitsizes49),"\n");
# No QUIT: the parent screen reuses orbitreps49.
