# Exhaustive SmallGroups classification of possible K=G' shapes imposed by
# DeMeyer's theorem for a hypothetical order-512 minimum counterexample.

Print("GAP_VERSION=", GAPInfo.Version, " D3_D4_DERIVED_SHAPES\n");
for spec in [[4, 32, [[1,2],[2,0]]], [3, 64, [[1,3],[2,1]]]] do
  d := spec[1];
  ord := spec[2];
  count := 0;
  ids := [];
  for id in [1..NumberSmallGroups(ord)] do
    K := SmallGroup(ord, id);
    DK := DerivedSubgroup(K);
    ZK := Centre(K);
    if Size(DK) = 2 then
      qinv := AbelianInvariants(FactorGroup(K, ZK));
      for pair in spec[3] do
        r := pair[1];
        b := pair[2];
        if Size(ZK) = 2^(b+1) and Length(qinv) = 2*r and
           ForAll(qinv, n -> n = 2) then
          count := count + 1;
          Add(ids, id);
          Print("D=", d,
                " R=", r,
                " B=", b,
                " K_ID=", id,
                " K_DESC=", StructureDescription(K),
                " K_EXPONENT=", Exponent(K),
                " CENTER_INVARIANTS=", AbelianInvariants(ZK),
                " K_AB_INVARIANTS=",
                    AbelianInvariants(FactorGroup(K, DK)), "\n");
        fi;
      od;
    fi;
  od;
  Print("D=", d, " TOTAL_SHAPE_MATCHES=", count,
        " IDS=", ids, "\n");
od;
QUIT;
