SizeScreen([ 1000, 40 ]);
Print("GAP_VERSION=", GAPInfo.Version, "\n");
orders := [ 9, 27, 81, 243, 729 ];
grandExp9 := 0;
grandClosed := 0;
grandBad := 0;
for n in orders do
  total := NrSmallGroups(n);
  exp9 := 0;
  closed := 0;
  bad := 0;
  nonabelianGeneratedPower := 0;
  nonclosedNonabelianGeneratedPower := 0;
  classCounts := [];
  for id in [1..total] do
    G := SmallGroup(n,id);
    if Exponent(G) = 9 then
      exp9 := exp9 + 1;
      vals := Set(Elements(G), x -> x^3);
      H := Group(vals);
      if not IsAbelian(H) then
        nonabelianGeneratedPower := nonabelianGeneratedPower + 1;
      fi;
      isClosed := Size(H) = Length(vals);
      if isClosed then
        closed := closed + 1;
        c := NilpotencyClassOfGroup(G);
        if not IsBound(classCounts[c]) then classCounts[c] := 0; fi;
        classCounts[c] := classCounts[c] + 1;
        if not IsAbelian(H) then
          bad := bad + 1;
          Print("COUNTEREXAMPLE_CANDIDATE order=", n, " id=", id,
                " class=", c, " |values|=", Length(vals),
                " |generated|=", Size(H), "\n");
        fi;
      elif not IsAbelian(H) and Exponent(H) = 3 then
        nonclosedNonabelianGeneratedPower :=
          nonclosedNonabelianGeneratedPower + 1;
      fi;
    fi;
  od;
  grandExp9 := grandExp9 + exp9;
  grandClosed := grandClosed + closed;
  grandBad := grandBad + bad;
  Print("ORDER=", n, " TOTAL=", total, " EXPONENT_9=", exp9,
        " POWER_SET_SUBGROUP=", closed, " NONABELIAN_POWER_SUBGROUP=", bad,
        " NONABELIAN_GENERATED_POWER=", nonabelianGeneratedPower,
        " NONCLOSED_NONABELIAN_GENERATED_POWER_EXP3=",
        nonclosedNonabelianGeneratedPower, " CLASS_COUNTS=", classCounts, "\n");
od;
Print("SUMMARY EXPONENT_9=", grandExp9, " POWER_SET_SUBGROUP=", grandClosed,
      " NONABELIAN_POWER_SUBGROUP=", grandBad, "\n");
QUIT;
