# Classify the possible subgroup K=G' in the d=5, |G|=512 case.
# DeMeyer forces |K|=16, |K'|=2, |Z(K)|=4, and K/Z(K)=C2^2.

Print("GAP_VERSION=", GAPInfo.Version, " ORDER=16\n");
for id in [1..NumberSmallGroups(16)] do
  K := SmallGroup(16, id);
  DK := DerivedSubgroup(K);
  ZK := Centre(K);
  if Size(DK) = 2 and Size(ZK) = 4 and
     AbelianInvariants(FactorGroup(K, ZK)) = [2, 2] then
    AK := AutomorphismGroup(K);
    Print("ID=", id,
          " DESC=", StructureDescription(K),
          " EXPONENT=", Exponent(K),
          " CENTER=", AbelianInvariants(ZK),
          " ABELIANIZATION=", AbelianInvariants(FactorGroup(K, DK)),
          " AUT_ORDER=", Size(AK),
          " AUT_DESC=", StructureDescription(AK), "\n");
  fi;
od;
QUIT;
