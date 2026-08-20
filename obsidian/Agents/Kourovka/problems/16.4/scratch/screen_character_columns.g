# Exact class-product screen using GMT Lemma 2.2 before structure constants.
# Usage: gap -q -c 'name:="S8(3)"; Read(".../screen_character_columns.g");'

if not IsBound(name) or name = "" then Error("bind the global name first"); fi;
tbl := CharacterTable(name);
if tbl = fail then Error("character table unavailable: ",name); fi;
irr := Irr(tbl);
n := NrConjugacyClasses(tbl);
sizes := SizesConjugacyClasses(tbl);
hits := [];
survivors := [];
tested := 0;
columnRejected := 0;
coeffCalls := 0;

Print("GAP version: ",GAPInfo.Version,"\n");
Print("CTblLib version: ",InstalledPackageVersion("ctbllib"),"\n");
Print("table: ",name,"; classes: ",n,
      "; ordered nonidentity pairs: ",(n-1)^2,"\n");

for i in [2..n] do
  for j in [2..n] do
    tested := tested + 1;
    # In a nonabelian simple group, the checked stabilizer lemma strengthens
    # the size inequalities to strict ones.
    candidates := Filtered([1..n], k ->
      sizes[k] > Maximum(sizes[i],sizes[j]) and
      (sizes[i]*sizes[j]) mod sizes[k] = 0 and
      sizes[i]*sizes[j] >= 2*sizes[k]);
    # GMT Lemma 2.2: chi(i)chi(j)=chi(1)chi(k) for every irreducible chi.
    compatible := Filtered(candidates, k ->
      ForAll(irr, chi -> chi[i]*chi[j] = chi[1]*chi[k]));
    if Length(compatible) = 0 then
      columnRejected := columnRejected + 1;
      continue;
    fi;
    Add(survivors,[i,j,compatible]);

    # Resolve every column-compatible pair by exact support, early-exiting at 2.
    support := [];
    for k in [1..n] do
      coeffCalls := coeffCalls + 1;
      if ClassMultiplicationCoefficient(tbl,i,j,k) <> 0 then
        Add(support,k);
        if Length(support)=2 then break; fi;
      fi;
    od;
    if Length(support)=1 then Add(hits,[i,j,support[1]]); fi;
  od;
  Print("completed row ",i,"/",n,"; pairs=",tested,
        "; columnRejected=",columnRejected,
        "; compatiblePairs=",Length(survivors),
        "; coefficientCalls=",coeffCalls,"; hits=",Length(hits),"\n");
od;

Print("COLUMN_COMPATIBLE_PAIRS=",survivors,"\n");
Print("FINAL table=",name," tested=",tested,
      " columnRejected=",columnRejected,
      " compatiblePairs=",Length(survivors),
      " coeffCalls=",coeffCalls,
      " singleClassProducts=",hits,"\n");
QUIT;
