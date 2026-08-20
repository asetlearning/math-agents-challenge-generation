# Necessary center-action filter for a DeMeyer-permitted K=G'.  The actual
# outer action is an elementary abelian quotient of G/K of rank at most d.
# Its induced action on Z(K) is therefore elementary abelian of rank at most d
# and must fuse w with w*z for every w outside <z>.

CenterElementaryCover := function(K, d, z)
  local W, welts, AK, ahom, R, cc, Q, ok, i, target;
  W := Centre(K);
  welts := Elements(W);
  AK := AutomorphismGroup(K);
  ahom := ActionHomomorphism(AK, welts, OnPoints);
  R := Image(ahom);
  for cc in ConjugacyClassesSubgroups(R) do
    Q := Representative(cc);
    if IsElementaryAbelian(Q) and Size(Q) <= 2^d then
      ok := true;
      for i in [1..Length(welts)] do
        if welts[i] <> One(K) and welts[i] <> z then
          target := Position(welts, welts[i]*z);
          if not target in Orbit(Q, i) then
            ok := false;
            break;
          fi;
        fi;
      od;
      if ok then
        return [true, Size(R), Size(Q), StructureDescription(Q)];
      fi;
    fi;
  od;
  return [false, Size(R), 0, "none"];
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
      " CENTER_ELEMENTARY_ACTION_D=", dtarget, "\n");
shape_count := 0;
pass_count := 0;
survivors := [];
for id in [1..NumberSmallGroups(ord)] do
  K := SmallGroup(ord, id);
  DK := DerivedSubgroup(K);
  ZK := Centre(K);
  if Size(DK) = 2 and Exponent(K) <= 16 then
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
      z := First(Elements(DK), x -> x <> One(K));
      result := CenterElementaryCover(K, dtarget, z);
      if result[1] then
        pass_count := pass_count + 1;
        Add(survivors, id);
      fi;
      Print("K_ID=", id,
            " CENTER=", AbelianInvariants(ZK),
            " CENTER_ACTION_ORDER=", result[2],
            " PASS=", result[1],
            " WITNESS_ACTION_ORDER=", result[3],
            " WITNESS_ACTION_DESC=", result[4], "\n");
    fi;
  fi;
od;
Print("D=", dtarget,
      " EXPONENT_AND_SHAPE_COUNT=", shape_count,
      " CENTER_ELEMENTARY_ACTION_PASS=", pass_count,
      " SURVIVOR_IDS=", survivors, "\n");
QUIT;
