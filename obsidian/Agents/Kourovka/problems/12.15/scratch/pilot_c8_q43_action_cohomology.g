# Cheap coefficient-safe pilot for the full-dual A=C8, Q=[32,43] branch.
# The affine group is the full dual holomorph C8 : Aut(C8).  Recover the
# induced action on the original C8 and compute H^2(Q,C8) as a Z-lattice
# quotient via Polycyclic's TwoCohomologyModCR; no F_2 replacement is used.

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

A:=CyclicGroup(IsPcGroup,8); ag:=GeneratorsOfGroup(A)[1];
AutA:=AutomorphismGroup(A); autgens:=GeneratorsOfGroup(AutA);
V:=CyclicGroup(IsPcGroup,8); vg:=GeneratorsOfGroup(V)[1];
dualauts:=List(autgens,aut->GroupHomomorphismByImages(
  V,V,[vg],[vg^InverseUnitMod8(UnitOnC8(aut,ag))]));
DualAut:=Group(dualauts);
acthom:=GroupHomomorphismByImages(AutA,DualAut,autgens,dualauts);
P:=SemidirectProduct(AutA,acthom,V);
proj:=Projection(P); embV:=Embedding(P,2);

Print("GAP_VERSION=",GAPInfo.Version,
      " POLYCYCLIC_VERSION=",PackageInfo("polycyclic")[1].Version,"\n");
Print("A_STRUCTURE=",StructureDescription(A),
      " AUT_A_ORDER=",Size(AutA),
      " DUAL_HOLOMORPH_ORDER=",Size(P),
      " DUAL_HOLOMORPH_ID=",IdGroup(P),
      " TRANSLATION_KERNEL_ORDER=",Size(Image(embV,V)),"\n");

piso:=IsomorphismPcpGroup(P); U:=Image(piso); upcp:=Pcp(U); ugens:=Igs(U);
mats:=[]; actionunits:=[];
for ug in ugens do
  pre:=PreImagesRepresentative(piso,ug);
  paut:=Image(proj,pre);
  unit:=UnitOnC8(paut,ag);
  Add(actionunits,unit);
  Add(mats,C8PermutationMatrix(unit));
od;
Print("PCP_LENGTH=",Length(upcp),
      " PCP_RELATIVE_ORDERS=",RelativeOrdersOfPcp(upcp),
      " ACTION_UNITS_MOD8=",actionunits,"\n");

# F=Z^8 has basis e_0,...,e_7 and maps to C8 by e_j |-> j mod 8.
# The following full lattice is its kernel: e_0, 8e_1, e_j-j e_1.
lat:=IdentityMat(8); lat[2]:=8*lat[2];
for j in [3..8] do lat[j][2]:=-(j-1); od;
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
QUIT;
