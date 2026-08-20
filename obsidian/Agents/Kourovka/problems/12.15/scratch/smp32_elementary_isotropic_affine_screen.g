# Exact affine-pairing screen for the only remaining non-Lagrangian case:
# A=C2^3 and Q=H/A an SMP order-32 subgroup of A^* semidirect Aut(A).
# For each subgroup embedding, test whether some 1<>a in A is alpha-regular:
# every affine element whose linear part fixes a has character part vanishing
# on a.  Such an a contradicts nondegeneracy of the original cocycle.

A := ElementaryAbelianGroup(8);
abasis := Pcgs(A);
AutA := AutomorphismGroup(A);
autgens := GeneratorsOfGroup(AutA);

V := ElementaryAbelianGroup(8);
vbasis := Pcgs(V);
dualauts := [];
for aut in autgens do
  M := List(abasis,a->ExponentsOfPcElement(abasis,Image(aut,a))*One(GF(2)));
  N := TransposedMat(M^-1);
  imgs := List(N,row->PcElementByExponents(vbasis,List(row,IntFFE)));
  Add(dualauts,GroupHomomorphismByImages(V,V,vbasis,imgs));
od;
DualAut := Group(dualauts);
acthom := GroupHomomorphismByImages(AutA,DualAut,autgens,dualauts);
P := SemidirectProduct(AutA,acthom,V);
embAut := Embedding(P,1);
embV := Embedding(P,2);
proj := Projection(P);

Print("GAP_VERSION=",GAPInfo.Version,
      " AFFINE_DUAL_ORDER=",Size(P),
      " AUT_ORDER=",Size(AutA)," V_ORDER=",Size(V),"\n");

targetids := [27,49];
casecount := 0;
for cc in ConjugacyClassesSubgroups(P) do
  S := Representative(cc);
  if Size(S)=32 and IdGroup(S)[2] in targetids then
    casecount := casecount+1;
    regularwitness := fail;
    for a in Elements(A) do
      if not IsOne(a) then
        avec := ExponentsOfPcElement(abasis,a);
        isregular := true;
        for s in Elements(S) do
          aut := Image(proj,s);
          if Image(aut,a)=a then
            residual := PreImagesRepresentative(embV,
                          Image(embAut,aut)^-1*s);
            vvec := ExponentsOfPcElement(vbasis,residual);
            if Sum([1..3],i->avec[i]*vvec[i]) mod 2 = 1 then
              isregular := false;
              break;
            fi;
          fi;
        od;
        if isregular then regularwitness:=avec; break; fi;
      fi;
    od;
    h2dim := fail;
    moduleSMP := true;
    moduleSMPwitness := fail;
    linimage := Image(proj,S);
    seenclosures := [];
    seenreps := [];
    for a in Elements(A) do
      if ForAll(seenreps,r->not a in Orbit(linimage,r,
            function(x,g) return Image(g,x); end)) then
        aorb := Orbit(linimage,a,function(x,g) return Image(g,x); end);
        acl := Subgroup(A,aorb);
        if acl in seenclosures then
          moduleSMP := false;
          moduleSMPwitness := [
            ExponentsOfPcElement(abasis,seenreps[Position(seenclosures,acl)]),
            ExponentsOfPcElement(abasis,a)];
          break;
        fi;
        Add(seenclosures,acl); Add(seenreps,a);
      fi;
    od;
    if regularwitness=fail then
      siso := IsomorphismPcGroup(S);
      Spc := Image(siso);
      smats := [];
      for spcg in GeneratorsOfGroup(Spc) do
        sg := PreImagesRepresentative(siso,spcg);
        saut := Image(proj,sg);
        Add(smats,List(abasis,a->
          ExponentsOfPcElement(abasis,Image(saut,a))*One(GF(2))));
      od;
      smodule := GModuleByMats(smats,GF(2));
      scoh := TwoCohomology(Spc,smodule);
      h2dim := Length(BasisVectors(Basis(Image(scoh.cohom))));
    fi;
    Print("CASE=",casecount,
          " Q_ID=",IdGroup(S)[2],
          " Q_STRUCTURE=",StructureDescription(S),
          " INTERSECTION_V_ORDER=",Size(Intersection(S,Image(embV,V))),
          " ALPHA_REGULAR_A_VECTOR=",regularwitness,
          " PASSES_A_NONDEGENERACY=",regularwitness=fail,
          " RESTRICTED_SMP_ON_A=",moduleSMP,
          " RESTRICTED_SMP_WITNESS=",moduleSMPwitness,
          " EXTENSION_H2_DIM=",h2dim,"\n");
  fi;
od;
Print("TOTAL_TARGET_EMBEDDING_CLASSES=",casecount,"\n");
QUIT;
