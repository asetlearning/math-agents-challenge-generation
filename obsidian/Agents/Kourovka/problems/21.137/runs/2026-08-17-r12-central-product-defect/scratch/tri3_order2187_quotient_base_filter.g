# Exact quotient-base filter for hypothetical TRI3 seeds of order 3^8.
# Coverage: every SmallGroup(3^7,i) in the rooted official SmallGrp layer.
# It does NOT test noncommuting cube pairs and does NOT enumerate extensions.

ORDER := 3^7;
EXPECTED_GROUPS := 9310;

loaded := LoadPackage("smallgrp");
Print("TRI3_QUOTIENT_BASE_BEGIN gap_version=", GAPInfo.Version,
      " smallgrp_loaded=", loaded, "\n");

if not SmallGroupsAvailable(ORDER) then
  Print("STATUS=BLOCKER reason=SmallGroups_library_order_2187_not_installed\n");
else
  nr := NumberSmallGroups(ORDER);
  Print("library_order=", ORDER, " group_count=", nr, "\n");

  if nr <> EXPECTED_GROUPS then
    Print("STATUS=BLOCKER reason=unexpected_order_2187_group_count expected=",
          EXPECTED_GROUPS, " observed=", nr, "\n");
  else
    countExp9 := 0;
    countClass56 := 0;
    countNontrivialCubeSet := 0;
    countCubeSubgroup := 0;

    for i in [1..nr] do
      Q := SmallGroup(ORDER, i);
      if Exponent(Q) = 9 then
        countExp9 := countExp9 + 1;
        cls := NilpotencyClassOfGroup(Q);
        if cls = 5 or cls = 6 then
          countClass56 := countClass56 + 1;
          els := Elements(Q);
          cubes := Set(List(els, x -> x^3));
          if Length(cubes) > 1 then
            countNontrivialCubeSet := countNontrivialCubeSet + 1;
            cubeGroup := Subgroup(Q, cubes);
            if Size(cubeGroup) = Length(cubes) then
              countCubeSubgroup := countCubeSubgroup + 1;
              Print("BASE_HIT id=", i,
                    " class=", cls,
                    " cube_subgroup_size=", Length(cubes), "\n");
            fi;
          fi;
        fi;
      fi;

      if i mod 500 = 0 then
        Print("PROGRESS i=", i,
              " exp9=", countExp9,
              " class56=", countClass56,
              " nontrivial_cube=", countNontrivialCubeSet,
              " cube_subgroup=", countCubeSubgroup, "\n");
      fi;
    od;

    Print("COMPLETE_BASE_FILTER=yes groups=", nr,
          " exp9=", countExp9,
          " class56=", countClass56,
          " nontrivial_cube=", countNontrivialCubeSet,
          " cube_subgroup=", countCubeSubgroup, "\n");
    Print("STATUS=QUOTIENT_BASE_FILTER_COMPLETE\n");
  fi;
fi;
