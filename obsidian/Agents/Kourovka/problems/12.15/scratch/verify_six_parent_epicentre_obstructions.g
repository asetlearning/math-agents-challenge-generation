# Independent obstruction verifier for central C2 lifts of the six marked
# order-256 parents.  This does not enumerate the 1,024 H^2(Q,C4xC2)
# classes.  For each canonical SmallGroup it computes the epicentre from a
# pcp Schur extension, then independently reconstructs a basis of H^2(H,C2)
# and checks the displayed epicentral element against every element of H in
# every basis extension.

if not IsBound(targetids) then
  targetids:=[53357,53358,53373,53374,53384,53385];
fi;

LexicographicallyLeastNonidentityV := function(G,pcgs)
  local elts;
  elts:=Filtered(Elements(G),x->not IsOne(x));
  Sort(elts,function(x,y)
    return ExponentsOfPcElement(pcgs,x)<ExponentsOfPcElement(pcgs,y);
  end);
  if Length(elts)=0 then return fail; fi;
  return elts[1];
end;

for hid in targetids do
  H:=SmallGroup(256,hid); hpcgs:=Pcgs(H); n:=Length(hpcgs);

  # Route 1: the pcp Schur-extension definition of the epicentre.
  hiso:=IsomorphismPcpGroup(H); P:=Image(hiso);
  sepi:=SchurExtensionEpimorphism(P); SC:=Source(sepi);
  epicP:=Image(sepi,Centre(SC)); epicH:=PreImage(hiso,epicP);
  epicBuiltinP:=Epicentre(P);
  ez:=LexicographicallyLeastNonidentityV(epicH,hpcgs);
  testz:=hpcgs[8];

  Print("PARENT_ID=",hid,
        " PCP_SCHUR_SOURCE_FINITE=",IsFinite(SC),
        " SCHUR_KERNEL_INVARIANTS=",AbelianInvariants(Kernel(sepi)),
        " EPICENTRE_ORDER=",Size(epicH),
        " EPICENTRE_EQUALS_BUILTIN=",epicP=epicBuiltinP,
        " EPICENTRE_CENTRAL_IN_H=",IsSubgroup(Centre(H),epicH),"\n");
  if ez=fail then
    Print("FAIL_NO_NONIDENTITY_EPICENTRAL_ELEMENT\n");
  else
    Print("EPICENTRAL_ELEMENT_EXPONENTS=",
          ExponentsOfPcElement(hpcgs,ez),
          " IS_PC_GENERATOR_8=",n>=8 and ez=hpcgs[8],
          " ORDER=",Order(ez),
          " CENTRALIZER_ORDER=",Size(Centralizer(H,ez)),"\n");
  fi;
  Print("C2_TEST_ELEMENT_EXPONENTS=",
        ExponentsOfPcElement(hpcgs,testz),
        " ORDER=",Order(testz),
        " CENTRAL_IN_H=",testz in Centre(H),
        " CENTRALIZER_ORDER=",Size(Centralizer(H,testz)),"\n");

  # Route 2: reconstruct all 15 cohomology basis extensions.  Since the
  # commutator of lifts of commuting base elements is linear in the H^2
  # class, vanishing on the zero class and every basis class proves
  # vanishing on all 2^dim central extension classes.
  mats:=List(hpcgs,x->IdentityMat(1,GF(2)));
  modu:=GModuleByMats(mats,GF(2));
  coh:=TwoCohomology(H,modu); classspace:=Image(coh.cohom);
  classbasis:=BasisVectors(Basis(classspace)); basisexts:=[];
  basisreconstructionok:=true;
  for classv in classbasis do
    cocycle:=PreImagesRepresentative(coh.cohom,classv);
    extgrp:=ExtensionSQ(coh.collector,H,modu,cocycle);
    ker:=ModuleOfExtension(extgrp);
    if Size(extgrp)<>512 or Size(ker)<>2 or
       not IsSubgroup(Centre(extgrp),ker) or
       IsomorphismGroups(FactorGroup(extgrp,ker),H)=fail then
      basisreconstructionok:=false;
    fi;
    Add(basisexts,extgrp);
  od;

  nontrivialcommutators:=0; firstfailure:=fail;
  if not IsOne(testz) and testz in Centre(H) then
    for j in [1..Length(basisexts)] do
      extgrp:=basisexts[j]; epcgs:=Pcgs(extgrp); lifts:=epcgs{[1..n]};
      eez:=MappedPcElement(testz,hpcgs,lifts);
      for k in Elements(H) do
        ek:=MappedPcElement(k,hpcgs,lifts);
        if not IsOne(Comm(eez,ek)) then
          nontrivialcommutators:=nontrivialcommutators+1;
          if firstfailure=fail then
            firstfailure:=[j,ExponentsOfPcElement(hpcgs,k)];
          fi;
        fi;
      od;
    od;
  fi;

  Print("H2_DIM=",Length(classbasis),
        " H2_CLASSES=",Size(classspace),
        " BASIS_EXTENSIONS=",Length(basisexts),
        " BASIS_EXTENSION_RECONSTRUCTION_OK=",basisreconstructionok,
        " ELEMENTS_CHECKED_PER_BASIS=",Size(H),
        " NONTRIVIAL_BASIS_COMMUTATORS=",nontrivialcommutators,
        " FIRST_FAILURE=",firstfailure,"\n");
  Print("ALL_C2_EXTENSION_CLASSES_OBSTRUCTED=",
        not IsOne(testz) and testz in Centre(H) and
        basisreconstructionok and
        nontrivialcommutators=0,"\n");
od;
