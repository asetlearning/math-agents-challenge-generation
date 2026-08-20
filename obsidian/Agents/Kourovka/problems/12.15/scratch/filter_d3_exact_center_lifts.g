# Exact action-level test for the d=3, r=1, b=3 branch.  Here the required
# center action has order 8, so all of A=G/K=C2^3 acts faithfully on Z(K).
# For each center-covering C2^3 subgroup R0 of the induced center-action
# group R, test whether R0 lifts to a complement modulo Inn(K), then apply
# the restricted SMP orbit/normal-closure test on K.

CenterCoverOnPermutationDomain := function(Q, welts, z)
  local i, target;
  for i in [1..Length(welts)] do
    if welts[i] <> One(welts[i]) and welts[i] <> z then
      target := Position(welts, welts[i]*z);
      if not target in Orbit(Q, i) then
        return false;
      fi;
    fi;
  od;
  return true;
end;

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

K := SmallGroup(64, idtarget);
DK := DerivedSubgroup(K);
ZK := Centre(K);
z := First(Elements(DK), x -> x <> One(K));
welts := Elements(ZK);
AK := AutomorphismGroup(K);
I := InnerAutomorphismsAutomorphismGroup(AK);
ahom := ActionHomomorphism(AK, welts, OnPoints);
R := Image(ahom);
J := Kernel(ahom);
center_subgroups := 0;
lift_classes := 0;
smp_lift_classes := 0;
survivors := [];
Print("GAP_VERSION=", GAPInfo.Version,
      " D3_EXACT_CENTER_LIFTS K_ID=", idtarget,
      " K_DESC=", StructureDescription(K),
      " AUT_ORDER=", Size(AK),
      " INNER_ORDER=", Size(I),
      " CENTER_ACTION_ORDER=", Size(R), "\n");
for cc in ConjugacyClassesSubgroups(R) do
  R0 := Representative(cc);
  if Size(R0) = 8 and IsElementaryAbelian(R0) and
     CenterCoverOnPermutationDomain(R0, welts, z) then
    center_subgroups := center_subgroups + 1;
    T := PreImage(ahom, R0);
    nat := NaturalHomomorphismByNormalSubgroup(T, I);
    Tbar := Image(nat);
    Jbar := Image(nat, J);
    pciso := IsomorphismPcpGroup(Tbar);
    Tpc := Image(pciso);
    Jpc := Image(pciso, Jbar);
    comps := ComplementClassesRepresentatives(Tpc, Jpc);
    lift_classes := lift_classes + Length(comps);
    for Qpc in comps do
      Qbar := PreImage(pciso, Qpc);
      P := PreImage(nat, Qbar);
      if HasInjectiveOrbitClosureMap(K, P) then
        smp_lift_classes := smp_lift_classes + 1;
        Add(survivors, [Size(P), StructureDescription(P)]);
      fi;
    od;
  fi;
od;
Print("CENTER_C2_3_CLASSES=", center_subgroups,
      " LIFT_COMPLEMENT_CLASSES=", lift_classes,
      " RESTRICTED_SMP_LIFT_CLASSES=", smp_lift_classes,
      " SURVIVOR_P_TYPES=", Set(survivors), "\n");
QUIT;
