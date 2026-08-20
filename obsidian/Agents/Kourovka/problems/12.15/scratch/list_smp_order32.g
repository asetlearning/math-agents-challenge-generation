# Exact character-kernel catalogue of the order-32 SMP quotients forced by
# the normal order-8 isotropic-subgroup reduction.

HasSMPCharacter32 := function(G)
  local irr, seen, i, sig, j;
  irr := Irr(G); seen := [];
  for i in [1..NrConjugacyClasses(G)] do
    sig := [];
    for j in [1..Length(irr)] do
      Add(sig, irr[j][i] = irr[j][1]);
    od;
    if sig in seen then return false; fi;
    Add(seen,sig);
  od;
  return true;
end;

Print("GAP_VERSION=",GAPInfo.Version,"\n");
smp32ids := [];
for id in [1..NumberSmallGroups(32)] do
  G := SmallGroup(32,id);
  if HasSMPCharacter32(G) then
    Add(smp32ids,id);
    Print("SMP32_ID=",id,
          " STRUCTURE=",StructureDescription(G),
          " CLASS=",NilpotencyClassOfGroup(G),
          " ABINV=",AbelianInvariants(G/DerivedSubgroup(G)),
          " DERIVED_INV=",AbelianInvariants(DerivedSubgroup(G)),
          " CENTER_INV=",AbelianInvariants(Centre(G)),"\n");
  fi;
od;
Print("SMP32_IDS=",smp32ids,"\n");
QUIT;
