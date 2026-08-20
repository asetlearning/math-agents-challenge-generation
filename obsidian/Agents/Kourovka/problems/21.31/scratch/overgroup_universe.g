T := SmallGroup(168,42);;
S := SchurCover(T);;
centerS := Centre(S);;
s := First(Elements(centerS),x->Order(x)=2);;
Print("GAP_VERSION=",GAPInfo.Version," T_ID=",IdGroup(T),
      " COVER_SIZE=",Size(S)," COVER_DESC=",StructureDescription(S),"\n");
total := 0;;
for kid in [1..5] do
  K := SmallGroup(12,kid);;
  centerK := Centre(K);;
  autK := AutomorphismGroup(K);;
  torsion2 := Filtered(Elements(centerK),x->Order(x)<=2);;
  orbits := Orbits(autK,torsion2);;
  Print("K_ID=",IdGroup(K)," K_DESC=",StructureDescription(K),
        " CENTER_DESC=",StructureDescription(centerK),
        " Z2_SIZE=",Length(torsion2)," Z2_ORBITS=",Length(orbits),"\n");
  for orb in orbits do
    z := orb[1];;
    if Order(z)=1 then
      G := DirectProduct(K,T);;
      kind := "split";
    else
      product := DirectProduct(K,S);;
      embK := Embedding(product,1);;
      embS := Embedding(product,2);;
      diagonal := Subgroup(product,[Image(embK,z)*Image(embS,s)]);;
      G := FactorGroup(product,diagonal);;
      kind := "schur-pushout";
    fi;
    total := total+1;
    Print("  CLASS=",kind," Z_REP_ORDER=",Order(z),
          " Z_ORBIT_SIZE=",Length(orb)," G_SIZE=",Size(G),
          " EXPECTED_RADICAL_ID=",IdGroup(K),
          " EXPECTED_QUOTIENT_SIZE=168\n");
  od;
od;
Print("TOTAL_DISTINGUISHED_EXTENSION_ORBITS=",total," RUN_COMPLETE=true\n");
QUIT;
