if LoadPackage("grape") <> true then
  Error("GRAPE 4.9.0 is required");
fi;

Read("Agents/Kourovka/problems/21.53/runs/2026-08-17-r3-psl211-two-colour-separation/scratch/matrix_data.g");
M := PSL211ProductOrderMatrix;
n := Length(M);
if n <> 55 or ForAny(M, row -> Length(row) <> n) then
  Error("expected a 55 by 55 matrix");
fi;
if ForAny([1..n], i -> M[i][i] <> 1) then
  Error("diagonal check failed");
fi;
if ForAny([1..n], i -> ForAny([1..n], j -> M[i][j] <> M[j][i])) then
  Error("symmetry check failed");
fi;

colours := Set(Concatenation(List([1..n-1], i -> M[i]{[i+1..n]})));
if colours <> [2,3,5,6] then
  Error("unexpected colour set");
fi;

MakeColourGraph := function(c)
  return Graph(
    Group(()), [1..n], OnPoints,
    function(x,y) return x <> y and M[x][y] = c; end,
    true
  );
end;

PreservesColour := function(tau,c)
  local i,j;
  for i in [1..n-1] do
    for j in [i+1..n] do
      if M[i][j] = c and M[i^tau][j^tau] <> c then
        return false;
      fi;
    od;
  od;
  return true;
end;

g2 := MakeColourGraph(2);
g3 := MakeColourGraph(3);
g5 := MakeColourGraph(5);
g6 := MakeColourGraph(6);

a2 := AutomorphismGroup(g2);
a3 := AutomorphismGroup(g3);
a5 := AutomorphismGroup(g5);
a6 := AutomorphismGroup(g6);
two := Intersection(a2,a3);
full := Intersection(Intersection(two,a5),a6);

if not IsSubgroup(two,full) then
  Error("full-colour group is not contained in the two-colour group");
fi;
if ForAny(GeneratorsOfGroup(two), tau ->
    not PreservesColour(tau,2) or not PreservesColour(tau,3)) then
  Error("two-colour generator exhaustiveness check failed");
fi;
if ForAny(GeneratorsOfGroup(full), tau ->
    ForAny(colours, c -> not PreservesColour(tau,c))) then
  Error("full-colour generator exhaustiveness check failed");
fi;

Print("PSL211_AUT_COMPARISON_OK\n");
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("GRAPE_VERSION=", InstalledPackageVersion("grape"), "\n");
Print("VERTICES=", n, "\n");
Print("COLOURS=", colours, "\n");
Print("AUT2_ORDER=", Size(a2), "\n");
Print("AUT3_ORDER=", Size(a3), "\n");
Print("AUT5_ORDER=", Size(a5), "\n");
Print("AUT6_ORDER=", Size(a6), "\n");
Print("TWO_COLOUR_ORDER=", Size(two), "\n");
Print("FULL_COLOUR_ORDER=", Size(full), "\n");
Print("FULL_SUBGROUP_TWO=", IsSubgroup(two,full), "\n");
Print("EQUALITY=", two = full, "\n");

if two <> full then
  tau := First(GeneratorsOfGroup(two), x -> not x in full);
  if tau = fail then
    Error("strict containment but no separating generator");
  fi;
  if not PreservesColour(tau,2) or not PreservesColour(tau,3) then
    Error("separator fails a required colour");
  fi;
  images := List([1..n], i -> i^tau);
  changed := fail;
  for i in [1..n-1] do
    for j in [i+1..n] do
      if M[i][j] <> M[i^tau][j^tau] then
        changed := [i,j,M[i][j],i^tau,j^tau,M[i^tau][j^tau]];
        break;
      fi;
    od;
    if changed <> fail then break; fi;
  od;
  if changed = fail then
    Error("separator has no changed colour edge");
  fi;
  Print("SEPARATOR_CYCLES=", tau, "\n");
  Print("SEPARATOR_IMAGES=", images, "\n");
  Print("SEPARATOR_PRESERVES_2=", PreservesColour(tau,2), "\n");
  Print("SEPARATOR_PRESERVES_3=", PreservesColour(tau,3), "\n");
  Print("CHANGED_EDGE=[i,j,old_colour,image_i,image_j,new_colour]=", changed, "\n");
fi;

QUIT;
