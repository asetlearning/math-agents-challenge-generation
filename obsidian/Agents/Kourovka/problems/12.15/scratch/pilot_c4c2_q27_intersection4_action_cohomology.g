# Coefficient-safe pilot for the distinct marked affine action
# A=C4xC2, Q=SmallGroup(32,27), |Q cap A-dual|=4.

if LoadPackage("polycyclic")<>true then Error("Polycyclic unavailable"); fi;

CoordC4C2I4 := function(x,a4,a2)
  local i,j;
  for i in [0..3] do
    for j in [0..1] do
      if x=a4^i*a2^j then return [i,j]; fi;
    od;
  od;
  Error("element has no C4xC2 coordinates");
end;

PermutationMatrixOnElementsI4 := function(aut,elts)
  local M,i;
  M:=NullMat(Length(elts),Length(elts));
  for i in [1..Length(elts)] do
    M[i][Position(elts,Image(aut,elts[i]))]:=1;
  od;
  return M;
end;

A4mod:=SmallGroup(8,2); aelts4:=Elements(A4mod);
a4i4:=First(aelts4,x->Order(x)=4); sub4i4:=Subgroup(A4mod,[a4i4]);
a2i4:=First(aelts4,x->Order(x)=2 and not x in sub4i4);

# Construct the full complex character dual and its contragredient action.
accs4:=ConjugacyClasses(A4mod); areps4:=List(accs4,Representative);
achars4:=Irr(A4mod); acharvals4:=List(achars4,chi->List(chi)); an4:=Length(achars4);
transperms4:=[];
for k4 in [1..an4] do
  imgs4:=[];
  for i4 in [1..an4] do
    vals4:=List([1..an4],j4->acharvals4[i4][j4]*acharvals4[k4][j4]);
    Add(imgs4,Position(acharvals4,vals4));
  od;
  Add(transperms4,PermList(imgs4));
od;
Trans4:=Group(transperms4);
AutA4:=AutomorphismGroup(A4mod); autgens4:=GeneratorsOfGroup(AutA4);
autperms4:=[];
for aut4 in autgens4 do
  imgs4:=[]; autinv4:=InverseGeneralMapping(aut4);
  for i4 in [1..an4] do
    vals4:=List(areps4,x4->acharvals4[i4][Position(areps4,Image(autinv4,x4))]);
    Add(imgs4,Position(acharvals4,vals4));
  od;
  Add(autperms4,PermList(imgs4));
od;
Lin4:=Group(autperms4);
autpermhom4:=GroupHomomorphismByImages(AutA4,Lin4,autgens4,autperms4);
Hol4:=Group(Concatenation(GeneratorsOfGroup(Trans4),autperms4));

allq27classes4:=Filtered(ConjugacyClassesSubgroups(Hol4),cc4->
  Size(Representative(cc4))=32 and IdGroup(Representative(cc4))=[32,27]);
qclasses4:=Filtered(allq27classes4,cc4->
  Size(Intersection(Representative(cc4),Trans4))=4);
qclasswitnesses4:=[]; passqclasses4:=[];
for cc4 in qclasses4 do
  Scand4:=Representative(cc4); regularwitness4:=fail;
  for aidx4 in [2..an4] do
    isregular4:=true;
    for se4 in Elements(Scand4) do
      lambdaidx4:=1^se4; lin4:=se4*transperms4[lambdaidx4]^-1;
      fixes4:=ForAll([1..an4],i4->
        acharvals4[i4^lin4][aidx4]=acharvals4[i4][aidx4]);
      if fixes4 and acharvals4[lambdaidx4][aidx4]<>1 then
        isregular4:=false; break;
      fi;
    od;
    if isregular4 then regularwitness4:=areps4[aidx4]; break; fi;
  od;
  Add(qclasswitnesses4,regularwitness4);
  if regularwitness4=fail then Add(passqclasses4,cc4); fi;
od;
if Length(passqclasses4)<>1 then
  Error("expected unique nondegenerate-on-A Q27 affine class with intersection 4");
fi;
S4:=Representative(passqclasses4[1]);

siso4:=IsomorphismPcpGroup(S4); U4:=Image(siso4); upcp4:=Pcp(U4);
ugens4:=Igs(U4); actionauts4:=[]; actioncoords4:=[]; mats4:=[];
for ug4 in ugens4 do
  sg4:=PreImagesRepresentative(siso4,ug4); lambdaidx4:=1^sg4;
  lin4:=sg4*transperms4[lambdaidx4]^-1;
  if not lin4 in Lin4 then Error("affine element did not split"); fi;
  aut4:=PreImagesRepresentative(autpermhom4,lin4);
  Add(actionauts4,aut4);
  Add(actioncoords4,[CoordC4C2I4(Image(aut4,a4i4),a4i4,a2i4),
                       CoordC4C2I4(Image(aut4,a2i4),a4i4,a2i4)]);
  Add(mats4,PermutationMatrixOnElementsI4(aut4,aelts4));
od;

# Exact finite module: Z[A] modulo the kernel of Z[A] -> C4 x C2.
pos4i4:=Position(aelts4,a4i4); pos2i4:=Position(aelts4,a2i4); lat4:=[];
for i4 in [1..Length(aelts4)] do
  coord4:=CoordC4C2I4(aelts4[i4],a4i4,a2i4);
  row4:=List(aelts4,x4->0);
  if i4=pos4i4 then
    row4[i4]:=4;
  elif i4=pos2i4 then
    row4[i4]:=2;
  else
    row4[i4]:=1; row4[pos4i4]:=row4[pos4i4]-coord4[1];
    row4[pos2i4]:=row4[pos2i4]-coord4[2];
  fi;
  Add(lat4,row4);
od;

Print("GAP_VERSION=",GAPInfo.Version,
      " POLYCYCLIC_VERSION=",PackageInfo("polycyclic")[1].Version,"\n");
Print("A_STRUCTURE=",StructureDescription(A4mod)," HOL_ORDER=",Size(Hol4),
      " ALL_Q27_AFFINE_CLASSES=",Length(allq27classes4),
      " Q27_INTERSECTION_ORDERS=",
      List(allq27classes4,cc4->Size(Intersection(Representative(cc4),Trans4))),
      " INTERSECTION4_CLASSES=",Length(qclasses4),
      " INTERSECTION4_ALPHA_REGULAR_WITNESSES=",qclasswitnesses4,
      " SURVIVING_TARGET_CLASSES=",Length(passqclasses4)," Q_ID=",IdGroup(S4),
      " DUAL_INTERSECTION_ORDER=",Size(Intersection(S4,Trans4)),"\n");
Print("PCP_LENGTH=",Length(upcp4),
      " PCP_RELATIVE_ORDERS=",RelativeOrdersOfPcp(upcp4),
      " ACTION_IMAGES_OF_A4_A2=",actioncoords4,"\n");
Print("LATTICE_DETERMINANT=",AbsInt(DeterminantMat(lat4)),
      " LATTICE_ACTION_INVARIANT=",
      ForAll(mats4,M4->ForAll(lat4,r4->ForAll(SolutionMat(lat4,r4*M4),IsInt))),
      "\n");

C4rec:=CRRecordByMats(U4,mats4);
coh4:=TwoCohomologyModCR(C4rec,lat4);
Print("H2_INVARIANTS=",coh4.factor.rels,
      " H2_ORDER=",Product(coh4.factor.rels),
      " COCYCLE_BASIS_LENGTH=",Length(coh4.gcc),
      " COBOUNDARY_BASIS_LENGTH=",Length(coh4.gcb),
      " TAIL_SLOTS=",Length(C4rec.enumrels),
      " TAIL_VECTOR_LENGTH=",8*Length(C4rec.enumrels),"\n");
# No QUIT: extension-screen wrappers reuse this exact setup.
