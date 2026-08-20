# Exact linear screen for central extensions 1 -> C2 -> E -> H -> 1.
# A cohomology class passes NONDEGENERATE when no nonidentity element of H
# is alpha-regular, equivalently (E,C2) is a central Camina pair.  When
# requirederived=true it also requires E''=C2 at the linear-constraint level.
#
# Required globals: ordtarget, idtarget.  Optional: requirederived (default
# true), stopafterfirst (default true).

if not IsBound(ordtarget) or not IsBound(idtarget) then
  Error("bind ordtarget and idtarget before reading this file");
fi;
if not IsBound(requirederived) then requirederived := true; fi;
if not IsBound(stopafterfirst) then stopafterfirst := true; fi;
if not IsBound(noquit) then noquit := false; fi;

CommutatorRowC2 := function(h, k, exts, hpcgs, n)
  local row, E, epcgs, lifts, eh, ek, ker, z, c, j;
  row := [];
  for j in [1..Length(exts)] do
    E := exts[j];
    epcgs := Pcgs(E);
    lifts := epcgs{[1..n]};
    eh := MappedPcElement(h, hpcgs, lifts);
    ek := MappedPcElement(k, hpcgs, lifts);
    ker := ModuleOfExtension(E);
    z := GeneratorsOfGroup(ker)[1];
    c := Comm(eh, ek);
    if IsOne(c) then
      Add(row, Zero(GF(2)));
    elif c = z then
      Add(row, One(GF(2)));
    else
      Error("commutator of commuting base elements escaped C2 kernel");
    fi;
  od;
  return row;
end;

NonzeroRow := function(row)
  return ForAny(row, x -> not IsZero(x));
end;

PassesRowSpaces := function(coeff, spaces)
  local rows, row;
  for rows in spaces do
    if ForAll(rows, row -> IsZero(coeff * row)) then
      return false;
    fi;
  od;
  return true;
end;

HasSMPExactLocal := function(E)
  local closures, cc, x, N;
  closures := [];
  for cc in ConjugacyClasses(E) do
    x := Representative(cc);
    N := NormalClosure(E, Subgroup(E,[x]));
    if N in closures then return false; fi;
    Add(closures,N);
  od;
  return true;
end;

basegrp := SmallGroup(ordtarget,idtarget);
hpcgs := Pcgs(basegrp);
n := Length(hpcgs);
mats := List(hpcgs, x -> IdentityMat(1,GF(2)));
modu := GModuleByMats(mats,GF(2));
coh := TwoCohomology(basegrp,modu);
classspace := Image(coh.cohom);
classbasis := BasisVectors(Basis(classspace));
dim := Length(classbasis);
basisexts := [];
for classv in classbasis do
  cocycle := PreImagesRepresentative(coh.cohom,classv);
  Add(basisexts,ExtensionSQ(coh.collector,basegrp,modu,cocycle));
od;

Print("GAP_VERSION=", GAPInfo.Version,
      " BASE=[",ordtarget,",",idtarget,"]",
      " H2_DIM=",dim,
      " H2_CLASSES=",2^dim,
      " CONJUGACY_CLASSES=",NrConjugacyClasses(basegrp),"\n");

rowspaces := [];
zeroobstruction := false;
for cc in ConjugacyClasses(basegrp) do
  h := Representative(cc);
  if not IsOne(h) then
    mycen := Centralizer(basegrp,h);
    rows := [];
    for k in Pcgs(mycen) do
      row := CommutatorRowC2(h,k,basisexts,hpcgs,n);
      if NonzeroRow(row) then Add(rows,row); fi;
    od;
    if Length(rows)=0 then
      Print("UNIVERSALLY_ALPHA_REGULAR_CLASS_REP=",h,
            " ORDER=",Order(h)," CENTRALIZER_ORDER=",Size(mycen),"\n");
      zeroobstruction := true;
      break;
    fi;
    Add(rowspaces,BaseMat(rows));
  fi;
od;

derivedrows := [];
if requirederived and not zeroobstruction then
  dergrp := DerivedSubgroup(basegrp);
  dpcgs := Pcgs(dergrp);
  for i in [1..Length(dpcgs)] do
    for j in [1..i-1] do
      row := CommutatorRowC2(dpcgs[i],dpcgs[j],basisexts,hpcgs,n);
      if NonzeroRow(row) then Add(derivedrows,row); fi;
    od;
  od;
  if Length(derivedrows)>0 then derivedrows:=BaseMat(derivedrows); fi;
  Print("DERIVED_ORDER=",Size(dergrp),
        " DERIVED_GENERATORS=",Length(dpcgs),
        " DERIVED_COMMUTATOR_CONSTRAINT_RANK=",Length(derivedrows),"\n");
  if Length(derivedrows)=0 then zeroobstruction:=true; fi;
fi;

passing := [];
if not zeroobstruction then
  for idx in [1..2^dim-1] do
    coeff := CoefficientsMultiadic(List([1..dim],j->2),idx) * One(GF(2));
    derivedpass := not requirederived;
    if requirederived then
      for row in derivedrows do
        if not IsZero(coeff*row) then
          derivedpass := true;
          break;
        fi;
      od;
    fi;
    if PassesRowSpaces(coeff,rowspaces) and derivedpass then
      Add(passing,[idx,coeff]);
      if stopafterfirst then break; fi;
    fi;
  od;
fi;

Print("NONDEGENERACY_ROW_SPACES=",Length(rowspaces),
      " PASSING_CLASSES_RECORDED=",Length(passing),"\n");

if Length(passing)>0 then
  idx := passing[1][1];
  coeff := passing[1][2];
  classv := Zero(classspace);
  for j in [1..dim] do classv := classv + coeff[j]*classbasis[j]; od;
  cocycle := PreImagesRepresentative(coh.cohom,classv);
  extgrp := ExtensionSQ(coh.collector,basegrp,modu,cocycle);
  ker := ModuleOfExtension(extgrp);
  z := GeneratorsOfGroup(ker)[1];
  caminaok := Size(Centre(extgrp))=2;
  if caminaok then
    for cc in ConjugacyClasses(extgrp) do
      x := Representative(cc);
      if not x in ker and not IsConjugate(extgrp,x,x*z) then
        caminaok := false;
        break;
      fi;
    od;
  fi;
  secondder := DerivedSubgroup(DerivedSubgroup(extgrp));
  Print("FIRST_PASS_INDEX=",idx,
        " COEFFICIENTS=",List(coeff,IntFFE),
        " EXTENSION_ORDER=",Size(extgrp),
        " KERNEL_ORDER=",Size(ker),
        " CENTER_ORDER=",Size(Centre(extgrp)),
        " CENTRAL_CAMINA=",caminaok,
        " SECOND_DERIVED_ORDER=",Size(secondder),
        " SECOND_DERIVED_IS_KERNEL=",secondder=ker,
        " QUOTIENT_ID=",IdGroup(FactorGroup(extgrp,ker)),
        " EXACT_SMP=",HasSMPExactLocal(extgrp),"\n");
fi;
# No QUIT here: callers may read this file repeatedly in one GAP process.
