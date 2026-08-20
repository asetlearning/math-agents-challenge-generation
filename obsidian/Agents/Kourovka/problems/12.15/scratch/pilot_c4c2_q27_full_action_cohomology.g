# Coefficient-safe pilot for the marked full-dual A=C4xC2,
# Q=SmallGroup(32,27), |Q cap A-dual|=8 action.

if LoadPackage("polycyclic")<>true then Error("Polycyclic unavailable"); fi;

CoordC4C2 := function(x,a4,a2)
  local i,j;
  for i in [0..3] do
    for j in [0..1] do
      if x=a4^i*a2^j then return [i,j]; fi;
    od;
  od;
  Error("element has no C4xC2 coordinates");
end;

PermutationMatrixOnElements := function(aut,elts)
  local M,i;
  M:=NullMat(Length(elts),Length(elts));
  for i in [1..Length(elts)] do
    M[i][Position(elts,Image(aut,elts[i]))]:=1;
  od;
  return M;
end;

A:=SmallGroup(8,2); elts:=Elements(A);
a4:=First(elts,x->Order(x)=4); sub4:=Subgroup(A,[a4]);
a2:=First(elts,x->Order(x)=2 and not x in sub4);

# Build the full complex dual and the contragredient automorphism action
# exactly as in the corrected full-dual affine screen.
ccs:=ConjugacyClasses(A); reps:=List(ccs,Representative);
chars:=Irr(A); charvals:=List(chars,chi->List(chi)); n:=Length(chars);
transperms:=[];
for k in [1..n] do
  imgs:=[];
  for i in [1..n] do
    vals:=List([1..n],j->charvals[i][j]*charvals[k][j]);
    Add(imgs,Position(charvals,vals));
  od;
  Add(transperms,PermList(imgs));
od;
Trans:=Group(transperms);
AutA:=AutomorphismGroup(A); autgens:=GeneratorsOfGroup(AutA); autperms:=[];
for aut in autgens do
  imgs:=[]; autinv:=InverseGeneralMapping(aut);
  for i in [1..n] do
    vals:=List(reps,a->charvals[i][Position(reps,Image(autinv,a))]);
    Add(imgs,Position(charvals,vals));
  od;
  Add(autperms,PermList(imgs));
od;
Lin:=Group(autperms);
autpermhom:=GroupHomomorphismByImages(AutA,Lin,autgens,autperms);
Hol:=Group(Concatenation(GeneratorsOfGroup(Trans),autperms));

qclasses:=Filtered(ConjugacyClassesSubgroups(Hol),cc->
  Size(Representative(cc))=32 and IdGroup(Representative(cc))=[32,27] and
  Size(Intersection(Representative(cc),Trans))=8);
if Length(qclasses)<>1 then Error("expected unique full-dual Q27 class"); fi;
S:=Representative(qclasses[1]);

siso:=IsomorphismPcpGroup(S); U:=Image(siso); upcp:=Pcp(U); ugens:=Igs(U);
actionauts:=[]; actioncoords:=[]; mats:=[];
for ug in ugens do
  sg:=PreImagesRepresentative(siso,ug);
  lambdaidx:=1^sg;
  lin:=sg*transperms[lambdaidx]^-1;
  if not lin in Lin then Error("affine element did not split into dual and linear parts"); fi;
  aut:=PreImagesRepresentative(autpermhom,lin);
  Add(actionauts,aut);
  Add(actioncoords,[CoordC4C2(Image(aut,a4),a4,a2),
                    CoordC4C2(Image(aut,a2),a4,a2)]);
  Add(mats,PermutationMatrixOnElements(aut,elts));
od;

# F=Z[A] maps e_x to x.  Give a full basis of the kernel lattice using
# a4 and a2 as quotient generators.
pos4:=Position(elts,a4); pos2:=Position(elts,a2); lat:=[];
for i in [1..Length(elts)] do
  coord:=CoordC4C2(elts[i],a4,a2); row:=List(elts,x->0);
  if i=pos4 then
    row[i]:=4;
  elif i=pos2 then
    row[i]:=2;
  else
    row[i]:=1; row[pos4]:=row[pos4]-coord[1];
    row[pos2]:=row[pos2]-coord[2];
  fi;
  Add(lat,row);
od;

Print("GAP_VERSION=",GAPInfo.Version,
      " POLYCYCLIC_VERSION=",PackageInfo("polycyclic")[1].Version,"\n");
Print("A_STRUCTURE=",StructureDescription(A),
      " HOL_ORDER=",Size(Hol)," TARGET_CLASSES=",Length(qclasses),
      " Q_ID=",IdGroup(S),
      " DUAL_INTERSECTION_ORDER=",Size(Intersection(S,Trans)),"\n");
Print("PCP_LENGTH=",Length(upcp),
      " PCP_RELATIVE_ORDERS=",RelativeOrdersOfPcp(upcp),
      " ACTION_IMAGES_OF_A4_A2=",actioncoords,"\n");
Print("LATTICE_DETERMINANT=",AbsInt(DeterminantMat(lat)),
      " LATTICE_ACTION_INVARIANT=",
      ForAll(mats,M->ForAll(lat,r->ForAll(SolutionMat(lat,r*M),IsInt))),"\n");

C:=CRRecordByMats(U,mats);
coh:=TwoCohomologyModCR(C,lat);
Print("H2_INVARIANTS=",coh.factor.rels,
      " H2_ORDER=",Product(coh.factor.rels),
      " COCYCLE_BASIS_LENGTH=",Length(coh.gcc),
      " COBOUNDARY_BASIS_LENGTH=",Length(coh.gcb),
      " TAIL_SLOTS=",Length(C.enumrels),
      " TAIL_VECTOR_LENGTH=",8*Length(C.enumrels),"\n");
# No terminal QUIT: the file can also supply this exact setup to bounded
# extension-screen wrappers.  Direct GAP invocation exits at end of input.
