DirectSMPValidation := function(G)
  local seen,cc,x,N;
  seen:=[];
  for cc in ConjugacyClasses(G) do
    x:=Representative(cc);
    N:=NormalClosure(G,Subgroup(G,[x]));
    if N in seen then return false; fi;
    Add(seen,N);
  od;
  return true;
end;

CharacterSMPValidation := function(G)
  local irr,seen,sig,i,j;
  irr:=Irr(G); seen:=[];
  for i in [1..NrConjugacyClasses(G)] do
    sig:=[];
    for j in [1..Length(irr)] do Add(sig,irr[j][i]=irr[j][1]); od;
    if sig in seen then return false; fi;
    Add(seen,sig);
  od;
  return true;
end;

for pairval in [[8,3],[128,134],[128,928],[256,53342],[256,56083]] do
  valgrp:=SmallGroup(pairval[1],pairval[2]);
  Print("ID=",pairval,
        " DIRECT=",DirectSMPValidation(valgrp),
        " CHARACTER_SIGNATURE=",CharacterSMPValidation(valgrp),"\n");
od;
QUIT;
