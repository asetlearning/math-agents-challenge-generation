RunDiagnostic := function()
  local s, a, fusions, f, cs, ca, invariant, i, restricted, decomp;

  s := CharacterTable("A6");
  a := CharacterTable("A6.2^2");
  fusions := PossibleClassFusions(s, a);
  f := fusions[1];
  cs := Irr(s);
  ca := Irr(a);

  invariant := Filtered([1 .. Length(cs)], i ->
    ForAll([1 .. Length(f)], j ->
      ForAll([1 .. Length(f)], k ->
        f[j] <> f[k] or cs[i][j] = cs[i][k])));

  Print("gap_version=", GAPInfo.Version, "\n");
  Print("orders=", Size(s), ",", Size(a), "\n");
  Print("fusion_count=", Length(fusions), " fusion=", f, "\n");
  Print("invariant_rows=", invariant,
        " invariant_degrees=", List(invariant, i -> cs[i][1]), "\n");

  for i in [1 .. Length(ca)] do
    restricted := ClassFunction(s, List(f, j -> ca[i][j]));
    decomp := List(cs, y -> ScalarProduct(s, y, restricted));
    if ForAny(invariant, j -> decomp[j] <> 0) then
      Print("aut_row=", i, " degree=", ca[i][1],
            " restriction=", decomp, "\n");
    fi;
  od;
end;

RunDiagnostic();

QUIT;
