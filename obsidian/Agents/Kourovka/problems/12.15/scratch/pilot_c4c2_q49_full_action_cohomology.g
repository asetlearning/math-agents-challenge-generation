# Coefficient-safe classification and cohomology pilot for every affine
# A=C4xC2 subgroup of type Q=SmallGroup(32,49), selecting only actions with no
# alpha-regular element of A.

if LoadPackage("polycyclic")<>true then Error("Polycyclic unavailable"); fi;

CoordC4C2Q49 := function(x,a4,a2)
  local i,j;
  for i in [0..3] do
    for j in [0..1] do
      if x=a4^i*a2^j then return [i,j]; fi;
    od;
  od;
  Error("element has no C4xC2 coordinates");
end;

PermutationMatrixQ49 := function(aut,elts)
  local M,i;
  M:=NullMat(Length(elts),Length(elts));
  for i in [1..Length(elts)] do
    M[i][Position(elts,Image(aut,elts[i]))]:=1;
  od;
  return M;
end;

A49:=SmallGroup(8,2); aelts49:=Elements(A49);
a4q49:=First(aelts49,x->Order(x)=4); sub4q49:=Subgroup(A49,[a4q49]);
a2q49:=First(aelts49,x->Order(x)=2 and not x in sub4q49);

accs49:=ConjugacyClasses(A49); areps49:=List(accs49,Representative);
achars49:=Irr(A49); acharvals49:=List(achars49,chi->List(chi));
an49:=Length(achars49); transperms49:=[];
for k49 in [1..an49] do
  imgs49:=[];
  for i49 in [1..an49] do
    vals49:=List([1..an49],j49->acharvals49[i49][j49]*acharvals49[k49][j49]);
    Add(imgs49,Position(acharvals49,vals49));
  od;
  Add(transperms49,PermList(imgs49));
od;
Trans49:=Group(transperms49);
AutA49:=AutomorphismGroup(A49); autgens49:=GeneratorsOfGroup(AutA49);
autperms49:=[];
for aut49 in autgens49 do
  imgs49:=[]; autinv49:=InverseGeneralMapping(aut49);
  for i49 in [1..an49] do
    vals49:=List(areps49,x49->
      acharvals49[i49][Position(areps49,Image(autinv49,x49))]);
    Add(imgs49,Position(acharvals49,vals49));
  od;
  Add(autperms49,PermList(imgs49));
od;
Lin49:=Group(autperms49);
autpermhom49:=GroupHomomorphismByImages(AutA49,Lin49,autgens49,autperms49);
Hol49:=Group(Concatenation(GeneratorsOfGroup(Trans49),autperms49));

qclasses49:=Filtered(ConjugacyClassesSubgroups(Hol49),cc49->
  Size(Representative(cc49))=32 and IdGroup(Representative(cc49))=[32,49]);
qclasswitnesses49:=[]; passqclasses49:=[];
for cc49 in qclasses49 do
  Scand49:=Representative(cc49); regularwitness49:=fail;
  for aidx49 in [2..an49] do
    isregular49:=true;
    for se49 in Elements(Scand49) do
      lambdaidx49:=1^se49;
      lin49:=se49*transperms49[lambdaidx49]^-1;
      fixes49:=ForAll([1..an49],i49->
        acharvals49[i49^lin49][aidx49]=acharvals49[i49][aidx49]);
      if fixes49 and acharvals49[lambdaidx49][aidx49]<>1 then
        isregular49:=false; break;
      fi;
    od;
    if isregular49 then regularwitness49:=areps49[aidx49]; break; fi;
  od;
  Add(qclasswitnesses49,regularwitness49);
  if regularwitness49=fail then Add(passqclasses49,cc49); fi;
od;
if Length(passqclasses49)<>1 then
  Error("expected exactly one nondegenerate-on-A Q49 affine class");
fi;
S49:=Representative(passqclasses49[1]);

siso49:=IsomorphismPcpGroup(S49); U49:=Image(siso49); upcp49:=Pcp(U49);
ugens49:=Igs(U49); actionauts49:=[]; actioncoords49:=[]; mats49:=[];
for ug49 in ugens49 do
  sg49:=PreImagesRepresentative(siso49,ug49); lambdaidx49:=1^sg49;
  lin49:=sg49*transperms49[lambdaidx49]^-1;
  if not lin49 in Lin49 then Error("affine element did not split"); fi;
  aut49:=PreImagesRepresentative(autpermhom49,lin49);
  Add(actionauts49,aut49);
  Add(actioncoords49,
    [CoordC4C2Q49(Image(aut49,a4q49),a4q49,a2q49),
     CoordC4C2Q49(Image(aut49,a2q49),a4q49,a2q49)]);
  Add(mats49,PermutationMatrixQ49(aut49,aelts49));
od;

# Exact full module as the quotient of Z[A] by the kernel lattice of Z[A]->A.
pos4q49:=Position(aelts49,a4q49); pos2q49:=Position(aelts49,a2q49);
lat49:=[];
for i49 in [1..Length(aelts49)] do
  coord49:=CoordC4C2Q49(aelts49[i49],a4q49,a2q49);
  row49:=List(aelts49,x49->0);
  if i49=pos4q49 then
    row49[i49]:=4;
  elif i49=pos2q49 then
    row49[i49]:=2;
  else
    row49[i49]:=1;
    row49[pos4q49]:=row49[pos4q49]-coord49[1];
    row49[pos2q49]:=row49[pos2q49]-coord49[2];
  fi;
  Add(lat49,row49);
od;

Print("GAP_VERSION=",GAPInfo.Version,
      " POLYCYCLIC_VERSION=",PackageInfo("polycyclic")[1].Version,"\n");
Print("A_STRUCTURE=",StructureDescription(A49)," HOL_ORDER=",Size(Hol49),
      " Q49_AFFINE_CLASSES=",Length(qclasses49),
      " Q49_INTERSECTION_ORDERS=",
      List(qclasses49,cc49->Size(Intersection(Representative(cc49),Trans49))),
      " ALPHA_REGULAR_WITNESSES=",qclasswitnesses49,
      " SURVIVING_TARGET_CLASSES=",Length(passqclasses49),
      " Q_ID=",IdGroup(S49),
      " DUAL_INTERSECTION_ORDER=",Size(Intersection(S49,Trans49)),"\n");
Print("PCP_LENGTH=",Length(upcp49),
      " PCP_RELATIVE_ORDERS=",RelativeOrdersOfPcp(upcp49),
      " ACTION_IMAGES_OF_A4_A2=",actioncoords49,"\n");
Print("LATTICE_DETERMINANT=",AbsInt(DeterminantMat(lat49)),
      " LATTICE_ACTION_INVARIANT=",
      ForAll(mats49,M49->ForAll(lat49,r49->
        ForAll(SolutionMat(lat49,r49*M49),IsInt))),"\n");

C49rec:=CRRecordByMats(U49,mats49);
coh49:=TwoCohomologyModCR(C49rec,lat49);
Print("H2_INVARIANTS=",coh49.factor.rels,
      " H2_ORDER=",Product(coh49.factor.rels),
      " COCYCLE_BASIS_LENGTH=",Length(coh49.gcc),
      " COBOUNDARY_BASIS_LENGTH=",Length(coh49.gcb),
      " TAIL_SLOTS=",Length(C49rec.enumrels),
      " TAIL_VECTOR_LENGTH=",8*Length(C49rec.enumrels),"\n");
# No QUIT: screen wrappers reuse this exact setup.
