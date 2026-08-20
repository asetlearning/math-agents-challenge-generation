for ord in [81,243,729] do
  Print("ORDER ", ord, " groups=", NumberSmallGroups(ord), "\n");
  for id in [1..NumberSmallGroups(ord)] do
    G := SmallGroup(ord,id);
    if Exponent(G)=9 then
      els := Elements(G);
      cubes := Set(els, g -> g^3);
      bad := fail;
      for a in cubes do
        for b in cubes do
          if a*b <> b*a then
            bad := [a,b];
            break;
          fi;
        od;
        if bad <> fail then break; fi;
      od;
      if bad <> fail then
        H := Subgroup(G,cubes);
        Print("HIT id=",id,
              " cube_values=",Length(cubes),
              " cube_generated=",Size(H),
              " cube_generated_exp=",Exponent(H),
              " closure=",Length(cubes)=Size(H),
              " class=",NilpotencyClassOfGroup(G),"\n");
        Print("a=",bad[1]," b=",bad[2]," comm=",Comm(bad[1],bad[2]),"\n");
        QUIT_GAP(0);
      fi;
    fi;
  od;
od;
Print("NO_HIT\n");
QUIT_GAP(0);
