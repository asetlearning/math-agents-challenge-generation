# GAP 4.12.1. Deterministic exhaustive scan of one SmallGroups order.
# Set `n` before reading this file; defaults to 7.
if not IsBound(n) then n := 7; fi;
ord := 2^n;

HasSMP := function(G)
  local reps, closures, i, j;
  reps := List(ConjugacyClasses(G), Representative);
  closures := List(reps, x -> NormalClosure(G, Subgroup(G, [x])));
  for i in [1..Length(reps)] do
    for j in [i+1..Length(reps)] do
      if closures[i] = closures[j] then
        return false;
      fi;
    od;
  od;
  return true;
end;

Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("ORDER=", ord, " NUMBER_SMALL_GROUPS=", NumberSmallGroups(ord), "\n");
nonmeta := 0;
tested := 0;
passing := [];
for id in [1..NumberSmallGroups(ord)] do
  G := SmallGroup(ord, id);
  if not IsAbelian(DerivedSubgroup(G)) then
    nonmeta := nonmeta + 1;
    tested := tested + 1;
    if HasSMP(G) then
      Add(passing, id);
      Print("CANDIDATE=SmallGroup(", ord, ",", id, ")\n");
    fi;
  fi;
od;
Print("NONMETABELIAN=", nonmeta, " TESTED_SMP=", tested,
      " CANDIDATE_IDS=", passing, "\n");
QUIT;
