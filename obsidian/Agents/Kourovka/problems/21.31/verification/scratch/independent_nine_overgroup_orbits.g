T := GL(3,2);
coverT := SchurCover(T);
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
Print("T_ID=", IdGroup(T), " T_PERFECT=", IsPerfectGroup(T),
      " T_AUT_SIZE=", Size(AutomorphismGroup(T)),
      " MULTIPLIER=", AbelianInvariantsMultiplier(T), "\n");
Print("COVER_SIZE=", Size(coverT), " COVER_DESC=", StructureDescription(coverT),
      " COVER_CENTER=", StructureDescription(Centre(coverT)), "\n");

total := 0;
for kid in [1..5] do
  K := SmallGroup(12,kid);
  centerK := Centre(K);
  autK := AutomorphismGroup(K);
  z2 := Filtered(Elements(centerK), x -> x^2 = One(K));
  z2orbits := Orbits(autK,z2);
  orbitOrders := List(z2orbits, o -> Set(List(o,Order)));
  orbitSizes := List(z2orbits,Length);
  splitG := DirectProduct(K,T);
  Print("K_ID=", IdGroup(K), " K_DESC=", StructureDescription(K),
        " Z_ID=", IdGroup(centerK), " Z_DESC=", StructureDescription(centerK),
        " Z2_SIZE=", Length(z2), " ORBIT_COUNT=", Length(z2orbits),
        " ORBIT_SIZES=", orbitSizes, " ORBIT_ELEMENT_ORDERS=", orbitOrders,
        " SPLIT_ORDER=", Size(splitG), " SPLIT_RADICAL_ID=", IdGroup(RadicalGroup(splitG)),
        "\n");
  total := total + Length(z2orbits);
od;
Print("TOTAL_PAIR_ISOMORPHISM_ORBITS=", total, "\n");
Print("RUN_COMPLETE=true\n");
QUIT;
