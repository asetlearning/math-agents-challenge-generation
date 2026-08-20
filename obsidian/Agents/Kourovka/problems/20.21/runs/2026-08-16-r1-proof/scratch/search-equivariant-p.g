# Targeted search for the sufficient equivariant 2-group reduction in
# Kourovka 20.21. Coverage is exactly SmallGroups of orders 16, 32, 64.
# A GAP run is forbidden until Lead grants a current heavy-compute lease.

Print("GAP_VERSION ", GAPInfo.Version, "\n");
Print("COVERAGE orders=[16,32,64]\n");
Print("CRITERION quotient(P/K)=C4; quotient(P/L)=V4; K~=L; ",
      "sigma order 3 stabilizes K,L; sigma is identity mod K and nonidentity mod L\n");

orders := [16, 32, 64];
totalGroups := 0;
filteredPairs := 0;
autGroupsBuilt := 0;
witnesses := 0;
started := Runtime();

for ord in orders do
  number := NrSmallGroups(ord);
  Print("ORDER_START ", ord, " groups=", number, "\n");
  for idx in [1..number] do
    totalGroups := totalGroups + 1;
    P := SmallGroup(ord, idx);
    normals := NormalSubgroups(P);
    indexFour := Filtered(normals, N -> Index(P, N) = 4);
    c4Kernels := Filtered(indexFour,
      N -> IdGroup(FactorGroup(P, N)) = [4, 1]);
    v4Kernels := Filtered(indexFour,
      N -> IdGroup(FactorGroup(P, N)) = [4, 2]);

    if Length(c4Kernels) > 0 and Length(v4Kernels) > 0 then
      for K in c4Kernels do
        for L in v4Kernels do
          if IdGroup(K) = IdGroup(L) then
            filteredPairs := filteredPairs + 1;
            A := AutomorphismGroup(P);
            autGroupsBuilt := autGroupsBuilt + 1;
            subgroupImageAction := function(N, a)
              return Image(a, N);
            end;
            pairStabilizer := Stabilizer(
              Stabilizer(A, K, subgroupImageAction),
              L, subgroupImageAction);
            if Size(pairStabilizer) mod 3 = 0 then
              sylowThree := SylowSubgroup(pairStabilizer, 3);
              for sigma in Elements(sylowThree) do
                if Order(sigma) = 3
                   and ForAll(GeneratorsOfGroup(P),
                     x -> Image(sigma, x) * x^-1 in K)
                   and ForAny(GeneratorsOfGroup(P),
                     x -> not (Image(sigma, x) * x^-1 in L)) then
                  witnesses := witnesses + 1;
                  Print("WITNESS P=SmallGroup(", ord, ",", idx, ")",
                        " K_id=", IdGroup(K),
                        " L_id=", IdGroup(L),
                        " K_pos=", Position(normals, K),
                        " L_pos=", Position(normals, L),
                        " aut_size=", Size(A),
                        " pair_stabilizer_size=", Size(pairStabilizer),
                        " sigma=", sigma, "\n");
                  break;
                fi;
              od;
            fi;
          fi;
        od;
      od;
    fi;
  od;
  Print("ORDER_DONE ", ord,
        " cumulative_groups=", totalGroups,
        " cumulative_filtered_pairs=", filteredPairs,
        " cumulative_aut_builds=", autGroupsBuilt,
        " cumulative_witnesses=", witnesses,
        " runtime_ms=", Runtime() - started, "\n");
od;

Print("FINAL groups=", totalGroups,
      " filtered_pairs=", filteredPairs,
      " aut_builds=", autGroupsBuilt,
      " witnesses=", witnesses,
      " runtime_ms=", Runtime() - started, "\n");
QUIT;
