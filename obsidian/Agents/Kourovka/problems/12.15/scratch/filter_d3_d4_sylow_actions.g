# Coarse, monotone automorphism-action obstruction for the DeMeyer-permitted
# K=G' shapes at d=3 or d=4.  Set dtarget before Read().  Any actual
# conjugation image is a 2-subgroup of Aut(K), hence is contained in a Sylow
# 2-subgroup.  Therefore central-Camina fusion x~xz and rational power fusion
# must already hold under a Sylow 2-subgroup of Aut(K).

PassesCentralCaminaSylow := function(K, S, z)
  local x;
  for x in Elements(K) do
    if x <> One(K) and x <> z and not x*z in Orbit(S, x) then
      return false;
    fi;
  od;
  return true;
end;

PassesRationalSylow := function(K, S)
  local x, ox;
  for x in Elements(K) do
    ox := Order(x);
    if not x^-1 in Orbit(S, x) then
      return false;
    fi;
    if ox >= 8 and not x^3 in Orbit(S, x) then
      return false;
    fi;
  od;
  return true;
end;

if dtarget = 4 then
  ord := 32;
  shapes := [[1,2],[2,0]];
elif dtarget = 3 then
  ord := 64;
  shapes := [[1,3],[2,1]];
else
  Error("dtarget must be 3 or 4");
fi;

Print("GAP_VERSION=", GAPInfo.Version,
      " SYLOW_ACTION_SCREEN_D=", dtarget, " ORDER_K=", ord, "\n");
shape_count := 0;
exponent_count := 0;
central_count := 0;
rational_count := 0;
survivors := [];
for id in [1..NumberSmallGroups(ord)] do
  K := SmallGroup(ord, id);
  DK := DerivedSubgroup(K);
  ZK := Centre(K);
  if Size(DK) = 2 then
    qinv := AbelianInvariants(FactorGroup(K, ZK));
    match := false;
    for pair in shapes do
      r := pair[1];
      b := pair[2];
      if Size(ZK) = 2^(b+1) and Length(qinv) = 2*r and
         ForAll(qinv, n -> n = 2) then
        match := true;
      fi;
    od;
    if match then
      shape_count := shape_count + 1;
      if Exponent(K) <= 16 then
        exponent_count := exponent_count + 1;
        z := First(Elements(DK), x -> x <> One(K));
        AK := AutomorphismGroup(K);
        S := SylowSubgroup(AK, 2);
        centralpass := PassesCentralCaminaSylow(K, S, z);
        rationalpass := PassesRationalSylow(K, S);
        if centralpass then central_count := central_count + 1; fi;
        if centralpass and rationalpass then
          rational_count := rational_count + 1;
          Add(survivors, id);
        fi;
        Print("K_ID=", id,
              " K_DESC=", StructureDescription(K),
              " AUT_ORDER=", Size(AK),
              " SYLOW2_ORDER=", Size(S),
              " CENTRAL_CAMINA_SYLOW_PASS=", centralpass,
              " RATIONAL_SYLOW_PASS=", rationalpass, "\n");
      else
        Print("K_ID=", id,
              " K_DESC=", StructureDescription(K),
              " REJECT_DERIVED_EXPONENT=", Exponent(K), "\n");
      fi;
    fi;
  fi;
od;
Print("D=", dtarget,
      " SHAPE_COUNT=", shape_count,
      " EXPONENT_PASS=", exponent_count,
      " CENTRAL_CAMINA_PASS=", central_count,
      " CENTRAL_AND_RATIONAL_PASS=", rational_count,
      " SURVIVOR_IDS=", survivors, "\n");
QUIT;
