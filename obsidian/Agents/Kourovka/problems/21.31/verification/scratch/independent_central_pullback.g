pairs := [ [2,2], [9,5], [17,1], [19,2], [27,3], [29,4], [38,5] ];
T := GL(3,2);
subgroupClasses := ConjugacyClassesSubgroups(T);
classes21 := Filtered(subgroupClasses, c -> Size(Representative(c)) = 21);
if Length(classes21) <> 1 then Error("expected one subgroup class of order 21"); fi;
P := Representative(classes21[1]);

Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
Print("T_ID=", IdGroup(T), " T_SIZE=", Size(T),
      " T_PERFECT=", IsPerfectGroup(T),
      " MULTIPLIER_INVARIANTS=", AbelianInvariantsMultiplier(T), "\n");
Print("ORDER21_SUBGROUP_CLASSES=", Length(classes21),
      " P_ID=", IdGroup(P), " P_DESC=", StructureDescription(P), "\n");

for pair in pairs do
  H := SmallGroup(252,pair[1]);
  candidates := Filtered(NormalSubgroups(H), K ->
    IdGroup(K) = [12,pair[2]] and IdGroup(FactorGroup(H,K)) = [21,1]);
  if Length(candidates) <> 1 then Error("unexpected K multiplicity"); fi;
  K := candidates[1];
  centerK := Centre(K);
  D := Centralizer(H,K);
  direct := DirectProduct(K,P);
  Print("PAIR=", [IdGroup(H),IdGroup(K)],
        " K_DESC=", StructureDescription(K),
        " Z_ID=", IdGroup(centerK), " Z_DESC=", StructureDescription(centerK),
        " D_SIZE=", Size(D), " D_ID=", IdGroup(D),
        " D_DESC=", StructureDescription(D),
        " K_INTER_D_SIZE=", Size(Intersection(K,D)),
        " K_INTER_D_EQUALS_Z=", Intersection(K,D)=centerK,
        " D_OVER_Z_ID=", IdGroup(FactorGroup(D,centerK)),
        " D_IS_Z_TIMES_P=", IdGroup(D)=IdGroup(DirectProduct(centerK,P)),
        " DIRECT_PRODUCT_PAIR_H_ID=", IdGroup(direct),
        " H_IS_K_TIMES_P=", IdGroup(H)=IdGroup(direct), "\n");
od;
Print("RUN_COMPLETE=true\n");
QUIT;
