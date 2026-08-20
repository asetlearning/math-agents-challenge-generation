# Exact early-exit screen for a named CTblLib character table.
# Usage: gap -q -c 'name:="U5(3)"; Read(".../screen_early_exit.g");'
# A class product is not one class as soon as two nonzero structure constants occur.

if not IsBound(name) or name = "" then Error("bind the global name first"); fi;
tbl := CharacterTable(name);
if tbl = fail then Error("character table unavailable: ", name); fi;
n := NrConjugacyClasses(tbl);
sizes := SizesConjugacyClasses(tbl);
hits := [];
tested := 0;
coeffCalls := 0;

Print("GAP version: ", GAPInfo.Version, "\n");
Print("CTblLib version: ", InstalledPackageVersion("ctbllib"), "\n");
Print("table: ", name, "; classes: ", n,
      "; ordered nonidentity pairs: ", (n-1)^2, "\n");

for i in [2..n] do
  for j in [2..n] do
    tested := tested + 1;
    support := [];
    # Necessary in any finite group if support were singleton k:
    # |Ki|,|Kj| <= |Kk| and |Kk| divides |Ki||Kj|.
    candidates := Filtered([1..n], k ->
      sizes[k] >= Maximum(sizes[i],sizes[j]) and
      (sizes[i]*sizes[j]) mod sizes[k] = 0);
    # First inspect only possible singleton outputs. If none has nonzero
    # coefficient, singleton support is impossible without inspecting the rest.
    for k in candidates do
      coeffCalls := coeffCalls + 1;
      if ClassMultiplicationCoefficient(tbl,i,j,k) <> 0 then
        Add(support,k);
        if Length(support) = 2 then break; fi;
      fi;
    od;
    if Length(support) = 1 then
      # A sole nonzero candidate is a hit only if every noncandidate coefficient
      # vanishes. Search them, again stopping at the second support class.
      for k in Difference([1..n],candidates) do
        coeffCalls := coeffCalls + 1;
        if ClassMultiplicationCoefficient(tbl,i,j,k) <> 0 then
          Add(support,k);
          break;
        fi;
      od;
    fi;
    if Length(support) = 1 then
      Add(hits,[i,j,support[1]]);
    fi;
  od;
  Print("completed row ",i,"/",n,"; pairs=",tested,
        "; coefficient calls=",coeffCalls,"; hits=",Length(hits),"\n");
od;

Print("FINAL table=",name," tested=",tested," coeffCalls=",coeffCalls,
      " singleClassProducts=",hits,"\n");
QUIT;
