# Necessary action-level screen for d=5 in a hypothetical order-512
# minimal counterexample.  K=G' is one of the order-16 groups selected by
# classify_derived_order16.g.  The conjugation image P in Aut(K) is a
# 2-subgroup containing Inn(K), with P/Inn(K) elementary abelian.

HasInjectiveOrbitClosureMap := function(K, P)
  local orbits, closures, orb, N;
  orbits := OrbitsDomain(P, Elements(K));
  closures := [];
  for orb in orbits do
    N := Subgroup(K, orb);
    if N in closures then
      return false;
    fi;
    Add(closures, N);
  od;
  return true;
end;

HasCentralCaminaOnK := function(K, P, z)
  local x;
  for x in Elements(K) do
    if x <> One(K) and x <> z and not x*z in Orbit(P, x) then
      return false;
    fi;
  od;
  return true;
end;

Print("GAP_VERSION=", GAPInfo.Version, " D5_ACTION_SCREEN\n");
for id in [1..NumberSmallGroups(16)] do
  K := SmallGroup(16, id);
  DK := DerivedSubgroup(K);
  ZK := Centre(K);
  if Size(DK) = 2 and Size(ZK) = 4 and
     AbelianInvariants(FactorGroup(K, ZK)) = [2, 2] then
    z := First(Elements(DK), x -> x <> One(K));
    A := AutomorphismGroup(K);
    I := InnerAutomorphismsAutomorphismGroup(A);
    candidates := 0;
    caminapass := 0;
    smppass := 0;
    survivors := [];
    for cc in ConjugacyClassesSubgroups(A) do
      P := Representative(cc);
      if IsSubgroup(P, I) and Set(FactorsInt(Size(P))) = [2] and
         IsElementaryAbelian(FactorGroup(P, I)) then
        candidates := candidates + 1;
        if HasCentralCaminaOnK(K, P, z) then
          caminapass := caminapass + 1;
          if HasInjectiveOrbitClosureMap(K, P) then
            smppass := smppass + 1;
            Add(survivors, [Size(P), StructureDescription(P),
                            Size(FactorGroup(P, I))]);
          fi;
        fi;
      fi;
    od;
    Print("K_ID=", id,
          " K_DESC=", StructureDescription(K),
          " ACTION_CANDIDATES=", candidates,
          " CENTRAL_CAMINA_PASS=", caminapass,
          " ORBIT_CLOSURE_PASS=", smppass,
          " SURVIVORS_P_ORDER_DESC_OUTER_ORDER=", survivors, "\n");
  fi;
od;
QUIT;
