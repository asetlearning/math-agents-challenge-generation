# Exact SMP list for quotients by a normal Lagrangian of order 16.

HasSMPCharacter16 := function(G)
  local irr, seen, i, sig, j;
  irr := Irr(G); seen := [];
  for i in [1..NrConjugacyClasses(G)] do
    sig := [];
    for j in [1..Length(irr)] do Add(sig,irr[j][i]=irr[j][1]); od;
    if sig in seen then return false; fi;
    Add(seen,sig);
  od;
  return true;
end;

Print("GAP_VERSION=",GAPInfo.Version,"\n");
smp16ids := [];
for id in [1..NumberSmallGroups(16)] do
  G := SmallGroup(16,id);
  if HasSMPCharacter16(G) then
    Add(smp16ids,id);
    Print("SMP16_ID=",id,
          " STRUCTURE=",StructureDescription(G),
          " CLASS=",NilpotencyClassOfGroup(G),
          " ABINV=",AbelianInvariants(G/DerivedSubgroup(G)),
          " DERIVED_INV=",AbelianInvariants(DerivedSubgroup(G)),
          " CENTER_INV=",AbelianInvariants(Centre(G)),"\n");
  fi;
od;
Print("SMP16_IDS=",smp16ids,"\n");
QUIT;
