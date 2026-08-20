# Coefficient-safe action and H^2 pilot for the exact normal-Lagrangian type
# L=C8xC2, Q=SmallGroup(16,11).  Every Hol(L^*)-conjugacy class of regular
# affine Q is included.  The Q-action on L is reconstructed as the exact
# contragredient of its linear action on L^*.

if LoadPackage("polycyclic")<>true then Error("Polycyclic unavailable"); fi;

CoordC8C2Lag := function(x,b8,b2)
  local i,j;
  for i in [0..7] do
    for j in [0..1] do
      if x=b8^i*b2^j then return [i,j]; fi;
    od;
  od;
  Error("element has no C8xC2 coordinates");
end;

PairC8C2Lag := function(k,a,k8,k2,l8,l2)
  local kc,ac;
  kc:=CoordC8C2Lag(k,k8,k2); ac:=CoordC8C2Lag(a,l8,l2);
  return E(8)^(kc[1]*ac[1]+4*kc[2]*ac[2]);
end;

DualBackAutC8C2Lag := function(phi,K,L,k8,k2,l8,l2,kelts,lelts)
  local limgs,a,y,theta,k;
  limgs:=[];
  for a in [l8,l2] do
    y:=First(lelts,z->ForAll(kelts,k->
      PairC8C2Lag(Image(phi,k),z,k8,k2,l8,l2)=
      PairC8C2Lag(k,a,k8,k2,l8,l2)));
    if y=fail then Error("dual image does not exist"); fi;
    Add(limgs,y);
  od;
  theta:=GroupHomomorphismByImages(L,L,[l8,l2],limgs);
  if theta=fail or not IsBijective(theta) then Error("dual map is not an automorphism"); fi;
  if not ForAll(kelts,k->ForAll(lelts,a->
       PairC8C2Lag(Image(phi,k),Image(theta,a),k8,k2,l8,l2)=
       PairC8C2Lag(k,a,k8,k2,l8,l2))) then
    Error("contragredient pairing validation failed");
  fi;
  return theta;
end;

PermutationMatrixLag := function(aut,elts)
  local M,i;
  M:=NullMat(Length(elts),Length(elts));
  for i in [1..Length(elts)] do
    M[i][Position(elts,Image(aut,elts[i]))]:=1;
  od;
  return M;
end;

RestrictedSMPLag := function(L,actgrp)
  local remaining,orbits,modules,reps,x,orb,sub,p;
  remaining:=ShallowCopy(Elements(L)); orbits:=[]; modules:=[]; reps:=[];
  while Length(remaining)>0 do
    x:=remaining[1];
    orb:=Orbit(actgrp,x,function(y,g) return Image(g,y); end);
    SubtractSet(remaining,orb);
    sub:=Subgroup(L,orb);
    if sub in modules then
      p:=Position(modules,sub);
      return [false,x,reps[p],Size(sub),
        List(Pcgs(sub),z->CoordC8C2Lag(z,l8lag,l2lag))];
    fi;
    Add(orbits,orb); Add(modules,sub); Add(reps,x);
  od;
  return [true,Length(orbits),List(modules,Size)];
end;

Klag:=SmallGroup(16,5); keltslag:=Elements(Klag);
k8lag:=First(keltslag,x->Order(x)=8); k2lag:=First(keltslag,x->
  Order(x)=2 and not x in Subgroup(Klag,[k8lag]));
Llag:=SmallGroup(16,5); leltslag:=Elements(Llag);
l8lag:=First(leltslag,x->Order(x)=8); l2lag:=First(leltslag,x->
  Order(x)=2 and not x in Subgroup(Llag,[l8lag]));

transpermslag:=List(keltslag,k->PermList(List(keltslag,x->
  Position(keltslag,x*k))));
Translag:=Group(transpermslag);
AutKlag:=AutomorphismGroup(Klag); autgenslag:=GeneratorsOfGroup(AutKlag);
autpermslag:=List(autgenslag,a->PermList(List(keltslag,x->
  Position(keltslag,Image(a,x)))));
AutPermlag:=Group(autpermslag);
autpermhomlag:=GroupHomomorphismByImages(AutKlag,AutPermlag,
  autgenslag,autpermslag);
Hollag:=Group(Concatenation(GeneratorsOfGroup(Translag),autpermslag));

targetclasseslag:=Filtered(ConjugacyClassesSubgroups(Hollag),cc->
  Size(Representative(cc))=16 and
  IsTransitive(Representative(cc),[1..16]) and
  IdGroup(Representative(cc))=[16,11]);
if Length(targetclasseslag)<>5 then Error("expected five regular Q11 classes"); fi;

# Exact index-16 permutation-lattice presentation of L=C8xC2.
pos8lag:=Position(leltslag,l8lag); pos2lag:=Position(leltslag,l2lag);
latlag:=[];
for ilag in [1..Length(leltslag)] do
  coordlag:=CoordC8C2Lag(leltslag[ilag],l8lag,l2lag);
  rowlag:=List(leltslag,x->0);
  if ilag=pos8lag then
    rowlag[ilag]:=8;
  elif ilag=pos2lag then
    rowlag[ilag]:=2;
  else
    rowlag[ilag]:=1;
    rowlag[pos8lag]:=rowlag[pos8lag]-coordlag[1];
    rowlag[pos2lag]:=rowlag[pos2lag]-coordlag[2];
  fi;
  Add(latlag,rowlag);
od;

Print("GAP_VERSION=",GAPInfo.Version,
      " POLYCYCLIC_VERSION=",PackageInfo("polycyclic")[1].Version,
      " L_STRUCTURE=",StructureDescription(Llag),
      " Q_ID=[16,11] HOL_ORDER=",Size(Hollag),
      " REGULAR_AFFINE_CLASSES=",Length(targetclasseslag),
      " LATTICE_DETERMINANT=",AbsInt(DeterminantMat(latlag)),"\n");

lagrecords:=[];
if not IsBound(lagcasetargets) then
  lagcasetargets:=[1..Length(targetclasseslag)];
fi;
if not ForAll(lagcasetargets,i->i in [1..Length(targetclasseslag)]) then
  Error("lagcasetargets escaped classified affine cases");
fi;
for caselag in lagcasetargets do
  Ulag:=Representative(targetclasseslag[caselag]);
  uisolag:=IsomorphismPcpGroup(Ulag); Qlag:=Image(uisolag);
  upcplag:=Pcp(Qlag); ugenslag:=Igs(Qlag);
  actionautslag:=[]; actioncoordslag:=[]; matslag:=[];
  for uglag in ugenslag do
    afflag:=PreImagesRepresentative(uisolag,uglag);
    lambdaidxlag:=1^afflag;
    linlag:=afflag*transpermslag[lambdaidxlag]^-1;
    if not linlag in AutPermlag then Error("affine split failed"); fi;
    phiautlag:=PreImagesRepresentative(autpermhomlag,linlag);
    thetautlag:=DualBackAutC8C2Lag(phiautlag,Klag,Llag,
      k8lag,k2lag,l8lag,l2lag,keltslag,leltslag);
    Add(actionautslag,thetautlag);
    Add(actioncoordslag,
      [CoordC8C2Lag(Image(thetautlag,l8lag),l8lag,l2lag),
       CoordC8C2Lag(Image(thetautlag,l2lag),l8lag,l2lag)]);
    Add(matslag,PermutationMatrixLag(thetautlag,leltslag));
  od;
  actgrplag:=Group(actionautslag);
  rhohomlag:=GroupHomomorphismByImages(Qlag,actgrplag,ugenslag,actionautslag);
  if not IsGroupHomomorphism(rhohomlag) then Error("Q action failed"); fi;
  invariantlag:=ForAll(matslag,M->ForAll(latlag,r->
    SolutionMat(latlag,r*M)<>fail and ForAll(SolutionMat(latlag,r*M),IsInt)));
  if not invariantlag then Error("coefficient lattice is not invariant"); fi;
  restrictlag:=RestrictedSMPLag(Llag,actgrplag);
  if IsBound(skipcohomologylag) and skipcohomologylag=true then
    Creclag:=fail; cohlag:=fail;
  else
    Creclag:=CRRecordByMats(Qlag,matslag);
    cohlag:=TwoCohomologyModCR(Creclag,latlag);
  fi;
  Add(lagrecords,rec(case:=caselag,U:=Ulag,Q:=Qlag,upcp:=upcplag,
    ugens:=ugenslag,actionauts:=actionautslag,
    actioncoords:=actioncoordslag,mats:=matslag,Crec:=Creclag,coh:=cohlag,
    restrictedSMP:=restrictlag));
  Print("CASE=",caselag,
        " TRANSLATION_INTERSECTION_ORDER=",Size(Intersection(Ulag,Translag)),
        " Q_PCP_RELATIVE_ORDERS=",RelativeOrdersOfPcp(upcplag),
        " ACTION_IMAGES_OF_L8_L2=",actioncoordslag,
        " ACTION_IMAGE_ORDER=",Size(actgrplag),
        " RESTRICTED_SMP=",restrictlag);
  if cohlag=fail then
    Print(" H2_SKIPPED=true\n");
  else
    Print(" H2_INVARIANTS=",cohlag.factor.rels,
          " H2_ORDER=",Product(cohlag.factor.rels),
          " TAIL_SLOTS=",Length(Creclag.enumrels),
          " TAIL_VECTOR_LENGTH=",16*Length(Creclag.enumrels),"\n");
  fi;
od;
# No QUIT: bounded screen wrappers reuse lagrecords.
